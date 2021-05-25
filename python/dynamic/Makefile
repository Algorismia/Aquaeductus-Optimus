test := ../../test/dynamic
interpreter=python3

all: test

# pylint without docstring warnings (the code is self-explanatory without comment)
pylint:
	pylint --disable=missing-docstring aqueducte.py

iterative:
	for t in $(test)/*.in; do $(interpreter) aqueducte.py $$t > sortida; diff -q -w $(test)/`basename $$t .in`.ans sortida; done
	rm sortida

test: iterative pylint

clean:
	rm -rf sortida
