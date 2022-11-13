Name:		texlive-simplecv
Version:	35537
Release:	1
Summary:	A simple class for writing curricula vitae
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/simplecv
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/simplecv.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/simplecv.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/simplecv.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A derivative of the cv class available to lyx users (renamed to
avoid the existing cv package).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/simplecv
%doc %{_texmfdistdir}/doc/latex/simplecv
#- source
%doc %{_texmfdistdir}/source/latex/simplecv

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
