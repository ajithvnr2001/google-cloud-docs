---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/intro/
title: Setup and configuration overview \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:21:38.564580+00:00
---

# Setup and configuration overview  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/intro/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Setup and configuration overview Stay organized with collections  Save and categorize content based on your preferences. 

This section provides instructions for administrators to set up and configure Google Distributed Cloud (GDC) air-gapped appliance.

## Required equipment

You need the following equipment to set up and configure the appliance:

  1. Four power cables
  2. Three Yubikeys
  3. A USB drive with the following files: 
     1. SSH keys credentials (either in devices.csv or another file format)
     2. cables.csv
  4. A laptop or computer with Linux or macOS RJ45 cable, to connect the laptop or computer to the switch
  5. A RJ45 to USB-C adapter, to connect the laptop or computer to the switch



## Set up the appliance

  * [Unbox the device](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/unboxing-the-device)
  * [Verify cabling](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/check-cables)
  * [Insert the YubiKeys](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/setup-prerequisites)
  * [Connect the laptop to the switch](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/connect-the-device)
  * [Create input configuration file](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/create-input-ciq)
  * [Configure device and install software](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/setup)



## Configure advanced settings

  * [Configure external NTP](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/configure-ntp)
  * [Configure external HSM network connection](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/configure-hsm-network-connection)
  * [Set up IO tools to access runbooks](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/iotool-setup)
  * [Configure a SMTP notification channel for alerts](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/smtp-alerts)
  * Manage PKI certs: 
    * [Web TLS certificate configurations](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/pki/web-tls-cert-config)
    * [Transition to different modes](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/pki/transition-pki-modes)
    * [Change the default issuer](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/pki/change-default-issuer)
    * [Reissue PKI web certificates](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/pki/pki-cert-reissue)
  * [Configure secret rotations](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/configure-secret-rotations)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
