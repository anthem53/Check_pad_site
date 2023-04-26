echo "> Git Pull"

git pull

echo "> Program Start"

rm nohup.out

nohup python -u main.py &

echo "> Program quit "
