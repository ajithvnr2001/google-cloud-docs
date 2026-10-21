---
url: https://docs.cloud.google.com/sdk/gcloud/reference/scc/assets/describe/
title: gcloud scc assets describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:30:56.817381+00:00
---

# gcloud scc assets describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/scc/assets/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud scc assets describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud scc assets describe - describe an asset given its resource name or asset id 
SYNOPSIS
    

`gcloud scc assets describe` [`PARENT`] (`--asset`=`ASSET` | `--resource-name`=`RESOURCE_NAME`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(DEPRECATED)` Security Command Center Asset APIs are deprecated and will be removed on or after June 26, 2024. Use Cloud Asset Inventory instead [(gcloud asset)](https://cloud.google.com/sdk/gcloud/reference/asset). For more information, [see the deprecation notice at Assets Page](https://cloud.google.com/security-command-center/docs/how-to-use-security-command-center#assets_page). Describe an asset given its resource name or asset id. 
EXAMPLES
     Describe an asset under organization 123456, given its full resource name (https://cloud.google.com/apis/design/resource_names#full_resource_name) e.g. //storage.googleapis.com/my-bucket: 
    
    
    gcloud scc assets describe 123456 --resource-name="//storage.googleapis.com/my-bucket"

Describe an asset under organization 123456, given its Cloud SCC asset id 5678 
    
    
    gcloud scc assets describe 123456 --asset=5678

Describe an asset under project example-project, given its Cloud SCC asset id 5678 
    
    
    gcloud scc assets describe projects/example-project/assets/5678

Describe an asset under folder 456, given its Cloud SCC asset id 5678 
    
    
    gcloud scc assets describe folders/456/assets/5678

POSITIONAL ARGUMENTS
    

Parent resource - parent organization, folder, or project in the Google Cloud resource hierarchy to be used for the `[gcloud scc](https://docs.cloud.google.com/sdk/gcloud/reference/scc)` command. Specify the argument as either [RESOURCE_TYPE/RESOURCE_ID] or [RESOURCE_ID], as shown in the preceding examples. This represents a Cloud resource. 
[`PARENT`]
     ID of the parent or fully qualified identifier for the parent. 

To set the `parent` attribute: 

  * provide the argument `parent` on the command line; 
  * Set the parent property in configuration using `gcloud config set scc/parent` if it is not specified in command line. 


REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--asset`=`ASSET`
     Cloud SCC specific asset. It's derived from the the asset's relative resource name. See: <https://cloud.google.com/apis/design/resource_names#relative_resource_name>. For Example, for the given asset name: "organizations/123/assets/456", 456 represents asset id. 
`--resource-name`=`RESOURCE_NAME`
     Asset's resource name. Full resource name of the Google Cloud Platform resource this asset represents. This field is immutable after create time. See: <https://cloud.google.com/apis/design/resource_names#full_resource_name>. For Example: "//cloudresourcemanager.googleapis.com/projects/1234567890123" could be the resource-name for a project. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `securitycenter/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/security-command-center>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha scc assets describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/assets/describe)
    
    
    [gcloud beta scc assets describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/scc/assets/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
