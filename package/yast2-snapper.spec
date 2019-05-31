#
# spec file for package yast2-snapper
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           yast2-snapper
Version:        4.1.2
Release:        0
Group:          System/YaST
Summary:        YaST - file system snapshots review
Url:            https://github.com/yast/yast-snapper/
License:        GPL-2.0-only

Source0:        %{name}-%{version}.tar.bz2

Requires:       snapper
Requires:       yast2 >= 4.1.60
Requires:       yast2-ruby-bindings >= 1.0.0
Requires:       rubygem(%{rb_default_ruby_abi}:ruby-dbus)

BuildRequires:  doxygen
BuildRequires:  update-desktop-files
BuildRequires:  yast2 >= 4.1.60
BuildRequires:  yast2-devtools >= 3.1.10
BuildRequires:  rubygem(%{rb_default_ruby_abi}:rspec)
BuildRequires:  rubygem(%{rb_default_ruby_abi}:ruby-dbus)

Supplements:    (snapper and yast2)

# change to noarch causes problems according to behlert
# BuildArch:      noarch

%description
YaST module for accessing and managing file-system snapshots

%prep
%setup -q

%build
%yast_build

%install
%yast_install
%yast_metainfo

%files
%{yast_yncludedir}
%{yast_clientdir}
%{yast_moduledir}
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_icondir}
%doc %{yast_docdir}
%license COPYING
