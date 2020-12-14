#===============================================
#
#	SCAB = "Scan and Build" package
#	author: Jade C. Rigby
#			www.jaderigby.com
#
#	Version: 1.5.2
#
#	Features:
#	1.5
#	Added "only" method which returns positive results as opposed to "reIgnore" which excludes all positive results
#	1.5.2
#	Added potential "catch" (via error handling), for creating a new folder using "build".  Moniter for accuracy
#   	Example:
#			t = new scab()
#			t.build('some/new/folder')
#
#	USERS GUIDE:
#	sample = scab()
#	sample.scan("/filepath/to/scan")
#	#== Note: "ignore()" must be deployed before "record()" or "build()" can be used
#	sample.ignore("ignore-this-folder", "ignore-this-file")
#	sample.record("/filepath/where/record/wll-be-stored.txt")
#	sample.build("/destination/filepath")
#
#===============================================

import os, json, re

class scab:
	def __init__(self, absRel='absolute'):
		self.obj = None
		self.contentsFolders = None
		self.contentsFiles = None
		self.isFilePat = "[/]{1}[A-Za-z0-9_-]+[.][A-Za-z]{2,4}"
		self.singleFolder = None
		self.singleFile = None
		self.singleFileCheck = False
		self.newFolder = None
		self.ignoreFolders = None
		self.ignoreFiles = None
		self.myFolderPat = None
		self.myFilePat = None
		self.absRel = absRel

	def clean(self):
		self.obj = None
		self.contentsFolders = None
		self.contentsFiles = None
		self.singleFolder = None
		self.singleFile = None
		self.singleFileCheck = False
		self.newFolder = None
		self.ignoreFolders = None
		self.ignoreFiles = None
		self.myFolderPat = None
		self.myFilePat = None

	def scan(self, myDir):
		self.obj = myDir
		#== check to see if specific file is being passed in
		match = re.search(self.isFilePat, myDir)
		singleFile = ""
		if match:
			self.singleFileCheck = True
			tempDir = re.sub(self.isFilePat, "", myDir)
			tempFile = (re.findall(self.isFilePat, myDir)[0])[1:]
			singleFile = tempDir+'/'+tempFile
			self.singleFolder = tempDir
			self.singleFile = singleFile
		def gather_folderList(self):
			for root, dirs, files in os.walk(myDir):
				if dirs == []:
					yield root
				else:
					for folder in dirs:
						yield os.path.join(root, folder)
			return
		def compile_folderList():
			get_file_object = gather_folderList(self.obj)
			make_list = []
			for i in get_file_object:
				make_list.append(i)
			return make_list
		def gather_fileList(self):
			for root, dirs, files in os.walk(myDir):
				for file in files:
					yield os.path.join(root, file)
			return
		def compile_fileList():
			get_file_object = gather_fileList(self.obj)
			make_list = []
			for i in get_file_object:
				make_list.append(i)
			return make_list
		self.contentsFolders = compile_folderList()
		self.contentsFiles = compile_fileList()
		if self.contentsFolders == []:
			singleFolders = []
			singleFolders.append(self.singleFolder)
			self.contentsFolders = singleFolders
		if self.contentsFiles == []:
			singleList = []
			singleList.append(self.singleFile)
			self.contentsFiles = singleList

	def ignore(self, foldersIgnoreList=[], filesIgnoreList=[]):
		self.ignoreFolders = foldersIgnoreList
		self.ignoreFiles = filesIgnoreList
		tempFolderList = []
		tempFileList = []
		for i in self.contentsFolders:
			if not i in self.ignoreFolders:
				tempFolderList.append(i)
		for i in self.contentsFiles:
			if not i in self.ignoreFiles:
				tempFileList.append(i)
		self.contentsFolders = tempFolderList
		self.contentsFiles = tempFileList

	def reIgnore(self, myPat=' '):
		self.myFolderPat = myPat
		self.myFilePat = myPat
		reFolderList = []
		reFileList = []
		print
		print "REGEX PATTERN: "
		print '"%s"' % myPat
		regexCount = 0
		for i in self.contentsFolders:
			match = re.search(myPat, i)
			if match:
				regexCount += 1
			if not match:
				reFolderList.append(i)
		for i in self.contentsFiles:
			match = re.search(myPat, i)
			if match:
				regexCount += 1
			if not match:
				reFileList.append(i)
		print
		print "Number of Matches: ", regexCount
		print
		self.contentsFolders = reFolderList
		self.contentsFiles = reFileList

	def only(self, myPat=' '):
		reFolderList = []
		reFileList = []
		for i in self.contentsFolders:
			match = re.search(myPat, i)
			if match:
				reFolderList.append(i)
		for i in self.contentsFiles:
			match = re.search(myPat, i)
			if match:
				reFileList.append(i)
		self.contentsFolders = reFolderList
		self.contentsFiles = reFileList

	def record(self, myRecord=""):
		def prep_doc(myContents):
			tempString = ""
			for i in myContents:
				if self.absRel == 'relative':
					i = i.replace(self.obj+"/", '')
				tempString = tempString+"\t'"+i+"',\n"
			makeString = "[\n"+tempString[:-2]+"\n]"
			return makeString
		dataFolders = prep_doc(self.contentsFolders)
		dataFiles = prep_doc(self.contentsFiles)
		data = "'Folders' : "+dataFolders+",\n'Files' : "+dataFiles
		if not myRecord == "":
			FILE = open(myRecord, 'w')
			FILE.write(data)
			FILE.close()

	def create(self, destination):
		newFolder = destination
		if not os.path.exists(newFolder):
			os.makedirs(newFolder)

	def build(self, destination):
		def doFolders():
			try:
				for folder in self.contentsFolders:
					newFolder = folder.replace(self.obj, destination)
					self.newFolder = newFolder
					if not os.path.exists(newFolder):
						os.makedirs(newFolder)
			except TypeError:
				"Captured Here! Must be creating a brand new folder"
				if not os.path.exists(destination):
					os.makedirs(destination)
		def doFile():
			try:
				for myFile in self.contentsFiles:
						GETFILE = open(myFile, 'r')
						data = GETFILE.read()
						finalDestination = myFile.replace(self.obj, destination)
						FILE = open(finalDestination, 'w')
						FILE.write(data)
						FILE.close()
			except TypeError:
				print "Warning: May be creating a new folder -- be sure to double-check"
		if (self.singleFileCheck == True):
			newFolder = re.sub(self.isFilePat, "", destination)
			print "Destination = ", newFolder
			if not os.path.exists(newFolder):
				print "Folder doesn't exist; creating it now!"
				os.makedirs(newFolder)
			doFile()
		else:
			doFolders()
			doFile()
