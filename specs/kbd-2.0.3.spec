# kbd package spec

declare -r PKG_NAME=kbd
declare -r PKG_VERSION=2.0.3
declare -r PKG_TARBALL=${PKG_NAME}-${PKG_VERSION}.tar.xz
declare -r PKG_URL=https://www.kernel.org/pub/linux/utils/kbd/kbd-2.0.3.tar.xz
declare -r PKG_SIG=md5sum:231b46e7142eb41ea3ae06d2ded3c208
declare -r PKG_PATCHES=${PKG_NAME}-${PKG_VERSION}.patches

# "check" is only needed by the testsuite, which we can add later.
# "vlock" requires libpam-devel.

pkg_configure() {
    std_configure \
	CHECK_CFLAGS=-I/does-not-exist \
	CHECK_LIBS=-L/does-not-exist \
	--disable-vlock
}
