---
url: https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/scopes/rbacrolebindings/update/
title: gcloud container hub scopes rbacrolebindings update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:17:40.371221+00:00
---

# gcloud container hub scopes rbacrolebindings update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/scopes/rbacrolebindings/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud container hub scopes rbacrolebindings update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud container hub scopes rbacrolebindings update - update a fleet scope RBAC RoleBinding 
SYNOPSIS
    

`gcloud container hub scopes rbacrolebindings update` (`NAME` : `--location`=`LOCATION` `--scope`=`SCOPE`) [`--update-labels`=[`KEY`=`VALUE`,…]] [`--clear-labels` | `--remove-labels`=[`KEY`,…]] [`--custom-role`=`CUSTOM_ROLE` | `--role`=`ROLE`] [`--group`=`GROUP` | `--user`=`USER`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     This command can fail for the following reasons: 

  * The RoleBinding does not exist in the project. 
  * The caller does not have permission to access the RoleBinding. 


EXAMPLES
     To update the RBAC RoleBinding `RBRB` in scope `SCOPE` in the active project to the `viewer` role: 
    
    
    gcloud container hub scopes rbacrolebindings update RBRB --scope=SCOPE --role=viewer

To update the RBAC RoleBinding `RBRB` in scope `SCOPE` in the active project to the custom role `custom-role`: 
    
    
    gcloud container hub scopes rbacrolebindings update RBRB --scope=SCOPE --custom-role=custom-role

To update the RBAC RoleBinding `RBRB` in scope `SCOPE` in the active project to the user `someone@google.com`: 
    
    
    gcloud container hub scopes rbacrolebindings update RBRB --scope=SCOPE --user=someone@google.com

POSITIONAL ARGUMENTS
    

Rbacrolebinding resource - The group of arguments defining an RBACRoleBinding. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `NAME` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`NAME`
     ID of the rbacrolebinding or fully qualified identifier for the rbacrolebinding. 

To set the `rbacrolebinding` attribute: 

  * provide the argument `NAME` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Location for the rbacrolebinding. 

To set the `location` attribute: 

  * provide the argument `NAME` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `gkehub/location`. 


`--scope`=`SCOPE`
     Name of the rbacrolebinding. 

To set the `scope` attribute: 

  * provide the argument `NAME` on the command line with a fully specified name; 
  * provide the argument `--scope` on the command line. 


FLAGS
    

`--update-labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to update. If a label exists, its value is modified. Otherwise, a new label is created. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

At most one of these can be specified: 

`--clear-labels`
     Remove all labels. If `--update-labels` is also specified then `--clear-labels` is applied first. 

For example, to remove all labels: 
    
    
    gcloud container hub scopes rbacrolebindings update --clear-labels

To remove all existing labels and create two new labels, ``foo`` and ``baz``: 
    
    
    gcloud container hub scopes rbacrolebindings update --clear-labels --update-labels foo=bar,baz=qux

`--remove-labels`=[`KEY`,…]
     List of label keys to remove. If a label does not exist it is silently ignored. If `--update-labels` is also specified then `--update-labels` is applied first. 
At most one of these can be specified: 

`--custom-role`=`CUSTOM_ROLE`
     Custom role to assign to principal. 
`--role`=`ROLE`
     Predefined role to assign to principal (admin, edit, view). `ROLE` must be one of: `admin`, `edit`, `view`. 
At most one of these can be specified: 

`--group`=`GROUP`
     Group for the RBACRoleBinding to update to. 
`--user`=`USER`
     User for the RBACRoleBinding to update to. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha container hub scopes rbacrolebindings update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/hub/scopes/rbacrolebindings/update)
    
    
    [gcloud beta container hub scopes rbacrolebindings update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/scopes/rbacrolebindings/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
