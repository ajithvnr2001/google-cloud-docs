---
url: https://docs.cloud.google.com/recaptcha/docs/identify-attacks/
title: Identify and investigate attacks \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:50:29.148960+00:00
---

# Identify and investigate attacks  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/identify-attacks/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Identify and investigate attacks Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to use the Attacks and Investigations feature to identify and investigate security threats such as credential stuffing. 

Google Cloud Fraud Defense detects attacks and displays them on the **Attacks** page in the Google Cloud console. You can view a list of potential attacks and drill down into investigation details to understand the scope and impact of an attack.

**Note:** This feature is only available to Enterprise subscription customers.

## Overview

The Attacks and Investigations feature helps you identify attacks targeting your sites. Fraud Defense analyzes your traffic to identify patterns of abuse. Fraud Defense detects abnormal behavior and flags it as a potential attack.

## Supported attack types

Attacks are categorized by type. Understanding the attack type can help you tailor your investigation. The following attack types are supported:

**Credential Stuffing** : This type of attack uses lists of stolen usernames and passwords to attempt to gain unauthorized access to user accounts.

**Scraping** : This type of attack uses automated bots to extract large amounts of data from your websites.

## View and investigate attacks

To view a list of detected attacks, go to the [**Attacks**](https://console.cloud.google.com/security/recaptcha/attacks) page in the Google Cloud console.

The **Attacks** page lists detected attacks along with key information to help you identify and prioritize threats. Clicking on an attack opens the **Attack details** page, which provides a comprehensive investigation view.

To understand an attack's scope, start by assessing its impact. The information in the **Attack details** page helps you understand the scale of the incident so you can prioritize which investigations require immediate attention.

### Analyze traffic patterns

Use the event timeline to help you visualize the attack lifecycle. Look for spikes in **Fraudulent** activity to identify when the attack was most aggressive. If available, review **Potentially Legitimate** events. These requests appear legitimate but share patterns with the detected attack, which can indicate sophisticated bot behavior or a compromised network.

## Identify and block threats

To stop the attack and prevent future ones, you need to identify its characteristics and origin. The detailed event list lets you inspect individual requests for commonalities. Look for patterns in the following data within the events:

  * **Site reported user IP:** Check if attacks are originating from a specific subnet.
  * **Site reported user agent:** Identify specific browser versions or bot signatures.
  * **Account defense label:** Look for signs of suspicious login activity or account takeovers.
  * **Score:** Review how Fraud Defense is scoring these specific requests.



Use these insights to configure your firewall rules or adjust your Fraud Defense security policies.

## Manage investigation status

You can track the progress of your investigations by updating the status. To change the status, click **Set status** on the **Attack details** page and select the appropriate status:

  * **New:** The default status for a newly detected attack.
  * **Active:** Indicates that the investigation is in progress.
  * **Closed:** Indicates that you finished investigating the attack. If new suspicious events are detected later, the status automatically changes from **Closed** to **Active**.



## What's next

  * Learn about the [user accounts protection features of Fraud Defense](https://docs.cloud.google.com/recaptcha/docs/protect-accounts-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
