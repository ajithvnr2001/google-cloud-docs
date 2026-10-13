---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/rotate-cert/
title: Manage internal network access compliance \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:21:57.398288+00:00
---

# Manage internal network access compliance  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/rotate-cert/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Manage internal network access compliance Stay organized with collections  Save and categorize content based on your preferences. 

After the device is bootstrapped successfully, the administrator must rotate the secrets every three months to ensure that the device is compliant and secure.

## Before you begin

Complete the following steps:

  1. Ensure that you meet the [laptop prerequisites](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/laptop).
  2. Complete the following actions regarding the `gdcloud` command-line interface (CLI) tools: 
     1. [Download](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-download) the `gdcloud` CLI tools.
     2. [Install](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-install) the `gdcloud` CLI tools.
     3. [Upgrade](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-upgrade) the `gdcloud` CLI tools as required.



## Rotate the network access secrets

To rotate network access secrets, complete the following steps on the bootstrapper machine:

  1. Connect a bootstrapper machine to port 12 of the switch.
  2. Set up the bootstrapper IPs:
         
         gdcloud appliance system network init \
           --config CELLCONFIG\
           --data-interface DATA_INTERFACE
         

Replace the following:

     * `CELLCONFIG`: the path to the cellconfig generated after [configuring the appliance](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/setup#configure-the-appliance).
     * `DATA_INTERFACE`: the network interface name on the bootstrapper connected to port 12 of the switch.
  3. Rotate the TLS certificate on the switch:
         
         gdcloud appliance rotate switch-certificate \
           --kubeconfig KUBECONFIG
         

Replace `KUBECONFIG` with the path to the kubeconfig file for the org infrastructure cluster saved during the [emergency credentials setup](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/setup#back_up_emergency_credentials).

The certificate that you generated is valid for three months and is not renewed until you manually rotate the certificate using the preceding process. Keep track of the date when you rotated the TLS certificate so that you know when to repeat this process. Generate the certificate every three months. Failing to rotate the TLS certificate every three months will result in network secret rotation failure, as well as [upgrade](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/update-patch) failure.

  4. Rotate all login passwords on the switch:
         
         gdcloud appliance rotate switch-credentials \
           --kubeconfig KUBECONFIG
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
