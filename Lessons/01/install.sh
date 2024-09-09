mkdir $HOME/myScript

cp find_keyword.py $HOME/myScript/
cp requirements.txt $HOME/myScript/

python3 -m venv $HOME/myScript/myvenv

source $HOME/myScript/myvenv/bin/activate

pip install -r requirements.txt
