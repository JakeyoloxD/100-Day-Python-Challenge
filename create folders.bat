@echo off
setlocal enabledelayedexpansion

for /l %%i in (1, 1, 100) do (
    set "day=Day %%i"
    mkdir "!day!"
)