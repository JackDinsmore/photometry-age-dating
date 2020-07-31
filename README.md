# Ensemble Photometry Age Dating

This repository was started in May of 2020 by Jack Dinsmore to contain code for his REU project on inferring the age of unresolved stellar clusters by analyzing the light curve.


## 1. Directory descriptions

For descriptions of the purposes of a certain jupyter notebook, read the text at the top of the notebook. Below are descriptions for directories.

- **initial-studies/\***: Several tutorials on `eleanor` and `lightkurve` which I did to get used to the code.

- **cluster-lightcurves/**_cluster-\*.ipynb_: programs to download the TPFs of certain clusters and generate background-corrected lightcurves. In its current state, this directory tests and uses the maxima method. Main file: _cluster-lightcurves-series.ipynb_

- **cluster-lightcurves/fourier-tests/***: investigates the possibility of using a fourier decomposition of a frame in a cluster's TPF to help generate the sky mask.

- **cluster-lightcurves/tests/\***: images collected from _cluster-\*.ipynb_. Most of them are screenshots of the lightcurves from three test clusters to determine what method for isolating the background is most effective, while _scale-factor-tests.png_ tests different scale factors on one cluster to determine an optimal choice.

- **astroquery-lightcurves/\***: programs to calculate (or download from CDIPS) the lightcurves of stars nearby the clusters we're investigating so that we can pinpoint the variations in the cluster lightcurve to individual stars and also check our cluster lightcurves by seeing how they compare to the sum of the lightcurves of the component stars. Main file: _compare-cdips-ourselves.ipynb_

- **tpf-zoom-in/\***: we started to try to isolate varying lightcurves to sections of the TPF; these programs cut the TPF into pieces and create lightcurves for each piece. Main file: _isolating-variable-stars.ipynb_

## 2. Running the code

I use jupyter notebooks on my Ubuntu subsystem for windows. My Windows install's version of ipython does not work with eleanor, and bare python on the Ubuntu subsystem cannot display matplotlib plots. So I used jupyter notebooks.

To run these notebooks (`.ipynb` files), install `jupyter notebook`, navigate in a bash terminal to the _photometry-age-dating_ directory, and run the command `jupyter notebook`. Copy and paste the URL into a browser. You can run and edit the code from the browser.

## 3. `eleanor` bugs

- Sometimes, the fits files for some eleanor stars becomes corrupted. I am unsure what causes this exactly, but it happened to me and other people several times. It may have something to do with `eleanor.TargetData.save()`. I encountered this error by running the tips and tricks tutorial. Specifically, when you reload the star with `eleanor.Source`, get the data with `eleanor.TargetData`, and then call `get_lightcurve` on the data, the error `"'TargetData' object has no attribute 'tpf_flux_bkg'` is thrown.\
\
My solution was to delete the cached fits files (both in the `~/.eleanor/mastDownload/HLSP/hlsp_...` directory and the one in the `~/.eleanor` directory), and delete the directory containing the metadata of the corresponding sector. Then I could redo the `Source` command and redownload everything and it worked.\
\
My suggestion would be to add an optional argument `use_cache=True` or something to the `Source` command which would clear the current cache for the star and redownload everything if set to `False`.
