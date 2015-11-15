# gdbm package spec

declare -r PKG_NAME=gdbm
declare -r PKG_VERSION=1.11
declare -r PKG_TARBALL=${PKG_NAME}-${PKG_VERSION}.tar.gz
declare -r PKG_URL=$OPT_URL_GNU/$PKG_NAME/$PKG_TARBALL

pkg_configure() {
    std_configure \
	--enable-libgdbm-compat
}
