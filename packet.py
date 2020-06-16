class packet():
	def __init__(self,msg,seqNo,checksum):
		self.msg = msg
		self.seqNo = seqNo
		self.checksum = checksum

	def __str__(self):
		return str(self.msg)