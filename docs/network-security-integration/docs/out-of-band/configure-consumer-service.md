---
url: https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-consumer-service/
title: Set up consumer services \u00a0|\u00a0 Network Security Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:05.246398+00:00
---

# Set up consumer services  |  Network Security Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-consumer-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Security Integration ](https://docs.cloud.google.com/network-security-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/network-security-integration/docs/nsi-overview)



Send feedback 

#  Set up consumer services Stay organized with collections  Save and categorize content based on your preferences. 

To enable consumer services in your network, you must set up the following consumer components:

  * Security profiles and security profile groups
  * Mirroring endpoint groups
  * Mirroring rules
  * Firewall policies



This document provides a high-level workflow that describes how to configure these consumer components.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Make sure that you have the following Identity and Access Management (IAM) roles and permissions: 
     * For security profile groups and security profiles, the [Security Profile Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.securityProfileAdmin) (`roles/networksecurity.securityProfileAdmin`) at the organization level for organization-level security profiles and security profile groups, and at either the project or the organization level for project-level security profiles and security profile groups.
     * For new consumer side networks creation, the [Compute Network Admin role](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin) (`roles/compute.networkAdmin`) on the project you're working with.
     * For mirroring resources, the Mirroring Endpoint Admin role (`roles/networksecurity.mirroringEndpointAdmin`) on your project.
     * Make sure the producer you are connecting to has granted you the Mirroring Deployment User role (`roles/networksecurity.mirroringDeploymentUser`) on the producer's project.
  7. Enable the Compute Engine and Network Security APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,networksecurity.googleapis.com)

  8. Make sure to install the Google Cloud CLI. For the conceptual and installation information about the tool, see [gcloud CLI overview](https://docs.cloud.google.com/sdk/gcloud). 

**Note:** If you haven't run the Google Cloud CLI previously, initialize your gcloud CLI directory by running the [`gcloud init` command](https://docs.cloud.google.com/sdk/gcloud/reference/init). 




## Configure consumer services for the direct mode of mirroring

To configure a consumer service in your network, do the following:

  1. Create a direct-mode [mirroring endpoint group](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-endpoint-groups#direct-mode) that directly corresponds to the producer's mirroring deployment group. For more information, see [Create and manage mirroring endpoint groups](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-endpoint-groups#direct_mode).

  2. Associate the mirroring endpoint group with one or more Virtual Private Cloud (VPC) networks. For more information, see [Create mirroring endpoint group associations](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-mirroring-endpoint-group-associations).

After you configure the endpoint group and the endpoint group association, your network is ready for traffic mirroring. However, mirroring only happens when the mirroring rules match the traffic. Traffic from the associated VPC network in a specific zone is mirrored and routed to the mirroring deployment group in the producer network. If no mirroring deployment exists in a specific zone on the producer side, then the VPC network traffic in that mirroring deployment zone is not mirrored on the consumer side.

  3. Create one or more custom [security profiles](https://docs.cloud.google.com/network-security-integration/docs/security-profiles-overview) of type `custom mirroring`. You add the mirroring endpoint group created in the previous step to this security profile. For more information about how to create a custom security profile, see [Create a custom security profile](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-custom-security-profiles#direct-mode).

  4. Create a [custom security profile group](https://docs.cloud.google.com/network-security-integration/docs/security-profile-groups-overview) with the security profile created in the previous step. For more information, see [Create and manage security profile groups](https://docs.cloud.google.com/network-security-integration/docs/configure-security-profile-groups).

  5. Create a network firewall policy and mirroring rules to select the traffic that needs to be mirrored for network traffic inspection by the producer service. These mirroring rules refer to the security profile group that you created in the previous step. For more information, see [Create and manage mirroring rules](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/create-manage-mirroring-rules).

  6. Associate the network firewall policy with your VPC network. For more information, see [Associate a policy with the network](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies#associate).




## Configure consumer services for the broker mode of mirroring

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To configure a consumer service in your network, do the following:

  1. Create a broker-mode [mirroring endpoint group](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-endpoint-groups#broker-mode) and define the connected producer mirroring deployment groups that are allowed to receive traffic from the consumer. For more information, see [Create and manage mirroring endpoint groups](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-endpoint-groups#broker-mode).

  2. Create a mirroring endpoint in the zones that are covered by the mirroring policy. When you create the mirroring endpoint, you associate it with the mirroring endpoint group that you created in the previous step. For more information, see [Create and manage mirroring endpoints](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-mirroring-endpoints).

  3. Associate the mirroring endpoint group with one or more Virtual Private Cloud (VPC) networks. You don't need to associate each zone separately. For more information, see [Create mirroring endpoint group associations](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-mirroring-endpoint-group-associations).

After you configure the endpoint group and the endpoint group association, your network is ready for traffic mirroring in zones where you have a mirroring endpoint and mirroring deployment present. For more information about how traffic mirroring works in broker mode, see [Broker mode of mirroring](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/out-of-band-integration-overview#broker-mode-of-mirroring).

  4. Create one or more custom [security profiles](https://docs.cloud.google.com/network-security-integration/docs/security-profiles-overview) of type `custom mirroring`. You add the mirroring endpoint group created in step 1 to this security profile and specify a subset of mirroring deployment groups connected to the broker. For more information about how to create a custom security profile, see [Create a custom security profile](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-custom-security-profiles#broker-mode).

  5. Create a [custom security profile group](https://docs.cloud.google.com/network-security-integration/docs/security-profile-groups-overview) with the security profile created in the previous step. For more information, see [Create and manage security profile groups](https://docs.cloud.google.com/network-security-integration/docs/configure-security-profile-groups).

  6. Create a network firewall policy and mirroring rules to select the traffic that needs to be mirrored for network traffic inspection by the producer service. These mirroring rules refer to the security profile group that you created in the previous step. For more information, see [Create and manage mirroring rules](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/create-manage-mirroring-rules).

  7. Associate the network firewall policy with your VPC network. For more information, see [Associate a policy with the network](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies#associate).




## What's next

  * [Monitor out-of-band integration](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/monitor-out-of-band-integration)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
