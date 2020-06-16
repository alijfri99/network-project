import tools
import pickle

class packet():
	def __init__(self,msg,seqNo):
		self.msg = bytearray(pickle.dumps(msg))
		self.seqNo = seqNo
		self.checksum = tools.complement(tools.calcsum(self.msg))
	def __str__(self):
		return str(pickle.loads(bytes(self.msg)))