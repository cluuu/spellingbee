import deepl 
import os 

AUTH = os.getenv("DEEPL_AUTH_KEY") 

SOURCE_LANG = "DE"
INTERMEDIATE_LANG = "EN-US"



def check_auth(): 

    if AUTH is None: 
        print("No Authentication key set. Please store API key in $DEEPL_AUTH_KEY environment variable.")
        sys.exit()


def main(): 

    check_auth()

    source = input("provide input: ")
    
    translator = deepl.Translator(os.getenv("DEEPL_AUTH_KEY"))

    intermediate = str(translator.translate_text(source , target_lang = INTERMEDIATE_LANG)) 
    print(intermediate)

    result = translator.translate_text(intermediate, target_lang = SOURCE_LANG) 

    print(result) 


if __name__ == "__main__": 
    main() 