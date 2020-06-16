class packet():
	def __init__(self,msg,seqNo):
		self.msg = msg
		self.seqNo = seqNo

	def __str__(self):
		return str(self.msg)