---
url: https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/flow-hooks/
title: Attaching a shared flow using a flow hook \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:14:16.069558+00:00
---

# Attaching a shared flow using a flow hook  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/flow-hooks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Attaching a shared flow using a flow hook Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

You can have shared flows perform boilerplate request pre-processing or response post-processing across a set of APIs. With a _flow hook_ , you attach a shared flow so that it executes at the same place for all API proxies deployed to a specific environment. This gives you a separately implemented and deployed sequence of logic that is not part of a proxy's implementation code.

**Note:** Attaching a shared flow to a flow hook is an action that has a very broad effect. The attached shared flow will execute at the flow hook's point **for every proxy deployed to that environment**.

Because code attached to a flow hook is outside the context of the API proxy core logic, some of its behavior differs from API proxies. Keep the following in mind:

  * You must have permission to attach a shared flow to a flow hook. You must be an org admin.
  * You can attach only one shared flow to each flow hook.
  * You can attach the same shared flow to multiple flow hooks.
  * If a shared flow attached to a flow hook raises a fault or there are errors during shared flow execution, the message will be rejected and fault will be sent back to the caller.
  * If a message gets rejected during execution of a flow hook, details will be logged to analytics in the context of the called proxy. The shared flow can also throw a fault with a custom code and error message

**Note:** This video was recorded with a previous version of the Apigee UI; however, the concepts are still valid. 

The following video demonstrates how to connect a shared flow to a flow hook, then trace it, in the Apigee UI.

A shared flow attached to a proxy via a flow hook provides a great place for logic that enforces broad policy requirements. For example, imagine that you have one team managing a single set of security requirements for multiple teams that represent different lines of businesses (LOBs). Each LOB team can develop APIs according to their own requirements, and without needing to account for the broader security requirements. The security team can implement those security requirements in a shared flow, then attach the flow to the Apigee environment using a flow hook. Because the shared flow isn't part of proxy code, the security team can revise it as needed without interfering with LOB code.

Shared flows attached via flow hooks execute at that position for **every API proxy deployed to the proxy hook's environment**. For this reason, the ability to use flow hooks is available only to administrators of an Apigee organization.

For more about shared flows, see [Creating reusable shared flows](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/shared-flows).

You attach a shared flow to a flow hook using the Apigee UI or [Flowhooks API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.flowhooks). You can attach at most one shared flow to a flow hook at each of the following places:

  * **Pre-proxy flow hook** for logic that needs to be enforced BEFORE a proxy endpoint executes.

For example, you could have logic for enforcing security across all the APIs in an environment.

  * **Pre-target flow hook** for logic that needs to be enforced BEFORE a target endpoint executes.

For example, you could implement logging before the request reaches the backend. You could also enforce mediation by removing certain fields from the request.

  * **Post-target flow hook** for logic that needs to be enforced AFTER the target response executes.

This will be enforced right after the response comes back from the backend. You can use it to log the backend response or perform some mediation by removing sensitive fields from the backend response.

  * **Post-proxy flow hook** for logic that needs to be enforced AFTER the proxy endpoint and right before the response is sent out to the client.

This could include some enforcement logic for CORS, logging the response, or performing some mashup or formatting.




![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/flow-hook-3.png)

### Attaching a shared flow to a flow hook

To attach a shared flow to a flow hook, you must be an administrator in the organization containing the shared flow.

**Note:** Attaching a shared flow to a flow hook is an action that has a very broad effect. The attached shared flow will execute at the flow hook's point **for every proxy deployed to that environment**. 

To attach a shared flow to a flow hook:

  1. In the Google Cloud console, go to the **Apigee > Management > Environments** page.

[Go to Environments](https://console.cloud.google.com/apigee/environments)

  2. Select the organization containing your shared flow. See [Switching between your organizations](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/switch-org). 

The shared flow will be available to any API proxies and shared flows deployed to an environment from this organization. It won't be available from outside this organization.

  3. Select the environment you wish to edit from the list of available environments.
  4. Click the **Flow hooks** tab on the **Environment details** page. 

The **Flow hooks** view displays.

  5. In the list of flow hooks, identify the flow hook to which you want to attach the shared flow. The flow hook you choose depends upon where you want the shared flow to be executed. Flow hook location | Description  
---|---  
Pre-proxy | Executes _before_ a proxy endpoint executes  
Pre-target | Executes _before_ a target endpoint executes  
Post-target | Executes _after_ the target response executes  
Post-proxy | Executes _after_ the proxy endpoint and right before the response is sent out to the client  
  6. In the list box of the flow hook you chose, select the shared flow that you want to attach.
  7. Attach shared flows to other flow hooks as needed.
  8. Click **Save** to attach the selected shared flows to the flow hooks.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
