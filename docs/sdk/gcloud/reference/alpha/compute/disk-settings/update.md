---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/disk-settings/update/
title: gcloud alpha compute disk-settings update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:44:56.993794+00:00
---

# gcloud alpha compute disk-settings update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/disk-settings/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute disk-settings update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute disk-settings update - update disk settings 
SYNOPSIS
    

`gcloud alpha compute disk-settings update` (`--region`=`REGION` | `--zone`=`ZONE`) [`--access-location-policy`=`ACCESS_LOCATION_POLICY`] [`--add-access-locations`=[`ADD_ACCESS_LOCATIONS`,…]] [`--remove-access-locations`=[`REMOVE_ACCESS_LOCATIONS`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Update disk settings. 
EXAMPLES
     To update the disk settings in zone us-west1-a, add the access location ``us-central1 `` and remove the access location ``us-central2`` in the project ``my-gcp-project``, run: 
    
    
    gcloud alpha compute disk-settings update --add-access-locations=us-central1 --remove-access-locations=us-central2 --project=my-gcp-project --zone=us-west1-a

REQUIRED FLAGS
    

Scope for disk settings. 

Exactly one of these must be specified: 

`--region`=`REGION`
     region for disk settings 
`--zone`=`ZONE`
     Zone for disk settings 
OPTIONAL FLAGS
    

`--access-location-policy`=`ACCESS_LOCATION_POLICY`
     The access location policy for disk settings. `ACCESS_LOCATION_POLICY` must be one of: 

`all-regions`
     All regions will be allowed to access the source disk. 
`specific-regions`
     Only the specified regions will be allowed to access the source disk. 
`--add-access-locations`=[`ADD_ACCESS_LOCATIONS`,…]
     Access locations to add to disk settings 
`--remove-access-locations`=[`REMOVE_ACCESS_LOCATIONS`,…]
     Access locations to remove from disk settings 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud beta compute disk-settings update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/disk-settings/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
