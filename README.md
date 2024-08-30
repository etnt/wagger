# RESTCONF/Swagger API Client

This project provides a Python client for interacting with a RESTCONF API.
It allows the Client to perform CRUD operations on records containing name,
surname, age, and shoe size information.

What is interesting about this project is that the API is defined by a Swagger
JSON file which is then used to generate the API client by the help of the
Cursor AI.

The time to create this client took around 30 minutes, and note that it
was the first time I used the Cursor AI.

## Features

- Create, read, update, and delete records
- Get and set individual fields (age, shoe size)
- Simple interface for API interactions

## Requirements

- Python 3.6+
- requests library

## Installation

1. Clone this repository:
   ```shell
   git clone https://github.com/etnt/wagger.git
   cd key-api-client
   ```

2. Set up a virtual environment and install dependencies:
   ```shell
   make
   ```

## Usage

It assumes that the RESTCONF service is running on `http://127.0.0.1:9080/`.

```shell
make run
```

