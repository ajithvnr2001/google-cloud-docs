---
url: https://docs.cloud.google.com/alloydb/docs/test-high-availability/
title: Test a primary instance for high availability \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:45:51.196161+00:00
---

# Test a primary instance for high availability  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/test-high-availability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Test a primary instance for high availability Stay organized with collections  Save and categorize content based on your preferences. 

AlloyDB for PostgreSQL offers regional and zonal instance types. To help ensure high availability (HA), every regional AlloyDB primary instance has both an active node and a standby node, located in two different zones. If the active node becomes unavailable for any reason, then AlloyDB automatically promotes the standby node to become the new active node.

You can test this automatic HA feature by using _fault injection_ to abruptly force your primary instance's active node offline. AlloyDB then activates the emergency HA procedure that checks the primary instance's health and then reassigns the standby node into the active-node role.

Fault injection also initiates a long-running operation that brings the former active node back online after a brief interval. That node becomes the new standby node of the primary instance.

For a faster method of swapping the active and standby roles of your primary instance's nodes, see [Fail over a primary instance manually](https://docs.cloud.google.com/alloydb/docs/instance-primary-secondary-failover).

## Before you begin

  * The Google Cloud project you are using must have been [enabled to access AlloyDB](https://docs.cloud.google.com/alloydb/docs/quickstart/create-and-connect#before-you-begin). 
  * You must have one of these IAM roles in the Google Cloud project you are using: 
    * `roles/alloydb.admin` (the AlloyDB Admin predefined IAM role)
    * `roles/owner` (the Owner basic IAM role)
    * `roles/editor` (the Editor basic IAM role)

If you don't have any of these roles, contact your Organization Administrator to request access.




## Simulate an outage with a fault injection

**Note:** This procedure does not apply to [basic instances](https://docs.cloud.google.com/alloydb/docs/basic-instance), which do not have a standby node to fail over to.

To test your primary instance's HA resiliency by abruptly shutting down its active node, use the [`gcloud alloydb instances inject-fault`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/inject-fault) command. After a long-running operation completes, AlloyDB reinstates the node.
    
    
    gcloud alloydb instances inject-fault INSTANCE_ID \
        --fault-type=stop-vm \
        --region=REGION_ID \
        --cluster=CLUSTER_ID \
        --project=PROJECT_ID
    

  * `INSTANCE_ID`: The ID of the instance.
  * `REGION_ID`: The region where the instance is placed.
  * `CLUSTER_ID`: The ID of the cluster where the instance is placed.
  * `PROJECT_ID`: The ID of the project where the cluster is placed.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
