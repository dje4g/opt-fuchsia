# db package spec
# Note: this package depends on missing-libc-0.1: sys/queue.h.
# This package was cribbed together and thus does not have a proper
# external url.

declare -r PKG_NAME=db
declare -r PKG_VERSION=1.85
declare -r PKG_TARBALL=${PKG_NAME}.${PKG_VERSION}.patched.tar.gz
declare -r PKG_URL=file:/${OPT_SRC_DIR}/${PKG_TARBALL}
declare -r PKG_SIG=md5sum:493a0ba5a82650c2dbd3af2b8d5593b5
declare -r PKG_SRC=${PKG_NAME}.${PKG_VERSION}
declare -r PKG_PATCHES=${PKG_NAME}.${PKG_VERSION}.patches
declare -r PKG_BUILD_IN_SRC=yes

# There is no configure step.

pkg_configure() {
    :
}

pkg_make() {
    cd PORT/linux
    make -j$OPT_PARALLELISM CC=${OPT_HOST_SYSTEM}-gcc
}

pkg_stage() {
    mkdir -m 0755 -p "${DESTDIR}${OPT_ROOT}/include"
    mkdir -m 0755 -p "${DESTDIR}${OPT_ROOT}/include/sys"
    cp PORT/linux/include/db.h "${DESTDIR}${OPT_ROOT}/include"
    chmod 644 "${DESTDIR}${OPT_ROOT}/include/db.h"
    ln -s db.h "${DESTDIR}${OPT_ROOT}/include/db_185.h"
    cp PORT/linux/include/cdefs.h "${DESTDIR}${OPT_ROOT}/include/sys"
    chmod 644 "${DESTDIR}${OPT_ROOT}/include/sys/cdefs.h"
    mkdir -m 0755 -p "${DESTDIR}${OPT_ROOT}/lib"
    cp PORT/linux/libdb.a "${DESTDIR}${OPT_ROOT}/lib"
    chmod 644 "${DESTDIR}${OPT_ROOT}/lib/libdb.a"
    cp PORT/linux/libdb.so "${DESTDIR}${OPT_ROOT}/lib"
    chmod 755 "${DESTDIR}${OPT_ROOT}/lib/libdb.so"
}
