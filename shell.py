import vision 
# Rename Vision to vision
while True:
    code = input("Vision $ ")
    result, error = vision.run("<stdin>",code)

    if error: 
        print(error.as_string())
    else: 
        print(result)