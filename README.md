# fbdiff

Tool to show a brief summary of table differences in OpenType fonts

Example usage:

	$ fbdiff fontA.ttf fontB.ttf
    Tables only in font B:
      meta

    Different tables:        A      B
      GPOS is different  29628  29574 bytes
      STAT is different     28    162 bytes
      fpgm is different   4095   4078 bytes
      glyf is different  36984  26626 bytes
      head is different     54     54 bytes
      loca is different    940    940 bytes
      name is different   3078   4557 bytes
      prep is different   1339   1339 bytes

    Identical tables:
      GDEF, GSUB, HVAR, OS/2, TSI0, TSI1, TSI2, TSI3, TSI5, TSIC, VDMX,
      avar, cmap, cvar, cvt , fvar, gasp, gvar, hhea, hmtx, maxp, post
