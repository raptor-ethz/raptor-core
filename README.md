# RAPTOR: raptor-core

This repository contains all the necessary code to fly a mission from the reference generator and will execute it at one, launching the position control interface and MoCap publisher at the same time. 

## Usage

Clone the repository using 

```bash
git clone --recursive https://github.com/raptor-ethz/raptor-core
```

and then build the project. This will create the necessary executables to run all applications.

Then, 

```bash
cd raptor-core
python3 launcher.py
```
will launch all applications. To edit the configuration, go into `launcher.py` and change the parameters you want to customize. 