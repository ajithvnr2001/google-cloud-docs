---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mcafee-mvision-epo-v2/
title: Integrate McAfee MVISION ePO V2 with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T04:38:02.818876+00:00
---

# Integrate McAfee MVISION ePO V2 with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mcafee-mvision-epo-v2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate McAfee MVISION ePO V2 with Google SecOps

This document explains how to integrate McAfee MVISION ePO V2 with Google Security Operations (Google SecOps).

### Use cases

The McAfee MVISION ePO V2 integration supports the following common use cases:

  * **Endpoint data enrichment** : Enrich security alerts and cases with detailed information about devices and endpoints managed by McAfee MVISION ePO.

  * **Device and tag management** : List and manage devices and tags within the McAfee ePO environment.

  * **Active response on endpoints** : Trigger actions such as retrieving or updating endpoint details in response to security incidents.

  * **Event ingestion** : Collect and ingest event data from McAfee MVISION ePO into Google SecOps for centralized monitoring and analysis.




## Before you begin

Before you configure the McAfee MVISION ePO V2 integration in Google SecOps, make sure you have the following:

  * **McAfee MVISION ePO administrator account** : An administrator account with permissions in your McAfee MVISION ePO environment to manage API clients, generate API keys, and access relevant data (devices, events, tags, endpoints).

  * **API client credentials** : A `Client ID` and `Client Secret` generated from your McAfee MVISION ePO console.

  * **API key** : A unique API key generated from your McAfee MVISION ePO console.

  * **OAuth Scopes** : The required OAuth scopes configured for your API client to grant appropriate access to McAfee MVISION ePO V2 APIs.




### Create API client credentials and API key

To obtain the required credentials (Client ID, Client Secret, API key, and configure required scopes) from your McAfee MVISION ePO platform, complete these steps:

  1. Sign in to your McAfee MVISION ePO console as an administrator.

  2. Navigate to the section for **API Client Management** or **API Key Generation**. (The exact path may vary depending on your McAfee MVISION ePO version and configuration. Common paths include **Configuration** , **Integrations** , or **API Access**).

  3. Follow the instructions in the McAfee MVISION ePO console to **create a new API client**. During this process, you typically:

     * Generate a `Client ID` and `Client Secret`.

Copy and store these values securely. They are usually displayed only once.

     * Generate an API key. 

     * Configure API scopes for the API client. 

**Note:** Ensure you select scopes that grant the necessary permissions for the integration intended use cases (such as, for device read/write, event reading, tag management). 

Based on typical ePO integration needs, common scopes might include: `epo.device.r`, `epo.device.w`, `epo.evt.r`, `epo.taggroups.r`, `epo.taggroups.w`.

  4. Record your API endpoints:

     * **API Root** : typically `https://api.mvision.mcafee.com`

     * **IAM Root** : typically `https://iam.mcafee-cloud.com`




These are standard endpoints for the McAfee MVISION cloud platform.

## Integration parameters

The McAfee MVISION ePO V2 integration requires the following parameters:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
`API Root` | String | `https://api.mvision.mcafee.com` | Yes | Required. The base URL for the McAfee MVISION ePO API.  
`Client ID` | String | N/A | Yes | Required. The Client ID for the API client application created in your McAfee MVISION ePO console.  
`Client Secret` | Password | N/A | Yes | Required. The Client Secret associated with your API client application. This value is typically displayed only once when generated.  
`API Key` | Password | N/A | Yes | Required. The API key generated for your McAfee MVISION ePO integration. This value is typically displayed only once when generated.  
`Scopes` | String | `epo.device.r epo.device.w epo.evt.r epo.taggro...` | Yes | Required. A space-separated list of OAuth scopes granted to your API client, defining its permissions. Ensure the scopes match those configured in your McAfee MVISION ePO console (e.g., `epo.device.r epo.evt.r`).  
`IAM Root` | String | `https://iam.mcafee-cloud.com` | Yes | Required. The base URL for McAfee's Identity and Access Management service.  
`Verify SSL` | Boolean | Checked | No | Optional. If enabled, the integration verifies the SSL certificate when connecting to McAfee MVISION ePO. Selected by default.  
`Remote Agent` | Boolean | Unchecked | No | Optional. If enabled, the integration runs remotely. After enabling this parameter, select the appropriate remote user (agent). Disabled by default.  
`Proxy Server Address` | String | N/A | No | Optional. The address of the proxy server to use (for example, `http://proxy.company.com:8080`).  
`Proxy Username` | String | N/A | No | Optional. The username used to authenticate with the proxy server.  
`Proxy Password` | Password | N/A | No | Optional. The password used to authenticate with the proxy server.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

### How authentication works

The McAfee MVISION ePO V2 integration authenticates using two methods:

  1. **OAuth 2.0 Client Credentials**

     * The integration submits the `Client ID` and `Client Secret` to the `IAM Root` endpoint (McAfee's IdP).

     * In exchange, it receives an OAuth access token, scoped according to your `Scopes` setting.

  2. **API key**

     * For each request to the `API Root` endpoint, the integration includes the following:

       * The OAuth access token (in the `Authorization` header).

       * The `API Key` (often as a custom header or query parameter). 

     * This dual-header approach makes sure that every call is authenticated (by the token) and authorized (by the API key).




## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Add Tag To Device

Use the **Add Tag To Device** action to assign one or more tags to a specified device in McAfee MVISION ePO.

This action runs on the following Google SecOps entities:

  * `ADDRESS`
  * `HOSTNAME`



#### Action inputs

The **Add Tag To Device** action requires the following parameters:

Parameter | Description  
---|---  
`Tag Name` | Required. The name of the tag to assign to the device.  
  
### Enrich Endpoint

Use the **Enrich Endpoint** action to retrieve and update detailed information for a specific endpoint from McAfee MVISION ePO.

This action runs on the following Google SecOps entities:

  * `ADDRESS`
  * `HOSTNAME`



#### Action inputs

None.

### List Devices

Use the **List Devices** action to retrieve a comprehensive list of devices managed by McAfee MVISION ePO, based on specified criteria.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **List Devices** action requires the following parameters:

Parameter | Description  
---|---  
`Max Devices to Return` | Optional. The amount of devices to return. The default value is `100`.  
  
### List Tags

Use the **List Tags** action to retrieve a list of all available tags defined within McAfee MVISION ePO.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **List Tags** action requires the following parameters:

Parameter | Description  
---|---  
`Max Tags to Return` | Optional. The amount of tags to return. The default value is `100`.  
  
### Ping

Use the **Ping** action to test connectivity to the McAfee MVISION ePO V2 service using the configured integration parameters.

This action doesn't run on Google SecOps entities.

#### Action inputs

None.

### Remove Tag From Device

Use the **Remove Tag From Device** action to disassociate one or more tags from a specified device in McAfee MVISION ePO.

This action runs on the following Google SecOps entities:

  * `ADDRESS`
  * `HOSTNAME`



#### Action inputs

The **Remove Tag From Device** action requires the following parameters:

Parameter | Description  
---|---  
`Tag Name` | Required. The name of the tag to remove from the device.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
