---
url: https://docs.cloud.google.com/dns/docs/zones/managed-reverse-lookup-zones/
title: Create a managed reverse lookup zone \u00a0|\u00a0 Cloud DNS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:38:57.153056+00:00
---

# Create a managed reverse lookup zone  |  Cloud DNS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/zones/managed-reverse-lookup-zones/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Guides ](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name)



Send feedback 

#  Create a managed reverse lookup zone Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions about how to create a managed reverse lookup zone. For detailed background information, see [Managed reverse lookup zones](https://docs.cloud.google.com/dns/docs/zones/zones-overview#managed_reverse_lookup_zones).

By default, Cloud DNS forwards requests for PTR records of non-RFC 1918 addresses through the public internet. However, Cloud DNS also supports reverse lookup of non-RFC 1918 addresses by using private zones.

A managed reverse lookup zone is a private zone with a special attribute that instructs Cloud DNS to perform a PTR lookup against Compute Engine DNS data. You must set up managed reverse lookup zones for Cloud DNS to correctly resolve non-RFC 1918 PTR records for your virtual machine (VM) instances.

This configuration enables Cloud DNS to resolve non-RFC 1918 addresses locally instead of sending them over the internet when you configure your VPC network to use non-RFC 1918 addresses.

When you create a managed reverse lookup DNS zone, you cannot add records to the zone directly; the data comes from the Compute Engine IP address data.

Cloud DNS also supports outbound forwarding to non-RFC 1918 addresses by privately routing those addresses within Google Cloud. To enable this type of outbound forwarding, you must configure a forwarding zone with specific forwarding path arguments. For details, see [Forwarding targets and routing methods](https://docs.cloud.google.com/dns/docs/zones/zones-overview#fz-targets).

To create a new managed reverse lookup private zone, complete the following steps.

###  Console 

  1. In the Google Cloud console, go to the **Create a DNS zone** page.

[Go to Create a DNS zone](https://console.cloud.google.com/net-services/dns/zones/new/create)

  2. For the **Zone type** , select **Private**.

  3. Enter a **Zone name** such as `my-new-zone`.

  4. Enter a **DNS name** suffix for the zone. The suffix _must_ end with `in-addr.arpa` to be a reverse zone. This DNS name must match the reverse lookup name of the non-RFC 1918 PTR records that you are trying to resolve through Cloud DNS. For example, if you are trying to match the PTR record for `20.20.1.2`, you must create a reverse lookup zone with the DNS name of `2.1.20.20.in-addr.arpa`.

**Note:** Cloud DNS also supports matching of any child zone. For example, if you create a managed reverse lookup zone with the DNS name `20.in-addr.arpa.`, the zone matches any VPC-owned address `20. * . * . *`.
  5. Optional: Add a description.

  6. Under **Options** , select **Managed reverse lookup zone**.

  7. Select the networks to which the private zone must be visible.

  8. Click **Create**.




###  gcloud 

Run the [`dns managed-zones create`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/managed-zones/create) command:
    
    
    gcloud dns managed-zones create NAME \
        --description=DESCRIPTION \
        --dns-name=DNS_SUFFIX \
        --networks=VPC_NETWORK_LIST \
        --visibility=private \
        --managed-reverse-lookup
    

Replace the following:

  * `NAME`: a name for your zone
  * `DESCRIPTION`: a description for your zone
  * `DNS_SUFFIX`: the DNS suffix for your reverse zone that must end in `.in-addr.arpa`; typically, reverse zones take the form `${ip_block_in_reverse}.in-addr.arpa`
  * `VPC_NETWORK_LIST`: a comma-delimited list of VPC networks that contain the Google Cloud resources to which `PTR` records resolve



###  Terraform 
    
    
    resource "google_dns_managed_zone" "default" {
      name           = "my-new-zone"
      description    = "Example DNS reverse lookup"
      provider       = google-beta
      visibility     = "private"
      dns_name       = "2.2.20.20.in-addr.arpa."
      reverse_lookup = "true"
    }

**Note:** You cannot add records to a reverse lookup DNS zone directly; the data comes from the Compute Engine IP address data.

## What's next

  * To work with managed zones, see [Create, modify, and delete zones](https://docs.cloud.google.com/dns/docs/zones).
  * To find solutions for common issues that you might encounter when using Cloud DNS, see [Troubleshooting](https://docs.cloud.google.com/dns/docs/troubleshooting).
  * To get an overview of Cloud DNS, see [Cloud DNS overview](https://docs.cloud.google.com/dns/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
