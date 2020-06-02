def is_anagram(s1,s2):
	s1.sort()
	s2.sort()
	return s1 == s2

s1=list('sapo')
s2=list('posa')
print(is_anagram(s1,s2))