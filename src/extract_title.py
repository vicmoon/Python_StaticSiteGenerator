
def extract_title(markdown):
    #find the line staring with a single # and return it 
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("No h1 header found")


    

    


