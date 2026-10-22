---
url: https://docs.cloud.google.com/dns/docs/policies/
title: Configure DNS server policies \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:12:31.896974+00:00
---

# Configure DNS server policies  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Guides ](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name)



Send feedback 

#  Configure DNS server policies Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure DNS server policies and use them with Virtual Private Cloud (VPC) networks. Before you use this page, review the [DNS server policies](https://docs.cloud.google.com/dns/docs/server-policies-overview) overview.

## Before you begin

The Cloud DNS API requires that you create a Google Cloud project and enable the Cloud DNS API.

If you are creating an application that uses the REST API, you must also create an OAuth 2.0 client ID.

  1. If you don't already have one, [sign up for a Google Account](https://accounts.google.com/SignUp). 
  2. [ Enable the Cloud DNS API in the Google Cloud console](https://console.cloud.google.com/start/api?id=dns&credential=client_key). You can choose an existing Compute Engine or App Engine project, or you can create a new project. 
  3. If you need to make requests to the REST API, you need to create an OAuth 2.0 ID. See [Setting up OAuth 2.0](https://support.google.com/cloud/answer/6158849). 
  4. In the project, note the following information that you need to input in later steps: 
     * The client ID (`xxxxxx.apps.googleusercontent.com`). 
     * The project ID that you want to use. You can find the ID at the top of the **Overview** page in the Google Cloud console. You can also ask your user to provide the project name that they want to use in your app. 



If you have not run the Google Cloud CLI previously, you must run the following command to specify the project name and authenticate with the Google Cloud console:
    
    
    gcloud auth login
    

To choose a different project than one you have chosen previously, specify the `--project` option at the command line.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `dns.policies.create` to create a DNS server policy
  * `dns.policies.delete` to delete a DNS server policy
  * `dns.policies.get` to fetch the current configuration of a DNS server policy
  * `dns.policies.list` to list all DNS server policies associated with a project
  * `dns.policies.update` to update a DNS server policy
  * `dns.managedZones.list` to list managed zones



**Roles**

  * DNS Administrator (`roles/dns.admin`)



## Create DNS server policies

Each DNS server policy object can define any of the following server policies:

  * An [inbound DNS server policy](https://docs.cloud.google.com/dns/docs/server-policies-overview#dns-server-policy-in), enabling inbound forwarding
  * An [outbound DNS server policy](https://docs.cloud.google.com/dns/docs/server-policies-overview#dns-server-policy-out), specifying one or more alternative name servers
  * Both an inbound and an outbound DNS server policy
  * A [DNS64 server policy](https://docs.cloud.google.com/dns/docs/configure-dns64)



Each VPC network can reference no more than one DNS server policy. If you need to define both inbound and outbound forwarding for a VPC network, create one policy that defines both an inbound and an outbound policy. You can't configure DNS64 with an inbound DNS server policy.

### Create an inbound DNS server policy

To create an inbound DNS server policy, follow these instructions. Cloud DNS creates a set of _inbound forwarder IP addresses_ from the primary IPv4 address ranges of subnets in each VPC network to which the policy applies. After you create your policy, you can list the entry points that Cloud DNS creates.

**Important:** For important details about how inbound server entry points associate DNS queries with a VPC network and region, carefully review the [Inbound server policies](https://docs.cloud.google.com/dns/docs/server-policies-overview#dns-server-policy-in) section of the **Cloud DNS server policies** page.

###  Console 

  1. In the Google Cloud console, open the **Cloud DNS server policies** page.

[Go to Cloud DNS server policies](https://console.cloud.google.com/networking/dns/policies)

  2. Click **Create policy**.

  3. In the **Name** field, enter the name of the inbound DNS server policy that you want to create, such as `inbound-dns-server-policy`.

  4. In the **Inbound query forwarding** section, select **On**.

  5. You can optionally enable DNS64 to enable communication between IPv6-only workloads and IPv4-only destinations. See [Configure DNS64](https://docs.cloud.google.com/dns/docs/configure-dns64) for more information.

  6. You can optionally enable private DNS logs in the **Logs** section, however, this can increase your costs in Cloud Logging.

  7. In the **Networks** list, select VPC networks that you want to bind to this DNS server policy.

A network can only be bound to a single policy. If you can't select a network from the list, it's being used by another policy. To see what network is being used by a policy, view the **In use by** column on the **DNS server policies** page.

  8. Click **Create**.




###  gcloud 

To create an inbound DNS server policy, run the [`dns policies create`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/policies/create) command:
    
    
    gcloud dns policies create NAME \
        --description="DESCRIPTION" \
        --networks="VPC_NETWORK_LIST" \
        --enable-inbound-forwarding
    

Replace the following:

  * `NAME`: a name for the policy
  * `DESCRIPTION`: a description for the policy
  * `VPC_NETWORK_LIST`: a comma-delimited list of VPC networks that the DNS server policy must bind to



###  Terraform 
    
    
    resource "google_dns_policy" "default" {
      name                      = "example-inbound-policy"
      enable_inbound_forwarding = true
    
      networks {
        network_url = google_compute_network.default.id
      }
    }
    
    resource "google_compute_network" "default" {
      name                    = "network"
      auto_create_subnetworks = false
    }

### Create an outbound DNS server policy

To specify a list of alternative name servers for a VPC network, you can create an outbound DNS server policy.

**Important:** For important details about how use of alternative name servers affects VPC network-scoped response policies, VPC network-scoped private zones, and Compute Engine internal DNS, carefully review the [Outbound server policies](https://docs.cloud.google.com/dns/docs/server-policies-overview#dns-server-policy-out) section of the "DNS server policies overview" page. Also review [Alternative name server types, routing methods, and addresses](https://docs.cloud.google.com/dns/docs/server-policies-overview#altns-targets) and [Alternative name server network requirements](https://docs.cloud.google.com/dns/docs/server-policies-overview#altns-net-req).

###  Console 

  1. In the Google Cloud console, open the **Cloud DNS server policies** page.

[Go to Cloud DNS server policies](https://console.cloud.google.com/networking/dns/policies)

  2. Click **Create policy**.

  3. In the **Name** field, enter the name of the outbound DNS server policy that you want to create, such as `outbound-dns-server-policy`.

  4. In the **Inbound query forwarding** section, select **Off**.

  5. You can optionally enable private DNS logs in the **Logs** section, however, this can increase your costs in Cloud Logging.

  6. In the **Alternative DNS servers (Optional)** section, click **Add item** , and enter the IP address of your outbound DNS servers in the **IP Address** field.

     * Select the **Private forwarding** checkbox if you want to force private routing to outbound DNS servers.
  7. In the **Networks** list, select VPC networks that you want to bind to this DNS server policy.

  8. Click **Create**.




###  gcloud 

To create an outbound DNS server policy, run the [`dns policies create`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/policies/create) command:
    
    
    gcloud dns policies create NAME \
        --description="DESCRIPTION" \
        --networks="VPC_NETWORK_LIST" \
        --alternative-name-servers="ALTERNATIVE_NAMESERVER_LIST" \
        --private-alternative-name-servers="PRIVATE_ALTERNATIVE_NAMESERVER_LIST"
    

Replace the following:

  * `NAME`: a name for the policy
  * `DESCRIPTION`: a description for the policy
  * `VPC_NETWORK_LIST`: a comma-delimited list of VPC networks that query the alternative name servers
  * `ALTERNATIVE_NAMESERVER_LIST`: a comma-delimited list of IP addresses that you can use as alternative name servers
  * `PRIVATE_ALTERNATIVE_NAMESERVER_LIST`: a comma-delimited list of IP addresses that you can use as alternative name servers, accessed by using private routing



###  Terraform 
    
    
    resource "google_dns_policy" "default" {
      name = "example-outbound-policy"
    
      alternative_name_server_config {
        target_name_servers {
          ipv4_address    = "172.16.1.10"
          forwarding_path = "private"
        }
        target_name_servers {
          ipv4_address = "172.16.1.20"
        }
      }
    
      networks {
        network_url = google_compute_network.default.id
      }
    }
    
    resource "google_compute_network" "default" {
      name                    = "network"
      auto_create_subnetworks = false
    }

### Create a DNS server policy for both inbound and outbound forwarding

###  Console 

  1. In the Google Cloud console, open the **Cloud DNS server policies** page.

[Go to Cloud DNS server policies](https://console.cloud.google.com/networking/dns/policies)

  2. Click **Create policy**.

  3. In the **Name** field, enter the name of the inbound DNS server policy that you want to create, such as `inbound-outbound-dns-server-policy`.

  4. In the **Inbound query forwarding** section, select **On**.

  5. You can optionally enable private DNS logs in the **Logs** section, however, this can increase your costs in Cloud Logging.

  6. In the **Alternative DNS servers (Optional)** section, click **Add item** , and enter the IP address of your outbound DNS servers in the **IP Address** field.

     * Select **Private forwarding** if you want to force private routing to outbound DNS servers.
  7. In the **Networks** list, select VPC networks that you want to bind to this DNS server policy.

  8. Click **Create**.




###  gcloud 

To create a DNS server policy for both inbound and outbound forwarding, run the [`dns policies create`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/policies/create) command:
    
    
    gcloud dns policies create NAME \
        --description="DESCRIPTION" \
        --networks="VPC_NETWORK_LIST" \
        --alternative-name-servers="ALTERNATIVE_NAMESERVER_LIST" \
        --private-alternative-name-servers="PRIVATE_ALTERNATIVE_NAMESERVER_LIST" \
        --enable-inbound-forwarding
    

Replace the following:

  * `NAME`: a name for the policy
  * `DESCRIPTION`: a description for the policy
  * `VPC_NETWORK_LIST`: a comma-delimited list of VPC networks where inbound forwarding addresses must be created and that must query the alternative name servers
  * `ALTERNATIVE_NAMESERVER_LIST`: a comma-delimited list of IP addresses that you can use as alternative name servers
  * `PRIVATE_ALTERNATIVE_NAMESERVER_LIST`: a comma-delimited list of IP addresses that you can use as alternative name servers, accessed by using private routing.



###  Terraform 
    
    
    resource "google_dns_policy" "example_policy" {
      name                      = "example-policy"
      enable_inbound_forwarding = true
    
      enable_logging = true
    
      alternative_name_server_config {
        target_name_servers {
          ipv4_address    = "172.16.1.10"
          forwarding_path = "private"
        }
        target_name_servers {
          ipv4_address = "172.16.1.20"
        }
      }
    
      networks {
        network_url = google_compute_network.network_1.id
      }
      networks {
        network_url = google_compute_network.network_2.id
      }
    }
    
    resource "google_compute_network" "network_1" {
      name                    = "network-1"
      auto_create_subnetworks = false
    }
    
    resource "google_compute_network" "network_2" {
      name                    = "network-2"
      auto_create_subnetworks = false
    }

### List inbound forwarder entry points

When an inbound DNS server policy applies to a VPC network, Cloud DNS creates a set of regional internal IP addresses that serve as destinations to which your on-premises systems or name resolvers can send DNS queries. These addresses serve as entry points to the name resolution order of your VPC network.

**Note:** If you disable and then re-enable inbound forwarding or if you delete and recreate a VPC network, the entry point IP addresses change.

Google Cloud firewall rules do _not_ apply to the regional internal addresses that act as entry points for inbound forwarders. Cloud DNS accepts TCP and UDP traffic on port `53` automatically.

Each inbound forwarder accepts and receives queries from Cloud VPN tunnels or Cloud Interconnect attachments (VLANs) in the same region as the regional internal IP address. VM instances can access the inbound forwarder through any of the internal IP addresses in the same VPC network. To access inbound forwarding, either the network interface must have an external IP address or a subnet of the NIC must have Private Google Access enabled.

###  Console 

View the list of inbound forwarder entry points for a policy:

  1. In the Google Cloud console, open the **Cloud DNS server policies** page.

[Go to Cloud DNS server policies](https://console.cloud.google.com/networking/dns/policies)

  2. Click the name of the policy.

  3. On the **Policy details** page, click the **In use by** tab.




Each network bound to the policy lists the **Inbound query forwarding IP** addresses.

###  gcloud 

To list the set of regional internal IP addresses that serve as entry points for all inbound forwarding policies, run the [`compute addresses list`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/list) command:
    
    
    gcloud compute addresses list \
        --filter='purpose = "DNS_RESOLVER"' \
        --format='csv(address, region, subnetwork)'
    

## Update DNS policies

The following sections provide information about changing VPC networks and enabling or disabling inbound forwarding.

### Change VPC networks

The following list describes what happens when you change the list of VPC networks to which a DNS policy applies:

  * If the policy specifies an inbound policy, entry points for inbound forwarders are created in VPC networks as needed.
  * If the policy specifies an outbound policy, the name resolution order of each VPC network is updated to include the specified alternative name servers.




###  Console 

  1. In the Google Cloud console, open the **Cloud DNS server policies** page.

[Go to Cloud DNS server policies](https://console.cloud.google.com/networking/dns/policies)

  2. Click the name of the policy you want to change.

  3. Click edit**Edit policy**.

  4. In the **Networks** list, select or clear the checkboxes next to the VPC networks.

  5. Click **Save**.




###  gcloud 

To modify the list of networks to which a DNS server policy applies, run the [`dns policies update`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/policies/update) command:
    
    
    gcloud dns policies update NAME \
        --networks="VPC_NETWORK_LIST"
    

Replace the following:

  * `NAME`: a name for the policy
  * `VPC_NETWORK_LIST`: a comma-delimited list of VPC networks to which the policy applies; the list of VPC networks that you specify replaces the previous list



### Enable or disable inbound forwarding

You can enable inbound forwarding for a DNS server policy that defines only an outbound policy (alternative name server). You can also disable inbound forwarding for an existing DNS policy.

###  Console 

Enable inbound forwarding for a DNS server policy:

  1. In the Google Cloud console, open the **Cloud DNS server policies** page.

[Go to Cloud DNS server policies](https://console.cloud.google.com/networking/dns/policies)

  2. Click the name of the policy you want to change.

  3. Click edit**Edit policy**.

  4. In the **Inbound query forwarding** section, select **On**.

  5. Click **Save**.




Disable inbound forwarding for a DNS server policy:

  1. Open the **Cloud DNS server policies** page.
  2. Click the name of the policy you want to change.
  3. Click edit**Edit policy**.
  4. In the **Inbound query forwarding** section, select **Off**.
  5. Click **Save**.



###  gcloud 

To enable inbound forwarding for a DNS server policy, run the [`dns policies update`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/policies/update) command:
    
    
    gcloud dns policies update NAME \
        --enable-inbound-forwarding
    

To disable inbound forwarding for a DNS server policy, specify the`--no-enable-inbound-forwarding` flag:
    
    
    gcloud dns policies update NAME \
        --no-enable-inbound-forwarding
    

Replace `NAME` with the name of the policy.

## List DNS policies

###  Console 

  1. In the Google Cloud console, open the **Cloud DNS server policies** page.

[Go to Cloud DNS server policies](https://console.cloud.google.com/networking/dns/policies)

  2. Any DNS server policy created in your project is listed.




###  gcloud 

To list DNS server policies in your project, run the [`dns policies list`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/policies/list) command:
    
    
    gcloud dns policies list
    

## Delete a DNS policy

###  Console 

To delete a DNS server policy, it must not be bound to any network. Update your policy to remove all networks before deleting the policy.

  1. In the Google Cloud console, open the **Cloud DNS server policies** page.

[Go to Cloud DNS server policies](https://console.cloud.google.com/networking/dns/policies)

  2. Click delete**Delete** by the name of the policy you want to delete.




###  gcloud 

To delete a DNS server policy, run the [`dns policies delete`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/policies/delete) command:
    
    
    gcloud dns policies delete NAME
    

Replace `NAME` with the name of the policy to delete.

## What's next

  * To find solutions for common issues that you might encounter when using Cloud DNS, see [Troubleshooting](https://docs.cloud.google.com/dns/docs/troubleshooting).
  * To get an overview of Cloud DNS, see [Cloud DNS overview](https://docs.cloud.google.com/dns/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
