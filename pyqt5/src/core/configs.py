import json

with open('.env.json') as io_wrapper:
  envs = json.load(io_wrapper)