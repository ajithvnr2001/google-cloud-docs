---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/memorystore/acl-policies/update/
title: gcloud alpha memorystore acl-policies update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:00:28.832417+00:00
---

# gcloud alpha memorystore acl-policies update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/memorystore/acl-policies/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha memorystore acl-policies update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha memorystore acl-policies update - update aclPolicies 
SYNOPSIS
    

`gcloud alpha memorystore acl-policies update` (`ACL_POLICY` : `--location`=`LOCATION`) [`--async`] [`--request-id`=`REQUEST_ID`] [`--rules`=[`rule`=`RULE`],[`username`=`USERNAME`] | `--add-rules`=[`rule`=`RULE`],[`username`=`USERNAME`] `--clear-rules` | `--remove-rules`=[`rule`=`RULE`],[`username`=`USERNAME`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Update an aclPolicy 
EXAMPLES
     To update the aclPolicy, run: 
    
    
    gcloud alpha memorystore acl-policies update

POSITIONAL ARGUMENTS
    

AclPolicy resource - Identifier. Full resource path of the ACL policy. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `acl_policy` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`ACL_POLICY`
     ID of the aclPolicy or fully qualified identifier for the aclPolicy. 

To set the `acl_policy` attribute: 

  * provide the argument `acl_policy` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location id of the aclPolicy resource. 

To set the `location` attribute: 

  * provide the argument `acl_policy` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--request-id`=`REQUEST_ID`
     Idempotent request UUID. 
Update rules. 

At most one of these can be specified: 

`--rules`=[`rule`=`RULE`],[`username`=`USERNAME`]
     Set rules to new value. The ACL rules within the ACL policy. 

`rule`
     The rule to be applied to the username. Ex: "on >password123 ~` +@all" The format of the rule is defined by Valkey OSS: <https://valkey.io/topics/acl/>. `
username``
     Specifies the IAM user or service account to be added to the ACL policy. This username will be directly set on the Valkey OSS. 
Shorthand Example:`
    
    
    --rules=rule=string,username=string --rules=rule=string,username=string

`JSON Example:`
    
    
    --rules='[{"rule": "string", "username": "string"}]'

`File Example:`
    
    
    --rules=path_to_file.(yaml|json)

`
Or at least one of these can be specified: 

\--add-rules`=[`rule`=`RULE`],[`username`=`USERNAME`]`
     Add new value to rules list. The ACL rules within the ACL policy. 

rule``
     The rule to be applied to the username. Ex: "on >password123 ~ +@all" The format of the rule is defined by Valkey OSS: <https://valkey.io/topics/acl/>. 
`username`
     Specifies the IAM user or service account to be added to the ACL policy. This username will be directly set on the Valkey OSS. 
`Shorthand Example:`
    
    
    --add-rules=rule=string,username=string --add-rules=rule=string,username=string

`JSON Example:`
    
    
    --add-rules='[{"rule": "string", "username": "string"}]'

`File Example:`
    
    
    --add-rules=path_to_file.(yaml|json)

At most one of these can be specified: 

`--clear-rules`
     Clear rules value and set to empty list. 
`--remove-rules`=[`rule`=`RULE`],[`username`=`USERNAME`]
     Remove existing value from rules list. The ACL rules within the ACL policy. 

`rule`
     The rule to be applied to the username. Ex: "on >password123 ~` +@all" The format of the rule is defined by Valkey OSS: <https://valkey.io/topics/acl/>. `
username``
     Specifies the IAM user or service account to be added to the ACL policy. This username will be directly set on the Valkey OSS. 
Shorthand Example:`
    
    
    --remove-rules=rule=string,username=string --remove-rules=rule=string,username=string

`JSON Example:`
    
    
    --remove-rules='[{"rule": "string", "username": "string"}]'

`File Example:`
    
    
    --remove-rules=path_to_file.(yaml|json)

`
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `memorystore/v1alpha` API. The full documentation for this API can be found at: <https://cloud.google.com/memorystore/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud memorystore acl-policies update](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/acl-policies/update)
    
    
    [gcloud beta memorystore acl-policies update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/memorystore/acl-policies/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-21 UTC."],[],[]] 
