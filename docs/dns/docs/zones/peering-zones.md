---
url: https://docs.cloud.google.com/dns/docs/zones/peering-zones/
title: Create a peering zone \u00a0|\u00a0 Cloud DNS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:06.914118+00:00
---

# Create a peering zone  |  Cloud DNS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/zones/peering-zones/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Guides ](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name)



Send feedback 

#  Create a peering zone Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions about how to create a peering zone. For detailed background information, see [Peering zones](https://docs.cloud.google.com/dns/docs/zones/zones-overview#peering_zones).

You must be signed in to the Google Cloud console as an Identity and Access Management (IAM) member who has the [DNS Peer role](https://docs.cloud.google.com/dns/docs/access-control#dns.peer) (`roles/dns.peer`) to the project that contains the producer VPC network.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

Permission required in the project with the producer network:

  * `dns.networks.targetWithPeeringZone` to create a peering zone



Permission required in the project where you want to create the new zone:

  * `dns.managedZones.create` to create a managed zone



**Roles**

  * `roles/dns.admin` in both the project with the producer network and the project where you want to create the new zone
  * `roles/dns.peer` in the project that contains the producer VPC network



To create a new managed private peering zone when you need one VPC network (the _consumer network_) to query the VPC name resolution order of another VPC network (the _producer network_), follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **Create a DNS zone** page.

[Go to Create a DNS zone](https://console.cloud.google.com/net-services/dns/zones/new/create)

  2. For the **Zone type** , select **Private**.

  3. Enter a **Zone name** such as `my-new-zone`.

  4. Enter a **DNS name** suffix for the private zone. All records in the zone share this suffix, for example: `example.private`.

  5. Optional: Add a description.

  6. Under **Options** , select **DNS peering**.

  7. Select the networks to which the private zone must be visible.

  8. In **Peer project** , select a peer project.

  9. In **Peer network** , select a peer network.

  10. Click **Create**.




###  gcloud 

**Note:** If the IAM member is signed in to the Google Cloud CLI, or is signed in to the service account selected in step 1, you can skip steps 1 and 2. This service account must have at least the [DNS Peer role](https://docs.cloud.google.com/dns/docs/access-control#dns.peer) (`roles/dns.peer`) to the project that contains the producer VPC network.

  1. In the project that contains the consumer VPC network, identify or [create a service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating).

  2. Grant the [DNS Peer role](https://docs.cloud.google.com/dns/docs/access-control#dns.peer) (`roles/dns.peer`) to the service account (from the previous step) in the project that contains the producer VPC network.
         
         gcloud projects add-iam-policy-binding PRODUCER_PROJECT_ID \
            --member=SERVICE_ACCOUNT \
            --role=roles/dns.peer
         

Replace the following:

     * `PRODUCER_PROJECT_ID`: the ID of the project that contains the producer VPC network
     * `SERVICE_ACCOUNT`: the service account in the project that contains the consumer VPC network that was identified or created in step 1
  3. In the project that contains the consumer VPC network, grant the [DNS Administrator role](https://docs.cloud.google.com/dns/docs/access-control#dns.admin) (`roles/dns.admin`) to the service account and create a new managed private peering zone by running the [`dns managed-zones create`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/managed-zones/create) command:
         
         gcloud dns managed-zones create NAME \
           --description=DESCRIPTION \
           --dns-name=DNS_SUFFIX \
           --networks=CONSUMER_VPC_NETWORK \
           --account=SERVICE_ACCOUNT \
           --target-network=PRODUCER_VPC_NETWORK \
           --target-project=PRODUCER_PROJECT_ID \
           --visibility=private
         

Replace the following:

     * `NAME`: a name for your zone
     * `DESCRIPTION`: a description for your zone
     * `DNS_SUFFIX`: the DNS suffix for your zone, such as `example.com`
     * `CONSUMER_VPC_NETWORK`: the name of the consumer VPC network
     * `SERVICE_ACCOUNT`: the service account in the project that contains the consumer VPC network, identified in step 1 **Note:** If you don't add the service account in the project that contains the consumer VPC network, the gcloud CLI uses the currently active IAM member, as indicated by `gcloud auth list`.
     * `PRODUCER_VPC_NETWORK`: the name of the producer VPC network
     * `PRODUCER_PROJECT_ID`: the ID of the project that contains the producer VPC network



###  Terraform 
    
    
    resource "random_id" "zone_suffix" {
      byte_length = 8
    }
    
    resource "google_dns_managed_zone" "peering_zone" {
      name        = "peering-zone-${random_id.zone_suffix.hex}"
      dns_name    = "peering.example.com."
      description = "Example private DNS peering zone"
    
      visibility = "private"
    
      private_visibility_config {
        networks {
          network_url = google_compute_network.network_source.id
        }
      }
    
      peering_config {
        target_network {
          network_url = google_compute_network.network_target.id
        }
      }
    }
    
    resource "google_compute_network" "network_source" {
      name                    = "network-source"
      auto_create_subnetworks = false
    }
    
    resource "google_compute_network" "network_target" {
      name                    = "network-target"
      auto_create_subnetworks = false
    }

**Note:** You cannot add records to a peering zone directly; the data comes from the producer VPC network according to its [VPC name resolution order](https://docs.cloud.google.com/dns/docs/vpc-name-res-order).

## What's next

  * To work with managed zones, see [Create, modify, and delete zones](https://docs.cloud.google.com/dns/docs/zones).
  * To find solutions for common issues that you might encounter when using Cloud DNS, see [Troubleshooting](https://docs.cloud.google.com/dns/docs/troubleshooting).
  * To get an overview of Cloud DNS, see [Cloud DNS overview](https://docs.cloud.google.com/dns/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
