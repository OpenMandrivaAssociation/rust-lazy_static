# Generated by rust2rpm 10
%bcond_without check
%global debug_package %{nil}

%global crate lazy_static

Name:           rust-%{crate}
Version:        1.4.0
Release:        2%{?dist}
Summary:        Macro for declaring lazily evaluated statics in Rust

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/lazy_static
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Macro for declaring lazily evaluated statics in Rust.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.md
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+spin-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+spin-devel %{_description}

This package contains library source intended for building other packages
which use "spin" feature of "%{crate}" crate.

%files       -n %{name}+spin-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+spin_no_std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+spin_no_std-devel %{_description}

This package contains library source intended for building other packages
which use "spin_no_std" feature of "%{crate}" crate.

%files       -n %{name}+spin_no_std-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 26 05:32:55 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 23:19:54 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.0-5
- Regenerate

* Sun Jun 09 10:14:00 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.0-4
- Regenerate

* Sun Mar 10 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.0-3
- Do not pull optional dependencies

* Sat Mar 09 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.0-2
- Bring spin back

* Thu Feb 28 2019 Josh Stone <jistone@redhat.com> - 1.3.0-1
- Update to 1.3.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 10 2018 Josh Stone <jistone@redhat.com> - 1.2.0-1
- Update to 1.2.0

* Sat Oct 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.0-3
- Adapt to new packaging

* Sun Oct 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.0-2
- Run tests in infrastructure

* Tue Aug 07 2018 Josh Stone <jistone@redhat.com> - 1.1.0-1
- Update to 1.1.0

* Sun Jul 15 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 29 2018 Josh Stone <jistone@redhat.com> - 1.0.1-1
- Update to 1.0.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-2
- Rebuild for rust-packaging v5

* Thu Nov 30 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0

* Mon Nov 20 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.11-1
- Update to 0.2.11

* Tue Nov 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.10-1
- Update to 0.2.10

* Mon Nov 06 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.9-1
- Update to 0.2.9

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.8-1
- Update to 0.2.8

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.5-2
- Port to use rust-packaging

* Thu Mar 30 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.5-1
- Update to 0.2.5

* Sun Mar 05 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.4-1
- Update to 0.2.4

* Fri Feb 24 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.2-2
- Use rich dependencies

* Sat Feb 18 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.2-1
- Initial package
