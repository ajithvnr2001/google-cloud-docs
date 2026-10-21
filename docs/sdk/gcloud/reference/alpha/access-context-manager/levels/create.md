---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/levels/create/
title: gcloud alpha access-context-manager levels create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:59:05.877060+00:00
---

# gcloud alpha access-context-manager levels create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/levels/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha access-context-manager levels create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha access-context-manager levels create - create a new access level 
SYNOPSIS
    

`gcloud alpha access-context-manager levels create` (`LEVEL` : `--policy`=`POLICY`) `--title`=`TITLE` (`--custom-level-spec`=`CUSTOM_LEVEL_SPEC` | [`--basic-level-spec`=`BASIC_LEVEL_SPEC` : `--combine-function`=`COMBINE_FUNCTION`; default="and"]) [`--async`] [`--description`=`DESCRIPTION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a new access level in a given access policy. 
POSITIONAL ARGUMENTS
    

Level resource - The access level to create. The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`LEVEL`
     ID of the level or fully qualified identifier for the level. 

To set the `level` attribute: 

  * provide the argument `level` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--policy`=`POLICY`
     The ID of the access policy. To set the `policy` attribute: 

  * provide the argument `level` on the command line with a fully specified name; 
  * provide the argument `--policy` on the command line; 
  * set the property `access_context_manager/policy`; 
  * automatically, if the current account belongs to an organization with exactly one access policy.. 


REQUIRED FLAGS
    

`--title`=`TITLE`
     Short human-readable title of the access level. 
Level specification. 

Exactly one of these must be specified: 

Custom level specification. 
`--custom-level-spec`=`CUSTOM_LEVEL_SPEC`
     Path to a file representing an expression that represents an access level. 

The expression is in the Common Expression Language (CEL) format. For example: 
    
    
      expression: "origin.region_code in ['US', 'CA']"

Basic level specification. 
`--basic-level-spec`=`BASIC_LEVEL_SPEC`
     Path to a file containing a list of basic access level conditions. 

An access level condition file is a YAML-formatted list of conditions, which are YAML objects representing a Condition as described in the API reference. For example: 
    
    
     - ipSubnetworks:
       - 162.222.181.197/24
       - 2001:db8::/48
     - members:
       - user:user@example.com

This flag argument must be specified if any of the other arguments in this group are specified. 

`--combine-function`=`COMBINE_FUNCTION`; default="and"
     For a basic level, determines how conditions are combined. `COMBINE_FUNCTION` must be one of: `and`, `or`. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     Long-form description of access level. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `accesscontextmanager/v1alpha` API. The full documentation for this API can be found at: <https://cloud.google.com/access-context-manager/docs/reference/rest/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud access-context-manager levels create](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/levels/create)
    
    
    [gcloud beta access-context-manager levels create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/levels/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
