---
url: https://docs.cloud.google.com/iam/docs/cloud-oauth-userinfo/
title: Retrieve user info with the Cloud OAuth API \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:53.581556+00:00
---

# Retrieve user info with the Cloud OAuth API  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/cloud-oauth-userinfo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Identity and Access Management (IAM) ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Retrieve user info with the Cloud OAuth API Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This guide describes how to retrieve OpenID Connect (OIDC) standard claims, custom directory claims, and group memberships for authenticated workforce users by using the `/userinfo` endpoint in the Cloud OAuth API (`cloudoauth.googleapis.com`).

**Important:** The `/userinfo` endpoint is available only for Looker. 

## Before you begin

  1. Configure a workforce identity pool and provider. For more information, see [Configure Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/configuring-workforce-identity-federation).
  2. Register an OAuth client and exchange an authorization code for an access token. For more information, see [Exchange tokens with the Cloud OAuth API](https://docs.cloud.google.com/iam/docs/cloud-oauth-exchange-tokens).
  3. Ensure your access token includes the `openid` scope.
  4. Enable the Cloud OAuth API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudoauth.googleapis.com&redirect=https%3A//console.cloud.google.com)




## Organization-scoped endpoint

The Cloud OAuth API provides the organization-scoped (single-tenant) endpoint that you can use when your client application and resources are restricted to a specific Google Cloud organization:

The Cloud OAuth API's `[organizations.userinfo](https://docs.cloud.google.com/iam/docs/reference/cloudoauth/rest)` method retrieves OpenID Connect (OIDC) standard claims, custom claims, and group memberships for the authenticated user in a specific organization. 

Before using any of the request data, make the following replacements: 

  * `TOKEN`: the short-lived OAuth 2.0 access token obtained from the token exchange endpoint.
  * `ORGANIZATION_ID`: your numeric Google Cloud organization ID.



HTTP method and URL: 
    
    
    GET https://cloudoauth.googleapis.com/v1/organizations/ORGANIZATION_ID/userinfo

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer TOKEN" \  
         "https://cloudoauth.googleapis.com/v1/organizations/ORGANIZATION_ID/userinfo"

#### PowerShell (Windows)

Execute the following command: 
    
    
    $headers = @{ "Authorization" = "Bearer TOKEN" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://cloudoauth.googleapis.com/v1/organizations/ORGANIZATION_ID/userinfo" | Select-Object -Expand Content

For workforce identity pools without SCIM provisioning enabled, the endpoint returns profile attributes, custom claims, and group memberships inline:
    
    
    {
      "sub": "principal://iam.googleapis.com/locations/global/workforcePools/my-pool/subject/user@example.com",
      "email": "user@example.com",
      "custom_claim1": "engineering",
      "custom_claim2": "us-west",
      "groups": [
        "looker-developers",
        "analytics-viewers"
      ]
    }
    

## User claims and SCIM distributed groups

When a request succeeds, the `/userinfo` endpoint returns an HTTP `200 OK` status and a JSON object containing claims for the authenticated user.

The claims format depends on whether your workforce identity pool provider uses SCIM provisioning:

### Inline claims (non-SCIM identity pools)

For workforce identity pools without SCIM provisioning enabled, the endpoint returns profile attributes, custom claims, and group memberships inline:
    
    
    {
      "sub": "principal://iam.googleapis.com/locations/global/workforcePools/my-pool/subject/user@example.com",
      "email": "user@example.com",
      "custom_claim1": "engineering",
      "custom_claim2": "us-west",
      "groups": [
        "looker-developers",
        "analytics-viewers"
      ]
    }
    

### Distributed claims (SCIM-enabled identity pools)

For workforce identity pools with SCIM provisioning enabled, group memberships are returned as distributed claims. The response includes `_claim_names` and `_claim_sources` that reference the `/groups` endpoint:
    
    
    {
      "sub": "principal://iam.googleapis.com/locations/global/workforcePools/my-pool/subject/user@example.com",
      "name": "Jane Doe",
      "email": "user@example.com",
      "_claim_names": {
        "groups": "src1"
      },
      "_claim_sources": {
        "src1": {
          "endpoint": "https://cloudoauth.googleapis.com/v1/common/groups"
        }
      }
    }
    

### Claim fields

The response contains the following standard and distributed claim fields:

Field | Type | Description  
---|---|---  
`sub` | `string` | The unique principal identifier for the authenticated user in the workforce identity pool.  
`name` | `string` | The full name of the user, if available from the identity provider.  
`email` | `string` | The email address of the authenticated user.  
`groups` | `array of strings` | (Non-SCIM only) The list of enterprise group memberships for the user.  
`_claim_names` | `object` | (SCIM-enabled only) A JSON object that maps distributed claim names (such as `groups`) to source identifiers in `_claim_sources`.  
`_claim_sources` | `object` | (SCIM-enabled only) A JSON object that defines the source endpoint for each distributed claim identifier.  
  
For information about error responses returned by the `/userinfo` endpoint, see [Cloud OAuth user info and groups errors](https://docs.cloud.google.com/iam/docs/troubleshooting-workforce-identity-federation#cloud-oauth-userinfo-groups-errors).

## What's next

  * [Retrieve enterprise groups with the Cloud OAuth API](https://docs.cloud.google.com/iam/docs/cloud-oauth-groups)
  * [Exchange tokens with the Cloud OAuth API](https://docs.cloud.google.com/iam/docs/cloud-oauth-exchange-tokens)
  * [Cloud OAuth API overview](https://docs.cloud.google.com/iam/docs/cloud-oauth-api-overview)
  * [Manage OAuth applications for Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-manage-oauth-app)
  * [Cloud OAuth REST API reference](https://docs.cloud.google.com/iam/docs/reference/cloudoauth/rest)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
