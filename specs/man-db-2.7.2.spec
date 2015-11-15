# man-db package spec

declare -r PKG_NAME=man-db
declare -r PKG_VERSION=2.7.2
declare -r PKG_TARBALL=${PKG_NAME}-${PKG_VERSION}.tar.xz
declare -r PKG_URL=http://download.savannah.gnu.org/releases/man-db/man-db-2.7.4.tar.xz
declare -r PKG_SIG=md5sum:1b400af5b03c7ac44769dbfdd28a86fc

pkg_configure() {
    std_configure \
	--with-browser=${OPT_ROOT}/bin/lynx
}
