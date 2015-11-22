# bzip2 package spec

declare -r PKG_NAME=bzip2
declare -r PKG_VERSION=1.0.6
declare -r PKG_TARBALL=${PKG_NAME}-${PKG_VERSION}.tar.gz
declare -r PKG_URL=http://www.bzip.org/1.0.6/bzip2-1.0.6.tar.gz
declare -r PKG_SIG=md5sum:00b516f4704d4a7cb50a1d97e6e8e15b
declare -r PKG_BUILD_IN_SRC=yes

# bzip2 doesn't have a configure script

pkg_configure() {
    cd ${OPTPKG_SRCDIR}/${PKG_SRC}
    make clean
}

pkg_make() {
    std_make \
	CC=${OPT_HOST_SYSTEM}-gcc \
	AR=${OPT_HOST_SYSTEM}-ar \
	RANLIB=${OPT_HOST_SYSTEM}-ranlib
}

pkg_stage() {
    std_stage \
	PREFIX="\$(DESTDIR)/${OPT_ROOT}" \
	"$@"
}
