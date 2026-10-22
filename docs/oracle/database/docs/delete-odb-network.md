---
url: https://docs.cloud.google.com/oracle/database/docs/delete-odb-network/
title: Delete ODB Network and ODB Subnets \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:27:47.029577+00:00
---

# Delete ODB Network and ODB Subnets  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/delete-odb-network/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Delete ODB Network and ODB Subnets Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to delete an ODB Network and ODB Subnets.

Deleting an ODB Network or an ODB Subnet permanently removes it. You can't undo this later.

## Before you begin

  * Make sure that you have the required Identity and Access Management (IAM) roles and permissions to delete an ODB Network and ODB Subnets as described in [Deploy Oracle Database@Google Cloud environment](https://docs.cloud.google.com/oracle/database/docs/setup-oracle-database-environment#deploy-odb-environment).

  * Delete the Oracle Database@Google Cloud resources associated with the ODB Network and the ODB Subnet that you want to delete.




## Delete an ODB Subnet

To delete your ODB Subnet, do the following:

### Console

  1. Go to the **ODB Network** page.

[Go to ODB Network](https://console.cloud.google.com/oracle/odb-networks/)

  2. Click the ODB Network network for which you want to delete a subnet.

  3. Go to the **Subnets** section.

  4. For the subnet which you want to delete, click more_vert **View actions** , and then click **Delete**.

  5. In the **Delete ODB Subnet?** dialog, type the subnet name to confirm deletion of your subnet.

  6. Click **Confirm**.




### gcloud

Use the `gcloud oracle-database odb-networks odb-subnets delete` command to delete an ODB Subnet.
    
    
    gcloud oracle-database odb-networks odb-subnets delete ODB_SUBNET_ID \
        --project=PROJECT_ID \
        --location=REGION \
        --odb-network=ODB_NETWORK_ID
    

Replace the following:

  * ODB_SUBNET_ID: the ID of the ODB Subnet.
  * PROJECT_ID: the ID of your Google Cloud project which contains the ODB Subnet to be deleted. If you're using a Shared VPC, then this is the ID of your host project.
  * REGION: the region of the ODB Subnet.
  * ODB_NETWORK_ID: the ID of the ODB Network to which the ODB Subnet belongs.



###  API 

To delete an ODB Subnet, run the following `curl` command:
    
    
    curl -X DELETE \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/odbNetworks/ODB_NETWORK_ID/odbSubnets/ODB_SUBNET_ID"
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project which contains the ODB Subnet to be deleted. If you're using a Shared VPC, then this is the ID of your host project.
  * REGION: the region of the ODB Subnet.
  * ODB_NETWORK_ID: the ID of the ODB Network to which the ODB Subnet belongs.
  * ODB_SUBNET_ID: the ID of the ODB Subnet.



## Delete an ODB Network

Before deleting an ODB Network, you must delete its ODB Subnets.

To delete your ODB Network, do the following:

### Console

  1. Go to the **ODB Network** page.

[Go to ODB Network](https://console.cloud.google.com/oracle/odb-networks/)

  2. Click the ODB Network network which you want to delete.

  3. For the ODB Network which you want to delete, click more_vert **View actions** , and then click **Delete**.

  4. In the **Delete ODB Network?** dialog, type the ODB Network name to confirm deletion of your ODB Network.

  5. Click **Confirm**.




### gcloud

Use the `gcloud oracle-database odb-networks delete` command to delete an ODB Network.
    
    
    gcloud oracle-database odb-networks delete ODB_NETWORK_ID \
        --project=PROJECT_ID \
        --location=REGION
    

Replace the following:

  * ODB_NETWORK_ID: the ID of your ODB Network.
  * PROJECT_ID: the ID of your Google Cloud project which contains the ODB Network to be deleted. If you're using a Shared VPC, then this is the ID of your host project.
  * REGION: the region of the ODB Network.



###  API 

To delete an ODB Network, run the following `curl` command:
    
    
    curl -X DELETE \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/odbNetworks/ODB_NETWORK_ID"
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project which contains the ODB Network to be deleted. If you're using a Shared VPC, then this is the ID of your host project.
  * REGION: the region of your ODB Network.
  * ODB_NETWORK_ID: the ID of your ODB Network.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
