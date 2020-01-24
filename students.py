# coding: utf-8
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

from git_call import git_remote_add_FakeClass

STUDENTS = [
'victor-estrade',
# 'Didayolo', # Adrien
# 'herilalaina', # Heri
]

def main():
	for remote in STUDENTS:
		try:
			git_remote_add_FakeClass(remote)
		except AssertionError as e:
			print(e)

if __name__ == '__main__':
	main()