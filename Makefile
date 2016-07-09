PROJECT=cryptococcus
TESTDIR=testing_folder

develop:
	pip install -e .

test:
	mkdir -p $(TESTDIR)
	cd $(TESTDIR); python -c "import $(PROJECT); $(PROJECT).test()"
	rm -r $(TESTDIR)

coverage:
	mkdir -p $(TESTDIR)
	cd $(TESTDIR); python -c "import $(PROJECT); $(PROJECT).test(coverage=True, verbose=True)"
	rm -r $(TESTDIR)

pep8:
	pep8 --show-source $(PROJECT)

clean:
	find . -name "*.pyc" -exec rm -v {} \;
	rm -rvf dist MANIFEST *.egg-info __pycache__ .coverage .cache
	rm -rvf $(TESTDIR)
