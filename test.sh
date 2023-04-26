echo "> Git Pull"

git pull


echo "> Setting conda environment"

conda init bash
conda activate notice


echo "> Program Start"

rm nohup.out
nohup python -u /workspace/python_server/github/Check_pad_site/test7.py &

