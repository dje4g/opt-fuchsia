# sudo package spec
# TODO(dje): DESTDIR isn't treated consistently.
# E.g., etc files are not currently installed (which isn't a bad thing per se - at least we
# don't overwrite potentially hand-modified ones).

declare -r PKG_NAME=sudo
declare -r PKG_VERSION=1.8.14p3
declare -r PKG_TARBALL=${PKG_NAME}-${PKG_VERSION}.tar.gz
declare -r PKG_URL=ftp://ftp.sudo.ws/pub/sudo/sudo-1.8.14p3.tar.gz
declare -r PKG_SIG=md5sum:93dbd1e47c136179ff1b01494c1c0e75
declare -r PKG_PATCHES=${PKG_NAME}-${PKG_VERSION}.patches

# Leave setting permissions to the user.

pkg_stage() {
    std_stage \
	INSTALL_OWNER= \
	"$@"
}
