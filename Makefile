.PHONY: test
test: test_simple_programming_problems test_programming_practice_problems

test_simple_programming_problems:
	cd simple_programming_problems && $(MAKE) test

test_programming_practice_problems:
	cd programming_practice_problems && $(MAKE) test
