---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/reading-from-postgresql/
title: Read from a PostgreSQL database \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:38.322698+00:00
---

# Read from a PostgreSQL database  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/reading-from-postgresql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Read from a PostgreSQL database Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how you read data from a PostgreSQL database in a Cloud Data Fusion instance.

## Before you begin

  * [Create a Cloud Data Fusion instance](https://docs.cloud.google.com/data-fusion/docs/how-to/create-private-ip).
  * Enable your PostgreSQL database to accept connections from Cloud Data Fusion. To do this securely, we recommend that you use a private Cloud Data Fusion instance.



### Required roles

To get the permissions that you need to connect to a PostgreSQL database, ask your administrator to grant you the following IAM roles: 

  * [Dataproc Worker ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`) on the Dataproc service account in the project that contains the cluster
  * [Cloud Data Fusion Runner ](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.runner) (`roles/datafusion.runner`) on the Dataproc service account in the project that contains the cluster
  * To use Cloud SQL without the Cloud SQL Auth Proxy: [Cloud SQL Client ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.client) (`roles/cloudsql.client`) on the project that contains the Cloud SQL instance 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Open your instance in Cloud Data Fusion

  1. In the Google Cloud console, go to the Cloud Data Fusion page.

  2. To open the instance in the Cloud Data Fusion Studio, click **Instances** , and then click **View instance**.

[Go to Instances](https://console.cloud.google.com/data-fusion/locations/-/instances)




## Store your PostgreSQL password as a secure key

Enter your PostgreSQL password as a secure key to encrypt in your Cloud Data Fusion instance. For more information about keys, see [Cloud KMS](https://docs.cloud.google.com/kms/docs).

  1. In the Cloud Data Fusion UI, click **System admin > Configuration**.

  2. Click **Make HTTP Calls**. ![Configuration.](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/reading-from-postgresql/config.png)

  3. In the dropdown menu, choose **PUT**.

  4. In the path field, enter `namespaces/default/securekeys/pg_password`.

  5. In the **Body** field, enter `{"data":"POSTGRESQL_PASSWORD"}`. Replace `POSTGRESQL_PASSWORD` with your PostgreSQL password.

  6. Click **Send**.

![Password.](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/reading-from-postgresql/password.png)



The **Response** field notifies you of any errors.

## Connect to Cloud SQL for PostgreSQL

  1. In the Cloud Data Fusion UI, click the menu _menu_ and navigate to the **Wrangler** page.

  2. Click **Add connection**.

  3. Choose **Database** as the source type to connect. ![Add connection.](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/reading-from-postgresql/add-connection.png)

  4. Under **Google Cloud SQL for PostgreSQL** , click **Upload**. ![Choose source.](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/reading-from-postgresql/choose-source.png)

  5. Upload a JAR file that contains your PostgreSQL driver. Your JAR file must follow the format `NAME-VERSION.jar`. If your JAR file doesn't follow this format, rename it before you upload.

  6. Click **Next**.

  7. Enter the driver's name, class name, and version in the fields.

  8. Click **Finish**.

  9. In the **Add connection** window that opens, click **Google Cloud SQL for PostgreSQL**. Your JAR name should appear under **Google Cloud SQL for PostgreSQL**. ![JAR uploaded.](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/reading-from-postgresql/jar-uploaded.png)

  10. Fill in the required connection fields. In the **Password** field, select the secure key you stored previously. This ensures that your password is retrieved using [Cloud KMS](https://docs.cloud.google.com/kms/docs). ![Choose password.](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/reading-from-postgresql/choose-pw.png)

  11. In the **Connection string** field, enter your connection string as: 
         
         jdbc:postgresql://google/DATABASE_NAME?cloudSqlInstance=INSTANCE_CONNECTION_NAME&socketFactory=com.google.cloud.sql.postgres.SocketFactory&useSSL=false
         

Replace the following:

     * `DATABASE_NAME`: the Cloud SQL database name as listed in the **Databases** tab of the instance details page.
     * `INSTANCE_CONNECTION_NAME`: the Cloud SQL instance connection name as displayed in the **Overview** tab of the instance details page.
![Instance connection name.](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/reading-from-postgresql/instance-connection-name.png)

For example: 
    
    jdbc:postgresql://google/postgres?cloudSqlInstance=dis-demo:us-central1:pgsql-1&socketFactory=com.google.cloud.sql.postgres.SocketFactory&useSSL=false
    

  12. Enable the Cloud SQL Admin API.

  13. Click **Test connection** to ensure that the connection can be established with the database.

  14. Click **Add connection**.




After your PostgreSQL database is connected, you can apply transformations to your data (in **Wrangler**), create a [pipeline](https://docs.cloud.google.com/data-fusion/docs/concepts/overview#pipeline), and write your output to a sink (in **Studio**).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
