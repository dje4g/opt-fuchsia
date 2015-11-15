# wget package spec

declare -r PKG_NAME=wget
declare -r PKG_VERSION=1.16.3
declare -r PKG_TARBALL=${PKG_NAME}-${PKG_VERSION}.tar.xz
declare -r PKG_URL=$OPT_URL_GNU/$PKG_NAME/$PKG_TARBALL

# We don't have gnutls (at least not yet).

pkg_configure() {
    std_configure \
	--with-ssl=openssl
}
