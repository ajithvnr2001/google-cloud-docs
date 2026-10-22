---
url: https://docs.cloud.google.com/app-hub/docs/modify-app-hub-resources/
title: Manage services and workloads \u00a0|\u00a0 App Hub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:13.181130+00:00
---

# Manage services and workloads  |  App Hub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-hub/docs/modify-app-hub-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ App Hub ](https://docs.cloud.google.com/app-hub/docs)
  * [ Guides ](https://docs.cloud.google.com/app-hub/docs/overview)



Send feedback 

#  Manage services and workloads Stay organized with collections  Save and categorize content based on your preferences. 

When you [choose your application setup model](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub), you define an [application management boundary](https://docs.cloud.google.com/app-hub/docs/key-concepts#app-mgmt-boundary) for your App Hub applications in a [management project](https://docs.cloud.google.com/app-hub/docs/key-concepts#mgmt-project). You can then register services and workloads in applications inside this boundary. For recommended use cases to introduce application management practices, see [Prepare for application lifecycle management](https://docs.cloud.google.com/app-hub/docs/prepare-for-app-lifecycle-management).

To avoid configuration drift and maintain a clear source of truth, we recommend that you manage your application components in the environment where they were originally defined:

  * **For applications deployed from an Application Design Center template** : Use Application Design Center to manage and update the application. You can either [revise the template](https://docs.cloud.google.com/application-design-center/docs/design-application-templates#revise_and_reshare_your_template) for application design changes or [create an application revision](https://docs.cloud.google.com/application-design-center/docs/manage-applications#create-application-revision) to update settings such as application and component details.

[Go to Application Design Center](https://console.cloud.google.com/products/design-center/overview)

  * **For applications created by registering existing resources in App Hub** : Manage applications, services, and workloads directly within App Hub.

[Go to App Hub](https://console.cloud.google.com/apphub/applications)




This page describes how to manage services and workloads that are discovered or registered directly within App Hub. You can perform these actions using either the Google Cloud console or the Google Cloud CLI. For applications deployed from a [template](https://docs.cloud.google.com/app-hub/docs/key-concepts#template), see [Application Design Center](https://docs.cloud.google.com/application-design-center/docs/overview) documentation.

## Before you begin

This document assumes you have an application with [supported resources registered to it](https://docs.cloud.google.com/app-hub/docs/register-resources).

### Required roles

To get the permissions that you need to manage services and workloads in App Hub, ask your administrator to grant you the following IAM roles on the management project that defines your application management boundary : 

  * Update and unregister services and workloads: [App Hub Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/apphub#apphub.editor) (`roles/apphub.editor`) 
  * View services, workloads, and their details: [App Hub Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/apphub#apphub.viewer) (`roles/apphub.viewer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about App Hub roles, see [App Hub IAM roles and permissions](https://docs.cloud.google.com/app-hub/docs/roles-permissions).

## View details of services and workloads

Follow these steps to view details of services and workloads within your application management boundary, including the following:

  * [Location](https://docs.cloud.google.com/app-hub/docs/locations)
  * [Registration status to an application](https://docs.cloud.google.com/app-hub/docs/overview#registration-status)
  * [Properties and attributes](https://docs.cloud.google.com/app-hub/docs/overview#properties-and-attributes)



For more information about these details, see [App Hub concepts and data model](https://docs.cloud.google.com/app-hub/docs/overview#data-model).

###  Console 

View details from services and workloads of an application with a registration status value of _registered_ or _detached_ :

  1. In the Google Cloud console, use the project picker to select your management project.

  2. Navigate to the **Applications** page from App Hub:

[Go to Applications](https://console.cloud.google.com/apphub/applications)

The page displays a list of your applications.

  3. Click the name of the application from which you want to view service or workload details.

  4. In the **Services and workloads** tab, click the name of the service or workload you want to view.

  5. In the **Details** page of the component, you can look at information such as the display name, location, registration status, properties, and attributes.




Alternatively, view a list of all services and workloads with a registration status value of _discovered_ or _registered_ :

  1. Navigate to the **Services and workloads** page from App Hub:

[Go to Services and workloads](https://console.cloud.google.com/apphub/explore)

The page displays a list of all discovered and registered services and workloads.

  2. Use the **Filter** field to narrow the results by properties, attributes, or status, using values like **Environment** , **Owners** , or **Registration status**.




###  gcloud 

View details from services and workloads of an application with a registration status value of _registered_ or _detached_ :

  1. [Find the project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your management project.

  2. Describe a service or workload from an application to review its details, including properties and attributes:

     * Describe a service:
           
           gcloud apphub applications services describe SERVICE \
               --project=PROJECT_ID \
               --application=APPLICATION \
               --location=LOCATION
           

Replace the following:

       * `SERVICE`: the ID of the service.
       * `PROJECT_ID`: the ID of your management project.
       * `APPLICATION`: the ID of the application to which the service is registered.
       * `LOCATION`: the location of the service. Use `global` for global resources or a specific region, such as `us-east1`, for regional resources.
     * Describe a workload:
           
           gcloud apphub applications workloads describe WORKLOAD \
               --project=PROJECT_ID \
               --application=APPLICATION \
               --location=LOCATION
           

Replace the following:

       * `WORKLOAD`: the ID of the workload.
       * `PROJECT_ID`: the ID of your management project.
       * `APPLICATION`: the ID of the application to which the workload is registered.
       * `LOCATION`: the location of the workload. Use `global` for global resources or a specific region, such as `us-east1`, for regional resources.



The output displays details from the component, such as the display name, location, and registration status. It also includes [properties and attributes](https://docs.cloud.google.com/app-hub/docs/overview#properties-and-attributes), if they are present on the resource.

Alternatively, view a list of all services and workloads with a registration status value of _discovered_ or _registered_ :

###  Discovered 

Discovered Google Cloud resources within your application management boundary are available to be registered as services or workloads in an application. Follow these steps to list discovered resources:

  1. List discovered services:
         
         gcloud apphub discovered-services list \
             --project=PROJECT_ID \
             --location=LOCATION
         

Replace the following:

     * `PROJECT_ID`: the ID of your management project.
     * `LOCATION`: the location where you want to discover resources. Use `global` for global resources or a specific region, such as `us-east1`, for regional resources.
  2. List discovered workloads:
         
         gcloud apphub discovered-workloads list \
             --project=PROJECT_ID \
             --location=LOCATION
         




###  Registered 

Registered services and workloads are part of an application. Follow these steps to list registered components of a particular application. You can filter the list based on attributes, using the [`--filter` flag](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters):

  1. List registered services in an application:
         
         gcloud apphub applications services list \
             --application=APPLICATION_NAME \
             --project=PROJECT_ID \
             --location=LOCATION \
             --filter=FILTER_EXPRESSION
         

Replace the following:

     * `APPLICATION_NAME`: the name of your application. You specify this value when you [create an application](https://docs.cloud.google.com/app-hub/docs/register-resources#create-an-application).
     * `PROJECT_ID`: the ID of your management project.
     * `LOCATION`: the component location. Use `global` for global components or a specific region, such as `us-east1`, for regional components.
     * Optional: `FILTER_EXPRESSION`: the filter expression to specify attributes. For example, to list components with a `PRODUCTION` environment type, use `attributes.environment.type=PRODUCTION`.
  2. List registered workloads in an application:
         
         gcloud apphub applications workloads list \
             --application=APPLICATION_NAME \
             --project=PROJECT_ID \
             --location=LOCATION \
             --filter=FILTER_EXPRESSION
         




The registration status of services and workloads in an application might change to _detached_ if you move a project or folder out of your application management boundary or delete the underlying resource. Detached services and workloads remain in the application until you unregister them, but App Hub can no longer manage or monitor them. For more information, see [Registration status of services and workloads](https://docs.cloud.google.com/app-hub/docs/overview#registration-status).

To reattach services or workloads to an application, you must [register](https://docs.cloud.google.com/app-hub/docs/register-resources#register-services-and-workloads) them again.

## View extended metadata schemas

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

App Hub enriches your services and workloads with metadata to improve discoverability, governance, and integration with other systems. You can search for the available metadata schemas and view their definitions using the App Hub API.

Follow these steps to view the schema definition of the extended metadata property, listing all available schemas or getting the details of a specific schema if available.

For more information about the extended metadata property, see [Properties and attributes](https://docs.cloud.google.com/app-hub/docs/overview#properties-and-attributes). For a list of the supported metadata types and their schemas, see [Extended metadata schemas](https://docs.cloud.google.com/app-hub/docs/metadata-schemas).

###  gcloud 

  * List all available extended metadata schemas in a project and location:
        
        gcloud alpha apphub extended-metadata-schemas list \
            --project=PROJECT_ID \
            --location=LOCATION \
        

Replace the following:

    * `PROJECT_ID`: the ID of your management project.
    * `LOCATION`: the component location. Use `global` for global components or a specific region, such as `us-east1`, for regional components.
  * View the details of a specific schema:
        
        gcloud alpha apphub extended-metadata-schemas describe SCHEMA_NAME \
            --project=PROJECT_ID \
            --location=LOCATION \
        

Replace `SCHEMA_NAME` with the full name of the schema, for example, `apphub.googleapis.com/AgentProperties`.




###  Terraform 

You can use a data source in Terraform to retrieve the details of a specific schema. The following example lets you view the details of the `apphub.googleapis.com/AgentProperties` schema for a workload with the `AGENT` functional type in the `my-project-id` project at the `us-central1` location.
    
    
    data "google_apphub_extended_metadata_schema" "agent_properties" {
      project  = "my-project-id"
      location = "us-central1"
      name     = "apphub.googleapis.com/AgentProperties"
    }
    

## Update service and workload attributes

To modify the [attributes](https://docs.cloud.google.com/app-hub/docs/overview#properties-and-attributes) of services and workloads that are registered in an application, follow these steps:

**Note:** You cannot modify attributes for [shared services](https://docs.cloud.google.com/app-hub/docs/key-concepts#service).

###  Console 

  1. In the Google Cloud console, use the project picker to select your management project.

  2. Navigate to the **Applications** page from App Hub:

[Go to Applications](https://console.cloud.google.com/apphub/applications)

The page displays a list of your applications.

  3. Click the name the application for which you want to update service or workload attributes.

  4. In the **Services and workloads** tab, find the name of the service or workload you want to update.

  5. Click more_vert **More** , then click edit **Edit service** or edit **Edit workload**.

  6. In the pane that opens, edit the fields as required and click **Save**.




###  gcloud 

  1. [Find the project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your management project.

  2. Update service or workload attributes:

     * Update service attributes:
           
           gcloud apphub applications services update SERVICE_NAME \
               --application=APPLICATION_NAME \
               --project=PROJECT_ID \
               --location=LOCATION \
               --display-name=DISPLAY_NAME \
               --criticality-type=CRITICALITY_LEVEL \
               --environment-type=ENVIRONMENT \
               --developer-owners=display-name=DEV_NAME,email=DEV_EMAIL \
               --operator-owners=display-name=OPERATOR_NAME,email=OPERATOR_EMAIL \
               --business-owners=display-name=BUSINESS_NAME,email=BUSINESS_EMAIL
           

Replace `SERVICE_NAME` with the name of the service you want to update.

     * Update workload attributes:
           
           gcloud apphub applications workloads update WORKLOAD_NAME \
               --application=APPLICATION_NAME \
               --project=PROJECT_ID \
               --location=LOCATION \
               --display-name=DISPLAY_NAME \
               --criticality-type=CRITICALITY_LEVEL \
               --environment-type=ENVIRONMENT \
               --developer-owners=display-name=DEV_NAME,email=DEV_EMAIL \
               --operator-owners=display-name=OPERATOR_NAME,email=OPERATOR_EMAIL \
               --business-owners=display-name=BUSINESS_NAME,email=BUSINESS_EMAIL
           

Replace `WORKLOAD_NAME` with the name of the workload you want to update.

Replace the following required and optional flags:

       * Required: `APPLICATION_NAME`: the name of your application. You specify this value when you [create an application](https://docs.cloud.google.com/app-hub/docs/register-resources#create-an-application).
       * Required: `PROJECT_ID`: the ID of your management project.
       * Required: `LOCATION`: your component location. Use `global` for global components or a specific region, such as `us-east1`, for regional components.
       * Optional: `DISPLAY_NAME`: the display name of your component.
       * Optional: `CRITICALITY_LEVEL`: the importance level of the component. Use one of the following values:

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

To update service or workload attributes with Terraform, modify the arguments within the corresponding [`google_apphub_service`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/apphub_service) or [`google_apphub_workload`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/apphub_workload) resource block in your configuration file. When you apply the changes, Terraform updates the resource to match the new configuration.

The following examples update the criticality and environment attributes of services and workloads of a regional application:

  * Update service attributes:
        
        resource "google_apphub_service" "example" {
            # ... other arguments
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
        

  * Update workload attributes:
        
        resource "google_apphub_workload" "example" {
            # ... other arguments
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
        




## Unregister services and workloads

Unregistering a service or workload removes it from an application. The underlying resource is not deleted. If it is still within your application management boundary, it becomes a resource with a registration status value of _discovered_ , available for registration to another application.

Follow these steps to unregister services and workloads:

###  Console 

  1. In the Google Cloud console, use the project picker to select your management project.

  2. Navigate to the **Applications** page from App Hub:

[Go to Applications](https://console.cloud.google.com/apphub/applications)

The page displays a list of your applications.

  3. Click the name the application from which you want to unregister services or workloads.

  4. In the **Services and workloads** tab, click the name of the service or workload you want to unregister.

  5. In the details page of the component, click **Unregister**.




###  gcloud 

  1. [Find the project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your management project.

  2. Unregister a service or a workload:

     * Unregister a service:
           
           gcloud apphub applications services delete SERVICE_NAME \
               --application=APPLICATION_NAME \
               --project=PROJECT_ID \
               --location=LOCATION
           

Replace the following:

       * `SERVICE_NAME`: the name of the service you want to unregister.
       * `APPLICATION_NAME`: the name of your application. You specify this value when you [create an application](https://docs.cloud.google.com/app-hub/docs/register-resources#create-an-application).
       * `PROJECT_ID`: the ID of your management project.
       * `LOCATION`: the component location. Use `global` for global components or a specific region, such as `us-east1`, for regional components.
     * Unregister a workload:
           
           gcloud apphub applications workloads delete WORKLOAD_NAME \
               --application=APPLICATION_NAME \
               --project=PROJECT_ID \
               --location=LOCATION
           

Replace `WORKLOAD_NAME` with the name of the workload you want to unregister.




###  Terraform 

To unregister a service or workload managed by Terraform, remove the corresponding [`google_apphub_service`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/apphub_service) or [`google_apphub_workload`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/apphub_workload) resource block from your configuration file and run `terraform apply`. When you apply the changes, Terraform removes the registration from App Hub.

After unregistering all services and workloads, you can [delete the application](https://docs.cloud.google.com/app-hub/docs/manage-applications#delete).

## What's next

  * [Manage your applications](https://docs.cloud.google.com/app-hub/docs/manage-applications)
  * [Optimize an application with design recommendations](https://docs.cloud.google.com/app-hub/docs/optimize-applications)
  * [Monitor your applications](https://docs.cloud.google.com/app-hub/docs/monitor-applications)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
