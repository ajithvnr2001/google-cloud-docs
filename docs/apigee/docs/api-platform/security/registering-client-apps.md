---
url: https://docs.cloud.google.com/apigee/docs/api-platform/security/registering-client-apps/
title: Registering client apps \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:30:18.460575+00:00
---

# Registering client apps  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/security/registering-client-apps/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Registering client apps Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

To participate in OAuth 2.0 flows on Apigee, client apps must be registered. 

## What is registration?

Registration allows Apigee (the authorization server) to uniquely identify your app. When you register your app, you receive back two keys: a client ID and client secret. The app needs these keys when negotiating for access tokens with the authorization server.

## Quick steps

To register a new app, from the **Apps** page:

  1. In the Google Cloud console, go to the **Apigee > Distribution > Apps** page. 

[Go to Apps](https://console.cloud.google.com/apigee/apps)

  2. Click **Create**.
  3. Specify the **App Details** , as described in the following table: Field | Description | Required?  
---|---|---  
App Name | Name of the app. You can't change the name once the app is created. This name is used in [Apigee API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest) calls. | Required  
Display Name | Display name for the app that appears in the Apigee UI and the developer portal. | Optional  
Developer | Select a developer name from the drop-down. **Note:** For performance reasons, not all developers are displayed in the drop-down. Start typing the developer name or email in the search box, and the drop-down values are automatically refined to match the text you are typing. See also [Register app developers](https://docs.cloud.google.com/apigee/docs/api-platform/publish/adding-developers-your-api-product). | Required  
Callback URL | Typically specifies the URL of an app that is designated to receive an authorization code on behalf of the client app. This value is not required for all API products. | Optional  
Notes | Descriptive notes for the app. | Optional  
**Note:** The app details also include an App ID which is only viewable and editable from the API, not the UI. See [REST Resource: organizations.developers.apps](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps#DeveloperApp). 
  4. Specify the **Credentials** , including the API key expiration, status, and the associated API products. In the **Credentials** section, click **add Add credential** and enter the following information: Field | Description  
---|---  
Expiry | Select an expiration duration or date, or set the API key to never expire.  
Products | Associate one or more API products with the API key: 
     1. Click **add Add products**.
     2. Select one or more API products from list. **Note:** At least one API product must be selected.
     3. Click **OK**.
     4. Click **Add**.  
  5. Set the **Status** to **Approved** or **Revoked** for each API product. If you added an API product to the credential that requires manual approval, it will show `Pending approval status`. Otherwise, it will show `Approved`. In this step, you can change the approval status. 
     1. From the list of **Products** in the **Credentials** section, select one or more products from the list.
     2. Click **Approve** or **Revoke**.
  6. Click **Create**.
  7. Find your new app in the list of developer apps and select it.
  8. Click visibility_off to see the **Key** (client ID) and **Secret** (client secret) values. 



## More information

For a more detailed discussion of app registration, see [Register apps and manage API keys](https://docs.cloud.google.com/apigee/docs/api-platform/publish/creating-apps-surface-your-api). If you'd like to know more about the role of API products, see [What is an API product?](https://docs.cloud.google.com/apigee/docs/api-platform/publish/what-api-product).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
