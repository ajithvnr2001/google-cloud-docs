---
url: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/configuration/manage-networks/
title: Manage networks \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:24:04.959150+00:00
---

# Manage networks  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/configuration/manage-networks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage networks

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

You can add, modify, and delete networks in the platform using the Classless Inter-Domain Routing (CIDR) format. The system identifies network subnets to help Google Security Operations recognize internal assets and consider network sensitivity during playbook execution. 

## Network management and display

For readability, network names appear in **Cases** and **Reports**.

An entity with a set IP address appears as an **Internal Entity** on the **Cases** page and has the `isInternal:True` field.

## Manage multiple networks

To manage multiple networks, you have two options:

  * Use the **Export** and **Import** functions.
  * Download a template, add your network information to it, and then import it. This is particularly helpful for new customers who want to quickly add existing data to the platform.



## Add a new network

To add a new network, follow these steps:

  1. Go to **Settings > Environments > Networks**.
  2. Click  add  **Add**.
  3. In the **New Network** dialog, add the relevant information. The **Priority** function determines the order of the networks. If an entity matches several ranges, the system selects the one with the highest priority. 
  4. Click **Add**.

**Note:** The system matches an entity to the smallest network that fits, even when users add subnetworks with smaller ranges. 

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
