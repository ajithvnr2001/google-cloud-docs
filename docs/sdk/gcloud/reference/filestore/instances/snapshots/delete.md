---
url: https://docs.cloud.google.com/sdk/gcloud/reference/filestore/instances/snapshots/delete/
title: gcloud filestore instances snapshots delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:36:12.699331+00:00
---

# gcloud filestore instances snapshots delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/filestore/instances/snapshots/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud filestore instances snapshots delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud filestore instances snapshots delete - delete a Filestore snapshot 
SYNOPSIS
    

`gcloud filestore instances snapshots delete` `SNAPSHOT` `--instance`=`INSTANCE` (`--instance-location`=`INSTANCE_LOCATION` | `--instance-region`=`INSTANCE_REGION`) [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Delete a Filestore snapshot. 

This command can fail for the following reasons: 

  * The snapshot or instance specified does not exist. 
  * The active account does not have permission to delete the given snapshot. 


EXAMPLES
     To delete a snapshot named ``my-snapshot`` for the instance ``my-instance`` from ``us-central1``, run: 
    
    
    gcloud filestore instances snapshots delete my-snapshot --instance=my-instance --instance-region=us-central1

POSITIONAL ARGUMENTS
    

`SNAPSHOT`
     Name of the Filestore snapshot to be deleted. 
REQUIRED FLAGS
    

`--instance`=`INSTANCE`
     Name of the Filestore instance the snapshot belongs to. 
Exactly one of these must be specified: 

`--instance-location`=`INSTANCE_LOCATION`
     Location of the Filestore instance. 
`--instance-region`=`INSTANCE_REGION`
     Region of the Filestore instance. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `file/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/filestore/>
NOTES
     This variant is also available: 
    
    
    [gcloud beta filestore instances snapshots delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/filestore/instances/snapshots/delete)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
