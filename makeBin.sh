result=${PWD##*/}
EV3=".ev3"
fn=$result$EV3
zip ../$fn -x"README.md" *
