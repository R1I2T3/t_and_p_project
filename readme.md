# Category automation

## Tech stack
- Flask
- jinja template
- tailwind css

## For initialization of project

First clone repository.Then create a virtual environment with the help of venv package. with command: 

``` bash
py -m venv .venv
```
For activating venv:

``` bash
.venv/Scripts/activate/
```
then install python dependency:


``` bash
pip install -r requirements.txt
```

then install tailwind install packages with the help of:


``` bash
npm i
```

For running tailwind server run command:


``` bash
npx tailwindcss -i ./static/css/style.css -o ./static/css/output.css --watch
```