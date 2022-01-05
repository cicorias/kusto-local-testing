#!/usr/bin/env bash
#dotnet ./tmp/tools/Kusto.Cli.dll "https://???.eastus.kusto.windows.net;Fed=true"

# odd that no switch -- is prefixed on "location" or soft-delete-period
# https://github.com/Azure/azure-cli-extensions/blob/main/src/kusto/report.md#command-az-kusto-database-create

set -a; source .env; set +a

rv=$(az kusto database create \
    --cluster-name "$CLUSTER_NAME" \
    --database-name "$DB_NAME" \
    --read-write-database \
    location="$LOCATION" \
    soft-delete-period="P1D" \
    --resource-group "$RG")


echo "rv=$rv"
