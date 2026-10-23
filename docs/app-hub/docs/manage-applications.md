---
url: https://docs.cloud.google.com/app-hub/docs/manage-applications/
title: Manage App Hub applications \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:15:08.965125+00:00
---

# Manage App Hub applications  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-hub/docs/manage-applications/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ App Hub ](https://docs.cloud.google.com/app-hub/docs)
  * [ Guides ](https://docs.cloud.google.com/app-hub/docs/overview)



Send feedback 

#  Manage App Hub applications Stay organized with collections  Save and categorize content based on your preferences. 

When you [choose your application setup model](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub), you define an [application management boundary](https://docs.cloud.google.com/app-hub/docs/key-concepts#app-mgmt-boundary) for your App Hub applications in a [management project](https://docs.cloud.google.com/app-hub/docs/key-concepts#mgmt-project). You can then register services and workloads in applications inside this boundary.

For recommended use cases to introduce application management practices, see [Prepare for application management](https://docs.cloud.google.com/app-hub/docs/prepare-for-app-lifecycle-management). To create an application and register resources, see [Register existing resources to an application](https://docs.cloud.google.com/app-hub/docs/register-resources).

To avoid configuration drift and maintain a clear source of truth, we recommend that you manage your application components in the environment where they were originally defined:

  * **For applications deployed from an Application Design Center template** : Use Application Design Center to manage and update the application. You can either [revise the template](https://docs.cloud.google.com/application-design-center/docs/design-application-templates#revise_and_reshare_your_template) for application design changes or [create an application revision](https://docs.cloud.google.com/application-design-center/docs/manage-applications#create-application-revision) to update settings such as application and component details.

[Go to Application Design Center](https://console.cloud.google.com/products/design-center/overview)

  * **For applications created by registering existing resources in App Hub** : Manage applications, services, and workloads directly within App Hub.

[Go to App Hub](https://console.cloud.google.com/apphub/applications)




This page describes how to manage applications that were registered directly within App Hub. You can perform these actions using either the Google Cloud console or the Google Cloud CLI. For applications deployed from a [template](https://docs.cloud.google.com/app-hub/docs/key-concepts#template), see [Application Design Center](https://docs.cloud.google.com/application-design-center/docs/overview) documentation.

## Before you begin

This document assumes you have an application with [supported resources registered to it](https://docs.cloud.google.com/app-hub/docs/register-resources).

### Required roles

To get the permissions that you need to manage applications in App Hub, ask your administrator to grant you the following IAM roles on the management project that defines your application management boundary : 

  * Update and delete applications: [App Hub Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/apphub#apphub.editor) (`roles/apphub.editor`) 
  * View applications: [App Hub Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/apphub#apphub.viewer) (`roles/apphub.viewer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about App Hub roles, see [App Hub IAM roles and permissions](https://docs.cloud.google.com/app-hub/docs/roles-permissions).

## List applications

Follow these steps to list and filter all the applications within your application management boundary:

###  Console 

  1. In the Google Cloud console, use the project picker to select your management project.

  2. Navigate to the **Applications** page from App Hub:

[Go to Applications](https://console.cloud.google.com/apphub/applications)

The page displays a list of your applications.

  3. To filter the list, use the **Filter** field. You can filter by attributes such as **Criticality** or **Environment**.




###  gcloud 

  1. [Find the project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your management project.

  2. Display a list of your applications using one of the following options:

     * List all applications:
           
           gcloud apphub applications list \
               --project=PROJECT_ID \
               --location=LOCATION
           

Replace the following:

       * `PROJECT_ID`: the ID of your management project.
       * `LOCATION`: the location of your applications. Use `global` for global applications or a specific region, such as `us-east1`, for regional applications.
     * Filter the list of applications based on attributes, using the [`--filter` flag](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters):
           
           gcloud apphub applications list \
               --project=PROJECT_ID \
               --location=LOCATION \
               --filter=FILTER_EXPRESSION \
           

Replace the following:

       * `PROJECT_ID`: the ID of your management project.
       * `LOCATION`: the location of your applications. Use `global` for global applications or a specific region, such as `us-east1`, for regional applications.
       * `FILTER_EXPRESSION`: the filter expression to specify attributes. For example, to list all applications with a `PRODUCTION` environment type, use `attributes.environment.type=PRODUCTION`.



## View application details

Follow these steps to view the detailed information of a specific application, including its attributes and metadata:

###  Console 

  1. In the Google Cloud console, use the project picker to select your management project.

  2. Navigate to the **Applications** page from App Hub:

[Go to Applications](https://console.cloud.google.com/apphub/applications)

The page displays a list of your applications.

  3. Click the name of the application you want to view.

The application's **Details** tab is displayed.




###  gcloud 

  1. [Find the project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your management project.

  2. Describe an application:
         
         gcloud apphub applications describe APPLICATION_NAME \
             --project=PROJECT_ID \
             --location=LOCATION
         

Replace the following:

     * `APPLICATION_NAME`: the name of your application. You specify this value when you [create an application](https://docs.cloud.google.com/app-hub/docs/register-resources#create-an-application).
     * `PROJECT_ID`: the ID of your management project.
     * `LOCATION`: the location of your application. Use `global` for global applications or a specific region, such as `us-east1`, for regional applications.



## Update application attributes

To modify the [attributes](https://docs.cloud.google.com/app-hub/docs/overview#properties-and-attributes) of an application after it has been created, follow these steps. Services and workloads can also use the same application attributes during [registration](https://docs.cloud.google.com/app-hub/docs/register-resources).

###  Console 

  1. In the Google Cloud console, use the project picker to select your management project.

  2. Navigate to the **Applications** page from App Hub:

[Go to Applications](https://console.cloud.google.com/apphub/applications)

The page displays a list of your applications.

  3. For the application you want to update, click edit **Edit**.

  4. In the **Edit application** pane, modify the fields as needed.

  5. Click **Save**.




###  gcloud 

  1. [Find the project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your management project.

  2. Update application attributes. You can update any of the mutable attributes, such as `display-name`, `criticality-type`, `environment-type`, and owners:
         
         gcloud apphub applications update APPLICATION_NAME \
             --project=PROJECT_ID \
             --location=LOCATION \
             --display-name=DISPLAY_NAME \
             --criticality-type=CRITICALITY_LEVEL \
             --environment-type=ENVIRONMENT \
             --developer-owners=display-name=DEV_NAME,email=DEV_EMAIL \
             --operator-owners=display-name=OPERATOR_NAME,email=OPERATOR_EMAIL \
             --business-owners=display-name=BUSINESS_NAME,email=BUSINESS_EMAIL
         

Replace the following:

     * Required: `APPLICATION_NAME`: the name of your application. You specify this value when you [create an application](https://docs.cloud.google.com/app-hub/docs/register-resources#create-an-application).
     * Required: `PROJECT_ID`: the ID of your management project.
     * Required: `LOCATION`: the location of your application. Use `global` for global applications or a specific region, such as `us-east1`, for regional applications.
     * Optional: `DISPLAY_NAME`: the display name of your application.
     * Optional: `CRITICALITY_LEVEL`: the importance level of the application. Use one of the following values:

       * `MISSION_CRITICAL`
       * `HIGH`
       * `MEDIUM`
       * `LOW`
     * Optional: `ENVIRONMENT`: the stage of the software lifecycle. Use one of the following values:

       * `PRODUCTION`
       * `STAGING`
       * `DEVELOPMENT`
       * `TEST`
     * Optional: `DEV_NAME` and `DEV_EMAIL`: the display name and email address of the developer owner, respectively.

     * Optional: `OPERATOR_NAME` and `OPERATOR_EMAIL`: the display name and email address of the operator owner, respectively.

     * Optional: `BUSINESS_NAME` and `BUSINESS_EMAIL`: the display name and email address of the business owner, respectively.

**Note:** Email addresses must have the format `username@yourdomain`, for example, `jane-doe@gmail.com`.



###  Terraform 

To update application attributes with Terraform, modify the arguments within [the `google_apphub_application` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/apphub_application) block in your configuration file. When you apply the changes, Terraform updates the application to match the new configuration.

The following example updates the criticality and environment attributes of a regional application in `us-central1`:
    
    
    resource "google_apphub_application" "example" {
        project        = "my-project-id"
        location       = "us-central1"
        application_id = "my-application"
        display_name   = "My Application"
        description    = "This application represents our platform."
        attributes {
            criticality {
                type = "HIGH" # Updated criticality
            }
            environment {
                type = "PRODUCTION"
            }
            # ... other attributes
        }
    }
    

## Delete an application

Before you can delete an application, you must first [unregister all of its services and workloads](https://docs.cloud.google.com/app-hub/docs/modify-app-hub-resources#unregister). Then, follow these steps to delete the application:

###  Console 

  1. In the Google Cloud console, use the project picker to select your management project.

  2. Navigate to the **Applications** page from App Hub:

[Go to Applications](https://console.cloud.google.com/apphub/applications)

The page displays a list of your applications.

  3. Click the name of the application you want to delete.

  4. Go to the **Services and workloads** tab and make sure you have unregistered all the application components. For more information, see [Unregister services and workloads](https://docs.cloud.google.com/app-hub/docs/modify-app-hub-resources#unregister).

  5. After all services and workloads are unregistered, navigate back to the application details and click **Delete**.




###  gcloud 

  1. [Find the project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your management project.

  2. Make sure you have unregistered all the application components. For more information, see [Unregister services and workloads](https://docs.cloud.google.com/app-hub/docs/modify-app-hub-resources#unregister).

  3. After the application has no registered components, delete it:
         
         gcloud apphub applications delete APPLICATION_NAME \
             --project=PROJECT_ID \
             --location=LOCATION
         

Replace the following:

     * `APPLICATION_NAME`: the name of your application. You specify this value when you [create an application](https://docs.cloud.google.com/app-hub/docs/register-resources#create-an-application).
     * `PROJECT_ID`: the ID of your management project.
     * `LOCATION`: the location of your application. Use `global` for global applications or a specific region, such as `us-east1`, for regional applications.



###  Terraform 

To delete an application that is managed by Terraform, you have the following options:

  * **Remove the resource from your configuration** : Delete [the `google_apphub_application` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/apphub_application) block from your Terraform file and then run `terraform apply`. Terraform recognizes that the resource is no longer in the configuration and deletes it from your project.
  * **Terminate all resources** : Run the `terraform destroy` command to terminate all resources managed by your Terraform configuration, including the application.



## What's next

  * [Manage services and workloads](https://docs.cloud.google.com/app-hub/docs/modify-app-hub-resources)
  * [Optimize an application with design recommendations](https://docs.cloud.google.com/app-hub/docs/optimize-applications)
  * [Monitor your applications](https://docs.cloud.google.com/app-hub/docs/monitor-applications)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
