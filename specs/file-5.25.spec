# file package spec

declare -r PKG_NAME=file
# PKG_BASE_VERSION is local to this file
declare -r PKG_BASE_VERSION=5.25
declare -r PKG_VERSION=${PKG_BASE_VERSION}p1
declare -r PKG_TARBALL=${PKG_NAME}-${PKG_BASE_VERSION}.tar.gz
declare -r PKG_URL=ftp://ftp.astron.com/pub/file/file-5.25.tar.gz
declare -r PKG_SIG=md5sum:e6a972d4e10d9e76407a432f4a63cd4c
declare -r PKG_SRC=${PKG_NAME}-${PKG_BASE_VERSION}
declare -r PKG_PATCHES=${PKG_NAME}-${PKG_BASE_VERSION}.patches
