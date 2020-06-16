seqNo = 0
class packet():
	def __init__(self,msg):
		global seqNo
		self.msg = msg
		self.seqNo = seqNo
		seqNo = 1 - seqNo

	def __str__(self):
		return str(self.msg)