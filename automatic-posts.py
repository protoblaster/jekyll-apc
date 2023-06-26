import os
import datetime

def read_input():
    author = input('Enter the author\'s name> ')
    article_title = input('Enter the title for the aricle> ')
    timezone = input('Enter the timezone (London = +0100)> ')
    date = datetime.date.today()
    article_date = datetime.date.today().strftime('%Y-%m-%d') + ' ' + timezone
    layout = input('Enter the layout for the page> ')
    file_name = input('Enter the file name> ')
    path_name = input('Enter the path to store the file in> ')

    categories = []
    for _ in range(3):
        tag = input('Enter a tag for the article> ')
        categories.append(tag)

    return author, article_title, article_date, layout, file_name, path_name, categories, date

def check_input(variable_names, variable_values):
    os.system('clear')
    for name, value in zip(variable_names, variable_values):
        print(f'{name} {value}')
    print()

def write_file(author, article_title, article_date, layout, file_name, path_name, categories, date):
    try:
        file_path = os.path.join(path_name, f'{date}-{file_name}')

        with open(file_path, 'w') as file:
            file.write('---\n')
            file.write(f'author: {author}\n')
            file.write(f'title: {article_title}\n')
            file.write(f'date: {article_date}\n')
            file.write(f'layout: {layout}\n')
            file.write(f'categories: ' + ' '.join(categories) + '\n')
            file.write('---\n')

    except OSError:
        print('The Directory to store the file doesn\'t seem to exist!')
        path_name = input('Enter the path name only> ')
        file_name = input('Enter the file name only> ')
        write_file(author, article_title, article_date, layout, file_name, path_name, categories, date)

    else:
        print('The program executed successfully!')

def main():
    input_values = read_input()
    variable_names = ['Author:', 'Article Title:', 'Article Date:', 'Layout:', 'File Name:', 'Categories:']

    check_input(variable_names, input_values)
    write_file(*input_values)

if __name__ == '__main__':
    main()