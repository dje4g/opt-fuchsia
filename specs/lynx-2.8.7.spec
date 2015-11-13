# lynx package spec

declare -r PKG_NAME=lynx-2.8.7
declare -r PKG_TARBALL=lynx2.8.7rel.2.tar.gz
declare -r PKG_SRC=lynx2-8-7
declare -r PKG_PATCHES=${PKG_NAME}.patches

# lynx's configure won't look for openssl unless we explicitly tell it
# to use pkg-config.

pkg_configure() {
    std_configure \
	--enable-default-colors \
	--with-pkg-config \
	--with-ssl
}

# lynx tries to use C*FLAGS correctly, but doesn't quite get it right.
# The bug is buried in WWW/Library/Implementation/makefile IIUC.

pkg_make() {
    make -j$OPT_PARALLELISM
}

pkg_stage() {
    std_stage \
	install-doc install-help
}
