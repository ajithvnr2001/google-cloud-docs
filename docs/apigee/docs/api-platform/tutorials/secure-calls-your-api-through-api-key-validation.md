---
url: https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/secure-calls-your-api-through-api-key-validation/
title: Secure an API by requiring API keys \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:31:59.862329+00:00
---

# Secure an API by requiring API keys  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/secure-calls-your-api-through-api-key-validation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Secure an API by requiring API keys Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/ng-saas/chevrons-3-next.png)

**Note:** This video was recorded with a previous version of the Apigee UI; however, the concepts are still valid. 

**Video:** Check out this short video for an introduction on securing your API. 

**What you'll learn**

This tutorial explains how to:

  * Create an API proxy that requires an API key.
  * Create an API product, a developer, and a developer app.
  * Call your API with an API key.



It's important to protect your API from unauthorized access. One way to do that is with API keys.

When an app makes a request to an API proxy that is configured to verify an API key, the app must supply a valid key. At runtime, the Verify API Key policy checks that the supplied API key:

  * Is valid
  * Hasn't been revoked
  * Matches the API key for the API product that exposes the requested resources



If the key is valid, the request is allowed. If the key is invalid, the request results in an authorization failure.

**Note:** In order to complete this tutorial, you'll be creating and deploying a proxy that uses [ extensible policies vs. standard policies](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy). 

## Create the API proxy

Follow these steps to create an API proxy using the Apigee UI:

  1. In the Google Cloud console, go to the **Apigee > Proxy development > API proxies** page.

[Go to API proxies](https://console.cloud.google.com/apigee/proxies)

  2. Select your organization from the project picker in the Google Cloud pane. The organization name is the same as your Google Cloud project name.
  3. Click **\+ Create**.
  4. In the **Create a proxy** pane, under **Proxy template** , select **Reverse proxy (Most common)**. A reverse proxy routes incoming traffic to a backend service. 
  5. Configure the proxy as follows:  
Name | Value  
---|---  
**Proxy Name** | `helloworld_apikey`  
**Base Path** |  `/helloapikey` The **Project Base Path** is part of the URL used to make requests to the API proxy.  
**Description** | `hello world protected by API key`  
**Target (Existing API)** |  `http://mocktarget.apigee.net` This defines the target URL that Apigee invokes on a request to the API proxy. This target just returns a simple response: `Hello, Guest!`.  
  6. Click **Next**.
  7. **Deploy (optional)**. Leave these fields blank.
  8. Click **Create**.
  9. Apigee creates the new proxy and displays the summary of the proxy details in the **Proxy summary** pane.



## View the policies

Follow these steps to view the policies:

  1. In the **Proxy summary** pane for the **helloworld_apikey** proxy, click the **Develop** tab.
  2. In the **Policies** menu, click  control_point  **Add policy**.
  3. In the **Create policy** pane, under **Security** , select **Verify API Key**. 
  4. In the **Verify API Key** pane, complete the required fields in the **Name** and **Display name** sections using the following values: 
     * **Name** : Enter a policy name. For example, `VerifyAPIKey`.
     * **Display name** : Enter policy name for use in the UI. For example, `Verify API Key`.
  5. Click **Create**.
  6. Click control_point  to add another policy.
  7. In the **Create policy** pane, under **Mediation** , select **Assign Message**.
  8. In the **Assign Message** pane, complete the required fields in the **Name** and **Display name** sections using the following values: 
     * **Name** : Enter a policy name. For example, `AssignMessage`.
     * **Display name** : Enter policy name for use in the UI. For example, `Assign Message`.
  9. Click **Create**.
  10. The `<APIKey>` element in the XML code below specifies the location of the API key within the incoming request. By default, the policy retrieves the key from a query parameter named `apikey` in the HTTP request. 
         
         <APIKey ref="request.queryparam.apikey" />

The name `apikey` is arbitrary and can be any property that contains the API key.

  11. Update the contents of the **Assign Message** policy to the following: **Note:** The policy name will change to `Remove Query Param apikey` once you make this edit. 
    
    <AssignMessage async="false" continueOnError="false" enabled="true" name="remove-query-param-apikey">
        <DisplayName>Remove Query Param apikey</DisplayName>
        <Remove>
            <QueryParams>
                <QueryParam name="apikey"/>
            </QueryParams>
        </Remove>
        <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
        <AssignTo createNew="false" transport="http" type="request"/>
    </AssignMessage>

  12. Add the `VerifyApiKey` and `Remove Query Param apikey` policies. 
     1. In the **Proxy endpoints** menu, click **Preflow**.
     2. In the **Request** pane of the visual editor, click  control_point **Add policy step**.
     3. In the **Add policy step** pane, select **Verify API Key**.
     4. Click **Add**.
     5. In the **Request** pane of the visual editor, click  control_point **Add policy step**.
     6. In the **Add policy step** pane, select **Remove Query Param apikey**.
     7. Click **Add**.
  13. Click **Save**.
  14. Deploy your proxy to an environment: 
     1. Click **Deploy**.
     2. Select a **Revision** and an **Environment**.
     3. Click **Deploy**.
  15. Test your changes by calling the API as described in [ Try to call the API](https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/secure-calls-your-api-through-api-key-validation#trytocalltheapi).



## Try to call the API

In this step, you'll make a successful API call directly to the target service, then you'll make an unsuccessful call to the API proxy to see how it's being protected by the policies.

  1. **Success**

In a web browser, go to the following address. This is the target service that the API proxy is configured to forward the request to, but you'll hit it directly for now:
         
         http://mocktarget.apigee.net

You should get this successful response: `Hello, Guest!`

  2. **Failure**

Now try to call your API proxy:
         
         curl -v -k https://YOUR_ENV_GROUP_HOSTNAME/helloapikey

where `YOUR ENV_GROUP_HOSTNAME` is the environment group hostname. See [ Find the environment group hostname](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/test-proxy#find-the-environment-group-hostname).

**Note:** If you have trouble calling the proxy, you may need to add the `Host` header, as described in [Deploy a sample proxy](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/deploy-sample).

Without the Verify API Key policy, this call would give you the same response as the previous call. But in this case, you should get the following error response:
         
         {"fault":{"faultstring":"Failed to resolve API Key variable request.queryparam.apikey","detail":{"errorcode":"steps.oauth.v2.FailedToResolveAPIKey"}}}

which means, correctly, that you didn't pass a valid API key (as a query parameter).




In the next steps, you'll get the required API key.

## Adding an API product

To add an API product using the Apigee UI:

  1. In the Google Cloud console, go to the **Distribution > API products** page:

[Go to API products](https://console.cloud.google.com/apigee/apiproducts)

  2. Click **+Create**.
  3. Enter the **Product details** for your API product.  
Field | Description  
---|---  
Name | Internal name of the API product. Do not specify special characters in the name.   
**Note:** You cannot edit the name once the API product is created.  
Display name | Display name for the API product. The display name is used in the UI and you can edit it at any time. If not specified, the **Name** value is used. This field is auto-filled using the **Name** value; you can edit or delete its contents. The display name can include special characters.  
Description | Description of the API product.  
Environment | Environments to which the API product will allow access. For example, `test` or `prod`.  
Access | Select **Public**.  
Automatically approve access requests | Enable automatic approval of key requests for this API product from any app.   
Quota | Ignore for this tutorial.  
Allowed OAuth Scopes | Ignore for this tutorial.  
  4. In the **Operations** section, click **Add an operation**.
  5. In the **API Proxy** field, select the API proxy you just created.
  6. In the **Path** field, enter "/". Ignore the other fields.
  7. Click **Save** to save the operation.
  8. Click **Save** to save the API product.



For more information on adding an API product, see [ Create an API product](https://docs.cloud.google.com/apigee/docs/api-platform/publish/create-api-products#add).

## Add a developer and app to your organization

Next, we're going to simulate the workflow of a developer signing up to use your APIs. A developer will have one or more apps that call your APIs, and each app gets a unique API key. This gives you, the API provider, more granular control over access to your APIs and more granular reporting on API traffic by app.

### Create a developer

To create a developer using the Apigee UI:

  1. In the Google Cloud console, go to the **Distribution > Developers** page:

[Go to Developers](https://console.cloud.google.com/apigee/developers)

  2. Click **\+ Create**.
  3. Enter the following in the **Add Developer** window:  
Field | Value  
---|---  
**First Name** | `Keyser`  
**Last Name** | `Soze`  
**Email** | `keyser@example.com`  
**Username** | `keyser`  
  4. Click **Add**.



For more information on creating a developer, see [ Registering app developers](https://docs.cloud.google.com/apigee/docs/api-platform/publish/adding-developers-your-api-product).

### Register an app

To register a developer app using the Apigee UI:

  1. In the Google Cloud console, go to the **Distribution > Apps** page: 

[Go to Apps](https://console.cloud.google.com/apigee/apps)

  2. Click **\+ Create**.
  3. Enter the following in the **Create App** window:  
Field | Value  
---|---  
**App Name** | Enter: `keyser_app`  
**Display Name** | Enter: `keyser_app`  
**Developer** | Select: `Keyser Soze (keyser@example.com)`  
**Callback URL** | Leave blank  
**Notes** | Leave blank  
  4. In the Credentials section, click **Add credential**.
  5. Select **Never**. The credentials for this app will never expire.
  6. Click **Add products**.
  7. Select the product you just created.
  8. Click **Add**.
  9. Click **Create**.



For more information on registering an app, see [ Registering an app](https://docs.cloud.google.com/apigee/docs/api-platform/publish/creating-apps-surface-your-api#register).

### Get the API key

To get the API key using the Apigee UI:

  1. In the Google Cloud console, go to the **Apigee > Distribution > Apps** page.

[Go to Apps](https://console.cloud.google.com/apigee/apps)

  2. Select the required app from the list of apps.
  3. On the **View app** page, under **Credentials** , click visibility_off next to the **Key** field. Notice that the key is associated with the product you created.
  4. Click content_copy **Copy**. You'll use this key in the next step.



## Call the API with a key

Now that you have an API key, you can use it to call the API proxy. Paste the API key as shown, as a query parameter. Make sure there are no extra spaces in the query parameter.
    
    
    curl -v -k https://YOUR_ENV_GROUP_HOSTNAME/helloapikey?apikey=YOUR_API_KEY

Now when you call the API proxy, you should get this response: `Hello, Guest!`

Congratulations! You've created an API proxy and protected it by requiring that a valid API key be included in the call.

Note that in general it's not good practice to pass an API key as a query parameter. You should consider passing it in the HTTP header instead.

## Best practice: Passing the key in the HTTP header

**Note:** It's a good practice to pass the API key in a header rather than in a query parameter. Query parameters appear in the browser history and network logs, which could present a security risk. Headers do not appear in the browser history and network logs. 

In this step, you will modify the proxy to look for the API key in a header called `x-apikey`.

  1. In the Google Cloud console, go to the **Proxy development > API proxies** page.

[Go to API proxies](https://console.cloud.google.com/apigee/proxies)

  2. Select the required proxy from the list of proxies.
  3. On the **Proxy details** page, click **Develop**.
  4. Modify the policy XML to tell the policy to look in the header rather than in the queryparam:
    
    <APIKey ref="request.**header**.x-apikey"/>

  5. Click **Save** to save the changes.
  6. Click **Deploy**.
  7. Select a **Revision** and an **Environment**.
  8. Click **Deploy**.
  9. Make the following API call using cURL to pass the API key as a header called `x-apikey`. Don't forget to substitute your organization name.
         
         curl -v -H "x-apikey: YOUR_API_KEY" http://YOUR_ENV_GROUP_HOSTNAME/helloapikey




Note that to fully complete the change, you'd also need to configure the Assign Message policy to remove the header instead of the query parameter. For example:
    
    
    <Remove>
      <Headers>
          <Header name="x-apikey"/>
      </Headers>
    </Remove>
    

**Note:** You could also pass the API key as a form parameter. If you did, the Verify API Key policy would be configured like this: 
    
    
    <APIKey ref="request.**formparam**.YOUR_API_KEY"/>

## Related topics

Here are some topics related to API products and keys:

  * [Managing API products](https://docs.cloud.google.com/apigee/docs/api-platform/publish/create-api-products)
  * [API keys](https://docs.cloud.google.com/apigee/docs/api-platform/security/api-keys)
  * [Registering app developers](https://docs.cloud.google.com/apigee/docs/api-platform/publish/adding-developers-your-api-product)
  * [Register apps and manage API keys](https://docs.cloud.google.com/apigee/docs/api-platform/publish/creating-apps-surface-your-api)
  * [Verify API Key policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/verify-api-key-policy)



API protection often involves additional security such as [OAuth](https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/oauth-home), an open protocol that exchanges credentials (like username and password) for access tokens. Access tokens are long, random strings that can be passed through a message pipeline, including from app to app, without compromising the original credentials.

For an overview of security-related topics, see [Securing a proxy](https://cloud.google.com/apigee/docs/api-platform/security/api-security).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
