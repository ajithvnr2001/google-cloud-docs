---
url: https://docs.cloud.google.com/compute/docs/instances/sql-server/configure-availability-groups-shared/prerequisites/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:23.309868+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/sql-server/configure-availability-groups-shared/prerequisites/




Stay organized with collections  Save and categorize content based on your preferences. 

To complete this guide, you need the following:

  * An Active Directory domain with at least one domain controller. You can create an Active Directory domain [by using Managed Microsoft AD](https://docs.cloud.google.com/managed-microsoft-ad/docs/create-domain). Alternatively, you can deploy a [custom Active Directory environment on Compute Engine](https://docs.cloud.google.com/solutions/deploy-fault-tolerant-active-directory-environment) and [set up a private DNS forwarding zone](https://docs.cloud.google.com/compute/docs/instances/windows/best-practices#use_cloud_dns_private_forwarding_zones) that forwards DNS queries to your domain controllers.
  * An Active Directory user that has permission to join computers to the domain and can sign in by using RDP. If you're using Managed Microsoft AD, you can use the `setupadmin` user.
  * A Google Cloud project and VPC with connectivity to your Active Directory domain controllers.
  * A subnet to use for the failover cluster VM instances.



To complete the guide, you also need a Google Cloud project:

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 




When you finish this tutorial, you can avoid continued billing by deleting the resources you created. For more information, see Cleaning up.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
