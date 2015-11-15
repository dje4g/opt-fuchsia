# mpfr package support

declare -r PKG_NAME=mpfr
declare -r PKG_VERSION=3.1.2
declare -r PKG_TARBALL=${PKG_NAME}-${PKG_VERSION}.tar.gz
declare -r PKG_URL=http://www.mpfr.org/mpfr-3.1.3/mpfr-3.1.3.tar.xz
declare -r PKG_SIG=md5sum:6969398cd2fbc56a6af570b5273c56a9
declare -r PKG_PATCHES=${PKG_NAME}-${PKG_VERSION}.patches

pkg_configure() {
    std_configure \
	--with-gmp=$OPT_SYSROOT_ROOT
}
