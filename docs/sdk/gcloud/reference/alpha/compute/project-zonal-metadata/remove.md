---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/project-zonal-metadata/remove/
title: gcloud alpha compute project-zonal-metadata remove \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T08:29:48.605938+00:00
---

# gcloud alpha compute project-zonal-metadata remove  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/project-zonal-metadata/remove/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute project-zonal-metadata remove Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute project-zonal-metadata remove - remove project zonal metadata 
SYNOPSIS
    

`gcloud alpha compute project-zonal-metadata remove` `--zone`=`ZONE` [`--all` | `--keys`=`KEY`,[`KEY`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha compute project-zonal-metadata remove` is used to remove project zonal metadata from all VMs within the specified zone. For information about metadata, see <https://cloud.google.com/compute/docs/metadata>. 

Only the metadata keys that you provide in the command get removed. All other existing metadata entries remain the same. 

After you remove a specific project zonal metadata entry, if that metadata key has any project-wide value configured, then the VMs in the zone automatically inherit that project-wide value. 

EXAMPLES
     To remove the project zonal metadata with key=value in the zone ``us-central1-a`` for the project ``my-gcp-project``, run: 
    
    
    gcloud alpha compute project-zonal-metadata remove --keys=key --zone=us-central1-a --project=my-gcp-project

For more information and examples about how to remove project zonal metadata, see <https://cloud.google.com/compute/docs/metadata/setting-custom-metadata#remove-custom-project-zonal-metadata>

REQUIRED FLAGS
    

`--zone`=`ZONE`
     The zone in which you want to remove project zonal metadata 
OPTIONAL FLAGS
    

At most one of these can be specified: 

`--all`
     If provided, all project zonal metadata entries are removed from VM instances in the zone. 
`--keys`=`KEY`,[`KEY`,…]
     The keys for which you want to remove project zonal metadata 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute project-zonal-metadata remove](https://docs.cloud.google.com/sdk/gcloud/reference/compute/project-zonal-metadata/remove)
    
    
    [gcloud beta compute project-zonal-metadata remove](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/project-zonal-metadata/remove)
    
    
    [gcloud preview compute project-zonal-metadata remove](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/project-zonal-metadata/remove)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
