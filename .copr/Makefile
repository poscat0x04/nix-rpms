srpm-build:
	dnf -y install rpmdevtools
	spectool -g *.spec
	sha256sum -c checksum
	rpmbuild -bs *.spec --define "%_sourcedir %{getenv:PWD}" --define "%_srcrpmdir %{getenv:PWD}"

srpm: srpm-build
	mv *.src.rpm $(outdir)
