sudo zypper install fedora-packager @development-tools
sudo zypper install gawk m4 cmake gcc-c++ wxGTK3-devel xerces-c-devel spdlog-devel uchardet-devel
sudo zypper install libssh-devel openssl-devel libsmbclient-devel libnfs-devel 
sudo zypper install neon-devel libarchive-devel pcre2-devel python38-devel
sudo zypper install fdupes gawk hicolor-icon-theme libxerces-c-devel m4 ninja pkgconfig
sudo zypper install rpmdevtools rpm-build
rpmdev-setuptree
cp far2l-v_2.4.0.tar.gz ~/rpmbuild/SOURCES
rpmbuild -ba far2l.spec
