#!/usr/bin/env bash

set -a; source .env; set +a

dotnet tools/kusto/tools/Kusto.Cli.dll "https://scicoriadevloop.eastus.kusto.windows.net;Fed=true" -script:./s1.txt