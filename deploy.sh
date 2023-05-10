echo "> Setting conda environment"

conda init bash
source activate notice

echo "> Program Start"

rm nohup.out
nohup python -u main.py &

echo "> Program quit
