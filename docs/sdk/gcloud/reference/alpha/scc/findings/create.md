---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/findings/create/
title: gcloud alpha scc findings create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:46:14.123672+00:00
---

# gcloud alpha scc findings create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/findings/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha scc findings create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha scc findings create - create a Security Command Center finding 
SYNOPSIS
    

`gcloud alpha scc findings create` (`FINDING` : `--organization`=`ORGANIZATION` `--source`=`SOURCE`) `--category`=`CATEGORY` `--event-time`=`EVENT_TIME` `--resource-name`=`RESOURCE_NAME` [`--external-uri`=`EXTERNAL_URI`] [`--location`=`LOCATION`; default="global"] [`--source-properties`=[`KEY`=`VALUE`,…]] [`--state`=`STATE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a Security Command Center finding. 
EXAMPLES
     Create an ACTIVE finding `testFinding` with category: XSS_SCRIPTING attached to project with project number `9876` under organization `123456` and source `5678`: 
    
    
    gcloud alpha scc findings create `testFinding` --organization=123456 --source=5678 --state=ACTIVE --category='XSS_SCRIPTING' --event-time=2023-01-11T07:00:06.861Z --resource-name='//cloudresourcemanager.googleapis.com/projects/9876'

Create an ACTIVE finding `testFinding` with category: XSS_SCRIPTING attached to project with project number `9876` under organization `123456` and source `5678` using the full resource name: 
    
    
    gcloud alpha scc findings create organizations/123456/sources/5678/findings/testFinding --state=ACTIVE --category='XSS_SCRIPTING' --event-time=2023-01-11T07:00:06.861Z --resource-name='//cloudresourcemanager.googleapis.com/projects/9876'

Create an ACTIVE finding `testFinding` with category: `XSS_SCRIPTING` attached to project with project number`9876` under organization `123456`, source `5678` and `location=eu`: 
    
    
    gcloud alpha scc findings create `testFinding` --organization=123456 --source=5678 --state=ACTIVE --category='XSS_SCRIPTING' --event-time=2023-01-11T07:00:06.861Z --resource-name='//cloudresourcemanager.googleapis.com/projects/9876' --location=eu

`

POSITIONAL ARGUMENTS
    

Finding resource - The finding to be used for the SCC (Security Command Center) command. The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`FINDING`
     ID of the finding or fully qualified identifier for the finding. 

To set the `finding` attribute: 

  * provide the argument `finding` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--organization`=`ORGANIZATION`
     (Optional) If the full resource name isn't provided e.g. organizations/123, then provide the organization id which is the suffix of the organization. Example: organizations/123, the id is 123. 

To set the `organization` attribute: 

  * provide the argument `finding` on the command line with a fully specified name; 
  * provide the argument `--organization` on the command line; 
  * Set the organization property in configuration using `gcloud config set scc/organization` if it is not specified in command line.. 


`--source`=`SOURCE`
     (Optional) If the full resource name isn't provided e.g. organizations/123/sources/456, then provide the source id which is the suffix of the source. Example: organizations/123/sources/456, the id is 456. 

To set the `source` attribute: 

  * provide the argument `finding` on the command line with a fully specified name; 
  * provide the argument `--source` on the command line. 


REQUIRED FLAGS
    

`--category`=`CATEGORY`
     Taxonomy group within findings from a given source. Example: XSS_SCRIPTING 
`--event-time`=`EVENT_TIME`
     Time at which the event took place. For example, if the finding represents an open firewall it would capture the time the open firewall was detected. If event-time is not provided, it will default to UTC version of NOW. See `$ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes)` for information on supported time formats. 
`--resource-name`=`RESOURCE_NAME`
     Full resource name of the Google Cloud Platform resource this finding is for. 
OPTIONAL FLAGS
    

`--external-uri`=`EXTERNAL_URI`
     URI that, if available, points to a web page outside of Cloud SCC (Security Command Center) where additional information about the finding can be found. This field is guaranteed to be either empty or a well formed URL. 
`--location`=`LOCATION`; default="global"
     When data residency controls are enabled, this attribute specifies the location in which the resource is located and applicable. The `location` attribute can be provided as part of the fully specified resource name or with the `--location` argument on the command line. The default location is `global`. 

NOTE: If you override the endpoint to a [regional endpoint](https://cloud.google.com/security-command-center/docs/reference/rest/index.html?rep_location=global#regional-service-endpoint) you must specify the correct [data location](https://cloud.google.com/security-command-center/docs/data-residency-support#locations) using this flag. The default location on this command is unrelated to the default location that is specified when data residency controls are enabled for Security Command Center. 

NOTE: If no location is specified, the default location is `global` AND the request will be routed to the SCC V1 API. To use the SCC V2 API - please explicitly specify the flag. 

`--source-properties`=[`KEY`=`VALUE`,…]
     Source specific properties. These properties are managed by the source that writes the finding. The key names in the source_properties map must be between 1 and 255 characters, and must start with a letter and contain alphanumeric characters or underscores only. For example "key1=val1,key2=val2" 
`--state`=`STATE`
     State is one of: [ACTIVE, INACTIVE]. `STATE` must be one of: `active`, `inactive`, `state-unspecified`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the Security Command Center API. For more information, see [Security Command Center API.](https://cloud.google.com/security-command-center/docs/reference/rest)
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud scc findings create](https://docs.cloud.google.com/sdk/gcloud/reference/scc/findings/create)
    
    
    [gcloud beta scc findings create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/scc/findings/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
