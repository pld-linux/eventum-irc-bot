%define		php_min_version 5.6.0
Summary:	Eventum IRC Notification Bot
Summary(pl.UTF-8):	IRC-owy bot powiadamiający dla Eventum
Name:		eventum-irc-bot
Version:	1.0.0
Release:	0.2
License:	GPL v2+
Group:		Networking/Utilities
Source0:	https://github.com/eventum/irc-bot/archive/master/%{name}-%{version}-p2.tar.gz
# Source0-md5:	a9bd2dcf229b6212b4ac2a417d10af4c
URL:		https://github.com/eventum/scm
Requires:	php(sockets)
Requires:	php-pear-Net_SmartIRC >= 1.1.9
Provides:	eventum-irc = 4.4.0
Obsoletes:	eventum-irc < 4.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		appdir		%{_datadir}/%{name}
%define		confdir		%{_sysconfdir}/%{name}

%description
The IRC notification bot is a nice feature for remote teams that want
to handle issues and want to have a quick and easy way to get simple
notifications. Right now the bot notifies of the following actions:
- New Issues
- Blocked emails
- Issues that got their assignment list changed

NOTE: You will need to manually edit the bot.php script to set your
appropriate preferences, like IRC server and channel that the bot
should join.

%description -l pl.UTF-8
IRC-owy bot powiadamiający to miła funkcjonalność dla zdalnych
zespołów chcących obsługiwać sprawy i mieć szybki i łatwy sposób na
uzyskiwanie prostych powiadomień. Aktualnie bot powiadamia o
następujących zdarzeniach:
- nowych sprawach
- zablokowanych listach
- sprawach, dla których zmieniła się lista powiązań

UWAGA: w celu wprowadzenia własnych ustawień, takich jak serwer IRC i
kanał używany przez bota, trzeba ręcznie zmodyfikować skrypt bot.php .

%prep
%setup -qc
mv irc-bot-*/* .
mv config/{config.dist.php,config.php}

%build
composer install --no-dev -o

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{appdir},%{confdir}}
cp -a bin src vendor $RPM_BUILD_ROOT%{appdir}
cp -a config/*.php $RPM_BUILD_ROOT%{confdir}
ln -s %{confdir} $RPM_BUILD_ROOT%{appdir}/config

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%dir %{confdir}
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{confdir}/config.php
%attr(755,root,root) %{appdir}/bin/irc-bot.php
%dir %{appdir}
%dir %{appdir}/bin
%{appdir}/config
%{appdir}/src
%{appdir}/vendor
