import quit_app
import clean_bin

options = ['Quit all app', 'Clean bin', 'Clear cache']
i = 0
for option in options:
    i+=1
    print(f'{i})',option)
user_input = int(input("User choice: "))

if user_input == 1:
    quit_app.quit_all_app()
elif user_input == 2:
    clean_bin.cleaning_bin()
