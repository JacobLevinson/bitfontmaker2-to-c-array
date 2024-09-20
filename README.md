# bitfontmaker2-to-c-array
Python script for converting json output from bitfontmaker2 to a c array for use in a c program.

Use the website https://www.pentacom.jp/pentacom/bitfontmaker2/ to create
a bitmap font for the printable ascii characters, then click on the export
icon. Copy and paste the json into the script where it specifies and run the
script; it will output the c array needed for bitmap ascii in c.

Example of how you can render this font can be found at 
https://github.com/fantasticmao/font6x8.

## Tips
1. Make your glyphs in the bottom left of the grid at the website.
2. The script is currently for 6x8 glyphs. You can easily modify it to support
other widths by replacing the 6's.
