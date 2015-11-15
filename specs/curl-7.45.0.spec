# curl package spec

declare -r PKG_NAME=curl
declare -r PKG_VERSION=7.45.0
declare -r PKG_TARBALL=${PKG_NAME}-${PKG_VERSION}.tar.bz2
declare -r PKG_URL=http://curl.haxx.se/download/curl-7.45.0.tar.lzma
declare -r PKG_SIG=md5sum:c9a0a77f71fdc6b0f925bc3e79eb77f6

# Since we're cross-compiling we have to explicitly specify things that
# configure would otherwise auto-determine.

pkg_configure() {
    std_configure \
	--with-random=/dev/urandom \
	--with-ca-path=/etc/ssl/certs
}
