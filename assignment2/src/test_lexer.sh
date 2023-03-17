python run.py gen
echo "Run self-test"
python run.py test LexerSuite

echo "Run Nam test"
python run.py test LexerSuiteNam

echo "Run Dat test"
python run.py test LexerSuiteD

python run.py test LexerSuiteNhan

python run.py test LexerSuiteTai
