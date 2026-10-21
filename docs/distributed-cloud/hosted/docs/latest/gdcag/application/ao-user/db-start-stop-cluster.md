---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/db-start-stop-cluster/
title: Start and stop database clusters \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:08:45.645664+00:00
---

# Start and stop database clusters  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/db-start-stop-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Start and stop database clusters Stay organized with collections  Save and categorize content based on your preferences. 

Stopping a database cluster pauses the cluster to save resources. You can stop and start database clusters with the Google Distributed Cloud (GDC) air-gapped console or with the gdcloud CLI tool.

### Console

  1. From the main menu of the GDC console, choose **Database Service**.
  2. Select the database cluster to start or stop.
  3. Click **STOP** or **START**.



###  gdcloud CLI 

Use the following command to stop a database cluster:
    
    
    gdcloud database clusters stop CLUSTER_NAME
    

Use the following command to start a database cluster:
    
    
    gdcloud database clusters start CLUSTER_NAME
    

Replace the following:

  * CLUSTER_NAME with the name of the database cluster to start or stop.



###  API 
    
    
    kubectl patch dbcluster.postgresql.dbadmin.gdc.goog DBCLUSTER_NAME -p '{"spec":{"primarySpec": {"isStopped": IS_STOPPED}}}' --type=merge -n USER_PROJECT
    

Replace the following variables:

  * `DBCLUSTER_NAME`, the name of the database cluster.
  * `USER_PROJECT`, the name of the user project where the database cluster was created.
  * `IS_STOPPED` to indicate whether the database cluster should be stopped (`true`) or not (`false`).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
