
compile:
		@python3 scripts/compile.py symbols/ pid_kicad.kicad_sym

decompile:
		@python3 scripts/decompile.py pid_kidcad.kicad_sym symbols/

plot:
	@python3 scripts/plot.py pid_kicad.kicad_sym plots/
