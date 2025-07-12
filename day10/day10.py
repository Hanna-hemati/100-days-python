def format_name(f_name, l_name):
    a = """take a first and last name and format it lallal
    jfs
    sgj
    sfgsoo
    thbg"""
    if f_name == "" or l_name == "":
        return "you did not provide  valid inputs"
    else:
        formatted_f = f_name.title()
        formatted_l = l_name.title()
        return f"result: {formatted_f}, {formatted_l}"


# format_string = format_name(f_name= "hannA", l_name= "hemAti")

print(format_name(input("What is your first name?"), input("What is your last name?")))
