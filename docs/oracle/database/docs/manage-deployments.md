---
url: https://docs.cloud.google.com/oracle/database/docs/manage-deployments/
title: Manage Goldengate deployments \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:01.249256+00:00
---

# Manage Goldengate deployments  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/manage-deployments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Manage Goldengate deployments Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage Goldengate deployments in Google Cloud.

## Before you begin

  * Make sure that you have the required Identity and Access Management (IAM) roles and permissions to perform the tasks described in this page:

    * `roles/oracledatabase.goldenGateDeploymentAdmin`
    * `roles/oracledatabase.goldenGateDeploymentViewer`

For information on how to assign roles, see [Apply IAM roles](https://docs.cloud.google.com/oracle/database/docs/iam-roles).




## View deployment details

To view information about your Goldengate deployments, do the following:

### Console

  1. Go to the **Goldengate** page.

[Go to Goldengate](https://console.cloud.google.com/oracle/golden-gate/)

  2. Select the **Deployments** tab.

The **Deployment** section shows you the list of deployments.

  3. To view details of a deployment, click the name of the deployment.




### gcloud

  * **List deployments**

Use the `gcloud oracle-database goldengate-deployments list` command to list deployments.
        
        gcloud oracle-database goldengate-deployments list \
            --project=PROJECT_ID \
            --location=REGION
        

Replace the following:

    * PROJECT_ID: the ID of your Google Cloud project. If you're using a Shared VPC, then this is the ID of your host project.
    * REGION: the region where you want to view the deployments.
  * **View deployment details**

Use the `gcloud oracle-database goldengate-deployments describe` command to view details of a deployment.
        
        gcloud oracle-database goldengate-deployments describe DEPLOYMENT_ID \
            --project=PROJECT_ID \
            --location=REGION
        

Replace the following:

    * DEPLOYMENT_ID: the ID of the deployment.
    * PROJECT_ID: the ID of your Google Cloud project. If you're using a Shared VPC, then this is the ID of your host project.
    * REGION: the region where your deployment is located.



###  API 

  * **List Goldengate deployments**

To list deployments, run the following `curl` command:
        
        curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/goldengateDeployments"
        

Replace the following:

    * PROJECT_ID: the ID of your Google Cloud project. If you're using a Shared VPC, then this project ID is the ID of your host project.
    * REGION: the region where you want to view the deployments.
  * **View Goldengate deployment details**

To view details of a deployment, run the following `curl` command:
        
        curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/goldengateDeployments/DEPLOYMENT_ID"
        

Replace DEPLOYMENT_ID with the ID of your deployment.




## Start a deployment

Starting an instance allows connections and operations.

To start a Goldengate deployment instance, do the following:

### gcloud

Use the `gcloud oracle-database goldengate-deployments start` command to start a deployment instance.
    
    
    gcloud oracle-database goldengate-deployments start DEPLOYMENT_ID \
        --project=PROJECT_ID \
        --location=REGION \
    

Replace the following:

  * DEPLOYMENT_ID: the ID of your deployment
  * PROJECT_ID: the ID of your Google Cloud project
  * REGION: the region where your deployment is located



###  API 

To start a Goldengate deployment instance, run the following `curl` command:
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/goldengateDeployments/DEPLOYMENT_ID:start"
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project.
  * REGION: the region where your deployment is located.
  * DEPLOYMENT_ID: the ID of your deployment.



A deployment instance continues to run until you stop it.

## Stop a deployment

Stopping a deployment shuts down the deployment instance, along with its connections, open files, and running operations. It remains stopped until you restart it.

To stop a Goldengate deployment, do the following:

### gcloud

Use the `gcloud oracle-database goldengate-deployments stop` command to stop a deployment instance.
    
    
    gcloud oracle-database goldengate-deployments stop DEPLOYMENT_ID \
        --project=PROJECT_ID \
        --location=REGION \
    

Replace the following:

  * DEPLOYMENT_ID: the ID of your deployment
  * PROJECT_ID: the ID of your Google Cloud project
  * REGION: the region where your deployment is located



###  API 

To stop a Goldengate deployment, run the following `curl` command:
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/goldengateDeployments/DEPLOYMENT_ID:stop"
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project which contains your deployment
  * REGION: the region where your deployment is located
  * DEPLOYMENT_ID: the ID of your deployment



## Modify a deployment

You can modify your Goldengate deployment in the OCI console. To modify a deployment in the OCI console, do the following:

  1. Go to the **Goldengate** page.

[Go to Goldengate](https://console.cloud.google.com/oracle/golden-gate/)

  2. Select the **Deployments** tab.

The **Deployment** section shows you the list of deployments.

  3. For the deployment which you want to modify, click more_vert **View actions** , and then click **Manage in OCI**.




You're redirected to the OCI page to modify your Goldengate deployment.

## Delete a deployment

Deleting a deployment also deletes its connection assignment.

To delete a deployment, do the following:

### Console

  1. Go to the **Goldengate** page.

[Go to Goldengate](https://console.cloud.google.com/oracle/golden-gate/)

  2. Select the **Deployments** tab.

  3. For the deployment which you want to delete, click more_vert **View actions** , and then click **Delete**.

  4. In the **Delete deployment?** dialog, type the deployment ID to confirm the deletion of your deployment.

  5. Click **Confirm**.




### gcloud

Use the `gcloud oracle-database goldengate-deployments delete` command to delete a deployment.
    
    
    gcloud oracle-database goldengate-deployments delete DEPLOYMENT_ID \
        --project=PROJECT_ID \
        --location=REGION
    

Replace the following:

  * DEPLOYMENT_ID: the ID of the deployment.
  * PROJECT_ID: the ID of your Google Cloud project. If you're using a Shared VPC, then this is the ID of your host project.
  * REGION: the region where your deployment is located.



###  API 

To delete a Goldengate deployment, run the following `curl` command:
    
    
    curl -X DELETE \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/goldengateDeployments/DEPLOYMENT_ID"
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project which contains the deployment to be deleted. If you're using a Shared VPC, then this is the ID of your host project.
  * REGION: the region where your deployment is located.
  * DEPLOYMENT_ID: the ID of your deployment.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
