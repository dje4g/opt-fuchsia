# sudo package spec

declare -r PKG_NAME=sudo-1.8.14
declare -r PKG_TARBALL=sudo-1.8.14p3.tar.gz
declare -r PKG_SRC=sudo-1.8.14p3
declare -r PKG_PATCHES=${PKG_NAME}.patches

# Leave setting permissions to the user.

pkg_stage() {
    std_stage \
	INSTALL_OWNER=
}
