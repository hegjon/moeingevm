%define debug_package %{nil}

Name:    {{{ git_name name="moeingevm" }}}
Version: 0.1
Release: {{{ git_version }}}%{?dist}
Summary: A parallelized execution engine which manages multiple EVM

License:    ASL 2.0
URL:        https://github.com/smartbch/moeingevm
VCS:        {{{ git_vcs }}}

Source:     {{{ git_pack }}}

BuildRequires: make
BuildRequires: gcc-g++

%description
MoeingEVM is a parallelized execution engine which manages multiple EVM contexts
and executes multiple transactions concurrently.

%prep
{{{ git_setup_macro }}}

%build
pushd evmwrap
%make_build
popd

%install
install -D -m 755 ./evmwrap/host_bridge/libevmwrap.so %{buildroot}%{_libdir}/libevmwrap.so

%files
%doc README.md
%license LICENSE
%{_libdir}/libevmwrap.so

%changelog
{{{ git_changelog }}}
