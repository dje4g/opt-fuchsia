# gc package spec
# This package is needed by w3m-0.5.3.

declare -r PKG_NAME=gc
declare -r PKG_VERSION=7.4.2
declare -r PKG_TARBALL=${PKG_NAME}-${PKG_VERSION}.tar.gz
declare -r PKG_URL=http://www.hboehm.info/gc/gc_source/gc-7.4.2.tar.gz
declare -r PKG_SIG=md5sum:12c05fd2811d989341d8c6d81f66af87
declare -r PKG_PATCHES=${PKG_NAME}-${PKG_VERSION}.patches

pkg_configure() {
    (cd $OPTPKG_SRCDIR/$PKG_SRC && autoreconf -fi)
    std_configure \
	--enable-cplusplus
}
