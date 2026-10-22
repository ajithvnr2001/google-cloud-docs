---
url: https://docs.cloud.google.com/identity-platform/docs/multi-tenancy-billing/
title: Monitoring billing for tenants \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:28.844808+00:00
---

# Monitoring billing for tenants  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/multi-tenancy-billing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Guides ](https://docs.cloud.google.com/identity-platform/docs/how-to)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Monitoring billing for tenants

All tenants are billed as part of their Identity Platform project. This document explains how to export billing data and monitor the cost of individual tenants.

## Before you begin

To export tenant billing data, you'll need to be granted the IAM Owner role (`roles/owner`) on the following:

  * An Identity Platform project with multi-tenancy enabled.
  * The billing account linked to your project.



## Enabling billing export to BigQuery

To make billing data available in BigQuery, follow the steps in [Export billing data to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery).

**Note:** Data is not backfilled for the timeframe before exporting is enabled, so you should configure exporting before opening your project to customer traffic to ensure you have an accurate dataset.

You only need to complete the step once per project.

## Querying billing data

  1. Open the BigQuery page in the Google Cloud console.  
[Go to the BigQuery page](https://console.cloud.google.com/bigquery)

  2. Select the table containing your project's billing information.

  3. Click **Compose Query** to open the query editor.

  4. Enter a query.

To list the total cost for each tenant, use the following, replacing `dataset-name.table-name` with the name of the billing dataset and table you exported in step 1:
         
         SELECT labels.value as Tenant, SUM(cost) as TenantCost
         FROM [dataset-name.table-name]
         WHERE labels.key = "goog-identitytoolkit-tenant"
         GROUP BY 1
         

All monthly active user reports have a start time at the beginning of the month. You can use `WHERE usage_start_time` and the first day of the month (expressed in Pacific Time) to filter on a monthly basis. For example, to list the cost of each tenant for August 2019:
         
         SELECT labels.value as Tenant, SUM(cost) as TenantCost
         FROM [dataset-name.table-name]
         WHERE labels.key = "goog-identitytoolkit-tenant"
         AND usage_start_time = "2019-08-01 00:00:00 -07:00"
         GROUP BY 1
         

You can also get the costs for one specific tenant. Replace `tenant-id` with the ID of your tenant in the following example:
         
         SELECT labels.value as Tenant, SUM(cost) as TenantCost
         FROM [dataset-name.table-name]
         WHERE labels.key = "goog-identitytoolkit-tenant"
         AND labels.value = "tenant-id"
         GROUP BY 1
         

  5. Click **Run query** to execute it.




You should see a billing breakdown specific to one particular tenant.

## Pricing tiers

The identity provider (IdP) that authenticates the user determines the Identity Platform pricing tier, not the protocol that your application uses to communicate with Identity Platform.

For example, if your application integrates using OIDC or SAML, but the user authenticates with an email address and password or a social provider (such as Google or Facebook), this activity is billed under **Tier 1**. **Tier 2** pricing applies when Identity Platform delegates authentication to an external identity provider (such as Okta or Microsoft Entra ID) using SAML or OIDC federation.

For more information and detailed rate tiers, see the [Identity Platform pricing page](https://docs.cloud.google.com/identity-platform/pricing).

## What's next

  * [Learn more about billing on Google Cloud](https://docs.cloud.google.com/billing/docs/concepts).
  * [Pricing information for Identity Platform](https://docs.cloud.google.com/identity-platform/pricing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
