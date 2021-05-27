test := ../../test/backtracking
interpreter=python3
green='\033[0;32m'
nocol='\033[0m'

all: test

# pylint without docstring warnings (the code is self-explanatory without comment)
pylint:
	@echo -e ${green} Running pylint on iterative and recursive file ${nocol}
	pylint --disable=missing-docstring aqueducte.py
	pylint --disable=missing-docstring aqueducte_recursive.py
	
recursive:
	@echo -e ${green} Running recursive test ${nocol}
	for t in $(test)/*.in; do $(interpreter) aqueducte_recursive.py $$t > sortida; diff -q -w $(test)/`basename $$t .in`.ans sortida; done
	@rm sortida

iterative:
	@echo -e ${green} Running iterative test ${nocol}
	for t in $(test)/*.in; do $(interpreter) aqueducte.py $$t > sortida; diff -q -w $(test)/`basename $$t .in`.ans sortida; done
	@rm sortida

test: iterative recursive pylint
