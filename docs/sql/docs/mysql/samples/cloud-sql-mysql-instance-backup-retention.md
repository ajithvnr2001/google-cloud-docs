---
url: https://docs.cloud.google.com/sql/docs/mysql/samples/cloud-sql-mysql-instance-backup-retention/
title: Set automated backup retention for an instance \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:58.824919+00:00
---

# Set automated backup retention for an instance  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/samples/cloud-sql-mysql-instance-backup-retention/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Samples ](https://docs.cloud.google.com/sql/docs/mysql/samples)



#  Set automated backup retention for an instance Stay organized with collections  Save and categorize content based on your preferences. 

This sample specifies the number of automated backups to retain for an instance.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Manage standard backups](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/manage-standard-backups)



## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    resource "google_sql_database_instance" "default" {
      name             = "mysql-instance-backup-retention"
      region           = "asia-northeast1"
      database_version = "MYSQL_8_0"
      settings {
        tier = "db-f1-micro"
        backup_configuration {
          enabled = true
          backup_retention_settings {
            retained_backups = 365
            retention_unit   = "COUNT"
          }
        }
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudsqlformysql). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
