srpm-build:
	spectool -g *.spec
	if [ -f checksum ]; then sha256sum -c checksum; fi;
	rpmbuild -bs *.spec --define "%_sourcedir %{getenv:PWD}" --define "%_srcrpmdir %{getenv:PWD}"

install-deps:
	dnf -y install rpmdevtools

srpm: install-deps srpm-build
	mv *.src.rpm $(outdir)
