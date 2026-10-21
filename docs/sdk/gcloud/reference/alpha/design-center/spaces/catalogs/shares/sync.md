---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/catalogs/shares/sync/
title: gcloud alpha design-center spaces catalogs shares sync \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:20:50.902579+00:00
---

# gcloud alpha design-center spaces catalogs shares sync  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/catalogs/shares/sync/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha design-center spaces catalogs shares sync Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha design-center spaces catalogs shares sync - sync a share 
SYNOPSIS
    

`gcloud alpha design-center spaces catalogs shares sync` (`SHARE` : `--catalog`=`CATALOG` `--location`=`LOCATION` `--space`=`SPACE`) [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Sync a share in a catalog. 
EXAMPLES
     To sync the share `my-share` in catalog `my-catalog`, space `my-space`, project `my-project` and location `us-central1`, run: 
    
    
    gcloud alpha design-center spaces catalogs shares sync my-share --catalog=my-catalog --space=my-space --location=us-central1

Or run: 
    
    
    gcloud alpha design-center spaces catalogs shares sync projects/my-project/locations/us-central1/spaces/my-space/catalogs/my-catalog/shares/my-share

To sync the share `my-share` in catalog `my-catalog`, space `my-space`, project `my-project` and location `us-central1` asynchronously, run: 
    
    
    gcloud alpha design-center spaces catalogs shares sync --catalog=my-catalog --space=my-space --location=us-central1 --async

POSITIONAL ARGUMENTS
    

Share resource - The share name in the following format: `projects/$project/locations/$location/spaces/$space/catalogs/$catalog/shares/$share` The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `share` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`SHARE`
     ID of the share or fully qualified identifier for the share. 

To set the `share` attribute: 

  * provide the argument `share` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--catalog`=`CATALOG`
     The catalog id of the share resource. 

To set the `catalog` attribute: 

  * provide the argument `share` on the command line with a fully specified name; 
  * provide the argument `--catalog` on the command line. 


`--location`=`LOCATION`
     The location id of the share resource. 

To set the `location` attribute: 

  * provide the argument `share` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--space`=`SPACE`
     The space id of the share resource. 

To set the `space` attribute: 

  * provide the argument `share` on the command line with a fully specified name; 
  * provide the argument `--space` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `designcenter/v1alpha` API. The full documentation for this API can be found at: <http://cloud.google.com/application-design-center/docs>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud design-center spaces catalogs shares sync](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/catalogs/shares/sync)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-09 UTC."],[],[]] 
