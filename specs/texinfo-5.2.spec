# texinfo package spec

declare -r PKG_NAME=texinfo-5.2
declare -r PKG_TARBALL=${PKG_NAME}.tar.xz
declare -r PKG_SRC=${PKG_NAME}
declare -r PKG_PATCHES=none
#${PKG_NAME}.patches

# If cross-compiling texinfo builds itself twice.
# Alas it resets the environment when running the second configure:
#  env -i CC="$BUILD_CC" AR="$BUILD_AR" RANLIB="$BUILD_RANLIB"
# and this collides with our use of LD_LIBRARY_PATH to find libgmp,etc.
declare -r PKG_NATIVE_ONLY=yes


# texinfo doesn't recognize --enable-shared.
# This is just std_native_configure with --enable-shared removed.

pkg_configure() {
    $OPTPKG_SRCDIR/$PKG_SRC/configure \
	--build=$OPT_NATIVE_SYSTEM \
	--host=$OPT_NATIVE_SYSTEM \
	--prefix=$OPT_ROOT \
	--disable-nls \
	CFLAGS=-O2 CXXFLAGS=-O2
}
