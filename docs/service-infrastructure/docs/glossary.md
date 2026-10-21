---
url: https://docs.cloud.google.com/service-infrastructure/docs/glossary/
title: Glossary \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:40:33.027468+00:00
---

# Glossary  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/glossary/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure/docs)
  * [ Guides ](https://docs.cloud.google.com/service-infrastructure/docs/how-to)



Send feedback 

#  Glossary Stay organized with collections  Save and categorize content based on your preferences. 

#### Enabled service

  * Before a user can use a managed service, it must first be enabled for a service consumer project. Enabling a managed service for a service consumer project allows a user to use it, adds monitoring pages in the Google Cloud console, and enables billing for the service if billing is enabled for the project.



#### Managed service

  * A managed service offers access to a service through a well-defined interface, such as an API. Users access the managed service without having to manage the underlying resources, such as compute and storage, that implement the service.

For example, you can build a data storage service using Compute Engine and Cloud SQL and offer it to your users as an API. Your users interact with that API only. They don’t know or care how you implemented the managed service. A managed service is also referred to as a service.




#### Operation

  * Service Infrastructure uses the generic concept of an operation to represent the activities of a managed service, such as API calls and resource usage. Each operation is associated with a managed service and a specific service consumer, and has a set of properties that describe the operation, such as the API method name and resource usage amount.

**Note:** Service Infrastructure APIs use a separate resource to represent a long-running operation that is the result of a network API call. To learn more, see [Polling Long Running Operations](https://docs.cloud.google.com/service-infrastructure/docs/polling-operations).



#### Private service

  * Private services can only be enabled by users and members of groups with which the service has been explicitly shared, such as APIs created using [Cloud Endpoints](https://docs.cloud.google.com/endpoints).

A private service is not related to connectivity through public or private (RFC 1918) IP addresses.




#### Public service

  * Public APIs and services are globally visible to all users. Examples of public Google Cloud APIs and services include [BigQuery API](https://docs.cloud.google.com/bigquery), [Cloud Storage](https://docs.cloud.google.com/storage), and [Cloud Monitoring API](https://docs.cloud.google.com/monitoring). For a complete list of public APIs, see [Cloud APIs](https://docs.cloud.google.com/apis).

A public service is not related to connectivity through public or private (RFC 1918) IP addresses.




#### Service configurations

  * Each managed service is described by a service configuration which covers a wide range of features, including its name, title, RPC API definitions, REST API definitions, documentation, authentication, and more.

To change the configuration of a managed service, you need to publish an updated service configuration. To learn more, see [Managing Service Configurations](https://docs.cloud.google.com/service-infrastructure/docs/manage-config).

The Service Management API also allows publishing an [OpenAPI](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md) specification, formerly known as the Swagger Specification, which is automatically converted to a corresponding service configuration.




#### Service consumer

  * An agent (such as a user or group of users) who owns a Google Cloud project that has enabled and can therefore use APIs on a managed service. A managed service can have many service consumers.



#### Service Consumer Management API

  * Service Consumer Management provides utilities to help you manage your relationship with your managed services' users, including the ability to create and manage tenancy units and override quota limits.



#### Service Control API

  * The Service Control API works with a set of managed services and their operations, and checks whether an operation is allowed to proceed, and reports completed operations. To learn more, see [Service Infrastructure Overview](https://docs.cloud.google.com/service-infrastructure/docs/overview).



#### Service Management API

  * The Service Management API manages the creation and life cycle of managed services and service configurations. Use the Service Management API to rollout, publish, and update your managed services on Google Cloud so that your users can find, enable, and use them.



#### Service producer

  * An agent (such as a user or group of users) who owns a Google Cloud project responsible for publishing and maintaining a managed service. Each managed service is owned by exactly one service producer.



#### Service rollout

  * A service rollout defines how the Service Management API should deploy service configurations to Google Cloud Platform and how the configurations take effect. It lets you specify multiple service configuration versions to be deployed together and a strategy that indicates how they should be used.

The Service Management API keeps a history of service rollouts so that you can roll back to previous service configuration versions. You can roll back a service configuration by initiating a new rollout that clones a previously submitted rollout record.




#### Service Usage API

  * Provides methods for you and users of your managed services to list, enable, and disable APIs, and view and manage quota limits, in Google Cloud projects.



#### Tenant project

  * A tenant project is a Google-owned Google Cloud project used to host the resources of a managed service dedicated to a single service consumer. This approach creates an isolated environment for each consumer. A tenancy unit can contain multiple tenant projects.



#### Tenancy units

  * Tenancy units provide per-service, per-service consumer isolated environments used for deploying managed services. When a new user starts using your service, you can create all resources specific to that service consumer in a single tenancy unit. Creating a separate tenancy unit per service consumer helps ensure your user's data is isolated, and if a user stops using your service, deleting the tenancy unit helps ensure the user's data is deleted. To learn more about tenancy units, see [Getting Started with Tenancy Units](https://docs.cloud.google.com/service-infrastructure/docs/tenancy-units-tutorial).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
