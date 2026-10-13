---
url: https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/print-settings/npm/
title: gcloud artifacts print-settings npm \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:31:11.616421+00:00
---

# gcloud artifacts print-settings npm  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/print-settings/npm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud artifacts print-settings npm Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud artifacts print-settings npm - print credential settings to add to the .npmrc file 
SYNOPSIS
    

`gcloud artifacts print-settings npm` [`--json-key`=`JSON_KEY`] [`--scope`=`SCOPE`] [`--location`=`LOCATION` `--repository`=`REPOSITORY`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Print credential settings to add to the .npmrc file for connecting to an npm repository. 
EXAMPLES
     To print a snippet for the repository set in the `artifacts/repository` property in the default location: 
    
    
    gcloud artifacts print-settings npm

To print a snippet for repository `my-repository` in the default location: 
    
    
    gcloud artifacts print-settings npm --repository="my-repository"

To print a snippet using service account key: 
    
    
    gcloud artifacts print-settings npm --json-key=path/to/key.json

To print a snippet for the repository set in the `artifacts/repository` property with scope @my-company: 
    
    
    gcloud artifacts print-settings npm --scope=@my-company

FLAGS
    

`--json-key`=`JSON_KEY`
     Path to service account JSON key. If not specified, current active service account credentials or a placeholder for gcloud credentials is used. 
`--scope`=`SCOPE`
     The scope to associate with the Artifact Registry registry. If not specified, Artifact Registry is set as the default registry. 
Repository resource - The Artifact Registry repository. If not specified, the current artifacts/repository is used. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--repository` on the command line with a fully specified name; 
  * set the property `artifacts/repository` with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


`--location`=`LOCATION`
     Location of the repository. 

To set the `location` attribute: 

  * provide the argument `--repository` on the command line with a fully specified name; 
  * set the property `artifacts/repository` with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `artifacts/location`. 


`--repository`=`REPOSITORY`
     ID of the repository or fully qualified identifier for the repository. 

To set the `repository` attribute: 

  * provide the argument `--repository` on the command line; 
  * set the property `artifacts/repository`. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha artifacts print-settings npm](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/artifacts/print-settings/npm)
    
    
    [gcloud beta artifacts print-settings npm](https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/print-settings/npm)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
