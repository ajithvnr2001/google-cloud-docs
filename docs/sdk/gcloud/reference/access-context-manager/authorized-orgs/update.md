---
url: https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/authorized-orgs/update/
title: gcloud access-context-manager authorized-orgs update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:35:12.110366+00:00
---

# gcloud access-context-manager authorized-orgs update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/authorized-orgs/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud access-context-manager authorized-orgs update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud access-context-manager authorized-orgs update - update the organizations for an existing authorized organizations description 
SYNOPSIS
    

`gcloud access-context-manager authorized-orgs update` (`AUTHORIZED_ORGS_DESC` : `--policy`=`POLICY`) [`--add-orgs`=[`ORGS`,…] | `--clear-orgs` | `--remove-orgs`=[`ORGS`,…] | `--set-orgs`=[`ORGS`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     This command updates an authorized organizations description. 
EXAMPLES
     To update the organizations for an authorized organizations description: 
    
    
    gcloud access-context-manager authorized-orgs update my-authorized-orgs --add-orgs="organizations/123,organizations/456"

POSITIONAL ARGUMENTS
    

Authorized orgs desc resource - The authorized orgs desc to update. The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`AUTHORIZED_ORGS_DESC`
     ID of the authorized_orgs_desc or fully qualified identifier for the authorized_orgs_desc. 

To set the `authorized_orgs_desc` attribute: 

  * provide the argument `authorized_orgs_desc` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--policy`=`POLICY`
     The ID of the access policy. 

To set the `policy` attribute: 

  * provide the argument `authorized_orgs_desc` on the command line with a fully specified name; 
  * provide the argument `--policy` on the command line; 
  * set the property `access_context_manager/policy`. 


FLAGS
    

These flags modify the member orgs of this authorized_orgs_desc. Orgs must be organizations, in the form `organizations/<organizationsnumber>`. 

At most one of these can be specified: 

`--add-orgs`=[`ORGS`,…]
     Append the given values to the current orgs. 
`--clear-orgs`
     Empty the current orgs. 
`--remove-orgs`=[`ORGS`,…]
     Remove the given values from the current orgs. 
`--set-orgs`=[`ORGS`,…]
     Completely replace the current orgs with the given values. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This variant is also available: 
    
    
    [gcloud alpha access-context-manager authorized-orgs update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/authorized-orgs/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
