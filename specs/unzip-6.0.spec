# unzip package spec

declare -r PKG_NAME=unzip
declare -r PKG_VERSION=6.0
declare -r PKG_TARBALL=${PKG_NAME}60.tar.gz
declare -r PKG_URL=http://iweb.dl.sourceforge.net/project/infozip/UnZip%206.x%20%28latest%29/UnZip%206.0/unzip60.tar.gz
declare -r PKG_SIG=md5sum:62b490407489521db863b523a7f86375
declare -r PKG_SRC=${PKG_NAME}60
declare -r PKG_BUILD_IN_SRC=yes

# There is no configure step.

pkg_configure() {
    :
}

pkg_make() {
    std_make \
	-f unix/Makefile generic
}

pkg_stage() {
    make -f unix/Makefile install \
	 prefix=${DESTDIR}${OPT_ROOT} \
	 MANDIR=${DESTDIR}${OPT_ROOT}/share/man/man1
}
