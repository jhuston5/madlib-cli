from sys import exit
import re, os

def welcome():
  print("Welcome to Madlibs! You will be prompted to enter word type (Adjective, Noun, Animal, etc). \n Type whatever word you want that corresponds to the correct type, then press enter. \n Once you have inputted your last word, wait to see the Madlib Magic!")

test_path = "../assets/dark_and_stormy_night_template.txt"
example_path = "../assets/madlib_template.txt"
def user_input(words):
  madlib_word_list = []
  for i in words:
    response = input(f"Input a {i}: ")
    madlib_word_list.append(response)
  return madlib_word_list



def read_template(file_path):
  with open(file_path, 'r') as read_file:
    text = read_file.read()
    return text

def parse_template(text):
  fill_in = r"{([\w ',.-]+)}"
  prompts = tuple(re.findall(fill_in, text))
  text_template = re.sub(fill_in, '{}', text)
  return text_template, prompts

def merge(text_template, words):
  formatted_madlib = text_template.format(*words)
  return formatted_madlib


def create_new_file(full_madlib):
  with open('../new_madlibs/ultimate_madlib.txt', 'w') as written_full_madlib:
    text = written_full_madlib.write(full_madlib)

if __name__ == "__main__":

  welcome()
  """text = read_template(test_path)
  text_template, words = parse_template(text)
  word_text = user_input(words)
  full_madlib = merge(text_template, word_text)
  create_new_file(full_madlib)"""

  example_text = read_template(example_path)
  text_template, words = parse_template(example_text)
  word_text = user_input(words)
  full_madlib = merge(text_template, word_text)
  create_new_file(full_madlib)
  print(full_madlib)
  print('Finished your Madlib!')