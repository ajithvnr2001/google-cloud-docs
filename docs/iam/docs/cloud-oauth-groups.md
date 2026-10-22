---
url: https://docs.cloud.google.com/iam/docs/cloud-oauth-groups/
title: Retrieve enterprise groups with the Cloud OAuth API \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:31:00.345161+00:00
---

# Retrieve enterprise groups with the Cloud OAuth API  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/cloud-oauth-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Identity and Access Management (IAM) ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Retrieve enterprise groups with the Cloud OAuth API Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This guide describes how to retrieve enterprise group memberships for authenticated workforce users by using the `/groups` endpoint in the Cloud OAuth API (`cloudoauth.googleapis.com`).

The `/groups` endpoint serves as a distributed claims endpoint for OpenID Connect (OIDC) integrations, returning paginated enterprise group memberships for users in SCIM-enabled and non-SCIM workforce identity pools.

**Important:** The `/groups` endpoint is available only for Looker. 

## Before you begin

  1. Configure a workforce identity pool and provider. For more information, see [Configure Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/configuring-workforce-identity-federation).
  2. Register an OAuth client and exchange an authorization code for an access token. For more information, see [Exchange tokens with the Cloud OAuth API](https://docs.cloud.google.com/iam/docs/cloud-oauth-exchange-tokens).
  3. Enable the Cloud OAuth API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudoauth.googleapis.com&redirect=https%3A//console.cloud.google.com)




## Retrieve enterprise groups

To retrieve group memberships for the authenticated user, send an HTTP `GET` request to the `/groups` endpoint:

The Cloud OAuth API's `[common.groups](https://docs.cloud.google.com/iam/docs/reference/cloudoauth/rest)` method retrieves enterprise group memberships for the authenticated user. 

Before using any of the request data, make the following replacements: 

  * `TOKEN`: the short-lived OAuth 2.0 access token obtained from the token exchange endpoint.
  * `PAGE_SIZE`: Optional. The maximum number of groups to return per page (between 2500 and 5000).
  * `PAGE_TOKEN`: Optional. A pagination token received from a previous `/groups` response in the `next_page_token` field.



HTTP method and URL: 
    
    
    GET https://cloudoauth.googleapis.com/v1/common/groups?page_size=PAGE_SIZE&page_token=PAGE_TOKEN

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer TOKEN" \  
         "https://cloudoauth.googleapis.com/v1/common/groups?page_size=PAGE_SIZE&page_token=PAGE_TOKEN"

#### PowerShell (Windows)

Execute the following command: 
    
    
    $headers = @{ "Authorization" = "Bearer TOKEN" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://cloudoauth.googleapis.com/v1/common/groups?page_size=PAGE_SIZE&page_token=PAGE_TOKEN" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "groups": [
        "security-admin@example.com",
        "data-analysts@example.com",
        "looker-developers@example.com"
      ],
      "next_page_token": "AE12aBcDeFgHiJkLmNoPqRsTuVwXyZ"
    }
    

### Response fields

The response contains the following fields:

Field | Type | Description  
---|---|---  
`groups` | `array of strings` | The list of enterprise group identifiers or email addresses that the authenticated user belongs to.  
`next_page_token` | `string` | A token that you can pass as `page_token` in subsequent requests to retrieve the next page of results. If this field is empty or omitted, there are no subsequent pages.  
  
For information about error responses returned by the `/groups` endpoint, see [Cloud OAuth user info and groups errors](https://docs.cloud.google.com/iam/docs/troubleshooting-workforce-identity-federation#cloud-oauth-userinfo-groups-errors).

## What's next

  * [Retrieve user info with the Cloud OAuth API](https://docs.cloud.google.com/iam/docs/cloud-oauth-userinfo)
  * [Exchange tokens with the Cloud OAuth API](https://docs.cloud.google.com/iam/docs/cloud-oauth-exchange-tokens)
  * [Cloud OAuth API overview](https://docs.cloud.google.com/iam/docs/cloud-oauth-api-overview)
  * [Manage OAuth applications for Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-manage-oauth-app)
  * [Cloud OAuth REST API reference](https://docs.cloud.google.com/iam/docs/reference/cloudoauth/rest)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
