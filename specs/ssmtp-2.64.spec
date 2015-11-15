# curl package spec

declare -r PKG_NAME=ssmtp
declare -r PKG_VERSION=2.64
declare -r PKG_TARBALL=${PKG_NAME}_${PKG_VERSION}.orig.tar.bz2
declare -r PKG_URL=http://mirrors.kernel.org/debian/pool/main/s/ssmtp/ssmtp_2.64.orig.tar.bz2
declare -r PKG_SIG=md5sum:65b4e0df4934a6cd08c506cabcbe584f
declare -r PKG_PATCHES=${PKG_NAME}-${PKG_VERSION}.patches
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
