---
url: https://docs.cloud.google.com/dns/docs/migrating/
title: Migrate to Cloud DNS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:38:57.937691+00:00
---

# Migrate to Cloud DNS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/migrating/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Guides ](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name)



Send feedback 

#  Migrate to Cloud DNS Stay organized with collections  Save and categorize content based on your preferences. 

Cloud DNS supports the migration of an existing DNS domain from another DNS provider to Cloud DNS. This procedure describes how to complete the necessary steps: create a managed zone for your domain, export the DNS configuration from your existing provider, import your existing DNS configuration to Cloud DNS, update your registrar's name server records, and then verify the migration.

## Before you begin

  1. If you have not yet used the Google Cloud CLI, [set up the gcloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute).

  2. To specify the project name and authenticate with the Google Cloud console, run the following command:
         
         gcloud auth login
         

You can also specify the `--project` parameter for a command to operate against a different project for that invocation.




## Create a managed zone

To migrate an existing domain, first create a managed zone to contain your DNS records. When you create a zone, the new zone isn't used until you update your domain registration, point a resolver at it, or query one of your zone's name servers.

###  gcloud 

To create a zone, run the [`dns managed-zones create`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/managed-zones/create) command:
    
    
    gcloud dns managed-zones create --dns-name=example.com.
    --description=A_ZONE EXAMPLE_ZONE_NAME
    

Replace the following:

  * `example.com.`: the DNS name
  * `A_ZONE`: a description of the zone
  * `EXAMPLE_ZONE_NAME`: the name to identify the DNS zone



## Export your DNS configuration from your existing provider

To export your [zone file](https://wikipedia.org/wiki/Zone_file), see your provider's documentation. Cloud DNS supports the import of zone files in BIND or YAML records format.

For example:

  * For [Dyn](https://www.oracle.com/corporate/acquisitions/dyn/), go to [Download Your Zone File](https://help.dyn.com/dns-knowledge-base/download-your-zone-file/).

  * For [AWS Route 53](https://aws.amazon.com/route53/), which does not support export, you can use the open source [cli53](https://github.com/barnybug/cli53) tool.




## Import the record set

After you have the exported the file from your other provider, you can use `gcloud` commands to import it into your managed zone.

To import record sets correctly, you must remove the apex records or use the flags described on the `gcloud` tab.

###  gcloud 

To import record sets, run the [`dns record-sets import`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/record-sets/import) command. The `--zone-file-format` flag tells `import` to expect a BIND zone formatted file. If you omit this flag,`import` expects a YAML-formatted records file:
    
    
    gcloud dns record-sets import -z=EXAMPLE_ZONE_NAME
    --zone-file-format path-to-example-zone-file
    

Replace `EXAMPLE_ZONE_NAME` with the name of your DNS zone.

**Caution:**

If your import file contains NS or SOA records for the apex of the zone, they will conflict with the pre-existing Cloud DNS records. To use the pre-existing Cloud DNS records (recommended), ensure that you remove the NS or SOA records from your import file. However, there are use cases for overriding this behavior; see the following important information.

**Caution:**

If your authoritative DNS is split across multiple providers and you have a non-Cloud DNS primary name server, then you must replace the Cloud DNS SOA record with the record from the other provider. To do this, you must use the `--delete-all-existing` flag when importing record sets to replace the SOA records that Cloud DNS provides. Otherwise, the update fails because the imported records conflict with the pre-existing Cloud DNS records.

For similar reasons, you can specify that the NS records in the import file be used instead of the pre-existing Cloud DNS records by using the `--delete-all-existing` and `--replace-origin-ns` flags together. Specifying an NS record for the apex of a zone results in an error even if the `--replace-origin-ns` flag is not specified. Either remove these records from the import file or use both the `--delete-all-existing` and `--replace-origin-ns` flags together if appropriate.

**Note:**

Some DNS implementations and providers export BIND zone files without final periods on domain name data in CNAME, MX, PTR, and other records. In zone files, Cloud DNS follows RFC standards and interprets all domain names without a final period as relative to the DNS name of the zone. Therefore, importing the following MX records into a zone with the DNS name `example.com` results in identical (and probably undesired) records for both:
    
    
        in.smtp              IN MX 5 gmail-smtp-in.l.google.com
        in.smtp.example.com. IN MX 5 gmail-smtp-in.l.google.com.example.com.
    

Before importing your zone files, check them to ensure that all names that need final periods have them.

## Verify DNS propagation

To monitor and verify that the Cloud DNS name servers have picked up your changes, you can use the Linux `watch` and `dig` commands.

**Note:** The `watch` and `dig` commands are not `gcloud` commands and are not used with the `gcloud` prefix. On non-Linux operating systems, you might need to install the `watch` and `dig` commands.

###  gcloud and Linux 

  1. To look up your zone's Cloud DNS name servers, run the [`dns managed-zones describe`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/managed-zones/describe) command:
         
         gcloud dns managed-zones describe EXAMPLE_ZONE_NAME
         

Replace `EXAMPLE_ZONE_NAME` with the name of your DNS zone.

The output looks something like this:
         
         nameServers:
         - ns-cloud-a1.googledomains.com.
         - ns-cloud-a2.googledomains.com.
         - ns-cloud-a3.googledomains.com.
         - ns-cloud-a4.googledomains.com.
         

In the output, the letter following the `ns-cloud-` part of the name is referred to as the name server _shard_. There are five such shards (letters A-E). For more information about shards, see [Name server limits](https://docs.cloud.google.com/dns/quotas#name_server_limits).

  2. Check if the records are available on the name servers.
         
         watch dig example.com @ZONE_NAME_SERVER
         

Replace ZONE_NAME_SERVER with one of the name servers returned when you ran the previous command.

  3. After you see your change, press `Ctrl+C` to exit.




The `watch` command runs the `dig` command every 2 seconds by default. You can use this command to determine when your authoritative name server picks up your change, which should happen within 120 seconds.

## Update your registrar's name server records

Sign in to your registrar provider and change the authoritative name servers to point to the name servers that are listed in the output of the [`gcloud dns managed-zones describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/dns/managed-zones/describe). At the same time, make a note of the time to live (TTL) that your registrar has set on the records. That tells you how long you have to wait before the new name servers begin to be used.

## Wait for changes and then verify

To get the authoritative name servers for your domain on the internet, run the following Linux commands:
    
    
    dig +short NS example.com
    

If the output shows that all changes have propagated, your task is complete. If not, you can check intermittently or you can automatically run the command every 2 seconds while you wait for the name servers to change. To do that, run the following:
    
    
    watch dig +short NS example.com
    

`Ctrl+C` exits the command.

If you're not using Linux, you can use the [`nslookup` command](https://wikipedia.org/wiki/Nslookup).

## What's next

  * To add, delete, or update records, see [Manage records](https://docs.cloud.google.com/dns/docs/records).
  * To use JSON formats for Cloud DNS record types, see [Records format (JSON)](https://docs.cloud.google.com/dns/docs/reference/json-record).
  * To find solutions for common issues that you might encounter when using Cloud DNS, see [Troubleshooting](https://docs.cloud.google.com/dns/docs/troubleshooting).
  * To get an overview of Cloud DNS, see [Cloud DNS overview](https://docs.cloud.google.com/dns/docs/overview).
  * For the Cloud DNS command-line, see the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/dns) documentation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
