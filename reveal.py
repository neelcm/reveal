import glob
import os
from subprocess import call
from biplist import *

appDir = ''
tempDir = ''
outFileName = 'URLSchemes.txt'

call(['mkdir', tempDir])

call(['touch', outFileName])

for ipa in os.listdir(appDir):
	if ipa.endswith('.ipa'):
		ipaTempDir = 'reveal-tmp/' + str(ipa)
		call(['mkdir', ipaTempDir])
		call(['/usr/bin/unzip', '-d', ipaTempDir, appDir + str(ipa)])
		appName = (os.listdir(tempDir + '/' + ipa + '/Payload/'))[0]
		infoPlist = readPlist(tempDir + '/' + ipa + '/Payload/' + appName + '/Info.plist')
		try:
			urlScheme = infoPlist['CFBundleURLTypes'][0]['CFBundleURLSchemes'][0]
		except:
			urlScheme = ''
		with open(outFileName, "a") as file:
			file.write(ipa.split(' ', 1)[0] + '\t\t\t\t' + urlScheme + '\n')
