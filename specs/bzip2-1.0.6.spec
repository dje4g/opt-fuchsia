# bzip2 package spec

declare -r PKG_NAME=bzip2-1.0.6
declare -r PKG_TARBALL=${PKG_NAME}.tar.gz
declare -r PKG_SRC=${PKG_NAME}
declare -r PKG_PATCHES=none
#${PKG_NAME}.patches
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
	PREFIX="\$(DESTDIR)/${OPT_ROOT}"
}
