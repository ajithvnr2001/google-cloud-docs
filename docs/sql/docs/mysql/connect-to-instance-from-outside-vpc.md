---
url: https://docs.cloud.google.com/sql/docs/mysql/connect-to-instance-from-outside-vpc/
title: Connect to a Cloud SQL instance from outside its VPC \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:31:12.417656+00:00
---

# Connect to a Cloud SQL instance from outside its VPC  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/connect-to-instance-from-outside-vpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Connect to a Cloud SQL instance from outside its VPC Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/connect-to-instance-from-outside-vpc "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/connect-to-instance-from-outside-vpc "View this page for the SQL Server database engine")

This page describes how to connect to a Cloud SQL instance from outside its configured Virtual Private Cloud (VPC).

## Before you begin

Before you begin, make sure that you complete the following actions: 

  1. You [create a Cloud SQL instance](https://docs.cloud.google.com/sql/docs/mysql/create-instance).
  2. You [configure your instance to use an internal IP address](https://docs.cloud.google.com/sql/docs/mysql/configure-private-ip) instead of an external IP address.



## About external connections

Your Cloud SQL instance consists of a number of nodes within a Google-managed VPC. When you create an instance, you also configure [private services access](https://docs.cloud.google.com/sql/docs/mysql/configure-private-services-access) or [Private Service Connect](https://docs.cloud.google.com/sql/docs/mysql/configure-private-service-connect) between one of your VPCs and the Google-managed VPC containing your new instance. This peered connection lets you use internal IP addresses to access resources on the instance's VPC as if they're part of your own VPC.

In the following situations, connect to your instance from outside a connected VPC:

  * Your application runs outside of the VPC that you used to connect to your instance through private services access or Private Service Connect.

  * Your application runs on a VPC that exists outside of Google's network.

  * Your application runs on a machine that's located somewhere else on the public internet.




In all of these cases, you must configure an additional service to enable this kind of external connection to your Cloud SQL instance.

We recommend the following solutions for making external connections, depending upon your needs:

  * For project development or prototyping, or for a relatively low-cost production environment, configure an intermediary virtual machine (VM)—also known as a _bastion_ —within your VPC. Various methods exist to build on this intermediary VM to transform it into a secure connection between an external application environment and your Cloud SQL instance.

  * For production environments that require high availability, consider establishing a permanent connection between the VPC and your application through either Cloud VPN or Cloud Interconnect.




The following sections describe these solutions.

## Connect through an intermediary VM

To establish a connection to a Cloud SQL instance from outside its VPC using open source tools and a minimum of additional resources, run a proxy service on an intermediary VM that's configured within that VPC. You can configure a new VM or use a VM already running within your Cloud SQL instance's VPC.

As a self-managed solution, using an intermediary VM generally costs less and has a faster set-up time than using a Network Connectivity product. It also has downsides: the connection's availability, security, and data throughput all become dependent on the intermediary VM, which you must maintain as part of your project.

### Connect through IAP

Using [Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap/docs/concepts-overview), you can connect to your Cloud SQL instance securely without the need to expose the intermediary VM's internal IP address. You use a combination of firewall rules and Identity and Access Management (IAM) to limit access through this route. This makes IAP a good solution for non-production uses like development and prototyping.

![Identity-Aware Proxy architecture](https://docs.cloud.google.com/static/sql/images/iap-050824.svg)

In this diagram, IAP serves as the gateway between the external client that's outside the VPC and the intermediary VM that's in the VPC. The client creates an SSH tunnel to the IAP. The Cloud SQL Auth Proxy encrypts the traffic between the VM and the Cloud SQL instance. Through these two proxies, communication is established between the client and the instance.

To configure IAP access to your instance, follow these steps:

  1. On your external client, [install ](https://docs.cloud.google.com/sdk/docs/install)[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

  2. On the intermediary VM, [download and install the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/mysql/sql-proxy#install).

  3. On the intermediary VM, [start the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/mysql/connect-auth-proxy#start-proxy).

Because your VM is configured with an internal IP address, when you start the Cloud SQL Auth Proxy, you must provide the `--private-ip` option.

  4. In your Google Cloud project, [enable IAP TCP forwarding](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding#preparing_your_project_for_tcp_forwarding).

When defining the new firewall rule, allow ingress TCP traffic to port `22` (SSH). If you are using [your project's default network](https://docs.cloud.google.com/vpc/docs/vpc#default-network) with its [pre-populated `default-allow-ssh` rule](https://docs.cloud.google.com/vpc/docs/firewalls#more_rules_default_vpc) enabled, then you don't need to define an additional rule.

  5. Configure port forwarding between your external client and the intermediary VM using [SSH through IAP](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding#tunneling_ssh_connections):
         
         gcloud compute ssh VM_NAME \
         --tunnel-through-iap \
         --zone=ZONE_NAME \
         --ssh-flag="-L 3306:localhost:3306"

Make the following replacements:

     * VM_NAME: the name of the VM
     * ZONE_NAME: the name of the zone that's associated with the VM
  6. On your external client, test your connection using [`mysql`](https://docs.cloud.google.com/sql/docs/mysql/connect-admin-ip).




### Connect through a SOCKS proxy

Running a SOCKS service on the intermediary VM provides a flexible and scalable connection to your Cloud SQL instance, with end-to-end encryption provided by the Cloud SQL Auth Proxy.

For more information on using a SOCKS proxy to connect to your Cloud SQL instance, see [Connect using an intermediate proxy (SOCKS5)](https://docs.cloud.google.com/sql/docs/mysql/connect-multiple-vpcs#intermediate-proxy).

### Connect through a pooler

If you need to install and run the Cloud SQL Auth Proxy on the intermediary VM, instead of an external client, then you can enable secure connections to it by pairing it with a _protocol-aware proxy_ , also known as a _pooler_. A popular open source pooler for MySQL is [Proxy SQL](https://www.proxysql.com/). 

In this solution, you run both the Cloud SQL Auth Proxy and the pooler on the intermediary VM. Your client or application can then securely connect directly to the pooler over SSL, without the need to run any additional services. The pooler takes care of passing PostgreSQL queries along to your Cloud SQL instance through the Cloud SQL Auth Proxy.

Because every Cloud SQL instance has a separate internal IP address, each proxy service can communicate with only one specific instance: either the primary instance, the stand-by, or a read pool. Therefore, for every instance, you must run a separate pooler service with an appropriately configured SSL certificate.

## Connect through Cloud VPN or Cloud Interconnect

For production work requiring high availability (HA), we recommend the use of a Google Cloud [Network Connectivity](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product) product, such as [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn) or [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect), depending upon your external service's needs and network topology. You then configure [Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview) to advertise the appropriate routes.

To learn more about Network Connectivity solutions, see [Choosing a Network Connectivity product](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product).

## What's next

  * Learn more about [private IP](https://docs.cloud.google.com/sql/docs/mysql/private-ip).
  * Learn more about [Private services access and on-premises connectivity](https://docs.cloud.google.com/vpc/docs/private-services-access#on-premises-connectivity) in Google-managed VPCs.
  * Learn more about using [Private Service Connect](https://docs.cloud.google.com/sql/docs/mysql/configure-private-service-connect) to connect to a Cloud SQL instance.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
