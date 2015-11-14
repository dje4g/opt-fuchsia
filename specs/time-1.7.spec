# time package spec

declare -r PKG_NAME=time-1.7
declare -r PKG_TARBALL=${PKG_NAME}.tar.gz
declare -r PKG_SRC=${PKG_NAME}

# time configure doesn't like passing CFLAGS on the command line.
# Pass it in env vars instead.

pkg_configure() {
    CFLAGS=-O2 \
    $OPTPKG_SRCDIR/$PKG_SRC/configure \
	--build=$OPT_BUILD_SYSTEM \
	--host=$OPT_HOST_SYSTEM \
	--prefix=$OPT_ROOT \
	$OPTPKG_BUILD_SYSROOT_OPTION \
	--disable-nls \
	--enable-shared
}
