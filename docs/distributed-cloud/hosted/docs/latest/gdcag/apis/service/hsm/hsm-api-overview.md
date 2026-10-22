---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/hsm/hsm-api-overview/
title: Hardware security modules API overview \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:15:10.662629+00:00
---

# Hardware security modules API overview  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/hsm/hsm-api-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  Hardware security modules API overview Stay organized with collections  Save and categorize content based on your preferences. 

The hardware security modules (HSM) API provides the resources that the Platform Administrator (PA) uses to control the security keys in their organization. Storage systems in Google Distributed Cloud (GDC) air-gapped, such as Server Keys for disk encryption and storage data management software for block storage, create the keys and represent them as resources.

The PA views the keys, pulls their audit logs, and deletes them to erase data graphically. The PA cannot directly create keys. The storage systems create them as necessary.

**Note:** After the storage systems create the keys, it might take a few minutes for them to appear in each resource.

GDC encrypts all data at rest. It uses the HSM for all data at rest and all servers. Because you have access to the resource for keys, you can manage the keys that protect your data at rest. For more details on encryption in GDC, see [Encryption at rest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/encryption-at-rest).

**Warning:** Deleting keys wipes out your entire data. Delete your keys with caution for the stability of the system.

## Service endpoint and discovery document

Use the `kubectl proxy` command to access the following HSM API endpoint in your browser and obtain the discovery document for the KMS API:
    
    
    https://MANAGEMENT_API_SERVER_ENDPOINT/apis/hsm.gdc.goog/v1
    

Replace `MANAGEMENT_API_SERVER_ENDPOINT` with the endpoint of the Management API server.

The `kubectl proxy` command opens a proxy to the Kubernetes API server on your local machine. When the command is running, access the document through the following URL:

`http://127.0.0.1:8001/apis/hsm.gdc.goog/v1`

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
