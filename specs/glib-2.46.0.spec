# glib package spec

declare -r PKG_NAME=glib-2.46.0
declare -r PKG_TARBALL=${PKG_NAME}.tar.xz
declare -r PKG_SRC=${PKG_NAME}
declare -r PKG_PATCHES=none
#${PKG_NAME}.patches
# Ouch, we'd rather cross-compile.
declare -r PKG_NATIVE_ONLY=yes
