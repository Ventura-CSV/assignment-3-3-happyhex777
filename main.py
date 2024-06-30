def main():
    email = input('Enter your email: ')
    """
    ########################################
    Code Your Program here
    ########################################
    """
    def is_valid_email(email):
        result = False
        
        if not email[0].isalpha():
            return result
        
        if not (5 < len(email) < 30):
            return result
        
        if '@' not in email:
            return result
        
        at_index = email.index('@')
        if'.' not in email[at_index:]:
            return result
        result = True
        return result
    result = is_valid_email(email)
    print(result)

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
