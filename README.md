# spellingbee

python project used to fix spelling errors by translating the input into english and back using deepl API. This is a totally useless project and was only created for fun.  

## Prerequisites 

The code has been written in `python 3.8`, but might work with lower versions. The `deepl` package is needed: it can be installed from PyPI using pip: 
```sh
pip install --upgrade deepl
```

A deepl account is required in order to obtain an API key. The project assumes the key to be stored in `DEEPL_AUTH_KEY` environment variable. 