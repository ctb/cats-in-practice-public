# The analysis pipeline

Code & data for the analysis pipeline for the 'cats in practice' paper.

## Running me

Create a directory with the
[spacegraphcats](https://github.com/spacegraphcats/spacegraphcats),
[cats-in-practice](https://github.com/TheoryInPractice/cats-in-practice/),
and [nullgraph](https://github.com/dib-lab/nullgraph) repos checked
out.

Make sure you have the requirements in `spacegraphcats/requirements.txt`
installed, as well as the `pydoit` package.

Then,
```
cd cats-in-practice/pipeline
make
```

This will produce files that are plotted in `someplots.ipynb`.
