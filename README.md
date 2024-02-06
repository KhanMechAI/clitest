# Project Name: Docker+Poetry CLI Pass Through Test

## Description

This project demonstrates how to create a command-line tool using Poetry, package it as a Python package, and seamlessly integrate it with Docker for easy distribution and deployment.

## How to Use

### Prerequisites

- Python 3.9 or higher installed on your system
- Docker installed on your system

### Installation

1. Clone this repository to your local machine:

    ```bash
    git clone git@github.com:KhanMechAI/clitest.git
    ```

2. Navigate into the project directory:

    ```bash
    cd clitest
    ```

3. Install Poetry (if not already installed):

    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```

4. Install the project dependencies using Poetry:

    ```bash
    poetry install
    ```

### Usage

1. Build the Docker image:

    ```bash
    docker build -t myimage .
    ```

2. Run the Docker container:

    ```bash
    docker run myimage -h
    usage: mytest [-h] [--optional_arg1 OPTIONAL_ARG1]
    2024-02-06T09:25:48.084322543Z               [--optional_arg2 OPTIONAL_ARG2]
    2024-02-06T09:25:48.084326210Z               positional_arg
    2024-02-06T09:25:48.084328293Z mytest: error: the following arguments are required: positional_arg
    ```

