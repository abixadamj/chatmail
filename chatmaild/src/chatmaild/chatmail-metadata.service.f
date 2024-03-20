[Unit]
Description=Chatmail dict proxy for IMAP METADATA

[Service]
ExecStart={execpath} /run/dovecot/metadata.socket vmail {config_path} /home/vmail/metadata
Restart=always
RestartSec=30

[Install]
WantedBy=multi-user.target
