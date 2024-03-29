#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : the_silver_searcher
Version  : 2.2.0
Release  : 1
URL      : https://github.com/ggreer/the_silver_searcher/archive/2.2.0.tar.gz
Source0  : https://github.com/ggreer/the_silver_searcher/archive/2.2.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: the_silver_searcher-bin = %{version}-%{release}
Requires: the_silver_searcher-data = %{version}-%{release}
Requires: the_silver_searcher-man = %{version}-%{release}
BuildRequires : grep
BuildRequires : pkgconfig(liblzma)
BuildRequires : pkgconfig(libpcre)
BuildRequires : pkgconfig(zlib)

%description
# The Silver Searcher
A code searching tool similar to `ack`, with a focus on speed.

%package bin
Summary: bin components for the the_silver_searcher package.
Group: Binaries
Requires: the_silver_searcher-data = %{version}-%{release}

%description bin
bin components for the the_silver_searcher package.


%package data
Summary: data components for the the_silver_searcher package.
Group: Data

%description data
data components for the the_silver_searcher package.


%package man
Summary: man components for the the_silver_searcher package.
Group: Default

%description man
man components for the the_silver_searcher package.


%prep
%setup -q -n the_silver_searcher-2.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1569957353
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1569957353
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ag

%files data
%defattr(-,root,root,-)
/usr/share/the_silver_searcher/completions/ag.bashcomp.sh
/usr/share/zsh/site-functions/_the_silver_searcher

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/ag.1
