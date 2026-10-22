---
url: https://docs.cloud.google.com/memorystore/docs/redis/self-service-maintenance/
title: Self-service maintenance \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:13:50.560773+00:00
---

# Self-service maintenance  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/self-service-maintenance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  Self-service maintenance Stay organized with collections  Save and categorize content based on your preferences. 

This page describes self-service maintenance, which lets you accept a maintenance update on your instance outside of the normal flow of scheduled maintenance. To see what vulnerabilities are addressed by each self-service maintenance update, see [Maintenance changelog](https://docs.cloud.google.com/memorystore/docs/redis/maintenance-changelog).

## Overview

Memorystore for Redis regularly releases software improvements, such as patches for known vulnerabilities, through new maintenance versions. While Memorystore for Redis schedules maintenance updates once every few months to ensure you have the latest maintenance version, you might want to use self-service maintenance if:

  * You need an update sooner than your next scheduled maintenance event.
  * You want to stay up-to-date with CVE patches necessary for FedRAMP Compliance.



You're not required to manually update to the latest version. You can let Memorystore for Redis automatically update your maintenance version during your next scheduled maintenance event.

**Note:** You can only update your instance maintenance version to a newer version.

### Impact of self-service maintenance

Self-service maintenance updates have the same impact on your application as standard maintenance update. For more information, see [Impact of maintenance](https://docs.cloud.google.com/memorystore/docs/redis/about-maintenance#impact_of_maintenance).

## View your current maintenance version

Check your current maintenance version using the `describe` command:
    
    
    gcloud redis instances describe INSTANCE_ID
    

Replace the following:

  * INSTANCE_ID is the ID of your instance



The maintenance version is indicated beside the `maintenanceVersion` attribute.

## View available maintenance versions you can update to

### Console

  1. Go to the **Memorystore for Redis** page in the Google Cloud console.

[Memorystore for Redis](https://console.cloud.google.com/memorystore/redis/instances)

  2. Click your instance ID.

  3. If a maintenance update is available, _Update available_ text is visible in the **Maintenance** section of the **Overview** tab.

  4. Click **View and Apply**.

  5. The **Choose Maintenance Version** dropdown lists all maintenance versions you can update to.




### gcloud

To view available maintenance versions, use the `describe` command:
    
    
    gcloud redis instances describe INSTANCE_ID
    

Replace the following:

  * INSTANCE_ID is the ID of your instance



The list of available maintenance versions is indicated beside the `availableMaintenanceVersions` attribute. If no versions are listed using this attribute, then your instance has the latest version.

## Update your instance to a new maintenance version

### Console

  1. Go to the **Memorystore for Redis** page in the Google Cloud console.

[Memorystore for Redis](https://console.cloud.google.com/memorystore/redis/instances)

  2. Click your instance ID.

  3. If a maintenance update is available, _Update available_ text appears in the **Maintenance** section of the **Overview** tab.

  4. Click **View and Apply**.

  5. Select your desired maintenance version from the **Choose Maintenance Version** dropdown.

  6. Click the **Apply** button.




### gcloud

Use the following method to update your instance to the target maintenance version.
    
    
    gcloud redis instances update INSTANCE_ID --maintenance-version=MAINTENANCE_VERSION
    

Replace the following:

  * INSTANCE_ID is the ID of your instance
  * MAINTENANCE_VERSION is the maintenance version to apply. You can find these values by [Viewing available maintenance versions you can update to](https://docs.cloud.google.com/memorystore/docs/redis/self-service-maintenance#view_available_maintenance_versions_you_can_update_to).



## Revert your instance to the current default maintenance update

If for any reason you want to revert from the newest maintenance update version to the current default version, you can do so using the Google Cloud CLI. For example, if you update your instance to the newest self-service maintenance update, and doing this causes an issue/regression with your instance, then you can revert back to the current default maintenance version with the `update` command.

Run the `update` command and use the value `current_default` to revert the maintenance version:
    
    
    gcloud redis instances update INSTANCE_ID --maintenance-version=current_default
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
