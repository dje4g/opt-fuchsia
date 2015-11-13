# curl package spec

declare -r PKG_NAME=ssmtp-2.64
declare -r PKG_TARBALL=${PKG_NAME}.tar.bz2
declare -r PKG_SRC=${PKG_NAME}
declare -r PKG_PATCHES=${PKG_NAME}.patches
#declare -r PKG_BUILD_IN_SRC=yes

# ssmtp configure doesn't like passing CFLAGS on the command line.
# Pass it in env vars instead.
# configure doesn't check for ${host}-gcc either.

pkg_configure() {
    CC=${OPT_HOST_SYSTEM}-gcc \
    CFLAGS=-O2 \
    $OPTPKG_SRCDIR/$PKG_SRC/configure \
	--build=$OPT_BUILD_SYSTEM \
	--host=$OPT_HOST_SYSTEM \
	--prefix=$OPT_ROOT \
	$OPTPKG_BUILD_SYSROOT_OPTION \
	--disable-nls \
	--enable-shared \
	--enable-ssl
}

# ssmtp doesn't use C*FLAGS correctly :-(

pkg_make() {
    make -j$OPT_PARALLELISM \
	LDFLAGS=-lcrypto
}
