class Filexts:

	'''	This class scans files of a single specific file extension or file type.

	This class takes two arguements:

	(1)search_str: a directory string where the search stars and 

	(2)search_depth: the number of directories to scan from the "search_str", is optional and defaults to 1.

	'''

	import glob


	def __init__(self, search_str, search_depth = 1):
		self.search_str = search_str
		self.star = self.search_str.find('*')
		self.all_files = []
		self.warning = ''
		self.fix = '*/'
		self.call = 0

		while self.call <= search_depth:
			self.next_dir()
			self.call += 1

	def list(self):
		return self.all_files

	def next_dir(self):
		self.search_dir = self.glob.glob(self.search_str)
		for self.file in self.search_dir:

			if self.file not in self.all_files:
				self.all_files.append(self.file)
			else:
				self.warning = 'No file was found!'

		self.search_str = self.search_str[:self.star] + self.fix +  self.search_str[self.star:]
