---
url: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/deploy-sample/
title: Recommended next steps \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:48:47.852606+00:00
---

# Recommended next steps  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/deploy-sample/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Recommended next steps Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/ng-saas/chevrons-1-setup.png)

## What you're doing in this step

Follow the steps below to create and deploy a test API proxy. Finally, test the API proxy by sending an HTTP request to it. 

## Create and deploy an API proxy

#### Permissions required for this task

Creating and deploying proxies requires a minimum set of permissions. If you have the Apigee Org Admin role, you can complete this task. To learn about other roles you can employ, see [ Apigee roles](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/apigee-roles). 

The provisioning process for Apigee does not automatically create and deploy an API proxy for you. You must create and deploy a proxy manually. 

To create and deploy your first proxy:

  1. In the Google Cloud console, go to the **Apigee > Proxy development > API proxies** page.

[Go to API proxies](https://console.cloud.google.com/apigee/proxies)

  2. Be sure that your organization name is selected from the project picker in the **Google Cloud** pane. The organization name is the same as your Google Cloud project name.
  3. Click **\+ Create**. 

The **Create a proxy** page opens.

  4. In the **Proxy template** box, select **Reverse proxy (most common)**.
  5. In **Step 1: Proxy details** , configure your proxy with the following values: Parameter name | Value  
---|---  
Proxy name | `hello-world`  
Base path | `/hello-world`  
Target (Existing API) | `mocktarget.apigee.net`  
  6. Click **Next**.
  7. In **Step 2: Deploy (optional)** : 
     * **Deployment environments** : Optional. Use the checkboxes to select one or more environments in which to deploy your proxy. If you prefer not to deploy the proxy at this point, leave the **Deployment environments** field empty. You can always deploy the proxy later. 
     * **Service Account** : Optional. Attach a service account to your deployment to enable your proxy to access Google Cloud services, as specified in the service account's role and permissions. 
  8. Click **Create**. 

Your new API proxy is created and deployed in the selected environment.

**Note:** The proxy is not fully deployed instantaneously. It can take up to a minute for the proxy to deploy. 
  9. The **Proxy summary** page for your newly created proxy opens. A green check mark under **Status** indicates that the proxy was successfully deployed. If the proxy is not deployed, see [ Deploying an API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/ui-deploy-new) and follow the steps to deploy it manually.
  10. In the left navigation pane, select **Management > Environments > Environment Groups**.
  11. Copy the hostname for your environment group. You'll use this hostname to call the API proxy in the next steps.



##  Call the proxy with internal access 

If you allowed _internal_ access in [ Step 4: Customize access routing](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/configure-routing), follow the instructions in: [ Calling an API proxy with internal-only access](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/accessing-internal-proxies).

##  Call the proxy with external access 

If you allowed _external_ access in [ Step 4: Customize access routing](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/configure-routing), follow these steps: 

  1. Set up a DNS entry for your host. Here are two ways to accomplish this task: 
     * At your registrar, create an A record pointing your environment group hostname to the IP shown on the wizard page under **Configure DNS**. For example, if your hostname is `sales.example.com` and the IP is 10.23.0.2, then point the record for `sales.example.com` to the address `10.23.0.2`.
     * Use Google [Cloud DNS](https://docs.cloud.google.com/dns/docs) to map a URL to an IP address.
  2. Test the API proxy by sending the following request in a terminal window: **Note:** DNS changes are published immediately, but may take time to propagate. Because of this delay, you may have to wait up to an hour before you can call the sample proxy.
         
         curl -v -H "Host:YOUR_ENV_GROUP_HOSTNAME" \
           https://YOUR_INSTANCE_IP_OR_DNS/hello-world

Where:

     * The value of the `Host` header (YOUR_ENV_GROUP_HOSTNAME) is the hostname from the **Environments > Environment Groups** page. 

A successful request returns the string: `Hello, Guest!`. If your request is not successful, see [Troubleshooting](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/troubleshooting-install).




## Next steps

  * [Take a tour](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/tutorials) of the Apigee tutorials, including: 
    * [Guarding against sudden traffic spikes](https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/add-spike-arrest).
    * [Getting a detailed view of the request/response flow](https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/view-with-trace).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
