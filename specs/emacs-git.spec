# emacs package spec
# This emacs came from its git repository, 15oct10.
# Head commit: 1196e3fca6f9df107c76438b7d00090d19b13570

declare -r PKG_NAME=emacs-git
declare -r PKG_TARBALL=${PKG_NAME}.tar.xz
declare -r PKG_SRC=emacs
declare -r PKG_PATCHES=${PKG_NAME}.patches

pkg_configure() {
    std_configure \
	--sysconfdir=$OPT_ROOT/etc \
	--libexecdir=$OPT_ROOT/lib \
	--localstatedir=$OPT_ROOT/var \
	--with-gameuser=:games \
	--without-sound \
	--without-x \
	--without-xml2 \
	--without-file-notification
}
