---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/functions/describe/
title: gcloud beta functions describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:20:00.160202+00:00
---

# gcloud beta functions describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/functions/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta functions describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta functions describe - display details of a Google Cloud Function 
SYNOPSIS
    

`gcloud beta functions describe` (`NAME` : `--region`=`REGION`) [`--v2`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Display details of a Google Cloud Function. 
POSITIONAL ARGUMENTS
    

Function resource - The Cloud Function name to describe. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `NAME` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`NAME`
     ID of the function or fully qualified identifier for the function. 

To set the `function` attribute: 

  * provide the argument `NAME` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     The Cloud region for the function. Overrides the default `functions/region` property value for this command invocation. 

To set the `region` attribute: 

  * provide the argument `NAME` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line; 
  * set the property `functions/region`. 


FLAGS
    

`--v2`
     If specified, this command will use Cloud Functions v2 APIs and return the result in the v2 format (See https://cloud.google.com/functions/docs/reference/rest/v2/projects.locations.functions#Function). If not specified, 1st gen and 2nd gen functions will use v1 and v2 APIs respectively and return the result in the corresponding format (For v1 format, see https://cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions#resource:-cloudfunction). This command conflicts with `--no-gen2`. If specified with this combination, v2 APIs will be used. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud functions describe](https://docs.cloud.google.com/sdk/gcloud/reference/functions/describe)
    
    
    [gcloud alpha functions describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/functions/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
