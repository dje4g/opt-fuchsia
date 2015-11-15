# SSL certificates package (see README.txt in source tree)
# These are from mozilla, obtained via linuxfromscratch.org.
# http://www.linuxfromscratch.org/blfs/view/svn/postlfs/cacerts.html

declare -r PKG_NAME=certs
declare -r PKG_VERSION=0.1
declare -r PKG_TARBALL=${PKG_NAME}-${PKG_VERSION}.tar.gz
declare -r PKG_URL=http://anduin.linuxfromscratch.org/BLFS/other/certdata.txt
declare -r PKG_SIG=md5sum:e9d20e29c8442560cfc5245ed03bfa6a
