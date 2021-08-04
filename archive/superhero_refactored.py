import requests

def sphero_request_raw(name):
    url = "https://www.superheroapi.com/api.php/2619421814940190/"
    search = "search/"
    # name = input('Enter name of')
    name = name
    timeout = 5
    response = requests.get(url + search + name, timeout=timeout)
    output_classified = (response.json())

    # output name
    print((output_classified['results'][0]['name'], output_classified['results'][0]['powerstats']['intelligence']))

    # return tuple
    # int() for numbers against strings
    return (output_classified['results'][0]['name'], int(output_classified['results'][0]['powerstats']['intelligence']))


char1 = 'Hulk'
char2 = 'Captain America'
char3 = 'Thanos'

list_of_chars = ['Hulk', 'Captain America', 'Thanos']

unsorted_list_of_chars = {}  # empty dict

# cycle of hero list
for char in list_of_chars:
    hero = sphero_request_raw(char)  # return name-value pair
    unsorted_list_of_chars[hero[0]] = hero[1]  # name like key in dict, value as value

print(unsorted_list_of_chars)  # look for check on print output

# sorting
# unsorted_list_of_chars.items() sorting inside dict, but not dict itself
# reverse = True - descending order
# key=lambda intelligence: intelligence[1] - method of sorting. INT value, lies on index [1]
sorted_list_of_chars = sorted(unsorted_list_of_chars.items(), reverse=True, key=lambda intelligence: intelligence[1])

# output for checking
print(sorted_list_of_chars)
print('--------------------------')

# First element will be have most higher stats
print('Most intellgent guy: ' + sorted_list_of_chars[0][0])