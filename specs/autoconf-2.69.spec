# autoconf package spec

declare -r PKG_NAME=autoconf
decoare -r PKG_VERSION=2.69
declare -r PKG_TARBALL=${PKG_NAME}-${PKG_VERSION}.tar.xz
declare -r PKG_URL=$OPT_URL_GNU/$PKG_NAME/$PKG_TARBALL
declare -r PKG_PATCHES=${PKG_NAME}-${PKG_VERSION}.patches
