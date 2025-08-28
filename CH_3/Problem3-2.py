#Replaced String with another String by using Variable name . replace ("Old","New")
letter = """ Dear <|Name|>,
                You are selected! 
                <|Date|>"""

print(letter.replace("<|Name|>","Hammad").replace("<|Date|>","27 August 2025"))