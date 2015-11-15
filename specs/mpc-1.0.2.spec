# mpc package support

declare -r PKG_NAME=mpc
declare -r PKG_VERSION=1.0.2
declare -r PKG_TARBALL=${PKG_NAME}-${PKG_VERSION}.tar.gz
declare -r PKG_URL=http://www.multiprecision.org/mpc/download/mpc-1.0.3.tar.gz
declare -r PKG_SIG=md5sum:d6a1d5f8ddea3abd2cc3e98f58352d26
declare -r PKG_PATCHES=${PKG_NAME}-${PKG_VERSION}.patches

pkg_configure() {
    std_configure \
	--with-gmp=$OPT_SYSROOT_ROOT \
	--with-mpfr=$OPT_SYSROOT_ROOT
}
