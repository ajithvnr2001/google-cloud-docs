---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/billing/view-tag-level-costs/
title: View tag-level billing costs \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:43:42.786879+00:00
---

# View tag-level billing costs  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/billing/view-tag-level-costs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  View tag-level billing costs Stay organized with collections  Save and categorize content based on your preferences. 

**Preview:** This is a Preview feature that is available as-is and is not recommended for production environments. Google provides no Service-Level agreements (SLA) or technical support commitments for Preview features. For more information, see [feature stages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/feature-stages).

This document provides instructions for viewing cost for user defined tags in GDC. This allows user to track billing of all the projects under the same tag and total cost for each tag per SKU.

## Before you begin

To get the permissions that you need to view tag-level costs, you must ask your Organization IAM Admin to grant you the Organization Grafana Viewer (`organization-grafana-viewer`) role.

## Access Tag costs

To access costs at tag level, do the following:

  1. Open the following URL to access the Grafana home page:
         
         https://GDC_URL/platform-obs/grafana/
         

Replace `GDC_URL` with the URL of your Distributed Cloud organization.

  2. In the navigation menu, click **Explore** and select **Billing** from drop-down.

  3. Open the code view and query the public.costs table to fetch costs per tag.

  4. These are sample SQL queries to fetch total cost data at tags level-

To get total cost across all SKUs at tag level -:
         
         SELECT user_tags, sum(cost) FROM public.costs, UNNEST(tags) AS user_tags 
         where start_time > '2026-01-01 10:00:00' GROUP BY unnested_tags;
         

To get total cost for a specific SKU at tag level-:
         
         SELECT user_tags, sum(cost) FROM public.costs, UNNEST(tags) AS user_tags 
         where start_time > '2026-01-01 10:00:00' and sku = 'sku_id' GROUP BY unnested_tags;
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
