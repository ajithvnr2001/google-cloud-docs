---
url: https://docs.cloud.google.com/assured-workloads/docs/migrate-workload/
title: Migrate a workload \u00a0|\u00a0 Assured Workloads \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:36:08.052761+00:00
---

# Migrate a workload  |  Assured Workloads  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/docs/migrate-workload/

The names for some Assured Workloads control packages have changed. For information about the name change, see [Control package renaming notice](https://docs.cloud.google.com/assured-workloads/docs/overview#name-change). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-workloads/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Migrate a workload

This page describes how to perform a compliance analysis before migrating an existing project to an Assured Workloads folder. This analysis compares the source project and the destination Assured Workloads folder to determine what changes might be required before or after you initiate the migration. For example, if you have a project that you want to move to an Assured Workloads folder configured for FedRAMP Moderate, you can proactively address any potential compliance violations that might occur before moving the project.

The following types of findings are returned by the move analysis:

  * The source project uses unsupported products or services.
  * The source project contains resources that are located in a disallowed location.
  * The source project is configured with organization policy constraint values that are incompatible with the destination Assured Workloads folder.



These findings are important to discover before attempting a move. By default, an Assured Workloads folder can only contain resource types for the [services that are supported](https://docs.cloud.google.com/assured-workloads/docs/supported-products) by the folder's control package. If your project contains resources for a service that is not supported by the folder's control package, you may need to redeploy or remove those resources.

Although you can change the default list of supported services for an Assured Workloads folder by changing its [resource usage restriction organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) —thus allowing non-compliant services to be deployed in your folder— the non-compliant service and its resources will be ignored by background compliance checks. Therefore, by enabling an unsupported service, you are choosing to accept the risk that it may cause your workload to fall out of compliance.

**Note:** After performing a migration analysis and addressing any findings, the steps for moving a project to an Assured Workloads folder are the same as when moving any project in Google Cloud. See [Moving a project](https://docs.cloud.google.com/resource-manager/docs/moving-projects-folders) in the Resource Manager documentation.

## Migrating Assured Workloads folders and projects

If you're migrating Assured Workloads folders or projects, only migrate them to a folder that uses the same control package. Otherwise, you can incur additional billing fees and undermine your compliance status.

## Before you begin

  * Gather the resource IDs for both the source project and the destination Assured Workloads folder.
  * Assign or verify IAM permissions on both the source project and the destination Assured Workloads folder to ensure that the caller is authorized to perform the migration.



### Required IAM permissions

To perform a migration analysis, the caller must be granted IAM permissions using either a [predefined role](https://docs.cloud.google.com/iam/docs/roles-permissions) that includes a wider set of permissions, or a [custom role](https://docs.cloud.google.com/iam/docs/understanding-roles#custom_roles) that is restricted to the minimum necessary permissions.

The following permissions are required:

  * `assuredworkloads.workload.get` on the destination [workload](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/Workload)
  * `cloudasset.assets.searchAllResources` on the source project
  * `orgpolicy.policy.get` on the source project and destination Assured Workloads folder



## Performing a migration analysis

When performing an analysis on the source project and the destination Assured Workloads folder, you should address any findings before moving the project to the destination. Although the findings don't prevent you from moving the project, they may result in compliance violations in the destination Assured Workloads folder.

These findings are of two different types:

  * **Warning** : A warning result occurs when the source project is potentially incompatible with the destination, and may result in a compliance violation. Warnings should be investigated to verify that the incompatibility is either acceptable or should be addressed before the move.
  * **Blocker** : A blocker result occurs when a compliance violation is detected between the source project and the destination. Blockers must be addressed before proceeding with a move.



The following types of findings are reported:

  * **Resource locations** : Many control packages enforce location restrictions for resources to adhere to compliance requirements, such as if your source project contains resources that are located in a disallowed location.

To resolve this issue, move the affected resources to allowed locations, delete them, or modify the target's `gcp.resourceLocations` organization policy constraint setting.

  * **Unsupported products/services** : Each control package supports a specific list of Google Cloud products and services. If your project uses a service that is unsupported by the destination Assured Workloads folder's control package, this will be listed as a finding.

**Warning:** We recommend that you don't migrate a project that uses unsupported products or services without first disabling them. However, if you choose to accept the risk and proceed with the migration, be sure to [disable resource usage restrictions](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) on the destination folder or update it to allow the unsupported services.
  * **Organization Policy constraints** : Your source project may be configured with organization policy constraint values that differ from the destination Assured Workloads folder's effective policy, or are not compliant with the target control package. This analysis is performed only for constraints that are relevant to the destination Assured Workloads folder's control package; all of the project's constraint values are not evaluated. Several outcomes are possible, such as the following issues:

    * Your project and the destination's effective policy are incompatible.
    * Your project has organization policy constraint values that aren't set on the destination, or the other way around.
    * Your project has organization policy constraint values that aren't compliant with the target control package.

If a blocker is found for an organization policy constraint, the response includes the expected values that are compliant with the target control package. You can use these expected values to make changes to your project before you perform a migration.




To resolve this issue, determine which organization policy constraint needs to be modified, and [make the required changes](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#list_constraints).

### Unsupported finding types

The migration analysis doesn't support the following types of findings:

  * Resource-level incompatibilities for organization policy constraints other than `gcp.resourceLocations`. For example, some control packages are configured with the global `gcp.restrictCmekCryptoKeyProjects` constraint or the Compute Engine-specific `compute.disableNestedVirtualization` constraint; incompatibilities with these constraints between the source and destination are not analyzed or reported.
  * Service-specific features that may be disabled for a given control package. For example, [Cloud Monitoring's uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks#monitoring_uptime_check_create-console) are disabled for IL4 folders and [BigQuery's remote functions](https://docs.cloud.google.com/assured-workloads/docs/control-packages/itar#features_bigquery) are disabled for ITAR folders; if your source project uses such disabled features, these incompatibilities are not analyzed or reported.



### Analyzing moving a project to an Assured Workloads folder

The [`analyzeWorkloadMove`](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads/analyzeWorkloadMove) method performs an analysis of moving the source project to the destination Assured Workloads folder.

In the request example below, replace the following parameters with your own:

  * ENDPOINT_URI: The Assured Workloads [service endpoint URI](https://docs.cloud.google.com/assured-workloads/docs/reference/rest#rest_endpoints). This URI must be the endpoint matching the location of the destination workload, such as `https://us-west1-assuredworkloads.googleapis.com` for a regionalized workload in the `us-west1` region and `https://us-assuredworkloads.googleapis.com` for a multi-region workload in the US.
  * DESTINATION_ORGANIZATION_ID: The organization ID for the destination workload to which the source project will be migrated. For example: `919698201234`
  * DESTINATION_LOCATION_ID: The location of the destination workload. For example: `us-west1` or `us`. It corresponds to the `data region` value of the workload.
  * DESTINATION_WORKLOAD_ID: The ID of the destination Assured Workloads folder where the source project will be migrated. For example: `00-701ea036-7152-4780-a867-9f5`
  * SOURCE_PROJECT_ID: Query parameter for the ID of the source project to be migrated. For example: `my-project-123`
  * ASSET_TYPES: Optional. One [asset type](https://docs.cloud.google.com/asset-inventory/docs/supported-asset-types) per query parameter that will filter the findings to only the specified type(s). For example: `cloudresourcemanager.googleapis.com/Project`
  * PAGE_SIZE: Optional. Query parameter for the number of results to return per page, up to a maximum of 50. For example: `5`
  * PAGE_TOKEN: Optional. Query parameter for the token to continue paginated results. For example: `CiAKGjBpNDd2Nmp2Zml2cXRwYjBpOXA`



HTTP method, URL, and query parameters: 
    
    
    GET https://[ENDPOINT_URI]/v1/organizations/[DESTINATION_ORGANIZATION_ID]/locations/[DESTINATION_LOCATION_ID]/workloads/[DESTINATION_WORKLOAD_ID]:analyzeWorkloadMove?project=projects/SOURCE_PROJECT_ID&page_size=PAGE_SIZE&page_token=PAGE_TOKEN

For example: 
    
    
    GET https://us-west1-assuredworkloads.googleapis.com/v1/organizations/919698298765/locations/us-west1/workloads/00-701ea036-7152-4781-a867-9f5:analyzeWorkloadMove?project=projects/my-project-123&page_size=5&page_token=CiAKGjBpNDd2Nmp2Zml2cXRwYjBpOXA

You should receive a JSON response similar to the following:
    
    
    {
      "assetMoveAnalyses": [
        {
          "asset": "//orgpolicy.googleapis.com/projects/130536381852/policies/container.restrictNoncompliantDiagnosticDataAccess",
          "assetType": "orgpolicy.googleapis.com/Policy"
        },
        {
          "asset": "//compute.googleapis.com/projects/my-project-123/global/routes/default-route-9ca6e6b0ab7326f0",
          "assetType": "compute.googleapis.com/Route",
          "analysisGroups": [
            {
              "displayName": "RESOURCE_LOCATIONS",
              "analysisResult": {
                "warnings": [
                  {
                    "detail": "The asset's location 'global' is incompatible with the gcp.resourceLocations org policy effective at the target. In case of 'global only' assets, this may be ignored."
                  }
                ]
              }
            }
          ]
        },
        {
          "asset": "//compute.googleapis.com/projects/my-project-123/regions/europe-west10/subnetworks/default",
          "assetType": "compute.googleapis.com/Subnetwork",
          "analysisGroups": [
            {
              "displayName": "RESOURCE_LOCATIONS",
              "analysisResult": {
                "blockers": [
                  {
                    "detail": "The asset's location 'europe-west10' is incompatible with the gcp.resourceLocations org policy effective at the target."
                  }
                ]
              }
            }
          ]
        },
        {
          "asset": "//serviceusage.googleapis.com/projects/130536381852/services/servicemanagement.googleapis.com",
          "assetType": "serviceusage.googleapis.com/Service"
        },
        {
          "asset": "//serviceusage.googleapis.com/projects/130536381852/services/monitoring.googleapis.com",
          "assetType": "serviceusage.googleapis.com/Service"
        },
        {
          "asset": "//serviceusage.googleapis.com/projects/130536381852/services/bigquerymigration.googleapis.com",
          "assetType": "serviceusage.googleapis.com/Service",
          "analysisGroups": [
            {
              "displayName": "DISALLOWED_SERVICES",
              "analysisResult": {
                "warnings": [
                  {
                    "detail": "This service is not allowed by the gcp.restrictServiceUsage org policy effective at the target"
                  }
                ]
              }
            }
          ]
        },
        {
          "asset": "//cloudresourcemanager.googleapis.com/projects/my-project-123",
          "assetType": "cloudresourcemanager.googleapis.com/Project",
          "analysisGroups": [
            {
              "displayName": "ORG_POLICIES",
              "analysisResult": {
                "warnings": [
                  {
                    "detail": "constraints/gcp.resourceLocations: Target applies/inherits this custom policy and it is not applied by the source. Upon moving, this policy will get inherited from the target."
                  },
                  {
                    "detail": "constraints/compute.disableInstanceDataAccessApis: Source applies this custom policy and it is not applied by the target."
                  },
                  {
                    "detail": "constraints/cloudkms.allowedProtectionLevels: Source and target set different values for this policy."
                  },
                  {
                    "detail": "constraints/container.restrictNoncompliantDiagnosticDataAccess: Source and target set different values for this policy."
                  },
                  {
                    "detail": "constraints/gcp.restrictServiceUsage: Target applies/inherits this custom policy and it is not applied by the source. Upon moving, this policy will get inherited from the target."
                  }
                ],
                "blockers": [
                  {
                    "detail": "constraints/gcp.resourceLocations: The value applied at the source is not compliant with the target compliance program. The expected allowed values are [us-west4, us-west1, us-west2, us-west3, us-central1, us-east1, us-east4, us-south1, us-central2, us-east5]."
                  },
                  {
                    "detail": "constraints/container.restrictNoncompliantDiagnosticDataAccess: The value applied at the source is not compliant with the target compliance program. The expected value is [true]."
                  },
                  {
                    "detail": "constraints/container.restrictTLSVersion: The value applied at the source is not compliant with the target compliance program. The expected denied values are [TLS_VERSION_1, TLS_VERSION_1_1]."
                  }
                ]
              }
            }
          ]
        }
      ],
      "nextPageToken": "Ch8wLDc0MzY3NTExNCwzMzg4ODM1NTM2NDQ0NTg4MDMy"
    }

To filter the findings by a specific asset type, use the `asset_types` query parameter:
    
    
    GET https://assuredworkloads.googleapis.com/v1/organizations/919698298765/locations/us-west1/workloads/00-701ea036-7152-4781-a867-9f5:analyzeWorkloadMove?project=projects/my-project-123&asset_types=cloudresourcemanager.googleapis.com/Project&page_size=5&page_token=CiAKGjBpNDd2Nmp2Zml2cXRwYjBpOXA

The results will only contain any findings of the specified type (`cloudresourcemanager.googleapis.com/Project`):
    
    
    {
      "assetMoveAnalyses": [
        {
          "asset": "//cloudresourcemanager.googleapis.com/projects/my-project-123",
          "assetType": "cloudresourcemanager.googleapis.com/Project",
          "analysisGroups": [
            {
              "displayName": "ORG_POLICIES",
              "analysisResult": {
                "warnings": [
                  {
                    "detail": "constraints/gcp.resourceLocations: Target applies/inherits this custom policy and it is not applied by the source. Upon moving, this policy will get inherited from the target."
                  },
                  {
                    "detail": "constraints/compute.disableInstanceDataAccessApis: Source applies this custom policy and it is not applied by the target."
                  }
                ],
                "blockers": [
                  {
                    "detail": "constraints/gcp.resourceLocations: The value applied at the source is not compliant with the target compliance program. The expected allowed values are [us-west4, us-west1, us-west2, us-west3, us-central1, us-east1, us-east4, us-south1, us-central2, us-east5]."
                  }
                ]
              }
            }
          ]
        }
      ],
      "nextPageToken": "Ch8wLDc0MzY3NTExNCwzMzg4ODM1NTM2NDQ0NTg4MDMy"
    }

To filter the findings by more than one asset type, add each as an additional query parameter:
    
    
    GET https://assuredworkloads.googleapis.com/v1/organizations/919698298765/locations/us-west1/workloads/00-701ea036-7152-4781-a867-9f5:analyzeWorkloadMove?project=projects/my-project-123&asset_types=cloudresourcemanager.googleapis.com/Project&asset_types=serviceusage.googleapis.com/Service&page_size=5&page_token=CiAKGjBpNDd2Nmp2Zml2cXRwYjBpOXA

The results will only contain any findings of the specified types (`cloudresourcemanager.googleapis.com/Project` and `serviceusage.googleapis.com/Service`):
    
    
    {
      "assetMoveAnalyses": [
        {
          "asset": "//serviceusage.googleapis.com/projects/130536381852/services/bigquerymigration.googleapis.com",
          "assetType": "serviceusage.googleapis.com/Service",
          "analysisGroups": [
            {
              "displayName": "DISALLOWED_SERVICES",
              "analysisResult": {
                "warnings": [
                  {
                    "detail": "This service is not allowed by the gcp.restrictServiceUsage org policy effective at the target"
                  }
                ]
              }
            }
          ]
        },
        {
          "asset": "//cloudresourcemanager.googleapis.com/projects/my-project-123",
          "assetType": "cloudresourcemanager.googleapis.com/Project",
          "analysisGroups": [
            {
              "displayName": "ORG_POLICIES",
              "analysisResult": {
                "warnings": [
                  {
                    "detail": "constraints/gcp.resourceLocations: Target applies/inherits this custom policy and it is not applied by the source. Upon moving, this policy will get inherited from the target."
                  },
                  {
                    "detail": "constraints/compute.disableInstanceDataAccessApis: Source applies this custom policy and it is not applied by the target."
                  }
                ],
                "blockers": [
                  {
                    "detail": "constraints/gcp.resourceLocations: The value applied at the source is not compliant with the target compliance program. The expected allowed values are [us-west4, us-west1, us-west2, us-west3, us-central1, us-east1, us-east4, us-south1, us-central2, us-east5]."
                  }
                ]
              }
            }
          ]
        }
      ],
      "nextPageToken": "Ch8wLDc0MzY3NTExNCwzMzg4ODM1NTM2NDQ0NTg4MDMy"
    }

After you have performed the migration analysis, review and resolve any warnings or blockers, and then run the analysis again to verify that they have been addressed. Then, you can proceed with [moving the project](https://docs.cloud.google.com/resource-manager/docs/moving-projects-folders).

## What's next

  * Understand Assured Workloads' [control packages](https://docs.cloud.google.com/assured-workloads/docs/control-packages).
  * Learn which [products are supported](https://docs.cloud.google.com/assured-workloads/docs/supported-products) for each control package.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
