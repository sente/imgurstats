grep -w  'url_effective' output/*.txt | cut -f2 > data.0
grep -w  'content_type' output/*.txt | cut -f2 > data.1
grep -w  'size_download' output/*.txt | cut -f2 > data.2


