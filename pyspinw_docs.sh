# Warn about dangers

echo "Warning: If it is possible that this script could delete things you don't want it to. Make sure things are backed up."
echo
read -p "Are you sure? (Y/[N])" -n 1 -r
echo    

# Check confirmation
if [[ $REPLY =~ ^[Yy]$ ]]
then
    # Clean directory    
    mkdir -p docsbuild
    cd docsbuild
    #rm -rf *

    # Get git repo
    #git clone https://github.com/SpinW/pySpinW/

    cd pySpinW
    export PYTHONPATH="./pyspinw/:$PYTHONPATH"

    # Set up venv
    echo "Setting up VENV"
    #python3 -m venv .venv
    source .venv/bin/activate

    # Get required packages
    echo "Getting pdoc"
    #python -m pip install pdoc

    echo "Getting dependencies"
    #python -m pip install -r requirements.txt
    
    # Get ready to build
    echo "Building"
    python -m pdoc pyspinw --no-show-source -o ../docs

    cp ../docs/pyspinw.html ../../pythonapi.html

    echo "Done!"

fi
