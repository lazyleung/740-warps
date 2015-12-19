#!/bin/bash

TARGET=run_CAWA

now=$(date +"%T")
echo "$now Running backprop"
cp configs/$TARGET/5000.config $TARGET/gpgpusim.config
cp backprop $TARGET/backprop
cd $TARGET
./backprop 65536 > out_backprop.txt
echo ""
cd ..

now=$(date +"%T")
echo "$now Running bfs"
cp configs/$TARGET/5000.config $TARGET/gpgpusim.config
cp bfs $TARGET/bfs
cd $TARGET
./bfs ../../data/bfs/graph65536.txt > out_bfs.txt
echo ""
cd ..

now=$(date +"%T")
echo "$now Running b+tree"
cp configs/$TARGET/5000.config $TARGET/gpgpusim.config
cp b+tree $TARGET/b+tree
cd $TARGET
./b+tree file ../../data/b+tree/mil.txt command ../../data/b+tree/command.txt > out_b+tree.txt
echo ""
cd ..

now=$(date +"%T")
echo "$now Running cfd"
cp configs/$TARGET/500.config $TARGET/gpgpusim.config
cp euler3d $TARGET/euler3d
cd $TARGET
./euler3d ../../data/cfd/fvcorr.domn.097K > out_cfd.txt
echo ""
cd ..

now=$(date +"%T")
echo "$now Running gaussian"
cp configs/$TARGET/5000.config $TARGET/gpgpusim.config
cp gaussian $TARGET/gaussian
cd $TARGET
./gaussian -f ../../data/gaussian/matrix16.txt > out_gaussian0.txt
./gaussian -s 16 > out_gaussian1.txt
echo ""
cd ..

now=$(date +"%T")
echo "$now Running heartwall"
cp configs/$TARGET/50.config $TARGET/gpgpusim.config
cp heartwall $TARGET/heartwall
cd $TARGET
./heartwall ../../data/heartwall/test.avi 5 > out_heartwall.txt
echo ""
cd ..

now=$(date +"%T")
echo "$now Running hotspot"
cp configs/$TARGET/5000.config $TARGET/gpgpusim.config
cp hotspot $TARGET/hotspot
cd $TARGET
./hotspot 64 2 2 ../../data/hotspot/temp_64 ../../data/hotspot/power_64 output_hotspot.out > out_hotspot.txt
echo ""
cd ..

now=$(date +"%T")
echo "$now Running kmeans"
cp configs/$TARGET/500.config $TARGET/gpgpusim.config
cp kmeans $TARGET/kmeans
cd $TARGET
./kmeans -o -i ../../data/kmeans/kdd_cup > out_kmeans.txt
echo ""
cd ..

now=$(date +"%T")
echo "$now Running leukocyte"
cp configs/$TARGET/500.config $TARGET/gpgpusim.config
cp leukocyte $TARGET/leukocyte
cd $TARGET
./leukocyte ../../data/leukocyte/testfile.avi 5 > out_leukocyte.txt
echo ""
cd ..

now=$(date +"%T")
echo "$now Running lud"
cp configs/$TARGET/5000.config $TARGET/gpgpusim.config
cp lud $TARGET/lud
cd $TARGET
./lud -s 256 -v > out_lud.txt
echo ""
cd ..

now=$(date +"%T")
echo "$now Running myocyte"
cp configs/$TARGET/500.config $TARGET/gpgpusim.config
cp myocyte $TARGET/myocyte
cd $TARGET
./myocyte 100 1 0 > out_myocyte.txt
echo ""
cd ..

now=$(date +"%T")
echo "$now Running nw"
cp configs/$TARGET/5000.config $TARGET/gpgpusim.config
cp nw $TARGET/nw
cd $TARGET
./nw 2048 10 > out_nw.txt
echo ""
cd ..

now=$(date +"%T")
echo "$now Running particlefilter"
cp configs/$TARGET/5000.config $TARGET/gpgpusim.config
cp particlefilter_float $TARGET/particlefilter_float
cd $TARGET
./particlefilter_float -x 128 -y 128 -z 10 -np 1000 > out_particlefilter_float.txt
echo ""
cd ..

now=$(date +"%T")
echo "$now Running pathfinder"
cp configs/$TARGET/5000.config $TARGET/gpgpusim.config
cp pathfinder $TARGET/pathfinder
cd $TARGET
./pathfinder 100000 100 20 > out_pathfinder.txt
echo""
cd ..

now=$(date +"%T")
echo "$now Running srad v1"
cp configs/$TARGET/50.config $TARGET/gpgpusim.config
cp srad $TARGET/srad
cd $TARGET
./srad 100 0.5 502 458 > out_srad.txt
echo ""
cd ..

now=$(date +"%T")
echo "$now Running streamcluster"
cp configs/$TARGET/50.config $TARGET/gpgpusim.config
cp streamcluster $TARGET/streamcluster
cd $TARGET
./streamcluster 10 20 256 65536 65536 1000 none output_sc.txt 1 > out_streamcluster.txt
echo ""
cd ..

now=$(date +"%T")
echo "$now Finished Simulations!"
