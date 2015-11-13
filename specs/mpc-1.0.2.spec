# Binutils package support

declare -r PKG_NAME=mpc-1.0.2
declare -r PKG_TARBALL=mpc-1.0.2.tar.gz
declare -r PKG_SRC=mpc-1.0.2
declare -r PKG_PATCHES=mpc-1.0.2.patches

pkg_configure() {
    std_configure \
	--with-gmp=$OPT_SYSROOT_ROOT \
	--with-mpfr=$OPT_SYSROOT_ROOT
}
