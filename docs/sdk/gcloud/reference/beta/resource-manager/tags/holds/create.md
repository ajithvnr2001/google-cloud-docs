---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/resource-manager/tags/holds/create/
title: gcloud beta resource-manager tags holds create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:44:03.679977+00:00
---

# gcloud beta resource-manager tags holds create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/resource-manager/tags/holds/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta resource-manager tags holds create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta resource-manager tags holds create - create a TagHold resource 
SYNOPSIS
    

`gcloud beta resource-manager tags holds create` `PARENT` `--holder`=`HOLDER` [`--help-link`=`HELP_LINK`] [`--location`=`LOCATION`] [`--origin`=`ORIGIN`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a TagHold under a TagValue, indicating that the TagValue is being used by a holder (cloud resource) from an (optional) origin. The TagValue can be represented with its numeric id or its namespaced name of {parent_namespace}/{tag_key_short_name}/{tag_value_short_name}. 
EXAMPLES
     To create a TagHold on tagValues/123, with holder cloud-resource-holder, origin creator-origin, in region us-central1-a, with help link www.example.help.link.com, run: 
    
    
    gcloud beta resource-manager tags holds create tagValues/123 --holder=cloud-resource-holder --origin=creator-origin --help-link=www.example.help.link.com --location=us-central1-a

To create a TagHold under TagValue test under TagKey env in organization id 789, with holder cloud-resource-holder, run: 
    
    
    gcloud beta resource-manager tags holds create 789/env/test --holder=cloud-resource-holder

POSITIONAL ARGUMENTS
    

`PARENT`
     Tag value name or namespaced name. 
REQUIRED FLAGS
    

`--holder`=`HOLDER`
     The name of the resource where the TagValue is being used. Must be less than 200 characters. 
OPTIONAL FLAGS
    

`--help-link`=`HELP_LINK`
     A URL where an end user can learn more about removing this hold. 
`--location`=`LOCATION`
     Region or zone where the TagHold will be stored. If not provided, the TagHold will be stored in a "global" region. 
`--origin`=`ORIGIN`
     An optional string representing the origin of this request. This field should include human-understandable information to distinguish origins from each other. Must be less than 200 characters. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud resource-manager tags holds create](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/holds/create)
    
    
    [gcloud alpha resource-manager tags holds create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/resource-manager/tags/holds/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
