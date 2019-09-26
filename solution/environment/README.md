# Running

1. [Local](#running-in-local)
2. [Development: Virtual Environment](#running-in-virtual-environment)

## Running in Local

- Install Python Dependencies, Test python environment and Delete all compiled Python files.

```shell script
sudo make

# Available rules:

# clean               Delete all compiled Python files
# lint                Lint using flake8
# requirements        Install Python Dependencies
# test_environment    Test python environment is setup correctly
```

```shell script
make requirements
make test_environment
make clean
```

- Install the libraries

```shell script
pip3 install -r requirements.txt            # libs necessary in notebooks
```

---

## Running in Virtual Environment

- Create virtual environment

```shell script
bash create_virtual_env.sh
```

- Activate this semi-isolated environment

```shell script
source venv/bin/activate
```

- Install the libraries

```shell script
pip3 install -r requirements.txt            # libs necessary in notebooks
```
