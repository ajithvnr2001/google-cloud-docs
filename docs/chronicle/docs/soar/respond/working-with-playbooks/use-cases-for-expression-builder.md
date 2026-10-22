---
url: https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/use-cases-for-expression-builder/
title: Expression Builder examples \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:14.161015+00:00
---

# Expression Builder examples  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/use-cases-for-expression-builder/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Expression Builder examples

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document provides uses cases that detail how to build and implement dynamic expressions within playbook actions across the Google Security Operations platform. It focuses on using the Expression Builder to parse, filter, and extract specific data from previous action results—such as list data, entity details, and scan reports—to drive complex automation logic in subsequent playbook steps. 

**Note:** Some characters in the Expression Builder like slash (/), back slash (\\) or quotation marks (") require an escape character like a back slash (\\) before it to return results. For example: `replace("\/","y") `

## Before you begin

Before you begin, follow these suggestions:

  * Use **Qualys – List Scans** to get all the latest scans from Qualys (30 days hard coded).
  * Use the Expression Builder to extract the ID (REF) of the newest scan as placeholder to download VM scan results. VM scan results download the relevant report.
  * Use **List Operations** to extract the list of the vulnerabilities' identifiers found on the network common vulnerabilities and exposures (CVEs) from the report and compare it to the CVE from the case.
  * Use an IPS alert to trigger the playbook.



## Use case: Intrusion Prevention System IPS

This use case assumes you're building a playbook that has found a malicious flow in a network.  
Imagine that a vulnerability management tool, such as Qualys, has scheduled a daily scan.

### Create a placeholder

To create a placeholder, do the following:

  1. Begin with an `Active Directory_Enrich Entities` action to enrich all potentially affected entities.
  2. Use **Qualys VM – List Scans** to retrieve the latest scan results for the network machines.
  3. Determine if any of the results are vulnerable to the detected flow.
  4. Look at `QualysVM_Download VM Scan Results_1`. You should see the placeholder and the added Expression Builder.



###  Add the placeholder

To add the placeholder, do the following: 

  1. Click [ ] **Placeholder**. The **Insert Placeholder** dialog appears. 
  2. Select **Playbook > QualysVM_list_Scans_1_JSONResult**. 
  3. Click the **Expression Builder** icon; the Expression Builder page appears. 
  4. In the **Expression** field, add the following: The expressions use MAX to take the latest result by date `LAUNCH_DATETIME` and then extract the specific scan ID of the relevant scan where REF is the scan ID.  
Example: `| max(LAUNCH_DATETIME) | REF`
  5. Click **Run**. The expected results should appear. 
  6. Click **Insert** to include the Expression Builder as part of the placeholder. 
  7. Click **Action > List operations** using CVEs from the cases + expression builder displays. 
  8. Once the playbook is triggered in real time, you can see the scan results in the side drawer, including the specific scan as a PDF file.  




## Use case: Too many failed login attempts 

This use case addresses failed login attempts by enriching entity data to determine alert severity. The goal is to quickly find the user's department and their last password change date.

  1. Start with the `ActiveDirectory_Enrich` entities action to gather detailed information on all internal entities associated with the alert.
  2. In the subsequent Insight message, use the Expression Builder to extract the target user and their last login time.



### Add the placeholder

To add these placeholders: 

  1. In the **Message** field, click **[ ] Placeholder**. 
  2. On the **Insert Placeholder** page, click the Expression Builder icon next to the `ActiveDirectory_Enrich entities_JSONResult`. 
  3. Add the following in the expression field: This will choose the entity identifier. If more than one entity returned results – we will get it as a comma separated list.  
| Entity  

  4. Click **Run** ; the sample result appears. In this case, `user@domain.com`. 
  5. Click **Insert** to use this as part of your placeholder message. Add the relevant free text to your message. 
  6. Click **[ ] Placeholder** and then click the Expression Builder icon next to the `ActiveDirectory_Enrich entities_JSONResult`. 
  7. Add the following expression. This captures the last logon time of the specified user. | EntityResult.lastLogon 
  8. Click **Insert** and then click **Save**. 
  9. Once the playbook is triggered in real time, a message on the Insight pane appears, showing the username and last login time.  




## Use case: VirusTotal hash analysis 

This use case shows how to extract a file hash's reputation from a specific scan engine, such as Kaspersky, to determine if the file is malicious and create a corresponding entity.

  * Use the **VirusTotal_Scan Hash** action to retrieve the file report.



The subsequent action, **Siemplify_Create** or **Update Entity Properties** , creates or modifies an entity property, such as `Detected by Kaspersky`, based on the scan results.

To add this placeholder: 

  1. In the Field Value field, click **[] Placeholder**. 
  2. On the **Insert Placeholder** page, click the **Expression Builder** icon next to the `VirusTotal_ScanHash_JSONResult`.  

  3. Add the following expression:  
`| filter(EntityResult.scans.Kaspersky.detected, "=", "true") | Entity`  


If we scanned more than one hash, it filters the results by all the entity objects that Kaspersky marked as malicious, and then returns only the entity name.

  4. Click **Insert** > click **Save**. Results appear at run time. 



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
