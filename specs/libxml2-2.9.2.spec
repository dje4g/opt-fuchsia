# libxml2 package spec
# This package is needed by emacs eww (web browswer in emacs).

declare -r PKG_NAME=libxml2
declare -r PKG_VERSION=2.9.2
declare -r PKG_TARBALL=${PKG_NAME}-${PKG_VERSION}.tar.gz
declare -r PKG_URL=ftp://xmlsoft.org/libxml2/libxml2-2.9.2.tar.gz
declare -r PKG_SIG=md5sum:9e6a9aca9d155737868b3dc5fd82f788
declare -r PKG_PATCHES=${PKG_NAME}-${PKG_VERSION}.patches

pkg_configure() {
    std_configure \
	--with-history
}
