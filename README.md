# buzzline-01-monsuru

This project introduces streaming data. The Python language includes generators—this feature will be used to generate streaming buzzline messages. As the code runs, it will continuously update a log file. A consumer will modify this log file and alert us when a special message is detected.

## Task 1. Set Up Your Machine

Before proceeding, make sure your machine is properly set up. Detailed instructions by operating system are provided.

1. Install **Git**.
2. Install **Python Version 3.11**.
3. Install **VS Code**.
4. Configure Git with `user.name` and `user.email`.
5. Enable **VS Code File Autosave**.
6. Install necessary **VS Code Extensions** (see instructions below).

For more detailed setup instructions:

- [SETUP-MAC-LINUX.md](docs/SETUP-MAC-LINUX.md)
- [SETUP-WINDOWS.md](docs/SETUP-WINDOWS.md)

## Python Versions (3.11 for this course)

This project requires Python **3.11**, though the latest version is 3.13. We will be using tools like Kafka that still require Python 3.11. It’s recommended to install both versions for practice, but Python 3.11 is sufficient for this course. For more details, refer to [PYTHON-VERSIONS.md](docs/PYTHON-VERSIONS.md).

## Task 2. Copy This Example Project & Change `case` to `yourname` (customized)

Once the required tools are installed, fork or copy this project into your GitHub account. Create your version of the project by renaming it **buzzline-01-yourname**, where `yourname` is your unique identifier. Follow the instructions in [FORK-THIS-REPO.md](docs/FORK-THIS-REPO.md) for the complete process.

## Task 3. Manage Local Project Virtual Environment

Python needs a virtual environment to manage dependencies for the project. This environment will be created in a `.venv` folder. 

Once the `.venv` folder is created, you need to activate it and install dependencies from `requirements.txt`. 

Important: You must activate `.venv` each time you open a new terminal. Follow the steps below to set up and manage your virtual environment:

1. Create your `.venv`
2. Activate `.venv`
3. Install dependencies from `requirements.txt`

Instructions for these steps are detailed in [MANAGE-VENV.md](docs/MANAGE-VENV.md).

## Task 4. Generate Streaming Data (Terminal 1)

This task will generate some streaming data, and you’ve already completed most of the setup! To begin, open a terminal in VS Code, activate your `.venv`, and run the generator module.

### Windows PowerShell:
```shell
.venv\Scripts\activate
py -m producers.basic_producer_monsuru

```

Mac/Linux:
```zsh
source .venv/bin/activate
python3 -m producers.basic_producer_monsuru
```

## Task 5. Monitor an Active Log File (Terminal 2)

A common streaming task is monitoring a log file as it is being written. 
This project has a consumer that reads and processes our own log file as log messages arrive. 

In VS Code, open a NEW terminal in your root project folder. 
Use the commands below to activate .venv, and run the file as a module. 

Windows:
```shell
.venv\Scripts\activate
py -m consumers.basic_consumer_prince.py
```

Mac/Linux:
```zsh
source .venv/bin/activate
python3 -m consumers.basic_consumer_prince.py
```

## Save Space
To save disk space, you can delete the .venv folder when not actively working on this project.
We can always recreate it, activate it, and reinstall the necessary packages later. 
Managing Python virtual environments is a necessary and valuable skill. 
We will get a good amount of practice. 

## License
This project is licensed under the MIT License as an example project. 
You are encouraged to fork, copy, explore, and modify the code as you like. 
See the [LICENSE](LICENSE.txt) file for more.
