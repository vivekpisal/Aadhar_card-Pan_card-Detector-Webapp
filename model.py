import cv2
import easyocr
from pylab import rcParams
from IPython.display import Image
import pytesseract



rcParams['figure.figsize']=8,16


def image_to_text(name):
	reader=easyocr.Reader(['en'])
	Image(name)
	op=reader.readtext(name)
	op1=pytesseract.image_to_string(name,lang='hin')
	op2=pytesseract.image_to_string(name)
	if 'INCOMETAX DEPARTMENT' in op2 or 'NCOMETAX DEPARTMENT' in op2 or 'आयकर विभाग' in op1 or 'ज्ञायकर विभाज' in op1 or 'ज्ञायकर विभाग' in op1 or 'अं स्आवायकर विभाण' in op1 or 'स्थायी लेखा संख्या कार्ड' in op1:
		res=True
	else:
		res=False
	return op,res,op1