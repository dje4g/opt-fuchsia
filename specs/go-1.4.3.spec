# go package spec

declare -r PKG_NAME=go
declare -r PKG_VERSION=1.4.3
declare -r PKG_TARBALL=${PKG_NAME}${PKG_VERSION}.src.tar.gz
declare -r PKG_URL=https://storage.googleapis.com/golang/go1.4.3.src.tar.gz
declare -r PKG_SIG=sha1:486db10dc571a55c8d795365070f66d343458c48
declare -r PKG_SRC=${PKG_NAME}
declare -r PKG_BUILD_IN_SRC=yes

# There is no configure step.

pkg_configure() {
    :
}

pkg_make() {
    export GOROOT_FINAL=$OPT_ROOT/lib/go
    # all.bash runs the tests, but not all pass:
    # /tmp may be missing, insufficient networking
    # TODO(dje): We've got env installed in /bin instead of /usr/bin.
    cd src
    env bash make.bash
}

pkg_stage() {
    # Ugh. go does things its own way.
    # In particular, it expects the entire src+build tree to be installed.
    # No point in installing the testsuite on a phone, for example.
    mkdir -m 0755 -p "${DESTDIR}${OPT_ROOT}/lib/go"
    cp -a bin pkg src "${DESTDIR}${OPT_ROOT}/lib/go"
    mkdir -m 0755 -p "${DESTDIR}${OPT_ROOT}/bin"
    ln -s ../lib/go/bin/go "${DESTDIR}${OPT_ROOT}/bin/go"
}
