# SQLite for Scientists

Slides for "SQLite for Scientists" talk at Research Software Engineering conference (RSECon24), Newcastle, 3 September 2024.

The slides are rendered online at: https://volcan01010.github.io/RSECon24/index.html.

Press s to activate Speaker View, which will also display additional speaker notes

You can download a version suitable for printing at https://volcan01010.github.io/RSECon24/index.html?print-pdf

Clone repository and view docs/index.html in browser to work on locally. An internet connection is necessary to view some images, which are served via external links.

Videos were created with Microsoft Snipping tool, but compressed significantly via the following FFMPEG command:

```bash
ffmpeg -i original.mp4 -vcodec libx264 -crf 24 small.mp4
```

White images to hide "r-stretch" images (which don't work with "fragment") created by:

```bash
convert image.png -fill white -colorize 100% image_white.png
```
