# time package spec

declare -r PKG_NAME=man-pages
declare -r PKG_VERSION=4.02
declare -r PKG_TARBALL=${PKG_NAME}-${PKG_VERSION}.tar.xz
declare -r PKG_URL=$OPT_URL_GNU/$PKG_NAME/$PKG_TARBALL
declare -r PKG_SIG=md5sum:6c5692af39eb5fe468a8bd1f110b0edd
declare -r PKG_BUILD_IN_SRC=yes

# There is no configure.

pkg_configure() {
    :
}

# The default make does an install, bleah.

pkg_make() {
    :
}

pkg_stage() {
    make install \
	 prefix=${OPT_ROOT} \
	 "$@"
}
