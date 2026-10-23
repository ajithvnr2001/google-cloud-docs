---
url: https://docs.cloud.google.com/memorystore/docs/memcached/upgrade-memcached-version/
title: Upgrade the Memcached version of an instance \u00a0|\u00a0 Memorystore for Memcached \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:16.421880+00:00
---

# Upgrade the Memcached version of an instance  |  Memorystore for Memcached  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/memcached/upgrade-memcached-version/

Memorystore for Memcached is being deprecated and will be shut down on January 31, 2029. After February 1, 2027, you can't create Memorystore for Memcached instances in new projects unless these instances already exist in these projects. We recommend that you migrate your workloads to [Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey), which offers superior performance and features.

[Learn more about the deprecation](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation) | [Read the migration guide](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation/migrate-to-valkey)

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Memcached ](https://docs.cloud.google.com/memorystore/docs/memcached)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/memcached/memcached-overview)



Send feedback 

#  Upgrade the Memcached version of an instance Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to upgrade the Memcached version of a Memorystore for Memcached instance. For a list of available versions, see [Supported versions](https://docs.cloud.google.com/memorystore/docs/memcached/supported-versions). For more information about instance behavior during an upgrade operation, see [About upgrading the Memcached version of an instance](https://docs.cloud.google.com/memorystore/docs/memcached/about-upgrading-version).

**Note:**

  * Upgrading an instance is irreversible. You cannot downgrade the Memcached version of a Memorystore for Memcached instance.
  * Upgrading the Memcached instance causes a full cache flush on the instance.
  * Version upgrade is only available by using the gcloud CLI.



## Upgrading the instance version

### Console

  1. Go to the **Memorystore for Memcached** page in the Google Cloud console   
[Memorystore for Memcached](https://console.cloud.google.com/memorystore/memcached/instances)

  2. Click the instance ID of the instance you want to upgrade

  3. In the **Instance properties** section next to **Version** , click **UPGRADE**

  4. Select the Memcached version to upgrade to

  5. Click the **Submit** button




### gcloud

To upgrade the Memcached version of your instance, run the `upgrade` command:
    
    
    gcloud memcache instances upgrade instance-id --memcached-version=memcached-version --region=region
    

Replace the following:

  * instance-id is the ID of your instance.

  * memcached-version is your desired Memcached version for your instance. The accepted values is `1.6.15`.

  * region is the region where you want to deploy your instance.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
