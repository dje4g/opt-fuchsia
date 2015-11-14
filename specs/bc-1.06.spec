# bc package spec

declare -r PKG_NAME=bc-1.06
declare -r PKG_TARBALL=${PKG_NAME}.tar.gz
declare -r PKG_SRC=${PKG_NAME}

# bc doesn't like C*FLAGS passed on the command line.
# This is std_cross_configure with C*FLAGS moved to env vars.

pkg_configure() {
    CFLAGS=-O2 CXXFLAGS=-O2 \
    $OPTPKG_SRCDIR/$PKG_SRC/configure \
	--build=$OPT_BUILD_SYSTEM \
	--host=$OPT_HOST_SYSTEM \
	--prefix=$OPT_ROOT \
	$OPTPKG_BUILD_SYSROOT_OPTION \
	--disable-nls \
	--enable-shared
}
