---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/lustre/instances/mirrors/create/
title: gcloud alpha lustre instances mirrors create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:45:02.521133+00:00
---

# gcloud alpha lustre instances mirrors create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/lustre/instances/mirrors/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha lustre instances mirrors create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha lustre instances mirrors create - creates a Managed Lustre mirror 
SYNOPSIS
    

`gcloud alpha lustre instances mirrors create` (`MIRROR` : `--instance`=`INSTANCE` `--location`=`LOCATION`) `--direction`=`DIRECTION` `--gcs-path-uri`=`GCS_PATH_URI` `--lustre-path`=`LUSTRE_PATH` [`--async`] [`--deleted-files-retained`] [`--description`=`DESCRIPTION`] [`--labels`=[`LABELS`,…]] [`--request-id`=`REQUEST_ID`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Creates a Managed Lustre mirror for an instance. 
EXAMPLES
     To create a mirror `my-mirror` for instance `my-instance` in location `us-central1-a` syncing from `gs://my-bucket/data/` to `/data` run: 
    
    
    gcloud alpha lustre instances mirrors create my-mirror --instance=my-instance --location=us-central1-a --gcs-path-uri=gs://my-bucket/data/ --lustre-path=/data --direction=from-cloud-storage

POSITIONAL ARGUMENTS
    

Mirror resource - Identifier. Name of the mirror. Format: `projects/{project}/locations/{location}/instances/{instance}/mirrors/{mirror}` The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `mirror` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`MIRROR`
     ID of the mirror or fully qualified identifier for the mirror. 

To set the `mirror` attribute: 

  * provide the argument `mirror` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--instance`=`INSTANCE`
     The instance id of the mirror resource. 

To set the `instance` attribute: 

  * provide the argument `mirror` on the command line with a fully specified name; 
  * provide the argument `--instance` on the command line. 


`--location`=`LOCATION`
     The location id of the mirror resource. 

To set the `location` attribute: 

  * provide the argument `mirror` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

`--direction`=`DIRECTION`
     Represents the direction of the mirror. `DIRECTION` must be (only one value is supported): 

`from-cloud-storage`
     Mirror from Cloud Storage to Lustre. 
Specifies a Cloud Storage bucket and, optionally, a path inside the bucket. 

This must be specified. 

`--gcs-path-uri`=`GCS_PATH_URI`
     The URI to a Cloud Storage bucket, or a path within a bucket, using the format `gs://<bucket_name>/<optional_path_inside_bucket>/`. If a path inside the bucket is specified, it must end with a forward slash (`/`). 
The root directory path to the Lustre file system. 

This must be specified. 

`--lustre-path`=`LUSTRE_PATH`
     The root directory path to the Managed Lustre file system. Must start with `/`. Default is `/`. If you're importing data into Managed Lustre, any path other than the default must already exist on the file system. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--deleted-files-retained`
     If `true`, files are not deleted from Managed Lustre when the source files are deleted from Cloud Storage. Default is `false`. 
`--description`=`DESCRIPTION`
     Description of the mirror. 
`--labels`=[`LABELS`,…]
     Labels to apply to the mirror. 

`KEY`
     Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`VALUE`
     Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`Shorthand Example:`
    
    
    --labels=string=string

`JSON Example:`
    
    
    --labels='{"string": "string"}'

`File Example:`
    
    
    --labels=path_to_file.(yaml|json)

`--request-id`=`REQUEST_ID`
     The unique ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server guarantees that a request doesn't result in creation of duplicate mirrors for at least 60 minutes. 

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate mirrors. 

The request ID must be a valid UUID version 4 with the exception that zero UUID is not supported (`00000000-0000-0000-0000-000000000000`). This request is only idempotent if a `request_id` is provided. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `lustre/v1alpha` API. The full documentation for this API can be found at: <https://cloud.google.com/managed-lustre/docs>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
