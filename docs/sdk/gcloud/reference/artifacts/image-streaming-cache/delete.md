---
url: https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/image-streaming-cache/delete/
title: gcloud artifacts image-streaming-cache delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:31:10.473766+00:00
---

# gcloud artifacts image-streaming-cache delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/image-streaming-cache/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud artifacts image-streaming-cache delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud artifacts image-streaming-cache delete - removes the prewarmed state of a specific artifact from a specific stream location 
SYNOPSIS
    

`gcloud artifacts image-streaming-cache delete` ([`ARTIFACT`] [(`--tag`=`TAG` | `--version`=`VERSION`) : [`--package`=`PACKAGE` : `--location`=`LOCATION` `--repository`=`REPOSITORY`]]) `--stream-location`=`STREAM_LOCATION` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Removes the prewarmed state of a specific artifact from a specific stream location. 
EXAMPLES
    
Removes the prewarmed state of a specific artifact using flags
    
    
    
    gcloud artifacts image-streaming-cache delete --package=my-pkg --tag=latest --repository=my-repo --location=us-central1 --stream-location=us-east1

Using full resource name
    
    
    
    gcloud artifacts image-streaming-cache delete projects/my-proj/locations/us-central1/repositories/my-repo/packages/my-pkg/versions/sha256:abc123 --stream-location=us-east1

POSITIONAL ARGUMENTS
    

Exactly one of these must be specified: 

[`ARTIFACT`]
     The full resource name of the version or tag to remove. 
Or at least one of these can be specified: 

Exactly one of these must be specified: 

`--tag`=`TAG`
     The tag to remove (e.g., 'latest'). 
`--version`=`VERSION`
     The version to remove (e.g., 'sha256:abc123'). 
Package resource - The package to remove. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--package` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


`--package`=`PACKAGE`
     ID of the package or fully qualified identifier for the package. 

To set the `name` attribute: 

  * provide the argument `--package` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Location of the package. 

To set the `location` attribute: 

  * provide the argument `--package` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `artifacts/location`. 


`--repository`=`REPOSITORY`
     Repository of the package. 

To set the `repository` attribute: 

  * provide the argument `--package` on the command line with a fully specified name; 
  * provide the argument `--repository` on the command line; 
  * set the property `artifacts/repository`. 


REQUIRED FLAGS
    

`--stream-location`=`STREAM_LOCATION`
     The target Cloud Region where the artifact should be prewarmed. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-16 UTC."],[],[]] 
