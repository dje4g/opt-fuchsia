# lsof package spec
# TODO: PKG_URL is tarball of tarball

declare -r PKG_NAME=lsof
declare -r PKG_VERSION=4.89
declare -r PKG_TARBALL=${PKG_NAME}_${PKG_VERSION}.tar.xz
declare -r PKG_URL=ftp://sunsite.ualberta.ca/pub/Mirror/lsof/lsof_4.89.tar.bz2
declare -r PKG_SIG=md5sum:1b9cd34f3fb86856a125abbf2be3a386
declare -r PKG_SRC=${PKG_NAME}_${PKG_VERSION}/${PKG_NAME}_${PKG_VERSION}_src
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
