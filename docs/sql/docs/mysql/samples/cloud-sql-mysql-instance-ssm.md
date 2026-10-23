---
url: https://docs.cloud.google.com/sql/docs/mysql/samples/cloud-sql-mysql-instance-ssm/
title: Upgrade MySQL instance maintenance version \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:27.045784+00:00
---

# Upgrade MySQL instance maintenance version  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/samples/cloud-sql-mysql-instance-ssm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Samples ](https://docs.cloud.google.com/sql/docs/mysql/samples)



#  Upgrade MySQL instance maintenance version Stay organized with collections  Save and categorize content based on your preferences. 

This sample demonstrates how to upgrade your Cloud SQL for MySQL instance to the target maintenance version.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Perform self-service maintenance](https://docs.cloud.google.com/sql/docs/mysql/self-service-maintenance)



## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    resource "google_sql_database_instance" "mysql_ssm_instance_name" {
      name                = "mysql-ssm-instance-name"
      region              = "asia-northeast1"
      database_version    = "MYSQL_5_7"
      maintenance_version = "MYSQL_5_7_38.R20220809.02_00"
      settings {
        tier = "db-f1-micro"
      }
      # set `deletion_protection` to true, will ensure that one cannot accidentally delete this instance by
      # use of Terraform whereas `deletion_protection_enabled` flag protects this instance at the GCP level.
      deletion_protection = false
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudsqlformysql). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
