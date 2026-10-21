---
url: https://docs.cloud.google.com/chronicle/docs/detection/watchlist-getting-started/
title: Manage entity watchlists \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:38:05.624191+00:00
---

# Manage entity watchlists  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/watchlist-getting-started/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage entity watchlists

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

Learn how to use the **Watchlist** section. Watchlists in Google SecOps lets you manually curate entity lists to monitor, boost, or suppress their risk scores in the system. Security analysts can prioritize investigations and focus on entities that might be particularly important, even if their automated risk scores are low.

**Note:** Because these risk considerations aren't reflected in the risk score calculation, entities on watchlists usually don't appear in the [Risk Analytics dashboard](https://docs.cloud.google.com/chronicle/docs/detection/risk-analytics-dashboard).

## Before you begin

To access the Watchlist tab, follow these steps:

  1. In the left navigation menu, click **Detection**.
  2. From **Detection** , click **Risk analytics**.
  3. Click the **Watchlists** tab.



## Watchlists

Watchlists in Google Security Operations allow users to manually curate lists of entities to monitor, boosting or suppressing their risk scores in the system. This enables security analysts to prioritize investigations and focus on entities that may be of particular concern, even if their automated risk scores are low.

## Enhance risk scores with human insights

While Google SecOps' automated risk scoring provides valuable insights, watchlists incorporate human expertise and context into the risk assessment process. For example, a security analyst might have knowledge of high-value assets, sensitive data locations, or specific users who warrant closer monitoring. By adding these entities to a watchlist, analysts can ensure they receive appropriate attention, regardless of their computed risk scores.

The **Watchlists** page lets you monitor specific entities from across your enterprise according to preferences of your enterprise, regardless of the entity's risk score. For example: 

  * Create a watchlist of employees about to leave the company to monitor any possible data exfiltration
  * Create a watchlist of the C-suite to monitor closely any subtle changes in their security posture.



## Create a watchlist

To create a watchlist to your Google SecOps account, complete the following steps. You can configure up to 200 watchlists.

  1. Click **Create watchlist**.
  2. Specify a **Watchlist name**.
  3. (Optional) Specify a **Description**.
  4. (Optional) Specify **Multiplying factor** of between 0-100. The default is **1**.
  5. (Optional) Specify entities on the right side of the window following the [Add entities into a watchlist](https://docs.cloud.google.com/chronicle/docs/detection/risk-analytics-dashboard#add-entities-into-a-watchlist) section. You can add the following entity types here:

     * `ASSET_IP_ADDRESS`
     * `EMAIL`
     * `EMPLOYEE_ID`
     * `HOSTNAME`
     * `MAC`
     * `PRODUCT_OBJECT_ID`
     * `PRODUCT_SPECIFIC_ID`
     * `USERNAME`
     * `WINDOWS_SID`
  6. Click **Create watchlist**.




A watchlist lets you globally apply a risk score modifier to a set of entities. This modifier, called **Multiplying factor** , refines the risk scores for all entities in the watchlist. Each entity's base risk score is multiplied by the same factor. Enter a multiplying factor with a value from 0 -100. The default value is 1.

In addition to creating a watchlist, you can edit a watchlist, pin/unpin, delete and add entities to/ remove entities from it. For more on how to create watchlists, see [Add a watchlist](https://docs.cloud.google.com/chronicle/docs/detection/risk-analytics-dashboard#add_a_watchlist).

## Use cases

Here are a few use cases for the Watchlist section.

### Use case 1:

Create a watchlist to track activities of employees about to leave your company. These employees may attempt to copy internal specifications, plans, or presentations, particularly in highly competitive industries. For most employees, this type of information would be of little value, since that type of behavior would typically be considered to be normal.

### Use case 2: Unusual activity among senior leaders

Create a watchlist to track unusual activity among senior leaders within your organization. Leadership is frequently targeted by spear phishing attacks. Sudden increases in invoices or requests for funds transfers to outside accounts can be monitored using a watchlist, in particular when known phishing attacks have been identified within your enterprise. 

### Use case 3: internal red team

Create a watchlist for an internal red team that is active in your enterprise. The red team could trigger numerous alerts within your security infrastructure (as expected). You can specify the watchlist with a multiplying factor of 0 to reduce their visibility while they are in an active exercise. For more information, see [Add a watchlist](https://docs.cloud.google.com/docs/detection/risk-analytics-dashboard#add_a_watchlist). 

# What's next

  * [Add a watchlist](https://docs.cloud.google.com/chronicle/docs/detection/risk-analytics-dashboard#add_a_watchlist)
  * [Edit a watchlist](https://docs.cloud.google.com/chronicle/docs/detection/risk-analytics-dashboard#edit_a_watchlist)
  * [Pin a watchlist](https://docs.cloud.google.com/chronicle/docs/detection/risk-analytics-dashboard#pin_a_watchlist)
  * [Unpin a watchlist](https://docs.cloud.google.com/chronicle/docs/detection/risk-analytics-dashboard#unpin_a_watchlist)
  * [Delete a watchlist](https://docs.cloud.google.com/chronicle/docs/detection/risk-analytics-dashboard#delete_a_watchlist)
  * [Add entities to a watchlist](https://docs.cloud.google.com/chronicle/docs/detection/risk-analytics-dashboard#add-entities-into-a-watchlist)



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
