---
url: https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/scopes/rbacrolebindings/create/
title: gcloud container hub scopes rbacrolebindings create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:39:40.330491+00:00
---

# gcloud container hub scopes rbacrolebindings create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/scopes/rbacrolebindings/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud container hub scopes rbacrolebindings create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud container hub scopes rbacrolebindings create - create an RBAC RoleBinding 
SYNOPSIS
    

`gcloud container hub scopes rbacrolebindings create` (`NAME` : `--location`=`LOCATION` `--scope`=`SCOPE`) (`--custom-role`=`CUSTOM_ROLE` | `--role`=`ROLE`) (`--group`=`GROUP` | `--user`=`USER`) [`--labels`=[`KEY`=`VALUE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     This command can fail for the following reasons: 

  * The RBAC RoleBinding already exists. 
  * The caller does not have permission to access the given scope. 


EXAMPLES
     To create an admin RBAC RoleBinding `RBRB` in scope `SCOPE` for user `person@google.com`, run: 
    
    
    gcloud container hub scopes rbacrolebindings create RBRB --scope=SCOPE --role=admin --user=person@google.com

To create a viewer RBAC RoleBinding `RBRB` in scope `SCOPE` for group `people@google.com`, run: 
    
    
    gcloud container hub scopes rbacrolebindings create RBRB --scope=SCOPE --role=viewer --group=people@google.com

To create an RBAC RoleBinding with a custom role `custom-role` in scope `SCOPE` for user `person@google.com`, run: 
    
    
    gcloud container hub scopes rbacrolebindings create RBRB --scope=SCOPE --role=admin --user=person@google.com --custom-role=custom-role

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


REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--custom-role`=`CUSTOM_ROLE`
     Custom role to assign to principal. 
`--role`=`ROLE`
     Predefined role to assign to principal (admin, edit, view). `ROLE` must be one of: `admin`, `edit`, `view`. 
Exactly one of these must be specified: 

`--group`=`GROUP`
     Group for the RoleBinding. 
`--user`=`USER`
     User for the RoleBinding. 
OPTIONAL FLAGS
    

`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha container hub scopes rbacrolebindings create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/hub/scopes/rbacrolebindings/create)
    
    
    [gcloud beta container hub scopes rbacrolebindings create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/scopes/rbacrolebindings/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
