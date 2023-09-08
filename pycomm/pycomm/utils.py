#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 启动、关闭模拟器与同步器

import os
from io import TextIOWrapper
from pathlib import Path
from time import sleep
from typing import List, Optional
import logging
import subprocess
import time
import json
import yaml


__all__ = ["run", "wait","kill"]

def run(
    cmd: str,
    name: str,
    log_dir: Path,
    cwd: Path,
    job: Optional[str] = None,
):
    """
    run `docker DEFAULT_ARGS ADDITIONAL_ARGS image CMD`
    """
    os.makedirs(log_dir, exist_ok=True)
    stdout_path = (log_dir / f"{name}.stdout.log").absolute()
    stderr_path = (log_dir / f"{name}.stderr.log").absolute()
    stdout = open(stdout_path, "w")
    stderr = open(stderr_path, "w")
    args = cmd.split()
    if job is not None:
        args += ["-job", job]
    logging.info("Run: %s", " ".join(args))
    handle = subprocess.Popen(
        args,
        stdout=stdout,
        stderr=stderr,
        cwd=str(cwd),
    )
    return args, handle, stdout, stderr


def wait(
    args: List[str],
    handle: subprocess.Popen,
    stdout: TextIOWrapper,
    stderr: TextIOWrapper,
):
    returncode = handle.wait()
    if returncode != 0:
        logging.critical(
            "%s exited with code %d. Check %s for more details.",
            " ".join(args),
            returncode,
            stderr.name,
        )
    stdout.close()
    stderr.close()
    return returncode == 0


def kill(
    args: List[str],
    handle: subprocess.Popen,
    stdout: TextIOWrapper,
    stderr: TextIOWrapper,
):
    handle.terminate()


def load_visualize(filename):
    with open(filename, 'r') as f:
        visualize = json.load(f)
    return visualize