#!/bin/bash

URL=$1

if [ -z "$URL" ]; then
    echo "Usage: $0 <url>"
    exit 1
fi

echo "Connection Timing Analysis for: $URL"
echo "===================================="

curl -w "\n\
DNS Lookup:        %{time_namelookup}s\n\
TCP Connect:       %{time_connect}s\n\
TLS Handshake:     %{time_appconnect}s\n\
Server Processing: %{time_starttransfer}s\n\
Total Time:        %{time_total}s\n\
Download Size:     %{size_download} bytes\n\
HTTP Code:         %{http_code}\n" \
-o /dev/null -s "$URL"
