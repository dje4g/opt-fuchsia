# vim package spec

declare -r PKG_NAME=vim-7.4
declare -r PKG_TARBALL=${PKG_NAME}.tar.bz2
declare -r PKG_SRC=vim74
declare -r PKG_BUILD_IN_SRC=yes
declare -r PKG_NATIVE_ONLY=yes

# TODO(dje):
# checking whether toupper is broken... configure: error: cross-compiling: please set 'vim_cv_toupper_broken'

pkg_configure() {
    std_configure \
	--with-tlib=ncurses
}
