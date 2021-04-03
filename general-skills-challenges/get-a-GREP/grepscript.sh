#!/bin/bash
#nactf{gr3p_1s_c00l}
#this isn't the flag
c=0
create_folder() {
   if [ $1 -gt 0 ]
   then
      local a=$(($1 - 1))
      for i in {0..9}
      do
         foldername="branch$i"
         mkdir $foldername
         cd $foldername
         create_folder $a
         cd ..
      done
   else
      for i in {0..9}
      do
         filename="leaf$c.txt"
         if [ $c -eq 8351 ]
         then
            echo "nactf{v1kram_and_h1s_10000_l3av3s}" > $filename
         else 
            echo "No flag here... check another leaf" > $filename
         fi
         let "c+=1"
      done
   fi
}
rm -rf bigtree
mkdir bigtree
cd bigtree
create_folder 3
