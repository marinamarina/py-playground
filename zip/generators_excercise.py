'''In an earlier example that used headers and lines in a text
file to create a list of dictionaries with contact information?
Instead of just adding the dictionaries to a list,
we could use keyword unpacking to pass the arguments to the __init__ method on
 a specially built Contact object that accepts the same set of arguments.
 See if you can adapt the example to make this work.'''

# output list of dictionaries

import sys

out_name = sys.argv[1]
contacts = []

class Contact:
    def __init__(self, first, last, email):
        self.first_name = first
        self.last_name = last
        self.email = email

    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.email



with open(out_name) as outfile:
    header_list = outfile.readline().strip("\n").split(" ")

    # zipping header and lines together
    for l in outfile:
        dict = dict(
            zip(header_list, l.strip("\n").split(" "))
        )
        contact = Contact(**dict)
        contacts.append(contact)

for l in contacts:
    print l.__str__()
