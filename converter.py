import json


with open('Cookies.json', 'r', encoding='utf-8') as f: #открыли файл с данными
    firstCookies = json.load(f) #загнали все, что получилось в переменную
    



secondCookie = "["

i = 0
for majorkey in firstCookies:

	

	domain = firstCookies[i]['top_frame_site_key']
	if firstCookies[i]['expires_utc'] != 0:
		expirationDate = (firstCookies[i]['expires_utc'] / 1000000) - 11644473600
	else: expirationDate = 0

	
	if firstCookies[i]['is_httponly'] == 0:
		httpOnly = "false"
	elif firstCookies[i]['is_httponly'] == 1:
		httpOnly = "true"

	name = firstCookies[i]['name']
	path = firstCookies[i]['path']


	sameSite = ""
	if firstCookies[i]['samesite'] == 0:
		sameSite = "no_restriction"
	elif firstCookies[i]['samesite'] == -1:
		sameSite = "unspecified"

	secure = ""
	if firstCookies[i]['is_secure'] == 1:
		secure = "true"
	elif firstCookies[i]['is_secure'] == 0:
		secure = "false"


	session = ""
	if firstCookies[i]['has_expires'] == 0:
		session = "true"
	elif firstCookies[i]['has_expires'] == 1:
		session = "false"

	storeId = 0
	value = firstCookies[i]['encrypted_value']
	value = value.replace('\\', '\\\\')
	value = value.replace("\"", '\\"')


	secondCookie += "{\n"
	secondCookie += "\"domain\": " + "\"" + domain + "\",\n"
	secondCookie += "\"expirationDate\": " + str(expirationDate) + ",\n"
	secondCookie += "\"httpOnly\": " + httpOnly + ",\n"
	secondCookie += "\"name\": " + "\"" + name + "\",\n"
	secondCookie += "\"path\": " + "\"" + path + "\",\n"
	secondCookie += "\"sameSite\": " + "\"" + sameSite + "\",\n"
	secondCookie += "\"secure\": " + secure + ",\n"
	secondCookie += "\"session\": " + session + ",\n"
	secondCookie += "\"storeId\": " + "\"" + str(storeId) + "\",\n"
	secondCookie += "\"value\": " + "\"" + value + "\"\n"
	secondCookie += "},\n"
	i += 1
	



secondCookie = secondCookie[:-2]
secondCookie += "]\n"



my_file = open("converted_cookies.json", "w+")
my_file.write(secondCookie)
my_file.close()

print("Conversion completed")