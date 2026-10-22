---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/configure-secret-rotations/
title: Configure secret rotations \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:44.971754+00:00
---

# Configure secret rotations  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/configure-secret-rotations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Configure secret rotations Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the resources for information on how to set up and configure secret rotations for Google Distributed Cloud (GDC) air-gapped appliance.

  1. BM SSH keys and certificate: [PLATAUTH-G0003](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/gdch-io/service-manual/platauth/guides/platauth-g0003)
  2. Chassis certificate, username and password rotation: [APPL-G0001](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/gdch-io/service-manual/appl/guides/appl-g0001)
  3. Changing the iLO username and password for Baseboard Management Controller (BMC) and chassis: 
     1. Integrated Lights-Out (iLO) credential rotation: [SERV P0002](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/gdch-io/service-manual/serv/processes/serv-p0002)
     2. BMC certificate rotation: [SERV P0003](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/gdch-io/service-manual/serv/processes/serv-p0003)
     3. Ironic certificate rotation: [SERV P0004](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/gdch-io/service-manual/serv/processes/serv-p0004)
  4. Harbor: 
     1. In-cluster Harbor admin credentials rotation: [SAR-R2001](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/gdch-io/service-manual/sar/runbooks/sar-r2001)
     2. Harbor robot account credentials rotation: [SAR-R2003](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/gdch-io/service-manual/sar/runbooks/sar-r2003)
     3. Rotating SAR certificates: [SAR-T0001](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/gdch-io/service-manual/sar/toil/sar-t0001)
     4. Rotating Harbor components credentials: [SAR-T0002](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/gdch-io/service-manual/sar/toil/sar-t0002)
  5. Identity provider secrets rotation: 
     1. Keycloak: [IAM-T0001](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/gdch-io/service-manual/iam/toil/iam-t0001)
  6. Object storage: 
     1. [Object storage credentials](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/object-storage-key-rotation).
     2. [Disk encryption keys](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/disk-encryption-key-rotation).
     3. [Storage authentication keys and certificates](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/storage-auth-key-and-cert-rotation).
  7. Physical networking (PNET): 
     1. Switch credentials: [`gdcloud appliance rotate switch-credentials`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-appliance-rotate-switch-credentials)
     2. Switch certificate: [`gdcloud appliance rotate switch-certificate`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-appliance-rotate-switch-certificate)



To access the runbooks in the IO tools container, see [Set up the IO tools to access runbooks](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/iotool-setup)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
