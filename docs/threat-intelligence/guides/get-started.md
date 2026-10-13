---
url: https://docs.cloud.google.com/threat-intelligence/guides/get-started/
title: Get Started \u00a0|\u00a0 Google Threat Intelligence \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:31:41.873509+00:00
---

# Get Started  |  Google Threat Intelligence  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/threat-intelligence/guides/get-started/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Threat Intelligence ](https://docs.cloud.google.com/threat-intelligence)
  * [ Guides ](https://docs.cloud.google.com/threat-intelligence/guides/concepts)



Send feedback 

#  Get Started Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1), and the [Additional Terms for Generative AI Preview Products](https://cloud.google.com/trustedtester/aitos). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This guide provides a practical introduction to the Google Threat Intelligence API. You will learn how to authenticate and perform basic operations against Alerts, Findings, and Configurations using standard HTTP requests. For detailed API documentation, see the [REST API Reference](https://docs.cloud.google.com/threat-intelligence/reference/rest).

## Prerequisites

Before you begin, ensure you have the following:

  1. Your organization's Google Cloud Project ID, which is assigned by the Google Threat Intelligence team when your organization is onboarded. You can find this ID in the URL when accessing GTI Alerts (for example, in `https://proactive.virustotal.com/alerts?...&project=projects%2F**your-project-id**`, the Project ID is `your-project-id`), or contact your account team if you cannot find it. Enter your org's Project ID here: YOUR_ORG_PROJECT_ID
  2. A GTI API key, which you can find in the GTI UI under [Profile > API Key](https://www.virustotal.com/gui/my-apikey).



### Authentication

The API requires OAuth 2.0 authentication. You can exchange your GTI API key for an access token using the following endpoint:
    
    
    curl https://idp.prod.identity.proactive.virustotal.com/realms/master/exchange/api-key \
      -H "Content-Type: application/json" \
      -d '{"api_key": "YOUR_API_KEY"}'
        

The response will contain the access token and its expiration time (usually 4 hours).
    
    
    {
      "access_token": "ya29.d.s0Ad...",
      "issued_token_type": "urn:ietf:params:oauth:token-type:access_token",
      "token_type": "Bearer",
      "expires_in": 14398
    }
        

Copy the `access_token` from the response and enter it here: YOUR_ACCESS_TOKEN

## Working with Alerts

[Alerts](https://docs.cloud.google.com/threat-intelligence/guides/concepts#alerts) are the primary actionable units in the system. They represent consolidated groups of findings that require your attention.

### List Alerts

Retrieve all alerts for your project. Note by default, the alerts returned are unordered.
    
    
    curl -H "x-goog-user-project: YOUR_ORG_PROJECT_ID" \
         -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
         "https://threatintelligence.googleapis.com/v1beta/projects/YOUR_ORG_PROJECT_ID/alerts"
        

#### List Alerts with Filtering and OrderBy

Retrieve a filtered list of alerts for your project and order the results.

The following example only filters for the `data_leak` alert [detail type](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts#alertdetail) with a `HIGH` [severity](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts#dataleakalertdetail), and orders the results by create time with latest alerts first. For more filtering and ordering options with examples, see the [List Alerts API reference](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts/list).
    
    
    curl -G \
         -H "x-goog-user-project: YOUR_ORG_PROJECT_ID" \
         -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
         --data-urlencode 'filter=((detail.data_leak.severity="HIGH"))' \
         --data-urlencode 'orderBy=audit.create_time desc' \
         "https://threatintelligence.googleapis.com/v1beta/projects/YOUR_ORG_PROJECT_ID/alerts"
        

### Get an Alert

Retrieve full details for a specific alert using its resource ID. This includes the generated summary, severity scores, and status. You can get the resource ID from the `name` field in the response from the List Alerts call.
    
    
    # Replace ALERT_ID with the specific ID. 
    curl -H "x-goog-user-project: YOUR_ORG_PROJECT_ID" \
         -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
         "https://threatintelligence.googleapis.com/v1beta/projects/YOUR_ORG_PROJECT_ID/alerts/ALERT_ID"
        

## Working with Configurations

[Configurations](https://docs.cloud.google.com/threat-intelligence/guides/concepts#organization-profile) hold your Customer Profile and Threat Scenarios, which define what the system matches for.

### List Configurations

See all configurations associated with your project.
    
    
    curl -H "x-goog-user-project: YOUR_ORG_PROJECT_ID" \
         -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
         "https://threatintelligence.googleapis.com/v1beta/projects/YOUR_ORG_PROJECT_ID/configurations"
        

### Get a Configuration

View the details of a specific configuration, such as your defined profiles and threat scenarios.
    
    
    # Replace CONFIG_ID with the specific ID. You can get the ID from the name field in the response from the List Configurations call.
    curl -H "x-goog-user-project: YOUR_ORG_PROJECT_ID" \
         -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
         "https://threatintelligence.googleapis.com/v1beta/projects/YOUR_ORG_PROJECT_ID/configurations/CONFIG_ID"
        

### Upserting Configurations

#### Customer Profile

A `CustomerProfile` configuration is created by default when an organization is onboarded. Additional `CustomerProfile` configurations cannot be added, but the initial configuration can be updated. The example below shows how to add a new product, `YouTube`, to an existing `CustomerProfile` that currently only includes `Google Cloud`. You can replace each of the fields in the example below with your own values from the List Configurations call above.
    
    
    # Replace CONFIG_ID with the specific ID.
    curl -X POST -H "x-goog-user-project: YOUR_ORG_PROJECT_ID" \
         -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
         -H "Content-Type: application/json" \
         -d '{
           "name": "projects/YOUR_ORG_PROJECT_ID/configurations/CONFIG_ID",
           "provider": "GTI Alerts",
           "state": "ENABLED",
           "detail": {
             "customerProfile": {
               "org": "Google",
               "products": [
                 {
                   "product": "Cloud",
                   "brand": "Google Cloud"
                 },
                 {
                   "product": "Video Platform",
                   "brand": "YouTube"
                 }
               ]
             }
           }
         }' \
         "https://threatintelligence.googleapis.com/v1beta/projects/YOUR_ORG_PROJECT_ID/configurations:upsert"
        

#### Threat Scenario Configurations

The example below shows how to create a new [TechnologyWatchList](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#technologywatchlistconfig) threat scenario configuration.
    
    
    # Replace CONFIG_ID with the specific ID.
    curl -X POST -H "x-goog-user-project: YOUR_ORG_PROJECT_ID" \
         -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
         -H "Content-Type: application/json" \
         -d '{
           "name": "projects/YOUR_ORG_PROJECT_ID/configurations/CONFIG_ID",
           "provider": "GTI Alerts",
           "state": "ENABLED",
           "detail": {
             "technologyWatchlist": {
               "technologies": [
                 "Cloud"
               ],
               "alertThreshold": {
                "priorityMinimum": "P1",
                "cvssScoreMinimum": 7.0,
                "epssScoreMinimum": 0.8,
                "exploitationStates": [
                   "EXPLOITATION_STATE_CONFIRMED"
                 ],
                "riskRatingMinimum": "MEDIUM"
               }
             }
           }
         }' \
         "https://threatintelligence.googleapis.com/v1beta/projects/YOUR_ORG_PROJECT_ID/configurations:upsert"
        

## Working with Findings

[Findings](https://docs.cloud.google.com/threat-intelligence/guides/concepts#findings) are the raw pieces of evidence (e.g., a specific forum post or leaked credential) that are aggregated into Alerts.

### List Findings

Retrieve all findings for your project.
    
    
    curl -H "x-goog-user-project: YOUR_ORG_PROJECT_ID" \
         -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
         "https://threatintelligence.googleapis.com/v1beta/projects/YOUR_ORG_PROJECT_ID/findings"
        

### Get a Finding

Get the complete technical details of a specific finding. You can get the ID from the `name` field in the response from the List Findings call.
    
    
    # Replace FINDING_ID with the specific ID.
    curl -H "x-goog-user-project: YOUR_ORG_PROJECT_ID" \
         -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
         "https://threatintelligence.googleapis.com/v1beta/projects/YOUR_ORG_PROJECT_ID/findings/FINDING_ID"
        

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
