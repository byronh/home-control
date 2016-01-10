#!/usr/bin/env bash

~/.virtualenvs/ansible/bin/ansible-playbook -i ./ansible/inventory ./ansible/deploy.yml
