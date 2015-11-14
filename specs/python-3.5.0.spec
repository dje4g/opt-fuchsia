# python3 package spec

declare -r PKG_NAME=python-3.5.0
declare -r PKG_TARBALL=Python-3.5.0.tar.xz
declare -r PKG_SRC=Python-3.5.0
declare -r PKG_NATIVE_ONLY=yes

# TODO(dje):
# checking for /dev/ptmx... not set
# configure: error: set ac_cv_file__dev_ptmx to yes/no in your CONFIG_SITE file when cross compiling

pkg_configure() {
    std_configure \
	--disable-ipv6
}
