---
url: https://docs.cloud.google.com/composer/docs/composer-3/perform-failover-tests/
title: Perform failover tests for highly resilient environments \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:27:25.574781+00:00
---

# Perform failover tests for highly resilient environments  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-3/perform-failover-tests/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  Perform failover tests for highly resilient environments Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/perform-failover-tests "View this page for Managed Airflow \(Gen 2\)") | Managed Airflow (Legacy Gen 1)

This page describes how to perform a database failover test for [highly resilient (Highly Available) environments](https://docs.cloud.google.com/composer/docs/composer-3/set-up-highly-resilient-environments).

Failover tests for your environment simulate a complete outage of a zone in a data center. In such a scenario, a zonal outage of a database might happen. By performing a failover test, you can monitor how your highly resilient environment performs a failover and check how this affects your DAGs and tasks.

## Before you begin

  * To perform failover tests, your Google Account must have the following roles and permissions:

    * `composer.environments.update` permission. See [Access control with IAM](https://docs.cloud.google.com/composer/docs/composer-3/access-control#user-account) for a list of roles with this permission.

  * In Managed Airflow (Gen 3), the environment's cluster is located in the tenant project of your environment and it's not possible to simulate a zonal outage for it.




## Check that your environment is healthy

Make sure to perform failover tests only on healthy environments. To check that your environment is healthy:

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **Monitoring** tab.

  4. Make sure that all health metrics are green.




## Perform a database failover test

You can perform a database failover test, which simulates a zonal outage, by triggering it with a Google Cloud CLI command. For example, you might want to do it to measure the amount of time it takes for your environment's database to switch to another zone.

**Note:** The database failover test is not intended for troubleshooting; it is not possible to fix issues with the database component of an environment with the failover test.

To perform a database failover test for your environment:

  1. Make sure that your environment is healthy.

  2. Get the primary zone of your environment's database:
         
         gcloud composer environments fetch-database-properties \
             ENVIRONMENT_NAME \
             --location LOCATION
         

Replace the following:

     * `ENVIRONMENT_NAME`: the name of your Cloud Composer environment.
     * `LOCATION`: the region where the environment is located.

Example:
    
    gcloud composer environments fetch-database-properties \
        example-environment \
        --location us-central1
    

  3. Start the database failover test:
         
         gcloud composer environments database-failover \
             ENVIRONMENT_NAME \
             --location LOCATION
         

Replace the following:

     * `ENVIRONMENT_NAME`: the name of your Cloud Composer environment.
     * `LOCATION`: the region where the environment is located.

Example:
    
    gcloud composer environments database-failover \
        example-environment \
        --location us-central1
    

  4. Wait until the database failover test is finished. The process can take up to 3 minutes.

  5. Check that the primary zone of your environment's database is changed:
         
         gcloud composer environments fetch-database-properties \
             ENVIRONMENT_NAME \
             --location LOCATION
         

  6. Check your environment's health metrics to make sure that your environment is healthy.

  7. Your environment's database becomes ready for another failover when the **Database available for failover** (`composer.googleapis.com/environment/database/available_for_failover`) environment metric becomes `True`. For more information about viewing your environment's metrics in Cloud Monitoring, see [Monitor environments](https://docs.cloud.google.com/composer/docs/composer-3/monitor-environments#view-metrics).




## What's next

  * [Create environments](https://docs.cloud.google.com/composer/docs/composer-3/create-environments)
  * [Monitor environments](https://docs.cloud.google.com/composer/docs/composer-3/monitor-environments)
  * [Disaster recovery with environment snapshots](https://docs.cloud.google.com/composer/docs/composer-3/disaster-recovery-with-snapshots)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
