
call conda deactivate
call conda remove -y --name soren_kran --all
call conda create -y --name soren_kran
call conda activate soren_kran

pip install -r requirements.txt