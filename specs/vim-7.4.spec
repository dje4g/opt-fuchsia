# vim package spec

declare -r PKG_NAME=vim
declare -r PKG_VERSION=7.4
declare -r PKG_TARBALL=${PKG_NAME}-${PKG_VERSION}.tar.bz2
declare -r PKG_URL=http://ftp.vim.org/vim/unix/vim-7.4.tar.bz2
declare -r PKG_SIG=md5sum:607e135c559be642f210094ad023dc65
declare -r PKG_SRC=vim74
declare -r PKG_BUILD_IN_SRC=yes
declare -r PKG_NATIVE_ONLY=yes

# TODO(dje):
# checking whether toupper is broken... configure: error: cross-compiling: please set 'vim_cv_toupper_broken'

pkg_configure() {
    std_configure \
	--with-tlib=ncurses
}
