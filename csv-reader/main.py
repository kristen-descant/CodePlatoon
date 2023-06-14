import csv

cat_csv = 'data/cats.csv'
dog_csv = 'data/dogs.csv'

def search_for_pet(type_animal):
    if type_animal == 'dog':
        file_name = dog_csv
    if type_animal == 'cat':
        file_name = cat_csv
    try:
        with open(file_name, 'r') as infile:
            reader = csv.reader(infile)

            animals = []
            for row in reader:
                animals.append(row)
            
            testStr = ''
            for animal in range(1, len(animals)):
                testStr += f'{animals[animal][0]} is a {animals[animal][1]} year old {animals[animal][2]}\n'

        return testStr
    
    except Exception as e:
        e = f'There is no file for {type_animal}'
        return e



print(search_for_pet('dog'))
print(search_for_pet('cat'))
print(search_for_pet('snake'))


