# make package spec

declare -r PKG_NAME=make
declare -r PKG_VERSION=3.82
declare -r PKG_TARBALL=${PKG_NAME}-${PKG_VERSION}.tar.bz2
declare -r PKG_URL=$OPT_URL_GNU/$PKG_NAME/$PKG_TARBALL
declare -r PKG_PATCHES=${PKG_NAME}-${PKG_VERSION}.patches
