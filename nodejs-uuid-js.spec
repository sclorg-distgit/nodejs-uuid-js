%{?scl:%scl_package nodejs-uuid-js}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-uuid-js

%global npm_name uuid-js
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-uuid-js
Version:	0.7.5
Release:	3%{?dist}
Summary:	A js library to generate and parse UUIDs,TimeUUIDs and generate TimeUUID based on Date for range selections
Url:		http://github.com/pnegri/uuid-js
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:        ASL-2.0	

BuildArch:	noarch

%if 0%{?fedora} >= 19
ExclusiveArch:	%{ix86} x86_64 %{arm} noarch
%else
ExclusiveArch:	%{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:	%{?scl_prefix}npm(sinon)
%endif

%description
A js library to generate and parse UUIDs,TimeUUIDs and generate TimeUUID based on Date for range selections

%prep
%setup -q -n package

rm -rf node_modules

%build

#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json lib/ \
%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}

%check
%{nodejs_symlink_deps} --check

%endif

%files
%{!?_licensedir:%global license %doc}
%{nodejs_sitelib}/uuid-js

%doc README.md
%doc LICENSE.txt

%changelog
* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.7.5-3
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.7.5-2
- Rebuilt with updated metapackage

* Tue Jan 12 2016 Tomas Hrcka <thrcka@redhat.com> - 0.7.5-1
- Initial build
