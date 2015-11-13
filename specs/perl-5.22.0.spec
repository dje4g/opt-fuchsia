# perl package spec

declare -r PKG_NAME=perl-5.22.0
declare -r PKG_TARBALL=${PKG_NAME}.tar.gz
declare -r PKG_SRC=${PKG_NAME}
declare -r PKG_PATCHES=none
#${PKG_NAME}.patches
declare -r PKG_BUILD_IN_SRC=yes

# perl has a differently named configure script, bleah

pkg_configure() {
    # For perl CC,CFLAGS have to be passed in as env vars.
    CC=${OPT_HOST_SYSTEM}-gcc \
    CFLAGS=-O2 \
    $OPTPKG_SRCDIR/$PKG_SRC/configure.gnu \
	--prefix=$OPT_ROOT
}
