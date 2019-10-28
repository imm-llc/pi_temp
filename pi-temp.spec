
%define name pi-temp
%define version 1.0
%define unmangled_version 1.0
%define unmangled_version 1.0
%define release 1
%define _tmppath /tmp/rpm


Summary: Temperature and Humidity Monitoring
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}.tar.gz
Requires: python36 python36-setuptools python36-devel
License: None
Group: Monitoring
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Mitch Anderson <manderson@boulderheavyindustries.com>
Url: https://github.com/imm-llc/pi_temp

%description

A Flask API allowing you to poll temperature and humidity levels off a Rasperry Pi + DHT22.

%prep
rm -rf %{_tmppath}/*
rm -rf %{_builddir}/*
rm -rf %{buildroot}/*


%setup -c -n %{name}

%build

%install
mkdir -p %{buildroot}/var/local/pi_temp
mkdir -p %{buildroot}/etc/systemd/system
mkdir -p %{buildroot}/etc/sysconfig
mkdir -p %{buildroot}/src/app
mv %{_builddir}/src/app %{buildroot}/var/local/pi_temp
touch %{buildroot}/etc/sysconfig/pitemp
install -m 0640 %{_builddir}/src/main.py %{buildroot}/var/local/pi_temp
install -m 0640 %{_builddir}/reqs.txt %{buildroot}/var/local/pi_temp/pipfile
install -m 0644 %{_builddir}/pi-temp.service %{buildroot}/etc/systemd/system/

%pre

if [ "$1" = "1" ]; then
    echo "##############################"
    echo "Installing PiTemp"
    if [ ! $(id -u api 2> /dev/null) ] 
    then 
    echo "##############################"
    echo "Could not find api user....creating"
    adduser --system --no-create-home --shell /sbin/nologin api
    echo "##############################"
    echo "User created"
    fi
fi

if [ "$1" = "2" ]; then
  echo "##############################"
  echo "Stopping PiTemp upgrade"
  systemctl stop pi-temp
fi

%post 

if [ "$1" = "1" ]; then
    echo "##############################"
    echo "Checking dependencies"
    if [ ! -f /usr/local/bin/pip3 ]
        then
        echo "pip3 not installed.....installing"
        /usr/bin/easy_install-3.6 pip 1> /dev/null
    fi
    echo "##############################"
    echo "Installing python dependencies"
    /usr/local/bin/pip3 install -r /var/local/pi_temp/pipfile 
fi

if [ "$1" = "2" ]; then
  echo "##############################"
  echo "Upgrading PiTemp"
  echo "##############################"
  echo "Copying old config to /tmp/pi-temp.backup.$(date +%F%s)"
  cp /etc/sysconfig/pi-temp /tmp/pi-temp.backup.$(date +%F%s)
  echo "##############################"
  echo "Starting PiTemp"
  systemctl start pi-temp
fi


%clean
rm -rf %{_builddir}/*
rm -rf %{buildroot}/*

%files
%defattr(-,api,root)
/var/local/pi_temp
%attr(0644,root,root) /etc/systemd/system/pi-temp.service
%config %attr(0644,api,api) /etc/sysconfig/pi-temp