---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshot-settings/update/
title: gcloud compute snapshot-settings update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:47:51.607594+00:00
---

# gcloud compute snapshot-settings update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshot-settings/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute snapshot-settings update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute snapshot-settings update - update snapshot settings 
SYNOPSIS
    

`gcloud compute snapshot-settings update` [`--async`] [`--storage-location-names`=[`STORAGE_LOCATION_NAMES`,…]] [`--storage-location-policy`=`STORAGE_LOCATION_POLICY`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update the snapshot settings of a project. 
EXAMPLES
     To update the snapshot settings and set the storage location policy to the nearest multi-region as the source disk, run: 
    
    
    gcloud compute snapshot-settings update --storage-location-policy=nearest-multi-region

To update the snapshot settings and set the storage location policy to the same region as the source disk, run: 
    
    
    gcloud compute snapshot-settings update --storage-location-policy=local-region

To update the snapshot settings and set the storage location policy to store snapshots in a specific location like `us-west1`, run: 
    
    
    gcloud compute snapshot-settings update --storage-location-policy=specific-locations --storage-location-names=us-west1

FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--storage-location-names`=[`STORAGE_LOCATION_NAMES`,…]
     The custom storage location that you specify for the project's snapshots. You can specify only a single location. Use this flag only when you use the specific-locations value for the `--storage-location-policy` flag. For more information, refer to the snapshot settings documentation at <https://cloud.google.com/compute/docs/disks/snapshot-settings>. 
`--storage-location-policy`=`STORAGE_LOCATION_POLICY`
     The storage location policy. For more information, refer to the snapshot settings documentation at <https://cloud.google.com/compute/docs/disks/snapshot-settings>. STORAGE_LOCATION_POLICY must be one of: local-region, nearest-multi-region, specific-locations. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the compute/alpha or compute/beta or compute/v1 API. The full documentation for this API can be found at: <https://cloud.google.com/compute/>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha compute snapshot-settings update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/snapshot-settings/update)
    
    
    [gcloud beta compute snapshot-settings update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/snapshot-settings/update)
    
    
    [gcloud preview compute snapshot-settings update](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/snapshot-settings/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
