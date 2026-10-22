---
url: https://docs.cloud.google.com/distributed-cloud/gemini-on-gdcc/latest/docs/how-it-works/
title: How Gemini on GDC connected API on GDC connected works \u00a0|\u00a0 Gemini on GDC API on GDC connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:11.108795+00:00
---

# How Gemini on GDC connected API on GDC connected works  |  Gemini on GDC API on GDC connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/gemini-on-gdcc/latest/docs/how-it-works/

**Gemini on GDC API on GDC connected Public Preview (current)**

For version information, see the [Gemini on GDC API on GDC connected release notes](https://docs.cloud.google.com/distributed-cloud/gemini-on-gdcc/latest/docs/release-notes). 

Available versions: **Public Preview**

  * [ Home ](https://docs.cloud.google.com/)
  * [ Gemini on GDC API on GDC connected ](https://docs.cloud.google.com/distributed-cloud/gemini-on-gdcc/latest)
  * [ Documentation ](https://docs.cloud.google.com/distributed-cloud/gemini-on-gdcc/latest/docs)
  * [ Guides ](https://docs.cloud.google.com/distributed-cloud/gemini-on-gdcc/latest/docs/overview)



Send feedback 

#  How Gemini on GDC connected API on GDC connected works Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Warning:** During the Preview period, you may only use Gemini on GDC connected API for evaluation and testing purposes. You may not use the Preview release of Gemini on GDC connected API for commercial or production purposes, or disclose generated output to a third party.

This page describes how Gemini on Google Distributed Cloud connected API works, including information about its infrastructure, hardware and software capabilities.

## Overview

Gemini on GDC connected API is a turnkey software solution that lets you deploy Gemini models on your own Google-certified hardware connected to your local network. The models are hosted within Confidential Virtual Machines (CVMs) deployed on [Distributed Cloud connected](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/overview) clusters. The required hardware has a specific configuration established and certified by Google.

## Google-certified hardware

Gemini on GDC connected API requires Google-certified hardware configured exactly as described in [Google-certified hardware](https://docs.cloud.google.com/distributed-cloud/gemini-on-gdcc/latest/docs/requirements#hardware). You must order and install this hardware on your premises before ordering Gemini on GDC connected API. You must provide the corresponding service tags and other hardware identification information to Google when ordering Gemini on GDC connected API, as described in [Installation requirements](https://docs.cloud.google.com/distributed-cloud/gemini-on-gdcc/latest/docs/requirements).

The Google-certified hardware has the following specifications:

  * **Platform:** Dell XE9680 server chassis
  * **CPU:** Two (2) Intel Xeon Platinum 8592+ 64-core processors
  * **Memory** : 2TB DDR5 5600 MT/s RDIMM RAM
  * **GPU:** NVIDIA HGX H200 SXM assembly with eight (8) NVIDIA H200 series GPUs
  * **Storage** : FIPS-certified NVMe storage configured as follows: 
    * 2x 960 GB drives in hardware RAID1 for the operating system
    * 2x 15.36 TB drives in software RAID1 reserved for system-reserved functions
    * 6x 15.36 TB drives for storing data for the confidential virtual machines that locally serve your Gemini on GDC connected API endpoints.
  * **Networking** : 
    * Two (2) Mellanox ConnectX-6 dual-port 100 GbE QFSP56 network adapters
    * One (1) integrated Broadcom 5720 1 GbE network adapter
  * **Management** : Integrated Dell Remote Access Controller 9 (iDRAC9) Datacenter 16G for embedded system management
  * **Power:** Six (6) 2800W Titanium-certified power supplies



A single deployment of Gemini on GDC connected API consists of one (1) Google-certified machine. Gemini on GDC connected API **does not** run on non-Google-certified hardware configurations.

## Confidential virtual machines

The models served by Gemini on GDC connected API are hosted within Confidential Virtual Machines running on [Distributed Cloud connected](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/overview) clusters. Remote attestation ensures the security and integrity of the deployed CVMs and the secure software environment that runs them.

## Remote attestation

Gemini on GDC connected API requires a constant internet connection to maintain remote attestation of the deployed CVMs and the secure software environment that hosts them. The attestation mechanism is implemented using [Intel® Software Guard Extension (Intel® SGX) Remote Attestation Services](https://www.intel.com/content/www/us/en/developer/tools/software-guard-extensions/attestation-services.html). You must have an Intel® SGX Provisioning Certification Service subscription and provide the corresponding API keys to Google when ordering Gemini on GDC connected API.

### Remote attestation failure

The remote attestation service establishes a heartbeat between your Gemini on GDC connected API deployment and Google, which requires an uninterrupted internet connection. If this heartbeat is interrupted for more than 30 consecutive minutes, the CVMs are shut down until the heartbeat is reestablished. Contact your Google representative to resolve attestation failures.

## Supported models

This release of Gemini on GDC connected API supports the following models:

  * **Gemini 2.5 Flash 128k** with public ID `gemini-2.5-flash` and prompt ID `gemini-2.5-flash-ggc`.



Use the public ID of the model for all commands except interacting with its endpoint to create prompt requests. Use the prompt ID when creating prompt requests and sending them to the endpoint.

## Deployment steps

At a high level, the deployment of a Gemini model on Gemini on GDC connected API looks as follows:

  1. Procure and install the Google-certified hardware, as described in [Hardware](https://docs.cloud.google.com/distributed-cloud/gemini-on-gdcc/latest/docs/requirements#hardware).
  2. Complete the steps necessary to satisfy all of the installation requirements described in [Installation requirements](https://docs.cloud.google.com/distributed-cloud/gemini-on-gdcc/latest/docs/requirements).
  3. Order Gemini on GDC connected API as described in [Order Gemini on Google Distributed Cloud connected API on Distributed Cloud connected](https://docs.cloud.google.com/distributed-cloud/gemini-on-gdcc/latest/docs/order). When ordering, you must provide the information listed in [Installation requirements](https://docs.cloud.google.com/distributed-cloud/gemini-on-gdcc/latest/docs/requirements#provide-info) so that Google can provision your Gemini on GDC connected API deployment for software management and remote attestation of the CVMs that host the models you want to deploy.
  4. Schedule a visit with a Google technician who must visit your location to install and configure the Gemini on GDC connected API software on your Google-certified hardware.
  5. Enable the required APIs, as described in [Enable the required APIs](https://docs.cloud.google.com/distributed-cloud/gemini-on-gdcc/latest/docs/requirements#enable-apis).
  6. Set up a Cloud Billing account for your target Google Cloud project as described in [Create a new self-serve Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account).
  7. Grant your Gemini on Google Distributed Cloud connected API administrators and Gemini on GDC connected API model consumer accounts the required roles, as described in [Grant the required roles](https://docs.cloud.google.com/distributed-cloud/gemini-on-gdcc/latest/docs/endpoints#grant-roles).
  8. Create and deploy your Gemini on GDC connected API endpoints, as described in [Deploy a Gemini on GDC connected API endpoint](https://docs.cloud.google.com/distributed-cloud/gemini-on-gdcc/latest/docs/endpoints#deploy-endpoint).
  9. Interact with your deployed Gemini on GDC connected API endpoints as described in [Interact with a Gemini on GDC connected API endpoint](https://docs.cloud.google.com/distributed-cloud/gemini-on-gdcc/latest/docs/endpoints#interact-endpoint).



## What's next

  * [Installation requirements](https://docs.cloud.google.com/distributed-cloud/gemini-on-gdcc/latest/docs/requirements)
  * [Order Gemini on Google Distributed Cloud connected API on Distributed Cloud connected](https://docs.cloud.google.com/distributed-cloud/gemini-on-gdcc/latest/docs/order)
  * [Create and manage endpoints](https://docs.cloud.google.com/distributed-cloud/gemini-on-gdcc/latest/docs/endpoints)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
