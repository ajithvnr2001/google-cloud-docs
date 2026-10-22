---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/delete-dns-zones/
title: Delete DNS zones \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:30:08.465012+00:00
---

# Delete DNS zones  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/delete-dns-zones/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Delete DNS zones Stay organized with collections  Save and categorize content based on your preferences. 

This document guides you on how to delete a previously created public and private DNS zone in Google Distributed Cloud (GDC) air-gapped, when it is empty and no longer needed. The intended audience for this document is platform administrators and application operators responsible for managing DNS records within a project.

## Before you begin

To delete DNS zones in GDC, you must have the following:

  * An existing DNS zone to delete. See [List DNS zones](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/list-dns-zones) for guidance on listing your current zones.
  * The necessary identity and access roles. To manage DNS records for your project, ask your **IAM Project Admin** to grant you the **Managed DNS Project Admin** (`managed-dns-project-admin`) role.
  * To use the gdcloud CLI, ensure you have it installed. For more information, see [Install the gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-install).
  * If you are using `kubectl`, a kubeconfig file for the global API server. If you have not yet generated this file, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#global-resources-kubeconfig). For more information, see [Global and zonal API servers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers).

**Caution:** Ensure that the DNS zone has no existing DNS records. You must delete all DNS records within a DNS zone before deleting the zone itself. Refer to [List DNS records](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/list-dns-records) and [Delete DNS records](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/delete-dns-records) to clear these records first.

## Delete a public or private DNS zone

You can delete a public or private DNS zone using the gdcloud CLI or the Kubernetes API.

###  gdcloud 

To delete a DNS zone, use the [`gdcloud dns managed-zones delete`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-dns-managed-zones-delete) command:
    
    
    gdcloud dns managed-zones delete DNS_ZONE_NAME \
        [--project=PROJECT_NAMESPACE] \
        [--async]
    

Replace the following:

  * `DNS_ZONE_NAME`: the name of your DNS zone to delete.
  * `PROJECT_NAMESPACE`: the namespace of your project. This flag is optional if you have set a default project globally using `gdcloud config set project`.
  * `--async`: Specify this if you want the command to return immediately, rather than wait for the operation to complete. You can use [`describe`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/list-dns-zones#list-dns-zones) to check on the status of the operation.



###  API 

Use the Kubernetes API in GDC to delete a public or private DNS zone:
    
    
    kubectl --kubeconfig GLOBAL_API_SERVER \
    delete manageddnszones.networking.global.gdc.goog/v1 DNS_ZONE_NAME \
    -n PROJECT_NAMESPACE
    

Replace the following:

  * `GLOBAL_API_SERVER`: the global API server's kubeconfig path. For more information, see [Global and zonal API servers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers). If you have not yet generated a kubeconfig file for the API server, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in) for details.
  * `DNS_ZONE_NAME`: the name of your DNS zone which needs to be deleted.
  * `PROJECT_NAMESPACE`: the namespace of your project.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
