# setuptools package spec
# This is, I think, needed to install mako.

declare -r PKG_NAME=setuptools
declare -r PKG_VERSION=18.4
declare -r PKG_TARBALL=${PKG_NAME}-${PKG_VERSION}.tar.gz
declare -r PKG_URL=file:$OPT_ROOT/src/tarballs/$PKG_TARBALL
declare -r PKG_SIG=md5sum:214c6c43bd7035e870c1beab402c48e7
