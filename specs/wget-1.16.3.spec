# wget package spec

declare -r PKG_NAME=wget-1.16.3
declare -r PKG_TARBALL=${PKG_NAME}.tar.xz
declare -r PKG_SRC=${PKG_NAME}

# We don't have gnutls (at least not yet).

pkg_configure() {
    std_configure \
	--with-ssl=openssl
}
