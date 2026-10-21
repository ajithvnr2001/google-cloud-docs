---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/data-protection/
title: Data protection with multi-zone storage \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:43:35.344831+00:00
---

# Data protection with multi-zone storage  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/data-protection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Data protection with multi-zone storage Stay organized with collections  Save and categorize content based on your preferences. 

To protect your application data in a Google Distributed Cloud (GDC) air-gapped multi-zone universe and maintain highly available applications, you can implement a data protection strategy that is resilient to local outages or failures. GDC provides data replication strategies for [object storage](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/storage#object_storage) and [block storage](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/storage#block_storage) so you can maintain failover procedures for primary and secondary zones in your universe.

This document is for the following audience groups:

  * Platform administrators, such as IT administrators, who are responsible for developing disaster recovery workflows.
  * Application operators, such as application developers, who are responsible for developing and maintaining applications in a GDC universe.



For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Storage replication for disaster recovery

You can set up robust data protection for your application storage in a multi-zone universe using _asynchronous data replication_ for disaster recovery. This approach involves copying data from a primary zone to a secondary zone at periodic intervals. This mechanism keeps your data protected and accessible if the primary zone experiences an outage.

Data replication for object storage uses dual zone buckets to automatically replicate your data, and doesn't require manual intervention. For more information about creating a dual zone bucket, see [Create storage buckets](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-storage-buckets#cli).

Data replication for block storage uses dual zone persistent volumes to replicate your data, and requires a volume failover procedure. For more information, see [Replicate volumes asynchronously](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/async-block-replication).

After you configure data replication, your data follows a sequential _failover procedure_ when the primary zone is offline. The failover procedures are distinct for block and object storage replication. However, both data replication strategies follow these critical stages:

  1. Verify the primary zone outage.
  2. Stop the replication from the primary zone.
  3. Promote the backup secondary zone to assume the role of the primary zone with manual intervention or a pre-configured failover.
  4. Verify the operational status of the new primary zone.



Reach out to a member of the infrastructure operator group to confirm your two zones are configured for asynchronous data replication.

The inherent delay that comes with asynchronous data replication means that this setup is most useful for systems that require a low, but non-zero recovery point objective (RPO). If your system requires minimal data loss, but can tolerate a small predefined maximum amount of data loss measured in time, usually related to data generated just immediately before a disaster event that could be potentially unrecoverable, then asynchronous data replication is a valuable feature to implement for your applications.

An example of a low non-zero RPO might be a financial trading platform with an RPO of five minutes, where asynchronous data replication is set to copy trade data to a secondary disaster recovery zone every two minutes:

  * This is a _low RPO_ scenario because the five minutes represents the minimum acceptable data loss window for the high-volume system.
  * It's a _non-zero RPO_ scenario because the inherent delay in asynchronous replication of two minute intervals means that there is a small window of time where data has not yet been copied, resulting in potential loss.



You must work with your infrastructure operator group to define your dual zone asynchronous storage replication workflow, and verify the infrastructure's data replication capabilities support your RPO requirements.

## Limitations

_Synchronous data replication_ isn't supported in GDC air-gapped. Synchronous data replication maintains strict consistency between data in two zones by immediately duplicating all data written from a primary zone to the secondary zone, which provides zero RPO in disaster scenarios.

## What's next

  * [High availability for your apps](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/ha-apps/overview)
  * [Deploy a highly available VM application](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/ha-apps/deploy-ha-vm-app)
  * [Deploy a highly available container application](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/ha-apps/deploy-ha-container-app)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
