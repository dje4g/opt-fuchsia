# autoconf package spec
# It can be very painful trying to update makefile/configure files with
# versions of automake/autoconf that are way newer than what was originally
# used. This is an older copy to help ease the pain.

declare -r PKG_NAME=autoconf-2.64
declare -r PKG_TARBALL=${PKG_NAME}.tar.xz
declare -r PKG_SRC=${PKG_NAME}
declare -r PKG_PATCHES=${PKG_NAME}.patches

# Install this in a separate directory, otherwise the "share" directories
# collide.

pkg_configure() {
    std_configure \
	--prefix="${OPT_ROOT}/lib/${PKG_NAME}"
}
