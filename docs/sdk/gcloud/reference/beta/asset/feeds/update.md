---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/asset/feeds/update/
title: gcloud beta asset feeds update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:02:42.629464+00:00
---

# gcloud beta asset feeds update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/asset/feeds/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta asset feeds update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta asset feeds update - update an existing Cloud Asset Inventory Feed 
SYNOPSIS
    

`gcloud beta asset feeds update` `FEED_ID` (`--folder`=`FOLDER_ID` | `--organization`=`ORGANIZATION_ID` | `--project`=`PROJECT_ID`) [`--pubsub-topic`=`PUBSUB_TOPIC`] [`--add-asset-names`=[`ASSET-NAMES`,…] | `--clear-asset-names` | `--remove-asset-names`=[`ASSET-NAMES`,…]] [`--add-asset-types`=[`ASSET-TYPES`,…] | `--clear-asset-types` | `--remove-asset-types`=[`ASSET-TYPES`,…]] [`--add-relationship-types`=[`RELATIONSHIP-TYPES`,…] | `--clear-relationship-types` | `--remove-relationship-types`=[`RELATIONSHIP-TYPES`,…]] [`--clear-condition-description` | `--condition-description`=`CONDITION_DESCRIPTION`] [`--clear-condition-expression` | `--condition-expression`=`CONDITION_EXPRESSION`] [`--clear-condition-title` | `--condition-title`=`CONDITION_TITLE`] [`--clear-content-type` | `--content-type`=`CONTENT_TYPE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Update an existing Cloud Asset Inventory Feed. 
EXAMPLES
     To add an asset-type to an existing feed, run: 
    
    
    gcloud beta asset feeds update feed1 --project=p1 --add-asset-types=pubsub.googleapis.com/Topic

POSITIONAL ARGUMENTS
    

`FEED_ID`
     Identifier of the asset feed to update, which must be unique in its parent resource. Parent resource can be a project, folder, or an organization. 
REQUIRED FLAGS
    

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
    

`--pubsub-topic`=`PUBSUB_TOPIC`
     Name of the Cloud Pub/Sub topic to publish to, of the form `projects/PROJECT_ID/topics/TOPIC_ID`. You can list existing topics with `gcloud pubsub topics list --format="text(name)"`
These flags modify the member assetNames of this Feed. See <https://cloud.google.com/apis/design/resource_names#full_resource_name> for more information. 

At most one of these can be specified: 

`--add-asset-names`=[`ASSET-NAMES`,…]
     Append the given values to the current assetNames. 
`--clear-asset-names`
     Empty the current assetNames. 
`--remove-asset-names`=[`ASSET-NAMES`,…]
     Remove the given values from the current assetNames. 
These flags modify the member assetTypes of this Feed. See <https://cloud.google.com/resource-manager/docs/cloud-asset-inventory/overview> for all supported asset types. 

At most one of these can be specified: 

`--add-asset-types`=[`ASSET-TYPES`,…]
     Append the given values to the current assetTypes. 
`--clear-asset-types`
     Empty the current assetTypes. 
`--remove-asset-types`=[`ASSET-TYPES`,…]
     Remove the given values from the current assetTypes. 
These flags modify the member relationshipTypes of this Feed. See <https://cloud.google.com/resource-manager/docs/cloud-asset-inventory/overview> for all supported relationship types. 

At most one of these can be specified: 

`--add-relationship-types`=[`RELATIONSHIP-TYPES`,…]
     Append the given values to the current relationshipTypes. 
`--clear-relationship-types`
     Empty the current relationshipTypes. 
`--remove-relationship-types`=[`RELATIONSHIP-TYPES`,…]
     Remove the given values from the current relationshipTypes. 
At most one of these can be specified: 

`--clear-condition-description`
     Clear any existing condition description setting on the feed. Condition description will be empty. 
`--condition-description`=`CONDITION_DESCRIPTION`
     Condition description to overwrite the existing one. 
At most one of these can be specified: 

`--clear-condition-expression`
     Clear any existing condition expression setting on the feed. No condition will be applied to feed. 
`--condition-expression`=`CONDITION_EXPRESSION`
     Condition expression to overwrite the existing one. For more information, see: <https://cloud.google.com/asset-inventory/docs/monitoring-asset-changes#feed_with_condition>
At most one of these can be specified: 

`--clear-condition-title`
     Clear any existing condition title setting on the feed. Condition title will be empty. 
`--condition-title`=`CONDITION_TITLE`
     Condition title to overwrite the existing one. 
At most one of these can be specified: 

`--clear-content-type`
     Clear any existing content type setting on the feed. Content type will be unspecified, no content but the asset name and type will be returned in the feed. 
`--content-type`=`CONTENT_TYPE`
     Asset content type to overwrite the existing one. For more information, see: <https://cloud.google.com/resource-manager/docs/cloud-asset-inventory/overview#asset_content_type>. `CONTENT_TYPE` must be one of: `resource`, `iam-policy`, `org-policy`, `access-policy`, `os-inventory`, `relationship`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud asset feeds update](https://docs.cloud.google.com/sdk/gcloud/reference/asset/feeds/update)
    
    
    [gcloud alpha asset feeds update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-15 UTC."],[],[]] 
