---
url: https://docs.cloud.google.com/alloydb/docs/pgaudit/enable-audit/
title: Enable pgAudit \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:44:24.491890+00:00
---

# Enable pgAudit  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/pgaudit/enable-audit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Enable pgAudit Stay organized with collections  Save and categorize content based on your preferences. 

To enable auditing on an AlloyDB instance, you perform two steps. First, you enable alloydb.enable_pgaudit flag on the instance. Then, you connect to the cluster's primary instance and create the pgaudit extension in the databases.

**Note:** Only users who are members of the `alloydbsuperuser` role can create extensions. The postgres user role that is created when you create a new cluster is a member of the `alloydbsuperuser` role. 

  1. Enable pgAudit on the instance: 

### Console

     1. In the Google Cloud console, go to the **Clusters** page. 

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

     2. Click a cluster in the **Resource Name** column.
     3. In the **Overview** page, go to **Instances in your cluster** , select an instance, and then click **Edit**.
     4. Add the `alloydb.enable_pgaudit` flag on your instance: 
        1. Click **Add flag**.
        2. Select the `alloydb.enable_pgaudit` flag from the **New database flag** list.
        3. Select **on** from the **Value** list.
        4. Click **Done**.
     5. Click **Update instance**.

### gcloud

Enable pgAudit on an instance by setting that instance's `alloydb.enable_pgaudit` flag to `on`. For more information on setting an instance's database flags using the Google Cloud CLI, see [Configure an instance's database flags](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags).

Note that AlloyDB automatically restarts the instance after you update this flag.

**Note:** The default value for the `pgaudit.log` flag is `none`. To use the pgAudit extension, you must [set values for this flag.](https://docs.cloud.google.com/alloydb/docs/pgaudit/configure-log-behavior)
  2. Connect to the primary instance and create the extension in each database. You must perform the following steps on the primary instance even if you are enabling auditing on a read pool instance: 
     1. Connect a psql client to the cluster's primary instance, as described in [Connect a psql client to an instance](https://docs.cloud.google.com/alloydb/docs/connect-psql). 
     2. At the psql command prompt, connect to the database and create the extension: 
            
            \c DB_NAME
                CREATE EXTENSION IF NOT EXISTS pgaudit;
                

     3. Repeat the previous two steps to connect to other databases and create the extension in each one of them. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
