# gptfdisk package spec

declare -r PKG_NAME=gptfdisk
declare -r PKG_VERSION=1.0.1
declare -r PKG_TARBALL=${PKG_NAME}-${PKG_VERSION}.tar.gz
declare -r PKG_URL=http://iweb.dl.sourceforge.net/project/gptfdisk/gptfdisk/1.0.1/gptfdisk-1.0.1.tar.gz
declare -r PKG_SUM=d7f3d306b083123bcc6f5941efade586
declare -r PKG_PATCHES=${PKG_NAME}-${PKG_VERSION}.patches
declare -r PKG_BUILD_IN_SRC=yes

# There is no configure.

pkg_configure() {
    :
}

pkg_make() {
    std_make \
	CC=${OPT_HOST_SYSTEM}-gcc \
	CXX=${OPT_HOST_SYSTEM}-g++ \
	PREFIX=$OPT_ROOT
}

pkg_stage() {
    std_stage \
	prefix=$OPT_ROOT \
	mandir=$OPT_ROOT/share/man \
	"$@"
}
