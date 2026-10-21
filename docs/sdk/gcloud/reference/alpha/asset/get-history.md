---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/asset/get-history/
title: gcloud alpha asset get-history \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:35:48.534482+00:00
---

# gcloud alpha asset get-history  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/asset/get-history/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha asset get-history Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha asset get-history - get the update history of assets that overlaps a time window 
SYNOPSIS
    

`gcloud alpha asset get-history` `--asset-names`=[`ASSET_NAMES`,…] `--content-type`=`CONTENT_TYPE` `--start-time`=`START_TIME` (`--organization`=`ORGANIZATION_ID` | `--project`=`PROJECT_ID`) [`--end-time`=`END_TIME`] [`--relationship-types`=[`RELATIONSHIP_TYPES`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Get the update history of assets that overlaps a time window. 
EXAMPLES
     To get the history of asset metadata for '//compute.googleapis.com/projects/test-project/zones/us-central1-f/instances/instance1' between '2018-10-02T15:01:23.045Z' and '2018-12-05T13:01:21.045Z', run: 
    
    
    gcloud alpha asset get-history --project='test-project' --asset-names='//compute.googleapis.com/projects/test-project/zones/us-central1-f/instances/instance1' --start-time='2018-10-02T15:01:23.045Z' --end-time='2018-12-05T13:01:21.045Z' --content-type='resource'

To get the history of asset iam policy for '//cloudresourcemanager.googleapis.com/projects/10179387634' between '2018-10-02T15:01:23.045Z' and '2018-12-05T13:01:21.045Z', and project '10179387634' is in organization '1060499660910', run: 
    
    
    gcloud alpha asset get-history --organization='1060499660910' --asset-names='//cloudresourcemanager.googleapis.com/projects/10179387634' --start-time='2018-10-02T15:01:23.045Z' --end-time='2018-12-05T13:01:21.045Z' --content-type='iam-policy'

REQUIRED FLAGS
    

`--asset-names`=[`ASSET_NAMES`,…]
     A list of full names of the assets to get the history for. For more information, see: <https://cloud.google.com/apis/design/resource_names#full_resource_name>
`--content-type`=`CONTENT_TYPE`
     Asset content type. Specifying `resource` will export resource metadata, specifying `iam-policy` will export the IAM policy for each child asset, specifying `org-policy` will export the Org Policy set on child assets, specifying `access-policy` will export the Access Policy set on child assets, specifying `os-inventory` will export the OS inventory of VM instances, and specifying `relationship` will export relationships of the assets. `CONTENT_TYPE` must be one of: `resource`, `iam-policy`, `org-policy`, `access-policy`, `os-inventory`, `relationship`. 
`--start-time`=`START_TIME`
     Start time of the time window (inclusive) for the asset history. Must be after the current time minus 35 days. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on time formats. 
Exactly one of these must be specified: 

`--organization`=`ORGANIZATION_ID`
     The ID of the organization which is the root asset. 
`--project`=`PROJECT_ID`
     The project which is the root asset. 

The Google Cloud project ID to use for this invocation. If omitted, then the current project is assumed; the current project can be listed using `gcloud config list --format='text(core.project)'` and can be set using `gcloud config set project PROJECTID`. 

`--project` and its fallback `core/project` property play two roles in the invocation: they specify both the project of the resource to operate on, and the project for API enablement checks, quota, and billing. To specify a different project for quota and billing, use the `--billing-project` flag or the `billing/quota_project` property. 

OPTIONAL FLAGS
    

`--end-time`=`END_TIME`
     End time of the time window (exclusive) for the asset history. Defaults to current time if not specified. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on time formats. 
`--relationship-types`=[`RELATIONSHIP_TYPES`,…]
     A list of relationship types (i.e., "INSTANCE_TO_INSTANCEGROUP") to take a snapshot. This argument will only be honoured if content_type=RELATIONSHIP. If specified and non-empty, only relationships matching the specified types will be returned. See <http://cloud.google.com/asset-inventory/docs/supported-asset-types> for supported relationship types. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud asset get-history](https://docs.cloud.google.com/sdk/gcloud/reference/asset/get-history)
    
    
    [gcloud beta asset get-history](https://docs.cloud.google.com/sdk/gcloud/reference/beta/asset/get-history)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-15 UTC."],[],[]] 
