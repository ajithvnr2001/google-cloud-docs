---
url: https://docs.cloud.google.com/dns/docs/registrars/
title: Activate DNSSEC \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:12:31.490146+00:00
---

# Activate DNSSEC  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/registrars/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Guides ](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name)



Send feedback 

#  Activate DNSSEC Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to activate and deactivate Domain Name System Security Extensions (DNSSEC) at your domain registrar.

To learn about DNSSEC, see the [DNSSEC overview](https://docs.cloud.google.com/dns/docs/dnssec).

## Activate DNSSEC at your domain registrar

After you [enable DNSSEC for existing managed public zones](https://docs.cloud.google.com/dns/docs/dnssec-config#enabling), you must activate DNSSEC at your domain registrar. To activate DNSSEC, you create a DS record for your domain in the parent zone so that resolvers can identify that your domain is DNSSEC enabled and can validate its data.

Each registrar has a different procedure to create this DS record. Many registrars use a website form. For more information, see the documentation of your registrar.

After you activate DNSSEC, the DS record must propagate throughout the entire DNS. This process can take 24 hours or more, depending on the time to live (TTL) values that you set for your DNS records and the caching behavior of different DNS resolvers.

Before you activate DNSSEC on important domains, test your DNS configuration thoroughly.

### Get DS records

To get DS records for your zone, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **Create a DNS zone** page.

[Go to Create a DNS zone](https://console.cloud.google.com/networking/dns/zones/~new)

  2. Click the zone for which you want the DS records.

  3. Click **Registrar setup**.

  4. Copy the DS records from the dialog. The DS records are similar to the following: 
         
         18311 8 2 1A347FBF4EDA76375760AEB183E3B0081C9D8BE63384637D46ED5F6C010F961B
         




###  gcloud 

Use the [`gcloud dns dns-keys list` command](https://docs.cloud.google.com/sdk/gcloud/reference/dns/dns-keys/list).
    
    
    gcloud dns dns-keys list \
    --filter='type=keySigning' --format='value(ds_record())' \
    --zone=MANAGED_ZONE_NAME
    

Replace the following:

  * `MANAGED_ZONE`: the name of the managed zone



Your output is similar to the following:
    
    
    18311 8 2 1A347FBF4EDA76375760AEB183E3B0081C9D8BE63384637D46ED5F6C010F961B
    

## Deactivate DNSSEC at your domain registrar

Before you disable DNSSEC for a managed zone that you still want to use, you must deactivate DNSSEC for your zone at your domain registrar to help ensure that DNSSEC-validating resolvers can still resolve names in the zone.

To deactivate DNSSEC, remove all DS records for your domain from the parent zone; this action prevents resolvers from using DNSSEC to validate your domain data.

After you remove the DS records from the registrar, you must wait for the removal of the DS record to propagate to all resolvers before you can turn off DNSSEC for the zone. This process might take 24 hours or longer, depending on the propagation latency incurred by the registrar, registry, and resolver caching.

After you confirm that the DS record is removed from your registrar and is no longer accessible to the resolvers, you can safely [disable DNSSEC for the zone](https://docs.cloud.google.com/dns/docs/dnssec-config#disabling).

## What's next

  * To get information about specific DNSSEC configurations, see [Use advanced DNSSEC](https://docs.cloud.google.com/dns/docs/dnssec-advanced).
  * To find solutions for common issues that you might encounter when using Cloud DNS, see [Troubleshooting](https://docs.cloud.google.com/dns/docs/troubleshooting).
  * To get an overview of Cloud DNS, see [Cloud DNS overview](https://docs.cloud.google.com/dns/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
