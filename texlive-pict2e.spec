Name:		texlive-pict2e
Version:	56504
Release:	2
Summary:	New implementation of picture commands
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pict2e
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pict2e.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pict2e.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pict2e.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package was described in the 2nd edition of 'LaTeX: A
Document Preparation System', but the LaTeX project team
declined to produce the package. For a long time, LaTeX has
included a 'pict2e package' that merely produced an apologetic
error message. The new package extends the existing LaTeX
picture environment, using the familiar technique (cf. the
graphics and color packages) of driver files (at present,
drivers for PostScript output from LaTeX, and for use with
PDFLaTeX are available). The package documentation has a fair
number of examples of use, showing where things are improved by
comparison with the LaTeX picture environment.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pict2e
%doc %{_texmfdistdir}/doc/latex/pict2e
#- source
%doc %{_texmfdistdir}/source/latex/pict2e

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
