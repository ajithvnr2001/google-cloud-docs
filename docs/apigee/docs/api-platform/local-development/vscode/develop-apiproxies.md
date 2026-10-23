---
url: https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/develop-apiproxies/
title: Develop API proxies \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:14:17.544167+00:00
---

# Develop API proxies  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/develop-apiproxies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Develop API proxies Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Expose APIs on Apigee by implementing API proxies. API proxies decouple the app-facing API from your backend services, shielding those apps from backend code changes.

Develop your API proxies using Apigee in Cloud Code as described in the following sections. See also [Manage folders and files in an Apigee workspace](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-apigee-workspace#manage-folders-files).

**Before you begin** : Familiarize yourself with the concepts described in the following topics: 

  * [Understanding APIs and API proxies](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/understanding-apis-and-api-proxies)
  * [Key points of API proxy development](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/structure-api-proxies)



## Create an API proxy

To create an API proxy using Apigee in Cloud Code, make sure you've created a [local development workspace](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-apigee-workspace) and then:

  1. Perform one of the following actions:

     * In your workspace, position your cursor over the **apiproxies** folder and click ![Create API proxy icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-create.png).

![+ displays when you position the cursor over apiproxies folder](https://docs.cloud.google.com/static/apigee/docs/api-platform/local-development/vscode/images/vscode-create-proxy.png)

     * Select **View > Command Palette** to open the Command palette and select **Cloud Code: Create Apigee proxy bundle**.

The **Create proxy** wizard opens.

  2. Select one of the following options:

Type | Description  
---|---  
`Access token-based authentication` |  Adds OAuth 2.0 based authentication to your API proxy. Apigee automatically adds the following policies to your API proxy:
     * Quota to manage quota on the proxy.
     * AssignMessage to strip the API key, supplied in the API call as a query parameter, from the request forwarded to the backend server.
     * OAuthV2 as the authentication method.  
`API key-based authentication` |  An API proxy that uses simple API key verification. Apigee automatically adds the following policies to your API proxy:
     * Quota to manage quota on the proxy.
     * VerifyAPIKey to validate API keys presented by requesting apps.
     * AssignMessage to strip the API key, supplied in the API call as a query parameter, from the request forwarded to the backend server.  
`Echo request` |  An API proxy that echos requests. There is no target/API backend for this proxy type and no authentication. You are not prompted to specify a URL for the backend service (`Target (Existing API)`) and the default target endpoint configuration is not included.   
`Simple reverse proxy` |  An API proxy that passes through requests to a backend target. It does not include authentication, so requests are passed to the backend without any security checks.  
`OpenAPI 3.0 spec` |  Create a proxy by loading an existing OpenAPI 3.0 spec. For more information, see [OpenAPI Initiative](https://openapis.org).  
  3. See [API proxy primary fields](https://docs.cloud.google.com/apigee/docs/api-platform/develop/ui-create-proxy#api-proxy-primary-fields) for information on the fields, such as the base path, needed to create each proxy type. Respond to each of the prompts and press **`Enter`** to confirm and proceed, or **`Esc`** to cancel the wizard.




After you complete the steps in the wizard, the new `apiproxy-name` folder is added under `apiproxies` in the Apigee section. Each API proxy folder is structured as described in [API proxy configuration directory structure](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference#apiproxystructure).

The following provides an example of the default configuration created for a API proxy created with type `API key-based authentication`.

![The folder structure of an API key-based authentication proxy](https://docs.cloud.google.com/static/apigee/docs/api-platform/local-development/vscode/images/vscode-reverseproxy-structure.png)

For a description of the default configuration, see Exploring the default API proxy configuration.

### Explore the default API proxy configuration

The following table summarizes the contents included in the default configuration when you create an API proxy based on the API proxy type and authentication options selected.

Configuration file | Simple reverse proxy | Echo request | Access token (OAuthV2) authentication | API key authentication  
---|---|---|---|---  
`proxies/default.xml`  
[Default proxy endpoint configuration](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference#proxyendpoint). | check_circle | check_circle | check_circle | check_circle  
`targets/default.xml`  
[Default target endpoint configuration](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference#targetendpoint). | check_circle |  | check_circle | check_circle  
`impose-quota.xml`  
[Quota policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/quota-policy) to define a default quota. |  |  | check_circle | check_circle  
`remove-header-authorization.xml`  
[AssignMessage policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy) to remove the `Authorization` header that is passed for authentication. |  |  | check_circle |   
`remove-query-param-apikey.xml`  
[AssignMessage policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy) to remove the `apikey` query parameter that is passed for authentication. |  |  |  | check_circle  
`verify-api-key.xml`  
[VerifyAPIKey policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/verify-api-key-policy) to enforce the verification of API keys. |  |  |  | check_circle  
`verify-oauth-v2-access-token.xml`  
[OAuthV2](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy) policy to validate OAuth V2 access tokens. |  |  | check_circle |   
  
## Upload an API proxy bundle

To upload an API proxy bundle to Apigee in Cloud Code:

  1. Perform one of the following actions:

     * In your Apigee workspace, position your cursor over the **apiproxies** folder and click ![Import API proxy bundle icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-upload.png).

     * Select **View > Command Palette** to open the Command palette and select **Cloud Code: Import Apigee proxy bundle**.

  2. Navigate to the API proxy bundle that you want to upload and click **Select**. The API proxy bundle must be structured as described in [API proxy configuration directory structure](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference#apiproxystructure).

  3. (Optional) By default, the name of the zip file minus its extension is used for the name of the API proxy. If this name is not unique, you are prompted to enter a unique name.




The uploaded `apiproxy-name` folder is added under `apiproxies` in your workspace.

## Manage proxy endpoints

As described in [What is an API proxy?](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/understanding-apis-and-api-proxies#whatisanapiproxy), a **proxy endpoint (ProxyEndpoint)** defines the way client apps consume your APIs. You configure the proxy endpoint to define the URL of your API proxy. The proxy endpoint also determines whether apps access the API proxy over HTTP or HTTPS. You can [attach policies](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-policies) to the proxy endpoint to enforce security, quota checks, and other types of access control and rate-limiting.

Create and configure proxy endpoints as described in the following sections.

### Create proxy endpoints

When you create an API proxy, a default proxy endpoint is added to the API proxy configuration. For more information, see Exploring the default API proxy configuration. You can create additional proxy endpoints, as required.

**Note** : Before adding multiple proxy endpoints, review the following topic [Antipattern: Define multiple ProxyEndpoints in an API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/multiple-proxyendpoints). 

To create a proxy endpoint using Apigee in Cloud Code:

  1. In your Apigee workspace, perform one of the following actions:

     * Position your cursor over one of the following folders, click ![Create proxy endpoint icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-create.png), and select **Create proxy endpoint** : 
       * `apiproxy-name` proxy bundle
       * `apiproxy-name/apiproxy`
     * Position your cursor over the **`apiproxy-name /apiproxy/proxies`** folder and click ![Create proxy endpoint icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-create.png).

The **Create proxy endpoint** wizard opens.

  2. Enter the values for the next set of prompts. Press **`Enter`** after each to confirm and proceed or **`Esc`** to cancel.

Field | Description  
---|---  
`Proxy endpoint name` | Name used to identify the proxy endpoint.  
`API proxy base path` | Part of the URL used to make requests to your API. Apigee uses the URL to match and route incoming requests to the proper API proxy.  
`Target endpoint` | Select either `no target` or `default`. See [ProxyEndpoint configuration elements](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference#proxyendpoint-proxyendpointconfigurationelements) for information.  



The endpoint is created and added to the **`apiproxy-name /apiproxy/proxies`** folder in the Apigee section and opened in the editor. Configure the proxy endpoint, as described in the following section.

### Configure proxy endpoints

To configure proxy endpoints, refer to the following sections:

  * [Controlling how a proxy executes with flows](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-are-flows)
  * [Determining the URL of the API proxy endpoint](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/understanding-routes#determiningtheurloftheapiproxyendpoint)
  * [Adding features using policies](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-policies)
  * [Managing resources](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-resources)
  * [ProxyEndpoint configuration](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference#proxyendpoint-apiproxyproxiesdefaultxml)
  * [Flow configuration reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference)
  * [Endpoint properties reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/endpoint-properties-reference)



## Manage target endpoints

As described in [What is an API proxy?](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/understanding-apis-and-api-proxies#whatisanapiproxy), a **target endpoint (TargetEndpoint)** defines the way the API proxy interacts with your backend services. You configure the target endpoint to forward requests to the proper backend service, and define any security settings, HTTP or HTTPS protocol, and other connection information. You can [attach policies](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-policies) to the target endpoint to ensure that response messages are properly formatted for the app that made the initial request.

Create and configure target endpoints as described in this section.

### Create target endpoints

When you create a reverse API proxy, a default target endpoint is added to the API proxy configuration. When creating an API proxy with no backend target, only the default proxy endpoint is added to the API proxy configuration, no target endpoint is added. For more information, see Exploring the default API proxy configuration.

Create target endpoints, as required.

**Note** : An API proxy does not need a target endpoint. Proxy endpoints can be configured to call URLs directly. An API proxy with no target endpoints usually contains a proxy endpoint that either directly calls a backend service or is configured to call a service using Java or JavaScript. 

To create a target endpoint using Apigee in Cloud Code:

  1. In your Apigee workspace, perform one of the following actions:

     * Position your cursor over one of the following folders, click ![Create target endpoint icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-create.png), and select **Create target endpoint** : 
       * `apiproxy-name` proxy bundle
       * `apiproxy-name/apiproxy`
     * Position your cursor over the **`apiproxy-name /apiproxy/targets`** folder and click ![Create target endpoint icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-create.png).

The **Create target endpoint** wizard opens.

  2. Perform the following steps based on the type of target endpoint you want to create:

Type | Steps  
---|---  
External HTTP(s) target | To define an external HTTP(s) target:
     1. Select **HTTP(s) target**.
     2. Enter the name of the target endpoint in **Target endpoint name**.
     3. Enter the URL of the backend service that this target endpoint invokes in **Backend target URL**.
For more information, see [Determining the URL of the target endpoint](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/understanding-routes#determiningtheurlofthetargetendpoint).  
Proxy chaining | To define a locally deployed API proxy as your target:
     1. Select **Proxy chaining**.
     2. Enter the name of the target endpoint in **Target endpoint name**.
     3. Select an API proxy.
     4. Select the proxy endpoint.
For more information, see [Chaining proxies together](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/connecting-proxies-other-proxies).   
Load balanced target | To define a load balanced target using [target servers defined in the environment](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/deploy-environment#target-servers):
     1. Select **Load balanced target**.
     2. Enter the name of the target endpoint in **Target endpoint name**.
For more information, see [Configuring a TargetEndpoint to load balance across named TargetServers](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/load-balancing-across-backend-servers#configuringatargetendpointtoloadbalanceacrossnamedtargetservers).  



The target endpoint is created and added to the **`apiproxy-name /apiproxy/targets`** folder and opened in the editor. Configure the target endpoint, as described in the following section.

### Configuring target endpoints

Configure target endpoints, as described in the following topics. 

  * [Load balancing across backend servers](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/load-balancing-across-backend-servers)
  * [Controlling how a proxy executes with flows](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-are-flows)
  * [Chaining API proxies together](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/connecting-proxies-other-proxies)
  * [Determining the URL of the target endpoint](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/understanding-routes#determiningtheurlofthetargetendpoint)
  * [Adding features using policies](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-policies)
  * [Managing resources](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-resources)
  * [TargetEndpoint configuration](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference#targetendpoint-targetendpointconfiguration)
  * [Flow configuration reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference)
  * [Endpoint properties reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/endpoint-properties-reference)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
