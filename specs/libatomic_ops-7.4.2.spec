# libatomic_ops package spec
# This package is needed by gc-7.4.2.

declare -r PKG_NAME=libatomic_ops
declare -r PKG_VERSION=7.4.2
declare -r PKG_TARBALL=${PKG_NAME}-${PKG_VERSION}.tar.gz
declare -r PKG_URL=http://www.ivmaisoft.com/_bin/atomic_ops/libatomic_ops-7.4.2.tar.gz
declare -r PKG_SIG=1d6538604b314d2fccdf86915e5c0857

pkg_configure() {
    (cd $OPTPKG_SRCDIR/$PKG_SRC && autoreconf -fi)
    std_configure
}
