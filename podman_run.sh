#!/bin/bash

podman run -d --name flask_app -p 5000:5000 my_flask_app
