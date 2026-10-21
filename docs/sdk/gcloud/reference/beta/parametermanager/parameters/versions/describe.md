---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/parametermanager/parameters/versions/describe/
title: gcloud beta parametermanager parameters versions describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:34:40.758616+00:00
---

# gcloud beta parametermanager parameters versions describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/parametermanager/parameters/versions/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta parametermanager parameters versions describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta parametermanager parameters versions describe - gets a single Parameter Manager parameter version 
SYNOPSIS
    

`gcloud beta parametermanager parameters versions describe` (`PARAMETER_VERSION` : `--location`=`LOCATION` `--parameter`=`PARAMETER`) [`--view`=`VIEW`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Gets a single parameter version, along with payload supplied by the user at the time of creation. If the payload contains any references to secrets, these will not be rendered in the output. 
EXAMPLES
     To get a single parameter version `my-parameter-version` of parameter `my-parameter` in location `global` run: 
    
    
    gcloud beta parametermanager parameters versions describe my-parameter-version --parameter=my-parameter --location=global

POSITIONAL ARGUMENTS
    

ParameterVersion resource - Name of the resource in the format `projects/*/locations/*/parameters/*/versions/*`. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `parameter_version` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`PARAMETER_VERSION`
     ID of the parameterVersion or fully qualified identifier for the parameterVersion. 

To set the `parameter_version` attribute: 

  * provide the argument `parameter_version` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location id of the parameterVersion resource. 

To set the `location` attribute: 

  * provide the argument `parameter_version` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--parameter`=`PARAMETER`
     The parameter id of the parameterVersion resource. 

To set the `parameter` attribute: 

  * provide the argument `parameter_version` on the command line with a fully specified name; 
  * provide the argument `--parameter` on the command line. 


FLAGS
    

`--view`=`VIEW`
     View of the ParameterVersion. In the default FULL view, all metadata & payload associated with the ParameterVersion will be returned. `VIEW` must be one of: 

`basic`
     Include only the metadata for the resource. 
`full`
     Include metadata & other relevant payload data as well. This is the default view. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `parametermanager/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/secret-manager/parameter-manager/docs/overview>
NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud parametermanager parameters versions describe](https://docs.cloud.google.com/sdk/gcloud/reference/parametermanager/parameters/versions/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-09 UTC."],[],[]] 
