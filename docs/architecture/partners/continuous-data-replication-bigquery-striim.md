---
url: https://docs.cloud.google.com/architecture/partners/continuous-data-replication-bigquery-striim/
title: Continuous data replication to BigQuery using Striim \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:29:00.027743+00:00
---

# Continuous data replication to BigQuery using Striim  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/partners/continuous-data-replication-bigquery-striim/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Continuous data replication to BigQuery using Striim Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-02-13 UTC

By: Edward Bell, Solutions Architect, [Striim, Inc](https://www.striim.com/). 

This tutorial demonstrates how to migrate a MySQL database to [BigQuery](https://docs.cloud.google.com/bigquery) using Striim. Striim is a comprehensive streaming [extract, transform, and load (ETL)](https://wikipedia.org/wiki/Extract,_transform,_load) platform that enables online database migrations and continuous streaming replication from on-premises and cloud data sources to Google Cloud data services.

This tutorial focuses on the implementation of a continuous replication from [Cloud SQL for MySQL](https://docs.cloud.google.com/sql/docs/mysql) to BigQuery. It is intended for database administrators, IT professionals, and data architects interested in taking advantage of BigQuery capabilities. 

## Objectives

  * Launch the Stiim for BigQuery free trial.
  * Use Striim to continuously replicate from Cloud SQL for MySQL to BigQuery. 



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Cloud SQL for MySQL](https://docs.cloud.google.com/sql/pricing)
  * [BigQuery](https://cloud.google.com/bigquery/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

This tutorial also uses Striim, which includes a trial period. You can find Striim in the [Cloud Marketplace](https://console.cloud.google.com/marketplace/details/striim/striim). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  3. Enable the Compute Engine and BigQuery APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,bigquery.googleapis.com)

  4. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  5. Set the default compute zone to `us-central1-a`:
         
         gcloud config set compute/zone us-central1-a
         export COMPUTE_ZONE=us-central1-a
         

This zone is where you deploy your database. For more information about zones, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions).




## Create a Cloud SQL for MySQL instance

You create a Cloud SQL for MySQL instance that you later connect to Striim. In this case, the instance acts as the source transactional system that you later replicate. In a real-world scenario, the source database can be one of many transactional database systems.

  1. In Cloud Shell, create the environment variables to create the instance:
         
         CSQL_NAME=striim-sql-src
         CSQL_USERNAME=striim-user
         CSQL_USER_PWD=$(openssl rand -base64 18)
         CSQL_ROOT_PWD=$(openssl rand -base64 18)
         

If you close the Cloud Shell session, you lose the variables.

  2. Make a note of the `CSQL_USER_PWD` and `CSQL_ROOT_PWD` passwords generated by the following commands:
         
         echo $CSQL_USER_PWD and echo $CSQL_ROOT_PWD
         

  3. Create the Cloud SQL for MySQL instance:
         
         gcloud sql instances create $CSQL_NAME \
             --root-password=$CSQL_ROOT_PWD --zone=$COMPUTE_ZONE \
             --tier=db-n1-standard-2 --enable-bin-log
         

  4. Create a Cloud SQL for MySQL user that Striim can connect to:
         
         gcloud sql users create $CSQL_USERNAME --instance $CSQL_NAME \
             --password $CSQL_USER_PWD --host=%
         

The Cloud SQL for MySQL database is set up for Striim to read.

  5. Find the IP address of the Cloud SQL for MySQL instance and make a note of it:
         
         gcloud sql instances describe $CSQL_NAME --format='get(ipAddresses.ipAddress)'
         




## Set up Striim

To set up an instance of the Striim server software, you use the Cloud Marketplace.

  1. In the Google Cloud console, go to the **Striim** page in the Cloud Marketplace.

[Go to Striim in the Cloud Marketplace](https://console.cloud.google.com/marketplace/details/striim/striim)

  2. Click **Launch**.

  3. In the **New Striim Deployment** window, complete the following fields:

     * Select the project that you created or selected to use for this tutorial.
     * In the **Zone** drop-down menu, select **`us-central1-a`**.
     * If you accept the terms for service, select the **I accept the Google Cloud Marketplace Terms of Service** checkbox. Terms of Service** checkbox.

Cloud Marketplace solutions typically come with various resources that launch to support the software. Review the monthly billing estimate before launching the solution.

     * Leave all other settings at their default values.

  4. Click **Deploy**.

  5. In the Google Cloud console, go to the **Deployments** page.

[Go to Deployments](https://console.cloud.google.com/dm/deployments)

  6. To review the deployment details of the Striim instance, click the name of the Striim instance. Make a note of the name of the deployment and the name of the VM that has deployed.

  7. To allow Striim to communicate with Cloud SQL for MySQL, [add the Striim server's IP address](https://docs.cloud.google.com/sql/docs/mysql/connect-external-app) to the Cloud SQL for MySQL instance's authorized networks:
         
         STRIIMVM_NAME=STRIIM_VM_NAME
         STRIIMVM_ZONE=us-central1-a
         gcloud sql instances patch $CSQL_NAME \
             --authorized-networks=$(gcloud compute instances describe $STRIIM_VM_NAME \
             --format='get(networkInterfaces[0].accessConfigs[0].natIP)' \
             --zone=$STRIIMVM_ZONE)
         

Replace the following:

     * `STRIIM_VM_NAME`: the name of the VM that you deployed with Striim.
  8. In the Google Cloud console, on the deployment instance details page, click **Visit the site** to open the Striim web UI.

  9. In the Striim configuration wizard, configure the following:

     * Review the end-user license agreement. If you accept the terms, click **Accept Striim EULA and Continue**.
     * Enter your contact information.
     * Enter the Cluster Name, Admin, Sys, and Striim Key passwords of your choice. Make a note of these passwords. Click **Save and Continue**.
     * Leave the key field blank to enable the trial, and then click **Save and Continue**.
  10. Click **Launch**. It takes about a minute for Striim to be configured. When done, click **Log In**.

  11. To log in to the Striim administrator console, log in with the `admin` user and the administrator password that you previously set. Keep this window open because you return to it in a later step.




### Set up Connector/J

Use [MySQL Connector/J](https://dev.mysql.com/downloads/connector/j/5.1.html) to connect Striim to your Cloud SQL for MySQL instance. As of this writing, 5.1.49 is the latest version of Connector/J.

  1. In the Google Cloud console, go to the **Deployments** page.

[Go to Deployments](https://console.cloud.google.com/dm/deployments)

  2. For the Striim instance, click **SSH** to automatically connect to the instance.

  3. Download the Connector/J to the instance and extract it:
         
         wget https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-5.1.49.tar.gz
         tar -xvzf mysql-connector-java-5.1.49.tar.gz
         

  4. Copy the file to the Striim library path, allow it to be executable, and change ownership of the file that you downloaded:
         
         sudo cp ~/mysql-connector-java-5.1.49/mysql-connector-java-5.1.49.jar /opt/striim/lib
         sudo chmod +x /opt/striim/lib/mysql-connector-java-5.1.49.jar
         sudo chown striim /opt/striim/lib/mysql-connector-java-5.1.49.jar
         

  5. To recognize the new library, restart the Striim server:
         
         sudo systemctl stop striim-node
         sudo systemctl stop striim-dbms
         sudo systemctl start striim-dbms
         sudo systemctl start striim-node
         

  6. Go back to the browser window with the administration console in it. Reload the page, and then log in using the `admin` user credentials.

It can take a couple minutes for the server to complete its restart from the previous step, so you might get a browser error during that time. If you encounter an error, reload the page and log in again.




## Load sample transactions to Cloud SQL

Before you can configure your first Striim app, load transactions into the MySQL instance.

  1. In Cloud Shell, connect to the instance using the Cloud SQL for MySQL instance credentials that you previously set:
         
         gcloud sql connect $CSQL_NAME --user=$CSQL_USERNAME
         

  2. Create a sample database and load some transactions into it:
         
         CREATE DATABASE striimdemo;
         USE striimdemo;
         CREATE TABLE ORDERS (ORDER_ID Integer, ORDER_DATE VARCHAR(50), ORDER_MODE VARCHAR(8), CUSTOMER_ID Integer, ORDER_STATUS Integer, ORDER_TOTAL Float, SALES_REP_ID Integer, PROMOTION_ID Integer, PRIMARY KEY (ORDER_ID));
         INSERT INTO ORDERS (ORDER_ID, ORDER_DATE, ORDER_MODE, CUSTOMER_ID, ORDER_STATUS, ORDER_TOTAL, SALES_REP_ID, PROMOTION_ID) VALUES (1001, 1568927976017, 'In-Store', 1001, 9, 34672.59, 331, 9404);
         INSERT INTO ORDERS (ORDER_ID, ORDER_DATE, ORDER_MODE, CUSTOMER_ID, ORDER_STATUS, ORDER_TOTAL, SALES_REP_ID, PROMOTION_ID) VALUES (1002, 1568928036017, 'In-Store', 1002, 1, 28133.14, 619, 2689);
         INSERT INTO ORDERS (ORDER_ID, ORDER_DATE, ORDER_MODE, CUSTOMER_ID, ORDER_STATUS, ORDER_TOTAL, SALES_REP_ID, PROMOTION_ID) VALUES (1003, 1568928096017, 'CompanyB', 1003, 1, 37367.95, 160, 30888);
         INSERT INTO ORDERS (ORDER_ID, ORDER_DATE, ORDER_MODE, CUSTOMER_ID, ORDER_STATUS, ORDER_TOTAL, SALES_REP_ID, PROMOTION_ID) VALUES (1004, 1568928156017, 'CompanyA', 1004, 1, 7737.02, 362, 89488);
         INSERT INTO ORDERS (ORDER_ID, ORDER_DATE, ORDER_MODE, CUSTOMER_ID, ORDER_STATUS, ORDER_TOTAL, SALES_REP_ID, PROMOTION_ID) VALUES (1005, 1568928216017, 'CompanyA', 1005, 9, 15959.91, 497, 78454);
         INSERT INTO ORDERS (ORDER_ID, ORDER_DATE, ORDER_MODE, CUSTOMER_ID, ORDER_STATUS, ORDER_TOTAL, SALES_REP_ID, PROMOTION_ID) VALUES (1006, 1568928276017, 'In-Store', 1006, 1, 82531.55, 399, 22488);
         INSERT INTO ORDERS (ORDER_ID, ORDER_DATE, ORDER_MODE, CUSTOMER_ID, ORDER_STATUS, ORDER_TOTAL, SALES_REP_ID, PROMOTION_ID) VALUES (1007, 1568928336017, 'CompanyA', 1007, 7, 52929.61, 420, 66256);
         INSERT INTO ORDERS (ORDER_ID, ORDER_DATE, ORDER_MODE, CUSTOMER_ID, ORDER_STATUS, ORDER_TOTAL, SALES_REP_ID, PROMOTION_ID) VALUES (1008, 1568928396017, 'Online', 1008, 1, 26912.56, 832, 7262);
         INSERT INTO ORDERS (ORDER_ID, ORDER_DATE, ORDER_MODE, CUSTOMER_ID, ORDER_STATUS, ORDER_TOTAL, SALES_REP_ID, PROMOTION_ID) VALUES (1009, 1568928456017, 'CompanyA', 1009, 1, 97706.08, 124, 12185);
         INSERT INTO ORDERS (ORDER_ID, ORDER_DATE, ORDER_MODE, CUSTOMER_ID, ORDER_STATUS, ORDER_TOTAL, SALES_REP_ID, PROMOTION_ID) VALUES (1010, 1568928516017, 'CompanyB', 1010, 1, 47539.16, 105, 17868);
         

  3. To check the upload, count the records to ensure that 10 records were inserted:
         
         SELECT COUNT(*) FROM ORDERS;
         

  4. Leave the Cloud SQL for MySQL instance:
         
         Exit
         




## Create a BigQuery target dataset

In this section, you create a BigQuery dataset, and load service account credentials so that Striim can write to the target database from the Google Cloud console.

  1. In Cloud Shell, create a BigQuery dataset:
         
         bq --location=US mk -d \
         --description "Test Target for Striim." striimdemo
         

For this tutorial, you deploy BigQuery in the US.

  2. Create a new target table:
         
         bq mk \
             --table \
             --description "Striim Table" \
             --label organization:striimlab striimdemo.orders order_id:INTEGER,order_date:STRING,order_mode:STRING,customer_id:INTEGER,order_status:INTEGER,order_total:FLOAT,sales_rep_id:INTEGER,promotion_id:INTEGER
         

  3. Create a service account for Striim to connect to BigQuery:
         
         gcloud iam service-accounts create striim-bq \
             --display-name striim-bq
         export sa_striim_bq=$(gcloud iam service-accounts list \
             --filter="displayName:striim-bq" --format='value(email)')
         export PROJECT=$(gcloud info \
             --format='value(config.project)')
         gcloud projects add-iam-policy-binding $PROJECT \
             --role roles/bigquery.dataEditor \
             --member serviceAccount:$sa_striim_bq
         gcloud projects add-iam-policy-binding $PROJECT \
             --role roles/bigquery.user --member serviceAccount:$sa_striim_bq
         gcloud iam service-accounts keys create ~/striim-bq-key.json \
             --iam-account $sa_striim_bq
         

A key called `striim-bq-key.json` is created in your home path.

  4. Move the newly generated key to the server:
         
         gcloud compute scp ~/striim-bq-key.json $STRIIM_VM_NAME:~ \
             --zone=$COMPUTE_ZONE
         

  5. Move the key to the `/opt/striim` directory:
         
         gcloud compute ssh \
             --zone=$COMPUTE_ZONE $STRIIM_VM_NAME \
             -- 'sudo cp ~/striim-bq-key.json /opt/striim && sudo chown striim /opt/striim/striim-bq-key.json'
         

You are now ready to create a Striim app.




## Create an online database migration

An online database migration moves data from a source database (either on-premises or hosted on a cloud provider) to a target database or data warehouse in Google Cloud. The source database remains fully accessible by the business app and with minimal performance impact on the source database during this time.

In an online migration, you perform an initial bulkload, and also continuously capture any changes. You then synchronize the two databases to ensure that data isn't lost.

If you want to focus on creating a change data capture (CDC) pipeline, see the Create a continuous Cloud SQL for MySQL to BigQuery data pipeline section.

### Create the source connection

  1. In the Google Cloud console, on the instance details page, click **Visit the site** to open the Striim web UI.
  2. In the Striim web UI, click **Apps**.

  3. Click **Add App**.

  4. Click **Start from Scratch**.

  5. In the **Name** field, enter `MySQLToBigQuery_initLoad`.

  6. In the **Namespace** drop-down menu, select the default **Admin namespace**. This label is used to organize your apps.

  7. Click **Save**.

  8. On the **Flow Designer** page, to do a one-time initial bulkload of data, from the **Sources** pane, drag **Database** to the flow design palette in the center of the screen and enter the following connection properties:

     * In the **Name** field, enter `mysql_source`.
     * Leave the **Adapter** field at the default value of **DatabaseReader**.
     * In the **Connection URL** field, enter `jdbc:mysql://PRIMARY_ADDRESS:3306/striimdemo`. Replace `PRIMARY_ADDRESS` with the IP address of the Cloud SQL instance that you created in the previous section.
     * In the **Username** field, enter the username that you set as the `CSQL_USER` environment variable, `striim-user`.
     * In the **Password** field, enter the `CSQL_USER_PWD` value that you made a note of when you created a Cloud SQL for MySQL instance.
     * To see more configuration properties, click **Show optional properties**.
     * In the **Tables** field, enter `striimdemo.ORDERS`.
     * For **Output to** , select **New output**.
     * In the **New output** field, enter `stream_CloudSQLMySQLInitLoad`.
     * Click **Save**.
  9. To test the configuration settings to make sure that Striim can successfully connect to Cloud SQL for MySQL, click **Created** , and then select **Deploy App**.

  10. In the **Deployment** window, you can specify that you want to run parts of your app on some of your deployment topology. For this tutorial, select **Default** , and click **Deploy**.

  11. To preview your data as it flows through the Striim pipeline, click waves **`mysql_source DataBase reader`** , and then click remove_red_eye **Preview on run**.

  12. Click **Deployed** , and then click **Start App**.

The Striim app starts running, and data flows through the pipeline. If there are any errors, there is an issue connecting to the source database because there is only a source component in the pipeline. If you see your app successfully run, but no data flows through, typically that means that you don't have any data in your database.

  13. After you've successfully connected to your source database and tested that it can read data, click **Running** , and then select **Stop App**.

  14. Click **Stopped** , and then select **Undeploy App**. You are now ready to connect this flow to BigQuery.




### Perform an initial load into BigQuery

  1. In the Striim web UI, click waves **`mysql_source Database reader`**.

  2. Click add **Connect to next component** , select **Connect next Target component** , and then complete the following fields:

     * In the **Name** field, enter `bq_target`.
     * In the **Adapter** field, enter `BigQueryWriter`.
     * The **Tables property** is a source/target pair separated by commas. It is in the format of `srcSchema1.srcTable1,tgtSchema1.tgtTable1;srcSchema2.srcTable2,tgtSchema2.tgtTable2`. For this tutorial, enter `striimdemo.ORDERS,striimdemo.orders`.
     * The **Service Account Key** requires a fully qualified path and name of the key file that was previously generated. For this tutorial, enter `/opt/striim/striim-bq-key.json`.
     * In the **Project ID** field, enter your Google Cloud project ID.
  3. Click **Save**.

  4. To deploy the app and preview the data flow, do the following:

     * Click **Created** , and then select **Deploy App**.
     * In the **Deployment** window, select **Default** , and then click **Deploy**.
     * To preview your data as it flows through the Striim pipeline, click waves **`mysql_source Database reader`** , and then click remove_red_eye **Preview on run**.
     * Click **Deployed** , and then click **Start App**.
  5. In the Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  6. Click the **`striimdemo`** database.

  7. In the query editor, enter `SELECT COUNT(*) AS ORDERS, AVG(ORDER_TOTAL) AS ORDERS_AVE, SUM(ORDER_TOTAL) AS ORDERS_SUM FROM striimdemo.orders;` and then click **Run**. It can take up to 90 seconds for the transactions to fully replicate to BigQuery due to the default configuration settings. After it's successfully replicated, the results table outputs the average order of `43148.952` and the total size of the orders, `431489.52`.

You have successfully set up your Striim environment and pipeline to perform a batch load.




## Create a continuous data pipeline from Cloud SQL for MySQL to BigQuery

With an initial one-time bulkload in place, you can now set up a continuous replication pipeline. This pipeline is similar to the bulk pipeline that you created, but with a different source object.

### Create a CDC source

  1. In the Striim web UI, click **Home**.
  2. Click add **Apps**.
  3. Click **Start from Scratch**.
  4. In the **Name** field, enter `MySQLToBigQuery_cdc`.
  5. In the **Namespace** drop-down menu, select **Admin namespace**.
  6. On the **Flow Designer** page, drag a **MySQL CDC** source reader to the center of the design palette.
  7. Configure your new MySQL CDC source with the following information:

     * In the **Name** field, enter `mysql_cdc_source`.
     * Leave the **Adapter** field at the default value of **MysqlReader**.
     * In the **Connection URL** field, enter `jdbc:mysql://PRIMARY_ADDRESS:3306/striimdemo`.
     * Enter the username and password that you used in the previous section.
     * To see more configuration properties, click **Show optional properties**.
     * In the **Tables** field, enter `striimdemo.ORDERS`.
     * For **Output to** , select **New output.**
     * In the **New output** field, enter `stream_CloudSQLMySQLCDCLoad`.
     * Click **Save**.



### Load new transactions into BigQuery

  1. In the Striim web UI, click waves **MysqlReader**.
  2. Click add **Connect to next component** , and then select **Connect next Target component**.

     * In the **Name** field, enter `bq_cdc_target`.
     * In the **Adapter** field, enter `BigQueryWriter`.
     * The **Tables property** is a source/target pair separated by commas. It is in the format of `srcSchema1.srcTable1,tgtSchema1.tgtTable1;srcSchema2.srcTable2,tgtSchema2.tgtTable2`. For this tutorial, use `striimdemo.ORDERS,striimdemo.orders`.

     * The **Service Account Key** requires a fully qualified path and name of the key file that was previously generated. For this tutorial, enter `/opt/striim/striim-bq-key.json`

     * In the **Project ID** field, enter your Google Cloud project ID.

  3. Click **Save**.

  4. To deploy the app and preview the data flow, do the following:

     * Click **Created** , and then select **Deploy App**.
     * In the **Deployment** window, select **Default** , and then click **Deploy**.
     * To preview your data as it flows through the Striim pipeline, click waves **MysqlReader** , and then click remove_red_eye **Preview on Run**.
     * Click **Deployed** , and then click **Start App**.
  5. In Cloud Shell, connect to your Cloud SQL for MySQL instance:
         
         gcloud sql connect $CSQL_NAME --user=$CSQL_USERNAME
         

  6. Connect to your database and load new transactions into it:
         
         USE striimdemo;
         INSERT INTO ORDERS (ORDER_ID, ORDER_DATE, ORDER_MODE, CUSTOMER_ID, ORDER_STATUS, ORDER_TOTAL, SALES_REP_ID, PROMOTION_ID) VALUES (1011, 1568928576017, 'In-Store', 1011, 9, 13879.56, 320, 88252);
         INSERT INTO ORDERS (ORDER_ID, ORDER_DATE, ORDER_MODE, CUSTOMER_ID, ORDER_STATUS, ORDER_TOTAL, SALES_REP_ID, PROMOTION_ID) VALUES (1012, 1568928636017, 'CompanyA', 1012, 1, 19729.99, 76, 95203);
         INSERT INTO ORDERS (ORDER_ID, ORDER_DATE, ORDER_MODE, CUSTOMER_ID, ORDER_STATUS, ORDER_TOTAL, SALES_REP_ID, PROMOTION_ID) VALUES (1013, 1568928696017, 'In-Store', 1013, 5, 7286.68, 164, 45162);
         INSERT INTO ORDERS (ORDER_ID, ORDER_DATE, ORDER_MODE, CUSTOMER_ID, ORDER_STATUS, ORDER_TOTAL, SALES_REP_ID, PROMOTION_ID) VALUES (1014, 1568928756017, 'Online', 1014, 1, 87268.61, 909, 70407);
         INSERT INTO ORDERS (ORDER_ID, ORDER_DATE, ORDER_MODE, CUSTOMER_ID, ORDER_STATUS, ORDER_TOTAL, SALES_REP_ID, PROMOTION_ID) VALUES (1015, 1568928816017, 'CompanyB', 1015, 1, 69744.13, 424, 79401);
         

  7. In the Striim web UI, on the **Transactions view** page, transactions now populate the page and show that data is flowing.

  8. In the Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  9. Click the **`striimdemo`** database.

  10. To verify that your data is successfully replicated, in the **Query Editor** enter `SELECT COUNT(*) AS ORDERS, AVG(ORDER_TOTAL) AS ORDERS_AVE, SUM(ORDER_TOTAL) AS ORDERS_SUM FROM striimdemo.orders;` and then click **Run**. The results table outputs the average order of `43148.952` and the total size of the orders, `431489.52`.

It can take up to 90 seconds for the transactions to fully replicate to BigQuery due to the default configuration settings.




Congratulations, you have successfully set up a streaming replication pipeline from Cloud SQL for MySQL to BigQuery.

## Clean up

The easiest way to eliminate billing is to delete the Google Cloud project you created for the tutorial. Alternatively, you can delete the individual resources. 

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 
  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 
  * Look at the [Google Cloud Data Migration content](https://cloud.google.com/solutions/database-migration).
  * To learn about Striim, [visit the website](http://www.striim.com), [schedule a demo](https://go2.striim.com/demo-region-select) with a Striim technologist, and subscribe to the [Striim blog](http://www.striim.com/blog).
  * To learn how to set up continuous data movement from Oracle to BigQuery, see [Oracle to Google BigQuery – Continuous Movement of On-Premises Data via CDC](https://www.striim.com/blog/2018/09/oracle-to-google-bigquery/) and the [Move Oracle to Google BigQuery in Real Time](https://www.striim.com/blog/2018/09/oracle-to-google-bigquery/) video. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-02-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-02-13 UTC."],[],[]] 
