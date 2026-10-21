---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-deploy-proxy/
title: Step 2: Deploy an API proxy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:37:57.410771+00:00
---

# Step 2: Deploy an API proxy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-deploy-proxy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Step 2: Deploy an API proxy Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.13 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.13 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-deploy-proxy.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-deploy-proxy.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/install-deploy-proxy.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/install-deploy-proxy.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-deploy-proxy.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-deploy-proxy.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-deploy-proxy.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-deploy-proxy.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-deploy-proxy.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/install-deploy-proxy.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/install-deploy-proxy.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/install-deploy-proxy.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/install-deploy-proxy.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/install-deploy-proxy.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/install-deploy-proxy.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/install-deploy-proxy.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/install-deploy-proxy.html)



Now that you've configured Google Cloud and the Apigee UI, and installed and configured the runtime, you're ready to see how it all works together.

## 1\. Create a new API proxy using the Apigee UI

This section describes how to create a new API proxy in the UI using the API Proxy Wizard.

**Note:** There is a new version of the Apigee UI, which is integrated with the Google Cloud console. The new UI is called _Apigee in Cloud console_. The instructions in the first two tabs below explain how to use either Apigee in Cloud console or classic Apigee UI. 

### Apigee in the Cloud console

To create a new API proxy using Apigee in the Cloud console:

  1. Open the Apigee UI in a browser.
  2. Select your organization from the dropdown menu in the upper left corner.
  3. Select **Proxy development > API proxies** in the main view.
  4. Click **Create**.The API Proxy Wizard starts. 
  5. Select **Reverse proxy** (most common). 

The **Proxy details** view is displayed.

  6. Configure your proxy with the following settings: 
     * **Proxy name:** Enter **myproxy**. The remaining steps in this section assume that this is your proxy's ID.
     * **Base path:** Automatically set to **/** followed by the proxy name, which in this example is **/myproxy**. The **Base path** is part of the URL used to make requests to your API. Apigee uses the URL to match and route incoming requests to the proper API proxy.
     * (Optional)**Description:** Enter a description for your new API proxy, such as "Testing Apigee hybrid with a simple proxy".
     * **Target (Existing API):** Enter "https://mocktarget.apigee.net". This defines the target URL that Apigee invokes on a request to the API proxy. The mocktarget service is hosted at Apigee and returns simple data. It requires no API key or access token.

Your API proxy's details should look like the following:

![Proxy details in create proxy wizard.](https://docs.cloud.google.com/static/apigee/docs/hybrid/v1.13/images/test-proxy-wizard-details-cloud-console.png)

  7. Click **Next**.
  8. Under **Deploy (optional)** , you have the option to select one or more environments in which to deploy your proxy, in the **Deployment environments** field. If you prefer not to deploy the proxy at this point, leave the **Deployment environments** field empty. You can always deploy the proxy later.
  9. Click **Create**. Apigee generates the proxy (sometimes referred to as _the proxy bundle_). 



Apigee displays the **Proxy summary** view. If you chose to deploy the proxy, the **Deployments** section displays the **Revision** number, which is 1 when you first deploy. The **Status** column displays the environments in which the proxy is deployed with a green status indicator.

Below that, the **Revisions** section shows all revisions made to this proxy. By clicking on one of the **VIEW** items in the **Endpoint summary** column, the **Endpoint** section displays:

  * **Proxy endpoints** : The basepath you set for the proxy, which is this example is `/myproxy`.
  * **Target endpoints** : The basepath you set for the target, which in this example is `https://mocktarget.apigee.net`.



### Classic Apigee

To create a new API proxy using Classic Apigee:

  1. Open [Apigee UI](https://apigee.google.com) in a browser.
  2. Select your organization from the dropdown menu in the upper left corner.
  3. Select **Develop > API Proxies** in the main view.
  4. Click **Create New**.The API Proxy Wizard starts. 
  5. Select **Reverse proxy** (most common). 

The **Proxy details** view is displayed.

  6. Configure your proxy with the following settings: 
     * **Proxy Name:** Enter "myproxy". The remaining steps in this section assume that this is your proxy's ID.
     * **Proxy Base Path:** Automatically set to "/myproxy". The **Proxy Base Path** is part of the URL used to make requests to your API. Apigee uses the URL to match and route incoming requests to the proper API proxy.
     * (Optional)**Description:** Enter a description for your new API proxy, such as "Testing Apigee hybrid with a simple proxy".
     * **Target (Existing API):** Enter "https://mocktarget.apigee.net". This defines the target URL that Apigee invokes on a request to the API proxy. The mocktarget service is hosted at Apigee and returns simple data. It requires no API key or access token.

Your API proxy's details should look like the following:

![Proxy details in the Create Proxy wizard.](https://docs.cloud.google.com/static/apigee/docs/hybrid/v1.13/images/test-proxy-wizard-details.png)

  7. Click **Next**.
  8. On the **Common policies** screen, select **Pass through (no authorization)** as the security option. 
  9. Click **Next**.
  10. On the **Summary** screen, select an environment to deploy your proxy to and click **Create and Deploy**. 

Hybrid generates the proxy (sometimes referred to as _the proxy bundle_) and deploys it to the environment you selected.

  11. Click **Go to proxy list**. 

Apigee displays the **Proxies** view, which displays a list of API proxies. Your new proxy should display with a green status indicator, meaning that it has been deployed.




##  2\. Call the API proxy 

When the UI indicates your proxy is deployed, you can try calling it using cURL or the REST client of your choice. For example:

  1. Make sure your `DOMAIN` environment variable is set to the domain name you used for the hostname for your environment group in [Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/precog-add-environment). 
         
         echo $DOMAIN

  2. Find the external IP address and port of the Apigee ingress gateway with the following command:
         
         kubectl get svc -n APIGEE_NAMESPACE -l app=apigee-ingressgateway

Your output should look something like: 
         
         NAME                                        TYPE           CLUSTER-IP    EXTERNAL-IP     PORT(S)                                      AGE
         apigee-ingressgateway-prod-hybrid-37a39bd   LoadBalancer   192.0.2.123   **233.252.0.123**   15021:32049/TCP,80:31624/TCP,**443** :30723/TCP   16h

  3. Export your external IP and port to variables: 
         
         export INGRESS_IP_ADDRESS=EXTERNAL_IP_ADDRESS
         export INGRESS_PORT=PORT_NUMBER

  4. Call the API proxy: 
         
         curl  -H Host:$DOMAIN --resolve \
           $DOMAIN:$INGRESS_PORT:$INGRESS_IP_ADDRESS  \
           https://$DOMAIN:$INGRESS_PORT/myproxy -k -v

For example: 
         
         curl -v -H Host:example.com --resolve example.com:443:233.252.0.123 https://example.com:443/myproxy -k -v

  5. A successful call to the proxy returns an HTTP 200 response code and the following output. 
         
         Hello, Guest!




To learn more about building and deploying API proxies, see [Build your first proxy overview](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/get-started). 

**Congratulations!**

You've successfully installed Apigee hybrid. To learn more about building and deploying API proxies, see [Introduction to API proxy building](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/build-simple-api-proxy).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
  *[Google Cloud]: Google Cloud
