---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage/buckets/relocate/
title: gcloud alpha storage buckets relocate \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:54:39.085702+00:00
---

# gcloud alpha storage buckets relocate  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage/buckets/relocate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha storage buckets relocate Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha storage buckets relocate - relocates bucket between different locations 
SYNOPSIS
    

`gcloud alpha storage buckets relocate` ([`URL` `--location`=`LOCATION` : `--placement`=[`REGION`,…] `--destination-kms-key-name`=`DESTINATION_KMS_KEY_NAME` `--dry-run`] [`--operation`=`OPERATION` `--finalize` : `--ttl`=`TTL`]) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Relocates a bucket between different locations. 
EXAMPLES
     To move a bucket (``gs://my-bucket``) to the ``us-central1`` location, use the following command: 
    
    
    gcloud alpha storage buckets relocate gs://my-bucket --location=us-central1

To move a bucket to a custom dual-region, use the following command: 
    
    
    gcloud alpha storage buckets relocate gs://my-bucket --location=us --placement=us-central1,us-east1

To validate the operation without actually moving the bucket, use the following command: 
    
    
    gcloud alpha storage buckets relocate gs://my-bucket --location=us-central1 --dry-run

To schedule a write lock for the move, with ttl for reverting the write lock after 7h, if the relocation has not succeeded, use the following command: 
    
    
    gcloud alpha storage buckets relocate --operation=projects/_/buckets/my-bucket/operations/C894F35J --finalize --ttl=7h

POSITIONAL ARGUMENTS
    

Exactly one of these must be specified: 

Arguments for initiating the bucket relocate operation. 
`URL`
     The URL of the bucket to relocate. 

This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The final [location](https://cloud.google.com/storage/docs/locations) where the bucket will be relocated to. If no location is provided, Cloud Storage will use the default location, which is us. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--placement`=[`REGION`,…]
     A comma-separated list of regions that form the custom [dual-region](https://cloud.google.com/storage/docs/locations#location-dr). Only regions within the same continent are or will ever be valid. Invalid location pairs (such as mixed-continent, or with unsupported regions) will return an error. 
`--destination-kms-key-name`=`DESTINATION_KMS_KEY_NAME`
     This is only required when relocating a bucket that uses Customer-Managed Encryption Keys (CMEK). The full resource name of the Cloud KMS key to use for encrypting objects in the destination bucket. This key will be set as the default bucket encryption key. The key must exist in the destination location. Format: projects/PROJECT/locations/LOCATION/keyRings/RING/cryptoKeys/KEY 
`--dry-run`
     Prints the operations that the relocate command would perform without actually performing relocation. This is helpful to identify any issues that need to be detected asynchronously. 
Arguments for advancing the relocation operation. 
`--operation`=`OPERATION`
     Specify the relocation operation name to advance the relocation operation.The relocation operation name must include the Cloud Storage bucket and operation ID. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--finalize`
     Schedules the write lock to occur. Once activated, no further writes will be allowed to the associated bucket. This helps minimize disruption to bucket usage. For certain types of moves(between Multi Region and Custom Dual Regions), finalize is not required. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--ttl`=`TTL`
     Time to live for the relocation operation. Defaults to 12h if not provided. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud storage buckets relocate](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/relocate)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
