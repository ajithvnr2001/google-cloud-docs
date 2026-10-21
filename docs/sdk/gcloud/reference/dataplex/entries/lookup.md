---
url: https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/entries/lookup/
title: gcloud dataplex entries lookup \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:56:19.359768+00:00
---

# gcloud dataplex entries lookup  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/entries/lookup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud dataplex entries lookup Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud dataplex entries lookup - lookup a Dataplex entry 
SYNOPSIS
    

`gcloud dataplex entries lookup` (`ENTRY` : `--entry-group`=`ENTRY_GROUP` `--location`=`LOCATION`) [`--aspect-types`=[`ASPECT_TYPES`,…]] [`--paths`=[`PATHS`,…]] [`--view`=`VIEW`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Lookup a Dataplex entry. 

Displays the details of a Dataplex entry resource given a valid entry ID. Unlike `describe`, where the Dataplex permission is required for access, for `lookup` the permission from the original source system is required on the entry instead. For example, if the source is a BigQuery table, you need the `bigquery.tables.get` permission to lookup an entry. 

EXAMPLES
     To lookup a Dataplex entry `entry1` within entry group `entry-group1` in location `us-central1`, run: 
    
    
    gcloud dataplex entries lookup entry1 --entry-group=entry-group1 --location=us-central1 --project=test-project

POSITIONAL ARGUMENTS
    

Entry resource - Arguments and flags that define the Dataplex Entry you want to lookup. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `entry` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`ENTRY`
     ID of the entry or fully qualified identifier for the entry. 

To set the `entry` attribute: 

  * provide the argument `entry` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--entry-group`=`ENTRY_GROUP`
     Entry group containing Dataplex Entries. To set the `entry-group` attribute: 

  * provide the argument `entry` on the command line with a fully specified name; 
  * provide the argument `--entry-group` on the command line. 


`--location`=`LOCATION`
     Location of the Dataplex resource. To set the `location` attribute: 

  * provide the argument `entry` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `dataplex/location`. 


FLAGS
    

`--aspect-types`=[`ASPECT_TYPES`,…]
     Limits the aspects returned to the provided aspect types. Only works if the `--view=custom` is selected. 

For example, if two aspect types are specified: "projects/projectA/locations/us-central1/my-aspect-type,projects/projectB/locations/us/my-aspect-type2" then only aspects matching these aspect types will be returned. 

Can be further constrained by the `--paths` argument. 

`--paths`=[`PATHS`,…]
     Limits the aspects returned to those associated with the provided paths within the Entry. Only works if the `--view=custom` is selected. 

For example, if two paths are specified: "--paths=property1,property2" then only aspects on these paths will be returned. 

To return aspects without any path, the empty (root) path can be specified. For this "." can be used. For example, when "--paths=.,property1" are specified, then only aspects on the path "property1" and on the entry itself will be returned. 

Can be further constrained by `--aspect-types` argument. 

`--view`=`VIEW`
     Controls which parts of an entry are to be returned. `VIEW` must be one of: 

`all`
     Returns all aspects. If the number of aspects would exceed 100, the first 100 will be returned. 
`basic`
     Returns entry only, without aspects. 
`custom`
     Returns aspects filtered based on `--aspect-types` AND `--paths` arguments specified. When used, at least one of `--aspect-types` and `--paths` arguments must be specified. If the number of aspects would exceed 100, the first 100 will be returned. 
`full`
     Default value. Returns all required aspects, as well as the keys of all non-required aspects. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `dataplex/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/dataplex/docs>
NOTES
     This variant is also available: 
    
    
    [gcloud alpha dataplex entries lookup](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataplex/entries/lookup)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
