---
url: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/change-instance-ips/
title: Changing instance IPs \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:11.500608+00:00
---

# Changing instance IPs  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/change-instance-ips/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Changing instance IPs Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

**Important:** This topic only applies to organizations that were created with VPC peering enabled. See also [Apigee networking options](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/networking-options).

This topic explains how to change the IP of an Apigee instance by manually updating the VMs. 

##  Overview 

When an Apigee instance is [deleted](https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.instances/delete) and then [created](https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.instances/create) again, an IP address is generated for the newly created instance. For example, certain instance parameters, such as cidrRange and networking, are immutable. Therefore, if you want to change these parameters, you must delete the instance and recreate it with the desired configuration. 

In most cases, when you recreate an instance, the same instance IP is selected, but getting the same IP is not guaranteed. The VMs that are routing traffic from the load balancer to Apigee's private IP still have the old IP address; therefore, in cases where a new instance IP is generated, you have to manually update the VMs with the new IP. 

##  Changing the instance IP 

To update the VMs with a new instance IP, follow these steps: 

  1. In the Google Cloud console, go to the **Virtual Machines** > **Instance templates** page.

[Go to Instance templates](https://console.cloud.google.com/compute/instanceTemplates/list)

  2. Click on the Apigee instance template (the template that you want to copy and update). 
  3. Click **Create Similar**.
  4. In the **Name** field, provide a new name for the template. For example, you might add a suffix like "v2" at the end of the original name.
  5. Under **Advanced options** , click the **Management** tab.
  6. Scroll down to the **Metadata (Optional)** section and look for the key value pair containing the **ENDPOINT** key. Change the value of the endpoint to match the new instance IP. Use your IP, not the one shown in the screenshot: 

![alt_text](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/changing-instance-ips-2.png)

  7. Click **Create** to create the template. 
  8. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups/list)

  9. Under the **Name** column of the list, click the name of the Apigee instance group that you wish to modify. 
  10. Click **Edit** to modify this instance group.
  11. Under **Instance template** , select the new instance template (the one you just created).
  12. Click **Save**.
  13. At the top of the page, click **Rolling update**.
  14. Leave all the defaults/presets as-is and click **Update**.

It takes a few minutes for the new VMs to come up, and the old VMs will be shut down and removed. Once the new VMs are up, all API traffic will resume normally. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
