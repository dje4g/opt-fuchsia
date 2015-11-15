# expect package spec

declare -r PKG_NAME=expect
declare -r PKG_VERSION=5.45
declare -r PKG_TARBALL=${PKG_NAME}${PKG_VERSION}.tar.gz
declare -r PKG_URL=http://prdownloads.sourceforge.net/expect/expect5.45.tar.gz
declare -r PKG_SIG=md5sum:44e1a4f4c877e9ddc5a542dfa7ecc92b
declare -r PKG_SRC=${PKG_NAME}${PKG_VERSION}
declare -r PKG_PATCHES=${PKG_NAME}.patches

# expect can't be cross-compiled
declare -r PKG_NATIVE_ONLY=yes

# expect puts SHLIB_CFLAGS in CFLAGS :-(

pkg_make() {
    make -j$OPT_PARALLELISM
}
