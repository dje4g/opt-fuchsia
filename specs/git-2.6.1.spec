# git package spec

declare -r PKG_NAME=git
declare -r PKG_VERSION=2.6.1
declare -r PKG_TARBALL=${PKG_NAME}-${PKG_VERSION}.tar.xz
declare -r PKG_URL=https://www.kernel.org/pub/software/scm/git/git-2.6.1.tar.xz
declare -r PKG_SIG=https://www.kernel.org/pub/software/scm/git/git-2.6.1.tar.sign
declare -r PKG_BUILD_IN_SRC=yes
declare -r PKG_NATIVE_ONLY=yes

# TODO(dje):
# checking whether system succeeds to read fopen'ed directory... configure: error: in `/data/opt/staging/build/git-2.6.1':
# configure: error: cannot run test program while cross compiling
