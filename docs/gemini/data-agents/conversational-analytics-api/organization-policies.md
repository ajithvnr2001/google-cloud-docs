---
url: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/organization-policies/
title: Organization policy constraints \u00a0|\u00a0 Conversational Analytics API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:02:49.367693+00:00
---

# Organization policy constraints  |  Conversational Analytics API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/organization-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Conversational Analytics API ](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/overview)



Send feedback 

#  Organization policy constraints Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to use [Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) to manage Conversational Analytics API resources.

The Organization Policy Service provides centralized control over your Google Cloud resources through constraints that restrict how resources can be configured and used. You can apply these constraints to data agents and conversations at the organization, folder, or project level. By default, child resources inherit the policies of their parent resources.

To enforce a constraint, you create an organization policy and attach it to a resource in your resource hierarchy. You can set and manage these policies by using the Google Cloud console or the gcloud CLI. For detailed instructions, see [Creating and managing organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies).

## Before you begin

Before you can apply organization policies to restrict Conversational Analytics API resources, ensure that you have the required Identity and Access Management (IAM) roles.

### Required roles

To get the permissions that you need to manage or view organization policies, ask your administrator to grant you the following IAM roles: 

  * Manage organization policies: [Organization Policy Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) on the organization 
  * View organization policies: [Organization Policy Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyViewer) (`roles/orgpolicy.policyViewer`) on the organization, folder, or project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Predefined constraints

You can apply organization policies that use the following predefined constraints to restrict Conversational Analytics API resources. If you don't set an organization policy for a constraint, the default behavior is to allow all relevant actions.

Constraint | Description | Default behavior  
---|---|---  
`gcp.restrictServiceUsage` | Restricts whether the Conversational Analytics API service can be used in your resource hierarchy. | Using the Conversational Analytics API service is not restricted.  
`gcp.resourceLocations` | Limits the locations where data agents and conversations can be created. | Conversational Analytics API resources can be created in any supported location.  
  
### Restrict service usage

The [`constraints/gcp.restrictServiceUsage`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-services) constraint lets you control which Google Cloud services can be used in your resource hierarchy.

To restrict the Conversational Analytics API, you can add the Gemini Data Analytics service (`geminidataanalytics.googleapis.com`) to a denylist for this constraint, or you can omit it from an allowlist.

If you use an allowlist, you must also include any underlying data source services that the API uses, such as the BigQuery service (`bigquery.googleapis.com`) or the Looker (Google Cloud core) service (`looker.googleapis.com`). If any of these services are restricted, then users can't create or interact with data agents and conversations.

### Restrict resource locations

The [`constraints/gcp.resourceLocations`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) constraint limits the creation of new Conversational Analytics API data agents and conversations to specified Google Cloud locations. For a list of supported regions and multi-regions for the API, see [Conversational Analytics API locations](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/locations).

If this policy is enforced, any attempt to create a resource within a denied location fails. Existing Conversational Analytics API resources are not affected by changes to this policy.

To learn how to specify locations in your organization policy, see [Restrict resource locations](https://docs.cloud.google.com/organization-policy/restrict-locations).

## Troubleshoot policy violations

If a request violates an organization policy, the Conversational Analytics API returns an error with an HTTP status code of `403 Forbidden`. The error message includes the name of the constraint that was violated.

The following example shows an error message for a request that violates the `gcp.restrictServiceUsage` constraint:
    
    
    {
      "error": {
        "code": 403,
        "message": "Request is disallowed by organization's constraints/gcp.restrictServiceUsage constraint for projects/PROJECT_ID attempting to use service geminidataanalytics.googleapis.com.",
        "status": "PERMISSION_DENIED",
        "details": [
          {
            "@type": "type.googleapis.com/google.rpc.ErrorInfo",
            "reason": "SECURITY_POLICY_VIOLATED",
            "domain": "googleapis.com",
            "metadata": {
              "service": "geminidataanalytics.googleapis.com",
              "consumer": "projects/PROJECT_ID"
            }
          }
        ]
      }
    }
    

The error message includes the technical name of the constraint, but it doesn't include the human-readable description of the constraint. To understand the requirements of a specific constraint, see the descriptions in Predefined constraints.

## What's next

  * Learn more about the [Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview).
  * Read about [IAM access control](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/access-control) for Conversational Analytics API.
  * Protect resources with [CMEK](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/cmek).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
