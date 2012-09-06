Name:		cqrlog
Version:	1.5.1
Release:	1%{?dist}
Summary:	An amateur radio contact logging program

Group:		Applications/Databases
License:	GPLv2
URL:		http://www.cqrlog.com/
Source0:	http://www.cqrlog.com/files/%{name}_%{version}/%{name}_%{version}.deb.src.tar.gz
Patch0:		cqrlog.makefile.patch
Patch1:		cqrlog.desktop.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	fpc
BuildRequires:	lazarus
Requires:	mysql
Requires:	mysql-server
Requires:	trustedqsl
Requires:	hamlib 
#This entire library is required for this software as this library contains the information for connecting to various transceivers.
BuildRequires:	openssl-devel
BuildRequires:	desktop-file-utils

%description
CQRLOG is an advanced ham radio logger based on MySQL database. Provides radio
control based on hamlib libraries (currently support of 140+ radio types and 
models), DX cluster connection, QRZ callbook (web version), a grayliner, 
internal QSL manager database support and a most accurate country resolution 
algorithm based on country tables developed by OK1RR. CQRLOG is intended for 
daily general logging of HF, CW & SSB contacts and strongly focused on easy 
operation and maintenance.

%prep
tar -xpf %{SOURCE0}
tar -xpf %{name}_%{version}.orig.tar.gz
%setup -q -D -T
%patch0
%patch1

chmod -x src/azidis3.pas
chmod -x src/gline2.pas
chmod -x src/odbec.pas
chmod -x src/aziloc.pas
chmod -x src/znacmech.pas

%build
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

desktop-file-validate ${RPM_BUILD_ROOT}%{_datadir}/applications/cqrlog.desktop

sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/ctyfiles/lotw1.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/ria.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/okdxf.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/htc.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/pro.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/9acwg.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/gqrpc.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/prl.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/ctyfiles/iota.tbl
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/ffr.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/ctyfiles/eqsl.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/mfca.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/firac.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/cwsp.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/gacw.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/conveniat.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/was.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/jaig.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/mcl.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/cft.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/epc.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/tfc.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/fmc.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/hh.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/okdxc.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/ctyfiles/CountryDel.tab
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/qthloc.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/070-club.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/dtc.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/afm.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/prc.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/rtc.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/rnars.txt
iconv -f iso8859-1 -t utf-8 %{buildroot}%{_datadir}/%{name}/ctyfiles/eqsl.txt > %{buildroot}%{_datadir}/%{name}/ctyfiles/eqsl.txt.conv && mv -f %{buildroot}%{_datadir}/%{name}/ctyfiles/eqsl.txt.conv %{buildroot}%{_datadir}/%{name}/ctyfiles/eqsl.txt

%files
%doc %{_datadir}/%{name}
%{_datadir}/applications/cqrlog.desktop
%{_datadir}/icons/cqrlog.png
%{_datadir}/pixmaps/cqrlog/cqrlog.png
%{_bindir}/cqrlog
%{_mandir}/man1/cqrlog.1.gz

%changelog
* Tue Aug 14 2012 Eric "Sparks" Christensen <sparks@fedoraproject.org> - 1.5.1-1
- Initial package
