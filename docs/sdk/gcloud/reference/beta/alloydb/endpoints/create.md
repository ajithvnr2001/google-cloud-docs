---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/alloydb/endpoints/create/
title: gcloud beta alloydb endpoints create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:21:36.105685+00:00
---

# gcloud beta alloydb endpoints create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/alloydb/endpoints/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta alloydb endpoints create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta alloydb endpoints create - creates a new AlloyDB endpoint 
SYNOPSIS
    

`gcloud beta alloydb endpoints create` `ENDPOINT` `--endpoint-type`=`ENDPOINT_TYPE` `--region`=`REGION` `--target-instances`=[`TARGET_INSTANCES`,…] [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Creates a new AlloyDB endpoint. 
EXAMPLES
     To create a new write endpoint for an instance, run: 
    
    
    gcloud beta alloydb endpoints create my-endpoint --region=us-central1 --endpoint-type=WRITE_ENDPOINT --target-instances=projects/my-project/locations/us-central1/clusters/my-cluster/instances/my-instance

POSITIONAL ARGUMENTS
    

`ENDPOINT`
     AlloyDB endpoint ID 
REQUIRED FLAGS
    

`--endpoint-type`=`ENDPOINT_TYPE`
     Specifies endpoint type. `ENDPOINT_TYPE` must be (only one value is supported): 

`WRITE_ENDPOINT`
     Provide a consistent connection point that always directs traffic to the instance. The write endpoint can serve both read and write traffic. 
`--region`=`REGION`
     Regional location (e.g. `asia-east1`, `us-east1`). See the full list of regions at <https://cloud.google.com/sql/docs/instance-locations>. 
`--target-instances`=[`TARGET_INSTANCES`,…]
     Comma-separated list of target instances that the endpoint will direct traffic to.For example, `--target-instances=projects/my-project/locations/us-central1/clusters/my-cluster/instances/my-instance`.For WRITE endpoint, only one target instance is allowed. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud alpha alloydb endpoints create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/alloydb/endpoints/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-30 UTC."],[],[]] 
