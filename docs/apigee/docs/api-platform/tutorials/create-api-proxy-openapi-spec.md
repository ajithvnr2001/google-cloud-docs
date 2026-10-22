---
url: https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/create-api-proxy-openapi-spec/
title: Creating an API proxy from an OpenAPI Specification \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:49.915228+00:00
---

# Creating an API proxy from an OpenAPI Specification  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/create-api-proxy-openapi-spec/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Creating an API proxy from an OpenAPI Specification Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/ng-saas/chevrons-3-next.png)

**What you'll learn**

In this tutorial, you'll learn to:

  * Create an Apigee API proxy from an OpenAPI Specification.
  * Call the API proxy using cURL.
  * Add a policy to a conditional flow.
  * Test the policy invocation using cURL.



You'll learn how to create an Apigee API proxy from an OpenAPI Specification using the Apigee UI. When you call the API proxy with an HTTP client, such as cURL, the API proxy sends the request to the Apigee mock target service.

**About the Open API Initiative**

[![Open API Initiative](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/OpenAPI_Pantone.png)](https://openapis.org)

"The Open API Initiative (OAI) is focused on creating, evolving and promoting a vendor neutral API Description Format based on the Swagger Specification." For more information about the Open API Initiative, see [The OpenAPI Specification](https://openapis.org).

An _OpenAPI Specification_ uses a standard format to describe a RESTful API. Written in either JSON or YAML format, an OpenAPI Specification is machine readable, but is also easy for humans to read and understand. The specification describes such elements of an API as its base path, paths and verbs, headers, query parameters, operations, content types, response descriptions, and more. In addition, an OpenAPI Specification is commonly used to generate API documentation.

**About the Apigee mock target service**

The Apigee mock target service used in this tutorial is hosted at Apigee and returns simple data. It requires no API key or access token. In fact, you can access it in a web browser. Try it out by clicking the following:

[http://mocktarget.apigee.net](https://mocktarget.apigee.net)

The target service returns the greeting `Hello, guest!`

For information about the full set of APIs the mock target service supports, see [Apigee Sample APIs](https://mocktarget.apigee.net/help)

## What you'll need

  * **Before you begin, you must complete the steps in** [Overview and prerequisites](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/overview).
  * An OpenAPI Specification. In this tutorial, you'll use the `mocktarget.yaml` OpenAPI Specification which describes Apigee's mock target service, `http://mocktarget.apigee.net`. For more information, see [ apigee/api-platform-samples](https://github.com/apigee/api-platform-samples/tree/master/default-proxies/helloworld/openapi). 
  * [cURL](https://curl.haxx.se/) installed on your machine to make API calls from the command line; or a web browser.



## Create the API proxy

To create the API proxy from an OpenAPI Specification:

  1. In the Google Cloud console, go to the **Apigee > Proxy development > API proxies** page.

[Go to API proxies](https://console.cloud.google.com/apigee/proxies)

  2. In the **API Proxies** pane, click **\+ Create**.
  3. In the **Create a proxy** pane, under **Proxy template** > **OpenAPI spec template** , select **Reverse proxy (Most common)**.
  4. Navigate to the following URL in your web browser: 
         
         https://raw.githubusercontent.com/apigee/api-platform-samples/master/default-proxies/helloworld/openapi/mocktarget3.0.yaml

  5. Right-click on the displayed code and select **Save As**.
  6. Click **Save** to save the `mocktarget3.0.yaml` at the desired location.
  7. In the **OpenAPI specs** field, click the **Browse** button.
  8. Navigate to the `mocktarget3.0.yaml` file and click **Open**.
  9. Click **Next**.
  10. The **Proxy details** step of the **Create Proxy** wizard automatically populates its fields with values extracted directly from the OpenAPI Specification.

The following table describes the default values that are pre-populated using the OpenAPI Specification: 

Field | Description | Default  
---|---|---  
**Proxy name** | Name of the API proxy. For example: `Mock-Target-API`. | `title` property from the OpenAPI Specification with spaces replaced by dashes  
**Base path** | Path component that uniquely identifies this API proxy within the organization. The public-facing URL of this API proxy is comprised of your external or internal domain name and this base path. For example: `http://apitest.acme.com/mock-target-api` | **Name** field content converted to all lower case  
**Description** | Description of the API proxy. | `description` property from the OpenAPI Specification  
**Target (Existing API)** | Target URL invoked on behalf of this API proxy. Any URL that is accessible over the open Internet can be used. For example: `http://mocktarget.apigee.net` |  `servers` property from the OpenAPI Specification   
  
The following provides an excerpt from the OpenAPI Specification showing the properties that are used to pre-populate the fields.
    
    openapi: 3.0.0
          info:
            **description** : OpenAPI Specification for the Apigee mock target service endpoint.
            version: 1.0.0
            **title** : Mock Target API
          paths:
            /:
              get:
                summary: View personalized greeting
                operationId: View a personalized greeting
                description: View a personalized greeting for the specified or guest user.
                parameters:
                  - name: user
                    in: query
                    description: Your user name.
                    required: false
                    schema:
                      type: string
                responses:
                  "200":
                    description: Success
          ...
          **servers** :
            - url: http://mocktarget.apigee.net
            - url: https://mocktarget.apigee.net
          ...
          

  11. In the **Proxy details** step, edit the **Description** field as follows: 
         
         API proxy for the Apigee mock target service endpoint.

  12. Click **Next**.
  13. In the **Flows** step, make sure all operations are selected. **Tip:** Conditional flows are generated automatically from the operations that are defined within the `paths` object in the OpenAPI Specification. Conditional flows tell Apigee, "When you see this, perform this logic." For example, when an API call is a `GET` on the `/xml` resource (the condition), transform the response to JSON (through a policy attached to the conditional flow). Only one flow executes per transaction—the first flow whose condition evaluates to true.
  14. Click **Next**.
  15. In the **Deploy** step, select one or more environments, and click **OK**. 
  16. Click **Create**.

**Congratulations!** You've created an API proxy from an OpenAPI Specification. Next you'll test it to see how it works.

## Test the API proxy

You can test your `Mock-Target-API` API using cURL or a web browser.
    
    
    curl -v YOUR_ENV_GROUP_HOSTNAME/myproxy

where `YOUR_ENV_GROUP_HOSTNAME` is your environment group hostname. See [ Find your environment group hostname](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/test-proxy#find-your-environment-group-hostname).

For example: 
    
    
    curl -v -k https://apitest.acme.com/myproxy

**Response**

You should see the following response:
    
    
    Hello, Guest!

**Way to go!** You've built a simple API proxy from an OpenAPI Specification and tested it.

## Add an XML to JSON policy

Next, you'll add the XML to JSON policy to the **View XML Response** conditional flow that was generated automatically when you created the API proxy from the OpenAPI Specification. The policy will convert the target's XML response to a JSON response.

First, call the API so that you can compare the results with those received after you add the policy. In a terminal window execute the following cURL command. You're calling the target service's `/xml` resource, which natively returns a simple block of XML.
    
    
    curl -v https://YOUR_ENV_GROUP_HOSTNAME/mock-target-api/xml

where `YOUR ENV_GROUP_HOSTNAME` is the environment group hostname. See [ Find the environment group hostname](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/test-proxy#find-the-environment-group-hostname).

**Response**

You should see the following response:
    
    
    <root>
      <city>San Jose</city>
      <firstName>John</firstName>
      <lastName>Doe</lastName>
      <state>CA</state>
    </root>

Now let's do something that converts the XML response to JSON. Add the XML to JSON policy to the View XML Response conditional flow in the API proxy.

  1. Click the **Develop** tab in the **Mock-Target-API Overview** page in the Apigee UI.

![Select View XML Response](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/view-xml-response-policy.png)

  2. In the left-hand pane, under **Proxy Endpoints > default**, click the **View XML Response** conditional flow.
  3. In the left-hand pane, click the **+** button in the **Policies** row.
  4. In the **Create policy** dialog, click in the **Select policy type** field, scroll down to **Mediation** , and select **XMLToJSON**. Keep the default values for **Display Name** and **Name**.

  5. Click **Create** to create the policy.
  6. Click the **+** button next to the **View XML response** flow in the **Response**. 

![Select +Step](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/view-xml-response-add-step.png)

  7. In the **Add Policy Step** dialog, click in the **Select existing policy** field and select **XML to JSON-1**.
  8. Click **Add**. The XML to JSON policy is applied to the response.

![XML to JSON policy in flow](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/xml-to-json-in-flow.png)

To view the code for the **View XML Response** conditional flow, click **Switch To Code Editor**.

  9. Click **Save**.



Now that you've added the policy, call the API again using cURL. Notice that you're still calling the same `/xml` resource. The target service still returns its block of XML, but now the policy in the API proxy will convert the response to JSON. Make this call:
    
    
    curl -v https://YOUR_ENV_GROUP_HOSTNAME/mock-target-api/xml

where `YOUR ENV_GROUP_HOSTNAME` is the environment group hostname. See [ Find the environment group hostname](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/test-proxy#find-the-environment-group-hostname).

Note that the XML response is converted to JSON:
    
    
    {"root":{"city":"San Jose","firstName":"John","lastName":"Doe","state":"CA"}}

**Congratulations!** You have successfully tested the execution of a policy added to a conditional flow.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

  * ### Products and pricing

    * [ See all products ](https://cloud.google.com/products/)
    * [ Google Cloud pricing ](https://cloud.google.com/pricing/)
    * [ Google Cloud Marketplace ](https://cloud.google.com/marketplace/)
    * [ Contact sales ](https://cloud.google.com/contact/)
  * ### Support

    * [ Community forums ](https://discuss.google.dev/c/google-cloud/14/)
    * [ Support ](https://cloud.google.com/support-hub/)
    * [ Release Notes ](https://docs.cloud.google.com/release-notes)
    * [ System status ](https://status.cloud.google.com)
  * ### Resources

    * [ GitHub ](https://github.com/googlecloudPlatform/)
    * [ Getting Started with Google Cloud ](https://docs.cloud.google.com/docs/get-started/)
    * [ Code samples ](https://docs.cloud.google.com/docs/samples)
    * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture/)
    * [ Training and Certification ](https://cloud.google.com/learn/training/)
    * [ Builders Hub ](https://me.developers.google.com/)
  * ### Engage

    * [ Blog ](https://cloud.google.com/blog/)
    * [ Events ](https://cloud.google.com/events/)
    * [ X (Twitter) ](https://x.com/googlecloud)
    * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
    * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v9ce9cb5b22b62a465ff52c45061a0a6a2d86a80b685e9aa8a182b203fdfbf420/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)

  * [ Android ](https://developer.android.com/)
  * [ Chrome ](https://developer.chrome.com/)
  * [ Firebase ](https://firebase.google.com/)
  * [ Google AI ](https://ai.google.com/)



  * [ About Google ](https://about.google/)
  * [ Privacy ](https://policies.google.com/privacy)
  * [ Site terms ](https://policies.google.com/terms?hl=en)
  * [ Google Cloud terms ](https://cloud.google.com/product-terms)
  * Manage cookies 
  * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
  * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)



  * English
  * Deutsch
  * Español
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português
  * Português – Brasil
  * עברית
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어


