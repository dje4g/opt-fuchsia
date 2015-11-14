# gdbm package spec

declare -r PKG_NAME=gdbm-1.11
declare -r PKG_TARBALL=${PKG_NAME}.tar.gz
declare -r PKG_SRC=${PKG_NAME}

pkg_configure() {
    std_configure \
	--enable-libgdbm-compat
}
