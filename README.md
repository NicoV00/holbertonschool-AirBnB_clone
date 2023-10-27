# AirBnB Clone Project

## Description

The AirBnB Clone Project is a Python application that simulates some of the basic functionalities of the Airbnb platform. It includes a command-line interface for managing and interacting with different data models such as users, states, cities, places, reviews, and amenities.

## Command Interpreter

### How to Start It

To start the command interpreter, simply run `console.py`:

```
$ ./console.py
```

### How to Use It

Once the command interpreter is running, you can use the following commands:

- `create`: Create a new instance of a class and save it to a JSON file.
- `show`: Show the string representation of an instance.
- `destroy`: Delete an instance based on the class name and ID.
- `all`: Print string representations of all instances or of a specific class.
- `update`: Update an instance based on the class name and ID.

To see detailed usage for each command, you can run `help <command>` within the interpreter.

### Examples

- To create a new State instance:

```
(hbnb) create State
```

- To show details of a specific instance:

```
(hbnb) show State 12345
```

- To destroy an instance:

```
(hbnb) destroy State 12345
```

- To see all instances of a specific class:

```
(hbnb) all State
```

- To update an instance:

```
(hbnb) update State 12345 name "New York"
```

## Authors

This project was contributed to by the following individuals:
- Santiago Fleitas <6769@holbertonstudents.com>
- Nicolás Valles <@holbertonstudents.com>
