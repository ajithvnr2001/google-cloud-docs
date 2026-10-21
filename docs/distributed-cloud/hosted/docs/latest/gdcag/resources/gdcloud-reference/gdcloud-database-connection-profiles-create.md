---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-database-connection-profiles-create/
title: gdcloud database connection-profiles create \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:26:40.019894+00:00
---

# gdcloud database connection-profiles create  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-database-connection-profiles-create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  gdcloud database connection-profiles create Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud database connection-profiles create - Create a connection profile for data migration for specified database type.

## SYNOPSIS
    
    
    gdcloud database connection-profiles create DATABASE_TYPE CONNECTION_PROFILE_NAME [flags]
    

### EXAMPLES
    
    
    To create a connection profile for PostgreSQL, run:
    
      gdcloud database connection-profiles create postgresql pg-connection-profile-sample \
      --password=123456 --username=my-user --host=1.2.3.4 --port=5432 --ca-certificate=/path/to/ca.crt
    

### REQUIRED FLAGS
    
    
          --ca-certificate string   file path for x509 PEM-encoded certificate of the CA that signed the database server's certificate.
          --host string             IP or hostname of the database.
          --password string         Password for the user that the migration service uses to connect to the database.
          --username string         Username that the migration service uses to connect to the database.
    

### OPTIONAL FLAGS
    
    
          --client-certificate string   file path for x509 PEM-encoded certificate that will be used by the replica to authenticate against the database server.
          --port int32                  Network port of the database. (default 5432)
          --private-key string          file path for Unencrypted PKCS#1 or PKCS#8 PEM-encoded private key associated with the Client Certificate.
          --zone string                 Zone to use for this invocation. To preset the zone flag for all commands that require it, run: "gdcloud config set core/zone ZONE". The zone flag is available only in multi-zone environments.
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
