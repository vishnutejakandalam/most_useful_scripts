status=1
output=$(pacmd list | grep 'active profile' | grep -c "analog-stereo")
ou=$(pacmd list | grep "active profile")
echo $output 
echo $ou
if [ $output -eq 1 ]
then             
  sleep 2
  pacmd set-card-profile 0 output:hdmi-stereo
else
  sleep 2
  pacmd set-card-profile 0 output:analog-stereo+input:analog-stereo
fi
