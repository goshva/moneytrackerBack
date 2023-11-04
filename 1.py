my_shelf = {}
author = input('Введите автора:')
book = input('Введите книгу (s - стоп):')
books = []
while book != 's':
   books.append(book)
   book = input('Введите книгу (s - стоп):')
my_shelf[author] = books
print(my_shelf)