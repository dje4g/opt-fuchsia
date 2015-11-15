# python3 package spec

declare -r PKG_NAME=python
declare -r PKG_VERSION=3.5.0
declare -r PKG_TARBALL=Python-${PKG_VERSION}.tar.xz
declare -r PKG_SRC=Python-${PKG_VERSION}
declare -r PKG_URL=https://www.python.org/ftp/python/3.5.0/Python-3.5.0.tar.xz
declare -r PKG_SIG=md5sum:d149d2812f10cbe04c042232e7964171
declare -r PKG_NATIVE_ONLY=yes

# TODO(dje):
# checking for /dev/ptmx... not set
# configure: error: set ac_cv_file__dev_ptmx to yes/no in your CONFIG_SITE file when cross compiling

pkg_configure() {
    std_configure \
	--disable-ipv6
}
