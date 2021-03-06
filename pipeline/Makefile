SPG=../../spacegraphcats

all: acido-sim-catlas acido-genome-catlas acido-reads-catlas \
	15genome-catlas \
	15genome-catlas-gathermins.csv 15genome-catlas-fjacc.csv \
	15genome-catlas-fworst.csv

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
	./make-genome-catlas.py 15genome data/15genome.fa.gz -M 4e9 --clean
	rm -fr acido-genome acido-chunk-reads acido-reads-catlas 15genome

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
	$(SPG)/search-for-domgraph-nodes.py \
		--strategy frontier-jacc \
		acido-genome 3 data/acido-chunk[12].fa.sig.dump.txt
	$(SPG)/search-for-domgraph-nodes.py \
		--strategy frontier-worst \
		acido-genome 3 data/acido-chunk[12].fa.sig.dump.txt
	$(SPG)/search-for-domgraph-nodes.py \
		--strategy frontier-jacc \
		acido-genome 3 data/acido-chunk1.fa.sig.dump.txt
	$(SPG)/search-for-domgraph-nodes.py \
		--strategy frontier-worst \
		acido-genome 3 data/acido-chunk1.fa.sig.dump.txt

acido-reads-catlas: acido-sim-catlas
	./make-reads-catlas.py acido-reads-catlas acido-chunk[12].reads.fa

15genome-catlas:
	./make-genome-catlas.py 15genome data/15genome.fa.gz -M 4e9

15genome/15genome.gxt: 15genome-catlas

15genome-catlas-gathermins.csv: 15genome/15genome.gxt
	-rm -f 15genome-catlas-gathermins.csv
	$(SPG)/search-for-domgraph-nodes.py \
		--strategy gathermins2 --searchlevel 3 \
		15genome 3 \
		$(SPG)/data/15genome.fa.?.sig.dump.txt \
		$(SPG)/data/15genome.fa.??.sig.dump.txt \
		--append-csv 15genome-catlas-gathermins.csv

15genome-catlas-fjacc.csv: 15genome/15genome.gxt
	-rm -f 15genome-catlas-fjacc.csv
	$(SPG)/search-for-domgraph-nodes.py \
		--strategy frontier-jacc \
		15genome 3 \
		$(SPG)/data/15genome.fa.?.sig.dump.txt \
		$(SPG)/data/15genome.fa.??.sig.dump.txt \
		--append-csv 15genome-catlas-fjacc.csv

15genome-catlas-fworst.csv: 15genome/15genome.gxt
	-rm -f 15genome-catlas-fworst.csv
	$(SPG)/search-for-domgraph-nodes.py \
		--strategy frontier-worst \
		15genome 3 \
		$(SPG)/data/15genome.fa.?.sig.dump.txt \
		$(SPG)/data/15genome.fa.??.sig.dump.txt \
		--append-csv 15genome-catlas-fworst.csv
