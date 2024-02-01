
#IAmAPascalCasedString

# text = input('Enter your word here: ');


# def convert_to_snake_case(pascal_or_camel_cased_string):
#     # snake_cased_char_list = []
    
#     # for char in pascal_or_camel_cased_string:
#     #     if char.isupper():
#     #         lower_cased_char = '_' + char.lower()
#     #         snake_cased_char_list.append(lower_cased_char)
#     #     else:
#     #         snake_cased_char_list.append(char)    
#     # result =  ''.join(snake_cased_char_list).strip('_')
#     # return result;   
    
#     # List comprehesion
    
#     snake_cased_char_list = [
#         '_' + char.lower() if char.isupper()
#         else char
#         for char in pascal_or_camel_cased_string 
#     ]  
    
#     return ''.join(snake_cased_char_list).strip('_')
    
            
    
    
# def main():
#         print(convert_to_snake_case(text))
    
    
# if __name__ == '__main__':
#     main()
     
            
def testing():
    print('Testing');            