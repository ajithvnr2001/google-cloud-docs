---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/list-dns-zones/
title: List DNS zones \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:22:15.421735+00:00
---

# List DNS zones  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/list-dns-zones/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  List DNS zones Stay organized with collections  Save and categorize content based on your preferences. 

This document guides you on how to list all previously created public and private DNS zones in Google Distributed Cloud (GDC) air-gapped.

## Before you begin

To list DNS zones in GDC, you must have the following:

  * The necessary identity and access roles. To list DNS records for your project, ask your **IAM Project Admin** to grant you the **Managed DNS Project Viewer** (`managed-dns-project-viewer`) role.
  * To use the gdcloud CLI, ensure you have it installed. For more information, see [Install the gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-install).
  * If you are using `kubectl`, a kubeconfig file for the global API server. If you have not yet generated this file, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#global-resources-kubeconfig). For more information, see [Global and zonal API servers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers).



## List public or private DNS zones

You can list public or private DNS zones using the gdcloud CLI or the Kubernetes API.

###  gdcloud 

To list all DNS zones in a project, use the [`gdcloud dns managed-zones list`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-dns-managed-zones-list) command:
    
    
    gdcloud dns managed-zones list \
        [--project=PROJECT_NAMESPACE]
    

To fetch a single DNS zone by name, use the [`gdcloud dns managed-zones describe`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-dns-managed-zones-describe) command:
    
    
    gdcloud dns managed-zones describe DNS_ZONE_NAME \
        [--project=PROJECT_NAMESPACE]
    

Replace the following:

  * `DNS_ZONE_NAME`: the name of your DNS zone to fetch.
  * `PROJECT_NAMESPACE`: the namespace of your project. This flag is optional if you have set a default project globally using `gdcloud config set project`.



###  API 

Use the Kubernetes API in GDC to list public and private DNS zones.

To fetch a single DNS zone by name:
    
    
    kubectl --kubeconfig GLOBAL_API_SERVER get manageddnszones.networking.global.gdc.goog/v1 DNS_ZONE_NAME -n PROJECT_NAMESPACE
    

To list all DNS zones in a project:
    
    
    kubectl --kubeconfig GLOBAL_API_SERVER get manageddnszones.networking.global.gdc.goog/v1 -n PROJECT_NAMESPACE
    

Replace the following:

  * `GLOBAL_API_SERVER`: the global API server's kubeconfig path. For more information, see [Global and zonal API servers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers). If you have not yet generated a kubeconfig file for the API server, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in) for details.
  * `DNS_ZONE_NAME`: the name of your DNS zone to fetch.
  * `PROJECT_NAMESPACE`: the namespace of your project.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
