---
url: https://docs.cloud.google.com/data-studio/configure-network/
title: Configure network access for Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:18.967635+00:00
---

# Configure network access for Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/configure-network/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Configure network access for Data Studio Stay organized with collections  Save and categorize content based on your preferences. 

To ensure full functionality of Data Studio, especially within corporate networks with firewalls or proxies, ensure that the following domains are on your allowlist for outbound connections, typically on Port 443:

  * `datastudio.google.com` (Primary application URL)
  * `lookerstudio.google.com` (Legacy application URL)
  * `accounts.google.com` (Google Account authentication)
  * `*.googleapis.com` (Essential Google APIs)
  * `*.gstatic.com` / `ssl.gstatic.com` (Static content, fonts, icons)
  * `*.googleusercontent.com` (Embedded images, data extracts, user content)
  * `*.scf.usercontent.goog` (Critical for chart rendering. Blocking this domain may cause intermittent chart loading failures with errors like "sent no data".)
  * `maps.googleapis.com` (Required for Map visualizations)
  * `www.google.com`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
