---
url: https://docs.cloud.google.com/workload-manager/docs/observe/sap/supported-sap-systems/
title: Supported SAP systems \u00a0|\u00a0 Workload Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:07:04.623582+00:00
---

# Supported SAP systems  |  Workload Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/observe/sap/supported-sap-systems/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/workload-manager/docs/overview)



Send feedback 

#  Supported SAP systems Stay organized with collections  Save and categorize content based on your preferences. 

This document provides the list of SAP systems and architectures that you can monitor using the observability service in Workload Manager.

## Supported SAP systems

This section lists the SAP systems and operating systems that Workload Manager supports for observability.

### SAP products

**SAP Applications** | **Types**  
---|---  
SAP NetWeaver-based applications | ABAP and Java Note that some information on the application dashboards are specific to ABAP-based applications and those widgets appear empty for Java-based applications.  
  
### Databases

**Database** | **Version**  
---|---  
SAP HANA | 2.0 or later  
  
### Database scaling methods

**Database Scale Type** | **Description**  
---|---  
Scale-up | Single-node configuration  
Scale-out |  Multi-node configuration Workload Manager doesn't support observability for SAP HANA scale-out HA systems. For information about such limitations, see Limitations.  
  
### Supported operating systems

Workload Manager supports the following operating systems that are certified by SAP for production use with SAP on Google Cloud. For a complete list of versions of the supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning#supported_operating_systems).

  * RHEL for SAP
  * SUSE Linux Enterprise Server (SLES) for SAP



### Supported architecture

**Architecture** | **Description**  
---|---  
Centralized | An SAP system that uses a single compute instance to run all its components.  
Distributed | An SAP system that uses multiple compute instances to run its components. ASCS, PAS, application and database servers are running on separate compute instances.  
Distributed with high availability (HA) |  An SAP system using a distributed deployment model, with application servers running across two or more zones in the same region. The system must satisfy the following conditions:

  * The SAP system must be set up across two or more zones in the same region.
  * The SAP system must use an HA cluster for both, the SAP Central Services instance and the SAP HANA database.

  
Standalone SAP HANA database | An SAP HANA database on a single compute instance.  
Standalone HANA database with high availability (HA) | An SAP HANA database using a distributed deployment model across two or more zones in the same region.  
  
If your SAP system includes a disaster recovery (DR) site, then the DR site is displayed as a secondary instance in the **Overview** tab of the Workload Manager observability dashboard.

### Limitations

Workload Manager doesn't support setting up observability for the following system types:

  * Distributed systems that don't have an HA cluster for both the SAP Central Services instance and the SAP HANA database.
  * SAP HANA scale-out HA systems.



## What's next

  * Read about the [prerequisites for SAP observability](https://docs.cloud.google.com/workload-manager/docs/observe/sap/prerequisites).
  * Learn how to [observe an SAP workload](https://docs.cloud.google.com/workload-manager/docs/observe/sap/view-dashboards).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
