---
url: https://docs.cloud.google.com/sdk/gcloud/reference/secrets/versions/access/
title: gcloud secrets versions access \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:53:11.343742+00:00
---

# gcloud secrets versions access  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/secrets/versions/access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud secrets versions access Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud secrets versions access - access a secret version's data 
SYNOPSIS
    

`gcloud secrets versions access` (`VERSION` : `--secret`=`SECRET`) [`--location`=`LOCATION`] [`--out-file`=`OUT-FILE-PATH`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Access the data for the specified secret version. 
EXAMPLES
     Access the data for version 123 of the secret 'my-secret': 
    
    
    gcloud secrets versions access 123 --secret=my-secret

Note: The output will be formatted as UTF-8 which can corrupt binary secrets. 

To write raw bytes to a file use --out-file flag: 
    
    
    gcloud secrets versions access 123 --secret=my-secret --out-file=/tmp/secret

To get the raw bytes, have Google Cloud CLI print the response as base64-encoded and decode: 
    
    
    gcloud secrets versions access 123 --secret=my-secret --format='get(payload.data)' | tr '_-' '/+' | base64 -d

POSITIONAL ARGUMENTS
    

Version resource - Numeric secret version to access or a configured alias (including 'latest' to use the latest version). The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `VERSION` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`VERSION`
     ID of the version or fully qualified identifier for the version. 

To set the `version` attribute: 

  * provide the argument `VERSION` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--secret`=`SECRET`
     The secret of the version. 

To set the `secret` attribute: 

  * provide the argument `VERSION` on the command line with a fully specified name; 
  * provide the argument `--secret` on the command line. 


FLAGS
    

Location resource - The location to access secret. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--location` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


`--location`=`LOCATION`
     ID of the location or fully qualified identifier for the location. 

To set the `location` attribute: 

  * provide the argument `--location` on the command line. 


`--out-file`=`OUT-FILE-PATH`
     File path to which secret data is written. If this flag is not provided secret data will be written to stdout in UTF-8 format. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This variant is also available: 
    
    
    [gcloud beta secrets versions access](https://docs.cloud.google.com/sdk/gcloud/reference/beta/secrets/versions/access)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
