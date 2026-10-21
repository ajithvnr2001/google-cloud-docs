---
url: https://docs.cloud.google.com/secure-access-connect/docs/overview/
title: Secure Access Connect overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:08:42.311810+00:00
---

# Secure Access Connect overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-access-connect/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Secure Access Connect ](https://docs.cloud.google.com/secure-access-connect/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-access-connect/docs/overview)



Send feedback 

#  Secure Access Connect overview Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview of Secure Access Connect. Secure Access Connect lets you attach security service edge (SSE) services to NCC Gateway for security processing and secure access to the internet or your applications. For more information about NCC Gateway, see the [NCC Gateway overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/ncc-gateway-overview).

Secure Access Connect is made up of realms and attachments. A Secure Access Connect realm is a global resource that links your Google Cloud project and an Secure Access Connect attachment is a regional resource that enables NCC Gateway to process traffic with an SSE service.

For a list of supported locations, see [Locations supported for NCC Gateway](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/supported-locations).

## Supported SSE providers

Secure Access Connect supports connections to the following SSE products:

  * [Palo Alto Networks Prisma Access](https://docs.paloaltonetworks.com/prisma-access/integration/ncc-gateway-integration-in-prisma-access)
  * [Symantec Cloud Secure Web Gateway (Cloud SWG)](https://techdocs.broadcom.com/us/en/symantec-security-software/web-and-network-security/cloud-swg/help/conn-matrix/adm_addlocation_st/express-connect.html) ([Preview](https://cloud.google.com/products#product-launch-stages))



## Considerations

Before you set up Secure Access Connect, make sure that the following requirements are met:

If you are connecting to Symantec Cloud SWG ([Preview](https://cloud.google.com/products#product-launch-stages)), ensure the following:

  * The Symantec location must not already be in use by another attachment that you are using.
  * Your secret key must be valid.



## Set up Secure Access Connect

Setting up Secure Access Connect is one step of the process to [set up NCC Gateway](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/setup-overview). To set up Secure Access Connect, do the following:

  1. [Create a Secure Access Connect realm](https://docs.cloud.google.com/secure-access-connect/docs/create-realms)
  2. [Create Secure Access Connect attachments](https://docs.cloud.google.com/secure-access-connect/docs/create-attachments)



## Manage Secure Access Connect

After you have configured Secure Access Connect, you can manage it by doing the following:

  * [View Secure Access Connect realm information](https://docs.cloud.google.com/secure-access-connect/docs/view-realms)
  * [View Secure Access Connect attachment information](https://docs.cloud.google.com/secure-access-connect/docs/view-attachments)
  * [Delete Secure Access Connect realms and attachments](https://docs.cloud.google.com/secure-access-connect/docs/delete-realms-attachments)

**Note:** You can't edit realms and attachments after you create them. To make any changes to an existing realm or attachment, you must delete it and then create a new one.



## Pricing

For pricing information, see [NCC Gateway pricing](https://cloud.google.com/network-connectivity/pricing#ncc-gateway-pricing).

## What's next?

  * [Create a realm](https://docs.cloud.google.com/secure-access-connect/docs/create-realms)
  * Learn more about [NCC Gateway](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/ncc-gateway-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
