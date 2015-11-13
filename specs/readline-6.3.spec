# readline

declare -r PKG_NAME=readline-6.3
declare -r PKG_TARBALL=${PKG_NAME}.tar.gz
declare -r PKG_SRC=$PKG_NAME
declare -r PKG_PATCHES=none

# Bleah, readline handles cross-compiling problematically with
# pregenerated autoconf cache files.
# For now, build natively. TODO(dje)
declare -r PKG_NATIVE_ONLY=yes
