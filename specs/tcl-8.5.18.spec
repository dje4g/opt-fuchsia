# tcl package spec

declare -r PKG_NAME=tcl-8.5.18
declare -r PKG_TARBALL=tcl8.5.18-src.tar.gz
declare -r PKG_SRC=tcl8.5.18/unix
declare -r PKG_PATCHES=none
#${PKG_NAME}.patches

# TODO(dje): Compile natively to avoid:
# fixstrtod.c:(.text+0x0): multiple definition of `fixstrtod'
# strtod.o:strtod.c:(.text+0x0): first defined here
# Easy enough to fix, undef strtod in strtod.c. Maybe later.
declare -r PKG_NATIVE_ONLY=yes
