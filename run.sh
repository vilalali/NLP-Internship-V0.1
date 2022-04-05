input_dir=$1
ouput_dir=$2

for f in $input_dir*.ssf
do
	filename=`basename $f`
	python3 karakas-vibhakti_extractor.py $f > "$2/$filename.ssf"
done
cd $2
cat *.ssf> ../out.ssf
#for i in *.txt; do (cat $i; echo 'Sentence:') >> all.txt; done
echo "Program executed succesfully"
echo "Output file created and save in the directory 'NLP-Internship-V0.1' with the name of 'out.ssf'"

