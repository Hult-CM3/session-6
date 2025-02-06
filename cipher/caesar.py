alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-1: get input from the user if they want to decode or encrpyt
direction = 
text = 
shift = 

# TODO-2: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs. If you're clever you can make only 1 function that can handle both encryption and decryption. 
    # What happens if a user enters a shift > 26? 

# TODO-3: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    # e.g. 
    # plain_text = "hello"
    # shift = 5
    # cipher_text = "mjqqt"
    # print output: "The encoded text is mjqqt"
    
    ##HINT #1: How do you get the index of an item in a list:
    # https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##HINT #2: Get it working without capitzliation first, then figure out how to manage the capital letters. 
    # https://www.codecademy.com/resources/docs/python/strings/isupper

    ##🐛 Bug alert: What happens if you try to encode the word 'civilization'? 🐛

# TODO-4: Call the function and pass in the user inputs. You should be able to test the code and encrypt or decrypt a message.

# TODO-5: Print out the encoded text to the user

# TODO-6: Create a way for the user to continue or not HINT: Use a loop!

# Extra Challenge TODO-7: Can you import the art from logo.py and print it out at the beginning of the program?
  ## Create your own ASCII art here: https://www.asciiart.eu/text-to-ascii-art 
