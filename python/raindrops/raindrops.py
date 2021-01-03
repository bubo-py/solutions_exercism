# def convert(number):
#     sound = ''
#     if number %  3 == 0:
#         sound += 'Pling'
    
#     if number %  5 == 0:
#         sound += 'Plang'
    
#     if number %  7 == 0:
#         sound += 'Plong'

#     if sound == '':
#         return str(number)
    
#     return sound
def convert(number):
    result = ''
    lookup = {
        3: 'Pling',
        5: 'Plang',
        7: 'Plong'
    }
    for n in lookup:
        if not number % n:
            result += lookup[n]

    return result if result else str(number)