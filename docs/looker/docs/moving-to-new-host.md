---
url: https://docs.cloud.google.com/looker/docs/moving-to-new-host/
title: Moving Looker to a new host \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:33:54.800621+00:00
---

# Moving Looker to a new host  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/moving-to-new-host/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Moving Looker to a new host Stay organized with collections  Save and categorize content based on your preferences. 

This document details the steps required to move a customer-hosted Looker instance to a new host.

## Step 1: Prepare the new system

Complete just the first part of the Looker [installation](https://docs.cloud.google.com/looker/docs/installing-looker-application) steps on the new host. In other words:

  * Verify that the new server complies with the minimum server specifications
  * Enable ntpd or chronyd
  * Create the **looker** user and group
  * Create the **looker** home directory
  * Skip downloading the Looker application and all remaining installation steps



## Step 2: Stop Looker on the old host
    
    
    cd ~/looker
    ./looker stop
    

## Step 3: Copy the Looker directory from the old to new host

From the new host, as the **looker** user:
    
    
    rsync -av OLDHOSTNAME:/home/looker/ /home/looker
    

## Step 4: Start Looker on the new host
    
    
    cd looker
    ./looker start
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
