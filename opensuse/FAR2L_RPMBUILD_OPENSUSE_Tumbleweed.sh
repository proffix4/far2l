sudo zypper install -y gawk m4 cmake gcc-c++ wxGTK3-devel spdlog-devel
sudo zypper install -y libssh-devel openssl-devel libsmbclient-devel libnfs-devel
sudo zypper install -y neon-devel libarchive-devel pcre2-devel python38-devel
sudo zypper install -y fdupes gawk hicolor-icon-theme libxerces-c-devel m4 ninja pkgconfig
sudo zypper install -y update-desktop-files python3-virtualenv uchardet libuchardet-devel python3-pkgconfig xerces-c
sudo zypper install -y rpmdevtools rpm-build 
rpmdev-setuptree
cp far2l-v_2.4.0.tar.gz ~/rpmbuild/SOURCES
rpmbuild -ba far2l.spec
