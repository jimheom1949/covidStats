# this file defines the functions that are needed to insert
# html code that show 2 bootstrap tables
def printHtmlHead(dateOfRawData,addedInfo,width):
    print('<!DOCTYPE html>')
    print('<html lang="en">')
    print('<head>')
    print('<meta charset="utf-8">')
    print('<meta name="viewport" content="width=device-width, initial-scale=1">')
    print('<title>Oregon Daily Covid statistics</title>')
    print('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" \
rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" \
crossorigin="anonymous">')
    print('<link href="https://cdn.jsdelivr.net/gh/jimheom1949/covidStats/floater.css" rel="stylesheet" crossorigin="anonymous">')
    includeExternalCss()
    print('</head>')
    print('<body style="margin: 0 1%;padding:1%;background:  rgba(209, 164, 17, .05); height:98vh;">')
    print('<div class="container-fluid">')
    print('<div class="GeeksForGeeks" style="border-radius: 18px;">')
    print('<h5 style="padding: 20px;"> Oregon Daily Covid Infection Data for {}'.format(dateOfRawData) )
    print('</h5></div>')
    print('<div class="GeeksForGeeks" style="padding: 20px; border-radius: 15px; width:{}; margin-top: 20px; font-size:.95em;">'.format(width))
    print('{}'.format(addedInfo))    
    print('</div><br></div></div>')
    includeFloaters()
    print('<div class="row g-3" style="width: 98%; margin: auto">')

def printTableEnd():
    print('</tbody></table></div>')

def printTableStart():
    print('<div class="col-md-6">')
    print('<table class="table table-light table-striped table-sm T_borderStyle tableShadow">')                
    print('<tbody>')
    print('<tr><td>County:</td><td style="padding-right: 100px;">Infections</td></tr>')

def printDocumentEnd():
    print('</div>')
    print('</div>')
    print('</body>')
    print('</html>')

def includeExternalCss():
    file = open('mkCovid.css',mode='r')
    externalCss = file.read()
    file.close()
    print(externalCss)

def includeFloaters():
    print('<div class="wrapper">')
    print('    <div class="particle elem1  anim-delay1" ></div>')
    print('    <div class="particle elem2  anim-delay5" ></div>')
    print('    <div class="particle elem2  anim-delay6" ></div>')
    print('    <div class="particle elem3  anim-delay3" ></div>')
    print('    <div class="particle elem4  anim-delay8" ></div>')
    print('    <div class="particle elem5  anim-delay9" ></div>')
    print('    <div class="particle elem6  anim-delay2" ></div>')
    print('    <div class="particle elem7  anim-delay4" ></div>')
    print('    <div class="particle elem8  anim-delay3" ></div>')
    print('    <div class="particle elem9  anim-delay10"></div>')
    print('    <div class="particle elem11 anim-delay12"></div>')
    print('    <div class="particle elem12 anim-delay14"></div>')
    print('    <div class="particle elem13 anim-delay16"></div>')
    print('    <div class="particle elem14 anim-delay18"></div>')
    print('    <div class="particle elem15 anim-delay6" ></div>')
    print('    <div class="particle elem16 anim-delay9" ></div>')
    print('    <div class="particle elem17 anim-delay18"></div>')
    print('    <div class="particle elem17 anim-delay7" ></div>')
    print('    <div class="particle elem18 anim-delay11"></div>')
    print('    <div class="particle elem18 anim-delay6" ></div>')
    print('    <div class="particle elem19 anim-delay3" ></div>')
    print('</div>')

