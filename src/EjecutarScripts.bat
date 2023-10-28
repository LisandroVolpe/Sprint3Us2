echo. ##############TEST PATH #############
cd Test
python -m pytest tst_001.py tst_002.py tst_003.py --html=../Results/VolpeLisandro.html --self-contained-html
pause
