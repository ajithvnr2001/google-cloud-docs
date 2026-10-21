---
url: https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/update/
title: gcloud database-migration conversion-workspaces update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:40:51.257894+00:00
---

# gcloud database-migration conversion-workspaces update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud database-migration conversion-workspaces update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud database-migration conversion-workspaces update - update a Database Migration Service conversion workspace 
SYNOPSIS
    

`gcloud database-migration conversion-workspaces update` (`CONVERSION_WORKSPACE` : `--region`=`REGION`) [`--no-async`] [`--[no-]auto-conversion`] [`--[no-]conversion-assistance`] [`--display-name`=`DISPLAY_NAME`] [`--endpoint-mode`=`ENDPOINT_MODE`] [`--global-filter`=`GLOBAL_FILTER`] [`--[no-]pattern-matching`] [`--[no-]quality-assessment`] [`--source-database-name-override`=`SOURCE_DATABASE_NAME_OVERRIDE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update a Database Migration Service conversion workspace. 
EXAMPLES
     To update a conversion workspace: 
    
    
    gcloud database-migration conversion-workspaces update my-conversion-workspace --region=us-central1 --display-name=new-display-name

POSITIONAL ARGUMENTS
    

Conversion workspace resource - The conversion workspace to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `conversion_workspace` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`CONVERSION_WORKSPACE`
     ID of the conversion_workspace or fully qualified identifier for the conversion_workspace. 

To set the `conversion_workspace` attribute: 

  * provide the argument `conversion_workspace` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     The Cloud region for the conversion_workspace. 

To set the `region` attribute: 

  * provide the argument `conversion_workspace` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line. 


FLAGS
    

`--no-async`
     Waits for the operation in progress to complete before returning. 
`--[no-]auto-conversion`
     Whether to enable Gemini auto-conversion. Use `--auto-conversion` to enable and `--no-auto-conversion` to disable. 
`--[no-]conversion-assistance`
     Whether to enable Gemini conversion assistance. Use `--conversion-assistance` to enable and `--no-conversion-assistance` to disable. 
`--display-name`=`DISPLAY_NAME`
     A user-friendly name for the conversion workspace. The display name can include letters, numbers, spaces, and hyphens, and must start with a letter. The maximum length allowed is 60 characters. 
`--endpoint-mode`=`ENDPOINT_MODE`
     Specifies endpoint mode for a given command. Regional endpoints provide enhanced data residency and reliability by ensuring your request is handled entirely within the specified Google Cloud region. This differs from global endpoints, which may process parts of the request outside the target region. Overrides the default `regional/endpoint_mode` property value for this command invocation. `ENDPOINT_MODE` must be one of: 

`global`
     (Default) Use global rather than regional endpoints. 
`regional`
     Only use regional endpoints. An error will be raised if a regional endpoint is not available for a given command. 
`regional-preferred`
     Use regional endpoints when available, otherwise use global endpoints. Recommended for most users. 
`--global-filter`=`GLOBAL_FILTER`
     Filter the source entities based on [AIP-160](https://google.aip.dev/160) standard. This filter will be applied to all subsequent operations on the source entities, such as convert and describe-entities. 
`--[no-]pattern-matching`
     Whether to enable Gemini pattern matching. Use `--pattern-matching` to enable and `--no-pattern-matching` to disable. 
`--[no-]quality-assessment`
     Whether to enable Gemini quality assessment. Use `--quality-assessment` to enable and `--no-quality-assessment` to disable. 
`--source-database-name-override`=`SOURCE_DATABASE_NAME_OVERRIDE`
     The database name to use when seeding from a connection profile. If not specified, the database name from the connection profile is used. Currently only supported for SQL Server source seeding. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

REGIONAL ENDPOINTS
     This command supports regional endpoints. To use regional endpoints for this command, use the `--endpoint-mode=regional-preferred` flag. To use regional endpoints by default, run `$ [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) regional/endpoint_mode regional-preferred`. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-30 UTC."],[],[]] 
