---
url: https://docs.cloud.google.com/sdk/gcloud/reference/asset/feeds/create/
title: gcloud asset feeds create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:33:02.286641+00:00
---

# gcloud asset feeds create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/asset/feeds/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud asset feeds create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud asset feeds create - create a Cloud Asset Inventory Feed 
SYNOPSIS
    

`gcloud asset feeds create` `FEED_ID` `--pubsub-topic`=`PUBSUB_TOPIC` (`--asset-names`=[`ASSET_NAMES`,…] `--asset-types`=[`ASSET_TYPES`,…] `--relationship-types`=[`RELATIONSHIP_TYPES`,…]) (`--folder`=`FOLDER_ID` | `--organization`=`ORGANIZATION_ID` | `--project`=`PROJECT_ID`) [`--condition-description`=`CONDITION_DESCRIPTION`] [`--condition-expression`=`CONDITION_EXPRESSION`] [`--condition-title`=`CONDITION_TITLE`] [`--content-type`=`CONTENT_TYPE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a new Cloud Asset Inventory Feed for updates on assets. 
EXAMPLES
     To create a new feed 'feed1' in project 'p1' which alerts on compute disks and network resources types, run: 
    
    
    gcloud asset feeds create feed1 --project=p1 --asset-types=compute.googleapis.com/Network,compute.googleapis.com/Disk --content-type=resource --pubsub-topic=projects/project1/topics/feed-topic

POSITIONAL ARGUMENTS
    

`FEED_ID`
     Asset feed identifier being created, it must be unique under the specified parent resource project/folder/organization. 
REQUIRED FLAGS
    

`--pubsub-topic`=`PUBSUB_TOPIC`
     Name of the Cloud Pub/Sub topic to publish to, of the form `projects/PROJECT_ID/topics/TOPIC_ID`. You can list existing topics with `gcloud pubsub topics list --format="text(name)"`
At least one of these must be specified: 

`--asset-names`=[`ASSET_NAMES`,…]
     A comma-separated list of the full names of the assets to receive updates. For example: `//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1`. For more information, see: <https://cloud.google.com/apis/design/resource_names#full_resource_name>
`--asset-types`=[`ASSET_TYPES`,…]
     A comma-separated list of types of the assets types to receive updates. For example: `compute.googleapis.com/Disk,compute.googleapis.com/Network`. Regular expressions (https://github.com/google/re2/wiki/Syntax) are also supported. For more information, see: <https://cloud.google.com/resource-manager/docs/cloud-asset-inventory/overview>
`--relationship-types`=[`RELATIONSHIP_TYPES`,…]
     A comma-separated list of the relationship types (i.e., "INSTANCE_TO_INSTANCEGROUP") to receive updates. This argument will only be honoured if content_type=RELATIONSHIP.See <http://cloud.google.com/asset-inventory/docs/supported-asset-types> for supported relationship types. 
Exactly one of these must be specified: 

`--folder`=`FOLDER_ID`
     Folder of the feed. 
`--organization`=`ORGANIZATION_ID`
     Organization of the feed. 
`--project`=`PROJECT_ID`
     project of the feed. 

The Google Cloud project ID to use for this invocation. If omitted, then the current project is assumed; the current project can be listed using `gcloud config list --format='text(core.project)'` and can be set using `gcloud config set project PROJECTID`. 

`--project` and its fallback `core/project` property play two roles in the invocation: they specify both the project of the resource to operate on, and the project for API enablement checks, quota, and billing. To specify a different project for quota and billing, use the `--billing-project` flag or the `billing/quota_project` property. 

OPTIONAL FLAGS
    

`--condition-description`=`CONDITION_DESCRIPTION`
     Description of the feed condition. For reference only. 
`--condition-expression`=`CONDITION_EXPRESSION`
     Feed condition expression. If not specified, no condition will be applied to feed. For more information, see: <https://cloud.google.com/asset-inventory/docs/monitoring-asset-changes#feed_with_condition>
`--condition-title`=`CONDITION_TITLE`
     Title of the feed condition. For reference only. 
`--content-type`=`CONTENT_TYPE`
     Asset content type. If not specified, no content but the asset name and type will be returned in the feed. For more information, see <https://cloud.google.com/resource-manager/docs/cloud-asset-inventory/overview#asset_content_type>. `CONTENT_TYPE` must be one of: `resource`, `iam-policy`, `org-policy`, `access-policy`, `os-inventory`, `relationship`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha asset feeds create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/create)
    
    
    [gcloud beta asset feeds create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/asset/feeds/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-15 UTC."],[],[]] 
