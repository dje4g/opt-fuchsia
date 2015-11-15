# missing-libc package spec
# This package supplies misc things from glibc to simplify porting.

declare -r PKG_NAME=missing-libc
declare -r PKG_VERSION=0.1
declare -r PKG_TARBALL=${PKG_NAME}-${PKG_VERSION}.tar.gz
declare -r PKG_URL=file:/${OPT_SRC_DIR}/${PKG_TARBALL}
declare -r PKG_SIG=md5sum:50af219b506abee223a593778ed88288
