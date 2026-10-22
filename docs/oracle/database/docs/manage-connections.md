---
url: https://docs.cloud.google.com/oracle/database/docs/manage-connections/
title: Manage Goldengate connections \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:27:45.945726+00:00
---

# Manage Goldengate connections  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/manage-connections/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Manage Goldengate connections Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage Goldengate connections in Google Cloud.

## Before you begin

  * Make sure that you have the required Identity and Access Management (IAM) roles and permissions to perform the tasks described in this page:

    * `roles/oracledatabase.goldenGateConnectionAdmin`
    * `roles/oracledatabase.goldenGateConnectionViewer`

For more information about how to assign roles, see [Apply IAM roles](https://docs.cloud.google.com/oracle/database/docs/iam-roles).




## View connection details

To view information about your connections, do the following:

### Console

  1. Go to the **Goldengate** page.

[Go to Goldengate](https://console.cloud.google.com/oracle/golden-gate/)

  2. Select the **Connections** tab.

The **Connections** section shows you the list of connections.

  3. To view details of a specific connection, click the name of the connection.




### gcloud

  * **List connections**

Use the `gcloud oracle-database goldengate-connections list` command to list connections.
        
        gcloud oracle-database goldengate-connections list \
            --project=PROJECT_ID \
            --location=REGION
        

Replace the following:

    * PROJECT_ID: the ID of your Google Cloud project. If you're using a Shared VPC, then this is the ID of your host project.
    * REGION: the region where you want to view the connections.
  * **View connection details**

Use the `gcloud oracle-database goldengate-connections describe` command to view details of a connection.
        
        gcloud oracle-database goldengate-connections describe CONNECTION_ID \
            --project=PROJECT_ID \
            --location=REGION
        

Replace CONNECTION_ID with the ID of your connection.




###  API 

  * **List connections**

To list connections, run the following `curl` command:
        
        curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/goldengateConnections"
        

Replace the following:

    * PROJECT_ID: the ID of your Google Cloud project. If you're using a Shared VPC, then this project ID is the ID of your host project.
    * REGION: the region where you want to view the connections.
  * **View connection details**

To view details of a connection, run the following `curl` command:
        
        curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/goldengateConnections/CONNECTION_ID"
        

Replace CONNECTION_ID with the ID of your connection.




## Modify a connection

You can modify your connections in the OCI console. To view your connections in the OCI console, do the following:

  1. Go to the **Goldengate** page.

[Go to Goldengate](https://console.cloud.google.com/oracle/golden-gate/)

  2. Select the **Connections** tab.

The **Connections** section shows you the list of connections.

  3. For a connection that you want to modify, click more_vert **View actions** , and then **Manage in OCI**.




You're redirected to the OCI page to modify your connection.

## Delete a connection

You can delete a connection even if it's assigned to a deployment. Deleting a connection also deletes its connection assignment.

### Console

  1. Go to the **Goldengate** page.

[Go to Goldengate](https://console.cloud.google.com/oracle/golden-gate/)

  2. Select the **Connections** tab.

  3. For the connection which you want to delete, click more_vert **View actions** , and then click **Delete**.

  4. In the **Delete connection?** dialog, type the connection ID to confirm the deletion of your connection.

  5. Click **Confirm**.




### gcloud

Use the `gcloud oracle-database goldengate-connections delete` command to delete a connection.
    
    
    gcloud oracle-database goldengate-connections delete CONNECTION_ID \
        --project=PROJECT_ID \
        --location=REGION
    

Replace the following:

  * CONNECTION_ID: the ID of the connection.
  * PROJECT_ID: the ID of your Google Cloud project. If you're using a Shared VPC, then this is the ID of your host project.
  * REGION: the region where your connection is located.



###  API 

To delete a connection, run the following `curl` command:
    
    
    curl -X DELETE \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/goldengateConnections/CONNECTION_ID"
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project which contains the connection to be deleted. If you're using a Shared VPC, then this is the ID of your host project.
  * REGION: the region where your connection is located.
  * CONNECTION_ID: the ID of your connection.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
