DESCRIPTION = "Soft Test Python"
SECTION = "devel/python"

LICENSE = "PSF"
LIC_FILES_CHKSUM = "file://LICENSE.txt;md5=c557c64905dac5b725980b9505bf8d7b"

SRC_URI = "file://pythont.py"

S = "${WORKDIR}"

inherit setuptools

do_install_append () {
    install -d ${D}${bindir}
    install -m 0755 pythont.py "${D}${bindir}/test"
}
