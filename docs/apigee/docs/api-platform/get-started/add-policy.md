---
url: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/add-policy/
title: Step 5: Add a policy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:56:04.566211+00:00
---

# Step 5: Add a policy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/add-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Step 5: Add a policy Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/ng-saas/chevrons-2-build.png)

Now that you've [changed your target endpoint](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/change-endpoint), you're ready to add a policy to your proxy.

A _policy_ is an Apigee component that you can attach to different points in the message flow through your API proxies. Policies can transform message formats, enforce access control, call remote services, authorize users, examine message content for potential threats, and do much more.

In this tutorial, you're going to add the [XMLtoJSON policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/xml-json-policy) to your proxy. This policy converts the payload of an XML message to JSON. It also changes the response's `Content-Type` header.

You can attach a policy to a _flow_ in the proxy. Flows control how policies are executed. In this example, you'll add the policy to a special flow, called the _PreFlow_. Policies in the PreFlow, are executed before any other policies in the proxy. While you don't need to understand flows in detail to read this example, you can learn more about them in [Controlling API proxies with flows](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-are-flows).

### Further Reading

There are dozens of out-of-the-box policies that you can add to your proxies, including:

  * [AssignMessage policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy)
  * [RaiseFault policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/raise-fault-policy)
  * [JavaScript policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/javascript-policy)
  * [SpikeArrest policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy)
  * [ExtractVariables policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/extract-variables-policy)



For a complete list of policies, see [Policy reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy).

## Add the policy

Add the XMLtoJSON policy to your proxy.

There are two steps to add the XMLtoJSON policy to your proxy:

  * Create an instance of the policy.
  * Attach the policy to a step in the PreFlow.



### Create an instance of the policy

To use a policy, you first have to create a new instance of the policy from the policy template as follows:

  1. In the Google Cloud console, go to the **Apigee > Proxy development > API proxies** page.

[Go to API proxies](https://console.cloud.google.com/apigee/proxies)

  2. From the proxies list, select the proxy in which you want to add the policy.
  3. Click the **Develop** tab.

  4. In the left-hand pane, click the **+** button next to the **Policies** folder.
  5. In the **Create policy** dialog, select **Standard policies** to filter the available policy list by [policy type](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types).
  6. In the **Select policy type** text box, scroll down to **Mediation** and select [**XML To JSON**](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/xml-json-policy). 
  7. Optionally, you can change the **Name** and **Display name** of the policy. By default, Apigee provides a short prefix for the policy name, in this case, **X2J-** , You can add a sequence of descriptive words separated by dashes, after the prefix. See [ Naming conventions](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/best-practices-api-proxy-design-and-development#developmentstandards-namingconventions).

![Create policy dialog.](https://docs.cloud.google.com/static/apigee/docs/api-platform/get-started/images/create-policy-dialog.png)

When you are done, click **Create** to create the policy.




The XML To JSON policy is now displayed in the right-hand pane of the **Develop** view:

![XML To JSON policy displayed in Develop view.](https://docs.cloud.google.com/static/apigee/docs/api-platform/get-started/images/xml-to-json-policy.png)

The lower half of the pane displays the XML code for the policy.

To learn more about the policy, select the information icon ![Information icon.](https://docs.cloud.google.com/static/apigee/docs/api-platform/get-started/images/information-icon.png) next to the policy name and click [ XML To JSON policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/xml-json-policy). This displays the reference page for the policy.

### Use Gemini Code Assist to review policy instructions

You can use Gemini Code Assist in the UI to learn about policy elements. See [Use Gemini Code Assist code explain with policies](https://docs.cloud.google.com/apigee/docs/api-platform/develop/attaching-and-configuring-policies-management-ui#use-gemini-code-assist-code-explain) for information.

### Change the policy name

To change the name of a policy: 

  1. Select the policy under **Policies** in the left-hand pane.
  2. In the **< DisplayName>** element in the XML code for the policy, add a descriptive phrase for the policy, such as **change-xml-to-json** , after the abbreviation for the policy name: 

![Add change-xml-to-json to policy name.](https://docs.cloud.google.com/static/apigee/docs/api-platform/get-started/images/change-xml-to-json.png)

This automatically updates the policy name, displayed under **Policies**.

See [ Naming conventions](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/best-practices-api-proxy-design-and-development#developmentstandards-namingconventions).




### Attach the policy to a step in the PreFlow

Now that you have created the **XML To JSON** policy, you can attach it to a step in the PreFlow:

  1. Select **Proxy Endpoints > default > PreFlow** in the left-hand pane: 

![Target endpoints for PreFlow select in the Proxy Explorer.](https://docs.cloud.google.com/static/apigee/docs/api-platform/get-started/images/select-proxy-endpoints-preflow.png)

**Note:** You may need to expand the visual editor in the right-hand pane to see all the elements. To do so, click and drag the divider between the visual editor and the text editor down a little.

  2. Click the **+** button next to **PreFlow** in the **Response** pane at the bottom-right of the visual editor: 

![Click + button next to PreFlow in the Response pane.](https://docs.cloud.google.com/static/apigee/docs/api-platform/get-started/images/add-policy-to-response-preflow.png)

  3. In the **Add policy step** dialog, select the **X2J-change-xml-to-json** policy.
  4. Click **Add** to attach the policy.

The **X2J-change-xml-to-json** policy is now displayed in the **Response** pane:

![XML To JSON policy displayed in Response pane.](https://docs.cloud.google.com/static/apigee/docs/api-platform/get-started/images/xml-to-json-displayed-in-response-pane.png)

  5. Click **Save** to save the current revision with your changes.
  6. To deploy your changes to the revision, click **Deploy** and follow the instructions in [ Deploy an API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/deploy-proxy#deploy).



## Test the new policy

To test the new policy, execute the following `curl` command in a terminal window:
    
    
    curl https://YOUR_ENV_GROUP_HOSTNAME/myproxy

where `YOUR ENV_GROUP_HOSTNAME` is the environment group hostname. See [ Find the environment group hostname](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/test-proxy#find-the-environment-group-hostname).

See [ Call your API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/test-proxy) for more information.

Alternatively, you can open the same URL in a browser.

You should receive the following response:
    
    
    {
      "root": {
        "city": "San Jose",
        "firstName": "John",
        "lastName": "Doe",
        "state": "CA"
      }
    }

If the body of the response doesn't look like this, check that:

  1. Your target endpoint is `https://mocktarget.apigee.net/xml`, as described in [Step 4: Change your target endpoint](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/change-endpoint): 
     * If you get `Hello, Guest!` as a response, then you need to append `/xml` to the end of the target endpoint.
     * If you get a `404`, then check that you are accessing `apigee.net` and not `apigee.com`.
  2. The latest revision of your proxy is deployed. Try re-deploying your API proxy as described in [Deploying an API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/ui-deploy-new) and [Undeploying an API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/ui-undeploy).



To see the HTTP request and response headers, enable verbosity in `curl` with the `-vs` option (`v` makes the response verbose, but `s` suppresses some of the less interesting details). The following example assumes that the proxy is named `myproxy`::
    
    
    curl -vs https://YOUR_ENV_GROUP_HOSTNAME/myproxy  | python -m json.tool

You should get a response that looks like the following. Note that the `Content-Type` header in the response is `application/json`. The XMLtoJSON policy changes the header before sending the response back.
    
    
    *   Trying 10.20.30.40...
    * TCP_NODELAY set
    * Connected to apitest.acme.com (10.20.30.40) port 443 (#0)
    ...
    > GET /myproxy HTTP/1.1
    > Host: apitest.acme.com
    > User-Agent: curl/7.58.0
    > Accept: */*
    >
    < HTTP/1.1 200 OK
    < Date: Fri, 25 May 2018 16:20:00 GMT
    **< Content-Type: application/json;charset=UTF-8**
    < Content-Length: 77
    < Connection: keep-alive
    < X-Powered-By: Apigee
    < Access-Control-Allow-Origin: *
    ...
    { [77 bytes data]
    {
      "root": {
        "city": "San Jose",
        "firstName": "John",
        "lastName": "Doe",
        "state": "CA"
      }
    }

## Next step

[Go deeper](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/go-deeper)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
