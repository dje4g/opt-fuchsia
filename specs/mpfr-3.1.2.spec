# Binutils package support

declare -r PKG_NAME=mpfr-3.1.2
declare -r PKG_TARBALL=mpfr-3.1.2.tar.gz
declare -r PKG_SRC=mpfr-3.1.2
declare -r PKG_PATCHES=mpfr-3.1.2.patches

pkg_configure() {
    std_configure \
	--with-gmp=$OPT_SYSROOT_ROOT
}
