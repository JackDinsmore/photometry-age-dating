# Ensemble Photometry Age Dating
This repository was started in May of 2020 by Jack Dinsmore to contain code for his REU project on inferring the age of unresolved stellar clusters by analyzing the light curve.

## 1. Solutions to bugs I encountered

### 1.1 Wrong lightcurves
When the lightcurve for a system seems totally wrong &mdash; like full of spikes that make it unrecognizable &mdash; I found it is often because the file(s) containing the data for the sector that that star is in may have been corrupted. The solution was to delete the file(s). Eleanor will then re-download it. 

On linux, or in the Ubuntu Subsystem for Windows, the apppropriate command is 

`rm -r /home/<user name>/.eleanor/metadata/s<sector num>`

where `<user name>` is your user name and `<sector num>` is the sector number, which you may have put in your `eleanor.Source` command. For WASP-100 b, it's `0001`.

If this fails, you can try deleting the entire `.eleanor` directory. You will know this worked if `eleanor.Source` downloads a file instead of printing `INFO: Found cached file`.... Hopefully, this solves the problem.


### 1.2. `'IOStream' object has no attribute 'flush'` error on Windows.
I got this error or something similar when I was trying to display matplotlib plots. The problem was that my Windows install of ipython was not complete. There may be a better way to fix this, but I moved to my Ubuntu installation of python, which worked perfectly.


## 2. File descriptions

- **FITS-tests** directory: this contains some code designed to view entire fits files as images &mdash; large scale images for display / visualization purposes. I don't think it's very scientifically useful.
- _'WASP-100-b-analysis.ipynb_: the `eleanor` tutorial. Start here.
- _hd-332231.ipynb_: a version of the `eleanor` tutorial where the star name is a variable that can be arbitrarily assigned.
- _tips-tricks.ipynb_: the tips and tricks tutorial on `eleanor` which describes things such as how to remove points from the lightcurve, change the aperture size, introduce your own corrections, and more.
- _vis-crossmatch.ipynb_: another `eleanor` tutorial which demonstrates some fun visualization and display tools. Drawing the aperture as a unfilled box over the star instead of a filled box, for instance, as well as drawing the light curves for each pixel of the aperture, highlighting known stars in the background of the aperture, and more.
- _HAT-P-11b; KELT-9b lightcurves.ipynb_: a sampling of different lightcurves for the exoplanets HAT-P-11b and KELT-9b. I made it on week 3.


## 3. Running the code

I use jupyter notebooks on my Ubuntu subsystem for windows. My Windows install's version of ipython does not work with eleanor, and bare python on the Ubuntu subsystem cannot display matplotlib plots. So I used jupyter notebooks. 

To run these notebooks (`.ipynb` files), install `jupyter notebook`, navigate in a bash terminal to the _photometry-age-dating_ directory, and run the command `jupyter notebook`. Copy and paste the URL into a browser. You can run and edit the code from the browser.
