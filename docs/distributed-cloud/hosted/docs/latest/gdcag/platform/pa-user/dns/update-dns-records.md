---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/update-dns-records/
title: Update DNS records \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:24:49.508496+00:00
---

# Update DNS records  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/update-dns-records/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Update DNS records Stay organized with collections  Save and categorize content based on your preferences. 

This document guides you on how to update previously created DNS records in Google Distributed Cloud (GDC) air-gapped.

## Before you begin

To update DNS records in GDC, you must have the following:

  * An existing public or private DNS zone with DNS records.
  * The necessary identity and access roles. To manage DNS records for your project, ask your **IAM Project Admin** to grant you the **Managed DNS Project Admin** (`managed-dns-project-admin`) role.
  * To use the gdcloud CLI, ensure you have it installed. For more information, see [Install the gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-install).
  * If you are using `kubectl`, a kubeconfig file for the global API server. If you have not yet generated this file, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#global-resources-kubeconfig). For more information, see [Global and zonal API servers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers).



## Update a DNS record

**Note:** You can only update the `ttlSeconds` (time to live) and `rrData` (record data) fields in the DNS Record. You can't modify the DNS zone (`dnsZone`), record name (`name`), or type of record (`type`).

You can update a DNS record using the gdcloud CLI or the Kubernetes API.

###  gdcloud 

To update a DNS record, use the [`gdcloud dns record-sets update`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-dns-record-sets-update) command:
    
    
    gdcloud dns record-sets update RESOURCE_RECORD_NAME \
        [--rrdatas=RECORD_DATA] \
        [--ttl=TIME_TO_LIVE] \
        [--project=PROJECT_NAMESPACE] \
        [--async]
    

Replace the following:

  * `RESOURCE_RECORD_NAME`: The name of the DNS record to update.
  * `RECORD_DATA`: The updated data for the record. For multiple entries, use a comma-separated list.
  * `TIME_TO_LIVE`: The updated time to live (TTL) in seconds.
  * `PROJECT_NAMESPACE`: the namespace of your project. This flag is optional if you have set a default project globally using `gdcloud config set project`.
  * `--async`: Specify this if you want the command to return immediately, rather than wait for the operation to complete. You can use [`describe`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/list-dns-records#list-dns-records) to check on the status of the operation.



You must specify at least one of the optional flags (`--rrdatas`, `--ttl`).

Here are some examples of the `--rrdatas` flag based on the record type:

  * `A` record: `--rrdatas=10.6.7.8`
  * `CNAME` record: `--rrdatas=ai.system.example.com`
  * `TXT` record: `--rrdatas="Example text"`
  * `PTR` record: `--rrdatas=8.7.6.10.in-addr.arpa.`
  * `MX` record: `--rrdatas="10 mail.example.com."`



###  API 

Use the Kubernetes API in GDC to update a DNS record:
    
    
    kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
    apiVersion: networking.global.gdc.goog/v1
    kind: ResourceRecordSet
    metadata:
      name: RESOURCE_RECORD_NAME
      namespace: PROJECT_NAMESPACE
    spec:
      name:  RESOURCE_RECORD_FQDN
      ttlSeconds: TIME_TO_LIVE
      type: RR_TYPE
      rrData:
      - RECORD_DATA
      dnsZone: DNS_ZONE_NAME
    EOF
    

Replace the following:

  * `GLOBAL_API_SERVER`: the global API server's kubeconfig path. For more information, see [Global and zonal API servers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers). If you have not yet generated a kubeconfig file for the API server, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in) for details.
  * `PROJECT_NAMESPACE`: the namespace of your project.
  * `RESOURCE_RECORD_NAME`: the DNS record to update, such as `test.system.example.com`.
  * `RESOURCE_RECORD_FQDN`: the fully qualified domain name (FQDN) for the record, such as `another.ai.system.example.com`.
  * `TIME_TO_LIVE`: the updated time to live (TTL) for this record, in seconds, which specifies how long DNS resolvers can cache this record before querying for it again. This field is optional. The default value is `300`.
  * `RR_TYPE`: the type of this `ResourceRecordSet`. The options are: `A`, `CNAME`, `TXT`, `PTR`, and `MX`.
  * `RECORD_DATA`: the updated data for all resource records in the RRset. Each entry represents a separate resource record. Here are some examples depending on the record type:

    * `A` record: the IP address this `A` record points to:
          
          type: A
          rrData:
          - 10.6.7.8
          

    * `CNAME` record: the target domain name for this `CNAME` record:
          
          type: CNAME
          rrData:
          - "ai.system.example.com"
          

    * `TXT` record: the text data for this `TXT` record:
          
          type: TXT
          rrData:
          - "Example text"
          

    * `PTR` record: the domain name this `PTR` record points to, for reverse DNS lookup of an IP address:
          
          type: PTR
          rrData:
          - "8.7.6.10.in-addr.arpa."
          

    * `MX` record: the priority and the hostname of the mail server:
          
          type: MX
          rrData:
          - "10 mail.example.com."
          

  * `DNS_ZONE_NAME`: the name of the `ManagedDNSZone` custom resource where this record is added. For more information, see [Create DNS zones](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/create-dns-zone).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
