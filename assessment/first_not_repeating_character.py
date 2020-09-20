def first_not_repeating_character(s):
	for letter in s: # traverse
        # if the first occurrence is also the last occurence then it's the only occurrence
		if s.find(letter) == s.rfind(letter): # search for letters - (find = first occurence; rfind = last occurence)
			return letter

	return '_' # no such character