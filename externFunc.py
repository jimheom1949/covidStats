# this file defines the functions that are needed to insert
# html code that show 2 bootstrap tables
def printHtmlHead(dateOfRawData,addedInfo):
    print('<!DOCTYPE html>')
    print('<html lang="en">')
    print('<head>')
    print('<meta charset="utf-8">')
    print('<meta name="viewport" content="width=device-width, initial-scale=1">')
    print('<title>Oregon Daily Covid statistics</title>')
    print('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" \
rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" \
crossorigin="anonymous">')
    includeExternalCss()
    print('</head>')
    print('<body style="margin:0% 1% 0 1%;padding:1%;background:  rgba(209, 164, 17,.2); height:98vh;">')
    print('<div class="container-fluid">')
    print('<div class="GeeksForGeeks" style="border-radius: 18px;">')
    print('<h5 style="padding: 20px;"> Oregon Daily Covid Infection Data for {}'.format(dateOfRawData) )
    print('</h5></div>')
    print('<div class="GeeksForGeeks" style="padding: 20px; border-radius: 15px; width: 50%; margin-top: 20px; font-size:1.1em;" >')
    print('{}'.format(addedInfo))    
    print('</div><br></div></div>')
    print('<div class="row g-3" style="width: 98%; margin: auto">')

def printTableEnd():
    print('</tbody></table></div>')

def printTableStart():
    print('<div class="col-md-6">')
    print('<table class="table table-striped table-sm T_borderStyle shadow2">')                
    print('<tbody class="table-warning">')
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

