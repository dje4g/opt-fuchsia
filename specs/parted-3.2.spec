# parted package spec

declare -r PKG_NAME=parted
declare -r PKG_VERSION=3.2
declare -r PKG_TARBALL=${PKG_NAME}-${PKG_VERSION}.tar.xz
declare -r PKG_URL=$OPT_URL_GNU/$PKG_NAME/$PKG_TARBALL
declare -r PKG_PATCHES=${PKG_NAME}-${PKG_VERSION}.patches

# libdevmapper not installed, so we need --disable-device-mapper.

pkg_configure() {
    std_configure \
	--disable-device-mapper
}

# musl doesn't define loff_t in same place as glibc

pkg_make() {
    std_make \
	CPPFLAGS='-Dloff_t=off_t'
}
