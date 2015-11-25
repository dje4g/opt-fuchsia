# net-tools package spec

declare -r PKG_NAME=net-tools
declare -r PKG_VERSION=cvs-20101030
# PKG_ORIG_VERSION is local to this file
declare -r PKG_ORIG_VERSION=CVS_20101030
declare -r PKG_TARBALL=${PKG_NAME}-${PKG_ORIG_VERSION}.tar.gz
declare -r PKG_URL=ftp://anduin.linuxfromscratch.org/BLFS/net-tools/net-tools-CVS_20101030.tar.gz
declare -r PKG_SIG=md5sum:6be14ed473cacdd68edeaa9605adc469
declare -r PKG_SRC=${PKG_NAME}-${PKG_ORIG_VERSION}
declare -r PKG_PATCHES=${PKG_NAME}-${PKG_VERSION}.patches
declare -r PKG_BUILD_IN_SRC=yes

# The "configure" step is a bit odd.
# See http://www.linuxfromscratch.org/blfs/view/svn/basicnet/net-tools.html.
# "make config" has been run once manually and the result saved.

pkg_configure() {
    :
}

pkg_make() {
    std_make \
	CC=${OPT_HOST_SYSTEM}-gcc \
	CFLAGS="-g -O2 -DHAVE_MUSL"
}

pkg_stage() {
    make update \
	BASEDIR=${DESTDIR}${OPT_ROOT} \
	mandir=/share/man
}
