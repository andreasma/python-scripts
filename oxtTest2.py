import zipfile
import errno
import xml.etree.ElementTree as ET

extensionfile= raw_input('Please type in the name of the extension file you want to investigate: ')

zip=zipfile.ZipFile(extensionfile)

try:
    f=zip.open('description.xml')
    contents=f.read()
    tree = ET.parse(zip.open('description.xml'))
    root = tree.getroot()
    if 'http://openoffice.org/extensions/description/2006' in root.tag:
        print ('OpenOffice extension declaration included')
    elif 'http://libreoffice.org/extensions/description/2011' in root.tag:
        print ('LibreOffice extension declaration inclueded')
    else:
        ('There is a xml extension declarartion missing in the description.xml.')


    f.close
except (KeyError):
    print ('There is a file description.xml missing in the extension. Thus the extension is not valid!')