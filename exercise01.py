#!/usr/bin/env python

# Exercise 1.
# Extend the function name_to_number
# to deal with notes with mixed flats and sharps

def mod12(n):
    return n % 12

def note_name(number):
    notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    return notes[mod12(number)]

def assert_note_has_name(number,name):
    actual_name = note_name(number)
    assert actual_name == name, (
        "%(name)s expected for note %(number)d, found %(actual)s" %
        {"name": name, "number": number, "actual": actual_name}
    )

assert_note_has_name(0,"C")
assert_note_has_name(1,"C#")
assert_note_has_name(13,"C#")
assert_note_has_name(3,"D#")

def name_to_number(note_string):
    notes = ["C", ".", "D", ".", "E", "F", ".", "G", ".", "A", ".", "B"]
    name = note_string[0:1].upper()
    number = notes.index(name)
    for accidental in note_string[1:]:
        if accidental == "#":
            number += 1
        elif accidental == "b":
            number -= 1
    return mod12(number)

def assert_name_is_note(name,number):
  actual_number = name_to_number(name)
  assert actual_number == number, (
      "Note %(number)d expected for %(name)s, found %(actual)d" %
      {"number": number, "name": name, "actual": actual_number}
  )

assert_name_is_note("C#",1)
assert_name_is_note("Db",1)
assert_name_is_note("Ebb",2)
assert_name_is_note("B#",0)

assert_name_is_note("C#b#",1)

print "OK"
