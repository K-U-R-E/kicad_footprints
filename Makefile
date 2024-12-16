
compile:
		@python3 scripts/compile.py symbols/ pid_kicad.kicad_sym

decompile:
		@python3 scripts/decompile.py pid_kicad.kicad_sym symbols/

plot:
	@python3 scripts/plot.py symbols/ plots/

precommit:
	@python3 scripts/precommit.py pid_kicad.kicad_sym symbols/
