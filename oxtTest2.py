import zipfile
import errno
import xml.etree.ElementTree as ET
import re

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

    childtags = []
    for child in root:
        childtags.append(child.tag)

    z = ''
    for element in childtags:
        version = re.findall(r'version', element)
        registration = re.findall(r'registration', element)
        identifier = re.findall(r'identifier', element)
        icon = re.findall(r'icon', element)
        display= re.findall(r'display-name', element)
        description = re.findall(r'extension-description', element)
        dependencies = re.findall(r'dependencies', element)
        publisher = re.findall(r'publisher', element)

    if version.count > 0:
        print ('Extension version information included.')
    else:
        print ('There is an Extension version information missing.')

    if registration.count > 0:
        print ('Information about license included.')
    else:
        print ('There is a link to the license information missing. \nPlease add this link and make sure that it'
               'points to the license file inside the Extension.')

    if identifier.count > 0:
        print ('The identifier xml-tag is included.')
    else:
        print ('There is the identifier xml-tag missing. ')

    if icon.count > 0:
        print ('The icon xml-tag is included.')
    else:
        print ('The icon xml-tag with a link to an icon for the Extension is missing. Please add the following xml-tag:\n'
               '<icon>\n<default xlink:href="[relative link to the extensionicon in file format *.png]" />\n'
               '</icon>')

    if display.count > 0:
        print ('The display name xml-tag is set.')
    else:
        print ('There is no display name xml-tag set and thus the extension will not'
               ' show a name in the Extension-Manager')

    if description.count > 0:
        print ('The description xml-tag is included in the description.xml file.')
    else:
        print ('Please add a description xml-tag to the description.xml file of your extension.')

    if dependencies.count > 0:
        print ('Information about program version included.')
    else:
        print ('There is no information about the (minimal / maximal program version included')

    if publisher.count > 0:
        print ('Publisher xml-tag included.')
    else:
        print ('The publisher xml-tag with the extension author is missing.')

    f.close
except (KeyError):
    print ('There is a file description.xml missing in the extension. Thus the extension is not valid!')