# How to display TESSCUT files

1. Run `curl -O "https://mast.stsci.edu/tesscut/api/v0.1/astrocut?ra=102.7&dec=-70.50&y=3&x=3"` in a bash console in the project directory. Substitute in the correct numbers for right ascension and declination.
2. Rename the resulting file to have a .zip extension and unzip it.
3. Use the URL `file://` and the path to the file as the url in the code in `display.py`.