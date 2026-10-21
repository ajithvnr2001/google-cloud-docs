---
url: https://docs.cloud.google.com/composer/docs/composer-1/environment-scaling/
title: About environment scaling \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:27:39.172435+00:00
---

# About environment scaling  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-1/environment-scaling/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 1 Guides ](https://docs.cloud.google.com/composer/docs/composer-1/composer-overview)



Send feedback 

#  About environment scaling Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/environment-scaling "View this page for Managed Airflow \(Gen 3\)") | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/environment-scaling "View this page for Managed Airflow \(Gen 2\)") | **Managed Airflow (Legacy Gen 1)**

This page describes how environment scaling works.

Other pages about scaling:

  * For information about scaling your environments, see [Scale environments](https://docs.cloud.google.com/composer/docs/composer-1/scale-environments).



## Resizable environments

Managed Airflow (Legacy Gen 1) has environments that run a constant number of workers.

When you create an environment, you specify the number of nodes. This number corresponds to the number of workers in your environment. Managed Airflow distributes load between all workers in your environment. In addition to running Airflow workers, your environment nodes also run schedulers and other environment components.

You can scale your environment by changing the number of nodes in your environment.

## Scale and performance parameters

You can control the scale and performance parameters of your environment by adjusting the machine types used by the Airflow database and web server components of your environment. By doing so you can scale your environment vertically, in addition to the horizontal scaling provided by the number of nodes setting. You can adjust machine types of the Airflow database and web server at any time.

You set the machine type for environment nodes when you create an environment. You cannot change this parameter later. It means that you cannot scale Airflow workers vertically in Managed Airflow (Legacy Gen 1).

## Multiple schedulers

If your environment uses Airflow 2, You can specify a number of schedulers up to the number of nodes in your environment.

For more information about configuring the number of schedulers for your environment, see [Scale environments](https://docs.cloud.google.com/composer/docs/composer-1/scale-environments#scheduler-parameters).

## Database disk space

Disk space for the Airflow database automatically increases to accommodate the demand.

## What's next

  * [Scale environments](https://docs.cloud.google.com/composer/docs/composer-1/scale-environments)
  * [Managed Airflow pricing](https://docs.cloud.google.com/composer/pricing)
  * [Create environments](https://docs.cloud.google.com/composer/docs/composer-1/create-environments)
  * [Environment architecture](https://docs.cloud.google.com/composer/docs/composer-1/environment-architecture)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
