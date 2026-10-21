---
url: https://docs.cloud.google.com/integration-connectors/docs/vpcsc-connectors/
title: Set up VPC Service Controls for Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:28:51.080910+00:00
---

# Set up VPC Service Controls for Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/vpcsc-connectors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up VPC Service Controls for Integration Connectors

VPC Service Controls lets you define a security perimeter around the Integration Connectors Google Cloud service. With the security perimeter around your service, you can constrain data within a VPC Service Controls perimeter and mitigate data exfiltration risks. If you are not already familiar with VPC Service Controls, it is recommended that you go through the following information: 

  * [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview)
  * [Service perimeter details and configuration](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters)
  * [Grant access to VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/access-control)



This document describes how to restrict access to Integration Connectors service (`connectors.googleapis.com`) by using the VPC Service Controls perimeter. After setting up the perimeter, you can configure policies that determine what other Google Cloud services or users can access the `connectors.googleapis.com` service. 

## Considerations

  * If your connection is connecting to a Google Cloud resource, then that resource must be accessible from within the VPC Service Controls perimeter.
  * If you have existing connections to a public endpoint, before setting up the VPC Service Controls perimeter, ensure that such connections use the PSC ([Private Service Connect](https://docs.cloud.google.com/integration-connectors/docs/private-connectivity-overview)) attachment to connect the backend systems. Without the PSC attachment, existing connections to a public endpoint will fail after you set up the VPC Service Controls perimeter. 
  * If your connection is connecting to a non-Google Cloud resource, the destination of the connection should be a PSC attachment. Connections created without the PSC attacment will fail.
  * If you are setting up a VPC Service Controls perimeter for your Google Cloud project, you must enable private connectivity for event subscriptions to use the [event subscription feature](https://docs.cloud.google.com/integration-connectors/docs/eventsubscription) for the project.



## Before you begin

Ensure that you have the required permissions to configure VPC Service Controls perimeters. To view a list of IAM roles required to configure VPC Service Controls, see [Access control with IAM](https://docs.cloud.google.com/vpc-service-controls/docs/access-control) in the VPC Service Controls documentation. 

## Create a VPC Service Controls perimeter

To create a VPC Service Controls perimeter you can use either the `Google Cloud console`, or the `gcloud` command, or the [accessPolicies.servicePerimeters.create](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters/create) API. For more information, see [Create a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters#create-perimeter). 

The following steps show how to create a VPC Service Controls perimeter with a user access enabled by using the `gcloud` commands.

  1. Create an `access.yaml` file having the details of the user who is allowed to access the perimeter. For example: 
         
         - members:
             - user:USER_EMAIL

  2. Get your organization's access policy ID by using the following command:
    
    gcloud access-context-manager policies list --organization=ORGANIZATION_ID

This command lists all the policies for the organization. From the list, select the policy for which you want to create the VPC Service Controls perimeter. 

You can view your organization's resource ID by using the Google Cloud console. For more information, see [Getting your organization resource ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id). 

  3. Create access level for the user. 
         
         gcloud access-context-manager levels create ACCESS_LEVEL_NAME \
         --title "CUSTOM_TITLE" \
         --basic-level-spec access.yaml \
         --policy=POLICY_ID

In this command, POLICY_ID, is the value that you got from the previous step.

  4. In your Google Cloud project's global settings, set the value of the `vpcsc` attribute to `true`. 
         
         curl -X PATCH -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -d '{"vpcsc": true}' \
         https://connectors.googleapis.com/v1/projects/PROJECT_ID/locations/global/settings

This command returns an operation ID and starts a long-running operation (LRO) which may take some time to complete. Wait for the LRO to complete. You can track the progress of the operation by using the following command:
         
         curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         https://connectors.googleapis.com/v1/projects/PROJECT_ID/locations/global/operations/OPERATION_ID

  5. Create the VPC Service Controls perimeter and provide access to the user. 
         
         gcloud access-context-manager perimeters create PERIMETER_NAME \
         --title="PERIMETER_TITLE" \
         --resources=projects/PROJECT_ID \
         --restricted-services=connectors.googleapis.com \
         --access_levels=ACCESS_LEVEL_NAME

This command takes some time to complete, during which you can run other tasks in a new terminal.

If want to update the access level, and add the `connectors.googleapis.com` service to an existing perimeter, run the following command: 
         
         gcloud access-context-manager perimeters update PERIMETER_NAME \
         --add-restricted-services="connectors.googleapis.com" \
         --add-access-levels=ACCESS_LEVEL_NAME \
         --policy=POLICY_ID




## Verify your perimeter

To verify the perimeter, use the [gcloud access-context-manager perimeters describe PERIMETER_NAME](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/describe) command. For example:
    
    
    gcloud access-context-manager perimeters describe PERIMETER_NAME

For more information, see [Managing service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#list-and-describe). 

## Remove a project from the VPC Service Controls perimeter

To remove your Google Cloud project from the VPC Service Controls perimeter, perform the following steps:

  1. In your Google Cloud project's global settings, set the value of the `vpcsc` attribute to `false`. 
         
         curl -X PATCH -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -d '{"vpcsc": false}' \
         https://connectors.googleapis.com/v1/projects/PROJECT_ID/locations/global/settings

This command returns an operation ID and starts a long-running operation (LRO) which may take some time to complete. Wait for the LRO to complete. You can track the progress of the operation by using the following command:
         
         curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         https://connectors.googleapis.com/v1/projects/PROJECT_ID/locations/global/operations/OPERATION_ID

  2. Remove your project from the VPC Service Controls perimeter. 
         
         gcloud access-context-manager perimeters update accessPolicies/POLICY_ID/servicePerimeters/PERIMETER_NAME




## What's next

Learn how [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) protects your data. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
