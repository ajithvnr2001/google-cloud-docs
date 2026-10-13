---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/active-directory/domains/extend-schema/
title: gcloud beta active-directory domains extend-schema \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:09:53.217109+00:00
---

# gcloud beta active-directory domains extend-schema  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/active-directory/domains/extend-schema/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta active-directory domains extend-schema Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta active-directory domains extend-schema - initiate schema extension for a Managed Microsoft AD domain 
SYNOPSIS
    

`gcloud beta active-directory domains extend-schema` `DOMAIN` `--description`=`DESCRIPTION` `--ldif-file`=`PATH_TO_FILE` [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Initiate schema extension for a Managed Microsoft AD domain. 

This command can fail for the following reasons: 

  * The specified domain doesn't exist. 
  * The specified domain is either being created or updated. 
  * The specified domain is under maintenance. 
  * The active account doesn't have permission to initiate schema extension on the specified domain. 


EXAMPLES
     The following command initiates a schema extension for the domain `my-domain.com` in project `my-project`, with description `Test Description`, using the LDIF file `demo.ldif`
    
    
    gcloud beta active-directory domains extend-schema my-domain.com --description="Test Description" --ldif-file=demo.ldf --project=my-project --async

POSITIONAL ARGUMENTS
    

Domain resource - Name of the Managed Microsoft AD domain for which you want to extend schema. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `domain` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`DOMAIN`
     ID of the domain or fully qualified identifier for the domain. 

To set the `domain` attribute: 

  * provide the argument `domain` on the command line. 


REQUIRED FLAGS
    

`--description`=`DESCRIPTION`
     Description of schema change. 
`--ldif-file`=`PATH_TO_FILE`
     Local LDIF file path that contains commands for schema extension. The file size can't be larger than 1 MB. Use a full or relative path to a local file containing the value of ldif_file. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `managedidentities/v1beta1` API. The full documentation for this API can be found at: <https://cloud.google.com/managed-microsoft-ad/>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud active-directory domains extend-schema](https://docs.cloud.google.com/sdk/gcloud/reference/active-directory/domains/extend-schema)
    
    
    [gcloud alpha active-directory domains extend-schema](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/extend-schema)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
