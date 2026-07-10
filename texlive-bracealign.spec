%global tl_name bracealign
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Align braces under and over math expressions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bracealign
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bracealign.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bracealign.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bracealign.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A LaTeX package to align braces under and over math expressions. A new
environment called bracealign is provided, inside which braces and
brackets drawn with the commands \underbrace, \overbrace, \underbracket,
\overbracket, \underparen or \overparenare vertically aligned. The
package also allows adding support for new commands.

