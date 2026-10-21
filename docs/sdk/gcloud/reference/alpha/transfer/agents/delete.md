---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/transfer/agents/delete/
title: gcloud alpha transfer agents delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:50:55.693283+00:00
---

# gcloud alpha transfer agents delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/transfer/agents/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha transfer agents delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha transfer agents delete - delete Transfer Service transfer agents 
SYNOPSIS
    

`gcloud alpha transfer agents delete` [`--container-manager`=`CONTAINER_MANAGER`; default="docker"] [`--ids`=[`IDS`,…] | `--all` | `--uninstall`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Delete Transfer Service agents from your machine. 
EXAMPLES
     If you plan to delete specific agents, you can list which agents are running on your machine by running: 
    
    
    docker (or podman) container list --all --filter ancestor=gcr.io/cloud-ingest/tsop-agent

Then run: 
    
    
    gcloud alpha transfer agents delete --ids=id1,id2,…

FLAGS
    

`--container-manager`=`CONTAINER_MANAGER`; default="docker"
     The container manager to use for running agents. `CONTAINER_MANAGER` must be one of: `docker`, `podman`. 
At most one of these can be specified: 

`--ids`=[`IDS`,…]
     The IDs of the agents you want to delete. Separate multiple agent IDs with commas, with no spaces following the commas. 
`--all`
     Delete all agents running on your machine. 
`--uninstall`
     Fully uninstall the agent container image in addition to deleting the agents. Uninstalling the container image will free up space, but you'll need to reinstall it to run agents on this machine in the future. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud transfer agents delete](https://docs.cloud.google.com/sdk/gcloud/reference/transfer/agents/delete)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
