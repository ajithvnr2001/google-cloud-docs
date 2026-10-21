---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/monitoring/metrics-scopes/delete/
title: gcloud alpha monitoring metrics-scopes delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:49:13.377487+00:00
---

# gcloud alpha monitoring metrics-scopes delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/monitoring/metrics-scopes/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha monitoring metrics-scopes delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha monitoring metrics-scopes delete - delete a monitored project in a metrics scope 
SYNOPSIS
    

`gcloud alpha monitoring metrics-scopes delete` `MONITORED_RESOURCE_CONTAINER_NAME` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` This command can fail for the following reasons: 

  * The projects specified do not exist. 
  * The active account does not have permission to access one of the given project. 



More details can be found at <https://cloud.google.com/monitoring/api/ref_v3/rest/v1/locations.global.metricsScopes.projects/delete>

EXAMPLES
     The following command adds a monitored project with the ID `monitored-project-1` to a metrics scope with project id `metrics-scope-1` assuming the `metrics-scope-1` is the default project: 
    
    
    gcloud alpha monitoring metrics-scopes delete projects/monitored-project-1

The following command adds a monitored project with the ID `monitored-project-1` to a metrics scope with project id `metrics-scope-1`: 
    
    
    gcloud alpha monitoring metrics-scopes delete projects/monitored-project-1 --project=metrics-scope-1
    gcloud alpha monitoring metrics-scopes delete locations/global/metricsScopes/metrics-scope-1/projects/monitored-project-1

POSITIONAL ARGUMENTS
    

`MONITORED_RESOURCE_CONTAINER_NAME`
     Monitored resource container (example - projects/PROJECT_ID) project you want to delete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud beta monitoring metrics-scopes delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/monitoring/metrics-scopes/delete)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
