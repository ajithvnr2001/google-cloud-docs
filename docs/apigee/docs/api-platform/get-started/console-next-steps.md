---
url: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/console-next-steps/
title: Recommended next steps \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:11:31.693412+00:00
---

# Recommended next steps  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/console-next-steps/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Recommended next steps Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/ng-saas/chevrons-1-setup.png)

Congratulations! You have successfully set up an Apigee organization with Pay-as-you-go billing! There are two important tasks to complete as you begin your journey with Apigee: 

  * Test your runtime end to end
  * Add developers and other collaborators



## Test your runtime end to end

From the **Overview** , you can test your Apigee runtime end-to-end by deploying a sample proxy and then sending a test request to the proxy.

### Deploy the sample proxy

Click **Deploy API** on the **Test your Apigee runtime** card to deploy the sample `Hello World` proxy. When deployment completes, the card displays steps for sending a test request.

**Note:** It can take up to a minute for the proxy to deploy.

### Call the proxy with external access

If you selected _external_ access in [Step 4: Configure access routing](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/console-configure-access): 

  1. Send a test request to the proxy using the following command: 
         
         curl -H "Host: EXTERNAL_IP.nip.io" \
           https://EXTERNAL_IP/helloworld

Where EXTERNAL_IP is the external IP address of your runtime instance. For example: 
         
         curl -H "Host: 35.244.227.125.nip.io" \
           https://**35.244.227.125** /helloworld

A successful request returns the string: `Hello, Guest!` If your request is not successful, see [Troubleshooting](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/troubleshooting-install).

  2. Set up and test a DNS entry for your host. Create a DNS entry using either of the following methods: 
     * At your registrar, create an A record pointing your environment group hostname to the IP address of your Apigee instance. For example, if your hostname is `sales.example.com` and the IP is 10.23.0.2, then point the record for `sales.example.com` to the address `10.23.0.2`.
     * Use Google [Cloud DNS](https://docs.cloud.google.com/dns/docs) to map a URL to an IP address.
  3. Once DNS setup is complete, send a test request to the proxy using the following command: 
         
         curl https://EXTERNAL_IP/helloworld

Where EXTERNAL_IP is the external IP address of your runtime instance. For example: 
         
         curl https://**35.244.227.125** /helloworld

A successful request returns the string: `Hello, Guest!` If your request is not successful, see [Troubleshooting](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/troubleshooting-install).




### Call the proxy with internal access

If you selected _internal_ access in [Step 4: Configure access routing](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/console-configure-access), follow the instructions in [Calling an API proxy with internal-only access](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/accessing-internal-proxies) to test your proxy.

## Add developers and other collaborators

You can use Google Cloud Identity and Access Management (IAM) to grant permissions to developers or other collaborators to access and manage your API program. For more information on using IAM to define _who_ has _what access_ to _which resource_ in your Apigee implementation, see the [IAM overview](https://docs.cloud.google.com/iam/docs/overview).

## Next steps

  * [Take a tour](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/tutorials) of the Apigee tutorials, including: 
    * [Guarding against sudden traffic spikes](https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/add-spike-arrest).
    * [Getting a detailed view of the request/response flow](https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/view-with-trace).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
