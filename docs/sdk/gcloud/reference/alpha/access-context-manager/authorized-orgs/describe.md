---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/authorized-orgs/describe/
title: gcloud alpha access-context-manager authorized-orgs describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:59:03.745383+00:00
---

# gcloud alpha access-context-manager authorized-orgs describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/authorized-orgs/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha access-context-manager authorized-orgs describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha access-context-manager authorized-orgs describe - show details about an authorized organizations description 
SYNOPSIS
    

`gcloud alpha access-context-manager authorized-orgs describe` (`AUTHORIZED_ORGS_DESC` : `--policy`=`POLICY`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Show details about an existing authorized organizations description. 
EXAMPLES
     To get details about an existing authorized organizations description, run: 
    
    
    gcloud alpha access-context-manager authorized-orgs describe my_authorized_orgs_desc_id

POSITIONAL ARGUMENTS
    

Authorized orgs desc resource - The authorized organizations description for which you want to show details. The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`AUTHORIZED_ORGS_DESC`
     ID of the authorized-orgs-desc or fully qualified identifier for the authorized-orgs-desc. 

To set the `authorized_orgs_desc` attribute: 

  * provide the argument `authorized_orgs_desc` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--policy`=`POLICY`
     The ID of the access policy. To set the `policy` attribute: 

  * provide the argument `authorized_orgs_desc` on the command line with a fully specified name; 
  * provide the argument `--policy` on the command line; 
  * set the property `access_context_manager/policy`; 
  * automatically, if the current account belongs to an organization with exactly one access policy.. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `accesscontextmanager/v1alpha` API. The full documentation for this API can be found at: <https://cloud.google.com/access-context-manager/docs/reference/rest/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud access-context-manager authorized-orgs describe](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/authorized-orgs/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
