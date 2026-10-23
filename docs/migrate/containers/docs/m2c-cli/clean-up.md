---
url: https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/clean-up/
title: Clean up your local machine \u00a0|\u00a0 Migrate to Containers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:46:41.795912+00:00
---

# Clean up your local machine  |  Migrate to Containers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/clean-up/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Containers ](https://docs.cloud.google.com/migrate/containers/docs)
  * [ Guides ](https://docs.cloud.google.com/migrate/containers/docs/getting-started)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Clean up your local machine

After you've completed the migration, to clean up your local machine, you can remove the directory that contains the copy of the source machine file system.

This page describes how you can clean up your local machine.

## Clean up a Linux machine

To remove the directory that contains the copy of the source machine file system from your local machine, run the following command:
    
    
    ./m2c cleanup --source PATH_TO_COPIED_FILESYSTEM
    

Replace PATH_TO_COPIED_FILESYSTEM with the path to the copied file system directory.

**Note:** The `cleanup` command is supported on Linux machines only.

## Clean up a Windows machine

To clean up a Windows machine, you need to manually remove all the disk images that you have on your local machine.

## What's next

  * Learn how to [manage usage statistics](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/usage-statistics).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
