# w3m package spec

declare -r PKG_NAME=w3m
declare -r PKG_VERSION=0.5.3
declare -r PKG_TARBALL=${PKG_NAME}-${PKG_VERSION}.tar.gz
declare -r PKG_URL=http://iweb.dl.sourceforge.net/project/w3m/w3m/w3m-0.5.3/w3m-0.5.3.tar.gz
declare -r PKG_SIG=md5sum:1b845a983a50b8dec0169ac48479eacc
declare -r PKG_PATCHES=${PKG_NAME}-${PKG_VERSION}.patches

pkg_configure() {
    # Ugh. Setting ac_cv variables is just wrong.
    # The alternative is restricting this to native builds.
    ac_cv_func_setpgrp_void=yes \
    std_configure \
	--with-gc=$OPT_ROOT
}

# w3m doesn't use C*FLAGS correctly :-(

pkg_make() {
    make -j$OPT_PARALLELISM
}
