# automake package spec
# It can be very painful trying to update makefile/configure files with
# versions of automake/autoconf that are way newer than what was originally
# used. This is an older copy to help ease the pain.

declare -r PKG_NAME=automake
declare -r PKG_VERSION=1.11.1
declare -r PKG_TARBALL=${PKG_NAME}-${PKG_VERSION}.tar.bz2
declare -r PKG_URL=$OPT_URL_GNU/$PKG_NAME/$PKG_TARBALL
declare -r PKG_PATCHES=${PKG_NAME}-${PKG_VERSION}.patches

# Install this in a separate directory, just to make sure it doesn't
# collide with a newer version.

pkg_configure() {
    std_configure \
	--prefix="${OPT_ROOT}/lib/${PKG_NAME}"
}
