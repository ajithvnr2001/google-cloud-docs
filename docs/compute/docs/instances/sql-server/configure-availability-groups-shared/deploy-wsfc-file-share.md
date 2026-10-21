---
url: https://docs.cloud.google.com/compute/docs/instances/sql-server/configure-availability-groups-shared/deploy-wsfc-file-share/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:31:23.719796+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/sql-server/configure-availability-groups-shared/deploy-wsfc-file-share/




Stay organized with collections  Save and categorize content based on your preferences. 

### Creating file shares

Create two file shares on `witness` so that the VM instance can store SQL Server backups and act as a file share witness:

  1. Connect to `witness` [by using Remote Desktop](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows). Sign in with your domain user account.
  2. Right-click the **Start** button (or press **Win+X**) and click **Windows PowerShell (Admin)**.
  3. Confirm the elevation prompt by clicking **Yes**.
  4. Create a witness file share and grant yourself and the two cluster nodes access to the file share.
         
         New-Item "C:\QWitness" –type directory
         
         icacls C:\QWitness\ /grant 'node-1$:(OI)(CI)(M)'
         icacls C:\QWitness\ /grant 'node-2$:(OI)(CI)(M)'
         
         New-SmbShare `
           -Name QWitness `
           -Path "C:\QWitness" `
           -Description "SQL File Share Witness" `
           -FullAccess $env:username,node-1$,node-2$
         

  5. Create another file share to store backups and grant SQL Server full access.
         
         New-Item "C:\Backup" –type directory
         New-SmbShare `
           -Name Backup `
           -Path "C:\Backup" `
           -Description "SQL Backup" `
           -FullAccess  $env:USERDOMAIN\sql_server
         




Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
