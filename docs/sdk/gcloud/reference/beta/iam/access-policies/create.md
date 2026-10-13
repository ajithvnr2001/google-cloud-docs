---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/access-policies/create/
title: gcloud beta iam access-policies create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:44:33.405169+00:00
---

# gcloud beta iam access-policies create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/access-policies/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta iam access-policies create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta iam access-policies create - create AccessPolicy instance 
SYNOPSIS
    

`gcloud beta iam access-policies create` (`ACCESS_POLICY` : `--folder`=`FOLDER` `--location`=`LOCATION` `--organization`=`ORGANIZATION`) [`--annotations`=[`ANNOTATIONS`,…]] [`--async`] [`--details-rules`=[`conditions`=`CONDITIONS`],[`description`=`DESCRIPTION`],[`effect`=`EFFECT`],[`excludedPrincipals`=`EXCLUDEDPRINCIPALS`],[`operation`=`OPERATION`],[`principals`=`PRINCIPALS`]] [`--display-name`=`DISPLAY_NAME`] [`--etag`=`ETAG`] [`--validate-only`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create AccessPolicy instance. 
EXAMPLES
     To create a policy instance called `my-policy`, run: 
    
    
    gcloud beta iam access-policies create my-policy --organization=123 --location=global --details-rules=rule1.json

POSITIONAL ARGUMENTS
    

AccessPolicy resource - Identifier. The resource name of the access policy. 

The following formats are supported: 

  * `projects/{project_id}/locations/{location}/accessPolicies/{policy_id}`
  * `projects/{project_number}/locations/{location}/accessPolicies/{policy_id}`
  * `folders/{folder_id}/locations/{location}/accessPolicies/{policy_id}`
  * `organizations/{organization_id}/locations/{location}/accessPolicies/{policy_id}` The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 



To set the `project` attribute: 

  * provide the argument `access_policy` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. This resource can be one of the following types: [iam.folders.locations.accessPolicies, iam.organizations.locations.accessPolicies, iam.projects.locations.accessPolicies]. 



This must be specified. 

`ACCESS_POLICY`
     ID of the accessPolicy or fully qualified identifier for the accessPolicy. 

To set the `access_policy` attribute: 

  * provide the argument `access_policy` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--folder`=`FOLDER`
     The folder id of the accessPolicy resource. 

To set the `folder` attribute: 

  * provide the argument `access_policy` on the command line with a fully specified name; 
  * provide the argument `--folder` on the command line. Must be specified for resource of type [iam.folders.locations.accessPolicies]. 


`--location`=`LOCATION`
     The location id of the accessPolicy resource. 

To set the `location` attribute: 

  * provide the argument `access_policy` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--organization`=`ORGANIZATION`
     The organization id of the accessPolicy resource. 

To set the `organization` attribute: 

  * provide the argument `access_policy` on the command line with a fully specified name; 
  * provide the argument `--organization` on the command line. Must be specified for resource of type [iam.organizations.locations.accessPolicies]. 


FLAGS
    

`--annotations`=[`ANNOTATIONS`,…]
     User defined annotations. See <https://google.aip.dev/148#annotations> for more details such as format and size limitations. 

`KEY`
     Sets `KEY` value. 
`VALUE`
     Sets `VALUE` value. 
`Shorthand Example:`
    
    
    --annotations=string=string

`JSON Example:`
    
    
    --annotations='{"string": "string"}'

`File Example:`
    
    
    --annotations=path_to_file.(yaml|json)

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
Access policy details. 
`--details-rules`=[`conditions`=`CONDITIONS`],[`description`=`DESCRIPTION`],[`effect`=`EFFECT`],[`excludedPrincipals`=`EXCLUDEDPRINCIPALS`],[`operation`=`OPERATION`],[`principals`=`PRINCIPALS`]
     Required, A list of access policy rules. 

`conditions`
     The conditions that determine whether this rule applies to a request. Conditions are identified by their key, which is the FQDN of the service that they are relevant to. For example: `"conditions": { "iam.googleapis.com": { "expression": <cel expression> } }`. Each rule is evaluated independently. If this rule does not apply to a request, other rules might still apply. Currently supported keys are as follows: 

  * `eventarc.googleapis.com`: Can use `CEL` functions that evaluate resource fields. 


  * `iam.googleapis.com`: Can use `CEL` functions that evaluate [resource tags](https://cloud.google.com/iam/help/conditions/resource-tags) and combine them using boolean and logical operators. Other functions and operators are not supported. 



`KEY`
     Sets `KEY` value. 
`VALUE`
     Sets `VALUE` value. 

`description`
     Description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI. 
`expression`
     Textual representation of an expression in Common Expression Language syntax. 
`location`
     String indicating the location of the expression for error reporting, e.g. a file name and a position in the file. 
`title`
     Title for the expression, i.e. a short string describing its purpose. This can be used e.g. in UIs which allow to enter the expression. 
`description`
     Customer specified description of the rule. Must be less than or equal to 256 characters. 
`effect`
     The effect of the rule. 
`excludedPrincipals`
     The identities that are excluded from the access policy rule, even if they are listed in the `principals`. For example, you could add a Google group to the `principals`, then exclude specific users who belong to that group. 
`operation`
     Attributes that are used to determine whether this rule applies to a request. 

`excludedPermissions`
     Specifies the permissions that this rule excludes from the set of affected permissions given by `permissions`. If a permission appears in `permissions` `and` in `excluded_permissions` then it will `not` be subject to the policy effect. 

The excluded permissions can be specified using the same syntax as `permissions`. 

`permissions`
     The permissions that are explicitly affected by this rule. Each permission uses the format `{service_fqdn}/{resource}.{verb}`, where `{service_fqdn}` is the fully qualified domain name for the service. Currently supported permissions are as follows: 

  * `eventarc.googleapis.com/messageBuses.publish`. 


`principals`
     The identities for which this rule's effect governs using one or more permissions on Google Cloud resources. This field can contain the following values: 

  * `principal://goog/subject/{email_id}`: A specific Google Account. Includes Gmail, Cloud Identity, and Google Workspace user accounts. For example, `principal://goog/subject/alice@example.com`. 

If an identifier that was previously set on a policy is soft deleted, then calls to read that policy will return the identifier with a deleted prefix. Users cannot set identifiers with this syntax. 
  * `deleted:principal://goog/subject/{email_id}?uid={uid}`: A specific Google Account that was deleted recently. For example, `deleted:principal://goog/subject/alice@example.com?uid=1234567890`. If the Google Account is recovered, this identifier reverts to the standard identifier for a Google Account. 


  * `deleted:principalSet://goog/group/{group_id}?uid={uid}`: A Google group that was deleted recently. For example, `deleted:principalSet://goog/group/admins@example.com?uid=1234567890`. If the Google group is restored, this identifier reverts to the standard identifier for a Google group. 


  * `deleted:principal://iam.googleapis.com/projects/-/serviceAccounts/{service_account_id}?uid={uid}`: A Google Cloud service account that was deleted recently. For example, `deleted:principal://iam.googleapis.com/projects/-/serviceAccounts/my-service-account@iam.gserviceaccount.com?uid=1234567890`. If the service account is undeleted, this identifier reverts to the standard identifier for a service account. 


`Shorthand Example:`
    
    
    --details-rules=conditions={string={description=string,expression=string,location=string,title=string}},description=string,effect=string,excludedPrincipals=[string],operation={excludedPermissions=[string],permissions=[string]},principals=[string] --details-rules=conditions={string={description=string,expression=string,location=string,title=string}},description=string,effect=string,excludedPrincipals=[string],operation={excludedPermissions=[string],permissions=[string]},principals=[string]

`JSON Example:`
    
    
    --details-rules='[{"conditions": {"string": {"description": "string", "expression": "string", "location": "string", "title": "string"}}, "description": "string", "effect": "string", "excludedPrincipals": ["string"], "operation": {"excludedPermissions": ["string"], "permissions": ["string"]}, "principals": ["string"]}]'

`File Example:`
    
    
    --details-rules=path_to_file.(yaml|json)

`--display-name`=`DISPLAY_NAME`
     The description of the access policy. Must be less than or equal to 63 characters. 
`--etag`=`ETAG`
     The etag for the access policy. If this is provided on update, it must match the server's etag. 
`--validate-only`
     If set, validate the request and preview the creation, but do not actually post it. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `iam/v3beta` API. The full documentation for this API can be found at: <https://cloud.google.com/iam/>
NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud iam access-policies create](https://docs.cloud.google.com/sdk/gcloud/reference/iam/access-policies/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
