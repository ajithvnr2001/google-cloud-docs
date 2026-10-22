---
url: https://docs.cloud.google.com/database-migration/docs/mysql/create-connection-profiles/
title: Create a source connection profile \u00a0|\u00a0 Database Migration Service for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:06.655322+00:00
---

# Create a source connection profile  |  Database Migration Service for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/mysql/create-connection-profiles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ MySQL ](https://docs.cloud.google.com/database-migration/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/mysql/scenario-overview)



Send feedback 

#  Create a source connection profile Stay organized with collections  Save and categorize content based on your preferences. 

Connection profiles capture identifiers for your source databases. Each connection profile contains the minimum required amount of information Database Migration Service needs to facilitate data movement between the data source and destination.

To create a source connection profile, follow these steps:

### Console

  1. Go to the [ Connection Profiles](https://console.cloud.google.com/dbmigration/connection-profiles) page in the Google Cloud Console. 
  2. Click **Create profile**.
  3. On the **Create a connection profile** page, from the **Profile role** list, select **Source**. 
  4. From the **Database engine** list, select your source database engine. If you select **Cloud SQL for MySQL** from this Select the ID of the Cloud SQL instance that you want to migrate. list, then an **Instance ID** list appears. 
  5. In the **Connection profile name** field, enter a human-readable name for your connection profile. This value is displayed in the connection profile list.
  6. Keep the auto-generated **Connection profile ID**.
  7. Enter a **Hostname** or **IP address**. 
     * The value you use here depends on the connectivity method you use for your migration. For example, if the source database is hosted in Google Cloud, or if a reverse SSH tunnel is used to connect the destination database to the source database, then specify the private (internal) IP address for the source database. For more information, see [ Network connectivity overview](https://docs.cloud.google.com/database-migration/docs/mysql/networking-methods). 

     * MySQL limits the hostname to 60 characters. Amazon RDS database hostnames are typically longer than 60 characters. If this is the case for the database you're migrating, then configure a DNS redirect to create a CNAME record that associates your domain name with the domain name of your RDS DB instance. To learn more about setting up DNS CNAME, see [ Set up DNS records for a domain name](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name) in the Cloud DNS documentation, or check [ Routing internet traffic to your AWS resources](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-resources.html) in the AWS documentation. 
  8. Enter the **Port** that's used to access the host. The default MySQL port is 3306.
  9. Enter a username and password for the source database.
  10. In the **Connection profile region** section of the page, select the region where you want to save the connection profile. Connection profiles, like all resources, are saved in a region. Region selection doesn't impact which migration jobs can use them, or which regions can connect to the data location itself, but can impact availability in the case of regional downtime.
  11. Click **Create**.

The **Connection profiles** page appears, and the newly created connection profile is displayed.




### gcloud

This sample uses the optional `--no-async` flag so that all operations are performed synchronously. This means that some commands might take a while to complete. You can skip the `--no-async` flag to run commands asynchronously. If you do, you need to use the [`gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/describe) command to verify if your operation is successful.

Before using any of the command data below, make the following replacements: 

  * CONNECTION_PROFILE_ID with a machine-readable identifier for your connection profile.
  * REGION with the identifier of the region where you want to save the connection profile.
  * HOST_IP_ADDRESS with the IP address where Database Migration Service can reach your source database instance. This value can vary depending on which [ connectivity method](https://docs.cloud.google.com/database-migration/docs/mysql/networking-methods) you use for your migration.
  * PORT_NUMBER with the port number where your source database accepts incoming connections. The default MySQL port is 3306.
  * USERNAME with the name of the database user account you want Database Migration Service to connect as to your source database instance.
  * PASSWORD with the password for the database user account.
  * (Optional) CONNECTION_PROFILE_NAME with a human-readable name for your connection profile. This value is displayed in the Google Cloud console. 



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration connection-profiles \
    create mysql CONNECTION_PROFILE_ID \
      --no-async \
      --region=REGION \
      --host=HOST_IP_ADDRESS \
      --port=PORT_NUMBER \
      --username=USERNAME \
      --password=PASSWORD \
      --display-name=CONNECTION_PROFILE_NAME

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration connection-profiles `
    create mysql CONNECTION_PROFILE_ID `
      --no-async `
      --region=REGION `
      --host=HOST_IP_ADDRESS `
      --port=PORT_NUMBER `
      --username=USERNAME `
      --password=PASSWORD `
      --display-name=CONNECTION_PROFILE_NAME

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration connection-profiles ^
    create mysql CONNECTION_PROFILE_ID ^
      --no-async ^
      --region=REGION ^
      --host=HOST_IP_ADDRESS ^
      --port=PORT_NUMBER ^
      --username=USERNAME ^
      --password=PASSWORD ^
      --display-name=CONNECTION_PROFILE_NAME

You should receive a response similar to the following:
    
    
    Waiting for connection profile [CONNECTION_PROFILE_ID]
    to be created with [OPERATION_ID]
    
    Waiting for operation [OPERATION_ID] to complete...done.
    
    Created connection profile CONNECTION_PROFILE_ID [OPERATION_ID]
    

## What's next

  * [ Manage connection profiles](https://docs.cloud.google.com/database-migration/docs/mysql/manage-connection-profiles)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
