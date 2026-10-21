---
url: https://docs.cloud.google.com/deployment-manager/docs/configuration/sharing-types-across-projects/
title: Sharing Types Across Projects \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:25:46.433897+00:00
---

# Sharing Types Across Projects  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/configuration/sharing-types-across-projects/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  Sharing Types Across Projects Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to share [types and type providers](https://docs.cloud.google.com/deployment-manager/docs/fundamentals#types) that belong to your project with other projects. For example, assume you have a project that is responsible for maintaining pre-approved type providers for your company. You want to be able to share these type providers from that project with other projects and to use the project as a central repository of types. Similarly, you can also use this method to share composite types across projects.

To set up access, a project owner from the project that owns the type will need to grant the `deploymentmanager.typeViewer` (beta) role to the service account of the project that wants to consume the types. They also need to grant the role to users who want to view and list types from another project..

## Before you begin

  * If you want to use the command-line examples in this guide, install the [`gcloud` command-line tool](https://docs.cloud.google.com/sdk).
  * If you want to use the API examples in this guide, set up [API access](https://docs.cloud.google.com/deployment-manager/docs/reference/latest).
  * Read about Deployment Manager [configurations](https://docs.cloud.google.com/deployment-manager/docs/configuration/create-basic-configuration).
  * Read about [Types](https://docs.cloud.google.com/deployment-manager/docs/fundamentals#types).
  * Read the [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam) documentation.



## Limitations

The following are restrictions for using this feature:

  * Granting the `deploymentmanager.typeViewer` role grants permissions to all types in the specific project. It is not possible to limit sharing to individual types.
  * It is not possible to grant this role to [`allAuthenticatedUsers`](https://docs.cloud.google.com/iam/docs/principals-overview#allauthenticatedusers) or [`allUsers`](https://docs.cloud.google.com/iam/docs/principals-overview#allusers).



## Granting a project access to use types

To grant access to types that belong to other projects, the owner of the project that owns the types in question must grant the `deploymentmanager.typeViewer` role to the [Google APIs service account](https://docs.cloud.google.com/deployment-manager/docs/access-control#access_control_for_deployment_manager) of the project that wants to consume the types.

  1. Go to the IAM page in the Google Cloud console of the project that will be consuming the types. 

[Go to the IAM page](https://console.cloud.google.com/iam-admin/iam/)

  2. If prompted, select your project from the list.
  3. Look for the **Google APIs service account** , which has the email address in the following format:
         
         [PROJECT_NUMBER]@cloudservices.gserviceaccount.com
         

**Note:** This email address requires the project number, not the project ID. To learn how to identify the project number, see [Identifying projects](https://docs.cloud.google.com/compute/docs/projects#projectids).
  4. Make note of the email address above. Next, a project owner of the project where the desired types live can grant the Google APIs service account the `roles/deploymentmanager.typeViewer` role.

###  Console 

     1. While still in the Google Cloud console, go to the IAM page of the project that contains the types you want to share. 

[Go to the IAM page](https://console.cloud.google.com/iam-admin/iam/)

     2. Select the project from the project list.
     3. Click the **Add** button to add a new member.
     4. In the **Members** box, enter the email address of the service account.
     5. Expand the **Roles** dropdown and select **Other > Deployment Manager Types Viewer (beta)**.
     6. Click **Add** to add the account.

###  gcloud 

With the Google Cloud CLI, add a binding to the IAM policy for the project:
    
    gcloud projects add-iam-policy-binding [PROJECT_ID] \
        --member serviceAccount:[SERVICE_ACCOUNT_EMAIL] --role roles/deploymentmanager.typeViewer

where:

     * `[PROJECT_ID]` is the ID of the project containing images you want to share.
     * `[SERVICE_ACCOUNT_EMAIL]` is the email of the service account in the project you want to share types with.

For example:
    
    gcloud projects add-iam-policy-binding database-images \
        --member serviceAccount:123456789012@cloudservices.gserviceaccount.com  \
        --role roles/deploymentmanager.typeViewer

###  API 

In the API, make a `POST` request to the following URL, where `[PROJECT_ID]` is the ID of the project containing the types you want to share.
    
    POST https://cloudresourcemanager.googleapis.com/v1/projects/$[PROJECT_ID]:setIamPolicy
    

The request body should contain the list of bindings you want to apply to this project. The `roles/deploymentmanager.typeViewer` role should be part of the binding. For example:
    
    {
       "policy": {
           "version": "0",
           "bindings": [
           {
               "role": "roles/owner",
               "members": [
                   "user:example@gmail.com"
               ]
           },
           {
               "role": "roles/deploymentmanager.typeViewer",
               "members": [
                   "serviceAccount:123456789012@cloudservices.gserviceaccount.com"
               ]
           }
           ]
       }
    

}




## Using types from other projects in your configuration

Once you have access to your types, you can specify the type in configurations using the syntax. For [composite types](https://docs.cloud.google.com/deployment-manager/docs/configuration/composite-types/creating-composite-types):
    
    
    type: [PROJECT_ID]/composite:[TYPE]
    

For [type providers](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/process-adding-api):
    
    
    type: [PROJECT_ID]/[TYPE]:[COLLECTION]
    

Where:

  * `[PROJECT_ID]` is the project ID that owns the type.
  * `[TYPE]` is the name of the type provider or the composite type.
  * `[COLLECTION]` is the specific resource you are creating. This is only applicable for base types. For more information on specifying base types, read [Calling a Type Provider in a Configuration](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/calling-type-provider).



For example, if the project ID is `my-type-repository`, then you might provide the following type specification:
    
    
    resources:
    - name: a-special-vm
      type: my-type-repository/composite:autoscaled-igm
      properties:
        ...

## Granting users the ability to list and view types

Granting the project's service account the `deploymentmanager.typeViewer` role allows the project to deploy these types in your configurations but does not allow users to view or list these types. If you want to grant individual users to ability to view types, you must grant the `deploymentmanager.typeViewer` role to each user.

For example, in order for Jane to run the `gcloud beta deployment-manager types list --project another-project` command for a project that doesn't belong to her, the owner of `another-project` must grant Jane the `deploymentmanager.typeViewer` role.

Using the gcloud CLI, you can grant Jane the role like so:
    
    
     gcloud projects add-iam-policy-binding another-project \
            --member user:jane@gmail.com --role deploymentmanager.typeViewer
    

For comprehensive instructions on adding and removing roles from users, read the documentation for [granting, changing, and revoking access to project members](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## What's next?

  * Read about other [IAM roles](https://docs.cloud.google.com/iam/docs/understanding-roles) you can grant.
  * Learn more about [service accounts](https://docs.cloud.google.com/compute/docs/access/service-accounts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
