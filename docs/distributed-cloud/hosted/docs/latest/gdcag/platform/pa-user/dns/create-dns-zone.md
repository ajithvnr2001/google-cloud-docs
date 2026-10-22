---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/create-dns-zone/
title: Create DNS zones \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:22:03.106337+00:00
---

# Create DNS zones  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/create-dns-zone/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create DNS zones Stay organized with collections  Save and categorize content based on your preferences. 

This document guides you through how to configure DNS resolution for a new domain in Google Distributed Cloud (GDC) air-gapped through the use of DNS zones. Use a DNS zone to group a set of DNS records together, and control whether those records are visible outside your Virtual Private Cloud (VPC) in GDC.

The intended audience for this document is platform administrators and application operators responsible for managing DNS resolution for their organization.

You can create public or private DNS zones in your GDC environment to match the visibility and access requirements of your services:

  * **For services that require external network visibility and access:** Set up a public DNS zone to allow users and systems outside your network to access your service. If you have a website, a public-facing API, or any service that needs to be reachable from outside your GDC Cloud environment, you need a public DNS zone to map your domain name to the appropriate IP addresses.
  * **For services that require secure and restricted access to internal systems:** Set up a private DNS zone to hide your internal domain name and restrict access to your internal services. If you have an internal application, database, or microservice that needs to communicate with other internal services using only secure protocols and private IP addresses, you need a private DNS zone to map your domain name to the appropriate IP addresses A private DNS zone ensures that these services can find each other using internal domain names without exposing their existence or IP addresses to the external network. This enhances security and simplifies internal networking.



For more information about the difference between public and private DNS zones, see [Zone types for Cloud DNS](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/dns-overview#zone-types).

**Note:** The number of DNS zones you can create is subject to limits. See [System limits](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/system-limits#dns) for details.

## Before you begin

To configure DNS zones in GDC and add records, you must have the following:

  * An existing project. For more information, see [Create a project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-a-project).
  * The necessary identity and access roles. To manage DNS zones for your project, ask your **IAM Project Admin** to grant you the **Managed DNS Project Admin** (`managed-dns-project-admin`) role.
  * To use the gdcloud CLI, ensure you have it installed. For more information, see [Install the gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-install).
  * If you are using `kubectl`, a kubeconfig file for the global API server. If you have not yet generated this file, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#global-resources-kubeconfig). For more information, see [Global and zonal API servers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers).



## Create a public DNS zone

After you create a public DNS zone, you must configure your network's DNS resolver to forward requests to the appropriate name servers.

### Create the zone

You can create a public DNS zone using the gdcloud CLI or the Kubernetes API.

###  gdcloud 

To create a public DNS zone, use the [`gdcloud dns managed-zones create`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-dns-managed-zones-create) command:
    
    
    gdcloud dns managed-zones create DNS_ZONE_NAME \
        --dns-name=DOMAIN_NAME \
        --visibility=PUBLIC \
        --description="DESCRIPTION" \
        [--project=PROJECT_NAMESPACE] \
        [--async]
    

Replace the following:

  * `DNS_ZONE_NAME`: the name of your DNS zone.
  * `DOMAIN_NAME`: the domain name for your public DNS zone, such as `example.com`.
  * `DESCRIPTION`: a description for your DNS zone. For example, `Public DNS zone for example.com`. This field is optional.
  * `PROJECT_NAMESPACE`: the namespace of your project. This flag is optional if you have set a default project globally using `gdcloud config set project`.
  * `--async`: Specify this if you want the command to return immediately, rather than wait for the operation to complete. You can use [`describe`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/list-dns-zones#list-dns-zones) to check on the status of the operation.



###  API 

Use the Kubernetes API in GDC to create a public DNS zone:

  1. Create and apply a `ManagedDNSZone` resource to create a DNS zone accessible from outside of GDC:
         
         kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
         apiVersion: networking.global.gdc.goog/v1
         kind: ManagedDNSZone
         metadata:
           name: DNS_ZONE_NAME
           namespace: PROJECT_NAMESPACE
         spec:
           dnsName: DOMAIN_NAME
           description: DESCRIPTION
           visibility: PUBLIC
         EOF
         

Replace the following:

     * `GLOBAL_API_SERVER`: the global API server's kubeconfig path. For more information, see [Global and zonal API servers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers). If you have not yet generated a kubeconfig file for the API server, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in) for details.
     * `DNS_ZONE_NAME`: the name of your DNS zone.
     * `PROJECT_NAMESPACE`: the namespace of your project.
     * `DOMAIN_NAME`: the domain name for your public DNS zone, such as `example.com`.
     * `DESCRIPTION`: a description for your DNS zone. For example, `Public DNS zone for example.com`. This field is optional.

Note that `visibility` is case sensitive, and must have the exact value `PUBLIC`.




### Configure your DNS resolver

For a public DNS zone, you must configure the DNS resolver in your network to forward DNS requests for that DNS zone to the name servers in GDC that host that DNS zone.

  1. Fetch the name servers for the `ManagedDNSZone` you created. You need to use `kubectl` for this step.
         
         kubectl --kubeconfig GLOBAL_API_SERVER get manageddnszones DNS_ZONE_NAME -n PROJECT_NAMESPACE -oyaml
         

Replace the following:

     * `GLOBAL_API_SERVER`: the global API server's kubeconfig path. For more information, see [Global and zonal API servers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers). If you have not yet generated a kubeconfig file for the API server, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in) for details.
     * `DNS_ZONE_NAME`: the name of your DNS zone.
     * `PROJECT_NAMESPACE`: the namespace of your project. This flag is optional if you have set a default project globally using `gdcloud config set project`.

The name servers will be listed in the status output:
    
    apiVersion: networking.global.gdc.goog/v1
      kind: ManagedDNSZone
      metadata:
        name: DNS_ZONE_NAME
        namespace: PROJECT_NAMESPACE
      spec:
        dnsName: example.com
        description: "Public DNS zone for example.com"
        visibility: PUBLIC
      status:
      …
      nameServers:
        - ns.managed-dns-public.gdc1.staging.gpcdemolabs.com
    

  2. Update the DNS resolver in your network to forward DNS requests for the new zone. For this example, the DNS resolver needs to be updated to forward requests for `example.com` to `ns.managed-dns-public.gdc1.staging.gpcdemolabs.com`. This configuration assumes that the resolver already has the configuration needed to appropriately forward DNS requests for GDC's infrastructure DNS zone `gdc1.staging.gpcdemolabs.com`.




## Create a private DNS zone

You can create a private DNS zone using the gdcloud CLI or the Kubernetes API.

###  gdcloud 

To create a private DNS zone, use the [`gdcloud dns managed-zones create`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-dns-managed-zones-create) command:
    
    
    gdcloud dns managed-zones create DNS_ZONE_NAME \
        --dns-name=DOMAIN_NAME \
        --visibility=PRIVATE \
        --description="DESCRIPTION" \
        [--project=PROJECT_NAMESPACE] \
        [--async]
    

Replace the following:

  * `DNS_ZONE_NAME`: the name of your DNS zone.
  * `DOMAIN_NAME`: the domain name for your private DNS zone, such as `example.com`.
  * `DESCRIPTION`: a description for your DNS zone. For example, `Private DNS zone for example.com`. This field is optional.
  * `PROJECT_NAMESPACE`: the namespace of your project. This flag is optional if you have set a default project globally using `gdcloud config set project`.
  * `--async`: Specify this if you want the command to return immediately, rather than wait for the operation to complete. You can use [`describe`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/list-dns-zones#list-dns-zones) to check on the status of the operation.



###  API 

Use the Kubernetes API to create a private DNS zone:

  * Create and apply a `ManagedDNSZone` resource to create a DNS zone accessible only from within the default customer VPC:
        
        kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
        apiVersion: networking.global.gdc.goog/v1
        kind: ManagedDNSZone
        metadata:
          name: DNS_ZONE_NAME
          namespace: PROJECT_NAMESPACE
        spec:
          dnsName: DOMAIN_NAME
          description: DESCRIPTION
          visibility: PRIVATE
        EOF
        

Replace the following:

    * `GLOBAL_API_SERVER`: the global API server's kubeconfig path. For more information, see [Global and zonal API servers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers). If you have not yet generated a kubeconfig file for the API server, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in) for details.
    * `DNS_ZONE_NAME`: the name of your DNS zone.
    * `PROJECT_NAMESPACE`: the namespace of your project.
    * `DOMAIN_NAME`: the domain name for your private DNS zone, such as `example.com`.
    * `DESCRIPTION`: a description for your DNS zone. For example, `Private DNS zone for example.com`. This field is optional.

Note that `visibility` is case sensitive, and must have the exact value `PRIVATE`.




## What's next

  * [Create a DNS record](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/create-dns-records)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
