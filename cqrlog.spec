Name:		cqrlog
Version:	1.9.0
Release:	2%{?dist}
Summary:	An amateur radio contact logging program

License:	GPLv2
URL:		http://www.cqrlog.com/
Source0:	http://www.cqrlog.com/files/%{name}_%{version}/%{name}-%{version}.tar.gz

Patch0:		cqrlog-1.9.0-install.patch
Patch1:		cqrlog.desktop.patch

# fpc not available on these arches
#ExcludeArch:	s390 s390x armv7hl
ExcludeArch:	s390 s390x

BuildRequires:	fpc >= 2.6.4
BuildRequires:	lazarus
BuildRequires:	desktop-file-utils
Requires:	mariadb-server
Requires:	trustedqsl
Requires:	hamlib 
Requires:	openssl-devel
Requires:	mariadb-libs


%description
CQRLOG is an advanced ham radio logger based on MySQL database. Provides radio
control based on hamlib libraries (currently support of 140+ radio types and 
models), DX cluster connection, QRZ callbook (web version), a grayliner, 
internal QSL manager database support and a most accurate country resolution 
algorithm based on country tables developed by OK1RR. CQRLOG is intended for 
daily general logging of HF, CW & SSB contacts and strongly focused on easy 
operation and maintenance.

%prep
%setup -q
%patch0 -p1
%patch1

chmod -x src/azidis3.pas
chmod -x src/gline2.pas
chmod -x src/odbec.pas
chmod -x src/aziloc.pas
chmod -x src/znacmech.pas
chmod -x tools/cqrlog-apparmor-fix
chmod -x voice_keyer/voice_keyer.sh


%build
make %{?_smp_mflags}


%install
%make_install

desktop-file-validate %{buildroot}%{_datadir}/applications/cqrlog.desktop

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
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/ctyfiles/MASTER.SCP

iconv -f iso8859-1 -t utf-8 %{buildroot}%{_datadir}/%{name}/ctyfiles/eqsl.txt > %{buildroot}%{_datadir}/%{name}/ctyfiles/eqsl.txt.conv && mv -f %{buildroot}%{_datadir}/%{name}/ctyfiles/eqsl.txt.conv %{buildroot}%{_datadir}/%{name}/ctyfiles/eqsl.txt


%files
%if 0%{?rhel} < 7 || 0%{?fedora} < 21
%doc src/COPYING
%else
%license src/COPYING
%endif
%doc README.md src/AUTHORS src/CHANGELOG src/README
%{_bindir}/cqrlog
%{_datadir}/%{name}/
%{_datadir}/applications/cqrlog.desktop
%{_datadir}/pixmaps/cqrlog/cqrlog.png
%{_mandir}/man1/cqrlog.1.gz


%changelog
* Thu Jul 23 2015 Richard Shaw <hobbes1069@gmail.com> - 1.9.0-2
- Bump release for new build so it's newer than the temporary COPR builds.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar  6 2015 Richard Shaw <hobbes1069@gmail.com> - 1.9.0-1
- Update to latest upstream release.

* Fri Feb  6 2015 Richard Shaw <hobbes1069@gmail.com> - 1.8.3-1
- Update to latest upstream release.

* Fri Oct 24 2014 Eric "Sparks" Christensen <sparks@fedoraproject.org> - 1.8.1-4
- Allowing builds for ARM.

* Tue Sep 30 2014 Eric "Sparks" Christensen <sparks@fedoraproject.org> - 1.8.1-3
- Fixed empty debugging (BZ 1126233)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 28 2014 Eric "Sparks" Christensen <sparks@fedoraproject.org> - 1.8.1-1
- Program crashed with error about Exceptions.tbl when started for the first time
- After hit enter in New QSO window, it took long time to save QSO

* Mon Jul 21 2014 Eric "Sparks" Christensen <sparks@fedoraproject.org> - 1.8.0-1
- after click to "Upload all" qso to online logs, info about disabled services is not shown
- added new optimized MySQL configuration file (log should be faster and won't show error about missing tables)
- additional date formats for QSL label printing added (Tom, DL7BJ)
- alert for for callsign on specific mode and band added
- %h CW macro added (sends GM/GA/GE calculated from wkd station local time)
- %rs CW macro added (sends RST_S and replace 9 with N)
- design of gridlists can be changed in Preferences/Fonts/Gridlist settings (Tom, DL7BJ)
- additional options to split RST (TX and RX) in three fields for QSL label printing (Tom, DL7BJ)
- K3NG key support added
- "Use '+' key to add spots to band map" option added to Preferences -> Band map
- program crashed with error about Exceptions.tbl when started for the first time
- Shift+F12 didn't cancel the filtr - fixed
- "Filter is USED!" info wasn't canceled after click to Sort button (filter was disabled)
- reading signal strength from RBN spots fixed
- RBN default port is 7000 not 7300 - fixed
- fixed a bug in DXCC statistics, mode 'Paper QSL only' (Tom, DL7BJ)
- program crashed after close - fixed
- program crashed after click to Cancel in DB connection window
- sunrise, sunse and greeting info was broken - fixed
- xplanet opened from the "New QSO Window" was not centred on own lattitude and longitude

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 20 2014 Eric "Sparks" Christensen <sparks@fedoraproject.org> - 1.7.4-1
- F keys to CW type window added
- address to RBN server can be changed in Preferences
- full date (not only year,month) is supported in membership files
- Close the "Status of log upload" window after successful upload added
- moved to new LoTW url and updated upload routines
- band button description is editable (Preferences -> TRX control -> Change default frequencies)
- 6W/MM0NDX was marked as unknown country instead of Senegal - fixed
- after View QSO and CTRL+F2 fields was still read-only - fixed
- QSL information was added to Commend to QSO even if it already exists
- '+' character is now allowed in any field in New QSO window
- log could not recover from a wrong upload of updated QSO - fixed
- '+' as hotkey to add to bandmap function removed, use CTRL+A instead
- any result from ClubLog with 'Skipping QSO' won't stop uploading of the log

* Fri Feb 07 2014 Eric "Sparks" Christensen <sparks@fedoraproject.org> - 1.7.3-1
- after hitting ESC in any window opened from NewQSO, cursor will be returned to callsign edit field
- frequency in New QSO and QSO list wondow is formated to 0.0000
- added Help -> Keys and shortcut to menu in QSO window
- RBN integration into GrayLine showed CW speed instead of signal strench - fixed
- DXCC entity window didn't show when compiled in Debian Sid and Ubuntu 13.10 - fixed
- when CQRLOG was run for the first time, two mysqld proccesses opened the same database - fixed
- upload to ClubLog didn't work after enter QSO and delete - fixed (big thanks to Pawel, SQ5LTL)
- TRX control window's layout was broken with some font sizes - fixed

* Wed Jan 29 2014 Eric "Sparks" Christensen <sparks@fedoraproject.org> - 1.7.1-1
- "When TRX control is not active, use frequency and mode from NewQSO window" option to Preferences->Band map added
- CTRL+N hotkey to QSO list window added (do NOT send QSL)
- TRX control window was not sizeable - fixed
- when ESC was pressed twice in Remote mode, log crashed - fixed
- program crashed when freq was entered with comma as decimal separator - fixed
- broken grid square statistic fixed


* Wed Jan 15 2014 Eric "Sparks" Christensen <sparks@fedoraproject.org> - 1.7.0-1
- online QSO upload to HamQTH, ClubLog and HRDLog added
- improved QSL managers import, should be faster a bit
- "Long Path" button to Rotor Control added (Darek, SP2MKI)
- COMMENT field is exported to eQSL server
- Always overwrite info from previous QSO with callbook data option added
- help updated
- country files updated
- membership files updated
- layout improved (mostly new QSO window)
- LoTW QSL RCVD was not imported when ADIF didn't include LOTW_QSLRDATE value - fixed
- CONTESTIA mode was saved as CONSTESTI (increased max length of mode to 10 characters) - fixed
- ReverseBeacon support in Gray line didn't work - fixed
- after click to OK button in Preferences, bandmap stopped deleting old spots - fixed
- bandmap was not updated when any spot was not added - fixed
- station was added to bandmap when offline mode was activated - fixed
- big square statistics didn't work in newer versions of distributions - fixed
- QSO JT65* mode were not confirmed by eQSL - fixed

* Wed Dec 25 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.6.1-2
- Let rpmbuild strip executable (#1008236).

* Thu Nov 14 2013 Eric "Sparks" Christensen <sparks@fedoraproject.org> - 1.6.1-1
- 630M band added
- added OQRS (online QSL request system) to QSL sent menu
- added "Always sort by QSO date" option to Search function
- cursor is moved to last opened log in DB connection window
- "Ask before creating a backup" option to "Auto backup" added
- band map is much faster, a few optimization added
- program froze for a few milliseconds with every bandmap refresh - fixed
- "MySQL server has gone away" problem fixed
- membership values collation were case sensitive - fixed
- ADIF import sometimes crashed with access violation, now will show what happened
- qrz search with right click on a call in the recent QSOs list didn't work
- band map font settings was not loaded when program started

* Tue Sep 10 2013 Eric "Sparks" Christensen <sparks@fedoraproject.org> - 1.6.0-2
- Fixed rpmlint problems.

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
