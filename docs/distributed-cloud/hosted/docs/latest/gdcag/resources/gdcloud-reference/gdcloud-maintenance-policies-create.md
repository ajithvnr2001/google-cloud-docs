---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-maintenance-policies-create/
title: gdcloud maintenance policies create \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:02:00.963370+00:00
---

# gdcloud maintenance policies create  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-maintenance-policies-create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  gdcloud maintenance policies create Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud maintenance policies create - Create a single maintenance policy.

## SYNOPSIS
    
    
    gdcloud maintenance policies create POLICY_NAME [flags]
    

### EXAMPLES
    
    
    To create a weekly maintenance policy, run:
    
        gdcloud maintenance policies create example-policy \
            --project example-project \
            --weekly-cycle-days=Sat \
            --weekly-cycle-days=Sun \
            --weekly-cycle-duration=4h30m \
            --weekly-cycle-start-time=22:00
    

### OPTIONAL FLAGS
    
    
          --weekly-cycle-days strings        Comma-separated list of days of the week when maintenance can begin. Accepted values are RFC-822 style days of week, such as "Mon".
          --weekly-cycle-duration string     Maximum duration that the maintenance can last for. For example, "2h3m".
          --weekly-cycle-start-time string   Time of the day (in UTC timezone) when maintenance can begin, in "hh:mm" format. For example, "20:36".
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
