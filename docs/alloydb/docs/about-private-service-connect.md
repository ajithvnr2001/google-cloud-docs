---
url: https://docs.cloud.google.com/alloydb/docs/about-private-service-connect/
title: Private Service Connect overview \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:46:21.083750+00:00
---

# Private Service Connect overview  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/about-private-service-connect/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Private Service Connect overview Stay organized with collections  Save and categorize content based on your preferences. 

To establish private, secure connectivity between your Virtual Private Cloud (VPC) networks and your AlloyDB for PostgreSQL instances without configuring VPC Network Peering, you can use Private Service Connect. Private Service Connect supports the following connectivity scenarios:

  * Connect to an AlloyDB instance from multiple VPC networks that belong to different groups, teams, projects, or organizations.
  * Connect to a primary instance, a read pool instance, or a secondary instance.



Private Service Connect uses the concept of consumer and producer. For example, your VPC network is the _consumer_ of the AlloyDB service published by Google Cloud, which is the _producer_. For inbound connectivity, AlloyDB instances publish a service attachment URL, a unique identifier that is used to connect to an instance, and the allowed networks within the allowed projects create an endpoint to establish a secure connection to the AlloyDB service.

For outbound connectivity, consumer networks create and manage Private Service Connect network attachments. AlloyDB instances use these network attachments to manage connectivity for outbound operations, such as migration or foreign data wrappers (FDW).

For detailed information about using Private Service Connect in AlloyDB, see [Connect to an instance using Private Service Connect](https://docs.cloud.google.com/alloydb/docs/configure-private-service-connect).

## Service connection policy

A service connection policy lets you authorize AlloyDB to create a Private Service Connect connection between AlloyDB and consumer VPC networks. As a result, you can provision Private Service Connect endpoints automatically. For example, you can create a service connection policy in one or more of your (consumer) VPC networks and also specify a subnet. The subnet is used to allocate IP addresses for the endpoints that are automatically created through the policy to connect to AlloyDB. The policy also defines a connection limit that determines how many endpoints can be created.

For more information about service connection policy, see [About service connection policies](https://docs.cloud.google.com/vpc/docs/about-service-connection-policies).

## Service attachment

When you create any AlloyDB instance within a Private Service Connect-enabled cluster, AlloyDB creates a service attachment unique to that instance. For each primary instance, read pool instance, or secondary instance created, a unique service attachment URL is generated. This service attachment URL is used to create a Private Service Connect endpoint for your project or network.

## Network attachment

**Note:** You can't enable outbound connectivity on AlloyDB instances created prior to March 01, 2025. For more information about alternative approaches, see [Update an instance for outbound connectivity](https://docs.cloud.google.com/alloydb/docs/configure-private-service-connect#update-instance-outbound-connectivity).

To enable outbound connectivity from an AlloyDB instance to your consumer project, you need to create a network attachment within that VPC and project. This network attachment, which is a regional resource, acts as the connection point. You can create a network attachment that can accept connections automatically (`ACCEPT_AUTOMATIC`) or manually (`ACCEPT_MANUAL`). For more information about creating a network attachment, see [Create and manage network attachments](https://docs.cloud.google.com/vpc/docs/create-manage-network-attachments).

## Private Service Connect endpoint

A Private Service Connect endpoint is a forwarding rule that's associated with an internal IP address. When you create a Private Service Connect-enabled cluster and instance, you can let AlloyDB [automatically create endpoints](https://docs.cloud.google.com/alloydb/docs/configure-private-service-connect#create-endpoint-automatically) for you or create the endpoint manually. As part of [creating the endpoint manually](https://docs.cloud.google.com/alloydb/docs/configure-private-service-connect#create-the-endpoint-manually), you must specify the service attachment that's associated with the AlloyDB instance. The VPC network can then access the instance through the endpoint.

## DNS names and records

Because multiple endpoints across different VPC networks can connect to a single service attachment, each AlloyDB instance provides a unique pre-generated DNS name (`pscDnsName`). You can use this DNS name to [create a DNS record](https://docs.cloud.google.com/alloydb/docs/configure-private-service-connect#configure-dns) in a private Cloud DNS zone for each consumer VPC network that maps the instance's `pscDnsName` to the internal IP address of the Private Service Connect endpoint in that network:

  * **AlloyDB Auth Proxy and AlloyDB Language Connectors** : Require a private DNS record that resolves the instance's `pscDnsName` to the Private Service Connect endpoint's internal IP address.
  * **Direct connections (such as`psql`)**: Can connect by using either the Private Service Connect endpoint's internal IP address directly or the configured private DNS name. We recommend using the DNS name so applications can use a consistent hostname across multiple networks.



## Allowed Private Service Connect projects

When you create an AlloyDB instance, you can define which projects from your VPC network can access the AlloyDB instance within the AlloyDB cluster.

For each allowed project in your VPC network, create a unique Private Service Connect endpoint. If a project isn't allowed explicitly, then you can still create an endpoint for the instances in the project, but the endpoint remains in a `PENDING` state.

## Limitations

  * Private Service Connect endpoints can be created in both [RFC 1918](https://www.rfc-editor.org/rfc/rfc1918) and non-RFC 1918 ranges.
  * Private DNS resolution for Private Service Connect outbound connections (such as when using foreign data wrappers or `dblink`) isn't supported.



## What's next

  * Learn about [Private Service Connect in Google Cloud networking](https://docs.cloud.google.com/vpc/docs/private-service-connect).
  * Learn more about [connecting to an instance using Private Service Connect](https://docs.cloud.google.com/alloydb/docs/configure-private-service-connect).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
