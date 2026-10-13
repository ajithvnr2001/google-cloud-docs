---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/db-clone-cluster/
title: Clone a database cluster \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:10:07.041250+00:00
---

# Clone a database cluster  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/db-clone-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Clone a database cluster Stay organized with collections  Save and categorize content based on your preferences. 

You can clone a database cluster to create a new database cluster that contains the same data as the original cluster. Cloning is a good way to make database clusters for testing purposes.

## Before you begin

Make sure the source database cluster to clone from has the backup service enabled.

After the recovery window is available for the source database cluster, you can specify a point in time within the recovery window to base the clone on. You aren't limited to cloning the present state of a database cluster. The database service clones a new database cluster at the exact point in time you specify.

## Clone database cluster

You can clone a database cluster with the GDC console or with the gdcloud CLI tool:

### Console

  1. From the main menu of the GDC console, choose **Database Service**.
  2. Select the database cluster to clone.
  3. Click add_box **CLONE**.
  4. In the _Create a clone_ dialog, specify the point in time to clone from and specify an ID for the new database cluster.
  5. Click **CLONE**. This takes you to the Database cluster overview page for the new cluster where you can monitor its status.



###  gdcloud CLI 

Use the following command to clone a database cluster:
    
    
    gdcloud database clusters clone SOURCE \
       DESTINATION --point-in-time POINT_IN_TIME
    

Replace the following:

  * SOURCE with the name of the database cluster to create a clone from.
  * DESTINATION with the name of the new database cluster to create.
  * POINT_IN_TIME with the timestamp of the point in time to use as the basis of the clone. Use the [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) timestamp format (`yyyy-MM-dd'T'HH:mm:ss'Z'`). The timestamp must be within the recovery window of the source database cluster, otherwise the clone request gets rejected.



###  API 

To clone a database cluster, create a Restore resource:
    
    
    apiVersion: postgresql.dbadmin.gdc.goog/v1
    kind: Restore
    metadata:
      name: NEW_DBCLUSTER_NAME_restore
      namespace: NAMESPACE
    spec:
      sourceDBCluster: DBCLUSTER_NAME
      pointInTime: "POINT_IN_TIME"
      clonedDBClusterConfig:
        dbclusterName: NEW_DBCLUSTER_NAME
    

Replace the following:

  * `NEW_DBCLUSTER_NAME`: the name of the new database cluster to create.
  * `NAMESPACE`: the namespace to create the new database cluster in.
  * `POINT_IN_TIME`: the timestamp of the point in time to use as the basis of the clone. Use the [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) timestamp format (`yyyy-MM-dd'T'HH:mm:ss'Z'`). Set a timestamp within the recovery window of the source database cluster; otherwise, the system rejects the clone request. Run `kubectl get backupplan.o -n NAMESPACE` to determine the recovery window.

**Note:** The Restore resource must be created in the same namespace as the source database cluster.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
