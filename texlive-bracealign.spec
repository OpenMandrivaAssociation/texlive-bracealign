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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A LaTeX package to align braces under and over math expressions. A new
environment called bracealign is provided, inside which braces and
brackets drawn with the commands \underbrace, \overbrace, \underbracket,
\overbracket, \underparen or \overparenare vertically aligned. The
package also allows adding support for new commands.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/bracealign
%dir %{_datadir}/texmf-dist/source/latex/bracealign
%dir %{_datadir}/texmf-dist/tex/latex/bracealign
%doc %{_datadir}/texmf-dist/doc/latex/bracealign/LICENSE
%doc %{_datadir}/texmf-dist/doc/latex/bracealign/README.md
%doc %{_datadir}/texmf-dist/doc/latex/bracealign/bracealign-doc.sty
%doc %{_datadir}/texmf-dist/doc/latex/bracealign/bracealign.pdf
%doc %{_datadir}/texmf-dist/source/latex/bracealign/bracealign.dtx
%doc %{_datadir}/texmf-dist/source/latex/bracealign/bracealign.ins
%{_datadir}/texmf-dist/tex/latex/bracealign/bracealign.sty
