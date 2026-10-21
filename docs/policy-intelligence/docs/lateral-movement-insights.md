---
url: https://docs.cloud.google.com/policy-intelligence/docs/lateral-movement-insights/
title: Find service accounts with lateral movement permissions \u00a0|\u00a0 Policy Intelligence \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:46:49.244947+00:00
---

# Find service accounts with lateral movement permissions  |  Policy Intelligence  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/policy-intelligence/docs/lateral-movement-insights/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Policy Intelligence ](https://docs.cloud.google.com/policy-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/policy-intelligence/docs/overview)



Send feedback 

#  Find service accounts with lateral movement permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to manage lateral movement insights, which identify roles that allow a service account in one project to impersonate a service account in another project. For more information about lateral movement insights, see [ How lateral movement insights are generated](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview#lateral-movement-insights).

Lateral movement insights are sometimes linked to [ role recommendations](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview). Role recommendations suggest actions that you can take to remediate the issues identified by lateral movement insights. 

## Before you begin

  * Enable the Recommender API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=recommender.googleapis.com&redirect=https%3A//console.cloud.google.com)

  * Be familiar with [IAM role recommendations](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview).
  * Ensure that you have an [ organization-level or project-level activation](https://docs.cloud.google.com/security-command-center/pricing#security-command-center-pricing) of the Premium or Enterprise tier of Security Command Center. For more information, see [ Billing questions](https://docs.cloud.google.com/policy-intelligence/docs/billing-questions).
  * Optional: Read about [Recommender insights](https://docs.cloud.google.com/recommender/docs/insights/using-insights).



### Required roles

To get the permissions that you need to manage lateral movement insights, ask your administrator to grant you the following IAM roles on the project, folder, or organization that you want to manage insights for: 

  * To view lateral movement insights: [IAM Recommender Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/recommender#recommender.iamViewer) (`roles/recommender.iamViewer`) 
  * To modify lateral movement insights: [IAM Recommender Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/recommender#recommender.iamAdmin) (`roles/recommender.iamAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to manage lateral movement insights. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to manage lateral movement insights:

  * To view lateral movement insights: 
    * `recommender.iamPolicyLateralMovementInsights.get`
    * `recommender.iamPolicyLateralMovementInsights.list`
  * To modify lateral movement insights: `recommender.iamPolicyLateralMovementInsights.update`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## List lateral movement insights

To list all lateral movement insights for your project, folder, or organization, use one of the following methods: 

### Console

  1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project,folder,organizationId)

  2. Select a project, folder, or organization.



The **Security insights** column shows all security-related insights for your project, including lateral movement insights. Lateral movement insights have the form `N service account impersonations`, where `N` is the number of service accounts that the service account in the role binding can impersonate. 

### gcloud

Use the [`gcloud recommender insights list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/list) command to view all lateral movement insights for your project, folder, or organization. 

Before you run the command, replace the following values: 

  * `RESOURCE_TYPE`: The resource type that you want to list insights for. Use the value `project`, `folder`, or `organization`. 
  * `RESOURCE_ID`: The ID of the project, folder, or organization that you want to list insights for. 


    
    
    gcloud recommender insights list --insight-type=google.iam.policy.LateralMovementInsight \
        --RESOURCE_TYPE=RESOURCE_ID \
        --location=global

The output lists all of the lateral movement insights for your project, folder, or organization. For example: 
    
    
    INSIGHT_ID                            CATEGORY  INSIGHT_STATE  LAST_REFRESH_TIME     SEVERITY  INSIGHT_SUBTYPE              DESCRIPTION
    046f8b89-bcee-46cd-9ac4-06818ed5273a  SECURITY  ACTIVE         2022-05-24T07:00:00Z  LOW       CROSS_PROJECT_IMPERSONATION  Service account sa-1@another-project.iam.gserviceaccount.com from another project can impersonate 2 service account(s) under this project.
    1328df82-5af2-4493-9850-d8ede4e72b27  SECURITY  ACTIVE         2022-05-24T07:00:00Z  LOW       CROSS_PROJECT_IMPERSONATION  Service account sa-2@another-project.iam.gserviceaccount.com from another project can impersonate 1 service account(s) under this project.
    17f50957-333c-4f21-86c1-6a62216b309e  SECURITY  ACTIVE         2022-05-24T07:00:00Z  LOW       CROSS_PROJECT_IMPERSONATION  Service account sa-3@another-project.iam.gserviceaccount.com from another project can impersonate 1 service account(s) under this project.
    187200d2-b42c-48fb-86d7-c2746a87fed2  SECURITY  ACTIVE         2022-05-24T07:00:00Z  LOW       CROSS_PROJECT_IMPERSONATION  Service account sa-4@another-project.iam.gserviceaccount.com from another project can impersonate 32 service account(s) under this project.
    1f1740a4-ff98-4f64-99a4-5ef5df5a2097  SECURITY  ACTIVE         2022-05-24T07:00:00Z  LOW       CROSS_PROJECT_IMPERSONATION  Service account sa-5@another-project.iam.gserviceaccount.com from another project can impersonate 1 service account(s) under this project.

### REST

The Recommender API's `[insights.list](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.insightTypes.insights/list)` method lists all lateral movement insights for your project, folder, or organization. 

Before using any of the request data, make the following replacements: 

  * `RESOURCE_TYPE`: The resource type that you want to list insights for. Use the value `projects`, `folders`, or `organizations`. 
  * `RESOURCE_ID`: The ID of the project, folder, or organization that you want to list insights for. 
  * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.



HTTP method and URL: 
    
    
    GET https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/insightTypes/google.iam.policy.LateralMovementInsight/insights

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         "https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/insightTypes/google.iam.policy.LateralMovementInsight/insights"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/insightTypes/google.iam.policy.LateralMovementInsight/insights" | Select-Object -Expand Content

The response lists all of the lateral movement insights for your project, folder, or organization. For example: 
    
    
    {
      "insights": [
        {
          "name": "projects/123456789012/locations/global/insightTypes/google.iam.policy.LateralMovementInsight/insights/13088eec-9573-415f-81a7-46e1a260e860",
          "description": "Service account sa-1@another-project.iam.gserviceaccount.com from another project can impersonate 2 service account(s) under this project.",
          "content": {
            "impersonator": {
              "serviceAccount": "sa-1@another-project.iam.gserviceaccount.com",
              "serviceAccountOwner": "//cloudresourcemanager.googleapis.com/projects/987654321098",
              "isGoogleManaged": false
            },
            "targetServiceAccounts": [
              "target-service-account-1@this-project.iam.gserviceaccount.com",
              "target-service-account-2@this-project.iam.gserviceaccount.com"
            ],
            "impersonationPolicy": {
              "resource": "//cloudresourcemanager.googleapis.com/projects/123456789012",
              "role": "roles/editor",
              "member": "serviceAccount:sa-1@another-project.iam.gserviceaccount.com",
              "condition": {
                "expression": "",
                "title": "",
                "description": "",
                "location": ""
              }
            },
            "impersonationPermissionUsage": [
              {
                "permission": "iam.serviceAccounts.actAs"
                "used": false
              }
            ],
            "hasPermissionUsageData": true
          },
          "lastRefreshTime": "2022-05-24T07:00:00Z",
          "observationPeriod": "7776000s",
          "stateInfo": {
            "state": "ACTIVE"
          },
          "category": "SECURITY",
          "associatedRecommendations": [
            {
              "recommendation": "projects/123456789012/locations/global/recommenders/google.iam.policy.Recommender/recommendations/03f3dc20-f9e7-4502-95ab-bf7d3164846f"
            }
          ],
          "targetResources": [
            "//cloudresourcemanager.googleapis.com/projects/123456789012"
          ],
          "insightSubtype": "CROSS_PROJECT_IMPERSONATION",
          "etag": "\"f48fa6a1b15c7741\"",
          "severity": "LOW"
        }
      ]
    }

To learn more about the components of an insight, see Review lateral movement insights on this page. 

## Get a single lateral movement insight

To get more information about a single insight, including the insight's description, status, and any recommendations it's associated with, use one of the following methods: 

### Console

  1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project,folder,organizationId)

  2. Select a project, folder, or organization.
  3. In the **Security insights** column, click a lateral movement insight. Lateral movement insights have the form `N service account impersonations`, where `N` is the number of service accounts that the service account in the role binding can impersonate. 




The Google Cloud console opens a pane showing the details of the insight. 

### gcloud

Use the [`gcloud recommender insights describe`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/describe) command with your insight ID to view information about a single insight. 

  * `INSIGHT_ID`: The ID of the insight that you want to view. To find the ID, list the insights for your project, folder, or organization. 
  * `RESOURCE_TYPE`: The resource type that you want to manage insights for. Use the value `project`, `folder`, or `organization`. 
  * `RESOURCE_ID`: The ID of the project, folder, or organization that you want to manage insights for. 


    
    
    gcloud recommender insights describe INSIGHT_ID \
        --insight-type=google.iam.policy.LateralMovementInsight \
        --RESOURCE_TYPE=RESOURCE_ID \
        --location=global

The output shows the insight in detail. For example, the following insight indicates that the IAM policy on project `123456789012` allows `sa-1@another-project.iam.gserviceaccount.com` to impersonate `target-service-account-1@this-project.iam.gserviceaccount.com` and `target-service-account-2@this-project.iam.gserviceaccount.com`. 
    
    
    associatedRecommendations:
    - recommendation: projects/123456789012/locations/global/recommenders/google.iam.policy.Recommender/recommendations/03f3dc20-f9e7-4502-95ab-bf7d3164846f
    category: SECURITY
    content:
      hasPermissionUsageData: true
      impersonationPermissionUsage:
      - permission: iam.serviceAccounts.actAs
        used: false
      impersonationPolicy:
        condition:
          description: ''
          expression: ''
          location: ''
          title: ''
        member: serviceAccount:sa-1@another-project.iam.gserviceaccount.com
        resource: //cloudresourcemanager.googleapis.com/projects/123456789012
        role: roles/editor
      impersonator:
        isGoogleManaged: false
        serviceAccount: sa-1@another-project.iam.gserviceaccount.com
        serviceAccountOwner: //cloudresourcemanager.googleapis.com/projects/987654321098
      targetServiceAccounts:
      - target-service-account-1@this-project.iam.gserviceaccount.com
      - target-service-account-2@this-project.iam.gserviceaccount.com
    description: Service account sa-1@another-project.iam.gserviceaccount.com from another project can impersonate 2 service account(s) under this project.
    etag: '"f48fa6a1b15c7741"'
    insightSubtype: CROSS_PROJECT_IMPERSONATION
    lastRefreshTime: '2022-05-24T07:00:00Z'
    name: projects/123456789012/locations/global/insightTypes/google.iam.policy.LateralMovementInsight/insights/13088eec-9573-415f-81a7-46e1a260e860
    observationPeriod: 7776000s
    severity: LOW
    stateInfo:
      state: ACTIVE
    targetResources:
    - //cloudresourcemanager.googleapis.com/projects/123456789012

To learn more about the components of an insight, see Review lateral movement insights on this page. 

### REST

The Recommender API's `[insights.get](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.insightTypes.insights/get)` method gets a single insight. 

Before using any of the request data, make the following replacements: 

  * `RESOURCE_TYPE`: The resource type that you want to manage insights for. Use the value `projects`, `folders`, or `organizations`. 
  * `RESOURCE_ID`: The ID of the project, folder, or organization that you want to manage insights for. 
  * `INSIGHT_ID`: The ID of the insight that you want to view. If you don't know the insight ID, you can find it by listing the insights in your project, folder, or organization. The ID of an insight is everything after `insights/` in the `name` field for the insight. 
  * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.



HTTP method and URL: 
    
    
    GET https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/insightTypes/google.iam.policy.LateralMovementInsight/insights/INSIGHT_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         "https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/insightTypes/google.iam.policy.LateralMovementInsight/insights/INSIGHT_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/insightTypes/google.iam.policy.LateralMovementInsight/insights/INSIGHT_ID" | Select-Object -Expand Content

The response contains the insight. For example, the following insight indicates that the IAM policy on project `123456789012` allows `sa-1@another-project.iam.gserviceaccount.com` to impersonate `target-service-account-1@this-project.iam.gserviceaccount.com` and `target-service-account-2@this-project.iam.gserviceaccount.com`. 
    
    
    {
      "name": "projects/123456789012/locations/global/insightTypes/google.iam.policy.LateralMovementInsight/insights/13088eec-9573-415f-81a7-46e1a260e860",
      "description": "Service account sa-1@another-project.iam.gserviceaccount.com from another project can impersonate 2 service account(s) under this project.",
      "content": {
        "impersonator": {
          "serviceAccount": "sa-1@another-project.iam.gserviceaccount.com",
          "serviceAccountOwner": "//cloudresourcemanager.googleapis.com/projects/987654321098",
          "isGoogleManaged": false
        },
        "targetServiceAccounts": [
          "target-service-account-1@this-project.iam.gserviceaccount.com",
          "target-service-account-2@this-project.iam.gserviceaccount.com"
        ],
        "impersonationPolicy": {
          "resource": "//cloudresourcemanager.googleapis.com/projects/123456789012",
          "role": "roles/editor",
          "member": "serviceAccount:sa-1@another-project.iam.gserviceaccount.com",
          "condition": {
            "expression": "",
            "title": "",
            "description": "",
            "location": ""
          }
        },
        "impersonationPermissionUsage": [
          {
            "permission": "iam.serviceAccounts.actAs"
            "used": false
          }
        ],
        "hasPermissionUsageData": true
      },
      "lastRefreshTime": "2022-05-24T07:00:00Z",
      "observationPeriod": "7776000s",
      "stateInfo": {
        "state": "ACTIVE"
      },
      "category": "SECURITY",
      "associatedRecommendations": [
        {
          "recommendation": "projects/123456789012/locations/global/recommenders/google.iam.policy.Recommender/recommendations/03f3dc20-f9e7-4502-95ab-bf7d3164846f"
        }
      ],
      "targetResources": [
        "//cloudresourcemanager.googleapis.com/projects/123456789012"
      ],
      "insightSubtype": "CROSS_PROJECT_IMPERSONATION",
      "etag": "\"f48fa6a1b15c7741\"",
      "severity": "LOW"
    }

To learn more about the components of an insight, see Review lateral movement insights on this page. 

## Review lateral movement insights

After you get a single insight, you can review its contents to understand the pattern of resource usage that it highlights. 

### Console

When you click a lateral movement insight in the Google Cloud console, the Google Cloud console opens a pane showing the details of the insight. The appearance of these details depends on whether the insight is associated with a recommendation. 

**Note:** You can check if an insight is associated with a recommendation by looking for the **Recommendation available** ![](https://docs.cloud.google.com/static/policy-intelligence/img/recommender-yes.svg) icon in the **Security insights** column. 

If the insight is associated with a recommendation, the pane shows the [details of the recommendation](https://docs.cloud.google.com/policy-intelligence/docs/review-apply-role-recommendations#review). 

If the insight is not associated with a recommendation, the pane shows the following: 

  * **The service account's origin project** : The project that the service account with impersonation permissions was created in. 

![](https://docs.cloud.google.com/static/policy-intelligence/img/lmi-origin-project.png)![](https://docs.cloud.google.com/static/policy-intelligence/img/lmi-origin-project.png)
  * **Service accounts that can be impersonated in this project.** A list of all of the service accounts in the current project that the service account with impersonation permissions can impersonate. 

![](https://docs.cloud.google.com/static/policy-intelligence/img/lmi-target-sa-list.png)![](https://docs.cloud.google.com/static/policy-intelligence/img/lmi-target-sa-list.png)
  * **Permissions that allow impersonation in the project** : A list of the impersonation permissions that the service account has. 

![](https://docs.cloud.google.com/static/policy-intelligence/img/lmi-impersonation-permissions.png)![](https://docs.cloud.google.com/static/policy-intelligence/img/lmi-impersonation-permissions.png)
  * **Current permissions** : A list of all of the service account's permissions. 

![](https://docs.cloud.google.com/static/policy-intelligence/img/lmi-all-permissions.png)![](https://docs.cloud.google.com/static/policy-intelligence/img/lmi-all-permissions.png)



### gcloud

An insight's content is determined by its subtypes. Lateral movement insights (`google.iam.policy.LateralMovementInsight`) insights have the `CROSS_PROJECT_IMPERSONATION` subtype. 

`CROSS_PROJECT_IMPERSONATION` insights have the following components, not necessarily in this order: 

  * `associatedRecommendations`: The identifiers for any recommendations associated with the insight. If there are no recommendations associated with the insight, this field is empty. 
  * `category`: The category for IAM insights is always `SECURITY`. 
  * `content`: Reports the details of the service account's ability to impersonate service accounts in other projects. This field contains the following components: 

    * `hasPermissionUsageData`: A boolean value indicating whether there is permission usage data for this role binding. Permission usage data indicates whether the permissions in the role binding have been used. This data is not available for conditional role bindings.
    * `impersonationPermissionUsage`: A list of impersonation permissions and their usage information. If a permission was used in the past 90 days, it's considered used. If not, it's considered unused. 

If `hasPermissionUsageData` is false, the `impersonationPermissionUsage` field is empty.

    * `impersonationPolicy`: Information about the role binding that gives the service account impersonation permissions.
    * `impersonator`: Details about the service account that has permission to impersonate service accounts in your project, including the following: 
      * `isGoogleManaged`: Whether the service account is owned and managed by Google.
      * `serviceAccount`: The email address of the service account.
      * `serviceAccountOwner`: The project that owns the service account. If Google owns the service account, the value of this field is `Google managed`. If a project outside of your organization owns the service account, the value of this field is `Unknown to your org`.
    * `targetServiceAccounts`: A list of the service accounts that the service account in the `impersonator` field has permission to impersonate. If the impersonator can impersonate more than 1500 service accounts, the list is empty. To learn how many service accounts the impersonator can impersonate, see the `description` field.
  * `description`: A human-readable summary of the insight. 
  * `etag`: A unique identifier for the current state of an insight. Each time the insight changes, a new `etag` value is assigned. 

To change the state of an insight, you must provide the `etag` of the existing insight. Using the `etag` helps ensure that any operations are performed only if the insight has not changed since you last retrieved it. 

  * `insightSubtype`: The insight subtype. 
  * `lastRefreshTime`: The date when the insight was last refreshed, which indicates the freshness of the data used to generate the insight. 
  * `name`: The name of the insight, in the following format:
        
        RESOURCE_TYPE/RESOURCE_ID/locations/global/insightTypes/google.iam.policy.LateralMovementInsight/insights/INSIGHT_ID

The placeholders have the following values:

    * `RESOURCE_TYPE`: The resource type that the insight was generated for. 
    * `RESOURCE_ID`: The ID of the project, folder, or organization where the insight was generated. 
    * `INSIGHT_ID`: A unique ID for the insight.
  * `observationPeriod`: The time period leading up to the insight. The source data used to generate the insight ends at `lastRefreshTime` and begins at `lastRefreshTime` minus `observationPeriod`. 
  * `severity`: The severity of the insight. All lateral movement insights have a severity of `LOW`. 
  * `stateInfo`: Insights go through multiple state transitions after they are proposed: 

    * `ACTIVE`: The insight has been generated, but either no actions have been taken, or an action was taken without updating the insight's state. Active insights are updated when the underlying data changes. 
    * `ACCEPTED`: Some action has been taken based on the insight. Insights become accepted when an associated recommendation was marked `CLAIMED`, `SUCCEEDED`, or `FAILED`, or the insight was accepted directly. When an insight is in the `ACCEPTED` state, the content of the insight cannot change. Accepted insights are retained for 90 days after they are accepted. 
  * `targetResources`: The [full resource name ](https://docs.cloud.google.com/iam/docs/full-resource-names) of the organization, folder, project, or service account that the insight is for. For example, `//cloudresourcemanager.googleapis.com/projects/123456789012`. 



### REST

An insight's content is determined by its subtypes. Lateral movement insights (`google.iam.policy.LateralMovementInsight`) insights have the `CROSS_PROJECT_IMPERSONATION` subtype. 

`CROSS_PROJECT_IMPERSONATION` insights have the following components, not necessarily in this order: 

  * `associatedRecommendations`: The identifiers for any recommendations associated with the insight. If there are no recommendations associated with the insight, this field is empty. 
  * `category`: The category for IAM insights is always `SECURITY`. 
  * `content`: Reports the details of the service account's ability to impersonate service accounts in other projects. This field contains the following components: 

    * `hasPermissionUsageData`: A boolean value indicating whether there is permission usage data for this role binding. Permission usage data indicates whether the permissions in the role binding have been used. This data is not available for conditional role bindings.
    * `impersonationPermissionUsage`: A list of impersonation permissions and their usage information. If a permission was used in the past 90 days, it's considered used. If not, it's considered unused. 

If `hasPermissionUsageData` is false, the `impersonationPermissionUsage` field is empty.

    * `impersonationPolicy`: Information about the role binding that gives the service account impersonation permissions.
    * `impersonator`: Details about the service account that has permission to impersonate service accounts in your project, including the following: 
      * `isGoogleManaged`: Whether the service account is owned and managed by Google.
      * `serviceAccount`: The email address of the service account.
      * `serviceAccountOwner`: The project that owns the service account. If Google owns the service account, the value of this field is `Google managed`. If a project outside of your organization owns the service account, the value of this field is `Unknown to your org`.
    * `targetServiceAccounts`: A list of the service accounts that the service account in the `impersonator` field has permission to impersonate. If the impersonator can impersonate more than 1500 service accounts, the list is empty. To learn how many service accounts the impersonator can impersonate, see the `description` field.
  * `description`: A human-readable summary of the insight. 
  * `etag`: A unique identifier for the current state of an insight. Each time the insight changes, a new `etag` value is assigned. 

To change the state of an insight, you must provide the `etag` of the existing insight. Using the `etag` helps ensure that any operations are performed only if the insight has not changed since you last retrieved it. 

  * `insightSubtype`: The insight subtype. 
  * `lastRefreshTime`: The date when the insight was last refreshed, which indicates the freshness of the data used to generate the insight. 
  * `name`: The name of the insight, in the following format:
        
        RESOURCE_TYPE/RESOURCE_ID/locations/global/insightTypes/google.iam.policy.LateralMovementInsight/insights/INSIGHT_ID

The placeholders have the following values:

    * `RESOURCE_TYPE`: The resource type that the insight was generated for. 
    * `RESOURCE_ID`: The ID of the project, folder, or organization where the insight was generated. 
    * `INSIGHT_ID`: A unique ID for the insight.
  * `observationPeriod`: The time period leading up to the insight. The source data used to generate the insight ends at `lastRefreshTime` and begins at `lastRefreshTime` minus `observationPeriod`. 
  * `severity`: The severity of the insight. All lateral movement insights have a severity of `LOW`. 
  * `stateInfo`: Insights go through multiple state transitions after they are proposed: 

    * `ACTIVE`: The insight has been generated, but either no actions have been taken, or an action was taken without updating the insight's state. Active insights are updated when the underlying data changes. 
    * `ACCEPTED`: Some action has been taken based on the insight. Insights become accepted when an associated recommendation was marked `CLAIMED`, `SUCCEEDED`, or `FAILED`, or the insight was accepted directly. When an insight is in the `ACCEPTED` state, the content of the insight cannot change. Accepted insights are retained for 90 days after they are accepted. 
  * `targetResources`: The [full resource name ](https://docs.cloud.google.com/iam/docs/full-resource-names) of the organization, folder, project, or service account that the insight is for. For example, `//cloudresourcemanager.googleapis.com/projects/123456789012`. 



## Mark a lateral movement insight as `ACCEPTED`

If you take action based on an active insight, you can mark that insight as `ACCEPTED`. The `ACCEPTED` state tells the Recommender API that you have taken action based on this insight, which helps refine your recommendations. 

Accepted insights are retained for 90 days after they are marked as `ACCEPTED`. 

### Console

If an insight is associated with a recommendation, [applying the recommendation](https://docs.cloud.google.com/iam/docs/recommender-managing) changes the insight's state to `ACCEPTED`. 

To mark an insight as `ACCEPTED` without applying a recommendation, use the gcloud CLI or REST API. 

### gcloud

Use the [ `gcloud recommender insights mark-accepted`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/mark-accepted) command with your insight ID to mark an insight as `ACCEPTED`. 

  * `INSIGHT_ID`: The ID of the insight that you want to view. To find the ID, list the insights for your project, folder, or organization. 
  * `RESOURCE_TYPE`: The resource type that you want to manage insights for. Use the value `project`, `folder`, or `organization`. 
  * `RESOURCE_ID`: The ID of the project, folder, or organization that you want to manage insights for. 
  * `ETAG`: An identifier for a version of the insight. To get the `etag`, do the following: 

    1. Get the insight using the `gcloud recommender insights describe` command. 
    2. Find and copy the `etag` value from the output, including the enclosing quotes. For example, `"d3cdec23cc712bd0"`. 


    
    
    gcloud recommender insights mark-accepted INSIGHT_ID \
        --insight-type=google.iam.policy.LateralMovementInsight \
        --RESOURCE_TYPE=RESOURCE_ID \
        --location=global \
        --etag=ETAG

The output shows the insight, now with the state of `ACCEPTED`: 
    
    
    associatedRecommendations:
    - recommendation: projects/123456789012/locations/global/recommenders/google.iam.policy.Recommender/recommendations/03f3dc20-f9e7-4502-95ab-bf7d3164846f
    category: SECURITY
    content:
      hasPermissionUsageData: true
      impersonationPermissionUsage:
      - permission: iam.serviceAccounts.actAs
        used: false
      impersonationPolicy:
        condition:
          description: ''
          expression: ''
          location: ''
          title: ''
        member: serviceAccount:sa-1@another-project.iam.gserviceaccount.com
        resource: //cloudresourcemanager.googleapis.com/projects/123456789012
        role: roles/editor
      impersonator:
        isGoogleManaged: false
        serviceAccount: sa-1@another-project.iam.gserviceaccount.com
        serviceAccountOwner: //cloudresourcemanager.googleapis.com/projects/987654321098
      targetServiceAccounts:
      - target-service-account-1@this-project.iam.gserviceaccount.com
      - target-service-account-2@this-project.iam.gserviceaccount.com
    description: Service account sa-1@another-project.iam.gserviceaccount.com from another project can impersonate 2 service account(s) under this project.
    etag: '"f48fa6a1b15c7741"'
    insightSubtype: CROSS_PROJECT_IMPERSONATION
    lastRefreshTime: '2022-05-24T07:00:00Z'
    name: projects/123456789012/locations/global/insightTypes/google.iam.policy.LateralMovementInsight/insights/13088eec-9573-415f-81a7-46e1a260e860
    observationPeriod: 7776000s
    severity: LOW
    **stateInfo :
      state: ACCEPTED**
    targetResources:
    - //cloudresourcemanager.googleapis.com/projects/123456789012

To learn more about the state info of an insight, see Review lateral movement insights on this page. 

### REST

The Recommender API's `[insights.markAccepted](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.insightTypes.insights/markAccepted)` method marks an insight as `ACCEPTED`. 

Before using any of the request data, make the following replacements: 

  * `RESOURCE_TYPE`: The resource type that you want to manage insights for. Use the value `projects`, `folders`, or `organizations`. 
  * `RESOURCE_ID`: The ID of the project, folder, or organization that you want to manage insights for. 
  * `INSIGHT_ID`: The ID of the insight that you want to view. If you don't know the insight ID, you can find it by listing the insights in your project, folder, or organization. The ID of an insight is everything after `insights/` in the `name` field for the insight. 
  * `ETAG`: An identifier for a version of the insight. To get the `etag`, do the following: 
    1. Get the insight using the `insights.get` method.
    2. Find and copy the `etag` value from the response.
  * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.



HTTP method and URL: 
    
    
    POST https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/insightTypes/google.iam.policy.LateralMovementInsight/insights/INSIGHT_ID:markAccepted

Request JSON body: 
    
    
    {
      "etag": "ETAG"
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
         "https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/insightTypes/google.iam.policy.LateralMovementInsight/insights/INSIGHT_ID:markAccepted"

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
        -Uri "https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/insightTypes/google.iam.policy.LateralMovementInsight/insights/INSIGHT_ID:markAccepted" | Select-Object -Expand Content

The response contains the insight, now with the state of `ACCEPTED`: 
    
    
    {
      "name": "projects/123456789012/locations/global/insightTypes/google.iam.policy.LateralMovementInsight/insights/13088eec-9573-415f-81a7-46e1a260e860",
      "description": "Service account sa-1@another-project.iam.gserviceaccount.com from another project can impersonate 2 service account(s) under this project.",
      "content": {
        "impersonator": {
          "serviceAccount": "sa-1@another-project.iam.gserviceaccount.com",
          "serviceAccountOwner": "//cloudresourcemanager.googleapis.com/projects/987654321098",
          "isGoogleManaged": false
        },
        "targetServiceAccounts": [
          "target-service-account-1@this-project.iam.gserviceaccount.com",
          "target-service-account-2@this-project.iam.gserviceaccount.com"
        ],
        "impersonationPolicy": {
          "resource": "//cloudresourcemanager.googleapis.com/projects/123456789012",
          "role": "roles/editor",
          "member": "serviceAccount:sa-1@another-project.iam.gserviceaccount.com",
          "condition": {
            "expression": "",
            "title": "",
            "description": "",
            "location": ""
          }
        },
        "impersonationPermissionUsage": [
          {
            "permission": "iam.serviceAccounts.actAs"
            "used": false
          }
        ],
        "hasPermissionUsageData": true
      },
      "lastRefreshTime": "2022-05-24T07:00:00Z",
      "observationPeriod": "7776000s",
      **"stateInfo": {
        "state": "ACCEPTED"
      },**
      "category": "SECURITY",
      "associatedRecommendations": [
        {
          "recommendation": "projects/123456789012/locations/global/recommenders/google.iam.policy.Recommender/recommendations/03f3dc20-f9e7-4502-95ab-bf7d3164846f"
        }
      ],
      "targetResources": [
        "//cloudresourcemanager.googleapis.com/projects/123456789012"
      ],
      "insightSubtype": "CROSS_PROJECT_IMPERSONATION",
      "etag": "\"f48fa6a1b15c7741\"",
      "severity": "LOW"
    }

To learn more about the state info of an insight, see Review lateral movement insights on this page. 

## What's next

  * Learn how to [review and apply policy recommendations](https://docs.cloud.google.com/policy-intelligence/docs/review-apply-role-recommendations).
  * Use the [Active Assist](https://docs.cloud.google.com/recommender/docs/recommendation-hub/identify-configuration-problems) to view and manage all recommendations for your project, including IAM recommendations.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
