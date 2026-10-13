---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/sources/describe/
title: gcloud alpha scc sources describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:04:23.781143+00:00
---

# gcloud alpha scc sources describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/sources/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha scc sources describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha scc sources describe - describe a source given its display name or source id 
SYNOPSIS
    

`gcloud alpha scc sources describe` [`PARENT`] (`--source`=`SOURCE` | `--source-display-name`=`SOURCE_DISPLAY_NAME`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Describe a source given its display name or source id. 
EXAMPLES
     Describe source with display name `Security Scanner`: 
    
    
    gcloud alpha scc sources describe 123456 --source-display-name="Security Scanner"

Describe source with source id '5678': 
    
    
    gcloud alpha scc sources describe 123456 --source=5678

POSITIONAL ARGUMENTS
    

Parent resource - parent organization, folder, or project in the Google Cloud resource hierarchy to be used for the `[gcloud scc](https://docs.cloud.google.com/sdk/gcloud/reference/scc)` command. Specify the argument as either [RESOURCE_TYPE/RESOURCE_ID] or [RESOURCE_ID], as shown in the preceding examples. This represents a Cloud resource. 
[`PARENT`]
     ID of the parent or fully qualified identifier for the parent. 

To set the `parent` attribute: 

  * provide the argument `parent` on the command line; 
  * Set the parent property in configuration using `gcloud config set scc/parent` if it is not specified in command line. 


REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--source`=`SOURCE`
     Cloud SCC specific source. It's derived from the the source's relative resource name. See: <https://cloud.google.com/apis/design/resource_names#relative_resource_name>. For Example: For the given source name: "organizations/123/sources/456", 456 represents source id. 
`--source-display-name`=`SOURCE_DISPLAY_NAME`
     Source's display name must be unique amongst its siblings, for example, two sources with the same parent can't share the same display name. Display name must start and end with a letter or digit, may contain letters, digits, spaces, hyphens, and underscores, and can be no longer than 32 characters. This is captured by the regular expression: [\p{L}\p{N}]({\p{L}\p{N}`- ]{0,30}[\p{L}\p{N}])?. For example: 'Cloud Security Scanner' is the source display name. `
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `securitycenter/v2` API. The full documentation for this API can be found at: <https://cloud.google.com/security-command-center>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud scc sources describe](https://docs.cloud.google.com/sdk/gcloud/reference/scc/sources/describe)
    
    
    [gcloud beta scc sources describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/scc/sources/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
