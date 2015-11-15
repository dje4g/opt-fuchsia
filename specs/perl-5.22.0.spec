# perl package spec

declare -r PKG_NAME=perl
declare -r PKG_VERSION=5.22.0
declare -r PKG_TARBALL=${PKG_NAME}-${PKG_VERSION}.tar.bz2
declare -r PKG_URL=http://www.cpan.org/src/5.0/perl-5.22.0.tar.bz2
declare -r PKG_SIG=md5sum:f67b152160431b3180fb766bdc2d02e2
declare -r PKG_BUILD_IN_SRC=yes

# perl has a differently named configure script, bleah

pkg_configure() {
    # For perl CC,CFLAGS have to be passed in as env vars.
    CC=${OPT_HOST_SYSTEM}-gcc \
    CFLAGS=-O2 \
    $OPTPKG_SRCDIR/$PKG_SRC/configure.gnu \
	--prefix=$OPT_ROOT
}
