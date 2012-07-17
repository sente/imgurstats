#!/bin/bash

grep size_down output/* |awk -F'\t' '{if ($2==503){bad++;}else if ($2==0){bad2++}else{good++}}END{print NR,good,bad,bad2, 100*(good/NR),bad/NR,bad2/NR}'
