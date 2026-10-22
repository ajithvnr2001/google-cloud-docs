---
url: https://docs.cloud.google.com/asset-inventory/docs/roles-permissions/
title: Roles and permissions \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:41:36.833951+00:00
---

# Roles and permissions  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/roles-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Guides ](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview)



Send feedback 

#  Roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Asset Inventory uses [Identity and Access Management](https://docs.cloud.google.com/iam/docs) (IAM) for access control. Every Cloud Asset Inventory API method requires the caller to have the necessary permissions.

## Roles

To get the permissions that you need to work with asset metadata, ask your administrator to grant you the following IAM roles on the organization, folder, or project: 

  * To view asset metadata: 
    * [Cloud Asset Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudasset#cloudasset.viewer) (`roles/cloudasset.viewer`)
    * [Service Usage Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`)
  * To view asset metadata and work with feeds: 
    * [Cloud Asset Owner ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudasset#cloudasset.owner) (`roles/cloudasset.owner`)
    * [Service Usage Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to work with asset metadata. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to work with asset metadata:

  * To view asset metadata: 
    * `cloudasset.assets.*`
    * `recommender.cloudAssetInsights.get`
    * `recommender.cloudAssetInsights.list`
    * `serviceusage.services.use`
  * To view asset metadata and work with feeds: 
    * `cloudasset.*`
    * `recommender.cloudAssetInsights.*`
    * `serviceusage.services.use`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Permissions

The following table lists the permissions that the caller must have to call each API method in Cloud Asset Inventory, or to perform tasks using Google Cloud tools that use Cloud Asset Inventory such as the Google Cloud console or gcloud CLI.

The Cloud Asset Viewer (`roles/cloudasset.viewer`) and Cloud Asset Owner (`roles/cloudasset.owner`) roles include many of these permissions. If the caller has been granted one of these roles and the Service Usage Consumer (`roles/serviceusage.serviceUsageConsumer`) role, they might already have the permissions they need to use Cloud Asset Inventory.

###  RPC 

Method | Required permissions  
---|---  
All APIs  
All Cloud Asset Inventory calls |  All Cloud Asset Inventory calls require the `serviceusage.services.use` permission.   
Analysis APIs  
`AnalyzeIamPolicy` `AnalyzeIamPolicyLongRunning` `BatchGetEffectiveIamPolicies` |  All of the following permissions:

  * ` cloudasset.assets.analyzeIamPolicy `
  * ` cloudasset.assets.searchAllIamPolicies `
  * ` cloudasset.assets.searchAllResources `
  * ` iam.roles.get ` to analyze policies with custom roles 

[ Additional permissions are required for working with Google Workspace](https://docs.cloud.google.com/policy-intelligence/docs/analyze-iam-policies#gsuite-permissions).   
`AnalyzeMove` | ` cloudasset.assets.analyzeMove `  
`AnalyzeOrgPolicies` `AnalyzeOrgPolicyGovernedContainers` |  All of the following permissions:

  * ` cloudasset.assets.analyzeOrgPolicy `
  * ` cloudasset.assets.searchAllResources `

  
`AnalyzeOrgPolicyGovernedAssets` |  All of the following permissions:

  * ` cloudasset.assets.analyzeOrgPolicy `
  * ` cloudasset.assets.searchAllIamPolicies `
  * ` cloudasset.assets.searchAllResources `

  
Feed APIs  
`CreateFeed` |  ` cloudasset.feeds.create ` You also need one of the following permissions, depending on the [ content type](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview#content_types):

  * ` cloudasset.assets.exportIamPolicy `
  * ` cloudasset.assets.exportResource `

  
`DeleteFeed` | ` cloudasset.feeds.delete `  
`GetFeed` | ` cloudasset.feeds.get `  
`ListFeed` | ` cloudasset.feeds.list `  
`UpdateFeed` |  ` cloudasset.feeds.update ` You also need one of the following permissions, depending on the [ content type](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview#content_types):

  * ` cloudasset.assets.exportIamPolicy `
  * ` cloudasset.assets.exportResource `

  
Inventory APIs  
`BatchGetAssetsHistory` `ExportAssets` |  One of the following permissions, depending on the [ content type](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview#content_types):

  * ` cloudasset.assets.exportAccessPolicy ` When using the `ACCESS_POLICY` content type.
  * ` cloudasset.assets.exportIamPolicy ` When using the `IAM_POLICY` content type.
  * ` cloudasset.assets.exportOrgPolicy ` When using the `ORG_POLICY` content type.
  * ` cloudasset.assets.exportOSInventories ` When using the `OS_INVENTORY` content type.
  * ` cloudasset.assets.exportResource ` When using the `RELATIONSHIP` or `RESOURCE` content types.

#### **Limiting resource access**

Granting the ` cloudasset.assets.exportResource ` permission to a user allows them to export all resource types. To restrict what resource types a user can export, you can grant permissions for each resource type instead. For example, you can grant the `cloudasset.assets.exportComputeDisks` permission by itself to allow a user to only export the `compute.googleapis.com/Disk` resource type.  These granular permissions only apply to `RESOURCE` and unspecified [ content types](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview#content_types).  [ View the list of granular `cloudasset.assets.export*` permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudasset#cloudasset.assets.exportAccessLevel). 

  
`ListAssets` |  One of the following permissions, depending on the [ content type](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview#content_types):

  * ` cloudasset.assets.listAccessPolicy `
  * ` cloudasset.assets.listIamPolicy `
  * ` cloudasset.assets.listOrgPolicy `
  * ` cloudasset.assets.listOSInventories `
  * ` cloudasset.assets.listResource ` When using the `RELATIONSHIP` or `RESOURCE` content types.

#### **Limiting resource access**

Granting the ` cloudasset.assets.listResource ` permission to a user allows them to list all resource types. To restrict what resource types a user can list, you can grant permissions for each resource type instead. For example, you can grant the `cloudasset.assets.listComputeDisks` permission by itself to allow a user to only list the `compute.googleapis.com/Disk` resource type.  These granular permissions only apply to `RESOURCE` and unspecified [ content types](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview#content_types).  [ View the list of granular `cloudasset.assets.list*` permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudasset#cloudasset.assets.listAccessLevel). 

  
`QueryAssets` |  One of the following permissions, depending on the [ content type](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview#content_types):

  * ` cloudasset.assets.queryAccessPolicy `
  * ` cloudasset.assets.queryIamPolicy `
  * ` cloudasset.assets.queryOSInventories `
  * ` cloudasset.assets.queryResource ` When using the `RELATIONSHIP` or `RESOURCE` content types.

  
Search APIs  
`SearchAllIamPolicies` | ` cloudasset.assets.searchAllIamPolicies `  
`SearchAllResources` |  ` cloudasset.assets.searchAllResources ` You also need ` cloudasset.assets.searchEnrichmentResourceOwners ` if searching for resource owner enrichment.  
  
###  REST 

Method | Required permissions  
---|---  
All APIs  
All Cloud Asset Inventory calls |  All Cloud Asset Inventory calls require the `serviceusage.services.use` permission.   
Analysis APIs  
`analyzeIamPolicy` `analyzeIamPolicyLongRunning` `effectiveIamPolicies.batchGet` |  All of the following permissions:

  * ` cloudasset.assets.analyzeIamPolicy `
  * ` cloudasset.assets.searchAllIamPolicies `
  * ` cloudasset.assets.searchAllResources `
  * ` iam.roles.get ` to analyze policies with custom roles 

[ Additional permissions are required for working with Google Workspace](https://docs.cloud.google.com/policy-intelligence/docs/analyze-iam-policies#gsuite-permissions).   
`analyzeMove` | ` cloudasset.assets.analyzeMove `  
`analyzeOrgPolicies` `analyzeOrgPolicyGovernedContainers` |  All of the following permissions:

  * ` cloudasset.assets.analyzeOrgPolicy `
  * ` cloudasset.assets.searchAllResources `

  
`analyzeOrgPolicyGovernedAssets` |  All of the following permissions:

  * ` cloudasset.assets.analyzeOrgPolicy `
  * ` cloudasset.assets.searchAllIamPolicies `
  * ` cloudasset.assets.searchAllResources `

  
Feed APIs  
`feeds.create` |  ` cloudasset.feeds.create ` You also need one of the following permissions, depending on the [ content type](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview#content_types):

  * ` cloudasset.assets.exportIamPolicy `
  * ` cloudasset.assets.exportResource `

  
`feeds.delete` | ` cloudasset.feeds.delete `  
`feeds.get` | ` cloudasset.feeds.get `  
`feeds.list` | ` cloudasset.feeds.list `  
`feeds.patch` |  ` cloudasset.feeds.update ` You also need one of the following permissions, depending on the [ content type](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview#content_types):

  * ` cloudasset.assets.exportIamPolicy `
  * ` cloudasset.assets.exportResource `

  
Inventory APIs  
`batchGetAssetsHistory` `exportAssets` |  One of the following permissions, depending on the [ content type](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview#content_types):

  * ` cloudasset.assets.exportAccessPolicy ` When using the `ACCESS_POLICY` content type.
  * ` cloudasset.assets.exportIamPolicy ` When using the `IAM_POLICY` content type.
  * ` cloudasset.assets.exportOrgPolicy ` When using the `ORG_POLICY` content type.
  * ` cloudasset.assets.exportOSInventories ` When using the `OS_INVENTORY` content type.
  * ` cloudasset.assets.exportResource ` When using the `RELATIONSHIP` or `RESOURCE` content types.

#### **Limiting resource access**

Granting the ` cloudasset.assets.exportResource ` permission to a user allows them to export all resource types. To restrict what resource types a user can export, you can grant permissions for each resource type instead. For example, you can grant the `cloudasset.assets.exportComputeDisks` permission by itself to allow a user to only export the `compute.googleapis.com/Disk` resource type.  These granular permissions only apply to `RESOURCE` and unspecified [ content types](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview#content_types).  [ View the list of granular `cloudasset.assets.export*` permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudasset#cloudasset.assets.exportAccessLevel). 

  
`assets.list` |  One of the following permissions, depending on the [ content type](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview#content_types):

  * ` cloudasset.assets.listAccessPolicy `
  * ` cloudasset.assets.listIamPolicy `
  * ` cloudasset.assets.listOrgPolicy `
  * ` cloudasset.assets.listOSInventories `
  * ` cloudasset.assets.listResource ` When using the `RELATIONSHIP` or `RESOURCE` content types.

#### **Limiting resource access**

Granting the ` cloudasset.assets.listResource ` permission to a user allows them to list all resource types. To restrict what resource types a user can list, you can grant permissions for each resource type instead. For example, you can grant the `cloudasset.assets.listComputeDisks` permission by itself to allow a user to only list the `compute.googleapis.com/Disk` resource type.  These granular permissions only apply to `RESOURCE` and unspecified [ content types](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview#content_types).  [ View the list of granular `cloudasset.assets.list*` permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudasset#cloudasset.assets.listAccessLevel). 

  
`queryAssets` |  One of the following permissions, depending on the [ content type](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview#content_types):

  * ` cloudasset.assets.queryAccessPolicy `
  * ` cloudasset.assets.queryIamPolicy `
  * ` cloudasset.assets.queryOSInventories `
  * ` cloudasset.assets.queryResource ` When using the `RELATIONSHIP` or `RESOURCE` content types.

  
Search APIs  
`searchAllIamPolicies` | ` cloudasset.assets.searchAllIamPolicies `  
`searchAllResources` |  ` cloudasset.assets.searchAllResources ` You also need ` cloudasset.assets.searchEnrichmentResourceOwners ` if searching for resource owner enrichment.  
  
###  gcloud 

Positional statement | Required permissions  
---|---  
All APIs  
All Cloud Asset Inventory calls |  All Cloud Asset Inventory calls require the `serviceusage.services.use` permission.   
Analysis APIs  
`analyze-iam-policy` `analyze-iam-policy-longrunning` `get-effective-iam-policy` |  All of the following permissions:

  * ` cloudasset.assets.analyzeIamPolicy `
  * ` cloudasset.assets.searchAllIamPolicies `
  * ` cloudasset.assets.searchAllResources `
  * ` iam.roles.get ` to analyze policies with custom roles 

[ Additional permissions are required for working with Google Workspace](https://docs.cloud.google.com/policy-intelligence/docs/analyze-iam-policies#gsuite-permissions).   
`analyze-move` | ` cloudasset.assets.analyzeMove `  
`analyze-org-policies` `analyze-org-policy-governed-containers` |  All of the following permissions:

  * ` cloudasset.assets.analyzeOrgPolicy `
  * ` cloudasset.assets.searchAllResources `

  
`analyze-org-policy-governed-assets` |  All of the following permissions:

  * ` cloudasset.assets.analyzeOrgPolicy `
  * ` cloudasset.assets.searchAllIamPolicies `
  * ` cloudasset.assets.searchAllResources `

  
Feed APIs  
`feeds create` |  ` cloudasset.feeds.create ` You also need one of the following permissions, depending on the [ content type](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview#content_types):

  * ` cloudasset.assets.exportIamPolicy `
  * ` cloudasset.assets.exportResource `

  
`feeds delete` | ` cloudasset.feeds.delete `  
`feeds describe` | ` cloudasset.feeds.get `  
`feeds list` | ` cloudasset.feeds.list `  
`feeds update` |  ` cloudasset.feeds.update ` You also need one of the following permissions, depending on the [ content type](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview#content_types):

  * ` cloudasset.assets.exportIamPolicy `
  * ` cloudasset.assets.exportResource `

  
Inventory APIs  
`export` `get-history` |  One of the following permissions, depending on the [ content type](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview#content_types):

  * ` cloudasset.assets.exportAccessPolicy ` When using the `ACCESS_POLICY` content type.
  * ` cloudasset.assets.exportIamPolicy ` When using the `IAM_POLICY` content type.
  * ` cloudasset.assets.exportOrgPolicy ` When using the `ORG_POLICY` content type.
  * ` cloudasset.assets.exportOSInventories ` When using the `OS_INVENTORY` content type.
  * ` cloudasset.assets.exportResource ` When using the `RELATIONSHIP` or `RESOURCE` content types.

#### **Limiting resource access**

Granting the ` cloudasset.assets.exportResource ` permission to a user allows them to export all resource types. To restrict what resource types a user can export, you can grant permissions for each resource type instead. For example, you can grant the `cloudasset.assets.exportComputeDisks` permission by itself to allow a user to only export the `compute.googleapis.com/Disk` resource type.  These granular permissions only apply to `RESOURCE` and unspecified [ content types](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview#content_types).  [ View the list of granular `cloudasset.assets.export*` permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudasset#cloudasset.assets.exportAccessLevel). 

  
`list` |  One of the following permissions, depending on the [ content type](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview#content_types):

  * ` cloudasset.assets.listAccessPolicy `
  * ` cloudasset.assets.listIamPolicy `
  * ` cloudasset.assets.listOrgPolicy `
  * ` cloudasset.assets.listOSInventories `
  * ` cloudasset.assets.listResource ` When using the `RELATIONSHIP` or `RESOURCE` content types.

#### **Limiting resource access**

Granting the ` cloudasset.assets.listResource ` permission to a user allows them to list all resource types. To restrict what resource types a user can list, you can grant permissions for each resource type instead. For example, you can grant the `cloudasset.assets.listComputeDisks` permission by itself to allow a user to only list the `compute.googleapis.com/Disk` resource type.  These granular permissions only apply to `RESOURCE` and unspecified [ content types](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview#content_types).  [ View the list of granular `cloudasset.assets.list*` permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudasset#cloudasset.assets.listAccessLevel). 

  
`query` |  One of the following permissions, depending on the [ content type](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview#content_types):

  * ` cloudasset.assets.queryAccessPolicy `
  * ` cloudasset.assets.queryIamPolicy `
  * ` cloudasset.assets.queryOSInventories `
  * ` cloudasset.assets.queryResource ` When using the `RELATIONSHIP` or `RESOURCE` content types.

  
Search APIs  
`search-all-iam-policies` | ` cloudasset.assets.searchAllIamPolicies `  
`search-all-resources` |  ` cloudasset.assets.searchAllResources ` You also need ` cloudasset.assets.searchEnrichmentResourceOwners ` if searching for resource owner enrichment.  
  
###  Console 

The Google Cloud console uses the `SearchAllResources` API to request data. To use Cloud Asset Inventory in the Google Cloud console, grant the following permissions: 

  * ` cloudasset.assets.searchAllResources `
  * ` serviceusage.services.use `



## VPC Service Controls

VPC Service Controls can be used with Cloud Asset Inventory to provide additional security for your assets. To learn more about VPC Service Controls, see the [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

To learn about the limitations in using Cloud Asset Inventory with VPC Service Controls, see the [supported products and limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
