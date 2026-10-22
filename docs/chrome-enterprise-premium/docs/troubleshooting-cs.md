---
url: https://docs.cloud.google.com/chrome-enterprise-premium/docs/troubleshooting-cs/
title: Troubleshoot Chrome Enterprise Premium and Falcon ZTA integration issues \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:20.750431+00:00
---

# Troubleshoot Chrome Enterprise Premium and Falcon ZTA integration issues  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chrome-enterprise-premium/docs/troubleshooting-cs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Chrome Enterprise Premium ](https://docs.cloud.google.com/chrome-enterprise-premium/docs)
  * [ Guides ](https://docs.cloud.google.com/chrome-enterprise-premium/docs/overview)



Send feedback 

#  Troubleshoot Chrome Enterprise Premium and Falcon ZTA integration issues Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how you can resolve the Falcon ZTA connection issues, and how you can retrieve the Google Chrome extension logs and Falcon ZTA logs for troubleshooting.

## Retrieve Chrome extension logs

To retrieve Chrome extension logs, do the following:

  1. From the Chrome browser, click **Chrome > Preferences > Extensions**. 
  2. In the **Endpoint Verification** pane, click **Details**.
  3. Click **Extension options**.
  4. In the dialog, from the **Log level** drop-down list, select **All** , and click **Download log**.

The log file downloads to your computer.




For more information about troubleshooting, see [Troubleshoot endpoint verification](https://support.google.com/a/users/answer/9018161).

## Retrieve Falcon ZTA logs

To retrieve Falcon ZTA logs, contact [support@crowdstrike.com](mailto:support@crowdstrike.com).

## Falcon ZTA data issues

The following table lists issues that you might encounter when verifying the Falcon ZTA data and provides suggestions for how to fix each of them. Issue | Workaround | The CrowdStrike section is not visible on the **Devices** page. | Check if Falcon ZTA is enabled for the organizational unit to which the device's user belongs. To enable Falcon ZTA, see [Enable Falcon ZTA for your organizational unit.](https://docs.cloud.google.com/chrome-enterprise-premium/docs/setting-up-cs#enable-client\))  
---|---  
DATA_NOT_RETRIEVABLE error | The `data.zta` file might be missing. Contact [support@crowdstrike.com](mailto:support@crowdstrike.com).   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
