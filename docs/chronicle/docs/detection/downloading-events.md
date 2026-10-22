---
url: https://docs.cloud.google.com/chronicle/docs/detection/downloading-events/
title: Download events \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:38:25.939735+00:00
---

# Download events  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/downloading-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Download events

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

You can display and download large numbers of the events associated with each threat detection. This lets you search across a broad set of the data stored in your Google Security Operations account to hunt for security issues.

### Display and download events

Complete the following steps to display and download the events associated with a detection:

  1. In the navigation bar, click **Detection > Rules & Detections**.

  2. Click the **Rules Dashboard** tab.

![Rules Dashboard](https://docs.cloud.google.com/chronicle/images/rules-dashboard.png)**Rules Dashboard**

  3. Click a rule to open the Rule Detections view.

**Note:** The **Download as CSV** option is only available for multi-event rules. It is not supported for detections from Test Rules.
  4. Select a Detection from the Detections list and expand the sample events list by clicking the arrow next to the list. Each event variable in a rule can display up to 10 sample events. For example, a rule with two event variables (`$e1`, `$e2`) can show up to 20 samples in total. Any samples beyond this limit are hidden on the **Detections** page., but they're included if you click **Download All** to view Unified Data Model (UDM) events associated with your detection.




The **Download as CSV** option appears if event samples were omitted from your detection. A maximum of 100,000 events can be downloaded. The event samples are sorted by event timestamp in the UI. Google does not guarantee any sorting of event samples when reading detections from Chronicle APIs.

Optional: Click  view_column  **Columns** to add more fields to the sample events list. These fields are also included in the downloaded CSV.

  1. Click the **Download as CSV** link. The event samples are downloaded as a CSV file which you can then open in most spreadsheet applications.

**Note:** Your security data is continuously ingested into your Google SecOps account. When you click Download all, the CSV file is dynamically generated and includes the latest event samples. It might differ from the data displayed in the user interface.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
