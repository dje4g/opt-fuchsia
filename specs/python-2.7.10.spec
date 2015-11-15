# python2 package spec

declare -r PKG_NAME=python
declare -r PKG_VERSION=2.7.10
declare -r PKG_TARBALL=Python-${PKG_VERSION}.tar.xz
declare -r PKG_SRC=Python-${PKG_VERSION}
declare -r PKG_URL=https://www.python.org/ftp/python/2.7.10/Python-2.7.10.tar.xz
declare -r PKG_SIG=md5sum:c685ef0b8e9f27b5e3db5db12b268ac6
declare -r PKG_NATIVE_ONLY=yes

# TODO(dje):
# checking for /dev/ptmx... not set
# configure: error: set ac_cv_file__dev_ptmx to yes/no in your CONFIG_SITE file when cross compiling

pkg_configure() {
    std_configure \
	--disable-ipv6
}
