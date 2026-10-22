---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-harbor-backup-plans-create/
title: gdcloud harbor backup-plans create \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:58:44.622894+00:00
---

# gdcloud harbor backup-plans create  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-harbor-backup-plans-create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  gdcloud harbor backup-plans create Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud harbor backup-plans create - Create a harbor instance backup plan.

## SYNOPSIS
    
    
    gdcloud harbor backup-plans create BACKUP_PLAN [flags]
    

### EXAMPLES
    
    
    To create a backup plan, run:
        gdcloud harbor backup-plans create daily-harbor-backup \
            --instance=my-harbor-registry \
            --backup-repository=main-repo \
            --cron-schedule="0 0 * * *" \
            --retain-days=45 \
            --description="Daily midnight backup for production registry"
    

### REQUIRED FLAGS
    
    
          --backup-repository string   Name of the backup repository identifying the secondary storage for the backup.
          --cron-schedule string       Cron string schedule on which the backup is executed.
          --instance string            Name of the harbor instance to back up in the same namespace.
    

### OPTIONAL FLAGS
    
    
          --async                Run the operation in the background without waiting for it to complete.
          --description string   Description for this backup plan.
          --retain-days uint     Number of days after which the service deletes a backup. If not provided, backups are not subject to automatic deletion.
          --state string         State of the backup plan. Options are ACTIVE or PAUSED. (default "ACTIVE")
          --timeout duration     Timeout for waiting for the resource to become ready. (default 5m0s)
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
