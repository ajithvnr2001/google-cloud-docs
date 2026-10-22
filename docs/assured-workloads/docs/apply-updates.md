---
url: https://docs.cloud.google.com/assured-workloads/docs/apply-updates/
title: Apply workload updates \u00a0|\u00a0 Assured Workloads \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:36:12.516608+00:00
---

# Apply workload updates  |  Assured Workloads  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/docs/apply-updates/

The names for some Assured Workloads control packages have changed. For information about the name change, see [Control package renaming notice](https://docs.cloud.google.com/assured-workloads/docs/overview#name-change). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-workloads/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Apply workload updates

This page describes how to enable, view, and apply workload updates for Assured Workloads folders. Assured Workloads regularly updates its [control packages](https://docs.cloud.google.com/assured-workloads/docs/control-packages) with new settings and general improvements, such as updated organization policy constraint values. This feature lets you evaluate your current Assured Workloads folder configuration against the latest available configuration, and choose to apply any proposed updates.

By default, this feature is automatically enabled for new Assured Workloads folders. For existing folders, we strongly recommend that you follow the steps to enable workload updates.

**Important:** If you choose not to enable workload updates for existing folders, you won't be automatically notified when new updates are available for your workloads, nor be able to update their configuration.

This feature does not incur any additional charges, nor does it affect the behavior of [Assured Workloads monitoring](https://docs.cloud.google.com/assured-workloads/docs/monitor-folder); you will still be alerted when your folder falls out of compliance with its current configuration, regardless of whether updates to its configuration are available.

### Workload updates overview

When you create a new Assured Workloads folder, the [control package type](https://docs.cloud.google.com/assured-workloads/docs/control-packages) you select—such as FedRAMP Moderate—determines the various configuration settings that are applied on your workload. Some of these settings are externally visible in the form of organization policy constraints, although others are only applicable to Google's internal systems. Assured Workloads uses an internal configuration versioning system to maintain changes for each control package type.

When a new internal configuration version becomes available, Assured Workloads compares your workload's configuration to the new internal version. Any differences are analyzed, and the resulting enhancements become available as an update that you can apply to your workload's configuration. When such enhancements include support for a new service, any organization policy constraints required for that service might also be applied on your workload.

Available Assured Workloads updates have been verified by Google to be compliant with the requirements of your workload's control package. However, it's still your responsibility to review each available update to verify that it meets your organization's regulatory or compliance requirements. See [Shared responsibility in Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/shared-responsibility) for more information.

**Note:** If a workload update becomes available, but you choose to manually change your workload's organization policy before applying that update, you will be unable to apply it. To apply the update, you either must restore the previous organization policy settings (prior to your manual changes), or wait until the next workload update becomes available. In this scenario, we recommend that you restore your previous organization policy settings and apply the workload update, since a new update might not be available for some time.

### Supported update types

This feature supports viewing and applying the following types of updates on an Assured Workloads folder:

  * **Organization policy constraints** : Any organization policy constraints that are applicable to your workload and enforced by Assured Workloads can be included in a workload update, with the following exceptions:

    * `gcp.resourceLocations`
    * `gcp.restrictCmekCryptoKeyProjects`
**Note:** `gcp.restrictServiceUsage` updates are available in the Google Cloud console but are not available when using the Assured Workloads API. For example, you won't receive `gcp.restrictServiceUsage` updates when calling the `updates` method as described in the View workload updates section.
  * **Control package launch stages** : This feature only supports viewing and applying updates when a given [control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages) is in the same [launch stage](https://cloud.google.com/products#product-launch-stages) as when you first deployed it. For example, if you deploy a workload for a control package when it's in the Preview launch stage and that control package later becomes generally available, you must first redeploy your workload using the GA version before you can apply updates. If you don't redeploy your workload, you may encounter errors or compliance violations after attempting to apply updates.




## Before you begin

  * Identify the resource IDs for the Assured Workloads folders for which to enable updates.
  * Assign or verify IAM permissions on the target Assured Workloads folders and workloads.



### Required IAM permissions

To enable, view, or apply workload updates, the caller must be granted IAM permissions using either a [predefined role](https://docs.cloud.google.com/iam/docs/roles-permissions) that includes a wider set of permissions, or a [custom role](https://docs.cloud.google.com/iam/docs/roles-overview#custom) that is restricted to the minimum necessary permissions. Note that the required `orgpolicy.policy.set` permission is unavailable for use in custom roles.

The following permissions are required:

  * `assuredworkloads.workload.update` on the target workload to enable updates. This permission is included in the [Assured Workloads Editor (`roles/assuredworkloads.editor`)](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.editor) and [Assured Workloads Admin (`roles/assuredworkloads.admin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.admin) predefined roles.
  * `assuredworkloads.updates.list` on the target workload to view available updates. This permission is included in the [Assured Workloads Reader (`roles/assuredworkloads.reader`)](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.reader), [Assured Workloads Editor (`roles/assuredworkloads.editor`)](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.editor), and [Assured Workloads Admin (`roles/assuredworkloads.admin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.admin) predefined roles.
  * `assuredworkloads.updates.update` on the target workload to apply available updates. This permission is included in the [Assured Workloads Editor (`roles/assuredworkloads.editor`)](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.editor), and [Assured Workloads Admin (`roles/assuredworkloads.admin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.admin) predefined roles.
  * `assuredworkloads.operations.get` on the target workload to get the status and results of an update operation. This permission is included in the [Assured Workloads Reader (`roles/assuredworkloads.reader`)](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.reader), [Assured Workloads Editor (`roles/assuredworkloads.editor`)](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.editor), and [Assured Workloads Admin (`roles/assuredworkloads.admin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.admin) predefined roles.
  * `orgpolicy.policy.get` on the target folder to apply available updates. This permission is included in the [Organization Policy Viewer (`roles/orgpolicy.policyViewer`)](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyViewer) and [Organization Policy Administrator (`roles/orgpolicy.policyAdmin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) predefined roles.
  * `orgpolicy.policy.set` on the target folder to apply available updates. This permission is not supported in custom roles, but it's included in the [Organization Policy Administrator (`roles/orgpolicy.policyAdmin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) predefined role.
  * `resourcemanager.folders.getIamPolicy` and `resourcemanager.folders.setIamPolicy`on the target folder to enable updates. These permissions are included in the [Folder IAM Admin (`roles/resourcemanager.folderIamAdmin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.folderIamAdmin) role and other highly permissive predefined roles.



## Enable workload updates

When you enable workload updates, the [Assured Workloads Service Agent](https://docs.cloud.google.com/iam/docs/service-agents#assured-workloads-service-agent) is created. This service agent is then granted the [**Assured Workloads Service Agent** (`roles/assuredworkloads.serviceAgent`)](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.serviceAgent) role on the target Assured Workloads folder. This role enables the service agent to check for any available updates on the folder.

To enable workload updates, complete the following steps:

###  Console 

  1. In the Google Cloud console, go to the **Assured Workloads** page.

[Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

  2. At the top of the page in the **Introducing Compliance Updates** pane, click **Enable compliance updates**.

  3. When prompted to **Enable compliance updates?** , click **Enable**.




Workload updates are now enabled for all Assured Workloads folders in your organization.

###  REST 

The [`enableComplianceUpdates`](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads/enableComplianceUpdates) method enables Assured Workloads to notify you of updates for a single Assured Workloads folder.

HTTP method, URL, and query parameters: 
    
    
    PUT https://[ENDPOINT_URI]/v1/organizations/[ORGANIZATION_ID]/locations/[LOCATION_ID]/workloads/[WORKLOAD_ID]:enableComplianceUpdates

Replace the following placeholder values with your own:

  * ENDPOINT_URI: The Assured Workloads [service endpoint URI](https://docs.cloud.google.com/assured-workloads/docs/reference/rest#rest_endpoints). This URI must be the endpoint matching the location of the destination workload, such as `https://us-west1-assuredworkloads.googleapis.com` for a regionalized workload in the `us-west1` region and `https://us-assuredworkloads.googleapis.com` for a multi-region workload in the US.
  * ORGANIZATION_ID: The organization ID for the Assured Workloads folder—for example, `919698201234`.
  * LOCATION_ID: The location of the Assured Workloads folder—for example, `us-west1` or `us`. It corresponds to the `data region` value of the workload.
  * WORKLOAD_ID: The ID of the Assured Workloads workload for which to enable updates—for example, `00-701ea036-7152-4780-a867-9f5`.



For example: 
    
    
    PUT https://us-west1-assuredworkloads.googleapis.com/v1/organizations/919698298765/locations/us-west1/workloads/00-701ea036-7152-4781-a867-9f5:enableComplianceUpdates

## View workload updates

To view workload updates, complete the following steps:

###  Console 

  1. In the Google Cloud console, go to the **Assured Workloads** page.

[Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

  2. In the **Name** column, click the name of the Assured Workloads folder for which you want to view updates. Alternatively, if updates are available for the folder, click the link in the **Updates** column.

  3. Under **Available updates** , click **Review available updates**.

  4. If available, organization policy updates are shown in the **Organization policy** tab. Review the affected organization policy constraint and click **View update** to preview the constraint settings that will be applied by the update.

**Note:** If `gcp.restrictServiceUsage` updates are available, any required service-specific organization policy constraints for a service won't appear in the list of available updates. However, if you choose to apply a `gcp.restrictServiceUsage` update, these required constraints (such as `compute.disableGlobalCloudArmorPolicy` for EU Data Boundary) will be applied to your workload.



###  REST 

The [`organizations.locations.workloads.updates.list`](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads.updates/list) method lists available updates for an Assured Workloads workload.

HTTP method, URL, and query parameters: 
    
    
    GET https://[ENDPOINT_URI]/v1/organizations/[ORGANIZATION_ID]/locations/[LOCATION_ID]/workloads/[WORKLOAD_ID]/updates?page_size=[PAGE_SIZE]&page_token=[PAGE_TOKEN]

Replace the following placeholder values with your own:

  * ENDPOINT_URI: The Assured Workloads [service endpoint URI](https://docs.cloud.google.com/assured-workloads/docs/reference/rest#rest_endpoints). This URI must be the endpoint matching the location of the destination workload, such as `https://us-central1-assuredworkloads.googleapis.com` for a regionalized workload in the `us-central1` region and `https://us-assuredworkloads.googleapis.com` for a multi-region workload in the US.
  * ORGANIZATION_ID: The organization ID for the Assured Workloads folder—for example, `919698201234`.
  * LOCATION_ID: The location of the Assured Workloads folder—for example, `us-central1` or `us`. It corresponds to the `data region` value of the workload.
  * WORKLOAD_ID: The ID of the Assured Workloads workload for which to list available updates—for example, `00-701ea036-7152-4780-a867-9f5`.
  * PAGE_SIZE (Optional): Limits the number of updates to return in the response. If unspecified, the default value is set to `20`. The maximum value is `100`.
  * PAGE_TOKEN (Optional): When one or more pages are available, a token for the next page is returned in the JSON response—for example, `nextPageToken": "chEKD4IBDAid1e-3BhCo68f6AQ`. If unspecified, no subsequent pages will be returned.



For example: 
    
    
    GET https://us-central1-assuredworkloads.googleapis.com/v1/organizations/919698298765/locations/us-west1/workloads/00-701ea036-7152-4781-a867-9f5/updates

If successful, you will receive a JSON response similar to the following example: 
    
    
    {
      "workloadUpdates": [
        {
          "name": "organizations/919698298765/locations/us-central1/workloads/00-701ea036-7152-4781-a867-9f5/updates/5320de45-6c98-41af-b4a0-2ef930b124c3",
          "state": "AVAILABLE",
          "createTime": "2024-10-01T16:33:10.154368Z",
          "updateTime": "2024-10-01T16:33:10.154368Z",
          "details": {
            "orgPolicyUpdate": {
              "appliedPolicy": {
                "resource": "folders/376585579673",
                "constraint": "constraints/gcp.resourceLocations",
                "rule": {
                  "values": {
                    "allowedValues": [
                      "us-central1",
                    ]
                  }
                }
              },
              "suggestedPolicy": {
                "resource": "folders/376585579673",
                "constraint": "constraints/gcp.resourceLocations",
                "rule": {
                  "values": {
                    "allowedValues": [
                      "us-central1",
                      "us-central2",
                      "us-west1",
                    ]
                  }
                }
              }
            }
          }
        }
      ],
      "nextPageToken": "chEKD4IBDAid1e-3BhCo68f6AQ"
    }

## Apply workload updates

Applying a workload update to a workload is a long-running operation. If your workload configuration changes after starting the operation and before it's complete, an error might occur.

Additionally, workload updates are periodically re-evaluated against the latest available configuration. In this case, additional updates might be available immediately after you've applied an update.

To apply workload updates, complete the following steps:

###  Console 

  1. In the Google Cloud console, go to the **Assured Workloads** page.

[Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

  2. In the **Name** column, click the name of the Assured Workloads folder for which you want to view updates. Alternatively, if updates are available for the folder, click the link in the **Updates** column.

  3. Under **Available updates** , click **Review available updates**.

  4. If available, organization policy updates are shown in the **Organization policy** tab. Review the affected organization policy constraint and click **View update** to preview the updated constraint settings.

**Note:** If `gcp.restrictServiceUsage` updates are available, any required service-specific organization policy constraints for a service won't appear in the list of available updates. However, if you choose to apply a `gcp.restrictServiceUsage` update, these required constraints (such as `compute.disableGlobalCloudArmorPolicy` for EU Data Boundary) will be applied to your workload.
  5. Click **Update organization policy** to apply the update.




The long-running update operation starts, and the folder's new organization policy settings will be applied.

###  REST 

The [`organizations.locations.workloads.updates.apply`](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads.updates/apply) method applies the specified update for an Assured Workloads workload.

HTTP method, URL, and query parameters: 
    
    
    POST https://[ENDPOINT_URI]/v1/organizations/[ORGANIZATION_ID]/locations/[LOCATION_ID]/workloads/[WORKLOAD_ID]/updates/[UPDATE_ID]:apply

Replace the following placeholder values with your own:

  * ENDPOINT_URI: The Assured Workloads [service endpoint URI](https://docs.cloud.google.com/assured-workloads/docs/reference/rest#rest_endpoints). This URI must be the endpoint matching the location of the destination workload, such as `https://us-central1-assuredworkloads.googleapis.com` for a regionalized workload in the `us-central1` region and `https://us-assuredworkloads.googleapis.com` for a multi-region workload in the US.
  * ORGANIZATION_ID: The organization ID for the Assured Workloads folder—for example, `919698201234`.
  * LOCATION_ID: The location of the Assured Workloads folder—for example, `us-central1` or `us`. It corresponds to the `data region` value of the workload.
  * WORKLOAD_ID: The ID of the Assured Workloads workload for which to list available updates—for example, `00-701ea036-7152-4780-a867-9f5`.
  * UPDATE_ID: The ID of the update to apply, selected from the list of available updates returned by the [`organizations.locations.workloads.updates.list`](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads.updates/list) method—for example, `edb84871-833b-45ec-9c00-c9b5c19d2d87`.



Request body: 
    
    
    {
      "name":"organizations/[ORGANIZATION_ID]/locations/[LOCATION_ID]/workloads/[WORKLOAD_ID]/updates/[UPDATE_ID]",
      "action": "APPLY"
    }

For example: 
    
    
    POST https://us-central1-assuredworkloads.googleapis.com/v1/organizations/919698298765/locations/us-central1/workloads/00-701ea036-7152-4781-a867-9f5/updates/edb84871-833b-45ec-9c00-c9b5c19d2d87:apply
    
    
    {
      "name": "organizations/919698298765/locations/us-central1/workloads/00-701ea036-7152-4781-a867-9f5/updates/edb84871-833b-45ec-9c00-c9b5c19d2d87",
      "action": "APPLY"
    }

If successful, you will receive a JSON response similar to the following example: 
    
    
    {
      "name": "organizations/919698298765/locations/us-central1/operations/647b1c77-b9a5-45d2-965e-70a1e867fe5b",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.assuredworkloads.v1.ApplyWorkloadUpdateOperationMetadata",
        "update_name": "organizations/919698298765/locations/us-central1/workloads/00-701ea036-7152-4781-a867-9f5/updates/edb84871-833b-45ec-9c00-c9b5c19d2d87",
        "create_time": "2024-10-01T14:34:30.290896Z",
        "action": "APPLY"
      }
    }

To get the status of a long-running update operation, use the operation ID in the `name` value from the JSON response. Using the previous example, the operation ID is `647b1c77-b9a5-45d2-965e-70a1e867fe5b`. Then make the following request, replacing the placeholder values with your own:
    
    
    GET https://[ENDPOINT_URI]/v1/organizations/[ORGANIZATION_ID]/locations/[LOCATION_ID]/operations/[OPERATION_ID]

For example: 
    
    
    GET https://us-central1-assuredworkloads.googleapis.com/v1/organizations/919698298765/locations/us-central1/operations/647b1c77-b9a5-45d2-965e-70a1e867fe5b

If successful, you will receive a JSON response similar to the following example: 
    
    
    {
      "name": "organizations/919698298765/locations/us-central1/operations/647b1c77-b9a5-45d2-965e-70a1e867fe5b",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.assuredworkloads.v1.ApplyWorkloadUpdateOperationMetadata",
        "updateName": "organizations/919698298765/locations/us-central1/workloads/00-701ea036-7152-4781-a867-9f5/updates/edb84871-833b-45ec-9c00-c9b5c19d2d87",
        "createTime": "2024-10-01T13:33:09Z"
        "action": "APPLY"
      },
      "done": true
      "response": {
        "@type": "type.googleapis.com/google.cloud.assuredworkloads.v1.ApplyWorkloadUpdateResponse",
        "appliedUpdate": {
          "name": "organizations/531459884741/locations/us-central1/workloads/00-0b328e90-da70-431e-befc-a4a/updates/db556beb-ce66-4260-bd3b-28115f1ec300",
          "state": "APPLIED",
          "createTime": "2024-10-01T14:31:24.310323Z",
          "updateTime": "2024-10-01T14:34:30.855792Z",
          "details": {
            "orgPolicyUpdate": {
              "appliedPolicy": {
                "resource": "folders/196232301850",
                "constraint": "constraints/compute.disableInstanceDataAccessApis",
                "rule": {
                  "enforce": true
                }
              },
              "suggestedPolicy": {
                "resource": "folders/196232301850",
                "constraint": "constraints/compute.disableInstanceDataAccessApis",
                "rule": {
                  "enforce": false
                }
              }
            }
          }
        }
      }
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
