
#Test Usage
##Linting
To lint the project, navigate to the plugin folder in your terminal and install the dependencies using 
```bash
  pip3 install -r requirements.txt
```
then run
```bash
  cd ..
  pylint -d C0301 plugin/*/*.py --rcfile  plugin/.pylintrc
```
##Testing with Docker
Ensure you are in the plugin directory to build with the dockerfile. 
```bash
    docker build . -t examplename
    docker run -it examplename python3 -m pytest -vs               
```