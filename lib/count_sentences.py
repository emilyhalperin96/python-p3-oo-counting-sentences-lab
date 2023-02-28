#!/usr/bin/env python3

class MyString:

  def __init__(self, value=""):
    self._value = value

  def get_value(self):
    return self._value

  def set_value(self, value):
    if not isinstance(value, str):
      print("The value must be a string.")
    else:
      self.value = value 
  
  value = property(get_value, set_value)

  def is_sentence(self):
    if self._value.endswith("."):
      return True
    else:
      return False

      #return self._value.endswith(".")

  def is_question(self):
    if self._value.endswith('?'):
      return True
    else:
      return False 
  
  def is_exclamation(self):
    if self._value.endswith('!'):
      return True
    else:
      return False 
  
  def count_sentences(self):
    value = self.value
    for punc in ['!','?']:
        value = value.replace(punc, '.')
    
    sentences = [s for s in value.split('.') if s]
    
    return len(sentences)


