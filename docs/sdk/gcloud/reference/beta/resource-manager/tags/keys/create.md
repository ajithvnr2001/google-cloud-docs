---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/resource-manager/tags/keys/create/
title: gcloud beta resource-manager tags keys create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:44:04.478830+00:00
---

# gcloud beta resource-manager tags keys create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/resource-manager/tags/keys/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta resource-manager tags keys create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta resource-manager tags keys create - creates a TagKey resource under the specified tag parent 
SYNOPSIS
    

`gcloud beta resource-manager tags keys create` (`SHORT_NAME` `--parent`=`PARENT`) [`--allowed-values-regex`=`ALLOWED_VALUES_REGEX`] [`--async`] [`--description`=`DESCRIPTION`] [`--purpose`=`PURPOSE`] [`--purpose-data`=[`network`=`NETWORK`],[`organization`=`ORGANIZATION`]] [`GCLOUD_WIDE_FLAG …`]
EXAMPLES
     To create a TagKey with the name env under 'organizations/123' with description 'description', run: 
    
    
    gcloud beta resource-manager tags keys create env --parent=organizations/123 --description=description

POSITIONAL ARGUMENTS
    

TagKey. 

This must be specified. 

`SHORT_NAME`
     User specified, friendly name of the TagKey or TagValue. The field must be 1-63 characters, beginning and ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores ( _ ), dots (.), and alphanumerics between. 

This positional argument must be specified if any of the other arguments in this group are specified. 

`--parent`=`PARENT`
     Parent of the TagKey in the form of organizations/{org_id}. 

This flag argument must be specified if any of the other arguments in this group are specified. 

FLAGS
    

`--allowed-values-regex`=`ALLOWED_VALUES_REGEX`
     User-assigned regex of allowed short names of TagValues under a TagKey. 
`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     User-assigned description of the TagKey or TagValue. Must not exceed 256 characters. 
`--purpose`=`PURPOSE`
     Purpose specifier of the TagKey that can only be set on creation. Specifying this field adds additional validation from the policy system that corresponds to the purpose. `PURPOSE` must be one of: `GCE_FIREWALL`, `DATA_GOVERNANCE`. 
`--purpose-data`=[`network`=`NETWORK`],[`organization`=`ORGANIZATION`]
     Purpose data of the TagKey that can only be set on creation. This data is validated by the policy system that corresponds to the purpose. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud resource-manager tags keys create](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/keys/create)
    
    
    [gcloud alpha resource-manager tags keys create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/resource-manager/tags/keys/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
