%global tl_name pict2e
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.4b
Release:	%{tl_revision}.1
Summary:	New implementation of picture commands
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pict2e
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pict2e.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pict2e.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pict2e.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package was described in the 2nd edition of 'LaTeX: A Document
Preparation System', but the LaTeX project team declined to produce the
package. For a long time, LaTeX included a 'pict2e package' that merely
produced an apologetic error message. The new package extends the
existing LaTeX picture environment, using the familiar technique (cf.
the graphics and color packages) of driver files (at present, drivers
for dvips, pdfTeX, LuaTeX, XeTeX, VTeX, dvipdfm, and dvipdfmx are
available). The package documentation has a fair number of examples of
use, showing where things are improved by comparison with the LaTeX
picture environment.

