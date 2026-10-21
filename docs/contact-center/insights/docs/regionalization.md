---
url: https://docs.cloud.google.com/contact-center/insights/docs/regionalization/
title: Regionalization \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:37:26.450706+00:00
---

# Regionalization  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/insights/docs/regionalization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Regionalization Stay organized with collections  Save and categorize content based on your preferences. 

Specifying a region is particularly helpful in the following use cases:

  * Your system has regulatory or policy requirements that govern where your data must reside.
  * Your network latencies might be improved when the data is in the same region as your customers. For example, if Belgium customers use `europe-west1`, they can expect better latency.



## Available regions

Country grouping | Geographical location | Endpoint | Resource Location  
---|---|---|---  
Global | Global serving, data-at-rest in US | `contactcenterinsights.googleapis.com` | `us-central1`  
Americas | South Carolina | `us-east1-contactcenterinsights.googleapis.com` | `us-east1`  
Americas | Oregon | `us-west1-contactcenterinsights.googleapis.com` | `us-west1`  
Americas | Montréal | `northamerica-northeast1-contactcenterinsights.googleapis.com` | `northamerica-northeast1`  
Americas | USA (multi-region) | `us-contactcenterinsights.googleapis.com` | `us`  
Europe | Belgium | `europe-west1-contactcenterinsights.googleapis.com` | `europe-west1`  
Europe | London | `europe-west2-contactcenterinsights.googleapis.com` | `europe-west2`  
Europe | Frankfurt | `europe-west3-contactcenterinsights.googleapis.com` | `europe-west3`  
Europe | Multi Region | `eu-contactcenterinsights.googleapis.com` | `eu`  
Europe | Netherlands | `europe-west4-contactcenterinsights.googleapis.com` | `europe-west4`  
Europe | Zurich | `europe-west6-contactcenterinsights.googleapis.com` | `europe-west6`  
Europe | EU (multi-region) | `eu-contactcenterinsights.googleapis.com` | `eu`  
Asia Pacific | Tokyo | `asia-northeast1-contactcenterinsights.googleapis.com` | `asia-northeast1`  
Asia Pacific | Seoul | `asia-northeast3-contactcenterinsights.googleapis.com` | `asia-northeast3`  
Asia Pacific | Mumbai | `asia-south1-contactcenterinsights.googleapis.com` | `asia-south1`  
Asia Pacific | Singapore | `asia-southeast1-contactcenterinsights.googleapis.com` | `asia-southeast1`  
Asia Pacific | Jakarta | `asia-southeast2-contactcenterinsights.googleapis.com` | `asia-southeast2`  
Asia Pacific | Sydney | `australia-southeast1-contactcenterinsights.googleapis.com` | `australia-southeast1`  
**Note:** Calls to the `global` region might have higher latency when called from outside of the US. Select a more specific region that is closer to your services and end-users, if possible. For more information, see the [Google Cloud regions](https://cloud.google.com/about/locations) and [Google Cloud geography and regions](https://docs.cloud.google.com/docs/geography-and-regions) documentation.**Note:** For historical reasons, Customer Experience Insights uses the resource location ID `us-central1` for the global endpoint, instead of `global` which is used by newer APIs.**Note:** You need to change both the host of the URL and the resource location to use the regional instance. Eg. `us-east1-contactcenterinsights.googleapis.com` and `projects/project-id/location/*us-east1*/conversation/conversation-id`.

## Sample Commands

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `contactcenterinsights.analyses.create`



### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID.
  * LOCATION_ID: regional location.
  * CONVERSATION_ID: the ID of the conversation you want to analyze. This value was returned in the `createConversation` response.



HTTP method and URL: 
    
    
    POST https://LOCATION_ID-contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/conversations/CONVERSATION_ID/analyses

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://LOCATION_ID-contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/conversations/CONVERSATION_ID/analyses"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://LOCATION_ID-contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/conversations/CONVERSATION_ID/analyses" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION_ID/operations/OPERATION_ID"
    }
    

## Python Client

While using the python client, both the host and the resource location needs to be updated to point to the regional instance.
    
    
    options = ClientOptions(api_endpoint="us-east1-contactcenterinsights.googleapis.com" )
    request = contact_center_insights_v1.ListConversationsRequest(
        parent=f"projects/{project_id}/locations/us-east1",
    )
    client = contact_center_insights_v1.ContactCenterInsightsClient(client_options=options)
    

## Cloud Logging

See the [Cloud Logging documentation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/logging/docs/regionalized-logs) to control the region where your logs are stored.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
