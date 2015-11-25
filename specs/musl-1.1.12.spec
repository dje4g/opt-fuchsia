# musl package spec
# This is present for testing purposes.
# As such it is installed in $OPT_ROOT/test.

declare -r PKG_NAME=musl
declare -r PKG_VERSION=1.1.12
declare -r PKG_TARBALL=${PKG_NAME}-${PKG_VERSION}.tar.gz
declare -r PKG_URL=http://www.musl-libc.org/releases/musl-1.1.12.tar.gz
declare -r PKG_SUM=http://www.musl-libc.org/releases/musl-1.1.12.tar.gz.asc
#declare -r PKG_PATCHES=${PKG_NAME}-${PKG_VERSION}.patches
declare -r PKG_BUILD_IN_SRC=yes

# This is std_cross_configure with --prefix set to $OPT_ROOT/test

pkg_configure() {
    CROSS_COMPILE=${OPT_HOST_SYSTEM}- \
    $OPTPKG_SRCDIR/$PKG_SRC/configure \
	--build=$OPT_BUILD_SYSTEM \
	--host=$OPT_HOST_SYSTEM \
	--prefix=$OPT_ROOT/test \
	$OPTPKG_BUILD_SYSROOT_OPTION \
	--disable-nls \
	--enable-shared \
	CFLAGS="-g -O2" CXXFLAGS="-g -O2"
}
