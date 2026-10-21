---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/hub/scopes/remove-app-operator-binding/
title: gcloud alpha container hub scopes remove-app-operator-binding \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:47:58.367260+00:00
---

# gcloud alpha container hub scopes remove-app-operator-binding  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/hub/scopes/remove-app-operator-binding/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha container hub scopes remove-app-operator-binding Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha container hub scopes remove-app-operator-binding - remove project-level and fleet scope-level IAM bindings and delete a fleet scope RBAC role binding for an app operator principal 
SYNOPSIS
    

`gcloud alpha container hub scopes remove-app-operator-binding` `SCOPE` (`--group`=`GROUP` | `--user`=`USER`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` One binding consists of an app operator principal (user/group) and a role (view/edit/admin). 

This command unsets the different permissions required for an app operator, including usage of fleet scopes, connect gateway, logging, and metrics. The authoritative list for removing the permissions is the existing RBAC role bindings under the specified scope. 

This command can fail for the following reasons: 

  * The scope specified does not exist. 
  * The user does not have access to the specified scope. 
  * The principal specified does not any binding for the scope. 
  * The principal specified has bindings with different roles for the scope. 


EXAMPLES
     The following command: 
    
    
    gcloud alpha container hub scopes remove-app-operator-binding SCOPE --group=people@google.com --project=PROJECT_ID

assuming the group already has the `view` role: 

  * removes IAM policy binding: roles/gkehub.scopeViewer from `SCOPE`
  * removes IAM policy binding: roles/gkehub.scopeViewerProjectLevel from `PROJECT_ID` if the group does not have the `view` role for any other scope under the project 
  * removes IAM policy binding: roles/logging.viewAccessor from `PROJECT_ID` condition where bucket corresponds to `SCOPE`
  * deletes existing fleet scope RBAC role binding: role `view` for group `people@google.com`. 



\--- 

The following command: 
    
    
    gcloud alpha container hub scopes remove-app-operator-binding SCOPE --user=person@google.com --project=PROJECT_ID

assuming the user already has the `edit` role: 

  * removes IAM policy binding: roles/gkehub.scopeEditor from `SCOPE`
  * removes IAM policy binding: roles/gkehub.scopeEditorProjectLevel from `PROJECT_ID` if the user does not have the `edit`/`admin` role for any other scope under the project 
  * removes IAM policy binding: roles/logging.viewAccessor from `PROJECT_ID` condition where bucket corresponds to `SCOPE`
  * deletes existing fleet scope RBAC role binding: role `edit` for user `person@google.com`. 



\--- 

The following command: 
    
    
    gcloud alpha container hub scopes remove-app-operator-binding SCOPE --user=person@google.com --project=PROJECT_ID

assuming the user already has a custom role: 

  * removes IAM policy binding: roles/gkehub.scopeViewer from `SCOPE`
  * removes IAM policy binding: roles/gkehub.scopeEditorProjectLevel from `PROJECT_ID` if the user does not have the `edit`/`admin` role for any other scope under the project 
  * removes IAM policy binding: roles/logging.viewAccessor from `PROJECT_ID` condition where bucket corresponds to `SCOPE`
  * deletes existing fleet scope RBAC role binding: role `admin` for user `person@google.com`. 



\--- 

The following command: 
    
    
    gcloud alpha container hub scopes remove-app-operator-binding SCOPE --user=person@google.com --project=PROJECT_ID

assuming the user already has the `admin` role: 

  * removes IAM policy binding: roles/gkehub.scopeAdmin from `SCOPE`
  * removes IAM policy binding: roles/gkehub.scopeEditorProjectLevel from `PROJECT_ID` if the user does not have the `edit`/`admin` role for any other scope under the project 
  * removes IAM policy binding: roles/logging.viewAccessor from `PROJECT_ID` condition where bucket corresponds to `SCOPE`
  * deletes existing fleet scope RBAC role binding: role `admin` for user `person@google.com`. 


POSITIONAL ARGUMENTS
    

Scope resource - The group of arguments defining the Fleet Scope. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `SCOPE` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `SCOPE` on the command line with a fully specified name; 
  * global is the only supported location. 



This must be specified. 

`SCOPE`
     ID of the scope or fully qualified identifier for the scope. 

To set the `scope` attribute: 

  * provide the argument `SCOPE` on the command line. 


REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--group`=`GROUP`
     Group for the role binding. 
`--user`=`USER`
     User for the role binding. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud beta container hub scopes remove-app-operator-binding](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/scopes/remove-app-operator-binding)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
