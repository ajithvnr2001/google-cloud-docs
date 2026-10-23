---
url: https://docs.cloud.google.com/alloydb/docs/connect-external/
title: Connect to a cluster from outside its VPC \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:42:55.305909+00:00
---

# Connect to a cluster from outside its VPC  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/connect-external/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Connect to a cluster from outside its VPC Stay organized with collections  Save and categorize content based on your preferences. 

To connect to an AlloyDB for PostgreSQL cluster from applications running outside its configured Virtual Private Cloud (VPC) network—such as on-premises environments, other cloud providers, or separate VPC networks—you can route traffic through an intermediary virtual machine (VM), Cloud VPN, or Cloud Interconnect. Before you begin, make sure that you have [created an AlloyDB cluster](https://docs.cloud.google.com/alloydb/docs/cluster-create).

## About external connections

Your AlloyDB cluster comprises a number of nodes within a Google Cloud VPC network. When you create a cluster, you can [configure private services access](https://docs.cloud.google.com/alloydb/docs/about-private-services-access) between one of your VPC networks and the Google-managed VPC network containing your new cluster. This peered connection lets you use private IP addresses to access resources on the cluster's VPC network as if they are part of your own VPC network.

Situations exist where your application must connect to your cluster from outside this connected VPC network:

  * Your application runs elsewhere within the Google Cloud ecosystem, outside of the VPC network that you connected to your cluster through private services access.

  * Your application runs on a VPC network that exists outside of Google's network.

  * Your application runs "on-premises", on a machine located somewhere else on the public internet.




In all of these cases, you must set up an additional service to enable this kind of external connection to your AlloyDB cluster.

## Summary of external-connection solutions

We recommend two general solutions for making external connections, depending upon your needs:

  * For project development or prototyping, or for a relatively low-cost production environment, set up an intermediary virtual machine (VM)—also known as a _bastion_ —within your VPC. A variety of methods exist to use this intermediary VM as a secure connection between an external application environment and your AlloyDB cluster.

  * For production environments that require high availability, consider establishing a permanent connection between the VPC and your application through either Cloud VPN or Cloud Interconnect.




The next several sections describe these external-connection solutions in detail.

## Connect through an intermediary VM

To establish a connection to an AlloyDB cluster from outside its VPC using open-source tools and a minimum of additional resources, run a proxy service on [an intermediary VM set up within that VPC](https://docs.cloud.google.com/alloydb/docs/connect-psql#create-vm). You can set up a new VM for this purpose, or use a VM already running within your AlloyDB cluster's VPC.

As a self-managed solution, using an intermediary VM generally costs less and has a faster set-up time than using a Network Connectivity product. It also has downsides: the connection's availability, security, and data throughput all become dependent on the intermediary VM, which you must maintain as part of your project.

### Connect through IAP

Using [Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap/docs/concepts-overview), you can securely connect to your cluster without the need to expose the intermediary VM's public IP address. You use a combination of firewall rules and Identity and Access Management (IAM) to limit access through this route. This makes IAP a good solution for non-production uses like development and prototyping.

To set up IAP access to your cluster, follow these steps:

  1. [Install the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk) on your external client.

  2. [Prepare your project for IAP TCP forwarding](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding#preparing_your_project_for_tcp_forwarding).

When defining the new firewall rule, allow ingress TCP traffic to port `22` (SSH). If you are using [your project's default network](https://docs.cloud.google.com/vpc/docs/vpc#default-network) with its [pre-populated `default-allow-ssh` rule](https://docs.cloud.google.com/firewall/docs/firewalls#more_rules_default_vpc) enabled, then you don't need to define an additional rule.

  3. Set up port forwarding between your external client and the intermediary VM using [SSH through IAP](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding#tunneling_ssh_connections).
         
         gcloud compute ssh my-vm \
                --tunnel-through-iap \
                --zone=ZONE_ID \
                --ssh-flag="-L PORT_NUMBER:ALLOYDB_IP_ADDRESS:5432"

Replace the following:

     * `ZONE_ID`: The ID of the zone where the cluster is located—for example, `us-central1-a`.
     * `ALLOYDB_IP_ADDRESS`: The IP address of the AlloyDB instance you want to connect to.
     * `PORT_NUMBER`: The port number of your VM.
**Note:** If you're using [managed connection pooling](https://docs.cloud.google.com/alloydb/docs/configure-managed-connection-pooling), then change the port number from `5432` to `6432`. Apply this change of port throughout the examples on this page.
  4. Test your connection using [`psql`](https://docs.cloud.google.com/alloydb/docs/connect-psql) on your external client, having it connect to the local port you specified in the previous step. For example, to connect as the `postgres` user role to port `5432`:
         
         psql -h localhost -p 5432 -U USERNAME

Replace the following:

     * `USERNAME`: The PostgreSQL user you want to connect to the instance—for example, the default user `postgres`.



### Connect through a SOCKS proxy

Running a SOCKS service on the intermediary VM provides a flexible and scalable connection to your AlloyDB cluster, with end-to-end encryption provided by the AlloyDB Auth Proxy. With appropriate configuration, you can make it suitable for production workloads.

This solution includes these steps:

  1. Install, configure, and run a SOCKS server on the intermediary VM. One example is [Dante](https://www.inet.no/dante/), a popular open-source solution.

Configure the server to bind to the VM's `ens4` network interface for both external and internal connections. Specify any port you want for internal connections.

  2. [Configure your VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls) to allow TCP traffic from the appropriate IP address or range to the SOCKS server's configured port.

  3. Install [the AlloyDB Auth Proxy](https://docs.cloud.google.com/alloydb/docs/auth-proxy/overview) on the external client.

  4. Run the AlloyDB Auth Proxy on your external client, with the `ALL_PROXY` environment variable set to the intermediary VM's IP address, and specifying the port that the SOCKS server uses.

This example configures the AlloyDB Auth Proxy to connect to the database at `my-main-instance`, by way of a SOCKS server running at `198.51.100.1` on port `1080`:
         
         ALL_PROXY=socks5://198.51.100.1:1080 ./alloydb-auth-proxy \
         projects/PROJECT_ID/locations/REGION_ID/clusters/CLUSTER_ID/instances/INSTANCE_ID

If you are connecting from a peered VPC network, you can use the intermediary VM's internal IP address; otherwise, use its external IP address.

  5. Test your connection using [`psql`](https://docs.cloud.google.com/alloydb/docs/connect-psql) on your external client, having it connect to the port that the AlloyDB Auth Proxy listens on. For example, to connect as the `postgres` user role to port `5432`:
         
         psql -h IP_ADDRESS -p PORT_NUMBER -U USERNAME




### Connect through a PostgreSQL pooler

If you need to install and run the AlloyDB Auth Proxy on the intermediary VM, instead of an external client, then you can enable secure connections to it by pairing it with a _protocol-aware proxy_ , also known as a _pooler_. Popular open-source poolers for PostgreSQL include [Pgpool-II](https://pgpool.net/) and [PgBouncer](https://www.pgbouncer.org/).

In this solution, you run both the AlloyDB Auth Proxy and the pooler on the intermediary VM. Your client or application can then securely connect directly to the pooler over SSL, without the need to run any additional services. The pooler takes care of passing PostgreSQL queries along to your AlloyDB cluster through the Auth Proxy.

Because every instance within an AlloyDB cluster has a separate internal IP address, each proxy service can communicate with only one specific instance: either the primary instance, the stand-by, or a read pool. Therefore, you need to run a separate pooler service, with an appropriately configured SSL certificate, for every instance in the cluster.

## Connect through Cloud VPN or Cloud Interconnect

For production work requiring high availability (HA), we recommend the use of a Google Cloud [Network Connectivity](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product) product: either [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn) or [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect), depending upon your external service's needs and network topology. You then configure [Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview) to advertise the appropriate routes.

While using a Network Connectivity product is a more involved process than setting up an intermediary VM, this approach shifts the burdens of uptime and availability from you to Google. In particular, HA VPN offers 99.99% SLA, making it appropriate for production environments.

Network Connectivity solutions also free you from the need to maintain a separate, secure VM as part of your application, avoiding the single-point-of-failure risks inherent with that approach.

To start learning more about these solutions, see [Choosing a Network Connectivity product](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product).

## What's next

  * Learn more about [Private services access and on-premises connectivity](https://docs.cloud.google.com/vpc/docs/private-services-access#on-premises-connectivity) in Google Cloud VPC networks.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
