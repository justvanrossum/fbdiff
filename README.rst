fbdiff
~~~~~~

`fbdiff` is a tool that reports a brief summary of table differences
in OpenType fonts. It reports which tables exist in only one of the
fonts, and it will report which common tables are different and which
are identical.

It only looks at the binary data: tables are not parsed.

Example usage:

.. code:: sh

	$ fbdiff fontA.ttf fontB.ttf
    Tables only in font B:
      meta

	Different tables:
	            A      B
	  GPOS  29628  29574 bytes
	  STAT     28    162 bytes
	  fpgm   4095   4078 bytes
	  glyf  36984  26626 bytes
	  head     54     54 bytes
	  loca    940    940 bytes
	  name   3078   4557 bytes
	  prep   1339   1339 bytes

    Identical tables:
      GDEF, GSUB, HVAR, OS/2, TSI0, TSI1, TSI2, TSI3, TSI5, TSIC, VDMX,
      avar, cmap, cvar, cvt , fvar, gasp, gvar, hhea, hmtx, maxp, post

Help text:

.. code:: sh

	$ fbdiff --help
	usage: fbdiff [-h] [-o] FONT_A FONT_B

	Compare the binary tables of two OpenType fonts.

	positional arguments:
	  FONT_A             an OpenType font file
	  FONT_B             an OpenType font file

	optional arguments:
	  -h, --help         show this help message and exit
	  -o, --table-order  show the table tags in sfnt order side-by-side
