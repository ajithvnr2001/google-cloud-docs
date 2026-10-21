---
url: https://docs.cloud.google.com/sql/docs/mysql/samples/cloud-sql-mysql-instance-public-ip/
title: Configure public IP for a instance \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:31:13.103293+00:00
---

# Configure public IP for a instance  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/samples/cloud-sql-mysql-instance-public-ip/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Samples ](https://docs.cloud.google.com/sql/docs/mysql/samples)



#  Configure public IP for a instance Stay organized with collections  Save and categorize content based on your preferences. 

This sample enables public IP and adds an authorized address range for a instance.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Configure public IP](https://docs.cloud.google.com/sql/docs/mysql/configure-ip)



## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    resource "google_sql_database_instance" "mysql_public_ip_instance_name" {
      database_version = "MYSQL_5_7"
      name             = "mysql-public-ip-instance-name"
      region           = "asia-southeast2"
      settings {
        availability_type = "ZONAL"
        disk_size         = 100
        disk_type         = "PD_SSD"
        ip_configuration {
          # Add optional authorized networks
          # Update to match the customer's networks
          authorized_networks {
            name  = "test-net-3"
            value = "203.0.113.0/24"
          }
          # Enable public IP
          ipv4_enabled = true
        }
        tier = "db-custom-4-26624"
      }
      # set `deletion_protection` to true, will ensure that one cannot accidentally delete this instance by
      # use of Terraform whereas `deletion_protection_enabled` flag protects this instance at the GCP level.
      deletion_protection = false
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudsqlformysql). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
