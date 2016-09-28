'''
Motherfucking Git
'''

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Get details about the cat before starting the story

# -----------------------------
# CAT ADVENTURE GAME
# -----------------------------

# Welcome Screen

print bcolors.BOLD + "\n\nHELLO FRIEND\n" + bcolors.ENDC
print """
-------------------------------------------------

      Make Decisions + Answer Questions
                CAT ADVENTURE 
            Different Everytime!
            
-------------------------------------------------           
      """
print "Let's get started\n"

print "\nThere once was a cat named?\n"
cat_name = raw_input("What was the cat's name: ")

# add check for valid input

print "\n%s was a _______ cat.\n" % cat_name
cat_breed = raw_input("What kind of cat was it: ")

print "\n%s has ______ fur\n" % cat_name
cat_fur = raw_input("What color fur did the cat have: ")


print """
Is %s a girl cat or a boy cat?
1 : Girl
2 : Boy
	""" %cat_name

girl_boy = raw_input(">> ")

if girl_boy == "2":
	he_she = "he"
	his_her ="his"
	him_her = "him"

else:
	he_she = "she"
	his_her = "her"
	him_her = "her"


print "\nThere once was a %s cat with %s fur named %s." % (cat_breed, cat_fur, cat_name) 
print "%s lost something special. Will you help %s find it?\n" % (cat_name, him_her) 

print """
1 : Yes
2 : No

	"""

cat_start = raw_input(">> ")

if cat_start == "2":
	print "\nThank You, Come Again.\n" 

else:
	print "\n%s has lost %s favorite ball." % (cat_name, his_her)
	
	print """
%s is an adventurous cat. %s travels 
both inside and outside %s house.

Where should we begin our search for %s's ball?
1 : Inside
2 : Outside

		""" % (cat_name, he_she, his_her, cat_name)

inside = ["kitchen", "bathroom", "bedroom", "dining"]
outside = ["tree", "bush", "car", "nyc"]


rooms = {
		"kitchen" : ["sink", "cabinet", "fridge", "stove"],
		"bathroom" : ["toliet", "tub", "soap"],
		"bedroom" : ["bed", "closet", "stairs", "dresser"],
		"dining" : ["table", "bowl", "chandalier"],
		# ------ outside
		"tree" : ["leaf", "apple", "branch", "nest"],
		"bush" : ["toliet", "tub", "soap"],
		"car" : ["bed", "closet", "stairs", "dresser"],
		"nyc" : ["table", "bowl", "chandalier"]
		}

# --- add outside
places = {	# ----- kitchen
			"sink" : "Under the sink you see ...",
			"cabinet" : "In the cabinet you see ...",
			"fridge" : "Under the refridgerator you see ...",
			"stove" : "Under the stove you see ...",
			# ----- bathroom
			"toliet" : "Behind the toliet you see...",
			"tub" : "In the bathtub you will see...",
			"soap" : "Looking inside the soap bottle you see ...",
			# ----- bedroom
			"bed" : "Under the bed you see...",
			"closet" : "Inside the closet you find",
			"stairs" : "Behind the bedroom stairs you find...",
			"dresser" : "Under the dresser you find...",
			# ----- dining
			"table" : "Under the dining room table you see..",
			"bowl" : "In the bowl on the dining room table you find...",
			"chandalier" : "Hanging from the chandalier you see...",
			# -----------------OUTSIDE
			# -----------
			"leaf" : "up in the tree you see..."
		} 

# -------------------------------
# print inside locations aka rooms
# --------------------------------

def inside_outside(in_or_out):
	if in_or_out == 1:
		location = inside
		print "\nSelect a room to search for %s's ball\n" % cat_name
	else: 
		location = outside
		print "\nWhere should we look for %s's ball\n" % cat_name


	e = 1
	for item in location:
		print "%s : %s" % (e, item)
		e = e +1
	print "%s : back" % e
	print "\n"

	room_choice = int(raw_input(">> "))
	room_choosen(room_choice, location)

# ------------------------
# user guess
# -----------------------

def guess(look_here, room_selected):
	look_here = look_here -1
	reveal = rooms[room_selected][look_here]
	print "\n"
	print places[reveal]
	print "\n"
	# -----------------
	# or if winner!!!
	#------------------

# ---------------------------
# print selected room items
# ask for guess 
# ---------------------------
def room_display(room_selected):
	print "\nWhere should we look for %s's ball\n" % cat_name
	i = 1
	for val in rooms.get(room_selected):
		print "%s : %s" % (i , val)
		i = i + 1
	print "%s : back" % i
	print "\n"

	look_here = int(raw_input(">> "))
	guess(look_here, room_selected)
	# Add verification
	
# ------------------------------
# parse user input - room choice
# feed function above room_display
# -------------------------------
def room_choosen (room_choice, location):
	# print "messy"
	# print "room choice %s" % room_choice
	# print "location %s" % location
	room_choice = room_choice -1
	# print location[room_choice]
	room_selected = location[room_choice]
	# print room_selected 
	room_display(room_selected)

# ------------
# user input
# -------------

in_or_out = int(raw_input(">> "))
inside_outside(in_or_out)



