#!/bin/python3

import sys


def main():
	q = int(sys.stdin.readline().strip())

	in_stack = []
	out_stack = []
	outputs = []

	def shift_stacks():
		if not out_stack:
			while in_stack:
				out_stack.append(in_stack.pop())

	for _ in range(q):
		query = sys.stdin.readline().split()
		query_type = query[0]

		if query_type == '1':
			in_stack.append(int(query[1]))
		elif query_type == '2':
			shift_stacks()
			out_stack.pop()
		else:  # query_type == '3'
			shift_stacks()
			outputs.append(str(out_stack[-1]))

	sys.stdout.write('\n'.join(outputs))
main()
