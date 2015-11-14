# man-db package spec

declare -r PKG_NAME=man-db-2.7.2
declare -r PKG_TARBALL=${PKG_NAME}.tar.xz
declare -r PKG_SRC=${PKG_NAME}

pkg_configure() {
    std_configure \
	--with-browser=${OPT_ROOT}/bin/lynx
}
