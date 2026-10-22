---
url: https://docs.cloud.google.com/dialogflow/es/docs/how/region/
title: Regionalization and data residency \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:45:03.077227+00:00
---

# Regionalization and data residency  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/how/region/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Regionalization and data residency Stay organized with collections  Save and categorize content based on your preferences. 

Dialogflow provides [data residency](https://cloud.google.com/blog/products/identity-security/meet-data-residency-requirements-with-google-cloud) to keep your data-at-rest physically within a geographical [region or location](https://cloud.google.com/about/locations). When a region is specified, your data-at-rest is not replicated outside the region. Pricing is the same for all regions.

Regions are used for the following reasons:

  * Your system may have regulatory or policy requirements that govern where your data must reside.
  * Your network latencies may be improved when the data is in the same region as your customers. For example, If UK customers use `europe-west2`, they can expect better latency.

**Note:** Dialogflow regionalization and data residency does not apply to [data-in-use](https://en.wikipedia.org/wiki/Data_in_use) or [data-in-transit](https://en.wikipedia.org/wiki/Data_in_transit).

## Data-at-rest

All Dialogflow developer user and end-user data is included in [data-at-rest](https://en.wikipedia.org/wiki/Data_at_rest). For example:

  * All agent resources set with console or API (intents, entities, etc.)
  * All agent settings set with console or API
  * Query history
  * Validation results
  * Model creation tasks
  * Training tasks
  * Long-running operation tasks



## Available regions

Dialogflow provides the following regions:

Country grouping | Geographical location | Region ID  
---|---|---  
Europe | Belgium | `europe-west1`  
Europe | London | `europe-west2`  
Asia Pacific | Sydney | `australia-southeast1`  
Asia Pacific | Tokyo | `asia-northeast1`  
Global | Dialogflow serving is global, data-at-rest is within US | `global` (preferred) or no region (default) *  
Symbol | Description  
---|---  
* | Calls to the `global` region may have higher latency when called from outside of the US. Prefer a more specific region that is closer to your services and end-users, if possible.  
  
## Select a region with the console

The top left area of the [Dialogflow ES console](https://dialogflow.cloud.google.com) has a drop-down for region selection. Every agent has an immutable region that is specified upon creation. When you select a region from the console, you can only list or create agents for the selected region. The default region is `global`.

**Note:** You can create one agent per region for a Google Cloud project.

## Select a region with the API

If your agent was created in a non-default region, you must specify that region when calling the API for either design-time or runtime requests.

To provide a region, you supply a `location` parameter to API requests. For REST calls, do both of the following:

  * Provide the `location` URL path parameter. For the `global` region, use `global`.
  * For the `global` region, use `dialogflow.googleapis.com` for the hostname. For all other regions, use `[REGION_ID]-dialogflow.googleapis.com` for the hostname.



Examples:

  * `https://dialogflow.googleapis.com/v2/projects/PROJECT/locations/global/agents/`
  * `https://asia-northeast1-dialogflow.googleapis.com/v2/projects/PROJECT/locations/asia-northeast1/agents/`



For client libraries, see the [client library documentation](https://docs.cloud.google.com/dialogflow/docs/reference/libraries/overview). You need to do the following:

  * Set the Dialogflow service endpoint to one of the following:
        
        dialogflow.googleapis.com:443
        REGION_ID-dialogflow.googleapis.com:443
        

  * Set the session name to:
        
        projects/PROJECT_ID/locations/REGION_ID/agent/sessions/SESSION_ID
        


**Caution:** As described in the [setup documentation](https://docs.cloud.google.com/dialogflow/es/docs/quick/setup#auth-env), you should use the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to provide your client libraries with credentials. However, if you need to manually provide a credentials file in your code, you need to take one additional step when calling a regionalized endpoint. Set the scope to `https://www.googleapis.com/auth/cloud-platform` when generating your authentication credentials. For example, this is accomplished in Java when creating a `GoogleCredentials` object: 
    
    
    GoogleCredentials.fromStream(new FileInputStream("credential_file"))
      .createScoped("https://www.googleapis.com/auth/cloud-platform")
      

## Cloud logging

See the [Cloud logging guide](https://docs.cloud.google.com/dialogflow/es/docs/logging) to control the region in which logs are stored.

## Limitations

When a non-default region is selected in the Dialogflow Console, the following features are not available:

  * [Integrations](https://docs.cloud.google.com/dialogflow/es/docs/integrations)
  * [Knowledge Connectors](https://docs.cloud.google.com/dialogflow/es/docs/knowledge-connectors)
  * [Prebuilt Agents](https://docs.cloud.google.com/dialogflow/es/docs/agents-prebuilt)
  * [Small Talk](https://docs.cloud.google.com/dialogflow/es/docs/agents-small-talk)
  * [Training tool](https://docs.cloud.google.com/dialogflow/es/docs/training#tool)



The [APIs Explorer](https://developers.google.com/explorer-help/), found on many [REST reference documents](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest), only supports the `global` region for API calls.

[ Previous arrow_back  Long-running operations  ](https://docs.cloud.google.com/dialogflow/es/docs/how/long-running-operations)

[ Next Migrating  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/how/migrating)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
