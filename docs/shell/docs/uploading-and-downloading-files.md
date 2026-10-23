---
url: https://docs.cloud.google.com/shell/docs/uploading-and-downloading-files/
title: Manage files with Cloud Shell \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:46:41.447505+00:00
---

# Manage files with Cloud Shell  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/shell/docs/uploading-and-downloading-files/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Shell ](https://docs.cloud.google.com/shell/docs)



Send feedback 

#  Manage files with Cloud Shell Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to upload and download files and folders with Cloud Shell.

## Upload and download files and folders

You can upload and download files and folders easily using Cloud Shell. To transfer files, use one of the following methods:

  * Click more_vert **More** > **Upload** or **Download** to move your files or folders to or from Cloud Shell. Files and folders can only be uploaded to and downloaded from your home directory.

  * Use the [`cloudshell download`](https://docs.cloud.google.com/shell/docs/using-cloudshell-command) command to download files:
        
        cloudshell download test1.md test2.md
        

  * [Use the `gcloud cloud-shell scp` command](https://docs.cloud.google.com/shell/docs/using-cloud-shell-with-gcloud-cli) on a local terminal to transfer files between Cloud Shell and your workstation. For example, to move a file, 'data.txt', from Cloud Shell to your local machine:
        
        gcloud cloud-shell scp cloudshell:~/data.txt localhost:~data.txt
        

  * In your Cloud Shell Editor Explorer, right-click a directory or file and then click **Copy Download Link** , **Download** , or **Upload Files**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
