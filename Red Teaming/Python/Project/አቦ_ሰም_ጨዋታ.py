from random import *

def intro():
	global a, i
	print("አቦ_ሰም_ጨዋታ 🎮".center(100, "_"))
	print("\n")

	a =  "አው"
	i = input("ለጨዋታው_ዝግጁ_ነክ = አው/አይደለሁም: ")
	print("")

try:

	def body():
		global x
		if i != a or i == "":
			print("".center(100, '_'))
			print("buy buy...")
			print('\n')
		elif i == a:
			print("".center(105, "_"))
			print('\nየጨዋታው_ህግ = ተጫዋች: ልዩ,  computer: አንድ_አይነት\n')
			print("መዳፍ እና አይበሉባ")
			print("")
			print("".center(105, "_"))
			x = input("""     
			                                         ተጫዋች\n
			                                    መዳፍ ወይስ አይበሉባ\n\n
			                                          >> """)
			g = ["አይበሉባ","መዳፍ"]
			if x == "መዳፍ":
				h = choice(g)
				print("".center(105, "_"))
				print("")
				print("ተጫዋች = መዳፍ")
				print(f"computer = {h}")
				print("".center(105, "_"))
				print("")
				if x == "መዳፍ" and h == "መዳፍ":
					print(" 😢😢😢 YOU LOSE 😢😢😢 ".center(100, '#'))
					print(" 🎉🎁🎉 COMPUTER IS WIN 🎉🎁🎉 ".center(100, '$'))
					print("".center(105, '_'))
				elif x == "መዳፍ" and h == "አይበሉባ":
					print(" 🎉🎁🎉 YOU WIN 🎉🎁🎉 ".center(100, '$'))
					print(" 😢😢😢 COMPUTER IS LOSE 😢😢😢 ".center(100, '#'))
					print("".center(105, '_'))
			elif x == "አይበሉባ":
				h = choice(g)
				print("".center(105, "_"))
				print("")
				print("ተጫዋች = አይበሉባ")
				print(f"computer = {h}")
				print("".center(105, "_"))
				print("")
				if x == "አይበሉባ" and h == "መዳፍ":
					print(" 🎉🎁🎉 YOU WIN 🎉🎁🎉 ".center(100, '$'))
					print(" 😢😢😢 COMPUTER IS LOSE 😢😢😢 ".center(100, '#'))
					print("".center(105, '_'))
				else:
					if x == "አይበሉባ" and h == "አይበሉባ":
						print(" 😢😢😢 YOU LOSE 😢😢😢 ".center(100, '#'))
						print(" 🎉🎁🎉 COMPUTER IS WIN 🎉🎁🎉 ".center(100, "$"))
						print("".center(105, '_'))

except Exception as f:
	print(f)







intro()
body()