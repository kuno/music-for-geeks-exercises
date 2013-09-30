#!/usr/bin/env python

# Exercise 2.
# Change the function name_to_number
# to use Hewlett's base-40 system [1].
#
# [1] See Example 3 in
# A Base-40 Number-line Representation of Musical Pitch Notation
# by Walter B. Hewlett
# http://www.ccarh.org/publications/reprints/base40/

def mod12(n):
  return n % 12

def note_name(number):
  notes = "C C# D D# E F F# G G# A A# B".split()
  return notes[mod12(number)]

def assert_note_has_name(number,name):
  actualName = note_name(number)
  assert actualName  == name, \
    "%(name)s expected for note %(number)d, found %(actual)s" \
      % {"name": name, "number": number, "actual": actualName}

assert_note_has_name(0,"C")
assert_note_has_name(1,"C#")
assert_note_has_name(13,"C#")
assert_note_has_name(3,"D#")

def accidentals(note_string):
  acc = len(note_string[1:])
  if "#" in note_string:
    return acc
  elif "b" in note_string:
    return -acc
  else:
    return 0

def name_to_number(note_string):
  notes = "C . D . E F . G . A . B".split()
  name = note_string[0:1].upper()
  number = notes.index(name)
  acc = accidentals(note_string)
  return mod12(number + acc)

def assert_name_is_note(name,number):
  actualNumber = name_to_number(name)
  assert actualNumber  == number, \
    "Note %(number)d expected for %(name)s, found %(actual)d" \
      % {"number": number, "name": name, "actual": actualNumber}

# Test each of the value in use in Hewlett's base-40 system [1]
assert_name_is_note("Cbb",  1)
assert_name_is_note("Cb",   2)
assert_name_is_note("C",    3)
assert_name_is_note("C#",   4)
assert_name_is_note("C##",  5)
# -
assert_name_is_note("Dbb",  7)
assert_name_is_note("Db",   8)
assert_name_is_note("D",    9)
assert_name_is_note("D#",  10)
assert_name_is_note("D##", 11)
# -
assert_name_is_note("Ebb", 13)
assert_name_is_note("Eb",  14)
assert_name_is_note("E",   15)
assert_name_is_note("E#",  16)
assert_name_is_note("E##", 17)
assert_name_is_note("Fbb", 18)
assert_name_is_note("Fb",  19)
assert_name_is_note("F",   20)
assert_name_is_note("F#",  21)
assert_name_is_note("F##", 22)
# -
assert_name_is_note("Gbb", 24)
assert_name_is_note("Gb",  25)
assert_name_is_note("G",   26)
assert_name_is_note("G#",  27)
assert_name_is_note("G##", 28)
# -
assert_name_is_note("Abb", 30)
assert_name_is_note("Ab",  31)
assert_name_is_note("A",   32)
assert_name_is_note("A#",  33)
assert_name_is_note("A##", 34)
# -
assert_name_is_note("Bbb", 36)
assert_name_is_note("Bb",  37)
assert_name_is_note("B",   38)
assert_name_is_note("B#",  39)
assert_name_is_note("B##", 40)

print "OK"