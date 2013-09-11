Name:		cqrlog
Version:	1.6.0
Release:	1%{?dist}
Summary:	An amateur radio contact logging program

Group:		Applications/Databases
License:	GPLv2
URL:		http://www.cqrlog.com/
Source0:	http://www.cqrlog.com/files/%{name}_%{version}/%{name}_%{version}.deb.src.tar.gz
Patch0:		cqrlog.makefile.patch
Patch1:		cqrlog.desktop.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# fpc not available on these arches
ExcludeArch:	s390 s390x armv7hl

BuildRequires:	fpc
BuildRequires:	lazarus
Requires:	mysql-server
Requires:	trustedqsl
Requires:	hamlib 
Requires:	openssl-devel
Requires:	mariadb-libs
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
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/okqrp.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/a1-op.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/mcwg.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/rsars.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/fnars.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/trc.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/mf.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/hacwg.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/wff.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/udxc.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/marac.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/nra.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/wwyc.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/bcc.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/ctc.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/bscc.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/ehsc.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/tenten.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/spcwc.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/armi.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/ten-ten.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/vhsc.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/cwjf.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/spar.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/cav.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/vrk.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/wap.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/wcc.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/uksmg.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/inorc.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/fists.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/yasme.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/uft.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/mdxg.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/shsc.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/rafars.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/gdxf.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/cfo.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/cct.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/cdxc.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/spar-rcc.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/marconista.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/fog.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/sdxg.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/spdxc.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/bmars.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/qcwa.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/hhc.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/rrdxa.txt
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/members/arktika.txt

iconv -f iso8859-1 -t utf-8 %{buildroot}%{_datadir}/%{name}/ctyfiles/eqsl.txt > %{buildroot}%{_datadir}/%{name}/ctyfiles/eqsl.txt.conv && mv -f %{buildroot}%{_datadir}/%{name}/ctyfiles/eqsl.txt.conv %{buildroot}%{_datadir}/%{name}/ctyfiles/eqsl.txt

%files
%doc %{_datadir}/%{name}
%{_datadir}/applications/cqrlog.desktop
%{_datadir}/icons/cqrlog.png
%{_datadir}/pixmaps/cqrlog/cqrlog.png
%{_bindir}/cqrlog
%{_mandir}/man1/cqrlog.1.gz

%changelog
* Tue Sep 10 2013 Eric "Sparks" Christensen <sparks@fedoraproject.org> - 1.6.0-1
- your CQ received by RBN will be visible in gray line map
- local mysqld is executed only when the log is stored to local machine
- added JT9 to list of modes
- added Power field to filter window
- option to show distance in miles instead of km added
- limit of max QSO on QSL label increased
- added whole new bandmap with frequecy indicator
- double click on bandmap didn't work when the spot had split info - fixed
- propagation info in spot notes has correct format
- existing band map record was not updated from dx cluster
- program didn't accept ITU zones 78 and 90 - fixed
- program used QTH from previous QSO even is the station was /P - fixed

* Mon Aug 12 2013 Eric "Sparks" Christensen <sparks@fedoraproject.org> - 1.5.8-5
- Added exclusion for armv7hl arch.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 12 2013 Eric "Sparks" Christensen <sparks@fedoraproject.org> - 1.5.8-3
- Fixed libmysqlclient.so.18 dependency

* Wed Jul 10 2013 Eric "Sparks" Christensen <sparks@fedoraproject.org> - 1.5.8-2
- Fixed openssl dependency.

* Tue Jul 9 2013 Eric "Sparks" Christensen <sparks@fedoraproject.org> - 1.5.8-1
- Upgraded to version 1.5.8
- Nothing happened after double click on bandmap spot - fixed
- Enter key in Filter window will activate the filter
- Blank locator field in Group edit clears locator field
- ADIF export didn't contain DXCC field with ADIF id of the country
- grayline caused program crash after compile with recent FPC and Lazarus versions
- When the grid was in lowercase, the Big square statistic was broken
- Bandmap didn't worked if the freq of QSO precision was to one Hz
- Debug level settings didn't worked at all
- QSO will be confirmed when time difference between QSO and QSO from LoTW is not more than 10 minutes


* Wed Jun 19 2013 Eric "Sparks" Christensen - 1.5.6-1
- Upgrade to version 1.5.6
- if any error message about LoTW import appear, you can open it in external app directly from CQRLOG
- LoTW upload url changed
- fixed "An invalid integer value" error during label export
- import of QSO with custom digi mode didn't worked if the list of modes didn't ended with comma (,) - fixed
- bandmap didn't worked if the freq of QSO precision was to ten Hz
- station with /AM and /MM caused error "You must enter correct WAZ zone!" - fixed
- removed mode from search criteria to confirm QSO via LoTW
- QSO will be confirmed when time difference between QSO and QSO from LoTW is not more than 1 hour
- default debug level is set 0, if you want to get more info what cqrlog does, run it with debug=1 or more

* Fri Mar 29 2013 Eric "Sparks" Christensen - 1.5.4-1
- Upgrade to version 1.5.4
- fixed problem with MASTER.SCP
- added support for Super Check Partial (Window -> Super Check Partial)
- added Tune function (for WinKeyerUSB and cwdaemon), hotkey CTRL+T
- added Repair table function to database connection window (Utils button)
- improved export for QSL labels printing (labels are sorted by dxcc, you can choose what fields will be be printed)
- updated membership tables
- fixed program crash when editing DX cluster info
- CW keys window doesn't show caption for F9 and F10 keys
- ADIF export ignored delimitter in TX_PWR (0.5 was exported as 05)
- CQRLOG killed rigctld even when autostart was disabled
- double click to spots listed with SH/DX didn't work
- QSO list window showed filter is enabled after reopen (filter was disabled)
- login to eQSL with password containing special character didn't work
- when QSO passed over the midnight, the qso was saved with wrong date

* Thu Feb 28 2013 Eric "Sparks" Christensen - 1.5.2-6
- Fixed OpenSSL requirements

* Fri Feb 22 2013 Eric "Sparks" Christensen - 1.5.2-5
- Repaired desktop category

* Fri Feb 22 2013 Eric "Sparks" Christensen - 1.5.2-4
- Changed openssl-devel from BuildRequires to Requires as it is needed for LoTW functionality

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 9 2012 Dan Horák <dan[at]danny.cz> - 1.5.2-2
- set ExcludeArch to match fpc

* Mon Oct 8 2012 Eric "Sparks" Christensen <sparks@fedoraproject.org> - 1.5.2-1
- added CTRL+W hotkey to send spots to dxcluster
- DX cluster shows also country name next to the spot (must be enabled in Prefereces)
- international characters in New QSO window should work again
- DX spots with freq eqauls to the start of the band (21.000, 14.000 etc., usually notes) are ignored
- HamQTH added to dx clusters list
- fixed reading A-index (was 1 even when actually was 10)
- /MM, /AM and stations with unknown DXCC country didn't appear in bandmap
- database update hangs
- fixed xml request address of qrz.com
- DXCC CFM count function didn't uses eQSL cfm QSO
- fixed reading mode from FT-920 (returned MEMO as VFO)
- fixed bug in dxcluster caused program crashed randomly
- program didn't apply eQSL rcvd when the band was in lowercase

* Tue Aug 14 2012 Eric "Sparks" Christensen <sparks@fedoraproject.org> - 1.5.1-1
- Initial package
