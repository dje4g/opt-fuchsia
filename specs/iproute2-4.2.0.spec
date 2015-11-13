# iproute2 package spec

declare -r PKG_NAME=iproute2-4.2.0
declare -r PKG_TARBALL=${PKG_NAME}.tar.xz
declare -r PKG_SRC=${PKG_NAME}
declare -r PKG_PATCHES=${PKG_NAME}.patches
declare -r PKG_BUILD_IN_SRC=yes

# There is no configure step.

pkg_configure() {
    :
}

pkg_make() {
    make \
	CC=${OPT_HOST_SYSTEM}-gcc \
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
	CONFDIR=$OPT_ROOT/etc \
	EXTRA_DEFINES=-DHAVE_MUSL \
	DBM_INCLUDE=${OPT_ROOT}/include
}
