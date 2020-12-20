import requests

def stats(username):
	"""scrapes stats from the hiscores.""" 
	url = 'https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player=' + username
	data = requests.get(url)
	if data.status_code == 200:
		print("Hiscores are down")
	elif data.status_code == 404: 
		print("Username not found")
	else:
		data_to_text = data.text
		data_newline_to_comma = data_to_text.replace('\n', ',')
		data_splitted_by_comma = data_newline_to_comma.split(',')
		#print(data_splitted_by_comma[0])

		#Level indexing
		attack = data_splitted_by_comma[4]
		defence = data_splitted_by_comma[7]
		strength = data_splitted_by_comma[10]
		hitpoints = data_splitted_by_comma[13]
		ranged = data_splitted_by_comma[16]
		prayer = data_splitted_by_comma[19]
		magic = data_splitted_by_comma[22]
		cooking = data_splitted_by_comma[25]
		woodcutting = data_splitted_by_comma[28]
		fletching = data_splitted_by_comma[31]
		fishing = data_splitted_by_comma[34]
		firemaking = data_splitted_by_comma[37]
		crafting = data_splitted_by_comma[40]
		smithing = data_splitted_by_comma[43]
		mining = data_splitted_by_comma[46]
		herblore = data_splitted_by_comma[49]
		agility = data_splitted_by_comma[52]
		thieving = data_splitted_by_comma[55]
		slayer = data_splitted_by_comma[58]
		farming = data_splitted_by_comma[61]
		runecraft = data_splitted_by_comma[64]
		hunter = data_splitted_by_comma[67]
		construction = data_splitted_by_comma[70]

		# Output
		print("Attack: " + attack)
		print("Defence: " + defence)
		print("Strength: " + strength)
		print("Hitpoints: " + hitpoints)
		print("Ranged: " + ranged)
		print("Prayer: " + prayer)
		print("Magic: " + magic)
	
stats('Username')

