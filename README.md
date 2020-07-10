# Ensemble Photometry Age Dating

This repository was started in May of 2020 by Jack Dinsmore to contain code for his REU project on inferring the age of unresolved stellar clusters by analyzing the light curve.

## 1. Solutions to bugs I encountered

### 1.1 Huge spikes in lightcurves

When the lightcurve for a system seems totally wrong &mdash; like full of spikes that make it unrecognizable &mdash; I found it is often because the file(s) containing the data for the sector that that star is in may have been corrupted. The solution was to delete the file(s). `eleanor` will then re-download it.

There are three places where files need to be deleted.

1. When the `eleanor.Source` command is called, eleanor will print out several “INFO: Found cached file \<file name\>…” messages. Navigate to the directory containing these files and delete the directory.
1. Delete the `.eleanor/metadata/s<sector num>` directory, where `<sector num>` is the sector that the star was observed in; it will be part of the name of the directory you deleted in step 1.
1. If `eleanor.Source` outputs one final "INFO: Found cached file..." line, but this time the file name is just a name and not a path, navigate to the `.eleanor` directory and delete this file.

You may need to try re-running the `eleanor.Source` command several times, each time deleting all these files, before you can find them all. But if this fails, you can try deleting the entire `.eleanor` directory.

### 1.2. `'IOStream' object has no attribute 'flush'` error on Windows

I got this error or something similar when I was trying to display matplotlib plots. The problem was that my Windows install of ipython was not complete. There may be a better way to fix this, but I moved to my Ubuntu installation of python, which worked perfectly.

### 1.3 `'TargetData' object has no attribute`... errors

I got these errors when the cached data for the star had been corrupted. The solution is to delete all the cached data. The process to do this is described in the solution to 1.1.

### 1.4 Transits appear as vague spikes above and below the mean, not just below

This happened to me when I flattened the lightcurves using the `lightkurve` flatten command. Try not flattening the data; the transits may show up more clearly where they are supposed to be. Oddly, this feature only appeared when I was using a Tess lightcurve, not Kepler.

## 2. File descriptions

- _'WASP-100-b-analysis.ipynb_: the `eleanor` tutorial. Start here.
- _hd-332231.ipynb_: a version of the `eleanor` tutorial where the star name is a variable that can be arbitrarily assigned.
- _tips-tricks.ipynb_: the tips and tricks tutorial on `eleanor` which describes things such as how to remove points from the lightcurve, change the aperture size, introduce your own corrections, and more.
- _vis-crossmatch.ipynb_: another `eleanor` tutorial which demonstrates some fun visualization and display tools. Drawing the aperture as a unfilled box over the star instead of a filled box, for instance, as well as drawing the light curves for each pixel of the aperture, highlighting known stars in the background of the aperture, and more.
- _HAT-P-11b; KELT-9b lightcurves.ipynb_: a sampling of different lightcurves for the exoplanets HAT-P-11b and KELT-9b. I made it on week 3.
- _detrending-eleanor.ipynb_: a notebook that loads the tpfs of a sample star using `eleanor` and transfers them to `lightkurve` for detrending analysis.

- **cluster-lightcurves/**_cluster-\*.ipynb_: a program to download the TPFs of certain clusters and generate background-corrected lightcurves.
- **cluster-lightcurves/**_fourier-transform-tests.ipynb_: a program investigating the possibility of using a fourier decomposition of a frame in a cluster's TPF to help generate the sky mask
- **cluster-lightcurves/**_\*.png_: images collected from _cluster-\*.ipynb_. Most of them are screenshots of the lightcurves from three test clusters to determine what method for isolating the background is most effective.

## 3. Running the code

I use jupyter notebooks on my Ubuntu subsystem for windows. My Windows install's version of ipython does not work with eleanor, and bare python on the Ubuntu subsystem cannot display matplotlib plots. So I used jupyter notebooks.

To run these notebooks (`.ipynb` files), install `jupyter notebook`, navigate in a bash terminal to the _photometry-age-dating_ directory, and run the command `jupyter notebook`. Copy and paste the URL into a browser. You can run and edit the code from the browser.

## 4. `eleanor` bugs

- Sometimes, the fits files for some eleanor stars becomes corrupted. I am unsure what causes this exactly, but it happened to me and other people several times. It may have something to do with `eleanor.TargetData.save()`. I encountered this error by running the tips and tricks tutorial. Specifically, when you reload the star with `eleanor.Source`, get the data with `eleanor.TargetData`, and then call `get_lightcurve` on the data, the error `"'TargetData' object has no attribute 'tpf_flux_bkg'` is thrown.\
\
My solution was to delete the cached fits files (both in the `~/.eleanor/mastDownload/HLSP/hlsp_...` directory and the one in the `~/.eleanor` directory), and delete the directory containing the metadata of the corresponding sector. Then I could redo the `Source` command and redownload everything and it worked.\
\
My suggestion would be to add an optional argument `use_cache=True` or something to the `Source` command which would clear the current cache for the star and redownload everything if set to `False`.
