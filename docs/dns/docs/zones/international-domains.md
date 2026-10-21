---
url: https://docs.cloud.google.com/dns/docs/zones/international-domains/
title: Create a zone with an Internationalized Domain Name \u00a0|\u00a0 Cloud DNS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:38:57.444770+00:00
---

# Create a zone with an Internationalized Domain Name  |  Cloud DNS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/zones/international-domains/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Guides ](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name)



Send feedback 

#  Create a zone with an Internationalized Domain Name Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use an [Internationalized Domain Name (IDN)](https://wikipedia.org/wiki/Internationalized_domain_name) with Cloud DNS.

## Create a new managed zone with an IDN suffix

You can create both public and private zones with IDN suffixes.

  * When using the Google Cloud console, Cloud DNS automatically encodes internationalized domain names when you create a DNS zone. You can use both IDN-encoded and unencoded names.

  * When using the Google Cloud CLI or an API, create a domain name by using [Punycode](https://wikipedia.org/wiki/Punycode), which some applications can recognize and render in an international language-specific script.

For example, for the domain name to appear as `example.ελ`, use the IDN representation of `ελ` for the suffix, which is `.xn--qxam.` All records in the zone share this suffix.




To see how your domain name visually converts from Unicode characters to the equivalent ASCII-Compatible Encoding (ACE) form, use the [IDN converter tool](https://www.verisign.com/en_US/channel-resources/domain-registry-products/idn/idn-conversion-tool/index.xhtml).

To create a new managed public zone with an IDN suffix, complete the following steps.

###  Console 

  1. In the Google Cloud console, go to the **Create a DNS zone** page.

[Go to Create a DNS zone](https://console.cloud.google.com/net-services/dns/zones/new/create)

  2. For the **Zone type** , select **Public**.

  3. Enter a **Zone name** , such as `my-new-zone`.

  4. Enter a **DNS name** suffix for the zone by using a domain name that you own.

  5. Under **DNSSEC** , select `Off`, `On`, or `Transfer`. For more information, see [Enabling DNSSEC for existing managed zones](https://docs.cloud.google.com/dns/docs/dnssec-config#enabling).

  6. Click **Create**. The **Zone details** page is displayed.

**Note:** For best results, URL values must comply with the format as defined by [RFC 3986](https://tools.ietf.org/html/rfc3986).



###  gcloud 

Run the [`dns managed-zones create`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/managed-zones/create) command:
    
    
    gcloud dns managed-zones create NAME \
        --description=DESCRIPTION \
        --dns-name=DNS_SUFFIX \
        --visibility=public \
        --dnssec-state=DNSSEC_STATE
    

Replace the following:

  * `NAME`: a name for your zone
  * `DESCRIPTION`: a description for your zone
  * `DNS_SUFFIX`: the DNS suffix in the Punycode format for your zone using a domain name that you own

  * `DNSSEC_STATE`: how DNS authenticates responses to domain name lookups for this managed zone

    * `off`: disable DNSSEC for the managed zone
    * `on`: enable DNSSEC for the managed zone
    * `transfer`: enable DNSSEC and allow transferring a signed zone in or out



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
  * `DNS_NAME`: the DNS suffix in the Punycode format for your zone using a domain name that you own



## What's next

  * To work with managed zones, see [Create, modify, and delete zones](https://docs.cloud.google.com/dns/docs/zones).
  * To find solutions for common issues that you might encounter when using Cloud DNS, see [Troubleshooting](https://docs.cloud.google.com/dns/docs/troubleshooting).
  * To get an overview of Cloud DNS, see [Cloud DNS overview](https://docs.cloud.google.com/dns/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
