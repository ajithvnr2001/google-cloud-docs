---
url: https://docs.cloud.google.com/composer/docs/composer-1/access-resources-in-another-project/
title: Access resources in another project \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:30.705115+00:00
---

# Access resources in another project  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-1/access-resources-in-another-project/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 1 Guides ](https://docs.cloud.google.com/composer/docs/composer-1/composer-overview)



Send feedback 

#  Access resources in another project Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/access-resources-in-another-project "View this page for Managed Airflow \(Gen 3\)") | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/access-resources-in-another-project "View this page for Managed Airflow \(Gen 2\)") | **Managed Airflow (Legacy Gen 1)**

This page describes how to access resources that are located in a different Google Cloud project than your Managed Airflow environment.

If you want to use a service account from one project to run environments in another project, see [Using a service account from another project](https://docs.cloud.google.com/composer/docs/composer-1/access-control#cross-project).

We recommend to access resources in other Google Cloud projects in the following way:

  1. In your DAGs, use the default connections that are preconfigured in your environment.

For example, the `google_cloud_default` connection is used by many Google Cloud operators and is automatically configured when you create an environment.

  2. Grant extra IAM permissions and roles to the [service account of your environment](https://docs.cloud.google.com/composer/docs/composer-1/access-control#service-account), so that it can access resources in a different project.




## Determine the service account of your environment

To determine the service account of your environment:

###  Console 

  1. In Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **Environment configuration** tab.

  4. The service account of your environment is listed in the **Service account** field.

The value is an email address, such as `service-account-name@example-project.iam.gserviceaccount.com`.




###  gcloud 
    
    
    gcloud composer environments describe ENVIRONMENT_NAME \
        --location LOCATION \
        --format="get(config.nodeConfig.serviceAccount)"
    

The value is an email address, such as `service-account-name@example-project.iam.gserviceaccount.com`.

## Grant IAM roles and permissions to access resources in another project

The service account of your environment requires permissions to access resources in another project. These roles and permissions can be different based on the resource that you want to access.

### Access a specific resource

We recommend to grant roles and permissions for specific resources, such as a single Cloud Storage bucket located in a different project. In this approach, you use resource-based access with conditional role bindings.

To access a specific resource:

  1. Follow the [Configure resource-based access](https://docs.cloud.google.com/iam/docs/configuring-resource-based-access) guide.
  2. When granting roles and permissions, specify the service account of your environment as a principal.



### Access a resource type

As an alternative, you can grant roles and permissions based on the resource type, such as all Cloud Storage buckets located in a different project.

To access a resource type:

  1. Follow the [Manage access to other resources](https://docs.cloud.google.com/iam/docs/manage-access-other-resources) guide.
  2. When granting roles and permissions, specify the service account of your environment as a principal.



After you grant the required permissions and roles, you can access resources in a different project with the same default Airflow connections that you use to access resources in the project where your environment is located.

## What's next

  * [Access control with IAM](https://docs.cloud.google.com/composer/docs/composer-1/access-control)
  * [Manage Airflow connections](https://docs.cloud.google.com/composer/docs/composer-1/manage-airflow-connections)
  * [Configure resource location restrictions](https://docs.cloud.google.com/composer/docs/composer-1/configure-resource-location-restrictions)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
