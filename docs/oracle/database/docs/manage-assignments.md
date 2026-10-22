---
url: https://docs.cloud.google.com/oracle/database/docs/manage-assignments/
title: Manage Goldengate connection assignments \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:27:46.411261+00:00
---

# Manage Goldengate connection assignments  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/manage-assignments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Manage Goldengate connection assignments Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage Goldengate connection assignments in Google Cloud.

## Before you begin

  * Make sure that you have the required Identity and Access Management (IAM) roles and permissions to perform the tasks described in this page:

    * `roles/oracledatabase.goldenGateConnectionAssignmentAdmin`
    * `roles/oracledatabase.goldenGateConnectionAssignmentViewer`

For more information about how to assign roles, see [Apply IAM roles](https://docs.cloud.google.com/oracle/database/docs/iam-roles).




## View connection assignment details

To view connection assignment information about your connection assignments, do the following:

### Console

  1. Go to the **Goldengate** page.

[Go to Goldengate](https://console.cloud.google.com/oracle/golden-gate/)

  2. Select the **Deployments** tab.

The **Deployment** section shows you the list of deployments.

  3. Click the name of the deployment whose connection assignments you want to view.

  4. On the **Deployment details** page, go to the **Assigned connections** section.

The **Assigned connections** section shows you the details of the connection assignments of the deployment.




### gcloud

  * **List connection assignments**

Use the `gcloud oracle-database goldengate-connection-assignments list` command to list connection assignments.
        
        gcloud oracle-database goldengate-connection-assignments list \
            --project=PROJECT_ID \
            --location=REGION
        

Replace the following:

    * PROJECT_ID: the ID of your Google Cloud project. If you're using a Shared VPC, then this is the ID of your host project.
    * REGION: the region where you want to view the connection assignments.
  * **View connection assignment details**

Use the `gcloud oracle-database goldengate-connection-assignments describe` command to view details of a connection assignment.
        
        gcloud oracle-database goldengate-connection-assignments describe ASSIGNMENT_ID \
            --project=PROJECT_ID \
            --location=REGION
        

Replace the ASSIGNMENT_ID with the ID of your connection assignment.




###  API 

  * **List connection assignments**

To list connection assignments, run the following `curl` command:
        
        curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/goldengateConnectionAssignments"
        

Replace the following:

    * PROJECT_ID: the ID of your Google Cloud project. If you're using a Shared VPC, then this project ID is the ID of your host project.
    * REGION: the region where you want to view the connection assignments.
  * **View connection assignment details**

To view details of a connection assignment, run the following `curl` command:
        
        curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/goldengateConnectionAssignments/ASSIGNMENT_ID"
        

Replace the ASSIGNMENT_ID with the ID of your connection assignment.




## Delete a connection assignment

To delete a connection assignment, do the following:

### gcloud

Use the `gcloud oracle-database goldengate-connection-assignments delete` command to delete a connection assignment.
    
    
    gcloud oracle-database goldengate-connection-assignments delete ASSIGNMENT_ID \
        --project=PROJECT_ID \
        --location=REGION
    

Replace the following:

  * ASSIGNMENT_ID: the ID of the connection assignment.
  * PROJECT_ID: the ID of your Google Cloud project. If you're using a Shared VPC, then this is the ID of your host project.
  * REGION: the region where your connection assignment is located.



###  API 

To delete a connection assignment, run the following `curl` command:
    
    
    curl -X DELETE \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/goldengateConnectionAssignments/ASSIGNMENT_ID"
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project which contains the connection assignment to be deleted. If you're using a Shared VPC, then this is the ID of your host project.
  * REGION: the region where your connection assignment is located.
  * CONNECTION_ID: the ID of your connection assignment.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
