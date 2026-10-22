---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/data-exfiltration/
title: Control data exfiltration \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:57:57.432887+00:00
---

# Control data exfiltration  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/data-exfiltration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Control data exfiltration Stay organized with collections  Save and categorize content based on your preferences. 

## Before you begin

To control data exfiltration, you must have the necessary identity and access roles:

  * Project Editor: has access to manage and delete projects. Ask your Organization IAM Admin to grant you the Project Editor (`project-editor`) role.



## Prevent data exfiltration

You can prevent data exfiltration from a GDC project by enabling data exfiltration protection when you create the project.

To enable data exfiltration protection, follow these steps when creating a project:

  1. Within the GDC console, navigate to **Projects**.
  2. Click the add **Add Project** button to create a project.
  3. Complete the required information for your project on the **Project name** page.
  4. On the **Network** page, ensure the **Enable data exfiltration protection** checkbox is checked.
  5. Click **Next**.
  6. Review the details on the **Review** page.
  7. Click **Create**.



## Disable data exfiltration protection

By default, a project has data exfiltration protection enabled. The following are the default policies for a project with data exfiltration protection enabled:

  * Allow inbound traffic only from the same project. All other traffic is denied.
  * Allow outbound traffic to all destinations within the same organization. All other traffic is denied, which means that external traffic outside your organization is denied.



With data exfiltration protection enabled, you cannot create `ProjectNetworkPolicy` resources for outbound traffic.

If you disable data exfiltration protection by clearing the corresponding checkbox in the GDC console for a project, the default policies for the project are the following:

  * Allow inbound traffic only from the same project. All other traffic is denied.
  * Allow outbound traffic to all destinations, including external projects from other organizations.



Work through the following steps to disable data exfiltration protection for a project:

  1. In the GDC console, go to **Projects** in the navigation menu.
  2. Click the name of the project where you want to disable data exfiltration protection.
  3. Click edit **Edit** on the **Data exfiltration protection** field.
  4. On the **Edit data exfiltration protection** page, clear the **Enable data exfiltration protection** checkbox.
  5. Click **Save**. The **Data exfiltration protection** field changes its value to **Disabled**.



You must create `ProjectNetworkPolicy` egress policies for your projects to restrict the outbound traffic. For more information, see [Configure project network policies](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/pnp/pnp-overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
