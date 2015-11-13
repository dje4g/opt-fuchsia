# parted package spec

declare -r PKG_NAME=parted-3.2
declare -r PKG_TARBALL=${PKG_NAME}.tar.xz
declare -r PKG_SRC=${PKG_NAME}
declare -r PKG_PATCHES=${PKG_NAME}.patches

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
