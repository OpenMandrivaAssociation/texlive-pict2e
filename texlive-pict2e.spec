# revision 32658
# category Package
# catalog-ctan /macros/latex/contrib/pict2e
# catalog-date 2014-01-13 11:26:35 +0100
# catalog-license lppl
# catalog-version 0.2z
Name:		texlive-pict2e
Version:	0.2z
Release:	2
Summary:	New implementation of picture commands
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pict2e
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pict2e.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pict2e.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pict2e.source.tar.xz
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
%{_texmfdistdir}/tex/latex/pict2e/p2e-dvipdfm.def
%{_texmfdistdir}/tex/latex/pict2e/p2e-dvipdfmx.def
%{_texmfdistdir}/tex/latex/pict2e/p2e-dvips.def
%{_texmfdistdir}/tex/latex/pict2e/p2e-pctex32.def
%{_texmfdistdir}/tex/latex/pict2e/p2e-pctexps.def
%{_texmfdistdir}/tex/latex/pict2e/p2e-pdftex.def
%{_texmfdistdir}/tex/latex/pict2e/p2e-textures.def
%{_texmfdistdir}/tex/latex/pict2e/p2e-vtex.def
%{_texmfdistdir}/tex/latex/pict2e/p2e-xetex.def
%{_texmfdistdir}/tex/latex/pict2e/pict2e.cfg
%{_texmfdistdir}/tex/latex/pict2e/pict2e.sty
%doc %{_texmfdistdir}/doc/latex/pict2e/README
%doc %{_texmfdistdir}/doc/latex/pict2e/manifest.txt
%doc %{_texmfdistdir}/doc/latex/pict2e/p2e-drivers.pdf
%doc %{_texmfdistdir}/doc/latex/pict2e/pict2e.pdf
#- source
%doc %{_texmfdistdir}/source/latex/pict2e/p2e-drivers.dtx
%doc %{_texmfdistdir}/source/latex/pict2e/pict2e.dtx
%doc %{_texmfdistdir}/source/latex/pict2e/pict2e.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
