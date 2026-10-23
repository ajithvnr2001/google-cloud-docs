---
url: https://docs.cloud.google.com/managed-microsoft-ad/docs/fgpp-concepts/
title: About fine-grained password policies \u00a0|\u00a0 Managed Service for Microsoft Active Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:00.219147+00:00
---

# About fine-grained password policies  |  Managed Service for Microsoft Active Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/docs/fgpp-concepts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview)



Send feedback 

#  About fine-grained password policies Stay organized with collections  Save and categorize content based on your preferences. 

This page explains the fine-grained password policies (FGPP) concepts and related best practices for Managed Service for Microsoft Active Directory.

## Overview

You can use [FGPP](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc770394\(v=ws.10\)) to define and enforce strong password settings on a specific Active Directory user or group. Note that password policies are different from the default domain password policy which is configured by a group policy and linked to the root of the domain.

FGPP is set in Password Settings Objects (PSO). Each PSO has a precedence value that indicates its priority. The lower this value, the higher the priority of that PSO. Managed Microsoft AD creates ten PSOs with default settings. You cannot change the names or precedences of these PSOs, but you can change the settings. For more information about the pre-created PSOs, see [Password Settings Objects](https://docs.cloud.google.com/managed-microsoft-ad/docs/objects#password_settings_objects).

### Policy settings

Each PSO can contain the following policy settings:

  * [Complexity enabled](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/password-must-meet-complexity-requirements)

  * [Lockout duration](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/hh994569\(v=ws.10\))

  * [Lockout observation window](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/hh994568\(v=ws.10\))

  * [Lockout threshold](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/hh994574\(v=ws.10\))

  * [Maximum password age](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/hh994573\(v=ws.10\))

  * [Minimum password length](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/hh994560\(v=ws.10\))

  * [Password history count](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/enforce-password-history)

  * [Reversible encryption enabled](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/hh994559\(v=ws.10\))




## What's next

  * [Configure fine-grained password policies](https://docs.cloud.google.com/managed-microsoft-ad/docs/how-to-use-fgpp)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
