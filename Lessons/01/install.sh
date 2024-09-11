mkdir $HOME/myScript

cp find_keyword.py $HOME/myScript/
cp requirements.txt $HOME/myScript/

cd $HOME/myScript/

python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt
