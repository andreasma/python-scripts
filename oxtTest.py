import zipfile
import errno

extensionfile= raw_input('Please type in the name of the extension file you want to investigate: ')

zip=zipfile.ZipFile(extensionfile)
try:
    f=zip.open('description.xml')
    contents=f.read()
    if contents.count('http://libreoffice.org/extensions/description/2011') >0:
        print('LibreOffice extension declaration included')
    elif contents.count('http://openoffice.org/extensions/description/2006') >0:
        print('OpenOffice extension declaration included')
    else:
        print('There is a xml extension declarartion missing in the description.xml.')
    f.close
except (KeyError):
    print ('There is a file description.xml missing in the extension. Thus the extension is not valid!')
    
try:
    g=zip.open('META-INF/manifest.xml')
    contents=g.read()
    if contents.count('<manifest:manifest xmlns:manifest="http://openoffice.org/2001/manifest">') > 0:
        pass
    else:
        print('There is a xml declaration missing in the file manifest.xml starting with the following xml-tag: \n'
        '<manifest:manifest xmlns:manifest="http://openoffice.org/2001/manifest">.')
    g.close
    
except (KeyError):
    print ('There is a file manifest.xml missing in the extension. Please add such file to the '
           'extension to get it valid!')


