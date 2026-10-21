---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/memberships/bindings/describe/
title: gcloud beta container hub memberships bindings describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:17:48.622352+00:00
---

# gcloud beta container hub memberships bindings describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/memberships/bindings/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta container hub memberships bindings describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta container hub memberships bindings describe - show Membership-Binding info 
SYNOPSIS
    

`gcloud beta container hub memberships bindings describe` (`BINDING` : `--location`=`LOCATION` `--membership`=`MEMBERSHIP`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` This command can fail for the following reasons: 

  * The Membership specified does not exist. 
  * The Membership Binding specified does not exist in the project. 
  * The caller does not have permission to access the Membership Binding. 
  * The caller did not specify the location (--location) if referring to location other than global. 


EXAMPLES
     To print metadata for the membership Binding `BINDING_NAME` in a global membership `MEMBERSHIP_NAME`, run: 
    
    
    gcloud beta container hub memberships bindings describe BINDING_NAME --membership=MEMBERSHIP_NAME

To print metadata for the Binding `BINDING_NAME` associated with regional membership `MEMBERSHIP_NAME`, provide the location LOCATION_NAME for the Membership where the Binding belongs along with membership name. 
    
    
    gcloud beta container hub memberships bindings describe BINDING_NAME --membership=MEMBERSHIP_NAME --location=LOCATION_NAME

POSITIONAL ARGUMENTS
    

Binding resource - The group of arguments defining a Membership Binding. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `BINDING` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`BINDING`
     ID of the binding or fully qualified identifier for the binding. 

To set the `binding` attribute: 

  * provide the argument `BINDING` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Location for the binding. 

To set the `location` attribute: 

  * provide the argument `BINDING` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `gkehub/location`. 


`--membership`=`MEMBERSHIP`
     Name of the binding. 

To set the `membership` attribute: 

  * provide the argument `BINDING` on the command line with a fully specified name; 
  * provide the argument `--membership` on the command line. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud container hub memberships bindings describe](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/memberships/bindings/describe)
    
    
    [gcloud alpha container hub memberships bindings describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/hub/memberships/bindings/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
