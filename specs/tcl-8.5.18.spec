# tcl package spec

declare -r PKG_NAME=tcl
declare -r PKG_VERSION=8.5.18
declare -r PKG_TARBALL=${PKG_NAME}${PKG_VERSIN}-src.tar.gz
declare -r PKG_URL=http://tcpdiag.dl.sourceforge.net/project/tcl/Tcl/8.5.18/tcl8.5.18-src.tar.gz
declare -r PKG_SIG=md5sum:9b80e9dde418ec92359ecc5739c6a9a8
declare -r PKG_SRC=${PKG_NAME}${PKG_VERSION}/unix

# TODO(dje): Compile natively to avoid:
# fixstrtod.c:(.text+0x0): multiple definition of `fixstrtod'
# strtod.o:strtod.c:(.text+0x0): first defined here
# Easy enough to fix, undef strtod in strtod.c. Maybe later.
declare -r PKG_NATIVE_ONLY=yes
