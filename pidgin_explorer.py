import os, time

def pidgin_explorer():
	log = "C:\\Users\\" + os.getlogin() + "\\AppData\\Roaming\\.purple\\logs\\jabber\\"
	os.system('cls')

	if len(os.listdir(log)) > 0:
		print("[*] Logs found")
		print("[*] All addresses found :")
		for addr in os.listdir(log):
			print("	[-] " + addr)
		addr_to_use = input("[?] What logs would you like to explore ? : ")
		if addr_to_use in os.listdir(log):
			os.system('cls')
			print("[*] All discussions found : ")
			for discussions in os.listdir(log + addr_to_use):
				print("	[-] " + discussions)
			discussion_to_explore = input("[?] What discussion would you like to explore ? : ")
			if discussion_to_explore in os.listdir(log + addr_to_use):
				os.system('cls')
				discussions = os.listdir(log + addr_to_use + "\\" + discussion_to_explore)
				if len(discussions) <= 0:
					print("[!] No discussion found")
					time.sleep(0.5)
					pidgin_explorer()
				print("[*] Total of " + str(len(discussions)) + " discussion(s) found : ")
				nbchat = 0
				for chat in discussions:
					nbchat+=1
					print("{} - ".format(nbchat) + "The " + chat.split('.')[0])
					time.sleep(0.01)
				nbchat = input("[?] What discussion would you like to read ? : ")
				if discussions[int(nbchat)-1] != "":
					os.system("start iexplore.exe \"" + log + addr_to_use + "\\" + discussion_to_explore + "\\" + discussions[int(nbchat)-1] + "\"")
					pidgin_explorer()
			else:
				print("[!] Discussion not found")
				time.sleep(0.5)
				pidgin_explorer()
		else:
			print("[!] Address not found")
			time.sleep(0.5)
			pidgin_explorer()
	else:
		print("[!] No log found")
		time.sleep(0.5)
		pidgin_explorer()

pidgin_explorer()
