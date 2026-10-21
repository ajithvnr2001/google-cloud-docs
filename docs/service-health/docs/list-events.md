---
url: https://docs.cloud.google.com/service-health/docs/list-events/
title: Quickstart: List events affecting a project or organization using the Service Health API \u00a0|\u00a0 Personalized Service Health \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:50:05.354726+00:00
---

# Quickstart: List events affecting a project or organization using the Service Health API  |  Personalized Service Health  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-health/docs/list-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Personalized Service Health ](https://docs.cloud.google.com/service-health/docs)
  * [ Guides ](https://docs.cloud.google.com/service-health/docs/overview)



Send feedback 

#  Quickstart: List events affecting a project or organization using the Service Health API Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to list service health events that might be impacting or have impacted Google Cloud products in your Google Cloud project or organization. You'll use the Service Health API.

## Before you begin

  1. Enable the Service Health API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable servicehealth.googleapis.com

  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  3. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions.



### Required roles

To get the permissions that you need to list service health events, ask your administrator to grant you the [Personalized Service Health Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/servicehealth#servicehealth.viewer) (`roles/servicehealth.viewer`) IAM role on the project or organization that you want to list events for. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** Granting a user a role on an organization gives the user those permissions on the organization _and_ on all projects, folders, and resources within that organization. For more information, see [Using the resource hierarchy for access control](https://docs.cloud.google.com/iam/docs/resource-hierarchy-access-control).

## References

See the Events ([v1](https://docs.cloud.google.com/service-health/docs/reference/rest/v1/projects.locations.events),[v1beta](https://docs.cloud.google.com/service-health/docs/reference/rest/v1beta/projects.locations.events)), OrganizationEvents ([v1](https://docs.cloud.google.com/service-health/docs/reference/rest/v1/organizations.locations.organizationEvents),[v1beta](https://docs.cloud.google.com/service-health/docs/reference/rest/v1beta/organizations.locations.organizationEvents)) and OrganizationImpacts ([v1](https://docs.cloud.google.com/service-health/docs/reference/rest/v1/organizations.locations.organizationImpacts), [v1beta](https://docs.cloud.google.com/service-health/docs/reference/rest/v1beta/organizations.locations.organizationImpacts)) API references for the methods you can use and the meaning of the fields in the response.

When setting the product or location, use the values found at [Google Cloud products](https://docs.cloud.google.com/service-health/docs/supported-products-locations) and [locations](https://docs.cloud.google.com/service-health/docs/supported-products-locations#locations).

## List all active incidents for a project

You can list all Google Cloud incidents for a specific Google Cloud project.

Before using any of the request data, make the following replacements: 

  * API_VERSION: The API version to use. Use `v1` or `v1beta`.
  * PROJECT_ID: the ID of the project.



HTTP method and URL: 
    
    
    GET https://servicehealth.googleapis.com/API_VERSION/projects/PROJECT_ID/locations/global/events?filter=state=ACTIVE%20category=INCIDENT&page_size=2&page_token={page_token}

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://servicehealth.googleapis.com/API_VERSION/projects/PROJECT_ID/locations/global/events?filter=state=ACTIVE%20category=INCIDENT&page_size=2&page_token={page_token}"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://servicehealth.googleapis.com/API_VERSION/projects/PROJECT_ID/locations/global/events?filter=state=ACTIVE%20category=INCIDENT&page_size=2&page_token={page_token}" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "events": [
        {
          "name": "projects/PROJECT_ID/locations/global/events/event-123",
          "title": "We are experiencing a connectivity issue affecting Google Cloud SQL in us-east1, australia-southeast2.",
          "description": "The issue with Google Cloud SQL has been resolved for all affected projects. We thank you for your patience while we worked on resolving the issue.",
          "category": "INCIDENT",
          "detailedCategory": "CONFIRMED_INCIDENT",
          "state": "ACTIVE",
          "detailedState": "CONFIRMED",
          "eventImpacts": [
            {
              "product": {
                "productName": "Google Cloud SQL",
                "id": "hV87iK5DcEXKgWU2kDri",
              },
              "location": {
                "locationName": "asia-east2",
              }
            },
            {
              "product": {
                "productName": "Google Cloud SQL",
                "id": "hV87iK5DcEXKgWU2kDri",
              },
              "location": {
                "locationName": "asia-southeast1",
              }
            }
          ],
          "relevance": "RELATED",
          "updateTime": "2022-10-18T17:44:05.690761Z",
          "startTime": "2022-10-18T17:41:20.112287Z",
        },
        {
          "name": "projects/PROJECT_ID/locations/global/events/event-567",
          "title": "Cloud Firestore may experience errors.",
          "description": "Mitigation work is currently underway by our engineering team. The mitigation is expected to complete by 2022-10-07T16:30:00Z.",
          "category": "INCIDENT",
          "detailedCategory": "CONFIRMED_INCIDENT",
          "state": "ACTIVE",
          "detailedState": "CONFIRMED",
          "eventImpacts": [
            {
              "product": {
                "productName": "Cloud Firestore",
                "id": "CETSkT92V21G6A1x28me",
              },
              "location": {
                "locationName": "us-central1-a",
              }
            }
          ],
          "relevance": "RELATED",
          "updateTime": "2022-10-07T15:19:59.409530Z",
          "startTime": "2022-10-07T15:10:35.887125Z",
          "nextUpdateTime": "2022-10-07T16:30:00Z"
        }
      ],
      "nextPageToken": "CgwIw8bDmgYQz4nUlgMQChomcHJvamVjdHMvcHNoLW1hbnVhbC"
    }
    

**Note:** **If the response is large, this example will not list all incidents.** The Service Health API will return a non-empty `nextPageToken`. Provide this value in a subsequent request as a query string to return the next page of results.

If you don't have [required permissions](https://docs.cloud.google.com/service-health/docs/manage-access#set_required_permissions) to list events, you will get a `PERMISSION_DENIED` error.
    
    
    {
      "error": {
        "code": 403,
        "message": "Permission 'servicehealth.events.list' denied on resource '//servicehealth.googleapis.com/projects/PROJECT_ID/locations/global' (or it may not exist).",
        "status": "PERMISSION_DENIED",
        "details": [
          {
            "@type": "type.googleapis.com/google.rpc.ErrorInfo",
            "reason": "IAM_PERMISSION_DENIED",
            "domain": "servicehealth.googleapis.com",
            "metadata": {
              "resource": "projects/PROJECT_ID/locations/global",
              "permission": "servicehealth.events.list"
            }
          }
        ]
      }
    }
    

## List all active incidents for an organization

You can list all Google Cloud incidents affecting any project that have enabled Personalized Service Health in the specific Google Cloud organization.

Before using any of the request data, make the following replacements: 

  * API_VERSION: the API version to use. Use `v1` or `v1beta`.
  * ORGANIZATION_ID: your Google Cloud organization ID.
  * PROJECT_ID: the project ID used for quota and billing.



HTTP method and URL: 
    
    
    GET https://servicehealth.googleapis.com/API_VERSION/organizations/ORGANIZATION_ID/locations/global/organizationEvents?filter=state=ACTIVE%20category=INCIDENT&page_size=2&page_token={page_token}

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         "https://servicehealth.googleapis.com/API_VERSION/organizations/ORGANIZATION_ID/locations/global/organizationEvents?filter=state=ACTIVE%20category=INCIDENT&page_size=2&page_token={page_token}"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://servicehealth.googleapis.com/API_VERSION/organizations/ORGANIZATION_ID/locations/global/organizationEvents?filter=state=ACTIVE%20category=INCIDENT&page_size=2&page_token={page_token}" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "organization_events": [
        {
          "name": "organizations/ORGANIZATION_ID/locations/global/organizationEvents/event-123",
          "title": "We are experiencing a connectivity issue affecting Google Cloud SQL in us-east1, australia-southeast2.",
          "description": "The issue with Google Cloud SQL has been resolved for all affected projects. We thank you for your patience while we worked on resolving the issue.",
          "category": "INCIDENT",
          "detailedCategory": "CONFIRMED_INCIDENT",
          "state": "ACTIVE",
          "detailedState": "CONFIRMED",
          "eventImpacts": [
            {
              "product": {
                "productName": "Google Cloud SQL",
                "id": "hV87iK5DcEXKgWU2kDri",
              },
              "location": {
                "locationName": "asia-east2",
              }
            },
            {
              "product": {
                "productName": "Google Cloud SQL",
                "id": "hV87iK5DcEXKgWU2kDri",
              },
              "location": {
                "locationName": "asia-southeast1",
              }
            }
          ],
          "updateTime": "2022-10-18T17:44:05.690761Z",
          "startTime": "2022-10-18T17:41:20.112287Z",
        },
        {
          "name": "organizations/ORGANIZATION_ID/locations/global/organizationEvents/event-567",
          "title": "Cloud Firestore may experience errors.",
          "description": "Mitigation work is currently underway by our engineering team. The mitigation is expected to complete by 2022-10-07T16:30:00Z.",
          "category": "INCIDENT",
          "detailedCategory": "CONFIRMED_INCIDENT",
          "state": "ACTIVE",
          "detailedState": "CONFIRMED",
          "eventImpacts": [
            {
              "product": {
                "productName": "Cloud Firestore",
                "id": "CETSkT92V21G6A1x28me",
              },
              "location": {
                "locationName": "us-central1-a",
              }
            }
          ],
          "updateTime": "2022-10-07T15:19:59.409530Z",
          "startTime": "2022-10-07T15:10:35.887125Z",
          "nextUpdateTime": "2022-10-07T16:30:00Z"
        }
      ],
      "nextPageToken": "CgwIw8bDmgYQz4nUlgMQChomcHJvamVjdHMvcHNoLW1hbnVhbC"
    }
    

To get your ORGANIZATION_ID, see [Getting your organization resource ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).

**Note:** If the response is large, this example won't list all incidents. The Service Health API will return a non-empty nextPageToken. Provide this value in a subsequent request as a query string to return the next page of results.

If you don't have [permissions to list events](https://docs.cloud.google.com/service-health/docs/manage-access#access-service-health-api-dashboard), you will get a `PERMISSION_DENIED` error.
    
    
    {
      "error": {
        "code": 403,
        "message": "Permission 'servicehealth.organizationEvents.list' denied on resource '//servicehealth.googleapis.com/organizations/ORGANIZATION_ID/locations/global' (or it may not exist).",
        "status": "PERMISSION_DENIED",
        "details": [
          {
            "@type": "type.googleapis.com/google.rpc.ErrorInfo",
            "reason": "IAM_PERMISSION_DENIED",
            "domain": "servicehealth.googleapis.com",
            "metadata": {
              "resource": "organizations/<var class="readonly">ORGANIZATION_ID</var>/locations/global",
              "permission": "servicehealth.organizationEvents.list"
            }
          }
        ]
      }
    }
    

## List projects under an organization that may be affected by an event

You can list all projects under a specific Google Cloud organization that:

  * May be affected by an event ([`OrganizationImpact`](https://docs.cloud.google.com/service-health/docs/reference/rest/v1/organizations.locations.organizationImpacts)).
  * Have enabled Personalized Service Health.



Before using any of the request data, make the following replacements: 

  * API_VERSION: the API version to use. Use `v1` or `v1beta`.
  * EVENT_ID: the ID of the event that may be affecting an organization.
  * ORGANIZATION_ID: your Google Cloud organization ID.
  * PROJECT_ID: the project ID used for quota and billing.



HTTP method and URL: 
    
    
    GET https://servicehealth.googleapis.com/API_VERSION/organizations/ORGANIZATION_ID/locations/global/organizationImpacts?filter=events:organizations%2FORGANIZATION_ID%2Flocations%2Fglobal%2FEVENT_ID&page_size=2&page_token={page_token}

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         "https://servicehealth.googleapis.com/API_VERSION/organizations/ORGANIZATION_ID/locations/global/organizationImpacts?filter=events:organizations%2FORGANIZATION_ID%2Flocations%2Fglobal%2FEVENT_ID&page_size=2&page_token={page_token}"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://servicehealth.googleapis.com/API_VERSION/organizations/ORGANIZATION_ID/locations/global/organizationImpacts?filter=events:organizations%2FORGANIZATION_ID%2Flocations%2Fglobal%2FEVENT_ID&page_size=2&page_token={page_token}" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "organization_impacts": [
        {
          "name": "organizations/ORGANIZATION_ID/locations/global/organizationImpacts/impact-123",
          "events": [
            "organizations/ORGANIZATION_ID/locations/global/organizationEvents/EVENT_ID",
          ],
          "asset": {
            "assetName": "//cloudresourcemanager.googleapis.com/projects/{PROJECT_NUMBER_1}",
            "assetType": "cloudresourcemanager.googleapis.com/Project",
          },
          "updateTime": "2022-10-18T17:44:05.690761Z",
        },
        {
          "name": "organizations/ORGANIZATION_ID/locations/global/organizationImpacts/impact-234",
          "events": [
            "organizations/ORGANIZATION_ID/locations/global/organizationEvents/EVENT_ID",
          ],
          "asset": {
            "assetName": "//cloudresourcemanager.googleapis.com/projects/{PROJECT_NUMBER_2}",
            "assetType": "cloudresourcemanager.googleapis.com/Project",
          },
          "updateTime": "2022-10-18T17:44:05.690761Z",
        }
      ],
      "nextPageToken": "CgwIw8bDmgYQz4nUlgMQChomcHJvamVjdHMvcHNoLW1hbnVhbC"
    }
    

If you don't have the [permissions to list events](https://docs.cloud.google.com/service-health/docs/manage-access#access-service-health-api-dashboard), you will get the following `PERMISSION_DENIED` error.
    
    
    {
      "error": {
        "code": 403,
        "message": "Permission 'servicehealth.organizationImpacts.list' denied on resource '//servicehealth.googleapis.com/organizations/ORGANIZATION_ID/locations/global' (or it may not exist).",
        "status": "PERMISSION_DENIED",
        "details": [
          {
            "@type": "type.googleapis.com/google.rpc.ErrorInfo",
            "reason": "IAM_PERMISSION_DENIED",
            "domain": "servicehealth.googleapis.com",
            "metadata": {
              "resource": "organizations/ORGANIZATION_ID/locations/global",
              "permission": "servicehealth.organizationImpacts.list"
            }
          }
        ]
      }
    }
    

**Note:** If the response is large, this example won't list all incidents. The Service Health API will return a non-empty nextPageToken. Provide this value in a subsequent request as a query string to return the next page of results.

## What's next

See how-tos for pulling event information by [project](https://docs.cloud.google.com/service-health/docs/project-events) or [organization](https://docs.cloud.google.com/service-health/docs/organization-events) using the Service Health API.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
