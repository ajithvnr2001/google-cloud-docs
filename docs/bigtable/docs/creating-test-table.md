---
url: https://docs.cloud.google.com/bigtable/docs/creating-test-table/
title: Create a test table \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:50.514035+00:00
---

# Create a test table  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/creating-test-table/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a test table

This page describes the steps to create a small Bigtable table that you can use to test code snippets. The table contains time-series data for smartphones and tablets.

These instructions use the Google Cloud console and the `cbt` CLI , a command-line interface built specifically for Bigtable.

## Before you begin

Before creating a test table, complete the following prerequisites.

### Set up authentication

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

For information about setting up authentication for a production environment, see [ Set up Application Default Credentials for code running on Google Cloud ](https://docs.cloud.google.com/bigtable/docs/authentication#on-gcp). 

### Grant IAM role

To get the permissions that you need to create a test table, ask your administrator to grant you the [Bigtable Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigtable#bigtable.admin) (`roles/bigtable.admin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Install the `cbt` CLI 

Run the following command to install the `cbt` CLI :
    
    
      gcloud components install cbt
    

## Create an instance

In the project of your choice, create a test instance to store your test table. The table is small, so you only need a single-node instance.

  1. Open the **Create instance** page in the Google Cloud console.

[Create an instance](https://console.cloud.google.com/bigtable/create-instance)

  2. For **Instance name** , enter `Test instance`.

  3. For **Instance ID** , enter `test-instance`.

  4. For **Storage type** , select **SSD**.

  5. For **Cluster ID** , enter `test-instance-c1`.

  6. For **Region** , select a region near you.

  7. For **Zone** , select a zone in the region you selected.

  8. Under **Nodes** , enter `1`.

  9. Click **Create** to create the instance.




## Connect to the instance

  1. Configure the `cbt` CLI to use your project and instance by creating a `.cbtrc` file, replacing `PROJECT_ID` with the ID for the project where you created your Bigtable instance:
         
         echo project = PROJECT_ID >> ~/.cbtrc && echo instance = test-instance >> ~/.cbtrc
         

  2. Verify that you set up the `.cbtrc` file correctly:
         
         cat ~/.cbtrc

The terminal displays the contents of the `.cbtrc` file, which looks similar to the following:
         
         project = PROJECT_ID
         instance = test-instance

Now you can use the `cbt` CLI with your instance.




## Create a test table

  1. Create a table named `test_table` that has two column families. For each column family, set a [garbage collection](https://docs.cloud.google.com/bigtable/docs/garbage-collection) policy to keep a maximum of 2 cells per column:
         
         cbt createtable test_table "families=stats_summary:maxversions=2,stats_detail:maxversions=2,cell_plan:maxversions=2"

  2. List the column families:
         
         cbt ls test_table

The terminal displays output similar to the following:
         
         Family Name       GC Policy
             -----------       ---------
             stats_detail        versions() > 2
             stats_summary       versions() > 2
             cell_plan           versions() > 2




## Populate the table

  1. Copy the following commands into your terminal window and press `Enter`.
         
         cbt set test_table phone#4c410523#20190501 stats_summary:connected_cell=1 stats_summary:connected_wifi=1 stats_summary:os_build=PQ2A.190405.003 cell_plan:data_plan_01gb=true cell_plan:data_plan_05gb=true
           cbt set test_table phone#4c410523#20190502 stats_summary:connected_cell=1 stats_summary:connected_wifi=1 stats_summary:os_build=PQ2A.190405.004 cell_plan:data_plan_05gb=true
           cbt set test_table phone#4c410523#20190505 stats_summary:connected_cell=0 stats_summary:connected_wifi=1 stats_summary:os_build=PQ2A.190406.000
           cbt set test_table phone#5c10102#20190501 stats_summary:connected_cell=1 stats_summary:connected_wifi=1 stats_summary:os_build=PQ2A.190401.002 cell_plan:data_plan_10gb=true
           cbt set test_table tablet#5c10102#20190502 stats_summary:connected_cell=1 stats_summary:connected_wifi=0 stats_summary:os_build=PQ2A.190406.000 cell_plan:data_plan_10gb=true

  2. Use the `cbt read` command to read the data you added to the table:
         
         cbt read test_table

The terminal displays output similar to the following. Note that timestamps are automatically assigned to cells because your write request does not include timestamps.
         
         ----------------------------------------
             phone#4c410523#20190501
               cell_plan:data_plan_01gb                 @ 2023/09/23-11:44:10.535000
                 "true"
               cell_plan:data_plan_05gb                 @ 2023/09/23-11:44:10.535000
                 "true"
               stats_summary:connected_cell             @ 2023/09/23-11:44:10.535000
                 "1"
               stats_summary:connected_wifi             @ 2023/09/23-11:44:10.535000
                 "1"
               stats_summary:os_build                   @ 2023/09/23-11:44:10.535000
                 "PQ2A.190405.003"
             ----------------------------------------
             phone#4c410523#20190502
               cell_plan:data_plan_05gb                 @ 2023/09/23-11:44:11.545000
                 "true"
               stats_summary:connected_cell             @ 2023/09/23-11:44:11.545000
                 "1"
               stats_summary:connected_wifi             @ 2023/09/23-11:44:11.545000
                 "1"
               stats_summary:os_build                   @ 2023/09/23-11:44:11.545000
                 "PQ2A.190405.004"
             ----------------------------------------
             phone#4c410523#20190505\
               stats_summary:connected_cell             @ 2023/09/23-11:44:12.503000
                 "0"
               stats_summary:connected_wifi             @ 2023/09/23-11:44:12.503000
                 "1"
               stats_summary:os_build                   @ 2023/09/23-11:44:12.503000
                 "PQ2A.190406.000"
             ----------------------------------------
             phone#5c10102#20190501
               cell_plan:data_plan_10gb                 @ 2023/09/23-11:44:13.553000
                 "true"
               stats_summary:connected_cell             @ 2023/09/23-11:44:13.553000
                 "1"
               stats_summary:connected_wifi             @ 2023/09/23-11:44:13.553000
                 "1"
               stats_summary:os_build                   @ 2023/09/23-11:44:13.553000
                 "PQ2A.190401.002"
             ----------------------------------------
             tablet#5c10102#20190502
               cell_plan:data_plan_10gb                 @ 2023/09/23-11:44:14.480000
                 "true"
               stats_summary:connected_cell             @ 2023/09/23-11:44:14.480000
                 "1"
               stats_summary:connected_wifi             @ 2023/09/23-11:44:14.480000
                 "0"
               stats_summary:os_build                   @ 2023/09/23-11:44:14.480000
                      "PQ2A.190406.000"
         

  3. Optional: Write new values to the same rows and columns. Bigtable creates new cells with new timestamps to store the new versions of the data. Copy the following commands into your terminal window and press `Enter`.
         
         cbt set test_table phone#4c410523#20190501 stats_summary:connected_cell=2 stats_summary:connected_wifi=5 stats_summary:os_build=PQ2A.190405.003 cell_plan:data_plan_01gb=true cell_plan:data_plan_05gb=false
           cbt set test_table phone#4c410523#20190502 stats_summary:connected_cell=2 stats_summary:connected_wifi=5 stats_summary:os_build=PQ2A.190405.004 cell_plan:data_plan_05gb=false
           cbt set test_table phone#4c410523#20190505 stats_summary:connected_cell=1 stats_summary:connected_wifi=4 stats_summary:os_build=PQ2A.190406.000
           cbt set test_table phone#5c10102#20190501 stats_summary:connected_cell=3 stats_summary:connected_wifi=3 stats_summary:os_build=PQ2A.190401.002 cell_plan:data_plan_10gb=false
           cbt set test_table tablet#5c10102#20190502 stats_summary:connected_cell=2 stats_summary:connected_wifi=0 stats_summary:os_build=PQ2A.190406.000 cell_plan:data_plan_10gb=false

  4. Use the `cbt read` command to read all of the data in the table:
         
         cbt read test_table

The terminal displays output similar to the following. Each column now contains two cells with unique timestamps.
         
         ----------------------------------------
           phone#4c410523#20190501
             cell_plan:data_plan_01gb                 @ 2024/07/09-17:48:21.191000
             "true"
             cell_plan:data_plan_01gb                 @ 2024/07/09-17:46:09.369000
             "true"
             cell_plan:data_plan_05gb                 @ 2024/07/09-17:48:21.191000
             "false"
             cell_plan:data_plan_05gb                 @ 2024/07/09-17:46:09.369000
             "true"
             stats_summary:connected_cell             @ 2024/07/09-17:48:21.191000
             "2"
             stats_summary:connected_cell             @ 2024/07/09-17:46:09.369000
             "1"
             stats_summary:connected_wifi             @ 2024/07/09-17:48:21.191000
             "5"
             stats_summary:connected_wifi             @ 2024/07/09-17:46:09.369000
             "1"
             stats_summary:os_build                   @ 2024/07/09-17:48:21.191000
             "PQ2A.190405.003"
             stats_summary:os_build                   @ 2024/07/09-17:46:09.369000
             "PQ2A.190405.003"
         
           ----------------------------------------
           phone#4c410523#20190502
             cell_plan:data_plan_05gb                 @ 2024/07/09-17:48:22.205000
             "false"
             cell_plan:data_plan_05gb                 @ 2024/07/09-17:46:10.455000
             "true"
             stats_summary:connected_cell             @ 2024/07/09-17:48:22.205000
             "2"
             stats_summary:connected_cell             @ 2024/07/09-17:46:10.455000
             "1"
              stats_summary:connected_wifi             @ 2024/07/09-17:48:22.205000
             "5"
             stats_summary:connected_wifi             @ 2024/07/09-17:46:10.455000
             "1"
             stats_summary:os_build                   @ 2024/07/09-17:48:22.205000
             "PQ2A.190405.004"
             stats_summary:os_build                   @ 2024/07/09-17:46:10.455000
             "PQ2A.190405.004"
         
           ----------------------------------------
           phone#4c410523#20190505
             stats_summary:connected_cell             @ 2024/07/09-17:48:23.206000
             "1"
             stats_summary:connected_cell             @ 2024/07/09-17:46:11.402000
             "0"
             stats_summary:connected_wifi             @ 2024/07/09-17:48:23.206000
             "4"
             stats_summary:connected_wifi             @ 2024/07/09-17:46:11.402000
             "1"
             stats_summary:os_build                   @ 2024/07/09-17:48:23.206000
             "PQ2A.190406.000"
             stats_summary:os_build                   @ 2024/07/09-17:46:11.402000
             "PQ2A.190406.000"
         
           ----------------------------------------
           phone#5c10102#20190501
             cell_plan:data_plan_10gb                 @ 2024/07/09-17:48:24.172000
             "false"
             cell_plan:data_plan_10gb                 @ 2024/07/09-17:46:12.388000
             "true"
             stats_summary:connected_cell             @ 2024/07/09-17:48:24.172000
             "3"
             stats_summary:connected_cell             @ 2024/07/09-17:46:12.388000
             "1"
             stats_summary:connected_wifi             @ 2024/07/09-17:48:24.172000
             "3"
             stats_summary:connected_wifi             @ 2024/07/09-17:46:12.388000
             "1"
             stats_summary:os_build                   @ 2024/07/09-17:48:24.172000
             "PQ2A.190401.002"
             stats_summary:os_build                   @ 2024/07/09-17:46:12.388000
             "PQ2A.190401.002"
         
           ----------------------------------------
           tablet#5c10102#20190502
             cell_plan:data_plan_10gb                 @ 2024/07/09-17:48:25.194000
             "false"
             cell_plan:data_plan_10gb                 @ 2024/07/09-17:46:13.391000
             "true"
             stats_summary:connected_cell             @ 2024/07/09-17:48:25.194000
             "2"
             stats_summary:connected_cell             @ 2024/07/09-17:46:13.391000
             "1"
             stats_summary:connected_wifi             @ 2024/07/09-17:48:25.194000
             "0"
             stats_summary:connected_wifi             @ 2024/07/09-17:46:13.391000
             "0"
             stats_summary:os_build                   @ 2024/07/09-17:48:25.194000
             "PQ2A.190406.000"
             stats_summary:os_build                   @ 2024/07/09-17:46:13.391000
             "PQ2A.190406.000"
         




## Use the test data

You can now use the `test_table` on the `test-instance` to test code samples or queries.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources created during these steps, delete the instance as soon as you finish testing. Deleting the .cbtrc file leaves you ready to work on a different project.

  1. If you want to keep the instance but delete the table, you can use the `deletetable` command:
         
         cbt deletetable test_table

  2. If you don't plan to use the instance for further testing, delete the instance. This action also deletes the table.
         
         cbt deleteinstance test-instance

  3. Delete the .cbtrc file:
         
         rm ~/.cbtrc




## What's next

  * [Explore Bigtable code samples.](https://docs.cloud.google.com/bigtable/docs/samples)
  * [Learn about the Key Visualizer tool for Bigtable.](https://docs.cloud.google.com/bigtable/docs/keyvis-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
