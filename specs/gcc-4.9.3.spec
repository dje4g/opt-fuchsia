# gcc package support

declare -r PKG_NAME=gcc-4.9.3
declare -r PKG_TARBALL=${PKG_NAME}.tar.gz
declare -r PKG_SRC=${PKG_NAME}
declare -r PKG_PATCHES=${PKG_NAME}.patches

# gcc's configure is extra complicated, so use our own version.
# gcc 4.9.? has a bug where not specifying --target (when it should
# default from --host) doesn't work.
# TODO(dje): We want to cross compile, but on a fuchsia system it's simpler
# to build a native toolchain. Revisit.
# TODO(dje): A sysroot of /. is perhaps a wart, but I don't mind it.
# TODO(dje): gcc has --with-build-sysroot, needed?

pkg_configure() {
    $OPTPKG_SRCDIR/$PKG_SRC/configure \
	--build=$OPT_BUILD_SYSTEM \
	--host=$OPT_BUILD_SYSTEM \
	--target=$OPT_HOST_SYSTEM \
	--prefix=$OPT_ROOT \
	--with-sysroot=/. \
	--with-local-prefix=$OPT_ROOT \
	--disable-nls \
	--enable-shared \
	--disable-werror \
	--enable-languages=c,c++ \
	--disable-libmudflap \
	--disable-libsanitizer \
	--disable-multilib \
	--with-gmp=$OPT_SYSROOT_ROOT \
	--with-mpfr=$OPT_SYSROOT_ROOT \
	--with-mpc=$OPT_SYSROOT_ROOT

    # GCC needs to see /usr/include.
    # TODO(dje): Cross builds from linux.
    # TODO(dje): Needed any more (with sysroot=/)?
    #rm -f $OPT_SYSROOT_DIR/lib
    #rm -f $OPT_SYSROOT_DIR/usr
    #/bin/ln -s /lib $OPT_SYSROOT_DIR/lib
    #/bin/ln -s /usr $OPT_SYSROOT_DIR/usr
}

# Note: binutils,gmp,mpfr,mpc need to be installed for "native"
# builds. Otherwise, for gmp,mpfr,mpc we'll need to augment LD_LIBRARY_PATH
# here (beyond having $OPT_ROOT/lib in it).
