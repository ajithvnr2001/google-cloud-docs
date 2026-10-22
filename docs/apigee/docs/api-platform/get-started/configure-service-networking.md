---
url: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/configure-service-networking/
title: Step 2: Set up networking \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:48:50.770223+00:00
---

# Step 2: Set up networking  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/configure-service-networking/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Step 2: Set up networking Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/ng-saas/chevrons-1-setup.png)

## What you're doing in this step

In this step, you configure Service Networking, which automates the private connectivity setup (using VPC Network Peering) between your network, Apigee, and Google Cloud services. For more information on VPC peering with Apigee, see [ Understanding peering ranges](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/peering-ranges).

## Perform the step

#### Permissions required for this task

You can give the Apigee provisioner a predefined role that includes the permissions needed to complete this task, or give more fine-grained permissions to provide the least privilege necessary. See [Predefined roles](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#predefined-roles) and [Service networking permissions](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#service-networking-permissions).

In Step 2, the console displays a list of networking configuration options and their pre-selected default values. To view or edit any of the configuration choices, click create **Edit** to open the **Set up networking** panel. 

You can accept the default configuration or select the following options: 

  1. In the **Authorized network** drop-down, select one of the following to use for peering connections with your Apigee instance: 
     * The [default](https://docs.cloud.google.com/vpc/docs/vpc#default-network) VPC network created for all Google Cloud projects. **Note:** Google recommends that you not use "default" in a production environment. Instead, we recommend that you create a custom VPC for your Apigee account and connect to that. For information about Apigee's peering network requirements, see [ Network sizing](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/peering-ranges#sizing). 
     * An existing VPC network in your Google Cloud project. 

The drop-down list includes all VPC networks in your Google Cloud project, even custom ones without peering connections. If you select a network that does not have a connection set up yet, you'll be prompted to allocate a peering range.

**Note:** If your project uses Shared Virtual Private Cloud (VPC) networking, you can select the shared network that will be used to peer with Apigee. If you do not see the network in the drop-down list, be sure you have the required permissions. See Permissions required for this task. 
  2. If prompted, choose one of these options in the **Allocated peering ranges** section: 
     * **Automatically allocate IP range:** Choose this option if you want Google Cloud to manage the IP range for you. Two ranges are allocated, one of length /22 and one of length /28. The ranges are named as follows: `google-managed-services-NETWORK_NAME-PREFIX_LENGTH`. For more information and important considerations, see [ Understanding peering ranges](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/peering-ranges). **Note:** We do not recommend this option if you are using dynamic routes (such as Cloud Router) or a network from a host project.
     * **Select one or more existing IP ranges or create a new one:** Choose this option if you want to select the IP range yourself. 
       * From the **Select or create an IP range** drop-down menu, select a /21 CIDR range.
       * If no IP ranges are available, click **Allocate a new IP range**. 
         * Enter the **IP range name** in the available field.
         * Enter the **allocated IP address range** in the available field. The range must be able to hold a /21 CIDR length.
**Note:** If you want to select or allocate an IP range smaller than a /21 CIDR range, you can use the command-line interface, as explained in [ Step 4: Configure service networking](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#service-networking).
  3. In the **Select runtime IP range** section, choose one of these options: 
     * **Automatic (Recommended):** Apigee automatically selects an available CIDR range with a prefix size of /22. No further action on your part is required.
     * **Custom:** Select this option if you want to specify which IP ranges Apigee should use. 

Enter the custom IP ranges, one with a prefix size of /22, and one with a prefix size of /28. The ranges must be available as part of a private connection between your project and Apigee.

  4. Click **Allocate and connect**. 

Apigee configures the connection between the VPC and Google's services to use IP addresses within the allowed ranges. This operation may take a few minutes to complete.

  5. Once the service networking options are configured as desired, click **Next**. **Caution:** When you submit the completed configuration for provisioning Apigee (at the end of **Step 4**), you cannot go back and change the network service configuration. Apigee does not support updating or changing the network configuration once provisioning is complete.



Go to the next step, [Step 4: Configure hosting and encryption](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/console-configure-hosting).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
