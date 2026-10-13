---
url: https://docs.cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/diagnose/
title: gcloud notebooks runtimes diagnose \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:15:18.271314+00:00
---

# gcloud notebooks runtimes diagnose  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/diagnose/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud notebooks runtimes diagnose Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud notebooks runtimes diagnose - request for diagnose runtimes 
SYNOPSIS
    

`gcloud notebooks runtimes diagnose` (`RUNTIME` : `--location`=`LOCATION`) `--gcs-bucket`=`GCS_BUCKET` [`--async`] [`--enable-copy-home-files`] [`--enable-packet-capture`] [`--enable-repair`] [`--relative-path`=`RELATIVE_PATH`] [`--timeout-minutes`=`TIMEOUT_MINUTES`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Request for diagnose notebook runtimes. 
EXAMPLES
     To diagnose an runtime, run: 
    
    
    gcloud notebooks runtimes diagnose example-runtime --location=us-central1 --gcs-bucket=gs://example-bucket

To diagnose an runtime with a relative path: 
    
    
    gcloud notebooks runtimes diagnose example-runtime --location=us-central1 --gcs-bucket=gs://example-bucket --relative-path=logs

To diagnose an runtime, with packet capture: 
    
    
    gcloud notebooks runtimes diagnose example-runtime --location=us-central1 --gcs-bucket=gs://example-bucket --enable-packet-capture

POSITIONAL ARGUMENTS
    

Runtime resource - User-defined unique name of this runtime. The runtime name must be 1 to 63 characters long and contain only lowercase letters, numeric characters, and dashes. The first character must be a lowercase letter and the last character cannot be a dash. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `runtime` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`RUNTIME`
     ID of the runtime or fully qualified identifier for the runtime. 

To set the `runtime` attribute: 

  * provide the argument `runtime` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Google Cloud location of this runtime <https://cloud.google.com/compute/docs/regions-zones/#locations>. 

To set the `location` attribute: 

  * provide the argument `runtime` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `notebooks/location`. 


REQUIRED FLAGS
    

`--gcs-bucket`=`GCS_BUCKET`
     The Cloud Storage bucket where the log files generated from the diagnose command will be stored. storage.buckets.writer permissions must be given to project's service account or user credential. Format: gs://`{gcs_bucket}`
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--enable-copy-home-files`
     Enables flag to copy all `/home/jupyter` folder contents 
`--enable-packet-capture`
     Enables flag to capture packets from the runtime for 30 seconds 
`--enable-repair`
     Enables flag to repair service for runtime 
`--relative-path`=`RELATIVE_PATH`
     Defines the relative storage path in the Cloud Storage bucket where the diagnostic logs will be written. Default path will be the root directory of the Cloud Storage bucketFormat of full path: gs://`{gcs_bucket}`/`{relative_path}`/ 
`--timeout-minutes`=`TIMEOUT_MINUTES`
     Maximum amount of time in minutes before the operation times out 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
