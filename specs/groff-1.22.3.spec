# groff package spec

declare -r PKG_NAME=groff
declare -r PKG_VERSION=1.22.3
declare -r PKG_TARBALL=${PKG_NAME}-${PKG_VERSION}.tar.gz
declare -r PKG_URL=$OPT_URL_GNU/$PKG_NAME/$PKG_TARBALL

# groff doesn't use C*FLAGS correctly :-(

pkg_make() {
    make -j$OPT_PARALLELISM
}
