---
url: https://docs.cloud.google.com/asset-inventory/docs/asset-insights/
title: Improve your security posture with asset insights \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:41:38.526688+00:00
---

# Improve your security posture with asset insights  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/asset-insights/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Guides ](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview)



Send feedback 

#  Improve your security posture with asset insights Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Asset Inventory insights can help to detect potential risks in your asset configurations, and help you to improve your security posture. It's part of the [Recommender](https://docs.cloud.google.com/recommender/docs) service, and is provided as the `google.cloudasset.asset.Insight` insight type.

Insights are specific anomalies which require further analysis to determine appropriate action. They are generated daily, based on a snapshot of the data stored in Cloud Asset Inventory.

The [insights](https://docs.cloud.google.com/recommender/docs/insights/using-insights) provided by Cloud Asset Inventory are based on the IAM policies associated with your organization's resources.

## Before you begin

Before you can begin using asset insights, you must complete the following steps.

  1. [Enable the Recommender API](https://docs.cloud.google.com/recommender/docs/enable-api).

  2. Make sure that your account has the following permissions:

     * `recommender.cloudAssetInsights.get`

     * `recommender.cloudAssetInsights.list`

     * `recommender.cloudAssetInsights.update`

You can grant these permissions individually, or you can grant one of the following roles.

     * Cloud Asset Insights Viewer (`roles/recommender.cloudAssetInsightsViewer`) role

     * Cloud Asset Insights Admin (`roles/recommender.cloudAssetInsightsAdmin`) role




## Limitations

  * These insights don't consider group memberships or service accounts as part of their findings, and shouldn't be considered an exhaustive list of matching vulnerabilities.

  * Individual insights include a sampling of matching IAM policies capped at 100 distinct policies. All matching policies can be retrieved by [searching for IAM allow policies on resources](https://docs.cloud.google.com/asset-inventory/docs/search-allow-policies).




## Request asset insights

The easiest way to request asset insights is to list them, as shown in the following steps. For other types of insights interactions, see [Use the API - Insights](https://docs.cloud.google.com/recommender/docs/insights/using-api).

#### gcloud
    
    
    gcloud recommender insights list \
        --SCOPE \
        --location=global \
        --insight-type=google.cloudasset.asset.Insight \
        --filter="insightSubtype:SUBTYPE" \

Provide the following values:

  * `SCOPE`: Use one of the following values:

    * `project=PROJECT_ID`, where `PROJECT_ID` is the ID of the project you want insights for. 
    * `folder=FOLDER_ID`, where `FOLDER_ID` is the ID of the folder you want insights for. 

How to find the ID of a Google Cloud folder

### Google Cloud console

To find the ID of a Google Cloud folder, complete the following steps:

      1. Go to the Google Cloud console.

[ Go to the Google Cloud console ](https://console.cloud.google.com/)

      2. Click the **switcher** list box in the menu bar.
      3. Select your organization from the list box.
      4. Search for your folder name. The folder ID is shown next to the folder name.

### gcloud CLI

You can retrieve the ID of a Google Cloud folder that's located at the organization level with the following command:
    
    gcloud resource-manager folders list \
        --organization=$(gcloud organizations describe ORGANIZATION_NAME \
          --format="value(name.segment(1))") \
        --filter='"DISPLAY_NAME":"TOP_LEVEL_FOLDER_NAME"' \
        --format="value(ID)"

Where TOP_LEVEL_FOLDER_NAME is a partial or full string match for the folder's name. Remove the `--format` flag to see more information about the found folders.

The previous command doesn't return the IDs of subfolders within folders. To do so, run the following command using a top level folder's ID:
    
    gcloud resource-manager folders list --folder=FOLDER_ID

    * `organization=ORGANIZATION_ID`, where `ORGANIZATION_ID` is the ID of the organization you want insights for. 

How to find the ID of a Google Cloud organization

### Google Cloud console

To find the ID of a Google Cloud organization, complete the following steps:

      1. Go to the Google Cloud console.

[ Go to the Google Cloud console ](https://console.cloud.google.com/)

      2. Click the **switcher** list box in the menu bar.
      3. Select your organization from the list box.
      4. Click the **All** tab. The organization ID is shown next to the organization name.

### gcloud CLI

You can retrieve the ID of a Google Cloud organization with the following command:
    
    gcloud organizations describe ORGANIZATION_NAME --format="value(name.segment(1))"

  * `BILLING_PROJECT_ID`: Optional. The project ID that the default Cloud Asset Inventory service agent is in that has permissions to manage your billing and quota. [ Read more about setting the billing project](https://docs.cloud.google.com/asset-inventory/docs/multiple-projects#orchestrator). 
  * `SUBTYPE`: The asset insight subtype. One of the following values:

    * `EXTERNAL_MEMBER`: Detects IAM policies that contain users or groups that belong to a domain outside of your organization's domains. 
    * `EXTERNAL_POLICY_EDITOR`: Detects IAM policies that contain users or groups outside of your organization's domains that are granted permission to modify IAM policies. 
    * `EXTERNAL_CLOUD_STORAGE_OBJECT_VIEWER`: Detects IAM policies that contain users or groups outside of your organization's domains that are granted permission to get or list storage objects (`storage.objects.list` or `storage.objects.get` permission). 
    * `EXTERNAL_SERVICE_ACCOUNT_IMPERSONATOR`: Detects IAM policies that contain users or groups outside of your organization's domains that are granted permission to impersonate service accounts. 
    * `TERMINATED_MEMBER`: Detects IAM policies that contain users or groups with deactivated, deleted, or purged accounts. 
    * `PUBLIC_IAM_POLICY`: Detects IAM policies that contain all users or all authenticated users. 
    * `OWNER_TERMINATED_PROJECT`: Detects projects which do not contain any active users or groups in the project's IAM policy. 

If not specified, all subtypes are returned.




See the [gcloud CLI reference](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/list) for all options. 

### Example

Run the following command to list insights for the `my-project` project.
    
    
    gcloud recommender insights list \
        --project=**my-project** \
        --location=global \
        --insight-type=google.cloudasset.asset.Insight

#### Example response
    
    
    INSIGHT_ID: 00000000-0000-0000-0000-000000000000
    CATEGORY: SECURITY
    INSIGHT_STATE: ACTIVE
    LAST_REFRESH_TIME: 2024-01-30T00:00:00Z
    SEVERITY: LOW
    INSIGHT_SUBTYPE: EXTERNAL_MEMBER
    DESCRIPTION: Domain example.com detected in 1 IAM policies
    

#### REST

HTTP method and URL:
    
    
    GET https://recommender.googleapis.com/v1/SCOPE_PATH/locations/global/insightTypes/google.cloudasset.asset.Insight/insights
    

Headers:
    
    
    X-Goog-User-Project: BILLING_PROJECT_ID

Provide the following values:

  * `SCOPE_PATH`: Use one of the following values:

    * `projects/PROJECT_ID`, where `PROJECT_ID` is the ID of the project you want insights for. 
    * `projects/PROJECT_NUMBER`, where `PROJECT_NUMBER` is the number of the project you want insights for. 

How to find a Google Cloud project number

### Google Cloud console

To find a Google Cloud project number, complete the following steps:

      1. Go to the **Welcome** page in the Google Cloud console.

[ Go to Welcome](https://console.cloud.google.com/welcome)

      2. Click the **switcher** list box in the menu bar.
      3. Select your organization from the list box, and then search for your project name. The project name, project number, and project ID are shown near the **Welcome** heading. 

Up to 4,000 resources are displayed. If you don't see the project you're looking for, go to the [**Manage resources**](https://console.cloud.google.com//cloud-resource-manager) page and filter the list using the name of that project. 

### gcloud CLI

You can retrieve a Google Cloud project number with the following command:
    
    gcloud projects describe PROJECT_ID --format="value(projectNumber)"

    * `folders/FOLDER_ID`, where `FOLDER_ID` is the ID of the folder you want insights for. 

How to find the ID of a Google Cloud folder

### Google Cloud console

To find the ID of a Google Cloud folder, complete the following steps:

      1. Go to the Google Cloud console.

[ Go to the Google Cloud console ](https://console.cloud.google.com/)

      2. Click the **switcher** list box in the menu bar.
      3. Select your organization from the list box.
      4. Search for your folder name. The folder ID is shown next to the folder name.

### gcloud CLI

You can retrieve the ID of a Google Cloud folder that's located at the organization level with the following command:
    
    gcloud resource-manager folders list \
        --organization=$(gcloud organizations describe ORGANIZATION_NAME \
          --format="value(name.segment(1))") \
        --filter='"DISPLAY_NAME":"TOP_LEVEL_FOLDER_NAME"' \
        --format="value(ID)"

Where TOP_LEVEL_FOLDER_NAME is a partial or full string match for the folder's name. Remove the `--format` flag to see more information about the found folders.

The previous command doesn't return the IDs of subfolders within folders. To do so, run the following command using a top level folder's ID:
    
    gcloud resource-manager folders list --folder=FOLDER_ID

    * `organizations/ORGANIZATION_ID`, where `ORGANIZATION_ID` is the ID of the organization you want insights for. 

How to find the ID of a Google Cloud organization

### Google Cloud console

To find the ID of a Google Cloud organization, complete the following steps:

      1. Go to the Google Cloud console.

[ Go to the Google Cloud console ](https://console.cloud.google.com/)

      2. Click the **switcher** list box in the menu bar.
      3. Select your organization from the list box.
      4. Click the **All** tab. The organization ID is shown next to the organization name.

### gcloud CLI

You can retrieve the ID of a Google Cloud organization with the following command:
    
    gcloud organizations describe ORGANIZATION_NAME --format="value(name.segment(1))"

  * `BILLING_PROJECT_ID`: The project ID that the default Cloud Asset Inventory service agent is in that has permissions to manage your billing and quota. [ Read more about setting the billing project](https://docs.cloud.google.com/asset-inventory/docs/multiple-projects#orchestrator). 



### Command examples

Run on of the following commands to list insights for the `my-project` project.

#### curl (Linux, macOS, or Cloud Shell)

**Note** : The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login), or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the gcloud CLI. You can check the active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    curl -X GET \
         -H "X-Goog-User-Project: BILLING_PROJECT_ID" \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         https://recommender.googleapis.com/v1/projects/**my-project** /locations/global/insightTypes/google.cloudasset.asset.Insight/insights

#### PowerShell (Windows)

**Note** : The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [ `gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login). You can check the active account by running [ `gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    $cred = gcloud auth print-access-token
    
    $headers = @{ 
      "X-Goog-User-Project" = "BILLING_PROJECT_ID";
      "Authorization" = "Bearer $cred"
    }
    
    
    Invoke-WebRequest `
      -Method GET `
      -Headers $headers `
      -Uri "https://recommender.googleapis.com/v1/projects/**my-project** /locations/global/insightTypes/google.cloudasset.asset.Insight/insights" | Select-Object -Expand Content

#### Example response
    
    
    {
       "name": "organizations/000000000000/locations/global/insightTypes/google.cloudasset.asset.Insight/insights/00000000-0000-0000-0000-000000000000",
       "description": "Domain example.com detected in 1 IAM policies",
       "content": {
          "domain": "example.com",
          "policyCount": 1,
          "policySearchQuery": "policy: example.com",
          "matchedPolicies" :[
             {
                "resource" :"//cloudresourcemanager.googleapis.com/projects/000000000000",
                "project" :"projects/000000000000",
                "matchedBindings" :[
                   {
                      "role" :"roles/viewer",
                      "matchedMembers" :[
                         "user:example@example.com"
                      ]
                   }
                ]
             }
          ]
       },
       "lastRefreshTime": "2024-01-30T00:00:00Z",
       "observationPeriod": "0s",
       "stateInfo": {
          "state": "ACTIVE"
       },
       "category": "SECURITY",
       "targetResources": [
          "//cloudresourcemanager.googleapis.com/organizations/000000000000"
       ],
       "insightSubtype": "EXTERNAL_MEMBER",
       "etag": "\"00000000000\"",
       "initialRefreshTime": "2024-01-30T00:00:00Z"
    }

## Interpreting insight responses

In addition to the [standard insight attributes](https://docs.cloud.google.com/recommender/docs/insights/using-insights), asset insights provide several specialized subtypes and fields.

### Insight subtypes

The asset insight subtypes are as follows:

  * `EXTERNAL_MEMBER`: Detects IAM policies containing users or groups which belong to a domain outside of your organization's domains.

  * `EXTERNAL_POLICY_EDITOR`: Detects IAM policies containing users or groups outside of your organization's domains that are granted permission to modify IAM policies.

  * `EXTERNAL_CLOUD_STORAGE_OBJECT_VIEWER`: Detects IAM policies containing users or groups outside of your organization's domains that are granted permission to get or list storage objects (`storage.objects.list` or `storage.objects.get permission`).

  * `EXTERNAL_SERVICE_ACCOUNT_IMPERSONATOR`: Detects IAM policies containing users or groups outside of your organization's domains that are granted permission to impersonate service accounts.

  * `TERMINATED_MEMBER`: Detects IAM policies containing users or groups with deactivated, deleted, or purged accounts.

  * `PUBLIC_IAM_POLICY`: Detects IAM policies containing all users or all authenticated users.

  * `OWNER_TERMINATED_PROJECT`: Detects projects which don't contain any active users or groups in the project's IAM policy.




### Additional content fields

In addition to the standard fields in the response, asset insights provide several specialized fields in the `content` field.

  * `user`: The user email address detected in the members of the policy bindings for this insight. This field is included in the `TERMINATED_MEMBER` subtype.

  * `domain`: The domain detected in the members of the policy bindings of this insight. This field is included in the `EXTERNAL_MEMBER`, `EXTERNAL_POLICY_EDITOR`, `EXTERNAL_CLOUD_STORAGE_OBJECT_VIEWER`, and `EXTERNAL_SERVICE_ACCOUNT_IMPERSONATOR` subtypes.

  * `assetName`: The asset name for which access was detected in this insight. This field is included in the `OWNER_TERMINATED_PROJECT` and `PUBLIC_IAM_POLICY` subtypes.

  * `policyCount`: The total number of distinct IAM policies in which matching members were detected for this insight. This field is included for all asset insight subtypes.

  * `matchedPolicies`: A sampling of the IAM policies matching the detected insight. Matching policies only include the subset of bindings and binding members which match the detected insight. This field is included for all asset insight subtypes.

  * `policySearchQuery`: A query which can be used with the Cloud Asset Inventory IAM policy search API to retrieve the relevant policies in real time.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
