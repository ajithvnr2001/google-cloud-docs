---
url: https://docs.cloud.google.com/capacity-planner/docs/troubleshooting/
title: Troubleshoot Capacity Planner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:13:13.360586+00:00
---

# Troubleshoot Capacity Planner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/capacity-planner/docs/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Capacity Planner ](https://docs.cloud.google.com/capacity-planner/docs)
  * [ Guides ](https://docs.cloud.google.com/capacity-planner/docs/overview)



Send feedback 

#  Troubleshoot Capacity Planner Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to troubleshoot issues with Capacity Planner.

## Data retrieval errors

The following issues occur when Capacity Planner can't retrieve the data associated with your project, folder, or organization.

**Error messages:**
    
    
    Error retrieving usage data. Try again later.
    If this problem persists, contact your Google Technical Account Manager.
    
    
    
    Error retrieving forecast. Try again later.
    If this problem persists, contact your Google Technical Account Manager.
    
    
    
    Error retrieving usage data and forecast. Try again later.
    If this problem persists, contact your Google Technical Account Manager.
    

**Resolution:** To resolve these issues, try using Capacity Planner later. If Capacity Planner continues to display one of these errors, then contact your assigned [Technical Account Manager (TAM)](https://cloud.google.com/tam).

## Data availability errors

This section lists the data availability errors that you might encounter, as well as how to resolve these errors.

### Not enough data to show usage

The following issues occur when there is less than one day of actual usage data in your project, folder, or organization.

**Error messages:**
    
    
    The project PROJECT_ID doesn't have enough data to display.
    
    
    
    The folder FOLDER_ID doesn't have enough data to display.
    
    
    
    The organization ORGANIZATION_ID doesn't have enough data to display.
    

**Resolution:** To resolve this issue, try using Capacity Planner again a few days after your project, or one or more projects within your organization or folder, have at least one day of usage. If, after waiting for some time, you still encounter issues, then contact your assigned [TAM](https://cloud.google.com/tam).

### Not enough data to generate a forecast

The following issues occur when there is not enough forecasted usage data in your project, folder, or organization.

**Error messages:**
    
    
    The project PROJECT_ID doesn't have enough data to generate a forecast.
    
    
    
    The folder FOLDER_ID doesn't have enough data to generate a forecast.
    
    
    
    The organization ORGANIZATION_ID doesn't have enough data to generate a forecast.
    

**Resolution:** To resolve this issue, try using Capacity Planner again after your project, or one or more projects within your organization or folder, have at least one month of usage. If, after waiting for some time, you still encounter issues, then contact your assigned [TAM](https://cloud.google.com/tam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
