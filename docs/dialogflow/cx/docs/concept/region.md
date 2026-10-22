---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/region/
title: Regionalization and location settings \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:43:36.949170+00:00
---

# Regionalization and location settings  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/region/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Regionalization and location settings Stay organized with collections  Save and categorize content based on your preferences. 

When you create an agent, you must specify a region as the agent's location. Requests sent to your agent are handled by Google services in this region and Dialogflow CX keeps [data-at-rest](https://en.wikipedia.org/wiki/Data_at_rest) physically within the geographical [region or location](https://cloud.google.com/about/locations). For the best performance, you should choose a region that is near your services and end-users.

Once an agent is created, its location cannot change. In order to change an agent's location, you must [export and restore](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#export) to a new agent with a different location.

Each location has associated settings that apply across your project. In most cases, you do not need to edit these location settings, and the default settings will work well. If your system requires [customer-managed encryption keys](https://docs.cloud.google.com/dialogflow/cx/docs/concept/cmek) (often required by government entities or regulated industries), read more about [location settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/region#location-settings).

## Limitations

The following limitations apply:

  * Region support for different telephony integrations may vary. Check documentation for each integration.

  * System entity support differs for each [language](https://docs.cloud.google.com/dialogflow/cx/docs/reference/language). See the [system entity limitations](https://docs.cloud.google.com/dialogflow/cx/docs/reference/system-entities#limits) for details.

  * The [APIs Explorer](https://developers.google.com/explorer-help/), found on many [REST reference documents](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest), only supports the `global` region for API calls. 




## Available regions

**Important:** The "[AI/ML Data Location](https://cloud.google.com/terms/data-residency)" (Data Residency for ML Processing) commitment is only supported in the locations within the US and EU. ML Processing for generative models may occur within any location in the multi-regions when requests are made to regional APIs included within a multi-region. For more details, see the [Vertex AI documentation](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/locations).

Dialogflow CX supports the following regions for agent location. [Data store agents](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store-agent) are also supported in the regions listed in the following table, but the region IDs used by data stores differ slightly from the agent regions (as listed). All regions with a value entered in the **Data store region ID** column are supported by data store agents in [Vertex AI Agents](https://docs.cloud.google.com/generative-ai-app-builder/docs/agent-intro).

Country grouping | Geographical location | Agent region ID | Data store region ID  
---|---|---|---  
Americas | Iowa | `us-central1` | `us` (multi-region)  
Americas | Montréal | `northamerica-northeast1` | `global` (multi-region)  
Americas | South Carolina | `us-east1` | `us` (multi-region)  
Americas | Oregon | `us-west1` | `us` (multi-region)  
Americas | United States multi-region | `us` * | `us` (multi-region)  
Europe | Belgium | `europe-west1` | `eu` (multi-region)  
Europe | London | `europe-west2` | `eu` (multi-region)  
Europe | Frankfurt | `europe-west3` | `eu` (multi-region)  
Europe | Netherlands | `europe-west4` | `eu` (multi-region)  
Europe | Zurich | `europe-west6` | `eu` (multi-region)  
Asia Pacific | Sydney | `australia-southeast1` | `global` (multi-region)  
Asia Pacific | Tokyo | `asia-northeast1` | `global` (multi-region)  
Asia Pacific | Mumbai | `asia-south1` | `global` (multi-region)  
Asia Pacific | Singapore | `asia-southeast1` | `global` (multi-region)  
Asia Pacific | Jakarta | `asia-southeast2` | `global` (multi-region)  
Global | Global multi-region (global serving, [data-at-rest](https://en.wikipedia.org/wiki/Data_at_rest) in United States) | `global` (preferred) or no region (default) ¶ | `global` (multi-region) ¶  
Symbol | Description  
---|---  
* | For Gemini 2.x models, Vertex AI doesn't support the `us` or `eu` multi-region locations. As a result, using Dialogflow CX's generative AI features in the `us` or `eu` multi-regions relies on the respective existing US or EU single-region endpoints. For Gemini 3 and later models (such as `gemini-3.1-flash-lite`), the `us` and `eu` multi-region locations are supported and used for US and European regions. For more information, see [Generative quotas](https://docs.cloud.google.com/dialogflow/quotas#generative).  
¶ | Calls to the `global` region may have higher latency when called from outside of the US. Prefer a more specific region that is closer to your services and end-users, if possible.  
  
You can read more about regions used by Google Cloud at [Google Cloud regions](https://cloud.google.com/about/locations) and [Google Cloud geography and regions](https://docs.cloud.google.com/docs/geography-and-regions).

## Location settings

If your system requires [customer-managed encryption keys](https://docs.cloud.google.com/dialogflow/cx/docs/concept/cmek) (often required by government entities or regulated industries), you can use location settings to configure this feature.

Location settings are shared across the project, and each unique location has its own location settings.

Once settings for a specific location are configured for a project, an immutable `dialogflow.googleapis.com/LocationSettings` [resource](https://docs.cloud.google.com/asset-inventory/docs/asset-names) is created, and the settings cannot change for that location. If you need to change these settings or to delete the resource, you must create a new project.

If you need to allow your organization's developers to configure agents only in specific locations, you can [set up an organization policy that includes a resource locations constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services#dialogflow).

If you create an agent without editing the location settings, the default settings will be configured for that location, and they cannot be changed for the project. In addition, once an agent is created, its location cannot change. In order to change an agent's location, you must [export and restore](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#export) to a new agent with a different location.

The following location settings are available:

  * **Encryption** : This setting controls whether Google-managed or customer-managed encryption keys are used to protect data. The default is Google-managed. You must request access (by contacting your Google representative) to the [customer-managed encryption keys](https://docs.cloud.google.com/dialogflow/cx/docs/concept/cmek) feature to change this setting.



You can configure location settings in two ways:

  * Click **Location settings** from the [agent selector interface](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console#agent).
  * Click the **Edit** button next to the **Location** drop down when [creating an agent](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#create).

**Note:** Currently, you cannot update location settings with the API.

## Specify a region with the API

You must specify a region for all API requests.

For REST calls, you must do both of the following:

  * Provide the region ID for the `location` URL path parameter.

  * For the `global` region, use `dialogflow.googleapis.com` for the hostname. For all other regions, use `[region-id]-dialogflow.googleapis.com` for the hostname.




For example:

  * `dialogflow.googleapis.com/projects/{PROJECT_ID}/locations/global/agents/{AGENT_ID}`

  * `us-central1-dialogflow.googleapis.com/projects/{PROJECT_ID}/locations/us-central1/agents/{AGENT_ID}`




For client libraries, see the [client library documentation](https://docs.cloud.google.com/dialogflow/cx/docs/reference/library/overview) for a region configuration option.

You can find examples in the [API quickstart](https://docs.cloud.google.com/dialogflow/cx/docs/quick/api).

**Caution:** As described in the [setup documentation](https://docs.cloud.google.com/dialogflow/cx/docs/quick/setup#auth-env), you should use the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to provide your client libraries with credentials. However, if you need to manually provide a credentials file in your code, you need to take one additional step when calling a regionalized endpoint. Set the scope to `https://www.googleapis.com/auth/cloud-platform` when generating your authentication credentials. For example, this is accomplished in Java when creating a `GoogleCredentials` object: 
    
    
    GoogleCredentials.fromStream(new FileInputStream("credential_file"))
      .createScoped("https://www.googleapis.com/auth/cloud-platform")
      

## Cloud logging

See the [Cloud logging guide](https://docs.cloud.google.com/dialogflow/cx/docs/concept/logging) to control the region in which logs are stored.

[ Previous arrow_back  Mutual TLS authentication  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/mtls)

[ Next Custom CA certificates  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/custom-ca)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
