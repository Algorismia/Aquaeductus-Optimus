CC=g++
CFLAGS=-pedantic -Wall  -O3
test := ../../test/dynamic
green='\033[0;32m'
nocol='\033[0m'

all: aqueducte

aqueducte: aqueducte.cpp
	$(CC) $(CFLAGS) -o $@ $^

test: aqueducte
	@echo -e ${green} Running iterative test ${nocol}
	for t in $(test)/*.in; do ./aqueducte $$t > sortida; diff -q $(test)/`basename $$t .in`.ans sortida; done
	rm sortida

clean:
	rm -rf aqueducte sortida
