# An efficient method for decomposition and search of large compact De Bruijn
graphs.

## Introduction

Compact De Bruijn graphs (cDBG) are commonly used in biological sequence
analysis.

Dominating sets have been used to discover components in very large De
Bruijn graphs (Pell et al., 2012, PNAS).  (Some discussion of
dominating sets and/or sparse graph similarity in concepts?)  They are
potentially useful ways to investigate large scale graph structure but
are (a) large and (b) expensive to calculate, both in theory and in
practice.

Some theoretical work (DTF) has shown a method for efficiently
calculating dominating sets on graphs with bounded degree.

We apply DTF to cDBG and build an efficient search structure for
sequence content in cDBG.

## Results

1. DTF enables efficient calculation of dominating sets for large cDBG.

2. The 'atlas' data structure represents a hierarchy of dominating sets.

3. Piecewise composition of MinHash sketches on the atlas allows efficient
   search for cDBG content.
   
4. This can be used for taxonomic analysis and comparison of large
   sequencing data sets.

## Discussion

