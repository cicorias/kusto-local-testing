# Overview

As a developer, I'd like to be able to have a development loop that includes query validation using a known set of input data with my Query that I'm currently working on. This story focuses on "headless" approach that does not use a GUI based interface such as Kusto Explorer - which is Windows Only today or the ADX Browser Based interface. Ideally, this could also be run in a pipeline under an Agent in headless mode as well.

This should require a few environmental dependencies that are reasonable, although I'm aware that Kusto query must be tested against a Cloud Base Kusto cluster. In addition, the creation/destroy of an Azure Data Explorer cluster, even a Dev/Test scale size takes "minutes ~= 5 or more".

Assumptions:
 - cluster exists already and is cloud based
 - using WSL, MacOS, possibly Windows - Windows may be removed depending upon approach
 - Azure CLI may be needed 
 - Dotnet installed to support 
- I want to be able to provide "seed" data for testing known inputs against query and then validate expected outputs.
 - the ability to "add more seed data" is needed based upon feedback from production, other scenarios, etc. that affect the queries under validation/test.

What Might be acceptable:
 - a container-based model that that can run with known frameworks (dotnet) to issue commands against the ADX cluster
 - scripts - that are expecting frameworks that are x-plat compatible along with any installation instructions needed. e.g. Kusto CLI required dotnet and a "Tool" installation step" - Kusto CLI - Azure Data Explorer | Microsoft Docs

 - azure cli does not offer Kusto query mode currently and not known if it will. azure-cli-extensions/report.md at main · Azure/azure-cli-extensions (github.com)




test-kqlt.sh or gradle/junit/Kotlin task? 


## Assumptions


## Setup

### get the cli
```
mkdir -p tools/kusto
curl -o ./tools/Microsoft.Azure.Kusto.Tools.NETCore.zip -L https://www.nuget.org/api/v2/package/Microsoft.Azure.Kusto.Tools.NETCore/5.4.2 
unzip ./tools/Microsoft.Azure.Kusto.Tools.NETCore.zip -d ./tools/kusto
```
