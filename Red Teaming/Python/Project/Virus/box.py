def box():
	with open("box.vbs", "x") as file:
		file.close()
	with open("box.vbs", "w") as file:
		file.write('MsgBox "This system is infected by JOSI_VIRUS !!!", vbOKOnly + vbInformation, "JOSI_VIRUS"')