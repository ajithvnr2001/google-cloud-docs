---
url: https://docs.cloud.google.com/chronicle/docs/secops/content_hub/
title: Content Hub overview \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:07.274690+00:00
---

# Content Hub overview  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/secops/content_hub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

#  Content Hub overview

Supported in:

Google SecOps 

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.**Note:** This feature is for customers using the Google Security Operations unified platform only.**Note:** If you don't see the Content Hub in your platform, make sure you have configured a customer-managed project. For more information, see [Configure feature access](https://docs.cloud.google.com/chronicle/docs/onboard/configure-feature-access). In addition, you need to contact your Google SecOps representative and ask them to enable the Chronicle API feature flag.

## Permissions for Content Hub

For customers who haven't migrated their SOAR instance to Google Cloud, make sure the **Marketplace** and **Response Integrations** permissions are set in the **SOAR Settings > Permissions** page. 

For all other customers, to access modules within Content Hub, you must configure the following permissions in the IAM module. 

IAM permission name | Display name | Role in IAM  
---|---|---  
`chronicle.googleapis.com/featuredContentSearchQueries.get` | Get Search Query Content | `chronicle.reader`  
`chronicle.googleapis.com/featuredContentSearchQueries.list` | List Search Query Contents | `chronicle.reader`  
`chronicle.googleapis.com/featuredContentSearchQueries.install` | Install Search Query Content | `chronicle.writer`  
`chronicle.googleapis.com/featuredContentRules.list` |  List Featured Content Rules | `chronicle.reader`  
`chronicle.googleapis.com/featuredContentNativeDashboards.get ` |  Get Dashboard Content | `chronicle.reader`  
`chronicle.googleapis.com/featuredContentNativeDashboards.list` |  List Dashboard Contents | `chronicle.reader`  
`chronicle.googleapis.com/featuredContentNativeDashboards.install` |  Install Dashboard Content | `chronicle.writer`  
`chronicle.googleapis.com/feedPacks.get ` |  Get feed packs | `chronicle.reader`  
`chronicle.googleapis.com/feedPacks.list ` | List feed packs  | `chronicle.reader`  
`chronicle.googleapis.com/featuredContentPlaybooks.get ` | Get Featured Content Playbook  | `chronicle.reader`  
`chronicle.googleapis.com/featuredContentPlaybooks.list ` | List Featured Content Playbook  | `chronicle.reader`  
`chronicle.googleapis.com/featuredContentPlaybooks.install ` | Install Featured Content Playbook  | `chronicle.writer`  
  
## Overview

The Content Hub serves as a centralized platform for discovering, deploying, and managing content within Google SecOps.

From the Content Hub, you can do the following:

  * Deploy end-to-end content packs (including log ingestion, curated detections and dashboards) to enable your Google SecOps instance to work with products from the top supported list that we have defined.
  * Install third-party integrations for SOAR playbooks and connectors.
  * View and filter curated detections, inspect individual rule attributes and respective rule definitions (curated detections transparency). Navigate to the Rule Set page for full management capabilities. 
  * Add dashboards to enhance your visibility. 
  * Add saved search queries to SIEM search for quick reuse.
  * Install and run Power Ups to extend playbook capabilities.
  * Install and run playbooks to provide SOAR responses.
  * Access legacy SOAR use cases on the **Home** page.



## Content types

There are four types of content in the Content Hub:

  * **Google** : Content that has been developed, maintained and verified by Google SecOps. This category includes both new and updated content items.
  * **Partner** : Content that has been developed and maintained by a Partner. This content is validated through Google's automated quality and validation checks. For partner content, specific support contact details are provided. 
  * **Community** : Content that has been developed and maintained by Community users. This content is validated through Google's automated quality and validation checks.
  * **Custom** : Content that you created and which is only displayed on your own Content Hub. This content is private to your instance and is not verified by Google SecOps.



## What can I do on the Home page?

The **Home** page is the main landing page for the Content Hub. From here, you can access the following:

  * Content Packs, response integrations, dashboards, search queries, Power Ups, and curated detections. 
  * Legacy SOAR use cases. Google recommends using the new Content Packs instead of the legacy use cases because they offer more comprehesive and integrated solutions. 



You can search across all content types—including Content Packs, Detections, Response Integrations, and Dashboards—simultaneously. This capability eliminates the need to navigate through individual tabs to find related assets. The platform displays results with the total number of matches for each type. You can click any of the results to see further details. 

For example, if you search for **Crowdstrike** in the **Search** field, the platform returns the following:

  * Content Packs (1): For example, the Crowdstrike Falcon Comprehensive Pack.
  * Curated Detections (42): The top four cards are displayed, such as "Crowdstrike Falcon: Malware Detected" and "Crowdstrike Falcon: Sensor Tampering". Click **View all 42 results** to go straight to the **Detections** tab.
  * Response Integrations (2): For example, Crowdstrike Falcon (Response) – used for playbook actions like "Isolate Host".
  * Dashboards (3)



## What can I do on the Content Packs page?

On the **Content Packs** page, you can configure single and multiple feeds, and access all other Content Hub options. 

To onboard all data on the **Content Packs** page, follow these steps:

  1. [Configure multiple feeds for product families](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-entities/configure-multiple-feeds) based on the log type you need. 
  2. After you set up the feed, you can optionally configure the remaining components of the Content Pack (automatically downloaded in the background). 
     1. Before you can use any playbook, you must click **Configure Integrations** and set up an instance in order for the playbooks to work. For more information, see [Configure integration instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).
     2. To view or make changes to the downloaded playbook or run it using the simulator, click **View Playbooks**. For more information, see [Working with the playbook simulator](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/working-with-playbook-simulator). You need to copy the playbook name and search for it in the Default folder in the **Playbooks** page.
     3. Click **See all Detection Rules** to open the [**Curated Detections**](https://docs.cloud.google.com/chronicle/docs/detection/curated-detections) page.
     4. Click **See all Search Queries** to open the [**SIEM Search**](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search) page.
     5. Click **See all Dashboards** to open the [**Dashboards**](https://docs.cloud.google.com/chronicle/docs/reports/native-dashboards) page. 



## What can I do on the Curated Detections page?

On the **Curated Detections** page, you can view all supported detection rule definitions in Google SecOps, including rule logic and code.

To view and modify curated detections (rules), do the following:

  1. Find the required rule set you want to update and click **View & Manage**. 
  2. In the side bar that opens on the **Overview** tab, click **Manage Rule**. You'll be directed to the entire rule set on the [**Curated Detections**](https://docs.cloud.google.com/chronicle/docs/detection/curated-detections) page.
  3. Alternatively, in the side bar that opens, click the tab that says **Rule Definition**. This displays the rule logic. You cannot modify the rule from here, but you can create a new rule in the **Rules** page. Click **View Rule Performance** to pivot to the **Detections** page to manage the rule. 

**Note:** In certain situations, you might not be able to view the rule logic. This is by design.

## What can I do on the Response Integrations page?

On the **Response Integrations** page, you can view [integration details](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations), including Release Notes, and configure the individual response integrations. These can be used for SOAR connectors and for playbooks. 

You can also [roll back an integration to a previous version](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/version-rollback) if an update causes issues or if you need to revert custom code changes.

To install and configure an integration:

  1. Find the required integration and click **Install**.
  2. After successful installation, click **Configure** on the same integration to begin the setup. For more information, see [Configure integration instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).



## What can I do on the Dashboards page?

On the **Dashboards** page, you can view details of pre-installed dashboards and add new dashboards. To view or manage any dashboard, pre-installed or added from the Content Hub, go to the [**Dashboards**](https://docs.cloud.google.com/chronicle/docs/reports/native-dashboards) page. Note: Dashboards added through the Content Hub are labeled as **Marketplace**.

## What can I do on the Playbooks and Blocks page?

On the **Playbooks and Blocks** page, you can view and install both playbooks and playbook blocks (nested playbooks). You can display playbooks according to various filters and categories. For example, you can display only playbooks that contain integrations you have installed on your instance already, or you can choose to only display playbooks with specific integrations. 

To view and install a playbook or playbook block:

  1. Find the required playbook or block and click **View Details**.
  2. In the side drawer that opens, look through the information and click **Add**.
  3. Select the environment on which to add the playbook or block to. 
  4. Click the link to be redirected to the Playbook designer page with the playbook you just added on display. You can add the same playbook multiple times. Each playbook will be titled with an ascending number.

**Note:** The Playbooks page doesn't show indications of which playbooks or playbook blocks you have added. 

For more information, see the [**Playbooks**](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/whats-on-the-playbooks-screen) page. 

## What can I do on the Search Queries page?

On the **Search Queries** page, you can view search query details and add new queries. Once you add a search query, it is added to the saved searches and shared within the instance. To view or manage saved queries, go to the [**SIEM Search**](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search) page.

## What can I do on the Power Ups page?

On the **Power Ups** page, you can view details, install, and configure Google SecOps Power Ups for use in playbooks. For setup instructions, see [Use Power Ups](https://docs.cloud.google.com/chronicle/docs/soar/marketplace/using-the-marketplace#power-ups).

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
