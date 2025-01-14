
calls=0

def count_calls():
    global calls
    calls +=1

def string_info(string):
    count_calls()
    return (len(string), string.lower(), string.upper())


def is_contains(string,list_to_search):
    count_calls()
    string.lower()
    for i in range(len(list_to_search)):
        list_to_search[i].lower()
        if list_to_search[i] in string:
            return True
        elif list_to_search[i] not in string:
            return False


print(string_info('Capybara'))
print(string_info('Armaggedon'))
print(is_contains('Urban', ['ban','BaNan', 'urBaN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)