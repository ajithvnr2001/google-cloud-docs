---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/tls/overview/
title: How AlloyDB Omni uses TLS \u00a0|\u00a0 AlloyDB Omni using the RPM orchestrator: 18.1.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:40:32.423989+00:00
---

# How AlloyDB Omni uses TLS  |  AlloyDB Omni using the RPM orchestrator: 18.1.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/tls/overview/

This page documents AlloyDB Omni version **18.1.0** using the **RPM orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM orchestrator: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/overview)



Send feedback 

#  How AlloyDB Omni uses TLS Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For information about access to this release, see the [ access request page](https://forms.gle/zxuHekMtV67Bw9Av9). 

Select a documentation version: 18.1.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/tls/overview)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/tls/overview)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/tls/overview)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/tls/overview)

AlloyDB Omni uses Transport Layer Security (TLS) to secure communications between itself and external components such as PostgreSQL clients, backup servers, and database applications. If you don't configure TLS yourself, then AlloyDB Omni configures it for you using self-signed certificates. 

For more information on configuring the TLS certificates required for AlloyDB Omni, see [Configure TLS certificates](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/tls/configure-tls-certificates).

The following diagram illustrates the communication and network paths used in AlloyDB Omni.

![Architecture diagram outlining the control and data connection paths from the AlloyDB Omni application and the load balancer and database cluster components](https://docs.cloud.google.com/static/alloydb/omni/redhat-orchestrator/18.1.0/docs/images/tls-architecture.png)

The following table lists each communication path and its required certificate.

Communication path | Required certificate  
---|---  
`etcd` <\--> `etcd` | `etcd` SSL certificate  
AlloyDB Omni orchestrator <\--> Cluster manager | Control path SSL certificate  
Cluster manager <\--> `etcd` | `etcd` SSL certificate  
Cluster manager <\--> Node manager | Control path SSL certificate  
PostgreSQL client <\--> HAProxy <\--> AlloyDB Omni | Data path SSL certificate  
PostgreSQL Client <\--> PgBouncer <\--> HAProxy <\--> AlloyDB Omni  | Data path SSL certificate  
AlloyDB Omni <\--> pgBackRest repository server | Data path SSL certificate  
AlloyDB Omni <\--> log server (ELK stack) | Data path SSL certificate  
  
## What's next

  * [Configure TLS certificates](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/tls/configure-tls-certificates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
