# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/simplecv
# catalog-date 2008-08-23 15:48:35 +0200
# catalog-license lppl
# catalog-version 1.6
Name:		texlive-simplecv
Version:	1.6
Release:	8
Summary:	A simple class for writing curricula vitae
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/simplecv
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/simplecv.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/simplecv.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/simplecv.source.tar.xz
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
%{_texmfdistdir}/tex/latex/simplecv/simplecv.cls
%doc %{_texmfdistdir}/doc/latex/simplecv/README
%doc %{_texmfdistdir}/doc/latex/simplecv/testcv.pdf
%doc %{_texmfdistdir}/doc/latex/simplecv/testcv.tex
#- source
%doc %{_texmfdistdir}/source/latex/simplecv/simplecv.dtx
%doc %{_texmfdistdir}/source/latex/simplecv/simplecv.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.6-2
+ Revision: 756027
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.6-1
+ Revision: 719537
- texlive-simplecv
- texlive-simplecv
- texlive-simplecv
- texlive-simplecv

