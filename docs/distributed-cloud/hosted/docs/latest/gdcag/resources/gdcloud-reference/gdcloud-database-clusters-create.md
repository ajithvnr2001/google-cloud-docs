---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-database-clusters-create/
title: gdcloud database clusters create \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:20:15.921348+00:00
---

# gdcloud database clusters create  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-database-clusters-create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  gdcloud database clusters create Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud database clusters create - Create a DBCluster custom resource.

## SYNOPSIS
    
    
    gdcloud database clusters create CLUSTER_NAME [flags]
    

### EXAMPLES
    
    
    To create a DBCluster custom resource with database version PostgreSQL 14 with name "postgresql-db", run:
    
      gdcloud database clusters create postgresql-db \
        --database-version=POSTGRESQL_14
    
    To create a DBCluster custom resource with database version Oracle 19 with name "oracle-db" in the project "db", run:
    
      gdcloud database clusters create oracle-db --project=db \
        --database-version=ORACLE_19
    
    To create a DBCluster custom resource with database version AlloyDB Omni 15 with name "alloydbomni-db" in the project "db", run:
    
      gdcloud database clusters create alloydbomni-db --project=db \
        --database-version=ALLOYDBOMNI_15
    

### REQUIRED FLAGS
    
    
          --admin-password string     initial database password for admin user
          --database-version string   database version of the DBCluster to be created
    

### OPTIONAL FLAGS
    
    
          --availability-type string       level of availability. (zonal or zonal_ha) (default "zonal")
          --backup-retention-days int      number of days to keep backups since creation (1 ~ 90 days) (default 30)
          --cpu int                        number of cores to be used for the database
          --database-flags string          initial database flags
          --memory string                  amount of memory for the database
          --no-backup                      disables daily backup
          --retain-admin-password-secret   retain the secret of the admin password (default true)
          --storage-size string            amount of storage allocated to storing data
          --tier string                    machine type for a DBCluster with preset resources configuration (high-performance, standard or minimal) (default "standard")
          --zone string                    Zone to use for this invocation. To preset the zone flag for all commands that require it, run: "gdcloud config set core/zone ZONE". The zone flag is available only in multi-zone environments.
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
