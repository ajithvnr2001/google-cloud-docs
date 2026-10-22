---
url: https://docs.cloud.google.com/apigee/docs/apihub/auto-register-apis/
title: Auto-register APIs from Google Cloud projects \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:31:45.546854+00:00
---

# Auto-register APIs from Google Cloud projects  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/auto-register-apis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Auto-register APIs from Google Cloud projects Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

This page describes how to automatically register APIs from Google Cloud projects to API hub. This auto-registration process enables API hub to register API resources from multiple Google Cloud services, ensuring that all your APIs are captured in the central repository and that your API data remains synchronized with your API deployments. 

## How auto-registration works

The operation to automatically register APIs from Google Cloud projects to API hub is triggered when you attach a runtime project to API hub. Attaching a runtime project establishes a [project association](https://docs.cloud.google.com/apigee/docs/apihub/manage-project-associations) between the Google Cloud project and API hub. During this process, API hub automatically discovers deployed APIs within the project and creates the necessary [plugin instances](https://docs.cloud.google.com/apigee/docs/apihub/plugins) in API hub to manage data ingestion. 

## Supported Google Cloud services

Auto-registration is currently supported for the following Google Cloud services: 

Google Cloud service | Ingested data  
---|---  
[Apigee and Apigee hybrid](https://docs.cloud.google.com/apigee/docs/apigee-x/overview) | Deployed API proxies and their associated OpenAPI specifications  
[API Gateway](https://docs.cloud.google.com/api-gateway/docs/about-api-gateway) | Gateway definitions and managed endpoints  
  
### Project associations and plugins 

**Deprecated:** [Pull-based](https://docs.cloud.google.com/apigee/docs/apihub/plugins#plugin-data-ingestion-methods) ingestion is no longer supported for Apigee and Apigee hybrid plugins as of **July 31, 2025**. For existing projects that have pull-based Apigee and hybrid plugins configured, these plugins will continue to function and will be automatically migrated to the push-based type starting **August, 2025**. 

When you provision API hub as part of Apigee provisioning, it automatically identifies and attaches any associated Apigee runtime projects. This automatically creates an Apigee and hybrid plugin instance by default in API hub and ingests any deployed API proxies from Apigee. 

**Note:** If you provision API hub directly from the API hub UI, API hub doesn't automatically create a default plugin instance, nor does it auto-register proxies.

If you manually attach any additional Apigee runtime projects (Apigee or Apigee hybrid), API hub offers an option to import additonal API metadata. When this option is selected, API hub automatically creates the necessary plugin instance to manage the metadata import. These plugin instances are key to managing the connection and data ingestion for the auto-registration process.

### Auto-discovery of OpenAPI specs from Apigee proxies

To simplify API documentation and maintain synchronization with your Apigee proxy deployments, API hub automatically discovers and ingests valid OpenAPI specifications (OAS) when they are included in your Apigee API proxy resources. 

When a proxy is deployed in your Apigee runtime project (Apigee or Apigee hybrid), API hub automatically detects the presence of a valid OpenAPI spec in the proxy's resources folder. API hub then ingests and parses the spec, runs [linting](https://docs.cloud.google.com/apigee/docs/apihub/validate-spec) for validation, and uses the spec to populate the API's documentation, including its operations. This ensures that the API definition in API hub is always consistent with the deployed proxy in your Apigee runtime project. 

**Note:** Auto-discovery of OAS happens irrespective of whether you attach an Apigee runtime project to API hub or if your Apigee runtime project is automatically attached to API hub as part of Apigee provisioning. 

### Project associations scheduler

**Note:** This functionality applies only to [pull-based](https://docs.cloud.google.com/apigee/docs/apihub/plugins#plugin-data-ingestion-methods) Apigee and hybrid plugin instances. For push-based plugins, data ingestion is automatically triggered by changes in the source. 

API hub periodically (once in six hours) runs a scheduler that connects to your Apigee project, and gets the latest proxy definitions. For the projects that are newly attached, the scheduler gets all the proxy definitions, and then registers them in API hub. And for the existing projects, the scheduler gets only the changes made to the proxy definitions, and then accordingly updates the proxy information in API hub.

## Considerations

Consider the following when attempting to attach Apigee runtime projects:

  * All endpoints imported from Apigee will be given an `https://` prefix by default.
  * Proxies that aren't deployed in any environment, aren't fetched from the project.
  * Only proxies that are deployed in an environment are fetched. And the environment must be a part of an environment group.
  * Additional attributes representing the Apigee instance type (`Apigee X and Hybrid Environment` and `Apigee X and Hybrid Organization`) are automatically created and added to any proxy API deployments that are imported. **Deprecated:** The Apigee instance type attribute is no longer added to API deployments as of **July 31, 2025**. For existing projects that have Apigee instance type attributes configured, we recommend that you remove these attributes from any filtered search queries. You can use the **Source project** and **Source environment** fields instead. 
  * If the Apigee API isn't enabled for a runtime project, API hub can't auto-register or import the API proxies.



### Limitations

  * API hub doesn't support creating a plugin instance if [Data Residency is enabled](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts) for your Apigee organization.
  * API hub only parses and displays operations from the OAS file associated with the latest deployed revision of a proxy. If multiple revisions exist with different OAS files, only the spec from the most recently deployed revision is used to populate the API's documentation and operations list.



## What's next

  * Learn more about [plugins and plugin instances](https://docs.cloud.google.com/apigee/docs/apihub/plugins).
  * Learn about [curations](https://docs.cloud.google.com/apigee/docs/apihub/curations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
