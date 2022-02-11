#
# spec file for package far2l
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           far2l
Version:        v_2.4.0
Release:        0
Summary:        Linux port of FAR v2
License:        GPL-2.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/elfmz/far2l
Source:         %{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.0.2
BuildRequires:  fdupes
BuildRequires:  gawk
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libxerces-c-devel
BuildRequires:  m4
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libnfs)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(libssh)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(neon)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(smbclient)
BuildRequires:  pkgconfig(spdlog)
BuildRequires:  pkgconfig(uchardet)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3-virtualenv
BuildRequires:  update-desktop-files
BuildRequires:  wxGTK3-devel
#uildRequires:  wxQt-3_2-devel
Requires:       gvfs
Requires:       libnotify-tools
Requires:       xdg-utils
Requires:       xterm-bin

%description
Linux port of FAR Manager v2 (http://farmanager.com) BETA VERSION.
Currently interesting only for enthusiasts!!!

%prep
%autosetup
sed -i "s/\(Exec=\).*/\1%{name}/" %{name}/DE/%{name}.desktop

%build
%define __builder ninja
%cmake \
    -DBUILD_SHARED_LIBS:BOOL=OFF
%ninja_build

%install
%cmake_install
install -Dm 0755 build/tools/farlng %{buildroot}%{_bindir}/

rm -fv %{buildroot}%{_datadir}/icons/*.??g
rm -rfv %{buildroot}%{_datadir}/icons/hicolor/1024x1024
%suse_update_desktop_file -r %{name} System FileManager
%fdupes %{buildroot}%{_datadir}/icons/hicolor/

%files
%doc README.md
%{_bindir}/%{name}
%{_bindir}/farlng
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.??g
#%%{_libexecdir}/%%{name}/
%{_prefix}/lib/%{name}
%license LICENSE.txt

%changelog

