all: acido-stuff

acido-stuff:
	./make-sim-catlas.py acido-chunk-reads data/acido-chunk[12].fa.gz
	./recover-reads.py acido-chunk-reads data/acido-chunk1.fa.sig.dump.txt \
		acido-chunk1.reads.fa.abundtrim acido-chunk1-1.extract.fa
	./recover-reads.py acido-chunk-reads data/acido-chunk1.fa.sig.dump.txt \
		acido-chunk2.reads.fa.abundtrim acido-chunk1-2.extract.fa
	./recover-reads.py acido-chunk-reads data/acido-chunk2.fa.sig.dump.txt \
		acido-chunk1.reads.fa.abundtrim acido-chunk2-2.extract.fa
	./recover-reads.py acido-chunk-reads data/acido-chunk2.fa.sig.dump.txt \
		acido-chunk2.reads.fa.abundtrim acido-chunk2-2.extract.fa

