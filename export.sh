export file_dir=$(echo "pages/_tutorials/tutorial"$1 )
export tut_no=$(echo $file_dir | grep -oE "[[:digit:]]{1,}")
export subtitle=$(cat $file_dir/tutorial$tut_no.html | ./pup 'body' | ./pup 'h2[id=1]' | tail -n 2 | head -n 1)
export out_file=$(echo $file_dir/tutorial$tut_no.md)

echo --- > $out_file
echo layout: tutorial >> $out_file
echo title: Tutorial $tut_no >> $out_file
echo subtitle: $subtitle >> $out_file
echo --- >> $out_file

cat $file_dir/tutorial$tut_no.html | ./pup 'body' | sed 's/src=\"tut/src=\"\/tut/' | recode -f html..ascii >> $out_file

head -n 15 $out_file
