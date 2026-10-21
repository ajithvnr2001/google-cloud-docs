---
url: https://docs.cloud.google.com/chronicle/docs/investigation/investigate-file/
title: Investigate a file \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:33:25.049275+00:00
---

# Investigate a file  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/investigation/investigate-file/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Investigate a file

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

You can use Google Security Operations to search your data for a specific file based on its MD5, SHA-1, or SHA-256 hash value.

If additional information is available for a file hash found within a customer's Google SecOps account, this additional information is added to the associated UDM events automatically. You can search for these UDM events manually using UDM Search or by using rules.

## View a file hash

To view a file hash, you can:

  * View a file in **File hash** view directly

  * Navigate to **File hash** view from another view




## View a file in File hash view directly

To open **File hash** view directly, enter the hash value in the Google SecOps search field and click **Search**.

**Note:** [UDM search](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search) provides enhanced capabilities that let you conduct more thorough investigatzions of the events and alerts within your Google SecOps instance than is possible using **File hash** view alone. For more information, see [UDM search](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search).

Google SecOps provides additional information about the file, including the following:

  * **Partner engines detecting** : Other security vendors who have detected the file.

  * **Properties/metadata** : Known properties of the file.

  * **VT submitted/ITW filenames** : Known malicious in-the-wild (ITW) malware submitted to VirusTotal.




## Navigate to File hash view from another view

You can also navigate to **File hash** view while investigating an asset in an another view (for example, **Asset** view) by completing the following steps:

  1. Open an investigation view. For example, select an asset to view it within Asset view.

  2. In the **Timeline** to the left, scroll to any event tied to a process or file modification, such as **Network Connection**.

![Selecting an Event in Asset View](https://docs.cloud.google.com/chronicle/images/hash-view-start-asset.png)**Selecting an Event in Asset view**

  3. Open the Raw Log and UDM viewer by clicking the open icon in the **Timeline**.

  4. You can open **File hash** view for the file by clicking the hash value (for example, principal.process.file.md5) within the displayed UDM event.




## Considerations

Hash view has the following limitations:

  * You can only filter events that are displayed in this view.
  * Only DNS, EDR, Webproxy, and Alert event types are populated in this view. The first seen and last seen information populated in this view is also limited to these event types.
  * Generic events don't appear in any of the curated views. They appear only in raw log and UDM searches.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
