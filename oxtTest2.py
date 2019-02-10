import zipfile
import errno
import xml.etree.ElementTree as ET
import re
import sys

try:
    extensionfile = sys.argv[1]
    zip=zipfile.ZipFile(extensionfile)

    try:
        f=zip.open('description.xml')
        contents=f.read()
        tree = ET.parse(zip.open('description.xml'))
        root = tree.getroot()
        if 'http://openoffice.org/extensions/description/2006' in root.tag:
            print ('OpenOffice extension declaration included')
        elif 'http://libreoffice.org/extensions/description/2011' in root.tag:
            print ('LibreOffice extension declaration included')
        else:
            ('There is a xml extension declarartion missing in the description.xml.')

        childtags = []
        for child in root:
            childtags.append(child.tag)

        z = ''
        for element in childtags:
            version = re.findall(r'version', element)
            registration = re.findall(r'registration', element)
            license = re.findall(r'license', element)
            identifier = re.findall(r'identifier', element)
            icon = re.findall(r'icon', element)
            display= re.findall(r'display-name', element)
            description = re.findall(r'extension-description', element)
            dependencies = re.findall(r'dependencies', element)
            publisher = re.findall(r'publisher', element)

        if version.count > 0:
            print ('Extension version information included.')
        else:
            print ('There is an Extension version information missing.\n'
                   'Please add the following xml-tag:\n'
                   '<version value="[value for the version - a number]"/>')

        if (registration.count > 0) or (license > 0) :
            print ('Information about license included.')
        else:
            print ('There is a link to the license information missing. \nPlease add this link and make sure that it'
                   'points to the license file inside the Extension. Thus link could be as follows:\n'
                   '<registration>\n<simple-license accept-by="admin" >\n'
                   '<license-text xlink:href="[link to the license file in file format *.txt]" />\n'
                   '</simple-license>\n</registration>')

        if identifier.count > 0:
            print ('The identifier xml-tag is included.')
        else:
            print ('There is the identifier xml-tag missing. Please add an identifier'
                   'xml-tag like the following example:\n'
                   '<identifier value="org.[your organisation].[extension name]"/>')

        if icon.count > 0:
            print ('The icon xml-tag is included.')
        else:
            print ('The icon xml-tag with a link to an icon for the Extension is missing. Please add the following xml-tag:\n'
                   '<icon>\n<default xlink:href="[relative link to the extensionicon in file format *.png]" />\n'
                   '</icon>')

        if display.count > 0:
            print ('The display name xml-tag is set.')
        else:
            print ('There is no display name xml-tag set and thus the extension will not '
                   'show a name in the Extension-Manager. Please add a xml-tag with the'
                   'a display name like the following example:\n'
                   '<display-name>\n'
                   '<name>[Name that should be shown in the extension manager]\n'
                   '</name>\n</display-name>')
        if description.count > 0:
            print ('The description xml-tag is included in the description.xml file.')
        else:
            print ('Please add an extension-description xml-tag to the description.xml file of your extension '
                   'similar to the following example (the links points to the text files with the description;'
                   'it is possible to add a description for all supported language of the extension:\n'
                   '<extension-description>\n'
                   '<src xlink:href="description/description_en.txt" lang="en" />\n'
                   '<src xlink:href="description/description_de.txt" lang="de" />\n'
                   '</extension-descritption>')

        if dependencies.count > 0:
            print ('Information about program version included.')
        else:
            print ('There is no information about the (minimal / maximal program version included. Please'
                   'add a xml-tag with this information to the description.xml file like the following'
                   'example:\n'
                   '<dependencies xmlns:lo="http://libreoffice.org/extensions/description/2011">\n'
                   '<lo:LibreOffice-minimal-version name="LibreOffice 4.2" value="4.2"/>\n'
                   '</dependencies>\n'
                   'If you want to set the maximum program version, replace the word minimum with'
                   'maximum.')

        if publisher.count > 0:
            print ('Publisher xml-tag included.')
        else:
            print ('The publisher xml-tag with the extension author is missing. Please add a'
                   'xml-tag with the publisher of the extension in the following manner:\n'
                   '<publisher>\n'
                   '<name xlink:href="[link to the website or blog of the author]">[name of the author\n'
                   '</name>\n</publisher>')

        f.close
    except (KeyError):
        print ('There is a file description.xml missing in the extension. Thus the extension is not valid!')

    try:
        tree = ET.parse(zip.open('META-INF/manifest.xml'))
        root = tree.getroot()
        if "http://openoffice.org/2001/manifest" in root.tag:
            pass
        else:
            print ('A manifest xml-tag is missing in the manifest.xml file.')


    except (KeyError):
        print ('There is a file manifest.xml missing in the extension. Please add such file to the '
               'extension to get it valid!')



except IndexError:
    print ("Please submit an extension file within the call of this script: 'python oxtTest.py <name of the extension file>'")


