# MIT License
# Copyright (c) 2022 Laicy

import subprocess as process
import argparse as argparse
import os, time, datetime

def parse_pawn_arguments(args):
    for i, arg in enumerate(args):
        first = arg[0]
        modified = '-' + first + arg[1:]
        args[i] = modified

    return args

os_name = os.getenv('OS')
arch = os.environ['PROCESSOR_ARCHITECTURE']
user = os.getlogin()
host = os.getenv('COMPUTERNAME')
curr_timestamp = datetime.datetime.now().strftime('%d.%m.%Y %H:%M.%S')

with open('gamemodes/base.pwn', 'r') as file:
    lines = len(file.readlines())

with open('gamemodes/additionals/build-info.inc', 'w') as file:
    file.write(f'#define _LASTBUILD          "{curr_timestamp}"\n')
    file.write('#define _VER                "v0.0.1"\n')
    file.write(f'#define _AUTHOR             "{user}@{host}"\n')
    file.write(f'#define _SOURCE_LINES       "{lines}"\n')

print(f'* Running on {os_name} ({arch}), logged as {user}@{host}')
print(f'* Today is {curr_timestamp}')
print(f'* Currently source file is {lines} lines long')
print(' ')

parser = argparse.ArgumentParser('pawncc-ext.py')
parser.add_argument('-src', '--source', help='path to source file', required=True)
parser.add_argument('-dd', '--dump_dir', help='name of folder which to dump *.amx file', required=True)
parser.add_argument('-id', '--include_dir', help='path to folder containing includes', required=True)
parser.add_argument('-v', '--verbose', help='whether to enable verbose compilation', action='store_true', default=False)
parser.add_argument('-o', '--options', help='additional options (arguments) for compiler', default=None)

startTime = time.time()

args = parser.parse_args()
pawn_args = parse_pawn_arguments(args.options.split(','))

if args.verbose == True:
    buildProc = process.run(['toolchain/pawncc.exe', args.source, f'-D{args.dump_dir}', f'-i{args.include_dir}', ' '.join(pawn_args)]) 
else:
    buildProc = process.run(['toolchain/pawncc.exe', args.source, f'-D{args.dump_dir}', f'-i{args.include_dir}', ' '.join(pawn_args)], stdout=process.DEVNULL, stderr=process.DEVNULL) 

endTime = time.time()

elapsedTime = endTime - startTime
shortElapsedTime = f'{elapsedTime:.3f}'

print(' ')

if buildProc.returncode == 0: print(f'** Script was successfully compiled. Binary file should be placed in /{args.dump_dir} **')
else: print(f'** Compilation failed. Status code: {buildProc.returncode} ** ')

print(f'** Compiled in ~{shortElapsedTime} seconds. **')

with open('gamemodes/additionals/build.log', 'a') as file:
    file.write(' \n')
    file.write(f'******** BUILD LOG | {curr_timestamp} ********\n')
    file.write(f'** HOST: {os_name}_{arch}\n')
    file.write(f'** USER: {user}@{host}\n')
    file.write(f'** TIME: {shortElapsedTime}s ({elapsedTime}s)\n')
    file.write(f'** ARGS: {pawn_args}\n')
    if buildProc.returncode == 0: file.write('******** BUILD SUCCEEDED ********\n')
    else: file.write('******** BUILD FAILED ********\n')
    file.write(' \n')
