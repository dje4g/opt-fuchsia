# groff package spec

declare -r PKG_NAME=groff-1.22.3
declare -r PKG_TARBALL=${PKG_NAME}.tar.gz
declare -r PKG_SRC=${PKG_NAME}
declare -r PKG_PATCHES=none
#${PKG_NAME}.patches

# groff doesn't use C*FLAGS correctly :-(

pkg_make() {
    make -j$OPT_PARALLELISM
}
