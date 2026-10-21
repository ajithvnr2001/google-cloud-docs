---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/inject-fault/
title: gcloud alpha alloydb instances inject-fault \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:03:50.262117+00:00
---

# gcloud alpha alloydb instances inject-fault  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/inject-fault/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha alloydb instances inject-fault Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha alloydb instances inject-fault - inject fault on an AlloyDB instance within a given cluster 
SYNOPSIS
    

`gcloud alpha alloydb instances inject-fault` `INSTANCE` `--cluster`=`CLUSTER` `--fault-type`=`FAULT_TYPE` `--region`=`REGION` [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Inject fault on an AlloyDB instance within a given cluster. 
EXAMPLES
     To Inject fault on an instance, run: 
    
    
    gcloud alpha alloydb instances inject-fault my-instance --cluster=my-cluster --region=us-central1 --fault-type=stop-vm

POSITIONAL ARGUMENTS
    

`INSTANCE`
     AlloyDB instance ID 
REQUIRED FLAGS
    

`--cluster`=`CLUSTER`
     AlloyDB cluster ID 
`--fault-type`=`FAULT_TYPE`
     Specifies fault type. `FAULT_TYPE` must be (only one value is supported): 

`stop-vm`
     stop-vm fault type supports stopping the VM. 
`--region`=`REGION`
     Regional location (e.g. `asia-east1`, `us-east1`). See the full list of regions at <https://cloud.google.com/sql/docs/instance-locations>. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud alloydb instances inject-fault](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/inject-fault)
    
    
    [gcloud beta alloydb instances inject-fault](https://docs.cloud.google.com/sdk/gcloud/reference/beta/alloydb/instances/inject-fault)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
