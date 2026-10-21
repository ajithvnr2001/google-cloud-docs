---
url: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/producer-vpc-spokes-supported-services/
title: Supported services for producer VPC spokes \u00a0|\u00a0 Network Connectivity Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:19:04.163793+00:00
---

# Supported services for producer VPC spokes  |  Network Connectivity Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/producer-vpc-spokes-supported-services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Network Connectivity Center ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview)



Send feedback 

#  Supported services for producer VPC spokes Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the services supported with producer Virtual Private Cloud spokes.

To use a producer VPC spoke, the service must be consumed by using [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access) or [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering). That is, the name of the peering connection between your VPC network and the producer VPC network must be `servicenetworking-googleapis-com`.

The following Google services consumed through private services access can be used with producer VPC spokes.

If you're using [Google Cloud NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/get-started/configure-access/networking), the name of the peering connection must be `sn-netapp-*`.

For detailed information, see the following resources:

  * For information about configuring private service access, see [Configure private services access](https://docs.cloud.google.com/netapp/volumes/docs/get-started/configure-access/networking#configure_private_services_access).

  * For information about producer Virtual Private Cloud (VPC) spokes in Network Connectivity Center (NCC), see [Producer VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/producer-vpc-spokes-overview).




The following Google services consumed through private services access can be used with producer VPC spokes.

  * [AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/configure-connectivity)
  * [Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/configure-service-networking)
  * [Cloud Build](https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview)
  * [Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/private-ip)
  * [Filestore](https://docs.cloud.google.com/filestore/docs/overview)
  * [Google Cloud Managed Lustre](https://docs.cloud.google.com/managed-lustre/docs/overview)
  * [Google Cloud NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/connect-additional-networks#connect-additional-networks-with-ncc)
  * [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-create-private-ip)
  * [Memorystore for Memcached](https://docs.cloud.google.com/memorystore/docs/memcached/establishing-connection)
  * [Memorystore for Redis](https://docs.cloud.google.com/memorystore/docs/redis/establishing-connection)
  * [Vertex AI](https://docs.cloud.google.com/vertex-ai/docs/general/vpc-peering)



You can check whether a service producer exports only subnet routes by [listing peering routes](https://docs.cloud.google.com/vpc/docs/using-vpc-peering#list-peer-routes) and ensuring that the associated peering connection only has routes of type **Peering subnet**.

Producer VPC spokes don't support third-party services.

## What's next

  * [Create a producer VPC spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/create-producer-vpc-spoke)
  * [Troubleshoot NCC](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/support/troubleshooting)
  * [Get details about API and `gcloud` commands](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/apis)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
