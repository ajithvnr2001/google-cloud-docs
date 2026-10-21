---
url: https://docs.cloud.google.com/shell/docs/resetting-cloud-shell/
title: Disable or reset Cloud Shell \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:21.292593+00:00
---

# Disable or reset Cloud Shell  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/shell/docs/resetting-cloud-shell/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Shell ](https://docs.cloud.google.com/shell/docs)



Send feedback 

#  Disable or reset Cloud Shell Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to disable Cloud Shell for managed user accounts and how to reset Cloud Shell.

## Disable Cloud Shell for managed user accounts

To disable Cloud Shell for [Google Workspace](https://support.google.com/a/answer/4352075) and [Cloud Identity](https://support.google.com/a/answer/7319251) managed user accounts, go to the Google Admin console and then navigate to **Apps** > **Additional Google services** > **Google Cloud Platform** > **Cloud Shell Settings** and disable **Cloud Shell Access Settings**.

To disable Cloud Shell for specific users, you'll need to use access groups: add individual users to the group and turn off the group's Cloud Shell access setting. For more information, see [Controlling who uses Google Cloud in your organization guide](https://support.google.com/a/answer/9197205).

## Reset Cloud Shell

To reset Cloud Shell and restore your Cloud Shell home directory to a clean state, follow these steps.

**Note:** Before resetting your Cloud Shell home directory, consider using [Safe mode](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works#safe_mode) to sign in as root and fix issues with your files.

To restore your Cloud Shell home directory to a clean state:

  1. Check for personal files in the home directory and note that the next step deletes these files:
         
         ls -a $HOME
         

  2. Remove all files from your home directory:

**Important:** This will permanently delete all files in your home directory.
         
         sudo rm -rf $HOME
         

  3. In the Cloud Shell menu, click more_vert **More** and then click power_settings_new **Restart**. If prompted, click **Restart** in the confirmation dialog.

This provisions a new VM and restores the home directory to its default state.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
