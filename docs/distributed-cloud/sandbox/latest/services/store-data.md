---
url: https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/store-data/
title: Store data \u00a0|\u00a0 Google Distributed Cloud Sandbox \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:32.131206+00:00
---

# Store data  |  Google Distributed Cloud Sandbox  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/store-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Sandbox ](https://docs.cloud.google.com/distributed-cloud/sandbox/latest)



Send feedback 

#  Store data Stay organized with collections  Save and categorize content based on your preferences. 

GDC Sandbox lets you test your storage configurations to manage the size and capacity needs to store your data. For details on storage, see [Storage overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/application/ao-user/storage).

Before you configure and test storage, you must [install the storage CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/application/ao-user/install-configure-storage-cli). You can use the following GDC Sandbox-specific commands to fetch and configure the required certificate:
    
    
    curl -k https://console.org-1.zone1.google.gdch.test/.well-known/login-config | \
    grep certificateAuthorityData | head -1 | cut -d : -f 2 | awk '{print $1}' | \
    sed 's/"//g' | base64 --decode > gdc_trusted_certs.crt
    gdcloud config set storage/s3_custom_ca_certs_file gdc_trusted_certs.crt
    

Afterwards, create a storage bucket by following the steps in [Create storage buckets](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/application/ao-user/create-storage-buckets).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
