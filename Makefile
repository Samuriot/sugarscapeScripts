CONFIG = config.json
DATACHECK = data/data.complete
LOGS = log.csv log.json
PLOT = plot.py
PLOTCHECK = plots/plots.complete
RUN = run.py
SCREENSHOTS = *.ps
CUSTOM_CONFIG = config*
TEST_LOG = log_*
SUBMIT = submit*
PREPARE = prepare.sh
SLURM = slurm*

DATASET = $(DATACHECK) \
		data/*[[:digit:]]*.config \
		data/*.csv \
		data/*.json \
		data/*.sh

PLOTS = $(PLOTCHECK) \
		plots/*.png

CLEAN = $(DATASET) \
		$(LOGS) \
		$(PLOTS) \
		$(SCREENSHOTS) \
		$(TEST_LOG) \
		$(CUSTOM_CONFIG) \
		$(SUBMIT) \
		$(SLURM)

# Change to python3 (or other alias) if needed
PYTHON = python3
SUGARSCAPE = sugarscape.py

# Check for local Python aliases
PYCHECK = $(shell which python > /dev/null; echo $$?)
PY3CHECK = $(shell which python3 > /dev/null; echo $$?)

$(DATACHECK):
	cd data && $(PYTHON) $(RUN) --conf ../$(CONFIG) --mode csv
	touch $(DATACHECK)

$(PLOTCHECK): $(DATACHECK)
	cd plots && $(PYTHON) $(PLOT) --path ../data/ --conf ../$(CONFIG)
	touch $(PLOTCHECK)

all: $(DATACHECK) $(PLOTCHECK)

data: $(DATACHECK)

plots: $(PLOTCHECK)

seeds:
	cd data && $(PYTHON) $(RUN) --conf ../$(CONFIG) --mode csv --seeds

setup:
	@echo "Checking for local Python installation."
ifeq ($(PY3CHECK), 0)
	@echo "Found alias for Python."
	sed -i 's/PYTHON = python$$/PYTHON = python3/g' Makefile
	sed -i 's/"python"/"python3"/g' $(CONFIG)
else ifneq ($(PYCHECK), 0)
	@echo "Could not find a local Python installation."
	@echo "Please update the Makefile and configuration file manually."
else
	@echo "This message should never be reached."
endif

test:
	$(PYTHON) $(SUGARSCAPE) --conf $(CONFIG)

research:
	chmod u+x script
	chmod u+x prepare.sh
	./prepare.sh

plot:
	chmod u+x prepare_plot.sh
	chmod u+x plot_average.sh
	./prepare_plots.sh
	./plot_average.sh

clean:
	rm -rf $(CLEAN) || true

lean:
	rm -rf $(PLOTS) || true

.PHONY: all clean data lean plots setup

# vim: set noexpandtab tabstop=4:
