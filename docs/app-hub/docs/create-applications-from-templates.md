---
url: https://docs.cloud.google.com/app-hub/docs/create-applications-from-templates/
title: Create applications from published templates \u00a0|\u00a0 App Hub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:02.010104+00:00
---

# Create applications from published templates  |  App Hub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-hub/docs/create-applications-from-templates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ App Hub ](https://docs.cloud.google.com/app-hub/docs)
  * [ Guides ](https://docs.cloud.google.com/app-hub/docs/overview)



Send feedback 

#  Create applications from published templates Stay organized with collections  Save and categorize content based on your preferences. 

Deploying new App Hub applications from [templates](https://docs.cloud.google.com/app-hub/docs/key-concepts#template) helps you achieve the following:

  * Visualize the design as infrastructure code.
  * Quickly access templates for your deployments.
  * Comply with organizational best practices.
  * Gain visibility into application components, health, and operational status.



This guide shows you how to deploy applications using a standardized template with [Application Design Center](https://docs.cloud.google.com/application-design-center/docs/overview). This option is ideal for new infrastructure scenarios where no services or workloads for the application exist yet.

## Before you begin

You must complete the following steps before using templates to create applications:

  * **For administrators** :

    1. [Choose your application setup model](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub). Application Design Center requires a [management project](https://docs.cloud.google.com/app-hub/docs/key-concepts#mgmt-project).
    2. Enable required APIs for all Google Cloud resources you intend to use.
    3. [Set up Application Design Center](https://docs.cloud.google.com/application-design-center/docs/setup). You must configure Application Design Center to let users deploy new application components from templates.
    4. [Design](https://docs.cloud.google.com/application-design-center/docs/design-application-templates) and [publish](https://docs.cloud.google.com/application-design-center/docs/manage-catalogs#publish_an_application_template_to_a_catalog) an application template to a [catalog](https://docs.cloud.google.com/app-hub/docs/key-concepts#catalog). You can also use [pre-built Google templates](https://docs.cloud.google.com/application-design-center/docs/build-on-google-templates).
    5. [Grant access to users](https://docs.cloud.google.com/resource-manager/docs/manage-applications#assign-roles). Assign appropriate IAM roles based on user's responsibilities in the application lifecycle.
  * **For developers and operators** :

    1. Confirm with your administrator that the initial setup and template publication is finalized.
    2. [Make sure you have the necessary IAM roles](https://docs.cloud.google.com/resource-manager/docs/manage-applications#assign-roles) for the tasks you want to perform.
    3. Open your [management project](https://docs.cloud.google.com/app-hub/docs/key-concepts#mgmt-project) in the Google Cloud console.



## Configure and deploy the application

[Application Design Center](https://docs.cloud.google.com/application-design-center/docs/overview) lets you create a template, configure its parameters, and deploy application components based on it. Follow these steps to create and access a template from a catalog and deploy the application:

  1. In the Google Cloud console, navigate to the **Templates** page from Application Design Center to see the list of available application templates:

[Go to Templates](https://console.cloud.google.com/products/design-center/templates)

  2. Select the template for the application you want to deploy and review its details.

  3. [Create an application draft](https://docs.cloud.google.com/application-design-center/docs/manage-applications#create_an_application_draft) from the template, providing values for any required input parameters, such as the application name and deployment region.

  4. [Deploy your application](https://docs.cloud.google.com/application-design-center/docs/deploy-from-console) from the template.




The deployment process in Application Design Center automatically registers the application and its components in App Hub, where you can view application details, services, and workloads.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
