---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-organizations-upgrade-get-status/
title: gdcloud organizations upgrade get-status \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:19:55.571566+00:00
---

# gdcloud organizations upgrade get-status  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-organizations-upgrade-get-status/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  gdcloud organizations upgrade get-status Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud organizations upgrade get-status - Check the status of an upgrade for the specified organization(s).

## SYNOPSIS
    
    
    gdcloud organizations upgrade get-status [flags]
    

### EXAMPLES
    
    
    To check the current stage of the upgrade for organization "org-1", run:
    
        gdcloud organization upgrade get-status --names=org-1
    
    To check the full upgrade status of organizations "org-1" and "org-2", run:
    
        gdcloud organization upgrade get-status --names=org-1,org-2 --all-stages
    
    To check the upgrade status of all organizations in the current zone as JSON, run:
    
        gdcloud organization upgrade get-status --all-organizations --json
    
    

### OPTIONAL FLAGS
    
    
          --all-organizations   Retrieve status for all organizations in the given zone.
          --all-stages          Output all stages status information.
          --json                Output status in JSON format.
          --names strings       Comma-separated list of organizations to retrieve status for.
          --stages strings      Comma-separated list of stages to retrieve status for.
          --zone string         Zone to use for this invocation. To preset the zone flag for all commands that require it, run: "gdcloud config set core/zone ZONE". The zone flag is available only in multi-zone environments.
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
