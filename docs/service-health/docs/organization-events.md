---
url: https://docs.cloud.google.com/service-health/docs/organization-events/
title: Access organization events with the Personalized Service Health API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:33:10.057139+00:00
---

# Access organization events with the Personalized Service Health API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-health/docs/organization-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Personalized Service Health ](https://docs.cloud.google.com/service-health/docs)
  * [ Guides ](https://docs.cloud.google.com/service-health/docs/overview)



Send feedback 

#  Access organization events with the Personalized Service Health API Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to use the Service Health API to access [events](https://docs.cloud.google.com/service-health/docs/concepts#service_health_event) affecting your organization. 

Personalized Service Health provides the OrganizationEvents and OrganizationImpacts API resources, which let you get information on events that affect your organization. This information includes:

  * Service health events that may impact one or more projects in an organization.
  * List of projects that may be or are impacted by an event affecting your organization.



To learn how to view organization-level [incidents](https://docs.cloud.google.com/service-health/docs/concepts#incident) in the Google Cloud console, see [View organization incidents in the Google Cloud console](https://docs.cloud.google.com/service-health/docs/organization-views).

## Before you begin

  1. [Enable the Service Health API](https://docs.cloud.google.com/service-health/docs/manage-access#enable-service-health-api-single-project) for at least one project under your organization. The OrganizationEvents and OrganizationImpacts API resources get information only for projects that have the Service Health API enabled.
  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  3. Set [permissions to access the Service Health API](https://docs.cloud.google.com/service-health/docs/manage-access#access-service-health-api-dashboard).
  4. Configure Identity and Access Management (IAM) permissions on your organization to use the OrganizationEvents and OrganizationImpacts API resources. Run the following command: 
         
         gcloud organizations add-iam-policy-binding $ORGANIZATION_ID \
           --member {USER|GROUP|SERVICE_ACCOUNT} \
           --role roles/servicehealth.viewer
         

To get your ORGANIZATION_ID, see [Getting your organization resource ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).

The IAM policies granted on an organization are inherited by all projects in the organization. These policies allow you to access organization and project event APIs across the organization.




## References

See the [OrganizationEvents](https://docs.cloud.google.com/service-health/docs/reference/rest/v1/organizations.locations.organizationEvents) and [OrganizationImpacts](https://docs.cloud.google.com/service-health/docs/reference/rest/v1/organizations.locations.organizationImpacts) API reference for the methods you can use, and the meaning of the fields in the response. In the API response, each entry in the `impact` list includes the granular disruption `state` (`AFFECTED` or `RESOLVED`), `startTime`, and `endTime` (when resolved) for each impacted product and location.

When setting the product or location, use the values found at [Google Cloud products](https://docs.cloud.google.com/service-health/docs/supported-products-locations) and [locations](https://docs.cloud.google.com/service-health/docs/supported-products-locations#locations).

## List projects under an organization that may be affected by an event

See the [quickstart](https://docs.cloud.google.com/service-health/docs/list-events#list_projects_under_an_organization_that_may_be_affected_by_an_event).

## List all active incidents for an organization

See the [quickstart](https://docs.cloud.google.com/service-health/docs/list-events#list_all_active_incidents_for_an_organization).

## Get details for an event affecting an organization

You can use the Get API to view detailed information about an event affecting an organization.

Before using any of the request data, make the following replacements: 

  * API_VERSION: the API version to use. Use `v1` or `v1beta`.
  * ORGANIZATION_ID: your Google Cloud organization ID.
  * EVENT_ID: the ID of the event.
  * PROJECT_ID: the project ID used for quota and billing.



HTTP method and URL: 
    
    
    GET https://servicehealth.googleapis.com/API VERSION/organizations/ORGANIZATION_ID/locations/global/organizationEvents/EVENT_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         "https://servicehealth.googleapis.com/API VERSION/organizations/ORGANIZATION_ID/locations/global/organizationEvents/EVENT_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://servicehealth.googleapis.com/API VERSION/organizations/ORGANIZATION_ID/locations/global/organizationEvents/EVENT_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "organizations/ORGANIZATION_ID/locations/global/organizationEvents/EVENT_ID",
         "title": "We are experiencing a connectivity issue affecting Google Cloud SQL in us-east1, australia-southeast2.",
          "description": "The issue with Google Cloud SQL has been resolved for all affected projects as of Tuesday, 2022-10-18 11:00 US/Pacific. We thank you for your patience while we worked on resolving the issue.",
          "category": "INCIDENT",
          "detailedCategory": "CONFIRMED_INCIDENT",
          "state": "CLOSED",
          "detailedState": "RESOLVED",
          "eventImpacts": [
            {
              "product": {
                "productName": "Google Cloud SQL",
                "id": "hV87iK5DcEXKgWU2kDri",
              },
              "location": {
                "locationName": "us-central1",
              }
            }
          ],
       "updates": [
        {
          "updateTime": "2022-10-18T17:41:20.112287Z",
                  "title": "We are experiencing a connectivity issue affecting Google Cloud SQL in us-east1, australia-southeast2.",
          "description": "We are experiencing an intermittent issue with Google Cloud SQL. Our engineering team continues to investigate the issue.",
          "symptom": "None at this time.",
          "workaround": "None at this time."
        },
        {
          "updateTime": "2022-10-18T18:00:05.690761Z",
          "title": "We are experiencing a connectivity issue affecting Google Cloud SQL in us-east1, australia-southeast2.",
          "description": "The issue with Google Cloud SQL has been resolved for all affected projects as of Tuesday, 2022-10-18 11:00 US/Pacific.\n\nWe thank you for your patience while we worked on resolving the issue.",
          "symptom": "None at this time.",
          "workaround": "None at this time."
        }
      ],
      "updateTime": "2022-10-18T18:00:05.690761Z",
      "startTime": "2022-10-18T17:41:20.112287Z",
      "endTime":  "2022-10-18T18:00:05.690761Z",
    }
    

If you don't have permissions to get events, you will get the following `PERMISSION_DENIED` error.
    
    
    {
      "error": {
        "code": 403,
        "message": "Permission 'servicehealth.organizationEvents.get' denied on resource '//servicehealth.googleapis.com/organizations/ORGANIZATION_ID/locations/global/organizationEvents/EVENT_ID' (or it may not exist).",
        "status": "PERMISSION_DENIED",
        "details": [
          {
            "@type": "type.googleapis.com/google.rpc.ErrorInfo",
            "reason": "IAM_PERMISSION_DENIED",
            "domain": "servicehealth.googleapis.com",
            "metadata": {
              "resource": "organizations/ORGANIZATION_ID/locations/global/organizationEvents/EVENT_ID",
              "permission": "servicehealth.organizationEvents.get"
            }
          }
        ]
      }
    }
    

To fix this error, set the [required permissions](https://docs.cloud.google.com/service-health/docs/manage-access#access-service-health-api-dashboard).

## Get details for a project under an organization that may be affected by an event

For a given event, the event ID remains the same between your project and organization events. [`OrganizationImpact`](https://docs.cloud.google.com/service-health/docs/reference/rest/v1/organizations.locations.organizationImpacts#resource:-organizationimpact) contains an EVENT_ID and a PROJECT_NUMBER, which you can use to [get details for an event](https://docs.cloud.google.com/service-health/docs/project-events#get_incident_details) affecting your project. These details include [`state`](https://docs.cloud.google.com/service-health/docs/reference/rest/v1/projects.locations.events#state) and [`relevance`](https://docs.cloud.google.com/service-health/docs/reference/rest/v1/projects.locations.events#relevance).

PROJECT_NUMBER is interchangeable with PROJECT_ID, which the Get API returns.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
