---
url: https://docs.cloud.google.com/memorystore/docs/valkey/upgrade-valkey-version/
title: Upgrade the Valkey version of an instance \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:12:08.775580+00:00
---

# Upgrade the Valkey version of an instance  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/upgrade-valkey-version/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  Upgrade the Valkey version of an instance Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to upgrade the version of a Memorystore for Valkey instance. For a list of available versions, see [Supported versions](https://docs.cloud.google.com/memorystore/docs/valkey/supported-versions). For more information about the behavior of an instance during an upgrade operation, see [Version upgrade behavior](https://docs.cloud.google.com/memorystore/docs/valkey/about-upgrading-version#version-upgrade-behavior).

## Upgrade the instance version

**Important:** You can upgrade the version of an instance to any newer version. For example, you can upgrade from version 7.2 to 9.1. However, after you upgrade the version of an instance, you can't downgrade the instance to an earlier version.

### Console

  1. In the Google Cloud console, go to the Memorystore for Valkey page.

[Memorystore for Valkey](https://console.cloud.google.com/memorystore/valkey/instances)

  2. Click the ID of the instance that you want to upgrade.

  3. In the **Configurations** section, next to **Valkey version** , click **Upgrade**.

  4. In the **Upgrade version** dialog, do the following:

     1. Click the **Version** menu.
     2. Select the version to which you want to upgrade your instance.
     3. Click **Update instance**.



### gcloud

To upgrade the version of your instance, use the [`gcloud memorystore instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/update) command.
    
    
    gcloud memorystore instances update INSTANCE_ID \
    --project=PROJECT_ID \
    --location=REGION_ID \
    --engine-version=ENGINE_VERSION
    

Replace the following:

  * INSTANCE_ID: the ID of your Memorystore for Valkey instance.
  * PROJECT_ID: the project ID or number of the Google Cloud project where the instance is located.
  * REGION_ID: the region where the instance is located.
  * ENGINE_VERSION: the version number of Valkey to which you want to upgrade your instance. Accepted values are `VALKEY_7_2`, `VALKEY_8_0`, `VALKEY_9_0`, and `VALKEY_9_1`.



For example:
    
    
    gcloud memorystore instances update my-instance \
    --project=my-project \
    --location=us-central1 \
    --engine-version=VALKEY_9_1

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
