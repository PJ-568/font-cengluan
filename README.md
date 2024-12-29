# ![演示](assets/display.png)

## font-xibo

<div style="display: flex; flex-direction: row; justify-content: space-between;">
  <div>

xibo 是一个为 Linux 设计的中文 TTY 字体，旨在在不安装诸如 [cjktty](https://github.com/zhmars/cjktty-patches) 等内核补丁且不安装 [kmscon](http://www.freedesktop.org/wiki/Software/kmscon)、[fbterm](https://salsa.debian.org/debian/fbterm) 或 [zhcon](https://zhcon.sourceforge.net/) 等第三方软件的环境下提供 TTY 中文显示。

本项目的灵感来源自 [syllazh](https://github.com/oldherl/syllazh/) 字体。

## 表音文字

在使用本字体时，您可能注意到——读音相近的汉字会被统一显示为同一个汉字，如：“用永勇拥擁涌湧咏詠蛹雍踊庸踴泳”中的任意一个汉字会被会统一显示为“用”。

这是因为 Linux TTY 上的字体一般用 kbd 软件包的 setfont 工具更换。它最多支持 512 个字形（glyph），但单个字形可以映射到多个 Unicode 码位。
因此，xibo 将所有忽略声调的音节相同的汉字都会被映射到同一个字形上，以实现在有限字形数下的汉字显示。

## 构建字体

1. 克隆仓库：

   ```shellscript
   git clone https://github.com/PJ-568/font-xibo.git
   cd font-xibo
   ```

2. 安装依赖项：

   ```shellscript
   pip install -r requirements.txt
   ```

3. 构建字体：

   ```shellscript
   bash build.bash
   ```

   在构建过程中，脚本会安装 `psftools`，用于生成字体。

构建完成后，会在 `output/` 生成一个名为 `xibo.psfu.gz` 的 PSF2 字体文件。

## 使用字体

> 请确保 `setfont` 命令的版本为 `2.6rc1` 或更高。
> 此版本之前的 setfont 不支持压缩前大于 65535（约 64KB）的字体。
> 在 `2.6rc1` 之后，上述限制放宽到了 4194304（约 4MB）。
>
> 执行 `setfont -V` 以检查版本。

将 `xibo.psfu.gz` 放入 `consolefonts` 目录下（在 Debian 中位于 `/usr/share/consolefonts/`、在 Arch Linux 中位于 `/usr/share/kbd/consolefonts/`），执行 `setfont xibo` 更换字体或执行 `setfont -d xibo` 切换到两倍大小的字体。

## 许可协议

本仓库中的脚本文件 `build.bash` 和 `build_font_from_bdf.py` 遵循 [GNU GENERAL PUBLIC LICENSE Version 3 许可协议](LICENSE)，
`original/references/` 目录下的所有参照文件遵循 [Unlicense 许可协议](original/references/LICENSE)，
本项目生成的字体文件遵循[自由中文字体和 GNU GENERAL PUBLIC LICENSE Version 2 许可协议](FONT-LICENSE)。

## 做出贡献

请参照[贡献指北](CONTRIBUTING.md)。

  </div>
  <div>

Xibo is a Chinese TTY font designed for Linux, aiming to provide Chinese display in TTY without installing kernel patches such as [cjktty](https://github.com/zhmars/cjktty-patches) or third-party software like [kmscon](http://www.freedesktop.org/wiki/Software/kmscon), [fbterm](https://salsa.debian.org/debian/fbterm), or [zhcon](https://zhcon.sourceforge.net/).

The inspiration for this project comes from the [syllazh](https://github.com/oldherl/syllazh/) font.

## Phonetic Characters

When using this font, you may notice that characters with similar pronunciations are displayed as the same character. For example, any of the characters “用永勇拥擁涌湧咏詠蛹雍踊庸踴泳” will be uniformly displayed as “用”.

This is because fonts on Linux TTY are generally changed using the `setfont` tool from the kbd package, which supports a maximum of 512 glyphs. However, a single glyph can map to multiple Unicode code points.
Therefore, Xibo maps all characters with the same pronunciation (ignoring tones) to the same glyph, allowing for Chinese character display within the limited number of glyphs.

## Building the Font

1. Clone the repository:

   ```shellscript
   git clone https://github.com/PJ-568/font-xibo.git
   cd font-xibo
   ```

2. Install dependencies:

   ```shellscript
   pip install -r requirements.txt
   ```

3. Build the font:

   ```shellscript
   bash build.bash
   ```

   During the build process, the script will install `psftools`, which is used to generate the font.

After building, a PSF2 font file named `xibo.psfu.gz` will be generated in the `output/` directory.

## Using the Font

> Ensure that the version of the `setfont` command is `2.6rc1` or higher.
> Versions prior to `2.6rc1` do not support fonts larger than 65535 (approximately 64KB).
> After `2.6rc1`, the limit has been relaxed to 4194304 (approximately 4MB).
>
> Run `setfont -V` to check the version.

Place `xibo.psfu.gz` in the `consolefonts` directory (located at `/usr/share/consolefonts/` on Debian and `/usr/share/kbd/consolefonts/` on Arch Linux), then execute `setfont xibo` to change the font or `setfont -d xibo` to switch to a double-sized font.

## License

The script files `build.bash` and `build_font_from_bdf.py` in this repository are licensed under the [GNU GENERAL PUBLIC LICENSE Version 3](LICENSE).
All reference files in the `original/references/` directory are licensed under the [Unlicense](original/references/LICENSE).
The generated font files in this project are licensed under the [Free Chinese Font License and GNU GENERAL PUBLIC LICENSE Version 2](FONT-LICENSE).

## Contributing

Refer to the [Contribution Guide](CONTRIBUTING.md).

  </div>
</div>
