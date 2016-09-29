num = input('')
for x in range(0,num):
	a = [chr(i) for i in range(ord('a'),ord('z')+1)]
	b = raw_input().lower()
	for c in b:
		try:
			a.remove(c)
		except ValueError:
			pass
	if not a:
		print "pangram"
	else:
		s = ""
		for g in a:
			s += g
		print "missing " + s

