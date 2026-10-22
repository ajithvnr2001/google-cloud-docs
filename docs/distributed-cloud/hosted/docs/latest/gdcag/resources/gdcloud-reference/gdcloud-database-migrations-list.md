---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-database-migrations-list/
title: gdcloud database migrations list \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:59:00.287017+00:00
---

# gdcloud database migrations list  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-database-migrations-list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  gdcloud database migrations list Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud database migrations list - list migrations.

## SYNOPSIS
    
    
    gdcloud database migrations list [flags]
    

### EXAMPLES
    
    
    To list migrations for source CONNECTION_PROFILE for PostgreSQL, run:
    
      gdcloud database migrations list --source=CONNECTION_PROFILE
    
    To list migrations for destination DESTINATION_DBCLUSTER for PostgreSQL, run:
    
      gdcloud database migrations list --destination=DESTINATION_DBCLUSTER
    
    To list migrations for destination DESTINATION_DBCLUSTER for AlloyDBOmni, run:
    
      gdcloud database migrations list --destination=DESTINATION_DBCLUSTER --database-engine ALLOYDBOMNI
    
    
    

### OPTIONAL FLAGS
    
    
          --database-engine string   Destination DBCluster type. (default "POSTGRESQL")
          --destination string       Destination DBCluster that will be created as migration target.
          --source string            Source connection-profile that the migration service uses to connect to the source database.
          --zone string              Zone to use for this invocation. To preset the zone flag for all commands that require it, run: "gdcloud config set core/zone ZONE". The zone flag is available only in multi-zone environments.
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
