import sys #interaction with program through terminal
import re #regex library

# variable "updated_email" is an ammended version of the original, possibly faulty email ammendments include adding
# @ symbols, making lowercase, and replacing "_dot_" with a period for example. 

"""
myEmailsFinal checks for validity of emails according to predetermined specifications. 
If invalid email detected, prints invalid emails out, with one reason for why they are invalid. 
If valid email detectd, prints valid emails out. 

@author William Wallace
@date 17/05/2020
"""

#list of valid_extensions
valid_extensions = ['.co.nz','.com.au','.co.ca','.com','.co.us','.co.uk']

"""
    Read_tokens function looks for empty entries, whitespace, and reads tokens in original_email to check if @ symbol present.
    If not present, the last "_at_" substring is searched for and replaced by @ symbol.
    If @ symbol or "_at_" not found, original_email is invalid.
    """
def read_tokens(updated_email,original_email):
    if(len(updated_email)<1):
        print("INVALID: no entry")
        return 0
    updated_email = updated_email.lower()
    whitespace = re.findall("\s",updated_email)
    if(len(whitespace)>0):
        print(original_email + " <-- " +"INVALID: should not include whitespace.")
        return 0
    email_list = list(updated_email)

    """ 
    Attempts to replace last "_at_" in updated_email with @ symbol if @ not found by reversing the updated_email and
    searching for "_ta_", starting from the beginning of the reversed email.
    """
    if("@" not in updated_email):
        index = 0 
        for i in reversed(range(len(email_list))):
            if(i>3):
                if((updated_email[i]+updated_email[i-1]+updated_email[i-2]+updated_email[i-3])=="_ta_"): 
                    index = i
                    break
            else:
                print(original_email + " <-- " +"INVALID: no @ or _at_ found.")
                return 0
        email_list[index] = ""
        email_list[index-1] = ""
        email_list[index-2] = ""
        email_list[index-3] = "@"
        #to help .txt files being parsed as args in terminal
        updated_email = "".join(email_list)    

    updated_email = updated_email.replace("_dot_",".")
    email_sections = updated_email.split("@") # divides email into a list of strings using @ symbol as delimiter.
    if(len(email_sections)>2):
        print(updated_email + " <-- INVALID: more than one @ symbol.")
        return 0
    if(len(email_sections[0])<1):
        print(updated_email + " <-- INVALID: missing mailbox name.")
        return 0
    if(len(email_sections[1])<1):
        print(updated_email + " <-- INVALID: missing domain name.")
        return 0
    return email_sections

    """
    Checks the validity of mailbox name. Searches for invalid characters and invalid usage of separators.
    """
def mailbox_check(mailbox_tokens,original_email): 
    invalid_char = re.findall(r'([^A-Z a-z 0-9 \- \. \_]+)',mailbox_tokens)    #invalid if not alphanumeric or containing underscore, hyphen or period.
    if(len(invalid_char)>0):
        print(original_email + " <-- INVALID: invalid characters exist in mailbox.")
        return 0
    adjacent_seps = re.findall(r'[ \. \- \_]{2,}',mailbox_tokens)
    start_sep = re.findall(r'^[\. \- \_]',mailbox_tokens)
    end_sep = re.findall(r'[\. \- \_]$',mailbox_tokens)
    if(len(adjacent_seps)>0):
        print(original_email + " <-- INVALID: mailbox contains two or more separators in a row.")
        return 0
    if(len(start_sep)>0):
        print(original_email + " <-- INVALID: mailbox starts with separator.")
        return 0
    if(len(end_sep)>0):
        print(original_email + " <-- INVALID: mailbox ends with separator.")
        return 0
    return mailbox_tokens

    """
    Checks the validity of domain name and extension. Checks for correct formatting of 
    IPv4 address,  invalid characters, and invalid usage of seperators. Domain name must also end in a valid extension. 
    """
def domain_check(domain_tokens,original_email):
    if(domain_tokens.startswith("[") and domain_tokens.endswith("]")):
       eight_bit_IP = domain_tokens[1:-1].split(".") #uses period as a delimiter to separate IPv4 address into eight_bit pieces
       if(len(eight_bit_IP)!=4):
           print(original_email + " <-- " +"INVALID: invalid numeric domain.")
           return 0
       else:
           for num_digits in eight_bit_IP:
               if(not num_digits.isdigit()):
                   print(original_email + " <-- " +"INVALID: IPv4 address contains invalid, non-numeric characters.")
                   return 0
               elif(int(num_digits)>255 or len(num_digits)>3):
                   print(original_email + " <-- " +"INVALID: number(s) in IPv4 sections exceeds 8 bits/255.")
                   return 0
           return domain_tokens
    invalid = re.findall(r'([^A-Z a-z 0-9 \.]+)',domain_tokens) #invalid if not alphanumeric or containing underscore, hyphen or period.
    if(len(invalid)>0):
        print(original_email + " <-- INVALID: domain name contains invalid characters.")
        return 0
    adjacent_seps = re.findall(r'[ \.]{2,}',domain_tokens)
    end_sep = re.findall(r'[\.]$',domain_tokens)
    start_sep = re.findall(r'^[\.]',domain_tokens)
    if(len(adjacent_seps)>0):
        print(original_email + " <-- INVALID: domain name contains two or more separators in a row.")
        return 0
    if(len(start_sep)>0):
        print(original_email + " <-- INVALID: domain name starts with seperator.")
        return 0
    if(len(end_sep)>0):
        print(original_email + " <-- INVALID: domain name end with seperator.")
        return 0
    for domain in valid_extensions:
        if(domain_tokens.endswith(domain)):
            return domain_tokens
    print(original_email + " <-- INVALID: domain name not recognised as part of valid list.")
    return 0

    """
    Main function takes original email as input, splits into mailbox and domain parts
     either side of @ symbol, checks mailbox name for validity, checks domain name 
     and extensions for validity, and outputs the result. Result is modified to be valid if necessary.
     Program breaks from pipe if email cannot be modified to become valid.   
    """
if __name__=="__main__":
    try:
        while(True):
            original_email = input()
            tokens = read_tokens(original_email,original_email)
            if(tokens==0):
                continue
            mailbox = mailbox_check(tokens[0],original_email)
            if(mailbox==0):
                continue
            domain = domain_check(tokens[1],original_email)
            if(domain ==0):
                continue
            final_email =  mailbox + "@" + domain
            print(final_email)
    except Exception:
        pass