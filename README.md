# pytest_selenium
The pytest and selenium E2E test framework



## Usage
### Build your environment
**1. Install chrome with version 81 or 83**

1. For mac: Please refer to the [chrome install url](https://google-chrome.en.uptodown.com/mac/download/2245134)

**2. Install python3 or use python venv to your machine**
```sh
python3 -m venv pytest
source pytest/bin/activate
```

**3. Install requirement python3 library**

```sh
cd pytest_selenium
pip install -r requirements.txt
```

**3. Run the pytest framework test case.**

```
cd pytest_selenium
python3 -m pytest
```
For more command example:
* Run test with test report file E.g.
```
python3 -m pytest --html=test.html
```

* Run test with stdout log. E.g.
```
python3 -m pytest -s
```

#### Reference
* Python Virtual Environment: [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/index.html#)
* Chrome Install: [chrome install for mac](https://google-chrome.en.uptodown.com/mac)