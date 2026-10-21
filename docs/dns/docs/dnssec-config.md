---
url: https://docs.cloud.google.com/dns/docs/dnssec-config/
title: Manage DNSSEC configuration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:38:58.488955+00:00
---

# Manage DNSSEC configuration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/dnssec-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Guides ](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name)



Send feedback 

#  Manage DNSSEC configuration Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to enable and disable Domain Name System Security Extensions (DNSSEC) for your Cloud DNS zones and verify DNSSEC deployment. Enabling DNSSEC helps to protect your domains from DNS spoofing and cache poisoning attacks.

For a conceptual overview of DNSSEC, see the [DNSSEC overview](https://docs.cloud.google.com/dns/docs/dnssec).

**Note:** You cannot enable or disable DNSSEC for existing zones that have more than 3000 resource record sets. To sign existing large zones, consider setting up a new zone with the same DNS name with DNSSEC enabled, populating it with your resource record sets in additional operations, and changing your delegation to point to the name server set for the new zone that has DNSSEC enabled.

## Enable DNSSEC for existing managed public zones

To enable DNSSEC for existing managed public zones, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **Cloud DNS** page.

[Go to Cloud DNS](https://console.cloud.google.com/net-services/dns/)

  2. Click the zone name for which you want to enable DNSSEC.

  3. On the **Zone details** page, click **Edit**.

  4. On the **Edit a DNS zone** page, click **DNSSEC**.

  5. Under **DNSSEC** , select **On**.

  6. Click **Save**.




Your selected DNSSEC state for the zone is displayed in the **DNSSEC** column on the **Cloud DNS** page.

###  gcloud 

Run the following command:
    
    
    gcloud dns managed-zones update EXAMPLE_ZONE \
        --dnssec-state on
    

Replace `EXAMPLE_ZONE` with the zone ID.

###  Terraform 
    
    
    resource "google_dns_managed_zone" "example" {
      name        = "example-zone-name"
      dns_name    = "example.com."
      description = "Example Signed Zone"
      dnssec_config {
        state = "on"
      }
    }

## Enable DNSSEC when creating zones

To enable DNSSEC when you are creating a zone, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **Cloud DNS** page.

[Go to Cloud DNS](https://console.cloud.google.com/net-services/dns/)

  2. Click **Create zone**.

  3. In the **Zone name** field, enter a name.

  4. In the **DNS name** field, enter a name.

  5. Under **DNSSEC** , select **On**.

  6. Optional: Add a description.

  7. Click **Create**.

![Create DNSSEC signed zone](https://docs.cloud.google.com/static/dns/images/create-signed-zone.png)




###  gcloud 

Run the following command:
    
    
    gcloud dns managed-zones create EXAMPLE_ZONE \
        --description "Signed Zone" \
        --dns-name myzone.example.com \
        --dnssec-state on
    

Replace `EXAMPLE_ZONE` with the zone ID.

## Verify DNSSEC deployment

To verify correct deployment of your DNSSEC-enabled zone, make sure that you placed the correct DS record in the parent zone. DNSSEC resolution can fail if either of the following occurs:

  * The configuration is wrong, or you have mistyped it.
  * You have placed the incorrect DS record in the parent zone.



To verify that you have the right configuration in place and to cross-check the DS record before placing it in the parent zone, use the following tools:

  * [DNSViz](https://dnsviz.net/)
  * [Verisign DNSSEC debugger](https://dnssec-analyzer.verisignlabs.com/)
  * [Zonemaster](https://zonemaster.net/)



You can use the Verisign DNSSEC debugger and Zonemaster sites to validate your DNSSEC configuration _before_ you update your registrar with your Cloud DNS name servers or DS record. A domain that is properly configured for DNSSEC is [`example.com`](http://dnsviz.net/d/www.example.com/dnssec), viewable using DNSViz.

## Recommended TTL settings for DNSSEC-signed zones

TTL is the time to live (in seconds) for a DNSSEC-signed zone.

**Important:** In DNSSEC-enabled zones, avoid TTLs longer than **259200** (3 days).

Unlike TTL expirations, which are relative to the time a name server sends a response to a query, DNSSEC signatures expire at a fixed absolute time. TTLs configured longer than a signature lifetime can lead to many clients requesting records at the same time as the DNSSEC signature expires. Short TTLs can also cause problems for DNSSEC-validating resolvers.

For more recommendations about TTL selection, see [RFC 6781 section 4.4.1 Time Considerations](https://tools.ietf.org/html/rfc6781#section-4.4.1) and [RFC 6781 Figure 11](https://tools.ietf.org/html/rfc6781#page-50).

**Note:** Having a TTL that is at least a few times smaller than your signature validity period avoids query load peaks.

When reading RFC 6781 section 4.4.1, consider that many signature time parameters are fixed by Cloud DNS and you cannot change them. You cannot change the following parameters (subject to change without notice or update to this document):

  * Inception offset = 1 day 
  * Validity period = 21 days 
  * Re-sign period = 3 days 
  * Refresh period = 18 days 
  * Jitter interval = ½ day (or ±6 hours) 
  * Minimum signature validity = refresh – jitter = 17.75 days = 1533600



You must never use a TTL longer than the minimum signature validity.

## Disable DNSSEC for managed zones

**Important:** Before disabling DNSSEC for a managed zone that you want to use, you must [deactivate DNSSEC at your domain registrar](https://docs.cloud.google.com/dns/docs/registrars#del-ds) to ensure that DNSSEC-validating resolvers can still resolve names in the zone.

After you have removed DS records and waited for them to expire from cache, you can use the following `gcloud` command to turn off DNSSEC:
    
    
    gcloud dns managed-zones update EXAMPLE_ZONE \
        --dnssec-state off
    

Replace `EXAMPLE_ZONE` with the zone ID.

## What's next

  * To get information about specific DNSSEC configurations, see [Use advanced DNSSEC](https://docs.cloud.google.com/dns/docs/dnssec-advanced).
  * To work with managed zones, see [Create, modify, and delete zones](https://docs.cloud.google.com/dns/docs/zones).
  * To find solutions for common issues that you might encounter when using Cloud DNS, see [Troubleshooting](https://docs.cloud.google.com/dns/docs/troubleshooting).
  * To get an overview of Cloud DNS, see [Cloud DNS overview](https://docs.cloud.google.com/dns/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
