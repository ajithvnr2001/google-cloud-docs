---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/delete-org/
title: Immediately delete an Apigee or Apigee hybrid organization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:27:25.012152+00:00
---

# Immediately delete an Apigee or Apigee hybrid organization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/delete-org/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Immediately delete an Apigee or Apigee hybrid organization Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

This document outlines the steps to immediately delete an Apigee or Apigee hybrid organization without a soft-deletion data retention period. 

You can perform an immediate deletion of an Apigee or Apigee hybrid organization by calling the Apigee API [`organizations.delete`](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/delete) method and setting the `retention` query parameter to `NO_RETENTION`. 

**Note:** You will NOT be able to restore the Apigee organization when using the `NO_RETENTION` option as it will be immediately deleted. 

## Instructions

Follow these steps to start and track the immediate deletion of an Apigee or Apigee hybrid organization. 

  1. Issue the immediate delete request by calling the [`organizations.delete`](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/delete) API with the `retention=NO_RETENTION` query parameter: 
         
         curl -X DELETE -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           'https://apigee.googleapis.com/v1/organizations/ORG_NAME?retention=NO_RETENTION'
         

Where ORG_NAME is the name of the Apigee organization that you want to delete. 

When the immediate deletion request starts successfully, the command returns a long-running operation similar to the following output: 
         
         {
           "name": "organizations/shreypaidapgx/operations/29b3280b-4287-46dc-8a08-069daf9f9bd4",
           "metadata": {
             "@type": "type.googleapis.com/google.cloud.apigee.v1.OperationMetadata",
             "operationType": "DELETE",
             "targetResourceName": "organizations/shreypaidapgx",
             "state": "IN_PROGRESS"
           }
         }

  2. Track the status of the delete operation using the operation ID returned in the output of the previous command. The deletion is expected to take at most 2 hours. 

In the following commands, replace ORG_NAME with the name of your Apigee organization and OPERATION_ID with the operation ID from the previous step (for example, `29b3280b-4287-46dc-8a08-069daf9f9bd4`). 

     * While the deletion is in progress, polling the operation returns a `state` of `IN_PROGRESS`: 
           
           curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             'https://apigee.googleapis.com/v1/organizations/ORG_NAME/operations/OPERATION_ID'
           
           
           {
             "name": "organizations/shreypaidapgx/operations/29b3280b-4287-46dc-8a08-069daf9f9bd4",
             "metadata": {
               "@type": "type.googleapis.com/google.cloud.apigee.v1.OperationMetadata",
               "operationType": "DELETE",
               "targetResourceName": "organizations/shreypaidapgx",
               "state": "IN_PROGRESS"
             }
           }

     * When the deletion is completed, polling the operation returns a `state` of `FINISHED` and `"done": true`: 
           
           curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             'https://apigee.googleapis.com/v1/organizations/ORG_NAME/operations/OPERATION_ID'
           
           
           {
             "name": "organizations/shreypaidapgx/operations/29b3280b-4287-46dc-8a08-069daf9f9bd4",
             "metadata": {
               "@type": "type.googleapis.com/google.cloud.apigee.v1.OperationMetadata",
               "operationType": "DELETE",
               "targetResourceName": "organizations/shreypaidapgx",
               "state": "FINISHED"
             },
             "done": true,
             "response": {
               "@type": "type.googleapis.com/google.protobuf.Empty"
             }
           }




## Troubleshooting immediate delete

If the operation `state` stays `IN_PROGRESS` for more than 2 hours, contact [Google Cloud Support](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support) for investigation. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
