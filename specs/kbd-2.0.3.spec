# kbd package spec

declare -r PKG_NAME=kbd-2.0.3
declare -r PKG_TARBALL=${PKG_NAME}.tar.xz
declare -r PKG_SRC=${PKG_NAME}
declare -r PKG_PATCHES=${PKG_NAME}.patches

# "check" is only needed by the testsuite, which we can add later.
# "vlock" requires libpam-devel.

pkg_configure() {
    std_configure \
	CHECK_CFLAGS=-I/does-not-exist \
	CHECK_LIBS=-L/does-not-exist \
	--disable-vlock
}
