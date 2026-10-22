---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/db-delete-cluster/
title: Delete database clusters \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:14:53.307812+00:00
---

# Delete database clusters  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/db-delete-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Delete database clusters Stay organized with collections  Save and categorize content based on your preferences. 

You can delete database clusters with the GDC console or the Distributed Cloud CLI.

**Note:** When backup is disabled, deleting a database cluster is an irreversible action. When backup is enabled, you have the option to delete a cluster while keeping its backups. This makes the cluster recoverable within your set retention period.

###  Console 

  1. From the main menu of the GDC console, choose **Database Service**.
  2. Select the database cluster to delete.
  3. Click delete **DELETE**.
  4. Optional: If backup was previously enabled, select **Delete all backups**. This results in a permanent deletion. Otherwise, backups will be automatically deleted once the project's retention period expires.
  5. Confirm deletion by typing the cluster's ID.
  6. Click delete **DELETE** to finish.



###  gdcloud CLI 

Delete a database cluster while keeping its backups:
    
    
    gdcloud database clusters delete CLUSTER_NAME
    

To permanently delete a database cluster along with all of its backups, include the `--hard` flag:
    
    
    gdcloud database clusters delete CLUSTER_NAME --hard
    

Replace CLUSTER_NAME with the name of the database cluster to delete.

For database clusters with backup enabled, omitting `--hard` deletes the database cluster while keeping its backups (making the database cluster recoverable within the retention period). Adding `--hard` immediately and permanently deletes the database cluster and all of its backups.

###  API 
    
    
    kubectl patch dbcluster.DBENGINE_NAME.dbadmin.gdc.goog DBCLUSTER_NAME -p '{"spec":{"isDeleted": true}}' --type=merge -n USER_PROJECT
    kubectl delete dbcluster.DBENGINE_NAME.dbadmin.gdc.goog DBCLUSTER_NAME -n USER_PROJECT # for database clusters with backup enabled, this will permanently delete the database.
    

Replace the following variables:

  * `DBENGINE_NAME`, the name of the database engine. This is one of `alloydbomni`, `postgresql`, or `oracle`.
  * `USER_PROJECT`, the name of the user project where the database cluster was created.
  * `DBCLUSTER_NAME`, the name of the database cluster.



For database clusters without backup, only the first step is needed. For databases with backup, running the first command only will delete the database while keeping its backups (and therefore the database cluster is still recoverable). These backups will be deleted after their retention time if no action is taken. The second command can be used to immediately delete the database cluster and all of its backups.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
