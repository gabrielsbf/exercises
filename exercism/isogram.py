def is_isogram(string):
	string = str(string).lower()
	string_removed = list(filter(lambda x : not x == " " and not x == "-", list(string)))
	result = len(string_removed) == len(set(string_removed))
	return result



is_isogram("abc -- kçhd")
