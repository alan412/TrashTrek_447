result=${PWD##*/}
EV3=".ev3"
fn=$result$EV3
rm ../$fn
zip ../$fn -x"README.md" -x"*.ev3" *
cp ../$fn  TrashTrek_447.ev3
