---
url: https://docs.cloud.google.com/dns/docs/zones/
title: Create, modify, and delete zones \u00a0|\u00a0 Cloud DNS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:42:30.583296+00:00
---

# Create, modify, and delete zones  |  Cloud DNS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/zones/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Guides ](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name)



Send feedback 

#  Create, modify, and delete zones Stay organized with collections  Save and categorize content based on your preferences. 

This page provides directions for creating, updating, listing, and deleting Cloud DNS managed zones. Before you use this page, familiarize yourself with the [Cloud DNS overview](https://docs.cloud.google.com/dns/docs/overview) and [Key terms](https://docs.cloud.google.com/dns/docs/key-terms).

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `dns.managedZones.create` to create a managed zone
  * `dns.managedZones.list` to list managed zones
  * `dns.networks.bindPrivateDNSZone`
  * `dns.networks.targetWithPeeringZone`
  * `dns.gkeClusters.bindPrivateDNSZone`
  * `dns.managedZones.update`
  * `dns.managedZones.list`
  * `dns.managedZones.patch`
  * `dns.activePeeringZones.getZoneInfo`
  * `dns.activePeeringZones.list`
  * `dns.activePeeringZones.deactivate`



**Roles**

  * `roles/dns.admin`
  * `roles/dns.peer`



## Before you begin

The Cloud DNS API requires that you create a Cloud DNS project and enable the Cloud DNS API.

If you are creating an application that uses the REST API, you must also create an OAuth 2.0 client ID.

  1. If you don't already have one, [sign up for a Google Account](https://accounts.google.com/SignUp). 
  2. [ Enable the Cloud DNS API in the Google Cloud console](https://console.cloud.google.com/start/api?id=dns&credential=client_key). You can choose an existing Compute Engine or App Engine project, or you can create a new project. 
  3. If you need to make requests to the REST API, you need to create an OAuth 2.0 ID. See [Setting up OAuth 2.0](https://support.google.com/cloud/answer/6158849). 
  4. In the project, note the following information that you need to input in later steps: 
     * The client ID (`xxxxxx.apps.googleusercontent.com`). 
     * The project ID that you want to use. You can find the ID at the top of the **Overview** page in the Google Cloud console. You can also ask your user to provide the project name that they want to use in your app. 



If you have not run the Google Cloud CLI previously, you must run the following command to specify the project name and authenticate with the Google Cloud console:
    
    
    gcloud auth login
    

If you want to run a `gcloud` command on Google Cloud resources in another project, specify the `--project` option for this command and for the other `gcloud` commands throughout this page.

## Create managed zones

Each managed zone that you create is associated with a [Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects). The following sections describe how to create the type of managed zone that Cloud DNS supports.

### Create a public zone

To create a new managed zone, complete the following steps.

###  Console 

  1. In the Google Cloud console, go to the **Create a DNS zone** page.

[Go to Create a DNS zone](https://console.cloud.google.com/net-services/dns/zones/new/create)

  2. For the **Zone type** , select **Public**.

  3. Enter a **Zone name** such as `my-new-zone`.

  4. Enter a **DNS name** suffix for the zone using a domain name that you own. All records in the zone share this suffix, for example: `example.com`.

  5. Under **DNSSEC** , select **Off** , **On** , or **Transfer**. For more information, see [Enable DNSSEC for existing managed zones](https://docs.cloud.google.com/dns/docs/dnssec-config#enabling).

  6. Click **Create**. The **Zone details** page is displayed.




###  gcloud 

Run the [`dns managed-zones create`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/managed-zones/create) command:
    
    
    gcloud dns managed-zones create NAME \
        --description=DESCRIPTION \
        --dns-name=DNS_SUFFIX \
        --labels=LABELS \
        --visibility=public
    

Replace the following:

  * `NAME`: a name for your zone
  * `DESCRIPTION`: a description for your zone
  * `DNS_SUFFIX`: the DNS suffix for your zone, such as `example.com`
  * `LABELS`: an optional comma-delimited list of key-value pairs such as `dept=marketing` or `project=project1`; for more information, see the [SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/dns/managed-zones/create#--labels)



###  Terraform 
    
    
    resource "google_dns_managed_zone" "example_zone" {
      name        = "example-zone"
      dns_name    = "example-${random_id.rnd.hex}.com."
      description = "Example DNS zone"
      labels = {
        name = "value"
      }
    }
    
    resource "random_id" "rnd" {
      byte_length = 4
    }

###  API 

Send a `POST` request using the [`managedZones.create`](https://docs.cloud.google.com/dns/docs/reference/v1/managedZones/create) method:
    
    
    POST https://dns.googleapis.com/dns/v1/projects/PROJECT_ID/managedZones
    {
      "name": "NAME",
      "description": "DESCRIPTION",
      "dnsName": "DNS_NAME",
      "visibility": "public"
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the managed zone is created
  * `NAME`: a name for your zone
  * `DESCRIPTION`: a description for your zone
  * `DNS_NAME`: the DNS suffix for your zone, such as `example.com`



**Important:** Cloud DNS creates `NS` and `SOA` records for you automatically when you create the zone. Do not change the name of your zone's `NS` record, and do not change the list of name servers that Cloud DNS selects for your zone. 

### Create a private zone

To create a new managed private zone with private DNS records managed by Cloud DNS, complete the following steps. For more information, see [Best practices for Cloud DNS private zones](https://docs.cloud.google.com/dns/docs/best-practices#best_practices_for_private_zones).

###  Console 

  1. In the Google Cloud console, go to the **Create a DNS zone** page.

[Go to Create a DNS zone](https://console.cloud.google.com/net-services/dns/zones/new/create)

  2. For the **Zone type** , select **Private**.

  3. Enter a **Zone name** such as `my-new-zone`.

  4. Enter a **DNS name** suffix for the private zone. All records in the zone share this suffix, for example: `example.private`.

  5. Optional: Add a description.

  6. Under **Options** , select **Default (private)**.

  7. Select the Virtual Private Cloud (VPC) networks to which the private zone must be visible. Only the VPC networks that you select are authorized to query records in the zone.

  8. Click **Create**.




###  gcloud 

Run the [`dns managed-zones create`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/managed-zones/create) command:
    
    
    gcloud dns managed-zones create NAME \
        --description=DESCRIPTION \
        --dns-name=DNS_SUFFIX \
        --networks=VPC_NETWORK_LIST \
        --labels=LABELS \
        --visibility=private
    

Replace the following:

  * `NAME`: a name for your zone
  * `DESCRIPTION`: a description for your zone
  * `DNS_SUFFIX`: the DNS suffix for your zone, such as `example.private`
  * `VPC_NETWORK_LIST`: a comma-delimited list of VPC networks that are authorized to query the zone
  * `LABELS`: an optional comma-delimited list of key-value pairs such as `dept=marketing` or `project=project1`; for more information, see the [SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/dns/managed-zones/create#--labels)



###  Terraform 
    
    
    resource "google_dns_managed_zone" "private_zone" {
      name        = "private-zone"
      dns_name    = "private.example.com."
      description = "Example private DNS zone"
      labels = {
        foo = "bar"
      }
    
      visibility = "private"
    
      private_visibility_config {
        networks {
          network_url = google_compute_network.network_1.id
        }
        networks {
          network_url = google_compute_network.network_2.id
        }
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

###  API 

Send a `POST` request using the [`managedZones.create`](https://docs.cloud.google.com/dns/docs/reference/v1/managedZones/create) method:
    
    
    POST https://dns.googleapis.com/dns/v1/projects/PROJECT_ID/managedZones
    {
    
      "name": "NAME",
      "description": "DESCRIPTION",
      "dnsName": "DNS_NAME",
      "visibility": "private",
      "privateVisibilityConfig": {
        "kind": "dns#managedZonePrivateVisibilityConfig",
        "networks": [
          {
            "kind": "dns#managedZonePrivateVisibilityConfigNetwork",
            "networkUrl": "VPC_NETWORK_1"
          },
          {
            "kind": "dns#managedZonePrivateVisibilityConfigNetwork",
            "networkUrl": "VPC_NETWORK_2"
          },
          ....
        ]
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the managed zone is created
  * `NAME`: a name for your zone
  * `DESCRIPTION`: a description for your zone
  * `DNS_NAME`: the DNS suffix for your zone, such as `example.private`
  * `VPC_NETWORK_1` and `VPC_NETWORK_2`: URLs for VPC networks in the same project that can query records in this zone. You can add multiple VPC networks as indicated. To determine the URL for a VPC network, use the following `gcloud` command, replacing `VPC_NETWORK_NAME` with the network's name:
        
        gcloud compute networks describe VPC_NETWORK_NAME \
         --format="get(selfLink)"
        




### Create a zone with specific IAM permissions

The Identity and Access Management (IAM) permission for individual resource managed zone lets you set up specific read, write, or administrator permissions for different managed zones under the same project.

For instructions about how to create a zone with specific Identity and Access Management (IAM) permissions, see [Create a zone with specific IAM permissions](https://docs.cloud.google.com/dns/docs/zones/iam-per-resource-zones).

### Create a Service Directory DNS zone

You can create a Service Directory zone that allows your Google Cloud-based services to query your Service Directory namespace through DNS.

For detailed instructions about how to create a Service Directory DNS zone, see [Configuring a Service Directory DNS zone](https://docs.cloud.google.com/service-directory/docs/configuring-service-directory-zone).

For instructions about how to use DNS to query your Service Directory, see [Querying using DNS](https://docs.cloud.google.com/service-directory/docs/query-dns).

**Note:** You cannot add records to a Service Directory DNS zone directly; the data comes from the Service Directory service registry.

### Create a managed reverse lookup private zone

A managed reverse lookup zone is a private zone with a special attribute that instructs Cloud DNS to perform a PTR lookup against Compute Engine DNS data. You must set up managed reverse lookup zones for Cloud DNS to correctly resolve non-RFC 1918 PTR records for your virtual machine (VM) instances.

For instructions on how to create a new managed reverse lookup private zone, see [Create a managed reverse lookup zone](https://docs.cloud.google.com/dns/docs/zones/managed-reverse-lookup-zones). 

### Create a forwarding zone

Forwarding zones let you target name servers for specific private zones. For instructions on how to create a new managed private forwarding zone, see [Create a forwarding zone](https://docs.cloud.google.com/dns/docs/zones/forwarding-zones).

### Create a peering zone

DNS peering lets you send requests for records that come from one zone's namespace to another VPC network. For instructions on how to create a peering zone, see [Create a peering zone](https://docs.cloud.google.com/dns/docs/zones/peering-zones).

### Create a cross-project binding zone

Create a managed private zone that can be bound to a network that is owned by a different project within the same organization. For instructions on how to create a cross-project binding zone, see [Cross-project binding zones](https://docs.cloud.google.com/dns/docs/zones/cross-project-binding).

## Update managed zones

Cloud DNS lets you modify certain attributes of your managed public or managed private zone.

### Update public zones

You can change the description or [DNSSEC configuration](https://docs.cloud.google.com/dns/docs/dnssec-config#enabling) of a public zone.

###  Console 

  1. In the Google Cloud console, go to the **Cloud DNS zones** page.

[Go to Cloud DNS zones](https://console.cloud.google.com/networking/dns/zones/)

  2. Click the public zone that you want to update.

  3. Click edit **Edit**.

  4. To change DNSSEC settings, under **DNSSEC** , select **Off** , **On** , or **Transfer**. For more information, see [Enabling DNSSEC for existing managed zones](https://docs.cloud.google.com/dns/docs/dnssec-config#enabling).

**Note:** Before you disable DNSSEC for a managed zone that you still want to use, you must deactivate DNSSEC for your zone at your domain registrar to ensure that DNSSEC-validating resolvers can still resolve names in the zone. For details, see [Disabling DNSSEC for managed zones](https://docs.cloud.google.com/dns/docs/dnssec-config#disabling).
  5. Optional: Update the description.

  6. Click **Save**.




###  gcloud 

Run the [`dns managed-zones update`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/managed-zones/update) command:
    
    
    gcloud dns managed-zones update NAME \
        --description=DESCRIPTION \
        --dnssec-state=STATE
    

Replace the following:

  * `NAME`: a name for your zone
  * `DESCRIPTION`: a description for your zone
  * `STATE`: a DNSSEC setting such as `Off`, `On`, or `Transfer`



### Update private zones

You can modify the VPC networks to which a private zone is visible.

###  Console 

  1. In the Google Cloud console, go to the **Cloud DNS zones** page.

[Go to Cloud DNS zones](https://console.cloud.google.com/networking/dns/zones/)

  2. Click the private zone that you want to update.

  3. Click edit **Edit**.

  4. Select the VPC networks to which the private zone must be visible. Only the selected VPC networks are authorized to query records in the zone.

  5. Click **Save**.




###  gcloud 

Run the [`dns managed-zones update`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/managed-zones/update) command:
    
    
    gcloud dns managed-zones update NAME \
        --description=DESCRIPTION \
        --networks=VPC_NETWORK_LIST
    

Replace the following:

  * `NAME`: a name for your zone
  * `DESCRIPTION`: a description for your zone
  * `VPC_NETWORK_LIST`: a comma-delimited list of VPC networks that are authorized to query the zone



### Update labels

To add new, change existing, remove selected, or clear all labels on a managed zone, complete the following steps.

###  gcloud 

Run the [`dns managed-zones update`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/managed-zones/update) command:
    
    
    gcloud dns managed-zones update NAME \
        --update-labels=LABELS
    
    
    
    gcloud dns managed-zones update NAME \
        --remove-labels=LABELS
    
    
    
    gcloud dns managed-zones update NAME \
        --clear-labels
    

Replace the following:

  * `NAME`: a name for your zone
  * `LABELS`: an optional comma-delimited list of key-value pairs such as `dept=marketing` or `project=project1`; for more information, see the [SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/dns/managed-zones/create#--labels)



## List and describe managed zones

The following sections show how to list or describe a managed zone.

### List managed zones

To list all of your managed zones within a project, complete the following steps.

###  Console 

  1. In the Google Cloud console, go to the **Cloud DNS zones** page.

[Go to Cloud DNS zones](https://console.cloud.google.com/networking/dns/zones/)

  2. View managed zones in the right pane.




###  gcloud 

Run the [`dns managed-zones list`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/managed-zones/list) command:
    
    
    gcloud dns managed-zones list
    

To list all managed zones, modify the command as follows: 
    
    
    gcloud dns managed-zones list --filter="visibility=public"
    

To list all managed private zones, modify the command as follows: 
    
    
    gcloud dns managed-zones list --filter="visibility=private"
    

### Describe a managed zone

To view the attributes of a managed zone, complete the following steps.

###  Console 

  1. In the Google Cloud console, go to the **Cloud DNS zones** page.

[Go to Cloud DNS zones](https://console.cloud.google.com/networking/dns/zones/)

  2. Click the zone that you want to inspect.




###  gcloud 

Run the [`dns managed-zones describe`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/managed-zones/describe) command:
    
    
    gcloud dns managed-zones describe NAME
    

Replace `NAME` with the name of your zone.

## Delete a managed zone

When you delete a zone, its DNS records are permanently removed; they cannot be recovered. To prevent losing your DNS records, export your zone data before deletion. For information about how to export zone data, see [Import and export resource record sets](https://docs.cloud.google.com/dns/docs/records#import-export).

To delete a managed zone, complete the following steps.

###  Console 

  1. In the Google Cloud console, go to the **Cloud DNS zones** page.

[Go to Cloud DNS zones](https://console.cloud.google.com/networking/dns/zones/)

  2. Click the managed zone that you want to delete.

  3. Click **Delete zone**.




###  gcloud 

  1. Remove all records in the zone except for the `SOA` and `NS` records. For more information, see [Removing a record](https://docs.cloud.google.com/dns/docs/records#removing_a_record). You can quickly empty an entire zone by importing an empty file into a record set. For more information, see [Importing and exporting record sets](https://docs.cloud.google.com/dns/docs/records#importing_and_exporting_record_sets). For example:
         
         touch empty-file
         gcloud dns record-sets import -z NAME \
            --delete-all-existing \
            empty-file
         rm empty-file
         

Replace `NAME` with the name of your zone.

  2. To delete a new managed private zone, run the [`dns managed-zones delete`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/managed-zones/delete) command:
         
         gcloud dns managed-zones delete NAME
         

Replace `NAME` with the name of your zone.




## What's next

  * To find solutions for common issues that you might encounter when using Cloud DNS, see [Troubleshooting](https://docs.cloud.google.com/dns/docs/troubleshooting).
  * To configure Cloud DNS server policies and use them with VPC networks, see [Apply Cloud DNS server policies](https://docs.cloud.google.com/dns/docs/policies).
  * To use IDNs with Cloud DNS, see [Create zones with internationalized domain names](https://docs.cloud.google.com/dns/docs/zones/international-domains).
  * To display an audit log of operations, see [View operations on managed zones](https://docs.cloud.google.com/dns/docs/zones/operations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
