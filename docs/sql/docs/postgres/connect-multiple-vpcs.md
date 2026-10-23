---
url: https://docs.cloud.google.com/sql/docs/postgres/connect-multiple-vpcs/
title: Connect your instance to multiple VPCs \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:12:08.167412+00:00
---

# Connect your instance to multiple VPCs  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/connect-multiple-vpcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Connect your instance to multiple VPCs Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/connect-multiple-vpcs "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/connect-multiple-vpcs "View this page for the SQL Server database engine")

This document describes how to connect to your Cloud SQL instance across transitively peered Virtual Private Cloud (VPC) networks.

The recommended method to connect your Cloud SQL instance across multiple VPC networks is to use Private Service Connect.

If your Cloud SQL instance can use only [private services access](https://docs.cloud.google.com/vpc/docs/about-private-services-access) for private network connectivity, then you have the following options to connect your Cloud SQL instance to multiple VPC networks:

  * Connect using custom advertised routes
  * Connect using an intermediate proxy (SOCKS5)
  * Connect using the Cloud SQL Auth Proxy as a service



## Connect using Private Service Connect

[Private Service Connect](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect) lets you connect to multiple VPC networks across different projects or organizations. You can use Private Service Connect to connect to either a primary instance or any of its read replicas. For more information about Private Service Connect, see [Private Service Connect overview](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect).

To configure a Cloud SQL instance to connect to multiple VPCs using Private Service Connect, see [Configure Private Service Connect](https://docs.cloud.google.com/sql/docs/postgres/configure-private-service-connect).

## Connect using custom advertised routes

You can use [Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview) to configure custom advertised routes between two networks that go through an intermediate VPC to connect multiple VPCs to your Cloud SQL instance. The two VPCs must be connected using a virtual private network (VPN), Cloud Interconnect , or any other [Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview) supported network.

![Custom route advertisements.](https://docs.cloud.google.com/static/sql/images/multiple-vpc-custom-route.svg)

With custom advertised routes, your Cloud SQL VPC, _VPC C_ , is connected to your main VPC, _VPC A_ , using an intermediate VPC, _VPC B_. You can configure shared routes between these networks in the following ways:

  * You can use Cloud Router to manually advertise routes between two networks that go through an intermediate VPC. For more information on how to configure Cloud Router to manually advertise routes, see [Transit network](https://docs.cloud.google.com/vpc/docs/vpc-peering#transit-network).

  * You can create two [HA VPN gateways](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/topologies#2-gcp-gateways) that connect to each other to bridge the two different VPCs and configure Cloud Router to share routes between them. For more information on how to set up HA VPN gateways, see [Create HA VPN gateways to connect VPC networks](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn2#creating-ha-gw-2-gw-and-tunnel).




We recommend using custom advertised routes to connect multiple VPCs to your Cloud SQL instance using [Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview).

## Connect using an intermediate proxy (SOCKS5)

You can set up an intermediate proxy, such as SOCKS5 proxy, on an intermediate VPC along with the [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/postgres/sql-proxy) in your main VPC between the client and your Cloud SQL instance. This enables the intermediate node to forward encrypted traffic from the Cloud SQL Auth Proxy to the Cloud SQL instance.

![Connecting using an intermediate proxy.](https://docs.cloud.google.com/static/sql/images/multiple-vpc-proxy.svg)

To use an intermediary proxy to connect to your Cloud SQL instance from multiple VPCs, follow these steps:

  1. On your external client, [install ](https://docs.cloud.google.com/sdk/docs/install)[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

  2. On the intermediary VM, install, configure, and run a SOCKS server. One example of this server is [Dante](https://www.inet.no/dante/), a popular open source solution.

  3. Configure the server to bind to the VM's `ens4` network interface for both external and internal connections. For internal connections, specify any port.

  4. [Configure your VPC's firewall](https://docs.cloud.google.com/vpc/docs/firewalls) to allow TCP traffic from the appropriate IP address or range to the SOCKS server's configured port.

  5. On your external client, [download and install the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/postgres/sql-proxy#install).

  6. On your external client, [start the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/postgres/connect-auth-proxy#start-proxy).

Because you configured your instance to use an internal IP address, when you start the Cloud SQL Auth Proxy, you must provide the `--private-ip` option.

Also, set the `ALL_PROXY` environment variable to the intermediary VM's IP address and specify the port that the SOCKS server uses. For example, `ALL_PROXY=socks5://VM_IP_ADDRESS:SOCKS_SERVER_PORT.`

**Note:** The default port for the SOCKS server is `1080`.

If you're connecting from a peered VPC, then use the intermediary VM's internal IP address; otherwise, use its external IP address.

  7. On your external client, test your connection using [`psql`](https://docs.cloud.google.com/sql/docs/postgres/connect-admin-ip).




## Connect using the Cloud SQL Auth Proxy as a service

You can install and run the Cloud SQL Auth Proxy on your intermediate VPC instead of your external client and enable secure connections by pairing it with a protocol-aware proxy, also known as a connection pooler. Examples of connection poolers include [PGbouncer](https://www.pgbouncer.org/), or [Pgpool-II](https://pgpool.net/)(PostgreSQL only).

This connection method allows your applications to securely connect directly to the pooler using a configured SSL. The pooler passes databases queries to your Cloud SQL instance using the Cloud SQL Auth Proxy.

**Note:** You'll need to set up your own secure connection. These connections aren't secured by Cloud SQL.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
