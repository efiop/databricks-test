# Databricks notebook source
import subprocess

print(subprocess.check_output("pwd && ls -la ../../../../", shell=True).decode())
