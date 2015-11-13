# lsof package spec

declare -r PKG_NAME=lsof-4.89
declare -r PKG_TARBALL=lsof_4.89.tar.xz
declare -r PKG_SRC=lsof_4.89/lsof_4.89_src
declare -r PKG_PATCHES=none
#${PKG_NAME}.patches
declare -r PKG_BUILD_IN_SRC=yes

pkg_configure() {
    export LSOF_CC=${OPT_HOST_SYSTEM}-gcc
    export LSOF_AR="${OPT_HOST_SYSTEM}-ar qv"
    export LSOF_RANLIB=${OPT_HOST_SYSTEM}-ranlib
    $OPTPKG_SRCDIR/$PKG_SRC/Configure -n linux
}

# lsof uses CFLAGS to record all flags :-(

pkg_make() {
    make -j$OPT_PARALLELISM
}

pkg_stage() {
    mkdir -m 0755 -p "${DESTDIR}${OPT_ROOT}/bin"
    cp lsof "${DESTDIR}${OPT_ROOT}/bin"
    mkdir -m 0755 -p "${DESTDIR}${OPT_ROOT}/share/man/man8"
    cp lsof.8 "${DESTDIR}${OPT_ROOT}/share/man/man8"
}
