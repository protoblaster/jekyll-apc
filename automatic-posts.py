import os
import datetime

author = None
article_title = None
date = datetime.date.today()
date = date.strftime('%Y-%m-%d')
timezone = None
article_date = None
layout = None
file_name = None
path_name = None
dashes = '---'
categories = []

variable_names = []
variable_values = []

def read_input():
    
    os.system('clear')

    global author, article_title, date, timezone, article_date, layout, file_name
    global path_name, variable_names, variable_values, categories

    author = input('Enter the author of the article> ')
    article_title = input('Enter the title of the article> ')
    timezone = input('Enter the timezone> ')
    article_date = date + ' ' + timezone
    layout = input('Enter the layout for the page> ')
    file_name = input('Enter the file name> ')
    path_name = input('Enter the path to store the new file> ')

    variable_names = ['Author:', 'Article Date:', 'Layout:', 'Path to file:',
                      'Article Title:', 'Categories:']
    variable_values = [author, article_date, layout, path_name + file_name,
                       article_title, categories]

    for index in range(3):
        tag = input('Enter a tag for the blog post> ')
        categories.append(tag)

def check_input():
    
    global variable_names, variable_values

    os.system('clear')

    for index, x in enumerate(variable_names):
        print(variable_names[index], variable_values[index])

    print('\n')


def write_file():
    
    global author, article_title, article_date, layout, file_name, path_name
    global categories

    try:
        with open(f'{path_name}/{file_name}', 'w') as file:
            file.write(f'{dashes} \n')
            file.write(f'author: {author} \n')
            file.write(f'title: {article_title} \n')
            file.write(f'date: {article_date} \n')
            file.write(f'layout: {layout} \n')
            file.write('categories: ')

            for index, x in enumerate(categories):
                file.write(x + ' ')

            file.write(f'\n{dashes} \n')

    except OSError as e:
        print('The Directory to store the file in does not exist.',
              '\n', e)
        path_name = input('Enter the path name> ')
        file_name = input('Enter the file name> ')
        
        write_file()
    
    else:
        print('The program has been successfully executed')

read_input()
check_input()
write_file()
