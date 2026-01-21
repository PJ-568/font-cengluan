# ![Demo](assets/display.png)

> ENGLISH | [简体中文](README.md)

## font-cengluan（Cengluan TTY Font）

cengluan is a Chinese TTY font designed for Linux, aiming to provide Chinese display in TTY without installing kernel patches like [cjktty](https://github.com/zhmars/cjktty-patches), nor third-party software such as [kmscon](http://www.freedesktop.org/wiki/Software/kmscon), [fbterm](https://salsa.debian.org/debian/fbterm), or [zhcon](https://zhcon.sourceforge.net/).

This project is inspired by the [syllazh](https://github.com/oldherl/syllazh/) font.

### Phonetic Characters

When using this font, you may notice that Chinese characters with similar pronunciations are displayed as the same character. For example: any character from "用永勇拥擁涌湧咏詠蛹雍踊庸踴泳" will be uniformly displayed as "用".

This is because fonts on Linux TTY are generally changed using the setfont tool from the kbd package, which supports up to 512 glyphs, but a single glyph can be mapped to multiple Unicode code points. Therefore, font-cengluan maps all Chinese characters with the same syllable (ignoring tones) to the same glyph, enabling Chinese display with a limited number of glyphs.

### Terminal Graphic Program Display Optimization

This font also optimizes the mapping of commonly used graphic symbols in terminals to make it more suitable for terminal use. Some examples:

- Original symbols:

  ```plaintext
  ┌───┬───┐
  │   │   │
  ├───┼───┤
  │   │   │
  └───┴───┘
  ```

- Before optimization:

  ```plaintext
  ?????????
  ?   ?   ?
  ?????????
  ?   ?   ?
  ?????????
  ```

  (Cannot be displayed properly)

- After optimization:

  ```plaintext
  r---T---7
  |   |   |
  ├---+---┤
  |   |   |
  L---┴---J
  ```

  Here, `┌` is mapped to the letter `r`, `┬` to `T`, `┘` to `J`, etc.
  Such mappings maximize display improvement while minimizing the use of additional glyphs (:-D).

### Character Width Display Optimization

In conventional text display scenarios:

- **Full-width characters** (such as Chinese characters and symbols in GB2312) have a display width of two units (occupying two character positions) and a height of one character row (occupying one line height);
- **Half-width characters** (such as English letters, Arabic numerals, and ASCII punctuation) have a display width of one unit and the same height of one character row.

That is: Chinese characters and symbols in GB2312 encoding are full-width, while ASCII characters and English symbols (like commas, periods) are typically half-width.

However, PC Screen Font 2 (PSF2) is a fixed-width bitmap font format that does not support characters of different sizes (widths) within a single font. Consequently:

- If all characters are displayed with a width of one unit: full-width characters only show the left half, with the right half displayed as the [32nd character](#the-32nd-character);
- If all characters are displayed with a width of two units: all half-width characters occupy two columns, but visually they are only one unit wide, resulting in [large gaps between two half-width characters](assets/display_old_old.png).

Given the high difficulty of finding or designing "tall, thin half-width monospaced Chinese character fonts" or "compatible full-width English letter fonts", font-cengluan adopts two design approaches:

1. Map all English letters, Arabic numerals, ASCII punctuation, and similar characters to full-width characters in the UTF-8 high range;
   the spacing between half-width characters remains slightly large.

   ![Full-width font-cengluan performance in btop](assets/btop_old.png)

2. Display all half-width characters with integer scaling doubled, while full-width characters are displayed at their original scaling ratio with padded blank lines above and below.

   ![Half-width scaling, full-width complement](assets/Half-width_characters_extended__full-width_characters_complemented.svg)
   ![New approach look](assets/display_new.png)
   ![Half-width scaling, full-width complement font-cengluan performance in btop](assets/btop.png)

Although each full-width character is still separated on the right by a [32nd character](#the-32nd-character), font-cengluan achieves a relatively balanced visual appearance overall.

### The 32nd Character

In Linux TTY, the 32nd character of the default font is `U+20`, i.e., a space. This character is used to fill positions in the background where no character is present.

## Get the Font

### Downloading the Font

- [Download the font](https://github.com/PJ-568/font-cengluan/releases/latest)

### Building the Font

1. Clone the repository:

   ```shellscript
   git clone https://github.com/PJ-568/font-cengluan.git
   cd font-cengluan
   ```

2. Install dependencies:

   ```shellscript
   pip install -r requirements.txt
   ```

3. Build the font:

   ```shellscript
   bash build.bash
   ```

   During the build process, the script will install `psftools` for font generation.

After building, a PSF2 font file named `cengluan.psfu.gz` will be generated in the `output/` directory.

## Using the Font

> Ensure the `setfont` command is version `2.6rc1` or higher.
> Versions before `2.6rc1` do not support fonts larger than 65535 bytes (≈64KB) before compression.
> After `2.6rc1`, this limit was raised to 4194304 bytes (≈4MB).
>
> Run `setfont -V` to check the version.

Place `cengluan.psfu.gz` into the `consolefonts` directory (located at `/usr/share/consolefonts/` in Debian, `/usr/share/kbd/consolefonts/` in Arch Linux). Then run `setfont cengluan` to change the font, or `setfont -d cengluan` to switch to double-sized font.

## License

> Thanks to **[oldherl](https://github.com/oldherl)** for the forward-looking technical exploration project [syllazh](https://github.com/oldherl/syllazh/);
>
> Thanks to **[TakWolf](https://github.com/TakWolf)** and their team for providing the [fusion-pixel-font](https://github.com/TakWolf/fusion-pixel-font) font.

The script files `build.bash`, `build_font_from_bdf.py`, and all files in `scripts/` in this repository follow the [GNU GENERAL PUBLIC LICENSE Version 3](LICENSE).
`original/references/pinyin_hanzi` in the `original/references/` directory follows the GNU Lesser General Public License (LGPL) 2.1, while other reference files follow the [Unlicense](original/references/LICENSE).
The font files generated by this project follow either the [MIT License](MIT-LICENSE) or the [SIL OPEN FONT LICENSE Version 1.1](SIL-LICENSE). For original font upstream licenses, see the files under [`FONT-LICENSE/`](FONT-LICENSE/).

## Contributing

Refer to the [Contribution Guide](CONTRIBUTING.md).
