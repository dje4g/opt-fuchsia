# readline

declare -r PKG_NAME=readline
declare -r PKG_VERSION=6.3
declare -r PKG_TARBALL=${PKG_NAME}-${PKG_VERSION}.tar.gz
declare -r PKG_URL=$OPT_URL_GNU/$PKG_NAME/$PKG_TARBALL

# Bleah, readline handles cross-compiling problematically with
# pregenerated autoconf cache files.
# For now, build natively. TODO(dje)
declare -r PKG_NATIVE_ONLY=yes
