import zipfile
import errno

extensionfile= raw_input('Please type in the name of the extension file you want to investigate: ')

zip=zipfile.ZipFile(extensionfile)
try:
    f=zip.open('description.xml')
    contents=f.read()
    if contents.count('http://libreoffice.org/extensions/description/2011') >0:
        print('LibreOffice extension declaration included')
    elif content.count('http://openoffice.org/extensions/description/2006') >0:
        print('OpenOffice extension declaration included')
    else:
        print('There is a xml extension declarartion missing in the description.xml.')
    f.close
except (KeyError):
    print ('There is a file description.xml missing in the extension. The extension is not valid!')


