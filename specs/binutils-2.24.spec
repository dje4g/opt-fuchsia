# binutils package spec

declare -r PKG_NAME=binutils-2.24
declare -r PKG_TARBALL=${PKG_NAME}.tar.gz
declare -r PKG_SRC=${PKG_NAME}
declare -r PKG_PATCHES=none

# --disable-werror shouldn't be needed for binutils releases.
# Provide it anyway "just in case".

# TODO(dje): A sysroot of /. is perhaps a wart, but I don't mind it.

# binutils doesn't provide the --with-local-prefix option that gcc does. :-(
# The value for lib-path was created by looking at the non-lib-path case
# and replacing /usr/local with $OPT_ROOT, but putting /lib,/usr/lib ahead
# of $OPT_ROOT/lib.

pkg_configure() {
    ${OPTPKG_SRCDIR}/${PKG_SRC}/configure \
	--build=$OPT_BUILD_SYSTEM \
	--host=$OPT_BUILD_SYSTEM \
	--target=$OPT_HOST_SYSTEM \
	--prefix=$OPT_ROOT \
	--disable-nls \
	--enable-shared \
	--disable-werror \
	--with-sysroot=/. \
	--with-lib-path="${OPT_ROOT}/${OPT_HOST_SYSTEM}/lib64:/lib64:/usr/lib64:${OPT_ROOT}/lib64:/lib:/usr/lib:${OPT_ROOT}/lib" \
	CFLAGS=-O2 CXXFLAGS=-O2
}
