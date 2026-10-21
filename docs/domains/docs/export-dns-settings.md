---
url: https://docs.cloud.google.com/domains/docs/export-dns-settings/
title: Migrate your Google Domains DNS settings to Cloud DNS or another provider \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:43:59.609771+00:00
---

# Migrate your Google Domains DNS settings to Cloud DNS or another provider  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/domains/docs/export-dns-settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Domains ](https://docs.cloud.google.com/domains/docs)
  * [ Guides ](https://docs.cloud.google.com/domains/docs/buy-register-domain)



Send feedback 

#  Migrate your Google Domains DNS settings to Cloud DNS or another provider Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** On September 7, 2023 Squarespace acquired all domain registrations and related customer accounts from Google Domains. For more information about how this change affects Cloud Domains, see [Cloud Domains feature deprecations](https://docs.cloud.google.com/domains/docs/deprecations/feature-deprecations), [Renew an expired domain registration](https://support.google.com/a/answer/6152355), and [Squarespace purchase of Google Domains FAQ](https://docs.cloud.google.com/domains/docs/faq). 

This page describes how to migrate your Google Domains DNS settings and export your domain and email forwarding configurations if you use Google Domains as your DNS provider.

  * If you don't use Google Domains as your DNS provider, you don't need to take any action.

  * If you don't use domain forwarding or email forwarding but use Google Domains as your DNS provider, you can Migrate your Google Domains DNS settings to Cloud DNS.

  * If you use domain or email forwarding, you can Export domain and email forwarding configurations.




## Before you begin

Check to see if you use Google Domains as your DNS provider, and if you have domain or email forwarding set up.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Domains** page.

[Go to Cloud Domains](https://console.cloud.google.com/net-services/domains/registrations/list)

The **Registrations** page lists your registrations.

  2. Click the domain name for which you want to get the information.

You can check if a specific domain uses Google Domains as its DNS provider or if the domain has domain or email forwarding configurations.




###  gcloud 

To view registration details for a specific domain, use the [`gcloud domains registrations describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/domains/registrations/describe):
    
    
    gcloud domains registrations describe DOMAIN_NAME
    

Replace `DOMAIN_NAME` with the name of the domain that you want to view details for—for example, `example.app`.

If your domain uses Google Domains as your DNS provider, the `dnsSettings` section of the output looks similar to the following example:
    
    
    dnsSettings:
        googleDomainsDns:
    

If your domain uses domain or email forwarding configurations, the `dnsSettings` section of the output looks similar to the following example:
    
    
    dnsSettings:
        ...
        googleDomainsRedirectsDataAvailable: true
    

## Migrate your Google Domains DNS settings to Cloud DNS

To migrate your Google Domains DNS settings, follow these steps.

###  gcloud 

  1. Create a managed public zone for your domain.

Use the [`dns managed-zones create` command](https://docs.cloud.google.com/sdk/gcloud/reference/dns/managed-zones/create):
         
         gcloud dns managed-zones create ZONE_NAME \
             --description=DESCRIPTION \
             --dns-name=DOMAIN_NAME \
             --visibility=public \
             [--labels=LABELS] \
             [--dnssec-state=DNSSEC_STATE]
         

Replace the following:

     * `ZONE_NAME`: a name for your zone
     * `DESCRIPTION`: a description for your zone
     * `DOMAIN_NAME`: the domain name for your zone—for example, `example.com`. To use a DNS zone for a domain name, you must ensure that the DNS suffix in the zone matches the domain name. Note that `example.com` and `example.com.` are considered equivalent.
     * `LABELS`: a comma-delimited list of key-value pairs such as `dept=marketing` or `project=project1`. This flag is optional. For more information, see the [SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/dns/managed-zones/create#--labels)
     * `DNSSEC_STATE`: the DNSSEC state for your zone. For more information, see [DNS Security Extensions (DNSSEC) overview](https://docs.cloud.google.com/dns/docs/dnssec). This flag is optional.
  2. Disable DNSSEC for your domain.

If DNSSEC is enabled, disable it and wait 24 hours for the change to take effect.

Use the [`gcloud domains registrations configure dns` command](https://docs.cloud.google.com/sdk/gcloud/reference/domains/registrations/configure/dns):
         
         gcloud domains registrations configure dns DOMAIN_NAME \
             --disable-dnssec
         

Replace `DOMAIN_NAME` with the name of the domain for which you want to disable DNSSEC

  3. Retrieve the DNS record information from your Google Domains DNS zone.

Use the [`gcloud domains registrations google-domains-dns export-dns-record-sets` command](https://docs.cloud.google.com/sdk/gcloud/reference/domains/registrations/google-domains-dns/export-dns-record-sets):
         
         gcloud domains registrations google-domains-dns export-dns-record-sets DOMAIN_NAME \
             --records-file=RECORDS_FILE \
             --zone-file-format
         

Replace the following:

     * `DOMAIN_NAME`: the name of the domain for which you want to retrieve the DNS record information
     * `RECORDS_FILE`: the file to which the record sets must be exported—for example, `records.zonefile`
  4. Import the records to the Cloud DNS zone.

Use the [`dns record-sets import` command](https://docs.cloud.google.com/sdk/gcloud/reference/dns/record-sets/import). The `--zone-file-format` flag sets the `import` command to expect a BIND zone file. If you omit this flag, `import` expects a YAML file:
         
         gcloud dns record-sets import RECORDS_FILE \
             --zone=ZONE_NAME \
             --zone-file-format \
             --delete-all-existing
         

Replace the following:

     * `RECORDS_FILE`: the file from which the record sets must be imported—for example, `records.zonefile`
     * `ZONE_NAME`: the name of the managed zone whose record sets you want to manage
  5. Start using the migrated Cloud DNS zone.

Use the `gcloud domains registrations configure dns` command:
         
         gcloud domains registrations configure dns DOMAIN_NAME \
             --cloud-dns-zone=ZONE_NAME
         

Replace the following:

     * `DOMAIN_NAME`: the name of the registered domain—for example, `example.app`.
     * `ZONE_NAME`: the name of the managed zone whose record sets you want to manage
  6. Monitor your domain. If you encounter any DNS configuration issues, roll back the migration.

Use the `gcloud domains registrations configure dns` command:
         
         gcloud domains registrations configure dns DOMAIN_NAME --use-google-domains-dns
         

Replace `DOMAIN_NAME` with the name of the registered domain—for example, `example.app`.

  7. Optional: Enable DNSSEC for your domain.

     1. Wait for at least 24 hours after completing step 5.
     2. Use the `gcloud domains registrations configure dns` command:
    
    gcloud domains registrations configure dns DOMAIN_NAME \
      --cloud-dns-zone=ZONE_NAME \
      --no-disable-dnssec
    

Replace the following:

     * `DOMAIN_NAME`: the name of the registered domain—for example, `example.app`.
     * `ZONE_NAME`: the managed zone name for which you want to disable DNSSEC



## Export your domain and email forwarding configurations to another hosting provider

###  gcloud 

  1. Disable DNSSEC for your domain.

If DNSSEC is enabled, you must disable it and wait 24 hours for the change to take effect.

Use the [`gcloud domains registrations configure dns` command](https://docs.cloud.google.com/sdk/gcloud/reference/domains/registrations/configure/dns):
         
         gcloud domains registrations configure dns DOMAIN_NAME \
             --disable-dnssec
         

Replace the following:

     * `DOMAIN_NAME`: the name of the domain for which you want to disable DNSSEC
  2. Export your Google Domains DNS configuration.

Use the [`gcloud domains registrations google-domains-dns export-dns-record-sets` command](https://docs.cloud.google.com/sdk/gcloud/reference/domains/registrations/google-domains-dns/export-dns-record-sets):
         
         gcloud domains registrations google-domains-dns export-dns-record-sets DOMAIN_NAME \
             --records-file=RECORDS_FILE \
             --zone-file-format
         

Replace the following:

     * `DOMAIN_NAME`: the name of the domain for which you want to retrieve the DNS record information
     * `RECORDS_FILE`: the file to which the record sets must be exported—for example, `records.zonefile`
  3. Retrieve your Google Domains domain and email forwarding configuration.

Use the [`gcloud domains registrations google-domains-dns get-forwarding-config` command](https://docs.cloud.google.com/sdk/gcloud/reference/domains/registrations/google-domains-dns/get-forwarding-config):
         
         gcloud domains registrations google-domains-dns get-forwarding-config DOMAIN_NAME
         

Replace `DOMAIN_NAME` with the name of the registered domain—for example, `example.app`.

  4. Import the DNS records and forwarding configuration to your new hosting provider. For instructions, contact your hosting provider.

  5. Configure domain and forwarding settings for your new hosting provider. For instructions, contact your hosting provider.

If you have `MX` and `CNAME` records, make sure that you configure these records to redirect services to your new hosting provider.

  6. Update the name server for your domain. You can get the name server information from your new hosting provider.

Use the `gcloud domains registrations configure dns` command:
         
         gcloud domains registrations configure dns DOMAIN_NAME \
             --name-servers=NAME_SERVERS_LIST
         

Replace `NAME_SERVERS_LIST` with a list of DNS name servers for the domain.

  7. Monitor your domain. If you encounter any DNS configuration issues, roll back the migration.

Use the `gcloud domains registrations configure dns` command:
         
         gcloud domains registrations configure dns DOMAIN_NAME --use-google-domains-dns
         

  8. Optional: Enable DNSSEC for your DNS zone at your hosting provider.

     1. Wait for 24 hours after you enable DNSSEC for your DNS zone.
     2. Enable DNSSEC for your domain.

Use the `gcloud domains registrations configure dns` command:
            
            gcloud domains registrations configure dns DOMAIN_NAME \
                --dns-settings-from-file=DNS_SETTINGS_FILE_NAME
            

Replace the following:

        * `DOMAIN_NAME`: the name of the registered domain—for example, `example.app`.
        * `DNS_SETTINGS_FILE_NAME`: the YAML file containing the required DNS settings. If specified, its content replaces the values used in the registration resource. If the YAML file is missing some of the `dns_settings` fields, those fields are removed.

Example of the file contents:
              
              customDns:
                  nameServers:
                  - new.ns1.com
                  - new.ns2.com
                  dsRecords:
                  - keyTag: 24
                    algorithm: RSASHA256
                    digestType: SHA256
                    digest: ab1cfa82b035c26cbbbdae632cea070514eb8b773f616aaeaf668e2f0be8f10d
              




## What's next

  * To find answers to frequently asked questions, see [Squarespace purchase of Google Domains FAQ](https://docs.cloud.google.com/domains/docs/faq).
  * To find solutions for common issues that you might encounter when using Cloud Domains, see [Troubleshoot Cloud Domains](https://docs.cloud.google.com/domains/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
