---
url: https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/policies/create/
title: gcloud access-context-manager policies create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:35:14.213535+00:00
---

# gcloud access-context-manager policies create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/policies/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud access-context-manager policies create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud access-context-manager policies create - create a new access policy 
SYNOPSIS
    

`gcloud access-context-manager policies create` `--organization`=`ORGANIZATION` `--title`=`TITLE` [`--async`] [`--scopes`=[`SCOPES`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a new Access Context Manager policy. An Access Context Manager policy, also known as an access policy, is a container for access levels and VPC Service Controls service perimeters. 

You can optionally specify either a folder or a project as a scope of an access policy. A scoped policy only allows projects under that scope to be restricted by any service perimeters defined with that policy. The scope must be within the organization that this policy is associated with. You can specify only one folder or project as the scope for an access policy. If you don't specify a scope, then the scope extends to the entire organization and any projects within the organization can be added to service perimeters in this policy. 

This command only creates an access policy. Access levels and service perimeters need to be created explicitly. 

EXAMPLES
     To create an access policy that applies to the entire organization, run: 
    
    
    gcloud access-context-manager policies create --organization=organizations/123 --title="My Policy"

To create an access policy that applies to the folder with the ID 345, run: 
    
    
    gcloud access-context-manager policies create --organization=organizations/123 --scopes=folders/345 --title="My Folder Policy"

Only projects within this folder can be added to service perimeters within this policy. 

To create an access policy that applies only to the project with the project number 567, run: 
    
    
    gcloud access-context-manager policies create --organization=organizations/123 --scopes=projects/567 --title="My Project Policy"

REQUIRED FLAGS
    

`--organization`=`ORGANIZATION`
     Parent organization for the access policies. 
`--title`=`TITLE`
     Short human-readable title of the access policy. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--scopes`=[`SCOPES`,…]
     Folder or project on which this policy is applicable. You can specify only one folder or project as the scope and the scope must exist within the specified organization. If you don't specify a scope, the policy applies to the entire organization. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `accesscontextmanager/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/access-context-manager/docs/reference/rest/>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha access-context-manager policies create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/policies/create)
    
    
    [gcloud beta access-context-manager policies create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/policies/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
