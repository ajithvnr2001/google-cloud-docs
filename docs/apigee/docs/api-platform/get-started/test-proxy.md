---
url: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/test-proxy/
title: Step 3: Call an API proxy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:48:36.841791+00:00
---

# Step 3: Call an API proxy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/test-proxy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Step 3: Call an API proxy Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

In this step, you will test the API proxy you just created and deployed.

  1. In the Google Cloud console, go to the **Apigee > Management > Environments** page. 

[Go to Environments](https://console.cloud.google.com//apigee/environments)

  2. Make sure the same Google Cloud project where you created the API proxy is selected from the dropdown at the top of the page.
  3. Select the **Environment Groups** tab.
  4. In the table, find the row for the environment group that contains the environment where **myproxy** is deployed. The hostname appears in the **Host Names** column of this row. For example: `mydomain.com`.
  5. Call the API proxy. The way you call the proxy depends on whether your Apigee instance is configured for external or internal network access. If you aren't sure how your Apigee instance is configured, contact your Apigee administrator. 
     * **External access** : If your Apigee instance is configured for external access, call the proxy as follows: 
           
           curl https://YOUR_ENV_GROUP_HOSTNAME/myproxy

Where `YOUR_ENV_GROUP_HOSTNAME` is the hostname you obtained in the previous step.

For example:
           
           curl https://mydomain.com/myproxy

Here's another example, where the wildcard DNS service `nip.io` is used for the host:
           
           curl https://198.51.100.251.nip.io/myproxy

     * **Internal access** : If your Apigee instance is configured for internal network access, some extra steps are needed to obtain access to the internal load balancer and its IP address. For details, see [Calling a proxy with internal-only access](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/accessing-internal-proxies).
  6. A successful call to the proxy returns the following output: 
         
         Hello, Guest!




If you get an error, check the following: 

  * If you see a timeout error (unusual), try [ undeploying and redeploying](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/ui-deploy-new) the new API proxy.
  * If the host cannot be resolved, for example you receive a 404 error, double check that you are using the correct hostname and proxy name.
  * Make sure the environment group hostname is configured with the Cloud Load Balancer. See [ Determining whether the Cloud Load Balancer is configured for a hostname](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environmentgroups-working-with#determining-whether-the-cloud-load-balancer-is-configured-for-a-hostname).
  * If you see a TLS/SSL error, such as an SSL handshake error, contact your DNS provider to make sure the DNS A record for the hostname is configured properly. Make sure the record has the IP of the load balancer that was created during Apigee provisioning. If you're not sure what the IP should be, see [ Determining whether the Cloud Load Balancer is configured for a hostname](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environmentgroups-working-with#determining-whether-the-cloud-load-balancer-is-configured-for-a-hostname).
  * If you see a TLS/SSL certificate error, the SSL certificate associated with the load balancer might not have the correct hostname, and therefore is being rejected. The certificate was created during the provisioning process. The troubleshooting steps in [ Determining whether the Cloud Load Balancer is configured for a hostname](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environmentgroups-working-with#determining-whether-the-cloud-load-balancer-is-configured-for-a-hostname) show you how to locate and inspect the certificate.
  * If you're unable to resolve the problem, contact the person who provisioned Apigee for further assistance.



In the next step, you will change the target endpoint of the API proxy. 

[1](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/create-proxy) [2](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/deploy-proxy) [3](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/test-proxy) [(NEXT) Step 4: Change the target endpoint](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/change-endpoint) [5](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/add-policy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
