---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-backup-plans-update/
title: gdcloud backup plans update \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:02:12.614859+00:00
---

# gdcloud backup plans update  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-backup-plans-update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  gdcloud backup plans update Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud backup plans update - Updates a backup plan.

## SYNOPSIS
    
    
    gdcloud backup plans update BACKUP_PLAN_NAME [flags]
    

## DESCRIPTION

Updates the backup plan with the specified information.

### EXAMPLES
    
    
    To update a backup plan named "backup-plan-name", run:
    
        gdcloud backup plans create backup-plan-name --project=project-name --zone=zone-name
    

### REQUIRED FLAGS
    
    
          --delete-lock uint   Prevents deletion of the backup for the number of days specified after backup creation.
          --project string     Backup plan project name.
          --retain uint        Deletes backups after the number of days specified after backup creation. (default 1)
          --retention-locked   Specifies whether the retention policy of this backup plan is locked.
    

### OPTIONAL FLAGS
    
    
          --custom-schedule string   A crontab schedule indicating when to schedule backups.If --schedule set "Custom".
          --schedule string          Schedule indicating when to schedule backups (Daily/Weekly/Monthly/Custom).
          --schedule-paused string   Specifies whether the scheduled operation is inactive or active.
          --zone string              Zone to use for this invocation. To preset the zone flag for all commands that require it, run: "gdcloud config set core/zone ZONE". The zone flag is available only in multi-zone environments.
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
