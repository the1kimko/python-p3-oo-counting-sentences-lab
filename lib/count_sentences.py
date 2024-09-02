#!/usr/bin/env python3
import re # Import the re model for regular expressions

class MyString:
  def __init__(self, value=""):
    self.value = value

  @property
  def value(self):
    """Get the value of the string."""
    return self._value
  
  @value.setter
  def value(self, new_value):
    """Set the value of the string, ensuring it is a string."""
    if not isinstance(new_value, str):
        print("The value must be a string.")  # Print the error message instead of raising an error
    else:
        self._value = new_value  # Assign the new value to the private variable

  def is_sentence(self):
      """Returns True if the value ends with a period, False otherwise."""
      return self.value.endswith('.')  # Check if the value ends with a period
  
  def is_question(self):
      """Returns True if the value ends with a question mark, False otherwise."""
      return self.value.endswith('?')  # Check if the value ends with a questionmark
  
  def is_exclamation(self):
      """Returns True if the value ends with an exclamation mark, False otherwise."""
      return self.value.endswith('!')  # Check if the value ends with a exclamation mark
  
  def count_sentences(self):
      """Returns the number of sentences in the value."""
      # Split the value into a list of sentences using regular expressions
      sentences = re.split(r'[.!?]+', self.value)
        
      # Filter out empty sentences
      sentences = [s for s in sentences if s.strip()]
        
      return len(sentences)