console.clear();
console.log("JIMMY here")

import { Vec2, Vec3, Vec4, Mat2, Mat3, Mat4, Quat } from 'https://cdn.skypack.dev/wtc-math';

import {
Camera,
Renderer,
Mesh,
Program,
Geometry,
Triangle,
FragmentShader,
RenderTarget,
GeometryAttribute,
Framebuffer,
Uniform, Texture,
ParticleSimulation } from 'https://cdn.skypack.dev/wtc-gl@1.0.0-beta.33';

const setup = function () {
  // Simulation dimensions
  const px = Math.min(window.devicePixelRatio, 2);
  const dimensions = [window.innerWidth, window.innerHeight];

  const t = new ParticleSimulation({
    rendererProps: {},
    textureSize: 128,
    simDimensions: 2,
    vertex: document.querySelector('#vertexShader_particle').innerText,
    fragment: document.querySelector('#fragmentShader_particle').innerText,
    uniforms: {
      'b_position': new Uniform({
        name: 'position',
        value: null,
        kind: 'texture' }),

      'b_velocity': new Uniform({
        name: 'velocity',
        value: null,
        kind: 'texture' }) },


    onBeforeRender: function (t, system) {

      this.uniforms['b_position'].value = positionBuffer.read.texture;

      // this.uniforms['s_data'] = new Uniform({ name: 'data', value: particleTexture, type: 'texture' });

      this.uniforms['u_resolution'].value = [positionBuffer.width, positionBuffer.height];
      // positionBuffer.read;
      positionBuffer.render(this.renderer, { scene: positionMesh });

      this.uniforms['u_resolution'].value = this.dimensions.array;
    } });


  t.program.depthTest = false;
  t.transparent = true;
  t.program.setBlendFunc(t.gl.SRC_ALPHA, t.gl.ONE_MINUS_SRC_ALPHA);

  window.addEventListener('keyup', e => {
    if (e.key === " ") {
      t.playing = !t.playing;
    }
  });

  const { gl, textureSize, particles, uniforms, renderer } = t;

  const dpr = renderer.dpr;

  // gl.clearColor(0.08, 0.1, 0.15, 0.);
  gl.clearColor(0.98, 0.99, 0.35, 1.);

  const positionData = new Float32Array(particles * 4).fill(0);
  const particleData = new Float32Array(particles * 4).fill(0);
  for (let i = 0; i < positionData.length; i += 4) {
    positionData[i] = window.innerWidth * .5 * dpr;
    positionData[i + 1] = Math.random() * 200 - 100 + window.innerHeight * .5 * dpr;
    positionData[i + 2] = Math.random() - .5;
    positionData[i + 3] = Math.random() - .5;

    particleData[i] = Math.random();
    particleData[i + 1] = 1. - Math.random() * 1.5;
    particleData[i + 2] = 0;
    particleData[i + 3] = 0;
  }

  const particleTexture = new Texture(gl, {
    data: particleData,
    width: textureSize,
    height: textureSize,
    minFilter: gl.NEAREST,
    magFilter: gl.NEAREST,
    generateMipmaps: false,
    type: gl.FLOAT,
    internalFormat: gl.RGBA16F });

  uniforms.s_data = new Uniform({ name: 'data', value: particleTexture, kind: 'texture' });
  const positionBuffer = new Framebuffer(gl, {
    name: 'position',
    width: textureSize,
    height: textureSize,
    dpr: 1,
    data: positionData,
    texdepth: Framebuffer.TEXTYPE_FLOAT,
    minFilter: gl.NEAREST });

  const defaultShaderV = `
  attribute vec3 position;
  attribute vec2 uv;
  varying vec2 v_uv;
  void main() {
  gl_Position = vec4(position, 1.0);
  v_uv = uv;
  }`;
  const geometry = new Triangle(gl);
  const positionProgram = new Program(gl, {
    vertex: defaultShaderV,
    fragment: document.getElementById('fragmentShader_position').innerText,
    uniforms: uniforms });

  const bufferResolution = new Uniform({
    name: 'resolution',
    value: [textureSize, textureSize],
    kind: "vec2" });

  positionProgram.uniforms.u_resolution = bufferResolution;
  uniforms.u_screen = new Uniform({
    name: 'screen',
    value: [window.innerWidth, window.innerHeight],
    kind: "vec2" });

  window.addEventListener('resize', e => {
    uniforms.u_screen.value = [window.innerWidth, window.innerHeight];
  });

  const positionMesh = new Mesh(gl, { geometry, program: positionProgram });

  // Set up mouse uniforms
  (function () {
    const tarmouse = new Vec4(0, 0, 0, 0);
    const curmouse = tarmouse.clone();
    let pointerdown = false;

    uniforms.u_mouse = new Uniform({
      name: 'mouse',
      value: tarmouse.array,
      kind: 'vec4' });

    document.body.addEventListener('pointermove', e => {
      tarmouse.x = e.x;
      tarmouse.y = window.innerHeight - e.y;
      if (pointerdown) {
      }
    });
    document.body.addEventListener('pointerdown', e => {
      pointerdown = true;
      if (e.button == 0) {
        curmouse.z = 1.;
      }
    });
    document.body.addEventListener('pointerup', e => {
      pointerdown = false;
      if (e.button == 0) {
        curmouse.z = 0.;
      }
    });
    let oldTime;
    const animouse = d => {
      const factor = d - oldTime;
      oldTime = d;
      const diff = tarmouse.xy.subtractNew(curmouse.xy);
      curmouse.xy = curmouse.xy.add(diff.scale(1. / factor * 2.));
      uniforms.u_mouse.value = curmouse.array;
      requestAnimationFrame(animouse);
    };
    requestAnimationFrame(animouse);
  })();
};

setup();