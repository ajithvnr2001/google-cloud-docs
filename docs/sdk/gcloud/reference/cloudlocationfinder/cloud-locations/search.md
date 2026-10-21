---
url: https://docs.cloud.google.com/sdk/gcloud/reference/cloudlocationfinder/cloud-locations/search/
title: gcloud cloudlocationfinder cloud-locations search \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T06:55:55.312056+00:00
---

# gcloud cloudlocationfinder cloud-locations search  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/cloudlocationfinder/cloud-locations/search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud cloudlocationfinder cloud-locations search Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud cloudlocationfinder cloud-locations search - search cloudLocations 
SYNOPSIS
    

`gcloud cloudlocationfinder cloud-locations search` `--source-cloud-location`=`SOURCE_CLOUD_LOCATION` [`--limit`=`LIMIT`] [`--location`=`LOCATION`] [`--page-size`=`PAGE_SIZE`] [`--query`=`QUERY`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Search Cloudlocations. 
EXAMPLES
     To search CloudLocations, run: 
    
    
    gcloud cloudlocationfinder cloud-locations search --source-cloud-location=aws-us-east-1 --query=display_name="us-east4"

REQUIRED FLAGS
    

Source cloud location resource - The source Cloud location. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--source-cloud-location` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--source-cloud-location` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * location is always global. 



This must be specified. 

`--source-cloud-location`=`SOURCE_CLOUD_LOCATION`
     ID of the source_cloud_location or fully qualified identifier for the source_cloud_location. 

To set the `cloud_location` attribute: 

  * provide the argument `--source-cloud-location` on the command line. 


OPTIONAL FLAGS
    

`--limit`=`LIMIT`
     Maximum number of resources to return. 
Location resource - The resource location. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--location` on the command line with a fully specified name; 
  * location is always global with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


`--location`=`LOCATION`
     ID of the location or fully qualified identifier for the location. 

To set the `location` attribute: 

  * provide the argument `--location` on the command line; 
  * location is always global. 


`--page-size`=`PAGE_SIZE`
     Maximum number of resources per page. 
`--query`=`QUERY`
     Query to use for searching Cloudlocations. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This variant is also available: 
    
    
    [gcloud alpha cloudlocationfinder cloud-locations search](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/cloudlocationfinder/cloud-locations/search)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
