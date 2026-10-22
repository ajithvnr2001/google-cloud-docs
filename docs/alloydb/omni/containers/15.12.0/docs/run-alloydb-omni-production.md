---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/run-alloydb-omni-production/
title: Run AlloyDB Omni in a production environment \u00a0|\u00a0 AlloyDB Omni for containers: 15.12.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:42:28.991737+00:00
---

# Run AlloyDB Omni in a production environment  |  AlloyDB Omni for containers: 15.12.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/run-alloydb-omni-production/

This page documents AlloyDB Omni version **15.12.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/overview)



Send feedback 

#  Run AlloyDB Omni in a production environment Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.12.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/run-alloydb-omni-production)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/run-alloydb-omni-production)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/run-alloydb-omni-production)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/run-alloydb-omni-production)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/run-alloydb-omni-production)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/run-alloydb-omni-production)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/run-alloydb-omni-production)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/run-alloydb-omni-production)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/run-alloydb-omni-production)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/run-alloydb-omni-production)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/run-alloydb-omni-production)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/run-alloydb-omni-production)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/run-alloydb-omni-production)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/run-alloydb-omni-production)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/run-alloydb-omni-production)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/run-alloydb-omni-production)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/run-alloydb-omni-production)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/run-alloydb-omni-production)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/run-alloydb-omni-production)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/run-alloydb-omni-production)

This page describes how to run AlloyDB Omni in production and how to subscribe to AlloyDB Omni licenses. 

AlloyDB Omni is a downloadable, PostgreSQL-compatible database software that is offered at no charge for evaluation purposes as defined under these [license terms](https://cloud.google.com/terms/alloydb-omni-marketplace-terms).

## Deploy AlloyDB Omni

Deploying AlloyDB Omni in production requires a product license subscription. To deploy AlloyDB Omni, choose one of the following options:

  * Contact your account team.
  * Contact the [Google Cloud sales team](https://cloud.google.com/contact).
  * If you have a Google Cloud account, you can manage AlloyDB Omni subscriptions or explore [deployment options](https://console.cloud.google.com/alloydb/omni).



For general and technical questions about AlloyDB Omni, contact the [AlloyDB Omni product team](https://docs.google.com/forms/d/e/1FAIpQLSfLhBlJbtPJuvXcAS7WSF4J_CcCfO7tSWdCLqztAg1PhLX_vw/viewform).

## Manage AlloyDB Omni subscriptions

Use the **Subscriptions** page in the Google Cloud console to purchase, update, and manage licenses for your AlloyDB Omni instances.

[Go to Subscriptions](https://console.cloud.google.com/alloydb/omni/subscriptions)

### Purchase a new subscription

To run AlloyDB Omni in production, purchase vCPU licenses for all instances, including production instances:

  1. In the Google Cloud console, go to the **Subscriptions** page.

[Go to Subscriptions](https://console.cloud.google.com/alloydb/omni/subscriptions)

  2. In the **Purchase subscription** section, locate the **vCPU Quantity** field.

  3. Enter the total number of vCPUs needed for your production workloads.

  4. Review the **Subscription Summary** to see the unit price (for example, $40.00/vCPU) and the **Estimated monthly cost**.

  5. Click **Purchase**.




### Update a subscription

If your workload requirements change, you can adjust the number of vCPUs in your active subscription:

  1. In the Google Cloud console, go to the **Subscriptions** page.

[Go to Subscriptions](https://console.cloud.google.com/alloydb/omni/subscriptions)

  2. In the **Update subscription** section, enter the new number of vCPUs in the **vCPU Quantity** field.

  3. Review the updated monthly cost in the **Subscription Summary**.

  4. Click **Update and Continue**.

  5. In the confirmation dialog, click **Update**.




### Cancel a subscription

If you no longer require a production license for AlloyDB Omni, you can cancel your subscription:

  1. In the Google Cloud console, go to the **Subscriptions** page.

[Go to Subscriptions](https://console.cloud.google.com/alloydb/omni/subscriptions)

  2. In the active subscription banner, click **Cancel subscription**.

  3. In the confirmation dialog, review the end date of your current billing cycle, and click **Cancel subscription**.




### Subscription pricing and discounts

  * Pricing: Subscriptions are billed monthly based on the total vCPU count.
  * Discounts: Applicable commitment-based discount programs (such as 1-year or 3-year term commitments) are automatically applied to your account.
  * License terms: All production deployments are subject to the [AlloyDB Omni license terms](https://cloud.google.com/terms/alloydb-omni-marketplace-terms).



## What's next

  * Explore available [AlloyDB Omni deployment options in the Google Cloud console](https://console.cloud.google.com/alloydb/omni).


  * Perform a quickstart to [install AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/quickstart).

  * [Perform a single instance installation of AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/deploy-vm) on any Linux VM.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
