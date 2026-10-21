---
url: https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/rbacrolebindingactuation/update/
title: gcloud container hub rbacrolebindingactuation update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:20:08.633389+00:00
---

# gcloud container hub rbacrolebindingactuation update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/rbacrolebindingactuation/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud container hub rbacrolebindingactuation update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud container hub rbacrolebindingactuation update - update RbacRoleBinding Actuation Feature 
SYNOPSIS
    

`gcloud container hub rbacrolebindingactuation update` (`--add-allowed-custom-role`=`ADD_ALLOWED_CUSTOM_ROLE` | `--allowed-custom-roles`=[`ROLES`,…] | `--remove-allowed-custom-role`=`REMOVE_ALLOWED_CUSTOM_ROLE`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     This command updates RbacRoleBinding Actuation Feature in a fleet. 
EXAMPLES
     To update the RbacRoleBinding Actuation Feature, run: 
    
    
    [gcloud container fleet](https://docs.cloud.google.com/sdk/gcloud/reference/container/fleet) rbacrolebinding-actuation update --allowed-custom-roles=role1,role2
    
    
    [gcloud container fleet](https://docs.cloud.google.com/sdk/gcloud/reference/container/fleet) rbacrolebinding-actuation update --add-allowed-custom-role=role1
    
    
    [gcloud container fleet](https://docs.cloud.google.com/sdk/gcloud/reference/container/fleet) rbacrolebinding-actuation update --remove-allowed-custom-role=role2

REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--add-allowed-custom-role`=`ADD_ALLOWED_CUSTOM_ROLE`
     Add a single custom role to the allowed custom roles list. 
`--allowed-custom-roles`=[`ROLES`,…]
     The list of allowed custom roles that can be used in scope RBACRoleBindings. 
`--remove-allowed-custom-role`=`REMOVE_ALLOWED_CUSTOM_ROLE`
     Remove a single custom role from the allowed custom roles list. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha container hub rbacrolebindingactuation update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/hub/rbacrolebindingactuation/update)
    
    
    [gcloud beta container hub rbacrolebindingactuation update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/rbacrolebindingactuation/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
