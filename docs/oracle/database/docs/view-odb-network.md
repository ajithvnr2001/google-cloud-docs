---
url: https://docs.cloud.google.com/oracle/database/docs/view-odb-network/
title: View ODB Network and ODB Subnet details \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:27:40.012817+00:00
---

# View ODB Network and ODB Subnet details  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/view-odb-network/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  View ODB Network and ODB Subnet details Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to view details of an ODB Network and ODB Subnets.

## Before you begin

  * Make sure that you have the required Identity and Access Management (IAM) roles and permissions to view details of an ODB Network and ODB Subnets as described in [Deploy Oracle Database@Google Cloud environment](https://docs.cloud.google.com/oracle/database/docs/setup-oracle-database-environment#deploy-odb-environment).



## List ODB Network and ODB Subnets

To list ODB Network and its ODB Subnets in a project, do the following:

### Console

  1. Go to the **ODB Network** page.

[Go to ODB Network](https://console.cloud.google.com/oracle/autonomous-databases/)

You can view the list of your ODB Networks.

  2. To view ODB Subnets of an ODB Network, click the ODB Network name, and go to the **Subnets** section.




### gcloud

Use the `gcloud oracle-database odb-networks list` command to list your ODB Networks.
    
    
    gcloud oracle-database odb-networks list \
        --project=PROJECT_ID \
        --location=REGION
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project. If you're using a Shared VPC, then this is the ID of your host project.
  * REGION: the region of the ODB Network.



Use the `gcloud oracle-database odb-networks odb-subnets list` command to list the ODB Subnets of an ODB Network.
    
    
    gcloud oracle-database odb-networks odb-subnets list \
        --project=PROJECT_ID \
        --location=REGION \
        --odb-network=ODB_NETWORK_ID
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project which contains the ODB Network. If you're using a Shared VPC, then this is the ID of your host project.
  * REGION: the region of the ODB Network.
  * ODB_NETWORK_ID: the ID of the ODB Network to which the ODB Subnet belongs.



###  API 

To list ODB Networks, run the following `curl` command:
    
    
    curl -X GET \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/odbNetworks"
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project. If you're using a Shared VPC, then this is the ID of your host project.
  * REGION: the region of your ODB Network.



To list ODB Subnets of an ODB Network, run the following `curl` command:
    
    
    curl -X GET \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/odbNetworks/ODB_NETWORK_ID/odbSubnets"
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project which contains the ODB Network. If you're using a Shared VPC, then this is the ID of your host project.
  * REGION: the region of your ODB Network.
  * ODB_NETWORK_ID: the ID of your ODB Network.



## View ODB Network and ODB Subnet details

To view details of an ODB Network and its ODB Subnets, do the following:

### Console

  1. Go to the **ODB Network** page.

[Go to ODB Network](https://console.cloud.google.com/oracle/autonomous-databases/)

  2. Click the ODB Network for which you want to view the details.

  3. On the **ODB Network details** page, you can view the details of the ODB Network.

  4. To view the details of the subnets, go to the **Subnets** section.

  5. To view change logs, select the **Operations** tab.




### gcloud

Use the `gcloud oracle-database odb-networks get` command to view details of an ODB Network.
    
    
    gcloud oracle-database odb-networks get ODB_NETWORK_ID \
        --project=PROJECT_ID \
        --location=REGION
    

Replace the following:

  * ODB_NETWORK_ID: the ID of your ODB Network.
  * PROJECT_ID: the ID of your Google Cloud project which contains the ODB Network. If you're using a Shared VPC, then this is the ID of your host project.
  * REGION: the region of the ODB Network.



Use the `gcloud oracle-database odb-networks odb-subnets get` command to view details of an ODB Subnet.
    
    
    gcloud oracle-database odb-networks odb-subnets get ODB_SUBNET_ID \
        --project=PROJECT_ID \
        --location=REGION \
        --odb-network=ODB_NETWORK_ID
    

Replace the following:

  * ODB_SUBNET_ID: the ID of the ODB Subnet.
  * PROJECT_ID: the ID of your Google Cloud project which contains the ODB Network. If you're using a Shared VPC, then this is the ID of your host project.
  * REGION: the region of the ODB Network.
  * ODB_NETWORK_ID: the ID of the ODB Network to which the ODB Subnet belongs.



###  API 

To view details of an ODB Network, run the following `curl` command:
    
    
    curl -X GET \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/odbNetworks/ODB_NETWORK_ID"
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project which contains the ODB Network. If you're using a Shared VPC, then this is the ID of your host project.
  * REGION: the region of your ODB Network.
  * ODB_NETWORK_ID: the ID of your ODB Network.



To view details of an ODB Subnet, run the following `curl` command:
    
    
    curl -X GET \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/odbNetworks/ODB_NETWORK_ID/odbSubnets/ODB_SUBNET_ID"
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project which contains the ODB Network. If you're using a Shared VPC, then this is the ID of your host project.
  * REGION: the region of your ODB Network.
  * ODB_NETWORK_ID: the ID of your ODB Network.
  * ODB_SUBNET_ID: the ID of the ODB Subnet.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
