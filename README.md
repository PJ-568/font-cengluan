# ![演示](assets/display.png)

> 简体中文 | [ENGLISH](README.en.md)

## font-xibo

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

> 感谢**文泉驿**团队提供的`文泉驿点阵宋体 v1.0.0-RC1 英雄`字体。

本仓库中的脚本文件 `build.bash` 和 `build_font_from_bdf.py` 遵循 [GNU GENERAL PUBLIC LICENSE Version 3 许可协议](LICENSE)，
`original/references/` 目录下的所有参照文件遵循 [Unlicense 许可协议](original/references/LICENSE)，
本项目生成的字体文件遵循[自由中文字体和 GNU GENERAL PUBLIC LICENSE Version 2 许可协议](FONT-LICENSE)。

## 做出贡献

请参照[贡献指北](CONTRIBUTING.md)。
