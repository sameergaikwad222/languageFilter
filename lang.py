from langdetect import detect

recepie = ['1 star anise , चकरी फूल',
           '1 inch cinnamon stick , दालचीनी',
           '2 heaped tbsp fried onion , बरिस्ता',
           '2 tbsp ghee  , घी ',
           '1 tbsp ghee घी',
           '5-6 black peppercorns , काली मिर्च के दाने',
           '2 inches cinnamon stick , दालचीनी',
           '2 heaped tbsp sour curd , खट्टा दही',
           '1 star anise  , चकरी फूल',
           '1 tsp degi red chilli powder , देगी लाल मिर्च पाउडर',
           '1 tbsp coriander powder , धनिया पाउडर',
           '5-6 curry leaves  , कड़ी पत्ता',
           '1 bay leaf ,  तेजपत्ता',
           '3 fresh green chillies, cut in half  , हरी मिर्च',
           '6 eggs, hard boiled , अंडे',
           '1 tbsp oil , तेल',
           '2 bay leaves , तेजपत्ता',
           '3-4 cloves garlic, chopped  , लहसुन',
           '2 fresh green chillies, slit in half ,  हरी मिर्च']


desirecepie = []


# Major Desi Language are Marathi, Hindi , Nepali as per List of ISO 639-1 codes Link : https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
def isDesi(value):
    if(detect(value) in ["mr", "hi", "ne"]):
        return True
    else:
        return False


# Check weather given word is an Integer or what
def isInteger(value):
    try:
        intValue = int(value)
        return True
    except ValueError as e:
        return False


# Prima Check for weather it is english or anything else. Filters major String as We expect major strings in English or Desi
def isOtherThanEnglish(value):
    if(detect(value) == "en"):
        return False
    else:
        return True


def extractDesi(str):  # Extracting Desi words and making String of same and return same
    tempStr = ""
    litarr = str.split(" ")
    for lit in litarr:
        if(not(isInteger(lit))):
            if(lit and isOtherThanEnglish(lit) and isDesi(lit)):
                tempStr += lit + " "
    if(tempStr):
        return tempStr


for mixStr in recepie:
    for str in mixStr.split(","):  # splitting Each Mix String
        if(isOtherThanEnglish(str)):  # Checking if String is Other Than English
            if(isDesi(str)):
                # if whole string is Desi than append in desirecepie
                desirecepie.append(str)
            else:
                # if String contains mix words than extract desi words as a String
                tempStr = extractDesi(str)
                if(tempStr):
                    # If got desi words than make string and append in desirecepie
                    desirecepie.append(tempStr)


print("\n")
print("\n")
print("\n")
for d in desirecepie:
    print(d)
