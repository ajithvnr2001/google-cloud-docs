---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/macsec/get-macsec-keys/
title: Get MACsec keys \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:34.498642+00:00
---

# Get MACsec keys  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/macsec/get-macsec-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Get MACsec keys Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to get your MACsec keys for MACsec for Cloud Interconnect.

MACsec for Cloud Interconnect generates GCM-AES-256 connectivity association key (CAK) and connectivity association key name (CKN) values. You use the values that MACsec for Cloud Interconnect generates when you configure your on-premises router. You can get the values at any time after configuring pre-shared keys on your Cloud Interconnect connection.

For more information, see [Configure your on-premises router](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/macsec/set-up-macsec#configure-your-on-premises-router).

## Required roles

To get the permissions that you need to retrieve MACsec keys, ask your administrator to grant you the [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

If you choose to use custom roles, ensure that your custom role for administrating MACsec for Cloud Interconnect includes the `compute.interconnects.getMacsecConfig` IAM permission.

## Get pre-shared keys

Select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the Cloud Interconnect **Physical connections** tab.

[Go to Physical connections](https://console.cloud.google.com/hybrid/interconnects/list?tab=interconnects)

  2. Select the connection that you want to view.

  3. On the **MACsec** tab, go to the **Pre-shared keys** section and find the name of the pre-shared key, and then click **View**. A window displays the connectivity association key (**CAK**) and the connectivity association key name (**CKN**). Click the **Copy** button to copy each value to your computer's clipboard.

  4. Click **Close**.




###  gcloud 

Run the following command:
    
    
    gcloud compute interconnects macsec get-config INTERCONNECT_CONNECTION_NAME
    

Replace `INTERCONNECT_CONNECTION_NAME` with the name of your Cloud Interconnect connection.

The output is similar to the following:
    
    
    preSharedKeys:
    - cak: 0123456789abcdef...0123456789abcdef
      ckn: 0101016789abcdef...0123456789abcdef
      name: key1
      startTime: 2023-07-01T21:00:01.000Z
    

## What's next?

  * [Rotate MACsec keys](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/macsec/rotate-macsec-keys)
  * [View MACsec status](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/macsec/view-macsec-status)
  * [Troubleshoot MACsec](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/macsec/troubleshoot-macsec)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
