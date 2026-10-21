---
url: https://docs.cloud.google.com/speech-to-text/docs/iam/
title: Access control with IAM \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:06:26.900700+00:00
---

# Access control with IAM  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/iam/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



Send feedback 

#  Access control with IAM Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud offers [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam), which lets you give more granular access to specific Google Cloud resources, and prevent unwanted access to other resources. For information about IAM, see [Identity and Access Management documentation](https://docs.cloud.google.com/iam/docs).

This page shows how you can control Cloud Speech-to-Text access and permissions by using Identity and Access Management (IAM) roles and permissions.

## Overview

Cloud Speech-to-Text (STT) provides a set of predefined roles that help you control access to your Cloud STT resources. You can also create your own [custom roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles), if the predefined roles don't provide the sets of permissions you need.

The basic roles of **Editor** , **Viewer** , and **Owner** are also available, though they don't provide fine-grained control like the Cloud STT roles. In particular, the basic roles provide access to resources across Google Cloud. The roles specific to Cloud STT provide only Cloud STT permissions. For more information, see the [IAM roles and permissions index](https://docs.cloud.google.com/iam/docs/roles-overview#basic).

## Predefined roles

Predefined roles provide finer-grained permissions to principals (individuals, groups, or service accounts). The role you grant to a principal controls what actions the principal can take. You can grant multiple roles to the same principal, and you can change the roles granted to a principal at any time, provided you have the permissions to do so.

Broader roles encompass the more narrowly defined roles. For example, the Cloud STT Editor role includes all Cloud STT Editor role permissions and the Cloud STT Viewer role permissions. Likewise, the Cloud STT Admin role includes all Cloud STT Admin role permissions and the Cloud STT Editor role permissions.

Name | Cloud STT permissions  
(`speech.`) | Description  
---|---|---  
Project > Owner | All `speech` permissions | Full access and control for all Google Cloud resources including user access and billing for a project  
Project > Editor | All `speech` permissions except:  
`config.update`  
| Read/write access to all Google Cloud and Cloud STT resources except `config.update` and the ability to modify permissions and billing  
Project > Viewer |  `*.get`  
`*.list`  
`recognizers.recognize`  
| Read-only access to all Google Cloud resources, including Cloud Speech-to-Text resources, and permission to make recognition requests  
Cloud Speech Administrator | All `speech` permissions | Full control for all Cloud Speech-to-Text resources  
Cloud Speech Editor |  `customClasses.*`  
`locations.*`  
`operations.*`  
`phraseSets.*`  
`recognizers.*`  
| Read/write access to all Cloud STT resources except `config`  
Cloud Speech Client |  `customClasses.get`  
`customClasses.list`  
`locations.get`  
`locations.list`  
`operations.get`  
`operations.list`  
`phraseSets.get`  
`phraseSets.list`  
`recognizers.get`  
`recognizers.list`  
`recognizers.recognize`  
| Read access to all Cloud STT resources  
  
## Manage Cloud STT IAM

You can get and set IAM policies and roles by using the [ Google Cloud console](https://console.cloud.google.com/iam-admin/iam). For more information, see [Manage access to projects, folders, and organizations ](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## What's next

  * Learn how to [grant and revoke access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).
  * Learn more about [IAM](https://docs.cloud.google.com/iam/docs).
  * Learn more about [basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic).
  * Learn more about [custom roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
