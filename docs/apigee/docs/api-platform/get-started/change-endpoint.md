---
url: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/change-endpoint/
title: Step 4: Change the target endpoint \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:48:09.432367+00:00
---

# Step 4: Change the target endpoint  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/change-endpoint/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Step 4: Change the target endpoint Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

An Apigee API proxy has two endpoints: a proxy endpoint and a target endpoint. The proxy endpoint is the client interface. It receives requests from clients and sends responses back to clients. The target endpoint is the API producer interface. It communicates from Apigee to an API producer, such as a backend service or API. To learn more about endpoints, see [What is an API proxy?](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/understanding-apis-and-api-proxies#whatisanapiproxy)

In this step, you will change the API proxy's target endpoint to `https://mocktarget.apigee.net/xml`, a resource that returns test XML data. After making the change, you will redeploy and test the revised API proxy. 

  1. In the Google Cloud console, go to the **Apigee > Proxy development > API proxies** page.

[Go to API proxies](https://console.cloud.google.com/apigee/proxies)

  2. Make sure the same Google Cloud project where you created the API proxy is selected from the dropdown at the top of the page.
  3. In the proxies table, select the proxy **myproxy** , which you created in [Step 1: Create an API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/create-proxy).
  4. Click the **Develop** tab.



### Explore the Develop view

In the left-hand pane of the **Develop** view, you can:

  * Search for text in the proxy in the **Search proxy** field.
  * Add new policies.
  * Add proxy and target endpoints.
  * Add other resources.



If you don't want to view the left-hand pane, you can collapse it by clicking the close button ![Close search pane button.](https://docs.cloud.google.com/static/apigee/docs/api-platform/get-started/images/close-pane-button.png).

The right-hand pane of the **Develop** view displays the visual and text editors for the proxy:

  * The visual editor provides a graphical view of the request and response flow.
  * The text editor lets you edit the XML for the proxy or target.



![Visual and text editors with selectable divider.](https://docs.cloud.google.com/static/apigee/docs/api-platform/get-started/images/visual-text-editors.png)

**Notes:**

  * You can click and drag the divider between the two editors up or down to expand the display area of either editor.
  * You can expand the display area of the visual editor by clicking the toggle button on the right side of the text editor, which closes the text editor pane. Click the toggle button again to re-open the text editor pane.



### Change the target endpoint

To change the target endpoint of the proxy:

  1. In the **Proxy revision** pane, select **Target Endpoints > default**. 

![Target endpoints selected in the Proxy Explorer.](https://docs.cloud.google.com/static/apigee/docs/api-platform/get-started/images/proxy-revision.png)

This displays a diagram of the target endpoint in the visual editor:

![Target endpoints selected in the Proxy Explorer.](https://docs.cloud.google.com/static/apigee/docs/api-platform/get-started/images/target-endpoints-default.png)

Below the visual editor, the XML code for the target endpoint is displayed in the text editor:

![XML for target endpoint displayed in text editor.](https://docs.cloud.google.com/static/apigee/docs/api-platform/get-started/images/xml-code-for-target-endpoint.png)

  2. In the text editor, change the `<URL>` to `https://mocktarget.apigee.net**/xml**`. (Append "/xml" to the existing URL.)

The new URL is shown below:
         
         ...
         <HTTPTargetConnection>
           <Properties/>
           **< URL>https://mocktarget.apigee.net/xml</URL>**
         </HTTPTargetConnection>
         ...

  3. Click the arrow next to **Save** at the top right of the Proxy Editor, and select **Save as new revision**.
  4. To deploy your changes, click **Deploy**.
  5. In the **Deploy** dialog, select the revision and environment in which to deploy, and click **Deploy**.



## Test the proxy

To test the API proxy revision, call the proxy just as you did in [Call an API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/test-proxy).

This time, the mocktarget endpoint returns XML in the body of the response:
    
    
    <?xml version="1.0" encoding="UTF-8"?>
    <root>
      <city>San Jose</city>
      <firstName>John</firstName>
      <lastName>Doe</lastName>
      <state>CA</state>
    </root>

Now that the API proxy returns XML data, in the next step you will add a policy that converts XML to JSON.

[1](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/create-proxy) [2](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/deploy-proxy) [3](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/test-proxy) [4](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/change-endpoint) [(NEXT) Step 5: Add a policy](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/add-policy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
