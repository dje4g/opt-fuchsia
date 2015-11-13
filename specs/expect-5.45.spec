# expect package spec

declare -r PKG_NAME=expect-5.45
declare -r PKG_TARBALL=expect5.45.tar.gz
declare -r PKG_SRC=expect5.45
declare -r PKG_PATCHES=${PKG_NAME}.patches

# expect can't be cross-compiled
declare -r PKG_NATIVE_ONLY=yes

# expect puts SHLIB_CFLAGS in CFLAGS :-(

pkg_make() {
    make -j$OPT_PARALLELISM
}
