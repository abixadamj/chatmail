#!/usr/bin/env bash
export CHATMAIL_DOMAIN="${1:-c1.testrun.org}"
venv/bin/pyinfra --ssh-user root "$CHATMAIL_DOMAIN" deploy.py
