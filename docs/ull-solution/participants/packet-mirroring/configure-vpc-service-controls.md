---
url: https://docs.cloud.google.com/ull-solution/participants/packet-mirroring/configure-vpc-service-controls/
title: Configure VPC Service Controls for ULL Packet Mirroring \u00a0|\u00a0 Ultra Low Latency Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:49.650706+00:00
---

# Configure VPC Service Controls for ULL Packet Mirroring  |  Ultra Low Latency Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ull-solution/participants/packet-mirroring/configure-vpc-service-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ ULL Solution ](https://docs.cloud.google.com/ull-solution)
  * [ Exchange participants ](https://docs.cloud.google.com/ull-solution/participants)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure VPC Service Controls for ULL Packet Mirroring

**Preview — ULL Packet Mirroring for exchange participants**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

VPC Service Controls provides security for Ultra Low Latency (ULL) Packet Mirroring to help reduce the risk of data theft when traffic or data moves between different network environments or organizations. You can use VPC Service Controls to place projects containing ULL Packet Mirroring resources inside service perimeters.

This page describes how to configure VPC Service Controls for ULL Packet Mirroring collector resources (`UllMirroringCollector`).

For more information, see [Components of ULL Packet Mirroring](https://docs.cloud.google.com/ull-solution/participants/packet-mirroring/packet-mirroring-ull#packet-mirroring-comp).

Before you begin, review the [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

## Before you begin

  1. Verify that you have the required Identity and Access Management (IAM) roles to administer VPC Service Controls. For more information, see [IAM roles for administering VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/access-control).

  2. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  3. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. Enable the Network Security API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=networksecurity)

  6. Verify that you have the required IAM roles to manage ULL Packet Mirroring resources. For more information, see [Set up Packet Mirroring for ULL VPC networks](https://docs.cloud.google.com/ull-solution/participants/packet-mirroring/set-up-packet-mirroring-ull#roles).



## Overview of perimeter rules for ULL Packet Mirroring

Perimeter rules for ULL Packet Mirroring act as security guardrails to control communication between isolated Virtual Private Cloud (VPC) environments while allowing specific, necessary traffic. Depending on your deployment topology, you might need to configure VPC Service Controls egress rules to allow communication between your collector project and the exchange operator's engine project when managing ULL mirroring collectors (`UllMirroringCollector`).

To protect ULL Packet Mirroring resources, add the Network Security API (`networksecurity.googleapis.com`) to the list of restricted services within your collector service perimeter.

The following table summarizes the required VPC Service Controls configuration for each deployment scenario:

Scenario | Topology | Required VPC Service Controls configuration  
---|---|---  
Create collector in a different project (same service perimeter) | Different project, same perimeter | No additional rules are required because both projects belong to the same service perimeter.  
Create collector in a different project (separate service perimeter) | Different project, separate perimeters | Add bidirectional egress rules between the engine project and the collector project for `networksecurity.googleapis.com`.  
  
## Add APIs to the service perimeter

To protect ULL Packet Mirroring resources within a service perimeter, add the Network Security API to the list of restricted services.

###  Google Cloud console 

  1. In the Google Cloud console, go to the **VPC Service Controls** page.

[Go to VPC Service Controls](https://console.cloud.google.com/security/service-perimeter)

  2. In the table, click the name of the service perimeter that you want to modify.

  3. Click **Edit**.

  4. On the **Edit service perimeter** page, click **Restricted services** and then **Add services**.

  5. Select **Network security API** (`networksecurity.googleapis.com`).

  6. Click **Add selected services** and then click **Save**.




###  gcloud 

To add restricted services to an existing service perimeter, use the [`gcloud access-context-manager perimeters update` command](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/update):
    
    
    gcloud access-context-manager perimeters update PERIMETER_NAME \
        --policy=POLICY_ID \
        --add-restricted-services=networksecurity.googleapis.com
    

Replace the following:

  * `PERIMETER_NAME`: the name of the service perimeter.
  * `POLICY_ID`: the ID of your organization's access policy.



## Configure egress rules for cross-perimeter collectors

Configure a collector-to-engine egress rule on your service perimeter to allow the `UllMirroringCollector` resource to connect to the `UllMirroringEngine` in the exchange operator's engine project.

### Configure egress from collector perimeter to engine project

Add the following egress policy to the collector service perimeter:
    
    
    egressPolicies:
    - egressFrom:
        identityType: ANY_IDENTITY
      egressTo:
        operations:
        - serviceName: networksecurity.googleapis.com
          methodSelectors:
          - method: '*'
        resources:
        - projects/ENGINE_PROJECT_NUMBER
      title: Allow egress from collector project to engine project
    

Replace `ENGINE_PROJECT_NUMBER` with the project number of the project that hosts the `UllMirroringEngine`.

## Create and manage access levels

To permit external access to protected resources inside a perimeter, you can use access levels. Access levels apply only to requests for protected resources coming from outside the service perimeter.

For more information, see [Allowing access to protected resources from outside a perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/use-access-levels).

## What's next

  * [Set up Packet Mirroring for ULL VPC networks](https://docs.cloud.google.com/ull-solution/participants/packet-mirroring/set-up-packet-mirroring-ull)
  * [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
