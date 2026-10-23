---
url: https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/understanding-default-oauth-20-configuration/
title: OAuth 2.0: Configuring a new API proxy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:45.889672+00:00
---

# OAuth 2.0: Configuring a new API proxy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/understanding-default-oauth-20-configuration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  OAuth 2.0: Configuring a new API proxy Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

The client credentials grant type defines a procedure for issuing access tokens in exchange for **app credentials**. These app credentials are the consumer key and secret pair that Apigee issues for each app that is registered in an organization. For more details, see [Implementing the authorization code grant type](https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/oauth-v2-policy-authorization-code-grant-type).

## Add OAuth v2.0 to a new API proxy

You can add OAuth verification to an API when you create a new API proxy in the Apigee UI.

To add OAuth verification to an API:

  1. In the Google Cloud console, go to the **Apigee > Proxy development > API proxies** page.

[Go to API proxies](https://console.cloud.google.com/apigee/proxies)

  2. Select your organization from the project picker in the Google Cloud pane. The organization name is the same as your Google Cloud project name. 
  3. In the **API Proxies** pane, click **\+ Create**.
  4. In the **Create a proxy** pane, under **Proxy template** , select **Reverse proxy (most common)**.
  5. Configure the proxy with the following:  
Name | Value  
---|---  
**Proxy Name** | `helloworld_oauth2`  
**Base Path** |  `/hellooauth2` The **Project Base Path** is part of the URL used to make requests to the API proxy.  
**Description** | `hello world protected by OAuth v2.0`  
**Target (Existing API)** |  `https://mocktarget.apigee.net/ip` This defines the target URL that Apigee invokes on a request to the API proxy. This target just returns a simple response: `Hello, Guest!`.  
  6. Click **Next**.
  7. **Deploy (optional)** : 
     * **Deployment environments** : Optional. Use the checkboxes to select one or more environments in which to deploy your proxy. If you prefer not to deploy the proxy at this point, leave the **Deployment environments** field empty. You can always deploy the proxy later. 
     * **Service Account** : Optional. Attach a service account to your deployment to enable your proxy to access Google Cloud services, as specified in the service account's role and permissions. 
  8. Click **Create**.
  9. In the **Proxy summary** pane for the **helloworld_apikey** proxy, click the **Develop** tab.
  10. In the **Policies** menu, click control_point **Add policy**.
  11. In the **Create policy** pane, under **Security** , select **Verify API Key**.
  12. In the **Verify API Key** pane, complete the required fields in the **Name** and **Display name** sections using the following values: 
     * **Name** : Enter a policy name. For example, `VerifyAPIKey`.
     * **Display name** : Enter policy name for use in the UI. For example, `Verify API Key`.
  13. Click **Create**.
  14. Click control_point to add another policy. 
  15. In the **Create policy** pane, under **Mediation** , select **Assign Message**.
  16. In the **Assign Message** pane, complete the required fields in the **Name** and **Display name** sections using the following values: 
     * **Name** : Enter a policy name. For example, `AssignMessage`.
     * **Display name** : Enter policy name for use in the UI. For example, `Assign Message`.
  17. Click **Create**.
  18. Update the contents of the **Assign Message** policy to the following:

**Note:** The policy name will change to `Remove Header Authorization` once you make this edit. 
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <AssignMessage async="false" continueOnError="false" enabled="true" name="remove-header-authorization">
             <DisplayName>Remove Header Authorization</DisplayName>
             <Remove>
                 <Headers>
                     <Header name="Authorization"/>
                 </Headers>
             </Remove>
             <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
             <AssignTo createNew="false" transport="http" type="request"/>
         </AssignMessage>
         

  19. Add the `VerifyApiKey` and `Remove Header Authorization` policies.
     1. In the **Proxy endpoints** menu, click **Preflow**.
     2. In the **Request** pane of the visual editor, click control_point **Add policy step**.
     3. In the **Add policy step pane** , select **Verify API Key**.
     4. Click **Add**.
     5. In the **Request** pane of the visual editor, click control_point **Add policy step**.
     6. In the **Add policy step pane** , select **Remove Header Authorization**.
     7. Click **Add**.
  20. Click **Save**.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
