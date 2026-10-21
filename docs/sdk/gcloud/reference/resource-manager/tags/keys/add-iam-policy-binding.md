---
url: https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/keys/add-iam-policy-binding/
title: gcloud resource-manager tags keys add-iam-policy-binding \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:11:50.130337+00:00
---

# gcloud resource-manager tags keys add-iam-policy-binding  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/keys/add-iam-policy-binding/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud resource-manager tags keys add-iam-policy-binding Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud resource-manager tags keys add-iam-policy-binding - adds a policy binding to the IAM policy of a TagKey 
SYNOPSIS
    

`gcloud resource-manager tags keys add-iam-policy-binding` `RESOURCE_NAME` `--member`=`PRINCIPAL` `--role`=`ROLE` [`--condition`=[`KEY`=`VALUE`,…] | `--condition-from-file`=`PATH_TO_FILE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Adds the IAM policy binding for a TagKey resource given the binding and an identifier for the TagKey. The identifier can be the TagKey's parent/short name or the TagKey's ID in the form: tagKeys/{numeric_id}. 
EXAMPLES
     To add an IAM policy binding for the role of 'roles/editor' for the user 'test-user@gmail.com' on the Tag Key 'tagKeys/123', run: 
    
    
    gcloud resource-manager tags keys add-iam-policy-binding tagKeys/123 --member='user:test-user@gmail.com' --role='roles/editor'

To add an IAM policy binding for a Tag Key with the name 'env' under 'organization/456' for the role of 'roles/resourcemanager.tagUser' for the user 'test-user@gmail.com', run: 
    
    
    gcloud resource-manager tags keys add-iam-policy-binding 456/env --member='user:test-user@gmail.com' --role='roles/resourcemanager.tagUser'

See <https://cloud.google.com/iam/docs/managing-policies> for details of policy role and member types. 

POSITIONAL ARGUMENTS
    

`RESOURCE_NAME`
     Resource name or namespaced name. The resource name should be in the form {resource_type}/{numeric_id}. The namespaced name should be in the form {org_id}/{short_name} where short_name must be 1-63 characters, beginning and ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores ( _ ), dots (.), and alphanumerics between. 
REQUIRED FLAGS
    

`--member`=`PRINCIPAL`
     The principal to add the binding for. Should be of the form `user|group|serviceAccount:email` or `domain:domain`. 

Examples: `user:test-user@gmail.com`, `group:admins@example.com`, `serviceAccount:test123@example.domain.com`, or `domain:example.domain.com`. 

Some resources also accept the following special values: 

  * `allUsers` \- Special identifier that represents anyone who is on the internet, with or without a Google account. 
  * `allAuthenticatedUsers` \- Special identifier that represents anyone who is authenticated with a Google account or a service account. 


`--role`=`ROLE`
     Role name to assign to the principal. The role name is the complete path of a predefined role, such as `roles/logging.viewer`, or the role ID for a custom role, such as `organizations/{ORGANIZATION_ID}/roles/logging.viewer`. 
OPTIONAL FLAGS
    

At most one of these can be specified: 

`--condition`=[`KEY`=`VALUE`,…]
     A condition to include in the binding. When the condition is explicitly specified as `None` (`--condition=None`), a binding without a condition is added. When the condition is specified and is not `None`, `--role` cannot be a basic role. Basic roles are `roles/editor`, `roles/owner`, and `roles/viewer`. For more on conditions, refer to the conditions overview guide: <https://cloud.google.com/iam/docs/conditions-overview>

When using the `--condition` flag, include the following key-value pairs: 

`expression`
     (Required) Condition expression that evaluates to True or False. This uses a subset of Common Expression Language syntax. 

If the condition expression includes a comma, use a different delimiter to separate the key-value pairs. Specify the delimiter before listing the key-value pairs. For example, to specify a colon (`:`) as the delimiter, do the following: `--condition=^:^title=TITLE:expression=EXPRESSION`. For more information, see <https://cloud.google.com/sdk/gcloud/reference/topic/escaping>. 

`title`
     (Required) A short string describing the purpose of the expression. 
`description`
     (Optional) Additional description for the expression. 
`--condition-from-file`=`PATH_TO_FILE`
     Path to a local JSON or YAML file that defines the condition. To see available fields, see the help for `--condition`. Use a full or relative path to a local file containing the value of condition. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha resource-manager tags keys add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/resource-manager/tags/keys/add-iam-policy-binding)
    
    
    [gcloud beta resource-manager tags keys add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/beta/resource-manager/tags/keys/add-iam-policy-binding)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
