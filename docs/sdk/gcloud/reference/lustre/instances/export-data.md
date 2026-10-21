---
url: https://docs.cloud.google.com/sdk/gcloud/reference/lustre/instances/export-data/
title: gcloud lustre instances export-data \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:36:35.751699+00:00
---

# gcloud lustre instances export-data  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/lustre/instances/export-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud lustre instances export-data Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud lustre instances export-data - exports data from a Managed Lustre instance to Cloud Storage 
SYNOPSIS
    

`gcloud lustre instances export-data` (`INSTANCE` : `--location`=`LOCATION`) `--gcs-path-uri`=`GCS_PATH_URI` [`--async`] [`--lustre-path`=`LUSTRE_PATH`] [`--request-id`=`REQUEST_ID`] [`--service-account`=`SERVICE_ACCOUNT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Exports data from a Managed Lustre instance to Cloud Storage. 
EXAMPLES
     To export data from instance `my-instance` in location `us-central1-a` to Cloud Storage bucket `gs://my-bucket/`, run: 
    
    
    gcloud lustre instances export-data my-instance --location=us-central1-a --gcs-path-uri=gs://my-bucket/ --lustre-path='/path/to/lustre/dir'

POSITIONAL ARGUMENTS
    

Instance resource - The name of the Managed Lustre instance in the format `projects/{project}/locations/{location}/instances/{instance}`. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `instance` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`INSTANCE`
     ID of the instance or fully qualified identifier for the instance. 

To set the `instance` attribute: 

  * provide the argument `instance` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location id of the instance resource. 

To set the `location` attribute: 

  * provide the argument `instance` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

`--gcs-path-uri`=`GCS_PATH_URI`
     The URI to a Cloud Storage bucket, or a path within a bucket, using the format `gs://<bucket_name>/<optional_path_inside_bucket>/`. If a path inside the bucket is specified, it must end with a forward slash (`/`). 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--lustre-path`=`LUSTRE_PATH`
     The root directory path to the Managed Lustre file system. Must start with `/`. Default is `/`. If you're importing data into Managed Lustre, any path other than the default must already exist on the file system. 
`--request-id`=`REQUEST_ID`
     UUID to identify requests. 
ServiceAccount resource - User-specified service account used to perform the transfer. If unspecified, the Managed Lustre service agent is used. 

Use one of the following formats: 

  * `{EMAIL_ADDRESS_OR_UNIQUE_ID}`
  * `projects/{PROJECT_ID}/serviceAccounts/{EMAIL_ADDRESS_OR_UNIQUE_ID}`
  * `projects/-/serviceAccounts/{EMAIL_ADDRESS_OR_UNIQUE_ID}` This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 



To set the `project` attribute: 

  * provide the argument `--service-account` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


`--service-account`=`SERVICE_ACCOUNT`
     ID of the serviceAccount or fully qualified identifier for the serviceAccount. 

To set the `service-account` attribute: 

  * provide the argument `--service-account` on the command line. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `lustre/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/managed-lustre/docs>
NOTES
     This variant is also available: 
    
    
    [gcloud alpha lustre instances export-data](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/lustre/instances/export-data)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
