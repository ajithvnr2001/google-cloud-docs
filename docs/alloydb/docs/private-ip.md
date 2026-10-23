---
url: https://docs.cloud.google.com/alloydb/docs/private-ip/
title: Private IP overview \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:11.619442+00:00
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

To keep your database traffic within a private network and minimize your attack surface, you can connect to your AlloyDB for PostgreSQL instances by using private IP addresses. Because private IP addresses are internal to your network and inaccessible from the public internet, they restrict network access to authorized private endpoints.

**Note:** If you plan to use AlloyDB along with other Google Cloud services, then you can use Terraform templates for setup and management of Google Cloud networking infrastructure. For more information, see [Simplified Cloud Networking Configuration Solutions](https://github.com/GoogleCloudPlatform/cloudnetworking-config-solutions).

## Private IP connectivity methods

To access your AlloyDB instances using private IP, you can choose either private services access or Private Service Connect. Because each connection method offers distinct advantages and trade-offs, use the information in this document to choose the best approach for your specific requirements.

**Caution:** After you create your AlloyDB cluster, the private IP access method cannot be changed. Therefore, careful consideration is required during the initial setup process.

### Private services access

Private services access is implemented as a Virtual Private Cloud (VPC) peering connection between your VPC network and the underlying Google Cloud VPC network where your AlloyDB for PostgreSQL instance resides. The private connection lets VM instances in your VPC network and the services that you access communicate exclusively by using internal IP addresses. VM instances don't need internet access or external IP addresses to reach services that are available through private services access.

To automate the setup of AlloyDB clusters with private services access using Terraform, see [Deploy AlloyDB using Terraform](https://github.com/GoogleCloudPlatform/cloudnetworking-config-solutions/blob/main/docs/AlloyDB/alloydbinstance-using-psa-accessed-from-gce.md).

For more information about using private services access for connectivity, see [Private services access overview](https://docs.cloud.google.com/alloydb/docs/about-private-services-access).

### Private Service Connect

[Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) lets you create private and secure connections between your VPC networks and a Google Cloud service, such as AlloyDB for PostgreSQL. You can connect to your AlloyDB instance from multiple VPC networks that belong to different groups, teams, projects, or organizations. When you create an AlloyDB cluster, you can enable it to support Private Service Connect. When creating an AlloyDB instance within the cluster, you specify which projects from your VPC network can access it.

For more information about using Private Service Connect, see [Private Service Connect overview](https://docs.cloud.google.com/alloydb/docs/about-private-service-connect) and the video [What is Private Service Connect?](https://www.youtube.com/watch?v=JAFagcQBV08).

## Choose between methods to use

Before you decide whether to use private services access or Private Service Connect as your connection method, consider the following comparison:

Private services access | Private Service Connect  
---|---  
Requires reserving a CIDR range (`/24` at a minimum) from the consumer VPC network. A range of IP addresses is reserved regardless of whether they are in use, locking all IP addresses in the range. | Requires a single IP address to create a forwarding rule at the endpoint per VPC network.  
Supports connections only from clients in [RFC 1918](https://www.rfc-editor.org/rfc/rfc1918) IP ranges (`10.0.0.0/8`, `172.16.0.0/12`, and `192.168.0.0/16`). If you require connectivity from clients that are outside RFC 1918 ranges, use [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect). | Both [RFC 1918](https://www.rfc-editor.org/rfc/rfc1918) and non-RFC 1918 ranges can be used for endpoints.  
Connects to projects within the same VPC network. | Connects across multiple VPC networks or projects.  
Well-suited for small-scale, single-VPC scenarios. | Well-suited for large-scale, multi-VPC setups.  
Minimal cost because you use existing VPC peering included in your project. | Higher cost compared to private services access due to costs for each endpoint per hour and data transfer per GiB.  
Less isolated compared to Private Service Connect due to VPC Network Peering. | More isolated due to separation of consumer and producer VPC networks.  
Connections are bidirectional, allowing both inbound and outbound traffic. | By default, connections are unidirectional, allowing inbound connections only. Additional configuration is required for outbound connections.  
  
## What's next

  * [Private services access overview](https://docs.cloud.google.com/alloydb/docs/about-private-services-access)
  * [Private Service Connect overview](https://docs.cloud.google.com/alloydb/docs/about-private-service-connect)
  * Watch a Google Cloud Skills Boost video to learn how to [use private services access to provide access to producer services](https://www.cloudskillsboost.google/paths/14/course_templates/36/video/500632).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
