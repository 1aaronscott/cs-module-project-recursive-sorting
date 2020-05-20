''' 1:1 code challenge '''
# list = ['Joe', '2', 'Ted', '4.98', '14', 'Sam',
#         'void *', '42', 'float', 'pointers', '5006']
# for value in list:
#     print(value, "\n")
list2 = ['Bob', 'Slack', ['reddit', '89', 101, [
    'alacritty', '(brackets)', 5, 375]], 0, ['{slice, owned}'], 22]
#out = [val for sublist in list2 for val in sublist]


def list_print(array):
    for value in array:
        if type(value) is list:
            list_print(value)
        else:
            print(value, "\n")


#[val for sublist in word_list for val in sublist]
list_print(list2)
