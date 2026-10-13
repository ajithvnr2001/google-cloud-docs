---
url: https://docs.cloud.google.com/alloydb/docs/private-ip/
title: Private IP overview \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:32:09.154137+00:00
---

# Private IP overview  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/private-ip/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Private IP overview Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of the ways in which you can connect to your AlloyDB for PostgreSQL instance using private IP addresses.

Using private IP addresses keeps your data traffic within a secured network and minimizes risk of interception. A resource's internal IP address, being internal to its network and inaccessible from the internet, effectively limits both its scope of accessing an AlloyDB instance and potential attack surface.

**Note:** If you plan to use AlloyDB along with other Google Cloud services, then you can use Terraform templates for setup and management of Google Cloud networking infrastructure. For more information, see [ Simplified Cloud Networking Configuration Solutions](https://github.com/GoogleCloudPlatform/cloudnetworking-config-solutions).

## Private IP connectivity methods

To access your AlloyDB instances using private IP, you can choose either private services access or Private Service Connect. Since each connection method offers distinct advantages and trade-offs, use the information in this document to choose the best approach for your specific requirements. 

**Caution:** Once you create your AlloyDB cluster, the private IP access method cannot be changed. Therefore, careful consideration is required during the initial setup process.

### Private services access

Private services access is implemented as a Virtual Private Cloud (VPC) peering connection between your VPC network and the underlying Google Cloud VPC network where your AlloyDB for PostgreSQL instance resides. The private connection enables VM instances in your VPC network and the services that you access to communicate exclusively by using internal IP addresses. VM instances don't need Internet access or external IP addresses to reach services that are available through private services access.

To automate the setup of AlloyDB clusters with private services access using Terraform, see [Deploy AlloyDB using Terraform](https://github.com/GoogleCloudPlatform/cloudnetworking-config-solutions/blob/main/docs/AlloyDB/alloydbinstance-using-psa-accessed-from-gce.md).

For more information about using private services access for connectivity, see [Private services access overview](https://docs.cloud.google.com/alloydb/docs/about-private-services-access).

### Private Service Connect

[Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) lets you create private and secure connections between your VPC networks and the Google Cloud service, such as AlloyDB for PostgreSQL. You can connect to your AlloyDB instance from multiple VPC networks that belong to different groups, teams, projects, or organizations. When you create an AlloyDB cluster, you can enable it to support Private Service Connect. When creating an AlloyDB instance within the cluster, you specify which projects from your VPC network can access it.

For more information about using Private Service Connect, see [Private Service Connect overview](https://docs.cloud.google.com/alloydb/docs/about-private-service-connect) and the video [What is Private Service Connect?](https://www.youtube.com/watch?v=JAFagcQBV08).

## Choose between methods to use

Before you make a decision about whether to use private services access or Private Service Connect as your connection method, consider the following comparison:

Private services access | Private Service Connect  
---|---  
Requires reserving a CIDR range (/24 at a minimum) from the consumer VPC. A range of IPs is reserved regardless of whether they are in use, leading to lock on all IP addresses in the range. | Requires a single IP address to create a forwarding rule at the endpoint per VPC network.  
Supports connections only from clients in [RFC 1918](https://www.rfc-editor.org/rfc/rfc1918) IP ranges (10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16). If you require connectivity from clients that are outside RFC 1918 ranges, use [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect). | Both [RFC 1918](https://www.rfc-editor.org/rfc/rfc1918) and Non-RFC 1918 ranges can be used for endpoints.  
Connect to projects within the same VPC network. | Connect across multiple VPCs or projects.  
Opt for small-scale, single-VPC scenarios. | Opt for large-scale, multi-VPC setups.  
Minimal cost since you use existing VPC peering included in your project. | More expensive as compared to private services access due to costs involved in initial setup, use of each endpoint per hour, and data transfer per GiB.  
Less secure compared to Private Service Connect due to direct connection. | More secure due to isolation of consumer and producer VPC.  
Connections are bi-directional, allowing both inbound and outbound traffic. | By default, connections are unidirectional allowing inbound connections only. Additional configuration is required for outbound connections.  
  
## What's next

  * [Private services access overview](https://docs.cloud.google.com/alloydb/docs/about-private-services-access)
  * [Private Service Connect overview](https://docs.cloud.google.com/alloydb/docs/about-private-service-connect)
  * Watch a Cloud Skills Boost video to learn how to [use private services access to provide access to producer services](https://www.cloudskillsboost.google/paths/14/course_templates/36/video/500632).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
