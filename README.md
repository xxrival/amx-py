
<p align="center" width="100%">
    <img width="33%" src="repo-logo.png" alt="python logo, plus sign, pawn logo">
</p>

# amx-py
### Python-wrapped Pawn build script to enhance and simplify some processes.

# Requirements
In order to use this wrapper you would only need:
- (https://www.python.org/)[Python] (i used latest version which currently is 3.11.1)


# How to use?
Pretty simple I might say, just place it into some folder inside root folder of your SA:MP/open.mp server
..and then start your IDE (i am using VSCode, so i am gonna explain this using this exact IDE.)

Go ahead and setup your Tasks (`tasks.json` file.)
My `tasks.json` file looks like this:

```json
{
    // See https://go.microsoft.com/fwlink/?LinkId=733558
    // for the documentation about the tasks.json format
    "version": "2.0.0",
    "tasks": [
        {
            "label": "make-pawn",
            "type": "shell",
            "command": "py",
            "args": [
                "toolchain/pawncc-ext.py",
                "--source", "../gamemodes/base.pwn", 
                "--dump_dir", "gamemodes",
                "--include_dir", "../includes",
                "--usegit",
                "--options", "d3, z+, ;+, (+",
                "--verbose"
            ],
            "isBackground": false,
            "problemMatcher": "$pawncc",
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "presentation": {
                "reveal": "silent",
                "panel": "dedicated",
                "revealProblems": "onProblem",
                "echo": false,
                "showReuseMessage": false,
                "clear": true
            }
        }
    ]
}
```

..and just go ahead and build! :^)

# Worth knowing..
I pre-defined some things for myself.
More specifically, paths.

```py
line 19: open('gamemodes/base.pwn', 'r')
line 22: open('gamemodes/additionals/build-info.inc', 'w')
line 62: open('gamemodes/additionals/build.log', 'a')
```

You might want to change those paths according to your file base.

# What 'processes' this is 'simplifing'?
Script takes care of versioning, kinda.
It grabs system name, system version, system arch, username and hostname, current date according to timestamp,
..and echoing current date, username, hostname specified version in line 24 and total amount of lines in `gamemodes/base.pwn`, (path is pre-defined, you can change it).
It also produces log after building, located in (also) pre-defined path, line 62.
Log contains current date based on timestamp, hostname and username, time elapsed since program started till the end of compilation process and used arguments, also information if build succeded.
Also, it prints some information to currently used terminal/console emulator.
Pretty same as described earlier, system name, system arch, username and hostname, as well as date according to current timestamp, and count of lines.
In addition to all that it provides you with some basic versioning system thru git. Program itself gets last commit ID if you use switch (`-g`) to enable that. Obviously, you need to setup a git repository in order for that to work.

# What are those arguments?
Simple stuff, you can provide some stuff yourself. I will explain this here, but you can also just use `pawncc-ext.py -h`.

- `-src/--source`, file which we want to be compiled.
- `-dd/--dump_dir`, name of folder where to dump *.amx files when compilation succeded.
- `-id/--include_dir`, path to includes.
- `-v/--verbose`, whether to show information about building (like errors, warnings, or debug information).
- `-o/--options`, additional arguments to build like `-d3`.
- `-g/--usegit`, whether to use git interaction with repository (getting last commit ID hash).

Script itself takes care of parsing those additional arguments and passing in correct format, so you just need to provide arguments without "-", like this: `d3, z+, ;+, (+`. 

# Soo, why is it created, once more..
I just thought I might need something like that, so I decided to create something like this and by the way share it with all of you. Some might think that's useful, some might think opposite.