---
url: https://docs.cloud.google.com/dns/docs/dnskeys/
title: View DNSSEC keys \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:38:58.697376+00:00
---

# View DNSSEC keys  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/dnskeys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Guides ](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name)



Send feedback 

#  View DNSSEC keys Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to view Domain Name System Security Extensions (DNSSEC) keys.

For a conceptual overview of DNSSEC, see the [DNSSEC overview](https://docs.cloud.google.com/dns/docs/dnssec).

A DNSKEY is a DNS record type that contains a public signing key. If you are migrating a DNSSEC signed zone to another DNS operator, you might need to see the DNSKEY records. The migration process in [RFC 6781](https://tools.ietf.org/html/rfc6781#section-4.3.5) requires importing the Zone Signing Key (ZSK) and Key Signing Key (KSK) DNSKEYs from the Cloud DNS zone into the other operator's zone.

If you have enabled DNSSEC for a zone, Cloud DNS automatically manages the creation and rotation of DNSSEC keys (DNSKEY records) and the signing of zone data with resource record digital signature (RRSIG) records. Cloud DNS does not support automatic rotation of KSKs because KSK rotations currently require manual interaction with the domain registrar. However, Cloud DNS does perform fully automatic ZSK rotations. You can view the automatically managed DNSKEYs with the Google Cloud CLI or REST API.

## Before you begin

Before you can view DNSSEC keys, you need to have [created a managed zone](https://docs.cloud.google.com/dns/docs/zones#creating_managed_zones) and [enabled DNSSEC for the zone](https://docs.cloud.google.com/dns/docs/dnssec-config#enabling) so that DNSKEY records are created.

**Note:** A DNSKEY collection is empty when `ManagedZones` are unsigned.

## Display current DNSKEYs

To display the current DNSKEY records for your zone, follow these steps.

###  gcloud 

For the following `gcloud` command-line examples, you can specify the `--project` parameter to operate on a specific project.

To print all DNSKEYs in JSON format, use the [`gcloud dns dns-keys list`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/dns-keys/list) command:
    
    
    gcloud dns dns-keys list --zone ZONE_NAME
    

Replace `ZONE_NAME` with the name of the managed zone.

To display the details of a specified DNSKEY in JSON format, use the [`gcloud dns dns-keys describe`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/dns-keys/describe) command:
    
    
    gcloud dns dns-keys describe DNSKEY_ID --zone ZONE_NAME
    

Replace the following:

  * `DNSKEY_ID`: the ID of the DNSKEY for which you want to view details
  * `ZONE_NAME`: the name of the managed zone



###  API 

To print all DNSKEYs to a `ResourceRecordSet` collection, use the [`dnsKeys.get`](https://docs.cloud.google.com/dns/docs/reference/v1/dnsKeys/get) method with an empty request body:
    
    
    GET https://dns.googleapis.com/dns/v1/projects/PROJECT/managedZones/ZONE_NAME/dnsKeys
    

Replace the following:

  * `PROJECT`: the name or ID of the DNS project
  * `ZONE_NAME`: the name of the managed zone



Your output is similar to the following:
    
    
    {
      "kind": "dns#dnsKeysListResponse",
      "header": {
        "operationId": string
      },
      "dnsKeys": [
        dnsKeys Resource
      ],
      "nextPageToken": string
    }
    

To display the details of a specified DNSKEY in JSON format, use the [`dnsKeys DNSKEY_ID.get`](https://docs.cloud.google.com/dns/docs/reference/v1/dnsKeys/get) method with an empty request body:
    
    
    GET https://dns.googleapis.com/dns/v1/projects/PROJECT/managedZones/ZONE_NAME/dnsKeys/DNSKEY_ID
    

Replace the following:

  * `PROJECT`: the name or ID of the DNS project
  * `ZONE_NAME`: the name of the managed zone
  * `DNSKEY_ID`: the ID of the DNSKEY for which you want to view details



###  Python 
    
    
      from apiclient import errors
      from apiclient.discovery import build
    
      PROJECT_NAME= 'PROJECT_NAME'
      ZONE_NAME= 'ZONE_NAME'
    
      try:
        service = build('dns', 'v1')
        response = service.dnskeys().list(project=PROJECT_NAME,
                                          managedZone=ZONE_NAME).execute()
      except errors.HttpError, error:
        print 'An error occurred: %s' % error
    
      try:
        response = service.dnskeys().list(project=PROJECT_NAME,
                                          managedZone=ZONE_NAME,
                                          keyId=KEY_ID).execute()
      except errors.HttpError, error:
        print 'An error occurred: %s' % error
    

Replace the following:

  * `PROJECT_NAME`: the name or ID of your DNS project
  * `ZONE_NAME`: the name of the managed zone



## What's next

  * To get information about specific DNSSEC configurations, see [Use advanced DNSSEC](https://docs.cloud.google.com/dns/docs/dnssec-advanced).
  * To monitor changes, see [Monitor DNS propagation](https://docs.cloud.google.com/dns/docs/monitoring#dns-propagation).
  * To find solutions for common issues that you might encounter when using Cloud DNS, see [Troubleshooting](https://docs.cloud.google.com/dns/docs/troubleshooting).
  * To get an overview of Cloud DNS, see [Cloud DNS overview](https://docs.cloud.google.com/dns/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
