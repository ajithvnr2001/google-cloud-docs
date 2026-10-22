---
url: https://docs.cloud.google.com/data-fusion/docs/concepts/manage-studio-administration/
title: Manage Studio administration \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:00.963294+00:00
---

# Manage Studio administration  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/concepts/manage-studio-administration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Manage Studio administration Stay organized with collections  Save and categorize content based on your preferences. 

This page explains the administration capabilities that the Cloud Data Fusion Studio provides to manage configurations. Cloud Data Fusion follows a hierarchy, where each instance can have multiple [namespaces](https://docs.cloud.google.com/data-fusion/docs/how-to/control-access-in-namespace). From the Cloud Data Fusion Studio, administrators can centrally manage all namespaces, or manage them individually. Cloud Data Fusion Studio provides the following system and namespace controls. 

## System administration

Clicking **System admin** in the Cloud Data Fusion Studio displays the following tabs:

  * The **Management** tab: view the health status of various Cloud Data Fusion services. You can also view logs for each of the services.
  * The **Configuration** tab: create, view, and edit the following controls:

    * **Namespaces**. For more information, see [Access control with a namespace service account](https://docs.cloud.google.com/data-fusion/docs/how-to/control-access-in-namespace).
    * **System compute profiles**. [Compute profiles](https://docs.cloud.google.com/data-fusion/docs/concepts/overview#concepts) indicate which provisioner to use when creating a cluster for pipeline execution and applying the associated configurations.



_Provisioners_ are responsible for creating, initializing, and destroying the cloud environment that pipelines run in. Each provisioner exposes a set of configurations that are used to control what type of cluster is created and deleted. Different provisioners create different types of clusters.

**Note:** The Managed Service for Apache Spark provisioner is recommended.

Each compute profile has a scope: system or user. You can use a system compute profile for any namespaces under it. User compute profiles exist within a namespace, and only pipelines in that namespace can use the user compute profiles.

On the system administrator **Configurations** tab, you can create a system compute profile that's applied to all the namespaces. Cloud Data Fusion assigns a default compute profile.

When you create a compute profile, you select the provisioner, which the profile uses to create and configure the cloud runtime details.

**Note:** In general, provisioner configurations can be overridden at runtime. For more information, see [Manage compute profiles](https://docs.cloud.google.com/data-fusion/docs/how-to/manage-compute-profiles).

## System preferences

Preferences are predefined configurations that apply at various levels within Cloud Data Fusion, including the system itself, namespaces, applications (which contain pipelines), and individual programs within pipelines. Preferences provide a way to set default values for commonly used configurations. These defaults can be inherited by pipelines and programs at lower levels, reducing repetitive configuration tasks. For more information, see [Manage macros, preferences, and runtime arguments](https://docs.cloud.google.com/data-fusion/docs/how-to/manage-macros-prefs-and-runtime-args).

### HTTP call action

The HTTP call action on the **System admin** page lets you interact with Cloud Data Fusion's own API, or potentially other Google Cloud service APIs, directly from the Cloud Data Fusion Studio interface. However, for building data processing pipelines with external data sources, instead use the HTTP plugin and its HTTP call Executor within your pipelines for a more comprehensive solution. It differs slightly from the HTTP call action, but the underlying concepts are alike.

#### Configurations and use cases

The HTTP call action is primarily used for administrative tasks or configuration purposes within Cloud Data Fusion. It lets you interact with the Cloud Data Fusion API or other Google Cloud services that expose an HTTP API, directly from the Cloud Data Fusion Studio.

##### Configurations

You can define the following details for an HTTP call:

  * **URL** : the target endpoint of the web service you want to call.
  * **Method** : the HTTP method to use, such as `GET`, `POST`, or `PUT`.
  * Optional: **Headers** : any custom headers required for the request.
  * Optional: **Body** : data to be sent in the request body, such as for `POST` and `PUT` calls.



You can then execute the defined HTTP call and view the response from the web service within the Cloud Data Fusion Studio.

##### Use cases

  * **Test Cloud Data Fusion API calls.** You can use the HTTP call action to test or explore Cloud Data Fusion API functionalities directly from the web interface. This action can be helpful for understanding API behavior or troubleshooting potential issues.
  * **Manage namespaces (advanced).** While there's a dedicated UI for namespace management, the HTTP call action can be used for advanced tasks by directly making calls to the Cloud Data Fusion API for namespace creation, deletion, or configuration.
  * **Interacting with other Google Cloud services (limited).** If other Google Cloud services you use have a publicly documented HTTP API, you can use the HTTP call action to interact with those services, though this is an uncommon use case.



##### Important considerations

  * **Security** : be cautious when using the HTTP call action, especially with sensitive data or Cloud Data Fusion API calls that could impact your environment. Be sure that you understand the implications of each API call before executing it.
  * **Limitations** : the HTTP call action is primarily for administrative tasks and testing purposes. It's not designed for building complex data processing pipelines that involve data manipulation within Cloud Data Fusion.
  * **Alternative for pipelines** : for integrating external data sources or services into your data pipelines, use the HTTP plugin and its associated HTTP call executor within your pipeline definitions. This provides a more robust and controlled way to manage HTTP interactions within your data processing workflows.



## Namespace administration

Clicking **Namespace admin** in the Cloud Data Fusion Studio lets you manage the configurations for the specific namespace. For each namespace, you can define the following aspects:

  * **Compute profiles** : the profiles set up in **Namespace admin** are _user_ compute profiles. Only pipelines in that namespace can use these user compute profiles. For more information, see [Manage compute profiles](https://docs.cloud.google.com/data-fusion/docs/how-to/manage-compute-profiles).
  * **Preferences** : preferences defined at namespace level are applicable to the namespace, applications (which contain pipelines), and individual programs within pipelines. For more information, see [Manage macros, preferences, and runtime arguments](https://docs.cloud.google.com/data-fusion/docs/how-to/manage-macros-prefs-and-runtime-args).
  * **Connections** : Cloud Data Fusion lets you reuse connections to sources and sinks in data pipelines. You can add connections in the Namespace Admin page. For more information, see [Create and manage connections](https://docs.cloud.google.com/data-fusion/docs/how-to/managing-connections).
  * **Drivers** : some plugins in Cloud Data Fusion require a JDBC driver to be added to the namespace. For example, before you can run a pipeline with a MySQL batch source plugin, you must add the supported MySQL driver to the namespace. You can upload or remove JDBC drivers to a namespace from the Namespace Admin page, or directly from the Hub. For more information, see [Plugin drivers](https://docs.cloud.google.com/data-fusion/docs/how-to/source-control-management).
  * **Source Control Management** : to efficiently manage the development process of deployed pipelines, Source Control Management lets you connect a namespace with the repository of your source control system. For more information, see [Manage pipelines using Source Control Management](https://docs.cloud.google.com/data-fusion/docs/how-to/source-control-management).
  * **Service account** : to control access to Google Cloud resources, namespaces in Cloud Data Fusion use the [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) by default.



For better data isolation, you can associate a customized Identity and Access Management (IAM) service account (known as a Per Namespace Service Account) with each namespace. The customized IAM service account, which can be different for different namespaces, lets you control access to Google Cloud resources between namespaces for pipeline design-time operations in Cloud Data Fusion, such as pipeline preview, Wrangler, and pipeline validation. For more information, see [Access control with namespace service account](https://docs.cloud.google.com/data-fusion/docs/how-to/control-access-in-namespace).

## What's next

  * Learn more about [compute profiles](https://docs.cloud.google.com/data-fusion/docs/how-to/manage-compute-profiles).
  * Learn more about [macros, preferences, and runtime arguments](https://docs.cloud.google.com/data-fusion/docs/how-to/manage-macros-prefs-and-runtime-args).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
