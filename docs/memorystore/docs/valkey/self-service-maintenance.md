---
url: https://docs.cloud.google.com/memorystore/docs/valkey/self-service-maintenance/
title: Self-service maintenance \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:00.420220+00:00
---

# Self-service maintenance  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/self-service-maintenance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  Self-service maintenance Stay organized with collections  Save and categorize content based on your preferences. 

This page describes self-service maintenance, which lets you accept a maintenance update on your instance outside of the typical flow of scheduled maintenance. To see which vulnerabilities are addressed by each self-service maintenance update, see [Memorystore for Valkey maintenance changelogs](https://docs.cloud.google.com/memorystore/docs/valkey/maintenance-changelog).

## Overview

Memorystore for Valkey releases software improvements regularly, such as patches for known vulnerabilities, through new maintenance versions. Although Memorystore for Valkey schedules maintenance updates once every few months to ensure that you have the latest maintenance version, you might want to use self-service maintenance if any of the following conditions apply:

  * You need an update sooner than your next scheduled maintenance event.
  * You want to stay up-to-date with CVE patches necessary for FedRAMP Compliance.



You're not required to update to the latest version manually. You can let Memorystore for Valkey update your maintenance version automatically during your next scheduled maintenance event.

**Note:** You can update your instance's maintenance version to a newer version only.

### Impact of self-service maintenance

Self-service maintenance updates have the same impact on your applications as standard maintenance updates. For more information, see [About maintenance](https://docs.cloud.google.com/memorystore/docs/valkey/about-maintenance).

## View maintenance versions

You can use either the Google Cloud console or the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) to view the following information about maintenance versions that are associated with your instance:

  * The current maintenance version.
  * Available maintenance versions to which you can update your instance.




### Console

  1. In the Google Cloud console, go to the **Memorystore for Valkey** page.

[Memorystore for Valkey](https://console.cloud.google.com/memorystore/valkey/instances)

  2. Click the instance about which you want to view maintenance version information.

  3. On the **Instance at a glance** page, scroll until the **Maintenance** card appears.

Next to the **Maintenance version** field, the current maintenance version appears. Also, if there are available maintenance versions to which you can update the instance, then the **Update available** status appears next to the **Self-service maintenance** field. If the **No updates are available** status appears, then the instance has the latest version.




### gcloud

To view maintenance version information about your instance, use the [`gcloud memorystore instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/describe) command.
    
    
    gcloud memorystore instances describe INSTANCE_ID /
    --location=REGION_NAME /
    --project=PROJECT_NAME
    

Make the following replacements:

  * INSTANCE_ID: the ID of the instance
  * REGION_NAME: the region name for the instance
  * PROJECT_NAME: the name of the Google Cloud project that contains the instance



The current maintenance version appears next to the `effectiveMaintenanceVersion` field. Also, the list of available maintenance versions appears next to the `availableMaintenanceVersions` field. If no versions appear, then your instance has the latest version.

## Update your instance to a new maintenance version

You can use either the Google Cloud console or the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) to update your instance to a newer maintenance version.

### Console

  1. In the Google Cloud console, go to the **Memorystore for Valkey** page.

[Memorystore for Valkey](https://console.cloud.google.com/memorystore/valkey/instances)

  2. Click the instance for which you want to update the maintenance version.

  3. On the **Instance at a glance** page, scroll until the **Maintenance** card appears.

  4. Next to the **Self-service maintenance** field, click **View and apply**.

If the **No updates are available** status appears next to this field, then the instance has the latest version.

  5. In the **Self-service maintenance** dialog, do the following:

     1. From the **Choose maintenance version** menu, select the maintenance version to which you want to update the instance.
     2. Click **Apply**.



### gcloud

To update the maintenance version for your instance, use the [`gcloud memorystore instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/update) command.
    
    
    gcloud memorystore instances update INSTANCE_ID /
    --location=REGION_NAME /
    --project=PROJECT_NAME
    --maintenance-version=MAINTENANCE_VERSION
    

Make the following replacements:

  * INSTANCE_ID: the ID of your instance.
  * REGION_NAME: the region name for the instance.
  * PROJECT_NAME: the name of the Google Cloud project that contains the instance.
  * MAINTENANCE_VERSION: the maintenance version to which you want to update your instance. To find available maintenance versions, see View maintenance versions.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
