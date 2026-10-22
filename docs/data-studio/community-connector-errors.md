---
url: https://docs.cloud.google.com/data-studio/community-connector-errors/
title: Community connector errors \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:35.124565+00:00
---

# Community connector errors  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/community-connector-errors/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Community connector errors Stay organized with collections  Save and categorize content based on your preferences. 

Because community connectors are built by third-party developers, when problems occur it's up to the developer to provide [clear and actionable error messages](https://developers.google.com/looker-studio/connector/error-handling). In general, if you encounter an error when using a community connector, contact the developer of that connector for assistance.

The following errors are related to Data Studio or the Google platform:

Message / Symptom  |  Cause  |  How to fix   
---|---|---  
Community connectors are disabled for your organization.  |  This message may appear for Google Workspace users.  Your administrator has turned off the ability to create data sources based on a third-party connector.  |  Contact your administrator for assistance and refer them to [Set policies for how users grant access to new and existing third-party visualizations in reports](https://support.google.com/a/answer/14340728).   
Can't show data. Apps Script is disabled for your organization.  |  This message may appear for Google Workspace users.  To view data in a chart that is based on a community connector, Apps Script must be enabled for your organization. When Apps Script is disabled, community connectors can't fetch data and you'll see an error in the chart.  |  If you see errors on charts based on a community connector, try asking your Google Admin to [ turn Apps Script on ](https://support.google.com/a?p=apps_script_on_off).   
Can't load community connectors. Try again later.  |  This message may appear when loading the list of third-party connectors.  Data Studio may be experiencing a temporary issue loading the connector list.  |  Wait a bit, then try loading the list again. If the problem persists, you can try to [ troubleshoot ](https://docs.cloud.google.com/data-studio/troubleshooting-guide) or [ report the problem ](https://docs.cloud.google.com/data-studio/troubleshooting-guide) to Google.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
