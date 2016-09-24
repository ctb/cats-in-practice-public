all: acido-sim-catlas acido-genome-catlas acido-reads-catlas

clean:
	./make-sim-catlas.py acido-chunk-reads data/acido-chunk[12].fa.gz --clean
	./make-genome-catlas.py acido-genome data/acido-chunk[12].fa.gz --clean
	./recover-reads.py acido-chunk-reads data/acido-chunk1.fa.sig.dump.txt \
		acido-chunk1.reads.fa.abundtrim acido-chunk1-1.extract.fa --clean
	./recover-reads.py acido-chunk-reads data/acido-chunk1.fa.sig.dump.txt \
		acido-chunk2.reads.fa.abundtrim acido-chunk1-2.extract.fa --clean
	./recover-reads.py acido-chunk-reads data/acido-chunk2.fa.sig.dump.txt \
		acido-chunk1.reads.fa.abundtrim acido-chunk2-1.extract.fa --clean
	./recover-reads.py acido-chunk-reads data/acido-chunk2.fa.sig.dump.txt \
		acido-chunk2.reads.fa.abundtrim acido-chunk2-2.extract.fa --clean
	./make-reads-catlas.py acido-reads-catlas acido-chunk[12].reads.fa --clean
	rm -fr acido-genome acido-chunk-reads acido-reads-catlas

acido-sim-catlas:
	./make-sim-catlas.py acido-chunk-reads data/acido-chunk[12].fa.gz
	./recover-reads.py acido-chunk-reads data/acido-chunk1.fa.sig.dump.txt \
		acido-chunk1.reads.fa.abundtrim acido-chunk1-1.extract.fa
	./recover-reads.py acido-chunk-reads data/acido-chunk1.fa.sig.dump.txt \
		acido-chunk2.reads.fa.abundtrim acido-chunk1-2.extract.fa
	./recover-reads.py acido-chunk-reads data/acido-chunk2.fa.sig.dump.txt \
		acido-chunk1.reads.fa.abundtrim acido-chunk2-1.extract.fa
	./recover-reads.py acido-chunk-reads data/acido-chunk2.fa.sig.dump.txt \
		acido-chunk2.reads.fa.abundtrim acido-chunk2-2.extract.fa

acido-genome-catlas:
	./make-genome-catlas.py acido-genome data/acido-chunk[12].fa.gz

acido-reads-catlas: acido-sim-catlas
	./make-reads-catlas.py acido-reads-catlas acido-chunk[12].reads.fa
