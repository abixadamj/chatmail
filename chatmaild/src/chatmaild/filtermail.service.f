[Unit]
Description=Chatmail Postfix BeforeQeue filter 

[Service]
ExecStart={execpath} 10080
Restart=always
RestartSec=30

[Install]
WantedBy=multi-user.target
