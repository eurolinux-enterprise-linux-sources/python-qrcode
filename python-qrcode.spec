%global pkgname qrcode

Name:           python-%{pkgname}
Version:        5.0.1
Release:        1%{?dist}
Summary:        Python QR Code image generator

License:        BSD
URL:            https://github.com/lincolnloop/python-qrcode
Source0:        http://pypi.python.org/packages/source/q/qrcode/qrcode-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-imaging
BuildRequires:  python-six
Requires:       python-imaging
Requires:       %{name}-core = %{version}-%{release}

%description
This module uses the Python Imaging Library (PIL) to allow for the
generation of QR Codes.


%package core
Requires:       python-six
Summary:        Python QR Code image generator (core library)

%description core
Core Python module for QR code generation. Does not contain image rendering.


%prep
%setup -q -n %{pkgname}-%{version}

# The pure plugin requires pymaging which is not packaged in Fedora.
rm qrcode/image/pure.py*


%build
%{__python} setup.py build


%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}


%check
# in lieue of a real test suite
for m in $(find qrcode -name '*.py' \
    | grep -v __init__ \
    | sort \
    | sed -e 's|/|.|g' \
    | sed -e 's|.py$||g');
do
    %{__python} -c "import $m"
done


%files
%{_bindir}/qr
%{_mandir}/man1/qr.1*
%{python_sitelib}/%{pkgname}/image/svg.py*
%{python_sitelib}/%{pkgname}/image/pil.py*


%files core
%doc LICENSE README.rst CHANGES.rst
%dir %{python_sitelib}/%{pkgname}/
%dir %{python_sitelib}/%{pkgname}/image
%{python_sitelib}/%{pkgname}*.egg-info
%{python_sitelib}/%{pkgname}/*.py*
%{python_sitelib}/%{pkgname}/image/__init__.py*
%{python_sitelib}/%{pkgname}/image/base.py*


%changelog
* Wed Sep 10 2014 Nathaniel McCallum <npmccallum@redhat.com> - 5.0.1-1
- Update to 5.0.1

* Tue Sep 09 2014 Nathaniel McCallum <npmccallum@redhat.com> - 2.4.1-7
- Create -core subpackage for minimal dependencies

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun  6 2012 Michel Salim <salimma@fedoraproject.org> - 2.4.1-2
- Clean up spec, removing unnecessary declarations
- Rename tool in %%{_bindir} to the less ambiguous qrcode

* Sat Jun  2 2012 Michel Salim <salimma@fedoraproject.org> - 2.4.1-1
- Initial package
