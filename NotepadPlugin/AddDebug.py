from Npp import *  

pos = editor.getSelectionEnd()
for i in range(0,100):
	if editor.getCharAt(pos) == 59:
		editor.insertText(pos + 1,"print_r("+editor.getSelText()+");die;")  
		break
	pos = pos + 1