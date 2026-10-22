---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/resolve-domain-names/
title: Resolve domain names or hostnames \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:10.010420+00:00
---

# Resolve domain names or hostnames  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/resolve-domain-names/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Resolve domain names or hostnames Stay organized with collections  Save and categorize content based on your preferences. 

DNS resolution is available in private instances running in Cloud Data Fusion version 6.7.0 or later. It lets you use hostnames or domain names for sources and sinks when you design your pipeline in a private Cloud Data Fusion instance so that you don't have to change the pipeline definition during failover.

Without it, you use hard-coded IP addresses, which are problematic when the addresses change in the event of a failover in highly-available deployments. DNS resolution is recommended when you design a pipeline in a private instance and want to retrieve schema, run previews, wrangle, and test connections.

**Note:** Internal IP address resolution is also available with VPC Peering in all Cloud Data Fusion versions.

For more information, see [DNS resolution in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/networking#dns-resolution).

## Before you begin

### Create a private instance

Create a private instance in Cloud Data Fusion and set up a VPC network or shared VPC network in the instance with the following steps.

  1. [Create a private Cloud Data Fusion instance](https://docs.cloud.google.com/data-fusion/docs/how-to/create-private-ip). When you create the instance, choose the following options:

     1. Choose version 6.7.0 or later.
     2. In the **Network** field, choose the appropriate associated network for the private connection.
     3. Enter any other instance details and click **Create**. For information about all fields, see [Create a private Cloud Data Fusion instance](https://docs.cloud.google.com/data-fusion/docs/how-to/create-private-ip).
  2. [Set up VPC Network Peering](https://docs.cloud.google.com/data-fusion/docs/how-to/create-private-ip#set-up-vpc-peering).

Cloud Data Fusion uses VPC Network Peering to establish network connectivity to your VPC or shared VPC network. This lets Cloud Data Fusion access resources on your network through internal IP addresses.

When you set it up, do the following:

     1. Enter a **Name** for your peering connection.
     2. For **Your VPC network** , choose the network where you created your Cloud Data Fusion instance.
     3. For **Peered VPC network** , choose **In another project**.
     4. For **Project ID** , enter the [tenant project ID](https://docs.cloud.google.com/data-fusion/docs/how-to/create-private-ip#find_your_tenant_project_ID).
     5. For **VPC network name** , enter `INSTANCE_REGION-INSTANCE_ID`.

Replace the following:

        * `INSTANCE_REGION`: the region in which you created your Cloud Data Fusion instance.
        * `INSTANCE_ID`: the ID of the Cloud Data Fusion instance.
     6. For **Exchange custom routes** , click **Export custom routes**. This allows for exchanging any custom routes defined in your VPC network with the tenant VPC network.

     7. Click **Create**.

If the VPC Network Peering is successfully set up, the **Status** on the VPC network details page is **Active**.

**Note:** Create a firewall rule on your VPC network that allows for incoming SSH connections from the IP address range you specified when you created the private Cloud Data Fusion instance.



### Create a managed private DNS zone

To resolve domain names in Cloud Data Fusion, create a new managed private DNS zone in the same VPC network or shared VPC network that was used for VPC network peering. For more information, see [Create a private zone](https://docs.cloud.google.com/dns/docs/zones#create-private-zone).

### Console

To create a private managed DNS zone, do the following:

  1. In the Google Cloud console, go to the **Create a DNS zone** page. 

[Go to Create a DNS zone](https://console.cloud.google.com/net-services/dns/zones/new/create)

  2. For **Zone name** , enter a name.
  3. For **Zone type** , click **Private**.
  4. For **DNS name** , enter a domain name.
  5. For **Options** , click **Default (private)**.
  6. For **Networks** , select the VPC network or shared VPC network that was used for VPC Network Peering.
  7. Click **Create**. 



### Create a record set in the DNS zone

Create the record set in the DNS zone that has the internal IP addresses to resolve when you design your pipeline. For more information, see [Add a record](https://docs.cloud.google.com/dns/docs/records#add_a_record).

### Console

To create the record set, do the following:

  1. In the Google Cloud console, go to the **Cloud DNS** page.

[Go to Cloud DNS](https://console.cloud.google.com/net-services/dns)

  2. Click the zone for which you want to create a resource record set.

  3. On the **Zone details** page, click **Add Standard**.

  4. For **DNS name** , enter a domain name that must be resolved during design time.

  5. Enter the record type details. For the IPv4 address, provide the internal IP address for the sink or source to be used in the pipeline. For more information about record types, see [Add a record](https://docs.cloud.google.com/dns/docs/records#add_a_record).

  6. Click **Create**.




## Add DNS Peering in an instance

### Console

To create DNS peering in the Google Cloud console, do the following:

  1. Open your instance.

     1. In the Google Cloud console, go to the Cloud Data Fusion page.

     2. Click **Instances** , and then click the instance's name to go to the **Instance details** page.

[Go to Instances](https://console.cloud.google.com/data-fusion/locations/-/instances)

  2. Click **Add DNS peering**.

The **Add DNS peering** dialog opens.

  3. For **DNS peering ID** , enter a name.

  4. For **Domain** , enter the domain name that you used for creating the private DNS zone.

  5. For the **Target project** , select the project name where the private DNS zone was created.

  6. For the **Network** , select the VPC network name where the private DNS zone was created.

  7. Click **Save** to create the DNS peering.




### REST API

To resolve domain and hostnames with the Cloud Data Fusion DNS Peering API, call its [`create()`](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.instances.dnsPeerings/create) method.

For more information and methods, see the Cloud Data Fusion [DNS Peering API reference](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.instances.dnsPeerings).

## DNS resolution in shared VPC networks

To create the Cloud DNS private zones in a [shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) network, create a [private zone](https://docs.cloud.google.com/vpc/docs/shared-vpc#shared_vpc_and_cloud_dns_private_zones) in the host project and authorize access to the zone for the shared VPC network or set up the zone in a service project using [cross-project binding](https://docs.cloud.google.com/dns/docs/zones/cross-project-binding). For more information, see [Best practices for Cloud DNS private zones](https://docs.cloud.google.com/dns/docs/best-practices#best_practices_for_private_zones).

### Required roles for shared VPC networks

To ensure that the Cloud Data Fusion Service Account has the necessary permissions to create a DNS peering in a shared VPC network, ask your administrator to grant the [DNS Peer ](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.peer) (`roles/dns.peer`) IAM role to the Cloud Data Fusion Service Account on the shared VPC host project. **Important:** You must grant this role to the Cloud Data Fusion Service Account, _not_ to your user account. Failure to grant the role to the correct principal might result in permission errors.  For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

Your administrator might also be able to give the Cloud Data Fusion Service Account the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information, see [Granting access to the required service accounts](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#granting-console).

## What's next

  * Learn more about [Networking in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/networking).
  * Refer to the [Cloud Data Fusion API](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.instances.dnsPeerings).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
