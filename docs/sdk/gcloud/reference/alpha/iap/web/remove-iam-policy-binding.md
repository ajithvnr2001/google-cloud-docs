---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iap/web/remove-iam-policy-binding/
title: gcloud alpha iap web remove-iam-policy-binding \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:40:20.834159+00:00
---

# gcloud alpha iap web remove-iam-policy-binding  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iap/web/remove-iam-policy-binding/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha iap web remove-iam-policy-binding Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha iap web remove-iam-policy-binding - remove IAM policy binding from an IAP IAM resource 
SYNOPSIS
    

`gcloud alpha iap web remove-iam-policy-binding` `--member`=`PRINCIPAL` `--role`=`ROLE` [`--all` | `--condition`=[`KEY`=`VALUE`,…] | `--condition-from-file`=`PATH_TO_FILE`] [`--instance`=`INSTANCE` `--region`=`REGION` `--resource-type`=`RESOURCE_TYPE` `--service`=`SERVICE` `--version`=`VERSION` `--agent`=`AGENT` | `--endpoint`=`ENDPOINT` | `--mcp-server`=`MCP_SERVER`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Removes a policy binding from the IAM policy of an IAP IAM resource. One binding consists of a member, a role and an optional condition. See $ [gcloud alpha iap web get-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iap/web/get-iam-policy) for examples of how to specify an IAP IAM resource. 
EXAMPLES
     See $ [gcloud alpha iap web get-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iap/web/get-iam-policy) for examples of how to specify an IAP IAM resource. 

To remove an IAM policy binding for the role of 'roles/editor' for the user 'test-user@gmail.com' on IAP IAM resource IAP_IAM_RESOURCE, run: 
    
    
    gcloud alpha iap web remove-iam-policy-binding --resource-type=IAP_IAM_RESOURCE --member='user:test-user@gmail.com' --role='roles/editor'

To remove an IAM policy binding for the role of 'roles/editor' for the user 'test-user@gmail.com' on regional IAP IAM resource IAP_IAM_RESOURCE, run: 
    
    
    gcloud alpha iap web remove-iam-policy-binding --resource-type=IAP_IAM_RESOURCE --member='user:test-user@gmail.com' --role='roles/editor' --region=REGION

To remove an IAM policy binding for the role of 'roles/editor' from all authenticated users on IAP IAM resource IAP_IAM_RESOURCE,run: 
    
    
    gcloud alpha iap web remove-iam-policy-binding --resource-type=IAP_IAM_RESOURCE --member='allAuthenticatedUsers' --role='roles/editor'

To remove an IAM policy binding with a condition of expression='request.time < timestamp("2019-01-01T00:00:00Z")', title='expires_end_of_2018', and description='Expires at midnight on 2018-12-31' for the role of 'roles/browser' for the user 'test-user@gmail.com' on IAP IAM resource IAP_IAM_RESOURCE, run: 
    
    
    gcloud alpha iap web remove-iam-policy-binding --resource-type=IAP_IAM_RESOURCE --member='user:test-user@gmail.com' --role='roles/browser' --condition='expression=request.time <
        timestamp("2019-01-01T00:00:00Z"),title=expires_end_of_2018,
        description=Expires at midnight on 2018-12-31'

To remove all IAM policy bindings regardless of the condition for the role of 'roles/browser' and for the user 'test-user@gmail.com' on IAP IAM resource IAP_IAM_RESOURCE, run: 
    
    
    gcloud alpha iap web remove-iam-policy-binding --resource-type=IAP_IAM_RESOURCE --member='user:test-user@gmail.com' --role='roles/browser' --all

See <https://cloud.google.com/iam/docs/managing-policies> for details of policy role and member types. 

REQUIRED FLAGS
    

`--member`=`PRINCIPAL`
     The principal to remove the binding for. Should be of the form `user|group|serviceAccount:email` or `domain:domain`. 

Examples: `user:test-user@gmail.com`, `group:admins@example.com`, `serviceAccount:test123@example.domain.com`, or `domain:example.domain.com`. 

Deleted principals have an additional `deleted:` prefix and a `?uid=UID` suffix, where ``UID`` is a unique identifier for the principal. Example: `deleted:user:test-user@gmail.com?uid=123456789012345678901`. 

Some resources also accept the following special values: 

  * `allUsers` \- Special identifier that represents anyone who is on the internet, with or without a Google account. 
  * `allAuthenticatedUsers` \- Special identifier that represents anyone who is authenticated with a Google account or a service account. 


`--role`=`ROLE`
     The role to remove the principal from. 
OPTIONAL FLAGS
    

At most one of these can be specified: 

`--all`
     Remove all bindings with this role and principal, irrespective of any conditions. 
`--condition`=[`KEY`=`VALUE`,…]
     The condition of the binding that you want to remove. When the condition is explicitly specified as `None` (`--condition=None`), a binding without a condition is removed. Otherwise, only a binding with a condition that exactly matches the specified condition (including the optional description) is removed. For more on conditions, refer to the conditions overview guide: <https://cloud.google.com/iam/docs/conditions-overview>

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
`--instance`=`INSTANCE`
     Instance ID. 
`--region`=`REGION`
     Region name. Not applicable for `resource-type=app-engine`. Required when `resource-type=backend-services` and regional scoped. Not applicable for global backend-services. Required when `resource-type=cloud-run`. 
`--resource-type`=`RESOURCE_TYPE`
     Resource type of the IAP resource. `RESOURCE_TYPE` must be one of: `app-engine`, `backend-services`, `forwarding-rule`, `cloud-run`, `agent-registry`. 
`--service`=`SERVICE`
     Service name. 
`--version`=`VERSION`
     Service version. Should only be specified with `--resource-type=app-engine`. 
At most one of these can be specified: 

`--agent`=`AGENT`
     Agent ID for the agent-registry resource type. 
`--endpoint`=`ENDPOINT`
     Endpoint ID for the agent-registry resource type. 
`--mcp-server`=`MCP_SERVER`
     MCP server ID for the agent-registry resource type. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud iap web remove-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/iap/web/remove-iam-policy-binding)
    
    
    [gcloud beta iap web remove-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/beta/iap/web/remove-iam-policy-binding)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
