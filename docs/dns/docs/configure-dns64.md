---
url: https://docs.cloud.google.com/dns/docs/configure-dns64/
title: Configure DNS64 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:20.368299+00:00
---

# Configure DNS64  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/configure-dns64/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Guides ](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name)



Send feedback 

#  Configure DNS64 Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure and use DNS64 server policies with Virtual Private Cloud (VPC) networks.

## Before you begin

  * DNS64 server policies don't apply to dual-stack virtual machine (VM) instances, IPv4-only VM instances, serverless workloads, or requests sent to endpoints created by an [inbound DNS server policy](https://docs.cloud.google.com/dns/docs/server-policies-overview#dns-server-policy-in).
  * Make sure that you have the required permissions to create a DNS64 server policy.



#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `dns.policies.create` to create a DNS64 server policy
  * `dns.policies.delete` to delete a DNS64 server policy
  * `dns.policies.get` to fetch the current configuration of a DNS64 server policy
  * `dns.policies.list` to list all DNS server policies associated with a project
  * `dns.policies.update` to update a DNS64 server policy
  * `dns.managedZones.list` to list managed zones



**Roles**

  * DNS Administrator (`roles/dns.admin`)



## Create a DNS64 server policy

Create a DNS64 server policy to enable communication between IPv6-only workloads and IPv4-only destinations.

After you create a DNS64 server policy, the following occurs when an IPv6 (`AAAA`) record is queried:

  * If an `AAAA` DNS record exists, the DNS server returns an IPv6 address. Your workload connects by using that IPv6 address.
  * If no `AAAA` DNS record exists, Cloud DNS looks for `A` records. Cloud DNS then creates IPv6 addresses for the IPv4 addresses in the `A` record, by using the `64:ff9b::/96` IPv6 prefix.



To create a DNS64 server policy, follow these steps.

###  gcloud 

To create a DNS64 server policy, run the [`gcloud dns policies create` command](https://docs.cloud.google.com/sdk/gcloud/reference/dns/policies/create):
    
    
    gcloud dns policies create NAME \
        --description=DESCRIPTION \
        --networks=VPC_NETWORK_LIST \
        --enable-dns64-all-queries
    

Replace the following:

  * `NAME`: a name for the policy
  * `DESCRIPTION`: a description for the policy
  * `VPC_NETWORK_LIST`: a comma-delimited list of VPC networks that the DNS server policy binds to



###  Terraform 
    
    
    resource "google_dns_policy" "default" {
      name = "NAME"
    
      dns64_config {
        scope {
          all_queries = true
        }
      }
    
      alternative_name_server_config {
        target_name_servers {
          ipv4_address    = "PRIVATE_IP_ADDRESS"
          forwarding_path = "private"
        }
        target_name_servers {
          ipv4_address = "PUBLIC_IP_ADDRESS"
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
    

Replace the following:

  * `NAME`: a name for the outbound DNS64 policy
  * `PRIVATE_IP_ADDRESS`: the IP address of an alternative name server using a private forwarding path
  * `PUBLIC_IP_ADDRESS`: the IP address of a different alternative name server



###  API 

To create a DNS64 server policy, use the [`policies.create` method](https://docs.cloud.google.com/dns/docs/reference/rest/v1/policies/create):
    
    
    POST https://dns.googleapis.com/dns/v1/projects/PROJECT_ID/policies
    {
      "kind": "dns#policy",
      "networks": [
        {
          "kind": "dns#policyNetwork",
          "networkUrl": "NETWORK_URL"
        }
      ],
      "dns64Config":
        {
            "scope":
            {
              allQueries: true,
            }
        }
      }
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `NETWORK_URL`: the fully qualified URL of the VPC network that your DNS server policy must bind to, formatted as follows: `https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/VPC_NETWORK_NAME`. Specify the network that contains the IPv6-only subnets and instances.



## Verify if a DNS64 server policy is enabled

###  gcloud 

To list all DNS server policies in your project, run the [`dns policies list` command](https://docs.cloud.google.com/sdk/gcloud/reference/dns/policies/list):
    
    
    gcloud dns policies list
    

To get detailed information about a specific DNS64 server policy, run the [`gcloud dns policies describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/dns/policies/describe):
    
    
    gcloud dns policies describe NAME
    

Replace `NAME` with the name of the DNS64 server policy about which you want detailed information.

## Disable a DNS64 server policy

###  gcloud 

To disable a DNS64 server policy, run the [`dns policies update` command](https://docs.cloud.google.com/sdk/gcloud/reference/dns/policies/update):
    
    
    gcloud dns policies update NAME \
        --no-enable-dns64-all-queries
    

Replace `NAME` with the name of the DNS64 server policy that you want to disable.

## What's next

  * To configure NAT64 for Public NAT translation from IPv6 to IPv4 addresses, follow the instructions in [Create a Cloud NAT gateway](https://docs.cloud.google.com/nat/docs/set-up-manage-network-address-translation#create-nat-gateway).
  * To get an overview of DNS server policies, see [DNS server policies](https://docs.cloud.google.com/dns/docs/server-policies-overview).
  * To find solutions for common issues that you might encounter when using Cloud DNS, see [Troubleshoot Cloud DNS](https://docs.cloud.google.com/dns/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
