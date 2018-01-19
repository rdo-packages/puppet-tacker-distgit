%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%{!?upstream_name: %global upstream_name openstack-tacker}

Name:                   puppet-tacker
Version:                11.4.0
Release:                1%{?dist}
Summary:                Puppet module for OpenStack Tacker
License:                ASL 2.0

URL:                    https://launchpad.net/puppet-tacker

Source0:                https://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz

BuildArch:              noarch

Requires:               puppet-inifile
Requires:               puppet-stdlib
Requires:               puppet-openstacklib
Requires:               puppet-keystone
Requires:               puppet-oslo

Requires:               puppet >= 2.7.0

%description
Installs and configures OpenStack Tacker.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/tacker/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/tacker/



%files
%{_datadir}/openstack-puppet/modules/tacker/


%changelog
* Fri Jan 19 2018 RDO <dev@lists.rdoproject.org> 11.4.0-1
- Update to 11.4.0

* Fri Dec 01 2017 RDO <dev@lists.rdoproject.org> 11.3.1-1
- Update to 11.3.1

* Fri Aug 25 2017 Alfredo Moralejo <amoralej@redhat.com> 11.3.0-1
- Update to 11.3.0

* Mon Jan 09 2017 Dan Radez <dradez@redhat.com> - XXX-XXX
- Initial Packaging

