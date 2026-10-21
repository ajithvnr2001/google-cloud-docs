---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/redis/acl-policies/create/
title: gcloud alpha redis acl-policies create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:35:14.586683+00:00
---

# gcloud alpha redis acl-policies create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/redis/acl-policies/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha redis acl-policies create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha redis acl-policies create - create a Redis ACL Policy 
SYNOPSIS
    

`gcloud alpha redis acl-policies create` (`ACL_POLICY` : `--region`=`REGION`) `--rules`=[`rule`=`RULE`],[`username`=`USERNAME`] [`--request-id`=`REQUEST_ID`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a Redis ACL Policy with the specified rules. 
EXAMPLES
     To create an ACL Policy named `my-acl-policy` in region `us-east1` with two rules, run: 
    
    
    gcloud alpha redis acl-policies create my-acl-policy --region=us-east1 --rules="username=user1,rule='on ~keys:* +get'" --rules="username=user2,rule='off ~* -@all'"

POSITIONAL ARGUMENTS
    

Acl policy resource - The ACL Policy to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `acl_policy` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`ACL_POLICY`
     ID of the acl policy or fully qualified identifier for the acl policy. 

To set the `acl_policy` attribute: 

  * provide the argument `acl_policy` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     The name of the Redis region of the acl policy. Overrides the default redis/region property value for this command invocation. To set the `region` attribute: 

  * provide the argument `acl_policy` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line; 
  * set the property `redis/region`. 


REQUIRED FLAGS
    

`--rules`=[`rule`=`RULE`],[`username`=`USERNAME`]
     Required, The ACL rules within the ACL policy. Specify this flag multiple times for multiple rules. Each rule consists of 'username' and 'rule'. 

`rule`
     The Redis ACL rule string. 
`username`
     The username for the ACL rule. 
`Shorthand Example:`
    
    
    --rules=rule=string,username=string --rules=rule=string,username=string

`JSON Example:`
    
    
    --rules='[{"rule": "string", "username": "string"}]'

`File Example:`
    
    
    --rules=path_to_file.(yaml|json)

OPTIONAL FLAGS
    

`--request-id`=`REQUEST_ID`
     Idempotent request UUID. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `redis/v1alpha1` API. The full documentation for this API can be found at: <https://cloud.google.com/memorystore/docs/redis/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud redis acl-policies create](https://docs.cloud.google.com/sdk/gcloud/reference/redis/acl-policies/create)
    
    
    [gcloud beta redis acl-policies create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/redis/acl-policies/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
