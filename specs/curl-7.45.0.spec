# curl package spec

declare -r PKG_NAME=curl-7.45.0
declare -r PKG_TARBALL=${PKG_NAME}.tar.bz2
declare -r PKG_SRC=${PKG_NAME}

# Since we're cross-compiling we have to explicitly specify things that
# configure would otherwise auto-determine.

pkg_configure() {
    std_configure \
	--with-random=/dev/urandom \
	--with-ca-path=/etc/ssl/certs
}
