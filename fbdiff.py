import argparse
import textwrap
from fontTools.ttLib import TTFont


def sorted_tags(ttf):
    """Return the table tags of ttf in the order of the file."""
    tables = ttf.reader.tables
    return sorted(tables.keys(), key=lambda tag: tables[tag].offset)


def main():
    parser = argparse.ArgumentParser(description="Compare the binary tables of two OpenType fonts.")
    parser.add_argument('-o', '--table-order', action="store_true",
                        help="show the table tags in sfnt order side-by-side")
    parser.add_argument('font_A', metavar="FONT_A", type=argparse.FileType("rb"),
                        help="an OpenType font file")
    parser.add_argument('font_B', metavar="FONT_B", type=argparse.FileType("rb"),
                        help="an OpenType font file")

    args = parser.parse_args()

    font_A = TTFont(args.font_A)
    font_B = TTFont(args.font_B)
    tags_A = set(font_A.reader.keys())
    tags_B = set(font_B.reader.keys())

    if args.table_order:
        sorted_tags_A = sorted_tags(font_A)
        sorted_tags_B = sorted_tags(font_B)
        sorted_tags_A.extend("    " for i in range(len(tags_B) - len(tags_A)))
        sorted_tags_B.extend("    " for i in range(len(tags_A) - len(tags_B)))
        assert len(sorted_tags_A) == len(sorted_tags_B)
        print("font A  font B  table order")
        print("------  ------")
        for tag_A, tag_B in zip(sorted_tags_A, sorted_tags_B):
            print(f"  {tag_A}    {tag_B}")
        print()

    if tags_A != tags_B:
        only_in_A = tags_A - tags_B
        only_in_B = tags_B - tags_A
        if only_in_A:
            print("Tables only in font A:")
            print(textwrap.fill(", ".join(sorted(only_in_A)),
                                initial_indent="  ", subsequent_indent="  "))
            print()
        if only_in_B:
            print("Tables only in font B:")
            print(textwrap.fill(", ".join(sorted(only_in_B)),
                                initial_indent="  ", subsequent_indent="  "))
            print()

    common_tags = sorted(tags_A & tags_B)
    max_length = 1
    for tag in common_tags:
        if font_A.reader.tables[tag].checkSum == font_B.reader.tables[tag].checkSum:
            continue
        max_length = max(max_length, font_A.reader.tables[tag].length)
        max_length = max(max_length, font_B.reader.tables[tag].length)
    max_digits = len(str(max_length))
    length_format = "{length:%dd}" % max_digits
    filler = " " * (max_digits - 1)

    did_print_header = False
    same_tables = []
    for tag in common_tags:
        data_A = font_A.reader[tag]
        data_B = font_B.reader[tag]
        if data_A != data_B:
            if not did_print_header:
                print(f"Different tables:")
                print(f"        {filler}A  {filler}B")
                did_print_header = True
            length_A = length_format.format(length=len(data_A))
            length_B = length_format.format(length=len(data_B))
            print(f"  {tag}  {length_A}  {length_B} bytes")
        else:
            same_tables.append(tag)

    if same_tables:
        if did_print_header:
            print()
        if set(same_tables) == tags_A == tags_B:
            print("Fonts are identical.")
        else:
            print("Identical tables:")
            print(textwrap.fill(", ".join(same_tables),
                                initial_indent="  ", subsequent_indent="  "))


if __name__ == "__main__":
    main()
