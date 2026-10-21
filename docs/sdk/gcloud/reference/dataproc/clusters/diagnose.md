---
url: https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/diagnose/
title: gcloud dataproc clusters diagnose \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:50:11.069490+00:00
---

# gcloud dataproc clusters diagnose  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/diagnose/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud dataproc clusters diagnose Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud dataproc clusters diagnose - run a detailed diagnostic on a cluster 
SYNOPSIS
    

`gcloud dataproc clusters diagnose` (`CLUSTER` : `--region`=`REGION`) [`--end-time`=`END_TIME`] [`--job-ids`=`JOB_IDS`] [`--start-time`=`START_TIME`] [`--tarball-access`=`TARBALL_ACCESS`] [`--tarball-gcs-dir`=`TARBALL_GCS_DIR`] [`--yarn-application-ids`=`YARN_APPLICATION_IDS`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Run a detailed diagnostic on a cluster. 
EXAMPLES
     To diagnose a cluster, run: 
    
    
    gcloud dataproc clusters diagnose my-cluster --region=us-central1

POSITIONAL ARGUMENTS
    

Cluster resource - The name of the cluster to diagnose. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `cluster` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`CLUSTER`
     ID of the cluster or fully qualified identifier for the cluster. 

To set the `cluster` attribute: 

  * provide the argument `cluster` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     Dataproc region for the cluster. Each Dataproc region constitutes an independent resource namespace constrained to deploying instances into Compute Engine zones inside the region. Overrides the default `dataproc/region` property value for this command invocation. 

To set the `region` attribute: 

  * provide the argument `cluster` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line; 
  * set the property `dataproc/region`. 


FLAGS
    

`--end-time`=`END_TIME`
     Time instant to stop the diagnosis at (in %Y-%m-%dT%H:%M:%S.%fZ format). 
`--job-ids`=`JOB_IDS`
     A list of jobs on which to perform the diagnosis. 
`--start-time`=`START_TIME`
     Time instant to start the diagnosis from (in %Y-%m-%dT%H:%M:%S.%fZ format). 
`--tarball-access`=`TARBALL_ACCESS`
     Target access privileges for diagnostic tarball. `TARBALL_ACCESS` must be one of: `GOOGLE_CLOUD_SUPPORT`, `GOOGLE_DATAPROC_DIAGNOSE`. 
`--tarball-gcs-dir`=`TARBALL_GCS_DIR`
     The output Cloud Storage directory for the diagnostic tarball. If not specified, a task-specific directory in the cluster's staging bucket will be used. 
`--yarn-application-ids`=`YARN_APPLICATION_IDS`
     A list of yarn applications on which to perform the diagnosis. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha dataproc clusters diagnose](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/clusters/diagnose)
    
    
    [gcloud beta dataproc clusters diagnose](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/clusters/diagnose)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
