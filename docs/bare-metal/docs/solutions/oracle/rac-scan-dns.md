---
url: https://docs.cloud.google.com/bare-metal/docs/solutions/oracle/rac-scan-dns/
title: Configure Single Client Access Name with Cloud DNS \u00a0|\u00a0 Bare Metal Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:02.202618+00:00
---

# Configure Single Client Access Name with Cloud DNS  |  Bare Metal Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bare-metal/docs/solutions/oracle/rac-scan-dns/

The availability of Bare Metal Solution is transitioning to a specialized, allowlist-only model. If you are an existing customer, please contact your Google account team to explore the value of migrating to new [Oracle and Google Cloud strategic partnership offerings](https://docs.cloud.google.com/bare-metal/docs/explore-oracle-partnership-offerings). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Bare Metal ](https://docs.cloud.google.com/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/bare-metal/docs/bms-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure Single Client Access Name with Cloud DNS

You can access an Oracle® Real Application Clusters (RAC) cluster via a highly-available DNS name provided by [Cloud DNS](https://cloud.google.com/dns). This is achieved by pointing the DNS entry at a RAC [Single Client Access Name (SCAN)](https://www.oracle.com/jp/a/tech/docs/technical-resources/single-client-access-name.pdf), which stays persistent as cluster topology changes.

**Note:** Customers are responsible for procuring licenses for the Oracle workloads they choose to run on Bare Metal Solution, and customers are responsible for complying with those licenses. Google does not provide licenses for Oracle workloads.

## Before you begin

You need access to the following resources and services to complete this guide:

  * A [configured Bare Metal Solution server](https://docs.cloud.google.com/bare-metal/docs/bms-setup) that connects to a Google [Virtual Private Cloud (VPC)](https://cloud.google.com/vpc) via a [Partner Cloud Interconnect](https://cloud.google.com/network-connectivity/docs/interconnect).
  * A configured RAC cluster on the Bare Metal Solution server, with a SCAN listener active on each node.
  * [Cloud DNS](https://cloud.google.com/dns).



## System architecture

The following diagram shows the system architecture used in this guide:

![A system architecture diagram of Google Cloud connected to an Oracle RAC cluster](https://docs.cloud.google.com/static/bare-metal/docs/solutions/oracle/images/rac-scan-architecture.svg)

## Set up Cloud DNS to point to your RAC cluster

To set up single DNS name access to your RAC cluster, complete the following steps:

  1. If you haven't run the [Google Cloud CLI](https://cloud.google.com/sdk/gcloud) previously, you must run the following command to specify your project name and authenticate with the Google Cloud console:
         
         gcloud auth login
         

  2. [Enable the Cloud DNS API](https://console.cloud.google.com/apis/enableflow?apiid=dns&credential=client_key) for your Google Cloud project.

  3. [Create an inbound server policy in Cloud DNS](https://cloud.google.com/dns/docs/policies#create-in) for the VPC connected to your Bare Metal Solution servers. This makes sure your Bare Metal Solution servers can communicate with Cloud DNS.

  4. [List the inbound forwarder entry points](https://cloud.google.com/dns/docs/policies#list-in-entrypoints) to determine the correct entry point IP address for each Bare Metal Solution server.

  5. Configure each Bare Metal Solution server to use the IP address from the previous step for name resolution. The steps involved are specific to your operating system.

For example, to configure name resolution in Red Hat Enterprise Linux 8:

     1. [Disable NetworkManager DNS processing](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_and_managing_networking/manually-configuring-the-etc-resolv-conf-file_configuring-and-managing-networking).
     2. Add the following line to `/etc/resolv.conf`, replacing ENTRY_POINT_IP_ADDRESS with the entry point IP address:
            
            nameserver ENTRY_POINT_IP_ADDRESS
            

  6. Configure [Cloud DNS for Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#config-domain).

  7. Log into a Bare Metal Solution server that hosts a RAC database as the database user that was configured at install time.

  8. If you haven't set the `ORACLE_HOME` and `PATH` environment variable in your shell profile, set it now so you can connect to your database.

  9. Request the SCAN configuration with `srvctl` to find the SCAN name:
         
         srvctl config scan
         

You should receive a response similar to the following example:
         
         SCAN name: cluster01-scan.mycompany.internal, Network: 1
         Subnet IPv4: /192.168.1.0/255.255.255.0/bond0.118, static
         Subnet IPv6:
         SCAN 1 IPv4 VIP: 192.168.1.30
         SCAN VIP is enabled
         SCAN 2 IPv4 VIP: 192.168.1.31
         SCAN VIP is enabled
         SCAN 3 IPv4 VIP: 192.168.1.32
         SCAN VIP is enabled
         

The SCAN name in the previous response is `cluster01-scan.mycompany.internal`.

  10. [Create a private zone in Cloud DNS](https://docs.cloud.google.com/dns/docs/zones#create-private-zone), providing the following details:

     * A new zone name, to identify the zone in configuration commands.
     * A description for your zone, to better define its purpose.
     * The DNS name suffix for your zone, such as `mycompany.internal`. This should match the suffix of the SCAN name returned in the previous `srvctl config scan` command.
     * The VPC network that the private DNS zone should be visible to.
  11. [Add a record](https://docs.cloud.google.com/dns/docs/records#adding_a_record) to the previous zone, providing the following details:

     * The name of the zone you created in the previous step.
     * The full DNS name. In this guide, that's `cluster01-scan.mycompany.internal`.
     * The time to live (TTL). This is how long the DNS record is cached before it's refreshed.
     * The resource record type. For SCAN, this is an `A` record.
     * The SCAN IPs returned in the previous `srvctl config scan` command.

Repeat this process for any additional names that need to be resolved.

  12. On the Bare Metal Solution server, validate that SCAN resolution is working with `nslookup`:
         
         nslookup cluster01-scan.mycompany.internal
         

If successful, you should receive a response similar to the following example:
         
         Server:  10.158.0.3
         Address: 10.158.0.3#53
         
         Name: cluster01-scan.mycompany.internal
         Address: 192.168.1.32
         Name: cluster01-scan.mycompany.internal
         Address: 192.168.1.30
         Name: cluster01-scan.mycompany.internal
         Address: 192.168.1.31
         




You can now access your RAC cluster using a single, highly available, resilient DNS name via Cloud DNS.

Oracle is a registered trademark of Oracle and/or its affiliates.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
