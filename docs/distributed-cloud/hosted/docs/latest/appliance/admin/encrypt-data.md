---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/encrypt-data/
title: Data encryption \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:43.557875+00:00
---

# Data encryption  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/encrypt-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Data encryption Stay organized with collections  Save and categorize content based on your preferences. 

**Important:** To access the URLs on this page, you must connect to the internet. The URLs are provided for use when you have such access.

This section describes the different layers of encryption in storage. Google Distributed Cloud (GDC) air-gapped appliance 

## Encryption at rest

There are different layers of data at rest encryption that GDC air-gapped appliance provides. 

## Encryption in transit

Data in transit is encrypted using IPsec on two types of OTS traffic:

  * External traffic between bare metal hosts and OTS Storage Virtual Machines (SVMs).
  * Internal traffic between OTS worker nodes.



The IPsec on both traffic is implemented by the third party library strongSwan (<https://strongswan.org/>). The OTS internal traffic is built with the OpenVSwitch vxlan tunnel and it also uses strongSwan to encrypt the data flow under the layer.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
