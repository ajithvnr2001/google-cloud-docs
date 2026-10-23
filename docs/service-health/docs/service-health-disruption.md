---
url: https://docs.cloud.google.com/service-health/docs/service-health-disruption/
title: Check for disruptions with Personalized Service Health \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:53:09.537125+00:00
---

# Check for disruptions with Personalized Service Health  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-health/docs/service-health-disruption/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Personalized Service Health ](https://docs.cloud.google.com/service-health/docs)
  * [ Guides ](https://docs.cloud.google.com/service-health/docs/overview)



Send feedback 

#  Check for disruptions with Personalized Service Health Stay organized with collections  Save and categorize content based on your preferences. 

This document explains what to do if Personalized Service Health is experiencing a disruption.

Personalized Service Health may be affected by an incident, partially or completely. You can check for incidents, processing problems, and performance issues with Service Health through the Status API resource and the Google Cloud Service Health dashboard.

## Use the Status API

The Status API resource of the Service Health API tells you if specific Service Health features are experiencing issues.

### Before you begin

To start using the Status API:

  1. [Enable the Service Health API](https://docs.cloud.google.com/service-health/docs/manage-access#enable-service-health-api-single-project) for the project or organization that you will use to access this status.
  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  3. Set [permissions to access the Service Health API](https://docs.cloud.google.com/service-health/docs/manage-access#access-service-health-api-dashboard).
  4. Configure Identity and Access Management (IAM) permissions on your project or organization to use the Status API. 

To configure permissions on your project, run the following command:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
         --member {USER|GROUP|SERVICE_ACCOUNT} \
         --role roles/servicehealth.viewer
         

To configure permissions on your organization, run the following command:
         
         gcloud organizations add-iam-policy-binding ORGANIZATION_ID \
         --member {USER|GROUP|SERVICE_ACCOUNT} \
         --role roles/servicehealth.viewer
         

To get your ORGANIZATION_ID, see [Getting your organization resource ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).




The IAM policies granted on an organization are inherited by all projects in the organization. These policies let you access organization and project event APIs across the organization.

### References

See the [Status API reference](https://docs.cloud.google.com/service-health/docs/reference/rest/v1beta/Status) for the method you can use and the meaning of the fields in the response.

When setting the product or location, use the values found at [Google Cloud products](https://docs.cloud.google.com/service-health/docs/supported-products-locations) and [locations](https://docs.cloud.google.com/service-health/docs/supported-products-locations#locations).

### Get Service Health status using a project ID

To get the status of Service Health using a project ID, use the following request:
    
    
    GET https://servicehealth.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/status
    

If the status value is `OK`, the request yields the following response:
    
    
    {
      "state": "OK",
    }
    

This status indicates that the features accessed using the project ID such as events or [impacts](https://docs.cloud.google.com/service-health/docs/reference/rest/v1beta/organizations.locations.organizationImpacts) aren't experiencing problems internally.

If the status value is `ISSUES_DETECTED`, the request yields the following response:
    
    
    {
      "state": "ISSUES_DETECTED",
      "issues": [
        {
          "message": "We are experiencing problems creating new events",
          "details": {
            "API": "events"
          }
        },
        {
          "message": "We are experiencing problems creating new impacts",
          "details": {
            "API": "impacts"
          }
        }
      ]
    }
    

An `ISSUES_DETECTED` state also returns a set of issues, indicating that features accessed using the project ID may not be accurate.

If you don't have [permissions](https://docs.cloud.google.com/service-health/docs/manage-access#set_required_permissions) to get the status, you will get a `PERMISSION_DENIED` error.
    
    
    {
      "error": {
        "code": 403,
        "message": "Permission 'servicehealth.statuses.get' denied on resource '//servicehealth.googleapis.com/projects/PROJECT_ID/locations/global/status' (or it may not exist).",
        "status": "PERMISSION_DENIED",
        "details": [
          {
            "@type": "type.googleapis.com/google.rpc.ErrorInfo",
            "reason": "IAM_PERMISSION_DENIED",
            "domain": "servicehealth.googleapis.com",
            "metadata": {
              "resource": "projects/PROJECT_ID/locations/global/status",
              "permission": "servicehealth.statuses.get"
            }
          }
        ]
      }
    }
    

### Get Service Health status using an organization ID

To get the status, use the following request:
    
    
    GET https://servicehealth.googleapis.com/v1beta/organizations/ORGANIZATION_ID/locations/global/status
    

If Service Health is operating without issues, the status should yield the following response:
    
    
    {
      "state": "OK",
    }
    

If Service Health is experiencing issues that may affect its accuracy or capability, the status should yield a response with the `ISSUES_DETECTED` state:
    
    
    {
      "state": "ISSUES_DETECTED",
      "issues": [
        {
          "message": "We are experiencing problems creating new organization level events",
          "details": {
            "API": "organizationEvents"
          }
        },
        {
          "message": "We are experiencing problems creating new organization level impacts",
          "details": {
            "API": "organizationImpacts"
          }
        }
      ]
    }
    

If you don't have the [permissions](https://docs.cloud.google.com/service-health/docs/manage-access#set_required_permissions) to get the status, you will get a `PERMISSION_DENIED` error.
    
    
    {
      "error": {
        "code": 403,
        "message": "Permission 'servicehealth.statuses.get denied on resource '//servicehealth.googleapis.com/organizations/ORGANIZATION_ID/locations/global/status' (or it may not exist).",
        "status": "PERMISSION_DENIED",
        "details": [
          {
            "@type": "type.googleapis.com/google.rpc.ErrorInfo",
            "reason": "IAM_PERMISSION_DENIED",
            "domain": "servicehealth.googleapis.com",
            "metadata": {
              "resource": "organizations/ORGANIZATION_ID/locations/global/status",
              "permission": "servicehealth.statuses.get"
            }
          }
        ]
      }
    }
    

## Check Google Cloud Service Health

[Google Cloud Service Health](https://status.cloud.google.com/) tells you if Personalized Service Health is experiencing an issue. You can also use an RSS feed to consume the data.

For more information on Google Cloud Service Health, see [Incidents and Google Cloud Service Health](https://docs.cloud.google.com/support/docs/dashboard).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
