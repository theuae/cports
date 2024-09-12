pkgname = "kgpg"
pkgver = "24.08.1"
pkgrel = 0
build_style = "cmake"
# flaky
make_check_args = ["-E", "kgpg-import"]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "akonadi-contacts-devel",
    "gpgme-devel",
    "karchive-devel",
    "kcodecs-devel",
    "kcontacts-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "kio-devel",
    "kjobwidgets-devel",
    "knotifications-devel",
    "kservice-devel",
    "kstatusnotifieritem-devel",
    "ktextwidgets-devel",
    "kwidgetsaddons-devel",
    "kwindowsystem-devel",
    "kxmlgui-devel",
    "qt6-qtdeclarative-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE GnuPG interface"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/kgpg"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kgpg-{pkgver}.tar.xz"
sha256 = "c6135d67854d4b21cd2a5474d5fd9adba5447cad28b824e8af5cc00258636485"
