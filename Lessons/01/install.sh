mkdir myScript

mv find_keywords.py myScript/
mv requirements.txt myScript/

cd myScript

python3 -m venv myvenv

source myvenv/bin/activate

pip install -r requirements.txt

python find_keywords.py
