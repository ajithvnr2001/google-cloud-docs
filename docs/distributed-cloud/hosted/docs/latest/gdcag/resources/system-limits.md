---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/system-limits/
title: System limits \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:19:50.192161+00:00
---

# System limits  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/system-limits/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  System limits Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the system limits that apply to Google Distributed Cloud (GDC) air-gapped. System limits are fixed values that cannot be changed.

System limits are applicable to all audience groups, and must be understood by each operator, platform administrator, and application developer to successfully use GDC. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## System limits

The following tables list the system limits that apply to components of GDC, and the value for each system limit.

**Important:** Google supports all system limits, but actual limits might be higher.

### Certificate Authority Service

System limit | Value | Notes  
---|---|---  
Maximum certificate requests per organization using `kubectl` | 5,000 | Applies to `CertificateRequest` custom resources. Exceeding this limit can degrade Certificate Authority Service and Management API Server performance.  
  
Operate within the limit by [deleting old or unnecessary `CertificateRequest` resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/ca-service/request-cert#delete-cert).   
Maximum certificate requests per organization using REST API | None | Unlike requests made using `kubectl`, certificate requests made through the REST API don't create persistent `CertificateRequest` custom resources, so no quota limit applies. For more information, see [Certificate request quota](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/ca-service/request-cert#request-quota).   
  
### Cluster management

System limit | Value | Notes  
---|---|---  
Maximum number of pods in a node | 110 | The current allocation of pods is based on IP address considerations for any given node.  
Maximum number of nodes in a Kubernetes cluster | 50 | The recommended node limit is 20 nodes for maintainability consideration. The maximum verified number of nodes in a cluster is 50. The maximum number of pods in a cluster is a factor of \\( 110 \times \text{number of nodes} \\).  
Minimum number of worker nodes in a Kubernetes cluster | 3 | If you create the minimum of three worker nodes in your Kubernetes cluster, you must allocate the machine type for the worker nodes as `n2-standard-8` or use GPU machines.  
Maximum number of standard clusters | Organization and project limited | The maximum number of standard clusters depends on the upper limit of the organization and the available vCPU and IP addresses. Any restrictions placed on a project by a platform administrator might further restrict the number of standard clusters you can create.  
Maximum number of shared clusters | Organization limited | The maximum number of shared clusters depends on the upper limit of the organization and the available vCPU and IP addresses.  
Maximum cluster name size | 50 characters |   
  
### Database

System limit | Value | Notes  
---|---|---  
Maximum number of single-zone database clusters per organization | 153 |   
Maximum number of Postgres connections per database cluster | 6000 | The number of maximum connections is highly dependent on workload, database CPU, and memory. When using up to 6000 connections, we recommend 64 vCPU and 1 TB of RAM, though lower CPU and RAM settings might work depending on the workload.  
Maximum storage size per database | 2 TB |   
  
### Cloud DNS Service

System limit | Value | Notes  
---|---|---  
Default limit for number of public DNS zones per organization | 25 | Contact your Infrastructure Operator (IO) to view your current limit or request an increase up to a maximum of 150 public DNS zones.  
Default limit for number of private DNS zones per organization | 75 | Contact your Infrastructure Operator (IO) to view your current limit or request an increase up to a maximum of 150 private DNS zones.  
Maximum number of resource record sets per DNS zone | 500 |   
Maximum number of Resource Record sets across all DNS zones per organization | 35,000 |   
  
### Logging

System limit | Value | Notes  
---|---|---  
Maximum data read per log query | 200 GB | Restricts a single Loki query from scanning more than 200 GB of log data.  
Maximum log lines returned per query | 5,000 | Limits the maximum number of log lines returned at a time for a single query.  
  
### Managed Harbor Service

System limit | Value | Notes  
---|---|---  
Maximum Harbor registry instances per organization | 5 |   
Maximum Harbor registry instances per GDC project | 1 | A GDC project is limited to a single Harbor instance, and multiple GDC projects can share a single Harbor instance  
Maximum Harbor registry image layer size | 128 GB |   
Maximum Harbor registry storage size | 1 TB | This storage limit might vary depending on the total storage available in object storage.  
Maximum concurrent requests | 30 | The artifact sizes vary from 1 KB to 1 GB.  
  
### Monitoring

System limit | Value | Notes  
---|---|---  
Maximum labels per metric | 40 |   
Maximum active time series per metric | 50,000 | Active time series refers to a unique metric label name/value combination that has recently received new data (samples).  
Maximum label value size | 2048 bytes |   
Maximum label name size | 1024 bytes |   
Maximum query range | 30 days | Restricts a single query from spanning more than 30 days of data.  
Maximum query period lookback | 90 days | Restricts queries to data within the last 90 days (start time must be greater than or equal to now-90 days).  
Maximum time series fetched per query | 100,000 | Queries that attempt to fetch more than 100,000 distinct time series are not allowed.  
Maximum samples per query | 50,000,000 | Limits the total number of samples loaded into memory for a query.  
  
### Multi-zone

System limit | Value | Notes  
---|---|---  
Maximum number of zones per universe | 6 |   
Maximum number of zones per region | 6 |   
  
### Object storage

System limit | Value | Notes  
---|---|---  
Maximum single-part object upload size | 5 GB |   
Maximum multi-part object upload size | 5 TB |   
  
### Resource Manager

System limit | Value | Notes  
---|---|---  
Maximum project name size | 30 characters | A minimum of four characters must be used for the project name. A project name can contain letters, numbers, single quotes, hyphens, spaces, or exclamation points. For more information, see [Project identifiers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/project-management#project-identifiers).  
Maximum project ID size | 30 characters | A minimum of six characters must be used for the project ID. A project ID can contain lowercase letters, numbers, and hyphens. For more information, see [Project identifiers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/project-management#project-identifiers).   
Maximum number of organizations per zone | 10 |   
Maximum number of projects per organization | 100 |   
Minimum physical servers per customer organization per zone | 6 physical servers | The physical server number contains three control plane servers and three worker servers.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
