---
url: https://docs.cloud.google.com/policy-intelligence/docs/review-apply-role-recommendations/
title: Review and apply role recommendations for projects, folders, and organizations \u00a0|\u00a0 Policy Intelligence \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:59:05.343153+00:00
---

# Review and apply role recommendations for projects, folders, and organizations  |  Policy Intelligence  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/policy-intelligence/docs/review-apply-role-recommendations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Policy Intelligence ](https://docs.cloud.google.com/policy-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/policy-intelligence/docs/overview)



Send feedback 

#  Review and apply role recommendations for projects, folders, and organizations Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to view, understand, and apply role recommendations for projects, folders, and organizations. Role recommendations help you enforce the principle of least privilege by ensuring that principals have only the permissions that they actually need.

## Before you begin

  * Enable the IAM and Recommender APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=iam.googleapis.com,recommender.googleapis.com&redirect=https%3A//console.cloud.google.com)

  * Understand [role recommendations](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview).

  * Review the [Best practices for role recommendations](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-best-practices).

  * Optional: If you want to view and manage role recommendations for non-basic and custom roles, ensure that you have an organization-level or project-level activation of [the Premium or Enterprise tier of Security Command Center](https://docs.cloud.google.com/security-command-center/pricing#security-command-center-pricing). For more information, see [Billing questions](https://docs.cloud.google.com/policy-intelligence/docs/billing-questions).

  * Set up authentication.

Select the tab for how you plan to use the samples on this page:

### gcloud

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Required IAM roles

This section describes the IAM roles and permissions that you need in order to work with role recommendations.

### View recommendations

To get the permissions that you need to view role recommendations, ask your administrator to grant you the following IAM roles on the resource that you want to view recommendations for (project, folder, or organization): 

  * [Role Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.roleViewer) (`roles/iam.roleViewer`)
  * [IAM Recommender Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/recommender#recommender.iamViewer) (`roles/recommender.iamViewer`)
  * To view project-level recommendations in the Google Cloud console: [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) 
  * To view folder-level recommendations in the Google Cloud console: [Folder IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.folderIamAdmin) (`roles/resourcemanager.folderIamAdmin`) 
  * To view organization-level recommendations in the Google Cloud console: [Organization Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.organizationAdmin) (`roles/resourcemanager.organizationAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to view role recommendations. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view role recommendations:

  * `iam.roles.get`
  * `iam.roles.list`
  * `recommender.iamPolicyRecommendations.get`
  * `recommender.iamPolicyRecommendations.list`
  * `recommender.iamPolicyInsights.get`
  * `recommender.iamPolicyInsights.list`
  * `recommender.iamPolicyLateralMovementInsights.get`
  * `recommender.iamPolicyLateralMovementInsights.list`
  * To view recommendations in the Google Cloud console: `resourcemanager.RESOURCE.getIamPolicy`, where `RESOURCE` is the resource type that you want to view recommendations for (`projects`, `folders`, or `organizations`) 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Apply and dismiss recommendations

To get the permissions that you need to view, apply, and dismiss role recommendations, ask your administrator to grant you the following IAM roles on the resource that you want to manage recommendations for (project, folder, or organization): 

  * [Role Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.roleViewer) (`roles/iam.roleViewer`)
  * [IAM Recommender Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/recommender#recommender.iamAdmin) (`roles/recommender.iamAdmin`)
  * To manage project-level recommendations: [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) 
  * To manage folder-level recommendations: [Folder IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.folderIamAdmin) (`roles/resourcemanager.folderIamAdmin`) 
  * To manage organization-level recommendations: [Organization Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.organizationAdmin) (`roles/resourcemanager.organizationAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to view, apply, and dismiss role recommendations. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view, apply, and dismiss role recommendations:

  * `iam.roles.get`
  * `iam.roles.list`
  * `recommender.iamPolicyRecommendations.get`
  * `recommender.iamPolicyRecommendations.list`
  * `recommender.iamPolicyInsights.get`
  * `recommender.iamPolicyInsights.list`
  * `recommender.iamPolicyLateralMovementInsights.get`
  * `recommender.iamPolicyLateralMovementInsights.list`
  * `recommender.iamPolicyRecommendations.update`
  * `resourcemanager.RESOURCE.getIamPolicy`, where `RESOURCE` is the resource type that you want to manage recommendations for (`projects`, `folders`, or `organizations`) 
  * `resourcemanager.RESOURCE.setIamPolicy`, where `RESOURCE` is the resource type that you want to manage recommendations for (`projects`, `folders`, or `organizations`) 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** Some project-level recommendations suggest [creating a new custom role](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview#custom-roles) as part of the recommendation. To create a custom role, you need the `iam.roles.create` permission on the project. To gain this permission while following the principle of least privilege, ask your administrator to grant you the Role Administrator role (`roles/iam.roleAdmin`) instead of the Role Viewer role (`roles/iam.roleViewer`).

## Review and apply recommendations

The easiest way to review and apply your recommendations is to use the Google Cloud console. Additionally, if you want to automatically create a custom role when you apply a recommendation, you must use the Google Cloud console.

You can also review and apply recommendations with the Google Cloud CLI and the Recommender API.

**Note:** The IAM recommender does not take other forms of access controls into account when making recommendations. If you use access controls that are separate from IAM, such as Cloud Storage [access control lists (ACLs)](https://docs.cloud.google.com/storage/docs/access-control/lists) or Kubernetes [role-based access control (RBAC)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control), ensure that each recommendation will not disrupt those access controls before you apply the recommendation.

### Console

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project,folder,organizationId)

  2. Select a project, folder, or organization.

  3. In the list of principals that have access to your project, find the **Security insights** column.

**Note:** The Google Cloud console does not automatically display role grants for service agents. To view these role grants and their associated recommendations, select **Include Google-provided role grants**.

For each role granted to a principal, this column shows any security-related [insights](https://docs.cloud.google.com/recommender/docs/insights/using-insights). These insights highlight patterns in how your principals access resources. For example, some insights highlight _excess permissions_ , or permissions that a principal does not need. Other insights highlight service accounts with [lateral movement capabilities](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview#lateral-movement-insights):

![](https://docs.cloud.google.com/static/policy-intelligence/img/recommender-roles-permissions.png)

![](https://docs.cloud.google.com/static/policy-intelligence/img/recommender-roles-permissions-2x.png)

If there is a recommendation available to address an insight, the Google Cloud console displays the **Recommendation available** ![](https://docs.cloud.google.com/static/policy-intelligence/img/recommender-yes.svg) icon.

**Note:** Recommender does not analyze permissions for all roles. To learn which roles Recommender analyzes, see [Availability of IAM policy recommendations](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview#availability).
  4. If there are recommendations to review, click a **Recommendation available** ![](https://docs.cloud.google.com/static/policy-intelligence/img/recommender-yes.svg) icon to get details about the recommendation.

If the recommendation is to replace the role, the role recommendation always suggests a set of [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles) that you can apply.

In some cases, the role recommendation also suggests creating a new [custom role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) at the project level. If a custom role recommendation is available, the Google Cloud console shows it by default. To switch to the predefined role recommendation, click **View recommended predefined role**.

Only for group principals with excessive permissions, you have an option to replace permanent access with temporary, on-demand access ([Preview](https://cloud.google.com/products#product-launch-stages)) using Privileged Access Manager. If members of a group don't need permanent access to a role's permissions, but might need them for unanticipated reasons in the future, you can remove their permanent access and use Privileged Access Manager to allow them to request temporary access when they need it. To learn how to remediate excessive permissions with Privileged Access Manager, see [Remediate excessive permissions with Privileged Access Manager](https://docs.cloud.google.com/iam/docs/pam-remediate-iam-recommendations).

  5. Review the recommendation carefully and make sure you understand when it was last refreshed and how it will change the principal's access to Google Cloud resources. Except in the case of [recommendations for service agents](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview#service-agents), a recommendation will never increase a principal's level of access. For more information, see [How role recommendations are generated](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview#how-recommender-works).

To learn how to review recommendations in the console, see Review recommendations on this page.

  6. Optional: If the recommendation is to create a custom role, update the **Title** , **Description** , **ID** , and **Role launch stage** as needed.

If you need to add permissions to the custom role, click **Add permissions**.

If you need to remove permissions from the custom role, clear the checkbox for each permission that you want to remove.

  7. Take action on the recommendation.

To apply the recommendation, click **Apply** or **Create and apply**. If you change your mind in the next 90 days, use the recommendations history to revert your choice.

To dismiss the recommendation, click **Dismiss** , then confirm your choice. You can restore a dismissed recommendation as long as the recommendation is still valid.

**Note:** You can also quickly apply and dismiss recommendations by clicking the arrow_right expander arrow next to an insight with a recommendation, then clicking **Apply recommendation** or **Dismiss recommendation**. You cannot apply recommendations to create custom roles in this way.
  8. Repeat the previous steps until you have reviewed all of your recommendations.




### gcloud

**Review your recommendations:**

To list your recommendations, run the [`gcloud recommender recommendations list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/recommendations/list) command:
    
    
    gcloud recommender recommendations list \
        --location=global \
        --recommender=google.iam.policy.Recommender \
        --RESOURCE_TYPE=RESOURCE_ID \
        --format=json
    

Replace the following values:

  * `RESOURCE_TYPE`: The resource type that you want to list recommendations for. Use the value `project`, `folder`, or `organization`.
  * `RESOURCE_ID`: The ID of the Google Cloud project, folder, or organization that you want to list recommendations for. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.



The response is similar to the following example. In this example, a service account has not used any permissions from the Compute Admin role (`roles/compute.admin`) in the past 90 days. As a result, the role recommendation suggests that you revoke the role:
    
    
    [
      {
        "associatedInsights": [
          {
            "insight": "projects/123456789012/locations/global/insightTypes/google.iam.policy.Insight/insights/279ef748-408f-44db-9a4a-1ff8865b9839"
          }
        ],
        "content": {
          "operationGroups": [
            {
              "operations": [
                {
                  "action": "remove",
                  "path": "/iamPolicy/bindings/*/members/*",
                  "pathFilter": {
                    "/iamPolicy/bindings/*/condition/expression": "",
                    "/iamPolicy/bindings/*/members/*": "serviceAccount:id-1234567890@example-project.iam.gserviceaccount.com",
                    **"/iamPolicy/bindings/*/role" : "roles/compute.admin"**
                  },
                  "resource": "//cloudresourcemanager.googleapis.com/projects/example-project",
                  "resourceType": "cloudresourcemanager.googleapis.com/Project"
                }
              ]
            }
          ]
        },
        **"description" : "This role has not been used during the observation window.",
        "recommenderSubtype": "REMOVE_ROLE",
        "etag": "\"770237e2c0decf40\"",**
        "lastRefreshTime": "2020-01-09T06:06:17Z",
        **"name" : "projects/123456789012/locations/global/recommenders/google.iam.policy.Recommender/recommendations/fb927dc1-9695-4436-0000-f0f285007c0f",**
        "primaryImpact": {
          "category": "SECURITY",
          "securityProjection": {
            "details": {
              "revokedIamPermissionsCount": 708
            }
          }
        },
        "priority": "P4",
        "stateInfo": {
          "state": "ACTIVE"
        }
      }
    ]

Review each recommendation carefully and consider when it was last refreshed and how it will change the principal's access to Google Cloud resources. To learn how to review recommendations from the gcloud CLI, see Review recommendations on this page.

**To apply a recommendation:**

  1. Use the [`gcloud recommender recommendations mark-claimed` command](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-claimed) to change the recommendation's state to `CLAIMED,` which prevents the recommendation from changing while you apply it:
         
         gcloud recommender recommendations mark-claimed \
             RECOMMENDATION_ID \
             --location=global \
             --recommender=google.iam.policy.Recommender \
             --RESOURCE_TYPE=RESOURCE_ID \
             --format=FORMAT \
             --etag=ETAG \
             --state-metadata=STATE_METADATA
         

Replace the following values:

     * `RECOMMENDATION_ID`: The unique identifier for the recommendation. This value appears at the end of the `name` field in the recommendation. In the example shown above, the ID is `fb927dc1-9695-4436-0000-f0f285007c0f`. 
     * `RESOURCE_TYPE`: The resource type that you want to manage recommendations for. Use the value `project`, `folder`, or `organization`. 
     * `RESOURCE_ID`: The ID of the Google Cloud project, folder, or organization that you want to manage recommendations for. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`. 
     * `FORMAT`: The format of the response. Use `json` or `yaml`. 
     * `ETAG`: The value of the `etag` field in the recommendation, such as `"dd0686e7136a4cbb"`. Note that this value can include quotes. 
     * `STATE_METADATA`: Optional. Comma-separated key-value pairs that contain your choice of metadata about the recommendation. For example, `--state-metadata=reviewedBy=alice,priority=high`. The metadata replaces the `stateInfo.stateMetadata` field in the recommendation. 

If the command succeeds, the response shows the recommendation in a `CLAIMED` state, as shown in the following example. For clarity, the example omits most fields:
    
    [
      {
        "description": "This role has not been used during the observation window.",
        "recommenderSubtype": "REMOVE_ROLE",
        "etag": "\"df7308cca9719dcc\"",
        "name": "projects/123456789012/locations/global/recommenders/google.iam.policy.Recommender/recommendations/fb927dc1-9695-4436-0000-f0f285007c0f",
        **"stateInfo" : {
          "state": "CLAIMED",
          "stateMetadata": {
            "reviewedBy": "alice",
            "priority": "high"
          }
        }**
      }
    ]

  2. [Get the allow policy](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#getting-policy) for the project, then [modify and set the allow policy](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#modifying-policy) so that it reflects the recommendation.

  3. Update the recommendation's state to `SUCCEEDED`, if you were able to apply the recommendation, or `FAILED`, if you could not apply the recommendation:
         
         gcloud recommender recommendations COMMAND \
             RECOMMENDATION_ID \
             --location=global \
             --recommender=google.iam.policy.Recommender \
             --RESOURCE_TYPE=RESOURCE_ID \
             --format=FORMAT \
             --etag=ETAG \
             --state-metadata=STATE_METADATA
         

Replace the following values:

     * `COMMAND`: Use `mark-succeeded`, if you were able to apply the recommendation, or `mark-failed`, if you could not apply the recommendation. 

     * `RECOMMENDATION_ID`: The unique identifier for the recommendation. This value appears at the end of the `name` field in the recommendation. In the example shown above, the ID is `fb927dc1-9695-4436-0000-f0f285007c0f`. 
     * `RESOURCE_TYPE`: The resource type that you want to manage recommendations for. Use the value `project`, `folder`, or `organization`. 
     * `RESOURCE_ID`: The ID of the Google Cloud project, folder, or organization that you want to manage recommendations for. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`. 
     * `FORMAT`: The format of the response. Use `json` or `yaml`. 
     * `ETAG`: The value of the `etag` field in the recommendation, such as `"dd0686e7136a4cbb"`. Note that this value can include quotes. 
     * `STATE_METADATA`: Optional. Comma-separated key-value pairs that contain your choice of metadata about the recommendation. For example, `--state-metadata=reviewedBy=alice,priority=high`. The metadata replaces the `stateInfo.stateMetadata` field in the recommendation. 

For example, if you marked the recommendation as having succeeded, the response shows the recommendation in a `SUCCEEDED` state. For clarity, this example omits most fields:
    
    [
      {
        "description": "This role has not been used during the observation window.",
        "recommenderSubtype": "REMOVE_ROLE",
        "etag": "\"dd0686e7136a4cbb\"",
        "name": "projects/123456789012/locations/global/recommenders/google.iam.policy.Recommender/recommendations/fb927dc1-9695-4436-0000-f0f285007c0f",
        **"stateInfo" : {
          "state": "SUCCEEDED",
          "stateMetadata": {
            "reviewedBy": "alice",
            "priority": "high"
          }
        }**
      }
    ]




### REST

**Review your recommendations:**

To list all available recommendations for your project, folder, or organization, use the Recommender API's `[recommendations.list](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.recommenders.recommendations/list)` method. 

Before using any of the request data, make the following replacements: 

  * `RESOURCE_TYPE`: The type of the resource that you want to manage recommendations for. Use the value `projects`, `folders`, or `organizations`.
  * `RESOURCE_ID`: The ID of the Google Cloud project, folder, or organization that you want to manage recommendations for. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.
  * `PAGE_SIZE`: Optional. The maximum number of results to return from this request. If not specified, the server will determine the number of results to return. If the number of recommendations is greater than the page size, the response contains a pagination token that you can use to retrieve the next page of results. 
  * `PAGE_TOKEN`: Optional. The pagination token returned in an earlier response from this method. If specified, the list of recommendations will start where the previous request ended.
  * `FILTER`: Optional. A filter expression to restrict the recommendations returned. You can filter recommendations based on the `stateInfo.state` field. For example, `stateInfo.state:"DISMISSED"` or `stateInfo.state:"FAILED"`. 
  * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.



HTTP method and URL: 
    
    
    GET https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/recommenders/google.iam.policy.Recommender/recommendations?pageSize=PAGE_SIZE&pageToken=PAGE_TOKEN&filter=FILTER

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         "https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/recommenders/google.iam.policy.Recommender/recommendations?pageSize=PAGE_SIZE&pageToken=PAGE_TOKEN&filter=FILTER"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/recommenders/google.iam.policy.Recommender/recommendations?pageSize=PAGE_SIZE&pageToken=PAGE_TOKEN&filter=FILTER" | Select-Object -Expand Content

The response is similar to the following example. In this example, a service account in the project `example-project` has not used any permissions from the Compute Admin role (`roles/compute.admin`) in the past 90 days. As a result, Recommender suggests that you revoke the role: 
    
    
    {
      "recommendations": [
        **"name": "projects/123456789012/locations/global/recommenders/google.iam.policy.Recommender/recommendations/fb927dc1-9695-4436-0000-f0f285007c0f",
        "description": "This role has not been used during the observation window.",**
        "lastRefreshTime": "2020-01-09T06:06:17Z",
        "primaryImpact": {
          "category": "SECURITY",
          "securityProjection": {
            "details": {
              "revokedIamPermissionsCount": 708
            }
          }
        },
        "priority": "P4",
        "content": {
          "operationGroups": [
            {
              "operations": [
                {
                  "action": "remove",
                  "path": "/iamPolicy/bindings/*/members/*",
                  "pathFilter": {
                    "/iamPolicy/bindings/*/condition/expression": "",
                    "/iamPolicy/bindings/*/members/*": "serviceAccount:id-1234567890@example-project.iam.gserviceaccount.com",
                    **"/iamPolicy/bindings/*/role": "roles/compute.admin"**
                  },
                  "resource": "//cloudresourcemanager.googleapis.com/projects/example-project",
                  "resourceType": "cloudresourcemanager.googleapis.com/Project"
                }
              ]
            }
          ]
        },
        "stateInfo": {
          "state": "ACTIVE"
        }
        **"etag": "\"770237e2c0decf40\"",
        "recommenderSubtype": "REMOVE_ROLE"** ,
        "associatedInsights": [
          {
            "insight": "projects/123456789012/locations/global/insightTypes/google.iam.policy.Insight/insights/279ef748-408f-44db-9a4a-1ff8865b9839"
          }
      ]
    }
    

Review each recommendation carefully and consider when it was last refreshed and how it will change the principal's access to Google Cloud resources. To learn how to review recommendations from the REST API, see Review recommendations on this page.

**To apply a recommendation:**

  1. Mark the recommendation as `CLAIMED`:

To mark a recommendation as `CLAIMED`, which prevents the recommendation from changing while you apply it, use the Recommender API's `[recommendations.markClaimed](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.recommenders.recommendations/markClaimed)` method. 

Before using any of the request data, make the following replacements: 

     * `RESOURCE_TYPE`: The type of the resource that you want to manage recommendations for. Use the value `projects`, `folders`, or `organizations`.
     * `RESOURCE_ID`: The ID of the Google Cloud project, folder, or organization that you want to manage recommendations for. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.
     * `RECOMMENDATION_ID`: The unique identifier for the recommendation. This value appears at the end of the `name` field in the recommendation. For example, if the `name` field is `projects/example-project/locations/global/recommenders/google.iam.policy.Recommender/recommendations/fb927dc1-9695-4436-0000-f0f285007c0f`, the recommendation ID is `fb927dc1-9695-4436-0000-f0f285007c0f`. 
     * `ETAG`: The value of the `etag` field in the recommendation, such as `"dd0686e7136a4cbb"`. Use backslashes to escape quotes, for example, `"\"df7308cca9719dcc\""`. 
     * `STATE_METADATA`: Optional. An object that contains key-value pairs with your choice of metadata about the recommendation. For example, `{"reviewedBy": "alice", "priority": "high"}`. The metadata replaces the `stateInfo.stateMetadata` field in the recommendation. 
     * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.

HTTP method and URL: 
    
    POST https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/recommenders/google.iam.policy.Recommender/recommendations/RECOMMENDATION_ID:markClaimed

Request JSON body: 
    
    {
      "etag": "ETAG",
      "stateMetadata": {
        "STATE_METADATA"
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/recommenders/google.iam.policy.Recommender/recommendations/RECOMMENDATION_ID:markClaimed"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/recommenders/google.iam.policy.Recommender/recommendations/RECOMMENDATION_ID:markClaimed" | Select-Object -Expand Content

The response shows the recommendation in a `CLAIMED` state, as shown in the following example. For clarity, this example omits most fields: 
    
    {
      "description": "This role has not been used during the observation window.",
      **"stateInfo": {
        "state": "CLAIMED",
        "stateMetadata": {
          "reviewedBy": "alice",
          "priority": "high"
        }
      },**
      "etag": "\"dd0686e7136a4cbb\"",
      "recommenderSubtype": "REMOVE_ROLE"
    }
    

  2. [Get the allow policy](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#getting-policy) for the project, then [modify the allow policy](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#modifying-policy) so that it reflects the recommendation.

  3. Update the recommendation's state to `SUCCEEDED`, if you were able to apply the recommendation, or `FAILED`, if you could not apply the recommendation:

### `SUCCEEDED`

To mark a recommendation as `SUCCEEDED`, indicating that you were able to apply it, use the Recommender API's `[recommendations.markSucceeded](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.recommenders.recommendations/markSucceeded)` method. 

Before using any of the request data, make the following replacements: 

     * `RESOURCE_TYPE`: The type of the resource that you want to manage recommendations for. Use the value `projects`, `folders`, or `organizations`.
     * `RESOURCE_ID`: The ID of the Google Cloud project, folder, or organization that you want to manage recommendations for. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.
     * `RECOMMENDATION_ID`: The unique identifier for the recommendation. This value appears at the end of the `name` field in the recommendation. For example, if the `name` field is `projects/example-project/locations/global/recommenders/google.iam.policy.Recommender/recommendations/fb927dc1-9695-4436-0000-f0f285007c0f`, the recommendation ID is `fb927dc1-9695-4436-0000-f0f285007c0f`. 
     * `ETAG`: The value of the `etag` field in the recommendation, such as `"dd0686e7136a4cbb"`. Use backslashes to escape quotes, for example, `"\"df7308cca9719dcc\""`. 
     * `STATE_METADATA`: Optional. An object that contains key-value pairs with your choice of metadata about the recommendation. For example, `{"reviewedBy": "alice", "priority": "high"}`. The metadata replaces the `stateInfo.stateMetadata` field in the recommendation. 
     * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.

HTTP method and URL: 
    
    POST https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/recommenders/google.iam.policy.Recommender/recommendations/RECOMMENDATION_ID:markSucceeded

Request JSON body: 
    
    {
      "etag": "ETAG",
      "stateMetadata": {
        "STATE_METADATA"
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/recommenders/google.iam.policy.Recommender/recommendations/RECOMMENDATION_ID:markSucceeded"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/recommenders/google.iam.policy.Recommender/recommendations/RECOMMENDATION_ID:markSucceeded" | Select-Object -Expand Content

The response shows the recommendation in a `SUCCEEDED` state, as shown in the following example. For clarity, this example omits most fields: 
    
    {
      "description": "This role has not been used during the observation window.",
      **"stateInfo": {
        "state": "SUCCEEDED",
        "stateMetadata": {
          "reviewedBy": "alice",
          "priority": "high"
        }
      },**
      "etag": "\"dd0686e7136a4cbb\"",
      "recommenderSubtype": "REMOVE_ROLE"
    }
    

### `FAILED`

To mark a recommendation as `FAILED`, indicating that you were not able to apply it, use the Recommender API's `[recommendations.markFailed](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.recommenders.recommendations/markFailed)` method. 

Before using any of the request data, make the following replacements: 

     * `RESOURCE_TYPE`: The type of the resource that you want to manage recommendations for. Use the value `projects`, `folders`, or `organizations`.
     * `RESOURCE_ID`: The ID of the Google Cloud project, folder, or organization that you want to manage recommendations for. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.
     * `RECOMMENDATION_ID`: The unique identifier for the recommendation. This value appears at the end of the `name` field in the recommendation. For example, if the `name` field is `projects/example-project/locations/global/recommenders/google.iam.policy.Recommender/recommendations/fb927dc1-9695-4436-0000-f0f285007c0f`, the recommendation ID is `fb927dc1-9695-4436-0000-f0f285007c0f`. 
     * `ETAG`: The value of the `etag` field in the recommendation, such as `"dd0686e7136a4cbb"`. Use backslashes to escape quotes, for example, `"\"df7308cca9719dcc\""`. 
     * `STATE_METADATA`: Optional. An object that contains key-value pairs with your choice of metadata about the recommendation. For example, `{"reviewedBy": "alice", "priority": "high"}`. The metadata replaces the `stateInfo.stateMetadata` field in the recommendation. 
     * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.

HTTP method and URL: 
    
    POST https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/recommenders/google.iam.policy.Recommender/recommendations/RECOMMENDATION_ID:markFailed

Request JSON body: 
    
    {
      "etag": "ETAG",
      "stateMetadata": {
        "STATE_METADATA"
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/recommenders/google.iam.policy.Recommender/recommendations/RECOMMENDATION_ID:markFailed"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/recommenders/google.iam.policy.Recommender/recommendations/RECOMMENDATION_ID:markFailed" | Select-Object -Expand Content

The response shows the recommendation in a `FAILED` state, as shown in the following example. For clarity, this example omits most fields: 
    
    {
      "description": "This role has not been used during the observation window.",
      **"stateInfo": {
        "state": "FAILED",
        "stateMetadata": {
          "reviewedBy": "alice",
          "priority": "high"
        }
      },**
      "etag": "\"dd0686e7136a4cbb\"",
      "recommenderSubtype": "REMOVE_ROLE"
    }
    




## Understand recommendations

Each recommendation includes information to help you understand why the recommendation was made.

### Console

To help you understand why the recommendation was made, the Google Cloud console shows the principal's permission usage, as reported by the [policy insight](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview#how-policy-insights-work) associated with the recommendation. For example, it might show a list like the following:

![](https://docs.cloud.google.com/static/policy-intelligence/img/recommender-analyzed-permissions.png)

![](https://docs.cloud.google.com/static/policy-intelligence/img/recommender-analyzed-permissions.png)

**Note** : If a recommendation is for a [basic role](https://docs.cloud.google.com/iam/docs/roles-overview#basic), the list of permissions in the Google Cloud console might not include all of the permissions that a principal needs. This is because some services use basic roles to indirectly grant additional roles. The list of permissions might not include permissions from these additional roles, even if a principal used them. Role recommendations automatically account for this discrepancy. 

Indirectly granted roles include roles granted through [Cloud Storage convenience values](https://docs.cloud.google.com/storage/docs/access-control/iam#convenience-values) and [BigQuery special group membership](https://docs.cloud.google.com/bigquery/docs/access-control-basic-roles). 

To help you understand the impact of applying the recommendation, the Google Cloud console also shows a color- and symbol-coded list of permissions. This list indicates how the principal's permissions will change if you apply the recommendation. For example, it might show a list like the following:

![](https://docs.cloud.google.com/static/policy-intelligence/img/recommender-replacement-role.png)

![](https://docs.cloud.google.com/static/policy-intelligence/img/recommender-replacement-role.png)

The types of permissions associated with each color and symbol are as follows:

  * **Gray with no symbol** : Permissions that are in both the principal's current role and the recommended roles.

![](https://docs.cloud.google.com/static/policy-intelligence/img/recommender-permission-gray.png)

  * **Red with a minus sign(-)**: Permissions that are in the principal's current role, but not in the recommended roles because the principal hasn't used them in the past 90 days.

![](https://docs.cloud.google.com/static/policy-intelligence/img/recommender-permission-red.png)

  * **Green with a plus sign(+)**: Permissions that are not in the principal's current role, but are in the recommended roles. This type of permission appears only in [recommendations for service agents](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview#service-agents).

![](https://docs.cloud.google.com/static/policy-intelligence/img/recommender-permission-green.png)

  * **Blue with a _Machine learning_ icon (![](https://docs.cloud.google.com/static/policy-intelligence/img/recommender-ml.svg))**: Permissions that are in both the principal's current role and the recommended roles, not because the principal has used the permissions in the past 90 days, but because Recommender has determined through [machine learning](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview#ml) that they are likely to need those permissions in the future.

![](https://docs.cloud.google.com/static/policy-intelligence/img/recommender-permission-blue.png)




Some recommendations are also associated with [lateral movement insights](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview#lateral-movement-insights). Lateral movement insights identify roles that allow a service account in one project to impersonate a service account in another project. If a recommendation is associated with a lateral movement insight, the Google Cloud console also shows the following:

  * **The service account's origin project** : The project that the service account with impersonation permissions was created in.

![](https://docs.cloud.google.com/static/policy-intelligence/img/lmi-origin-project.png)

![](https://docs.cloud.google.com/static/policy-intelligence/img/lmi-origin-project.png)

  * **Service accounts that can be impersonated in this project** : A list of all of the service accounts in the current project that the service account with impersonation permissions can impersonate.

![](https://docs.cloud.google.com/static/policy-intelligence/img/lmi-target-sa-list.png)

![](https://docs.cloud.google.com/static/policy-intelligence/img/lmi-target-sa-list.png)




### gcloud

For details on the fields of a recommendation, see the [`Recommendation` reference](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.recommenders.recommendations#resource-recommendation).

To see the permission usage that this recommendation is based on, view the [policy insights](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview#how-policy-insights-work) that are associated with the recommendation. These insights are listed in the `associatedInsights` field. To view a policy insight that is associated with the recommendation, do the following:

  * Identify which insights in the `associatedInsights` field are policy insights. Policy insights have the insight type `google.iam.policy.insight`. This type appears after `insightTypes` in the `insight` field.
  * Copy the policy insight's ID. The ID is everything after `insights/` in the `insight` field. In the preceding example, the insight ID is `279ef748-408f-44db-9a4a-1ff8865b9839`.
  * Follow the instructions to [get a policy insight](https://docs.cloud.google.com/policy-intelligence/docs/policy-insights#get-insight), using the insight ID you copied.



Some recommendations are also associated with [lateral movement insights](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview#lateral-movement-insights), which identify roles that allow service accounts in one project to impersonate service accounts in another project. These insights are also listed in the `associatedInsights` field. To view a lateral movement insight that is associated with the recommendation, do the following:

  * Identify which insights in the `associatedInsights` field are lateral movement insights. Lateral movement insights have the insight type `google.iam.policy.LateralMovementInsight`. This type appears after `insightTypes` in the `insight` field.
  * Copy the policy insight's ID. The ID is everything after `insights/` in the `insight` field. In the preceding example, the insight ID is `279ef748-408f-44db-9a4a-1ff8865b9839`.
  * Follow the instructions to [get a lateral movement insight](https://docs.cloud.google.com/policy-intelligence/docs/lateral-movement-insights#get-insight), using the insight ID you copied.



### REST

For details on the fields of a recommendation, see the [`Recommendation` reference](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.recommenders.recommendations#resource-recommendation).

To see the permission usage that this recommendation is based on, view the [policy insights](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview#how-policy-insights-work) that are associated with the recommendation. These insights are listed in the `associatedInsights` field. To view a policy insight that is associated with the recommendation, do the following:

  1. Identify which insights in the `associatedInsights` field are policy insights. Policy insights have the insight type `google.iam.policy.insight`. This type appears after `insightTypes` in the `insight` field.
  2. Copy the policy insight's ID. The ID is everything after `insights/` in the `insight` field. For example, if the `insight` field reads `projects/123456789012/locations/global/insightTypes/google.iam.policy.Insight/insights/279ef748-408f-44db-9a4a-1ff8865b9839`, then the insight ID is `279ef748-408f-44db-9a4a-1ff8865b9839`.
  3. Follow the instructions to [get a policy insight](https://docs.cloud.google.com/policy-intelligence/docs/policy-insights#get-insight), using the insight ID you copied.



Some recommendations are also associated with [lateral movement insights](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview#lateral-movement-insights), which identify roles that allow service accounts in one project to impersonate service accounts in another project. These insights are also listed in the `associatedInsights` field. To view a lateral movement insight that is associated with the recommendation, do the following:

  1. Identify which insights in the `associatedInsights` field are lateral movement insights. Lateral movement insights have the insight type `google.iam.policy.LateralMovementInsight`. This type appears after `insightTypes` in the `insight` field.
  2. Copy the policy insight's ID. The ID is everything after `insights/` in the `insight` field. For example, if the `insight` field reads `projects/123456789012/locations/global/insightTypes/google.iam.policy.LateralMovementInsight/insights/13088eec-9573-415f-81a7-46e1a260e860`, then the insight ID is `13088eec-9573-415f-81a7-46e1a260e860`.
  3. Follow the instructions to [get a lateral movement insight](https://docs.cloud.google.com/policy-intelligence/docs/lateral-movement-insights#get-insight), using the insight ID you copied.



## View, revert, and restore changes

After you apply or dismiss a recommendation for a project-level role binding, that action appears in the recommendations history.

To view the recommendations history:

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project,folder,organizationId)

  2. Select a project, folder, or organization.

  3. Near the top of the screen, click **Recommendations history**.

The Google Cloud console shows a list of previous actions on your role recommendations.

  4. To view details about a recommendation, click the expand_more expander arrow.

The Google Cloud console shows details about the action that was taken, including the principal that took the action:

![](https://docs.cloud.google.com/static/policy-intelligence/img/recommender-applied.png)

![](https://docs.cloud.google.com/static/policy-intelligence/img/recommender-applied.png)

  5. (Optional) If necessary, you can revert the recommendation, which undoes the changes in the recommendation, or restore a recommendation that you dismissed.

To revert a previously applied change for a recommendation, click **Revert**. The Google Cloud console reverts the changes to the principal's roles. The recommendation no longer appears in the Google Cloud console.

If you revert the recommendation that replaced permanent access with temporary, on-demand access, the system restores the original IAM binding and deletes the created Privileged Access Manager entitlement. If the revert process fails, then [delete the entitlement manually](https://docs.cloud.google.com/iam/docs/pam-view-update-delete-entitlements).

**Note:** If the previously applied change created a custom role, then reverting the change does not delete the custom role. You can [disable](https://docs.cloud.google.com/iam/docs/creating-custom-roles#disabling-custom-role) or [delete](https://docs.cloud.google.com/iam/docs/creating-custom-roles#deleting-custom-role) the custom role if you no longer need it.

To restore a recommendation that was dismissed, click **Restore**. The recommendation becomes visible on the **IAM** page in the Google Cloud console. No roles or permissions are changed.




## What's next

  * Learn more about [Recommender](https://docs.cloud.google.com/recommender/docs/overview).
  * Learn how to use [allow policy insights](https://docs.cloud.google.com/policy-intelligence/docs/policy-insights).
  * Learn how to use [lateral movement insights](https://docs.cloud.google.com/policy-intelligence/docs/lateral-movement-insights).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
