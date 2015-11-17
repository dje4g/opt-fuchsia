# emacs package spec
# This emacs came from its git repository, 15oct10.
# Head commit: 1196e3fca6f9df107c76438b7d00090d19b13570
# Should probably encode the commit id in the version.

declare -r PKG_NAME=emacs
declare -r PKG_VERSION=git
declare -r PKG_TARBALL=${PKG_NAME}-${PKG_VERSION}.tar.xz
declare -r PKG_URL=git://git.sv.gnu.org/emacs.git
declare -r PKG_SIG=md5sum:6703ae47e9a2cdda4f2584b58619ca25
declare -r PKG_SRC=emacs
declare -r PKG_PATCHES=${PKG_NAME}-${PKG_VERSION}.patches

pkg_configure() {
    std_configure \
	--sysconfdir=$OPT_ROOT/etc \
	--libexecdir=$OPT_ROOT/lib \
	--localstatedir=$OPT_ROOT/var \
	--with-gameuser=:games \
	--without-sound \
	--without-x \
	--without-file-notification
}
