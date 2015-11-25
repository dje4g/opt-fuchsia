# iproute2 package spec

declare -r PKG_NAME=iproute2
declare -r PKG_VERSION=4.2.0
declare -r PKG_TARBALL=${PKG_NAME}-${PKG_VERSION}.tar.xz
declare -r PKG_URL=https://www.kernel.org/pub/linux/utils/net/iproute2/iproute2-4.3.0.tar.xz
declare -r PKG_SIG=md5sum:1a2bbb80cfc7ab3f3e987e18b3207c2f
declare -r PKG_PATCHES=${PKG_NAME}-${PKG_VERSION}.patches
declare -r PKG_BUILD_IN_SRC=yes

# There is no configure step.

pkg_configure() {
    :
}

pkg_make() {
    make -j$OPT_PARALLELISM \
	CC=${OPT_HOST_SYSTEM}-gcc \
	CCOPTS="-g -O2" \
	AR=${OPT_HOST_SYSTEM}-ar \
	PREFIX=$OPT_ROOT \
	CONFDIR=${OPT_ROOT}/etc \
	EXTRA_DEFINES=-DHAVE_MUSL \
	DBM_INCLUDE=${OPT_ROOT}/include
}

pkg_stage() {
    make install \
	DESTDIR=$DESTDIR \
	CC=${OPT_HOST_SYSTEM}-gcc \
	AR=${OPT_HOST_SYSTEM}-ar \
	PREFIX=$OPT_ROOT \
	SBINDIR=$OPT_ROOT/sbin \
	CONFDIR=$OPT_ROOT/etc/iproute2 \
	ARPDDIR=$OPT_ROOT/var/lib/arpd \
	EXTRA_DEFINES=-DHAVE_MUSL \
	DBM_INCLUDE=${OPT_ROOT}/include
}
