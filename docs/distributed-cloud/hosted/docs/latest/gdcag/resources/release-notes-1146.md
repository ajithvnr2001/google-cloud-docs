---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/release-notes-1146/
title: Google Distributed Cloud air-gapped 1.14.6 release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:33:02.563127+00:00
---

# Google Distributed Cloud air-gapped 1.14.6 release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/release-notes-1146/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Google Distributed Cloud air-gapped 1.14.6 release notes Stay organized with collections  Save and categorize content based on your preferences. 

## July 25, 2025

* * *

Announcement

Google Distributed Cloud (GDC) air-gapped 1.14.6 is available.  
See the [product overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/overview) to learn about the features of Distributed Cloud. 

* * *

Issue

The following issues are identified: 

**Cluster management**

  * Cluster gets stuck in a deleting state. 



**File/block storage** :

  * A fileshare volume in a VM cannot be mounted. 

  * User pod freezes during volume unmount request. 




**OS**

  * OS policy resources can be slow to reconcile when there are a large number of servers provisioned. 



**Servers**

  * Previously installed servers fail to provision after being deprovisioned and reprovisioned. 



**Ticketing system** :

  * An RBAC error from customer networks might deny access to ServiceNow. 



**Upgrade**

  * The org admin node upgrade is stuck. 

  * The add-on upgrade is stuck. 

  * The VM boot gets stuck after OS node upgrade. 




**Virtual machines**

  * The KRM image import takes a long time. 



* * *

Fixed

The following issues are fixed: 

**Cluster management:**

  * Removing obsolete node pools from standard clusters fails. Standard clusters are in private preview and might not be available to all customers. 



**Virtual machines:**

  * An image import fails. 



* * *

Change

The following changes are identified: 

**Version updates** :

  * The Google Distributed Cloud for bare metal version is updated to 1.30.1000-gke.85 to apply the latest security patches and important updates.   
  
See the [Google Distributed Cloud for bare metal 1.30.1000 release notes](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/release-notes-ver-2#June_10_2025) for details.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
