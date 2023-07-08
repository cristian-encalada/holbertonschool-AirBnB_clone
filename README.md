# AirBnB clone - The console

<img align="center" alt="AirBnb_clone_logo" src="https://github.com/cristian-encalada/holbertonschool-AirBnB_clone/blob/assets/AirBnB_clone.png?raw=true" />

## Table of contents

1. [AirBnB clone Overview](#airbnb-clone-overview)

2. [Requirements](#requirements)

3. [AirBnB clone - The Console](#airbnb-clone---the-console)
   * [The console - File structure](#the-console---file-structure)
   * [The console - Usage](#the-console---usage)
   * [The console - Unit tests](#the-console---unit-tests)
4. [Authors](#Authors)

## AirBnB clone Overview

 The goal of the project is to build a simple copy of the [AirBnB website](https://www.airbnb.com/)

 Here is a preview of the final product.

 <img align="center" alt="AirBnb_final_product" src="https://github.com/cristian-encalada/holbertonschool-AirBnB_clone/blob/assets/AirBnB_final_product.png?raw=true" />

At the end of the project the complete web application will be composed by:

- __A command interpreter__ to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
- __A website (the front-end)__ that shows the final product to everybody: static and dynamic
- __A database or files__ that store data (data = objects)
- __An API__ that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`, `vscode`
- All the files will be interpreted/compiled on `Ubuntu 20.04 LTS` using python3 (version `3.8.5`)
- All the files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- The code should use the `pycodestyle` (version `2.7.*`)
- All the files must be executable
- The length of the files will be tested using `wc`
- All the modules, classes and functions should have a documentation 

## AirBnB clone - The Console

The first piece is to manipulate a powerful __storage system__. 

This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from the console code (the command interpreter itself) and from the front-end and RestAPI.

This abstraction will also allow us to change the type of storage easily without updating all of the codebase.

The __console will be a tool to validate this storage engine__.

The following is a diagram of this first stage:

 <img align="center" alt="AirBnb_console_diagram" src="https://github.com/cristian-encalada/holbertonschool-AirBnB_clone/blob/assets/AirBnB_console.png?raw=true" />

<br>

### The console - File structure

For the implementation, the following file structure was defind:

```
.
├── AUTHORS
├── console.py
├── models
│   ├── amenity.py
│   ├── base_model.py
│   ├── city.py
│   ├── engine
│   │   ├── file_storage.py
│   │   └── __init__.py
│   ├── __init__.py
│   ├── place.py
│   ├── review.py
│   ├── state.py
│   └── user.py
├── README.md
└── tests
    ├── __init__.py
    └── test_models
        ├── __init__.py
        ├── test_base_model.py
        └── test_engine

6 directories, 16 files
```

__Directories__

|Directory|Description|
|--|--|
|[models](./models/)|Contains all classes used for the entire project|
|[tests](./tests/)|Contains all unit tests|
|[models/engine](./models/engine/)|Contains all storage classes (using the same prototype)|

__Files__

|File|Description|
|--|--|
|[console.py](./console.py)|Is the entry point of our command interpreter|
|[models/base_model.py](./models/base_model.py)|Is the base class of all other models|
|[models/engine/file_storage.py](./models/engine/file_storage.py)|Is the first storage class implemented|


### The console - Usage

The console works in two modes:

__Interactive mode__

```sh
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

__Non-Interactive mode__

```sh
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

### The console - Unit tests

All unit tests pass in both modes:

__Interactive mode__

```sh
guillaume@ubuntu:~/AirBnB$ python3 -m unittest discover tests
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s

OK
guillaume@ubuntu:~/AirBnB$
```

__Non-Interactive mode__

```sh
guillaume@ubuntu:~/AirBnB$ echo "python3 -m unittest discover tests" | bash
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s

OK
guillaume@ubuntu:~/AirBnB$
```

## Authors

* __Cristian Encalada__ - *Holberton Student*
   - Github: [Cristian Encalada](https://github.com/cristian-encalada)
* __Aldo Sánchez__ - *Holberton Student*
   - Github: [Aldo Sánchez](https://github.com/Aldo2303)