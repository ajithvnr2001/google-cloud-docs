---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/create-dns-records/
title: Create DNS records \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:43:45.800988+00:00
---

# Create DNS records  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/create-dns-records/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create DNS records Stay organized with collections  Save and categorize content based on your preferences. 

This document guides you through creating DNS records to manage how traffic reaches your applications and services within Google Distributed Cloud (GDC) air-gapped. DNS records let you map a domain name to a specific resource so that you can give users access to an application, manage service aliases, verify ownership, enable reverse lookup, or route email. The intended audience for this document is platform administrators and application operators responsible for managing DNS records within a project.

After you have created your [DNS zone](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/create-dns-zone), you can create different types of DNS records to point your domain names and subdomains to your services. You can create the following DNS record types in GDC:

  * **Address (A) record:** maps a domain name to one or more IPv4 addresses. This record is the most fundamental record type for pointing a domain to a server.
  * **Canonical Name (CNAME) record:** creates an alias of one domain name to another canonical (authoritative) domain name. This record type is useful for redirecting traffic or simplifying DNS management.
  * **Text (TXT) record:** lets you associate arbitrary text with a domain name. These records are often used for verification purposes or to store information like Sender Policy Framework (SPF) records for email authentication.
  * **Pointer (PTR) record:** maps an IP address back to a domain name, also known as reverse DNS lookup. This record is often used for email server reputation and logging analysis.
  * **Mail Exchanger (MX) record:** specifies the mail servers responsible for accepting email for a domain. This is essential for setting up email services.



GDC doesn't support setting **Name Server (NS)** or **Start of Authority (SOA)** records for a domain.

**Note:** The number of DNS records you can create is subject to a limit. See [System limits](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/system-limits#dns) for details.

## Before you begin

To create DNS records in GDC, you must have the following:

  * An existing public or private DNS zone. For more information, see [Create DNS zones](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/create-dns-zone).
  * The necessary identity and access roles. To manage DNS records for your project, ask your **Project IAM Admin** to grant you the **Managed DNS Project Admin** (`managed-dns-project-admin`) role.
  * To use the gdcloud CLI, ensure you have it installed. For more information, see [Install the gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-install).
  * If you are using `kubectl`, a kubeconfig file for the global API server. If you have not yet generated this file, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#global-resources-kubeconfig). For more information, see [Global and zonal API servers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers).



## Create a DNS record

You can create a DNS record using the gdcloud CLI or the Kubernetes API.

###  gdcloud 

To create a DNS record, use the [`gdcloud dns record-sets create`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-dns-record-sets-create) command:
    
    
    gdcloud dns record-sets create RESOURCE_RECORD_NAME \
        --fqdn=RESOURCE_RECORD_FQDN \
        --type=RR_TYPE \
        --rrdatas=RECORD_DATA \
        --dns-zone=DNS_ZONE_NAME \
        [--ttl=TIME_TO_LIVE] \
        [--project=PROJECT_NAMESPACE] \
        [--async]
    

Replace the following:

  * `RESOURCE_RECORD_NAME`: your chosen unique name for this `ResourceRecordSet`resource within the namespace, such as `cname.system.example.com`
  * `RESOURCE_RECORD_FQDN`: the fully qualified domain name (FQDN) for the record, such as `another.ai.system.example.com`.
  * `RR_TYPE:`the type of this `ResourceRecordSet`. The options are: `A`, `CNAME`, `TXT`, `PTR`, and `MX`
  * `RECORD_DATA`: the data for all resource records in the `ResourceRecordSet`. Each entry represents a separate resource record. For multiple entries, use a comma-separated list.
  * `DNS_ZONE_NAME`: the name of the `ManagedDNSZone` custom resource where this record is added.
  * `TIME_TO_LIVE`: the time to live (TTL) in seconds for this record. This field is optional. The default value is `300`.
  * `PROJECT_NAMESPACE`: the namespace of your project. This flag is optional if you have set a default project globally using `gdcloud config set project`.
  * `--async`: Specify this if you want the command to return immediately, rather than wait for the operation to complete. You can use [`describe`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/list-dns-records#list-dns-records) to check on the status of the operation.



Here are some examples of the `--rrdatas` flag based on the record type:

  * `A` record: `--rrdatas=10.6.7.8`
  * `CNAME` record: `--rrdatas=ai.system.example.com`
  * `TXT` record: `--rrdatas="Example text"`
  * `PTR` record: `--rrdatas=8.7.6.10.in-addr.arpa.`
  * `MX` record: `--rrdatas="10 mail.example.com."`



###  API 

  * Create and apply a `ResourceRecordSet` resource to create a DNS record within an existing managed DNS zone:


    
    
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

  * `GLOBAL_API_SERVER`: the path to the global API server's kubeconfig file. If you have not yet generated this file, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#global-resources-kubeconfig).
  * `PROJECT_NAMESPACE`: the namespace of your project.
  * `RESOURCE_RECORD_NAME`: your chosen unique name for this `ResourceRecordSet`resource within the namespace, such as `cname.system.example.com`
  * `RESOURCE_RECORD_FQDN`: the fully qualified domain name (FQDN) for the record, such as `another.ai.system.example.com`.
  * `TIME_TO_LIVE`: the time to live (TTL) in seconds for this record. This field is optional. The default value is `300`.
  * `RR_TYPE:`the type of this `ResourceRecordSet`. The options are: `A`, `CNAME`, `TXT`, `PTR`, and `MX`
  * `RECORD_DATA`: the data for all resource records in the RRset. Each entry represents a separate resource record. Here are some examples depending on the record type:

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

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
