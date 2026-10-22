---
url: https://docs.cloud.google.com/memorystore/docs/memcached/self-service-maintenance/
title: Self-service maintenance \u00a0|\u00a0 Memorystore for Memcached \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:11.878410+00:00
---

# Self-service maintenance  |  Memorystore for Memcached  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/memcached/self-service-maintenance/

Memorystore for Memcached is being deprecated and will be shut down on January 31, 2029. After February 1, 2027, you can't create Memorystore for Memcached instances in new projects unless these instances already exist in these projects. We recommend that you migrate your workloads to [Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey), which offers superior performance and features.

[Learn more about the deprecation](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation) | [Read the migration guide](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation/migrate-to-valkey)

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Memcached ](https://docs.cloud.google.com/memorystore/docs/memcached)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/memcached/memcached-overview)



Send feedback 

#  Self-service maintenance Stay organized with collections  Save and categorize content based on your preferences. 

This page describes self-service maintenance, which lets you apply a maintenance update on your instance outside of the typical flow of scheduled maintenance. To see what changes each update has, see [Memorystore for Memcached maintenance changelogs](https://docs.cloud.google.com/memorystore/docs/memcached/maintenance-changelog).

## Overview

Memorystore for Memcached releases software improvements regularly, such as patches for known vulnerabilities, through new maintenance versions. Although Memorystore for Memcached schedules maintenance updates once every few months to ensure that you have the latest maintenance version, you might want to use self-service maintenance if any of the following conditions apply:

  * You need an update sooner than your next scheduled maintenance event.
  * You want to stay up-to-date with CVE patches necessary for FedRAMP Compliance.



You're not required to update to the latest version manually. You can let Memorystore for Memcached update your maintenance version automatically during your next scheduled maintenance event.

**Note:** You can update your instance's maintenance version to a newer version only.

### Impact of self-service maintenance

Self-service maintenance updates have the same impact on your applications as standard maintenance updates. For more information, see [About maintenance](https://docs.cloud.google.com/memorystore/docs/memcached/about-maintenance).

## View maintenance versions

You can use the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) to view the following information about maintenance versions that are associated with your instance:

  * The current maintenance version.
  * Available maintenance versions to which you can update your instance.



To view maintenance version information about your instance, use the [`gcloud memcache instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/memcache/instances/describe) command.
    
    
    gcloud memcache instances describe INSTANCE_ID \
    --region=REGION_NAME \
    --project=PROJECT_NAME
    

Make the following replacements:

  * INSTANCE_ID: the ID of the instance
  * REGION_NAME: the region name for the instance
  * PROJECT_NAME: the name of the Google Cloud project that contains the instance



The current maintenance version appears next to the `effectiveMaintenanceVersion` field. Also, the list of available maintenance versions appears next to the `availableMaintenanceVersions` field. If no versions appear, then your instance has the latest version.

## Update your instance to a new maintenance version

You can use the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) to update your instance to a newer maintenance version.

To update the maintenance version for your instance, use the [`gcloud memcache instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/memcache/instances/update) command.
    
    
    gcloud memcache instances update INSTANCE_ID \
    --region=REGION_NAME \
    --project=PROJECT_NAME \
    --maintenance-version=MAINTENANCE_VERSION
    

Make the following replacements:

  * INSTANCE_ID: the ID of the instance.
  * REGION_NAME: the region name for the instance.
  * PROJECT_NAME: the name of the Google Cloud project that contains the instance.
  * MAINTENANCE_VERSION: the maintenance version to which you want to update the instance. To find available maintenance versions, see View maintenance versions.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
