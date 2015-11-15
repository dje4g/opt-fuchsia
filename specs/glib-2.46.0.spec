# glib package spec

declare -r PKG_NAME=glib
declare -r PKG_VERSION=2.46.0
declare -r PKG_TARBALL=${PKG_NAME}-${PKG_VERSION}.tar.xz
declare -r PKG_URL=http://ftp.gnome.org/pub/gnome/sources/glib/2.46/glib-2.46.0.tar.xz
declare -r PKG_SIG=http://ftp.gnome.org/pub/gnome/sources/glib/2.46/glib-2.46.0.sha256sum

# Ouch, we'd rather cross-compile.
declare -r PKG_NATIVE_ONLY=yes
