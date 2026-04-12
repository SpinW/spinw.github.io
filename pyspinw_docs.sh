if [[ $# -eq 1 && "$1" == "rebuild" ]]; then
  echo "Rebuild flag is set"
  REBUILD=true
else
  REBUILD=false
fi

# Warn about dangers

echo "Warning: If it is possible that this script could delete things you don't want it to. Make sure things are backed up."
echo "Note: use '$0 rebuild' to clean directories first... more unsafe"
echo
read -p "Are you sure? (Y/[N])" -n 1 -r
echo    

# Check confirmation
if [[ $REPLY =~ ^[Yy]$ ]]
then
    mkdir -p docsbuild
    cd docsbuild
    
    if [[ "$REBUILD" == "true" ]]; then
    
        # Clean directory    
        rm -rf *

        # Get git repo
        git clone https://github.com/SpinW/pySpinW/
    fi

    cd pySpinW
    

    if [[ "$REBUILD" == "true" ]]; then
        export PYTHONPATH="./pyspinw/:$PYTHONPATH"

        # Set up venv
        echo "Setting up VENV"
        python3 -m venv .venv
        source .venv/bin/activate

        # Get required packages
        echo "Getting pdoc"
        python -m pip install pdoc

        echo "Getting dependencies"
        python -m pip install -r requirements.txt

    fi


    # Get ready to build
    echo "Building"
    python -m pdoc pyspinw --no-show-source --favicon /img/spinw3_logo_square.png --logo /img/pyspinw_logo.png -o ../docs

    cp ../docs/pyspinw.html ../../pythonapi.html

    echo "Done!"

fi
