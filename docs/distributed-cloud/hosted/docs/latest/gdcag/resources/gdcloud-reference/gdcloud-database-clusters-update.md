---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-database-clusters-update/
title: gdcloud database clusters update \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:01:58.088108+00:00
---

# gdcloud database clusters update  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-database-clusters-update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  gdcloud database clusters update Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud database clusters update - Update a DBCluster custom resource.

## SYNOPSIS
    
    
    gdcloud database clusters update CLUSTER_NAME [flags]
    

### EXAMPLES
    
    
    To update a DBCluster custom resource with name "postgresql-db" to enable backup, run:
    
      gdcloud database clusters update postgresql-db --backup --backup-retention-days 14
    
    To update the computation resources of a DBCluster custom resource with name "oracle-db" in the project "db", run:
    
      gdcloud database clusters update oracle-db --cpu 4 --memory 16G --storage-size 100Gi --project=db
    

### OPTIONAL FLAGS
    
    
          --admin-password string             database password for admin user
          --allow-external-incoming-traffic   enable external incoming traffic to database if set to true, else disable external incoming traffic.
          --availability-type string          level of availability. (zonal or zonal_ha). Only for PostgresSQL.
          --backup                            enable daily backup if set to true, else disable daily backup.
          --backup-retention-days int         number of days to keep backups since creation (1 ~ 90 days). (default 30)
          --clear-database-flags              Clear all database flags to their default values
          --cpu int                           number of cores to be used for the database.
          --database-flags string             database flags
          --memory string                     amount of memory for the database.
          --storage-size string               amount of storage allocated to storing data.
          --zone string                       Zone to use for this invocation. To preset the zone flag for all commands that require it, run: "gdcloud config set core/zone ZONE". The zone flag is available only in multi-zone environments.
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
