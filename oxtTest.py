import zipfile
import errno
import sys

try:
    extensionfile = sys.argv[1]
    zip=zipfile.ZipFile(extensionfile)
    try:
        f=zip.open('description.xml')
        contents=f.read()

        if contents.count('http://libreoffice.org/extensions/description/2011') >0:
            print('LibreOffice extension declaration inclueded')
        elif contents.count('http://openoffice.org/extensions/description/2006') >0:
            print('OpenOffice extension declaration included')
        else:
            print('There is a xml extension declarartion missing in the description.xml.')
        
        if contents.count('identifier value=') >0:
            print('Identifier tag for extension is included.')
        else:
            print('Identifier tag for extension is missing.')
        
        if contents.count('license-text xlink:href=') >0:
            print('Tag for License text link is included.')
        else:
            print('There is a tag for the license text link missing in the description.xml file.')
    
        f.close
    except (KeyError):
        print ('There is a file description.xml missing in the extension. Thus the extension is not valid!')
    
    try:
        g=zip.open('META-INF/manifest.xml')
        contents=g.read()
        if contents.count('<manifest:manifest xmlns:manifest="http://openoffice.org/2001/manifest">') > 0:
            pass
        elif contents.count('<manifest:manifest') > 0:
            pass
        else:
            print('There is a xml declaration missing in the file manifest.xml starting with the following xml-tag: \n'
            '<manifest:manifest xmlns:manifest="http://openoffice.org/2001/manifest">.')
        g.close
    
    except (KeyError):
        print ('There is a file manifest.xml missing in the extension. Please add such file to the '
           'extension to get it valid!')


except IndexError:
    print ("Please submit an extension file within the call of this script: 'python oxtTest.py <name of the extension file>'")
