---
url: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/api-migration-guide/
title: Migrate to Chronicle API \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:07.354701+00:00
---

# Migrate to Chronicle API  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/api-migration-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Migrate to Chronicle API

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document applies to you if you call SOAR API programmatically using integrations, custom scripts or custom actions. This document outlines the steps and considerations to help you update programmatic API references to the new SOAR API endpoints as part of Chronicle API.

The Chronicle API surface introduces several improvements designed to streamline your development process. It also addresses limitations and complexities present in the older API.

The legacy SOAR API and API keys will be available until March 31, 2027, after which they will no longer function. 

## Prerequisites

Before performing the SOAR API migration, you need to do the following:

  * [Complete Stage 1 of the migration](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp). 



## Key changes and enhancements

The following table highlights the major differences between the old and new API surfaces:

Feature area | Old API | New API | Details  
---|---|---|---  
Authentication | API token | OAuth 2.0 | The new authentication method provides enhanced security and standardizes the process.  
Data models | Flat structures | Resource-oriented design | This new design improves data consistency and simplifies object manipulation.  
Endpoint naming | Inconsistent | RESTful and standardized | Consistent naming makes the API more intuitive and easier to integrate.  
  
## Deprecation schedule

The old API surface for SOAR is scheduled to be fully deprecated on March 31, 2027. We recommend completing your migration before this date to avoid any service interruptions.

## Migration steps

This section outlines the steps to successfully migrate your applications to Chronicle API:

### Review the documentation

Familiarize yourself with the comprehensive documentation for the new API, including the [Chronicle API](https://docs.cloud.google.com/chronicle/docs/reference/rest) reference guide.

### Map endpoints to the new API surface

Identify the corresponding new endpoints for each of the old API calls your application makes. Similarly, map the old data models to the new ones, accounting for any structural changes or new fields. For details, see [API endpoint mapping table](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/endpoint-mapping-table).

### Optional: Create a staging integration

If you're editing a custom integration or a component of a commercial integration, we recommend that you push the changes to a staging integration first. This process lets you test without impacting your production automation flows. If you're migrating a custom-built application that uses the SOAR API, you can skip to the next step. For details about integration staging, see [Test integrations in staging mode](https://docs.cloud.google.com/chronicle/docs/soar/respond/ide/test-integrations-in-staging-mode).

### Update the service endpoint and URLs

A service endpoint is the base URL that specifies the network address of an API service. A single service can have multiple service endpoints. Chronicle is a regional service and only supports regional endpoints.

All new endpoints use a consistent prefix, making the final endpoint address predictable. The following example shows the new endpoint URL structure:
    
    
    [api_version]/projects/[project_id]/locations/[location]/instances[instance_id]/...
    

This structure makes the final address to the endpoint as follows:
    
    
    https://[service_endpoint]/[api_version]/projects/[project_id]/locations/[location]/instances/[instance_id]/...
    

Where:

  * `service_endpoint`: A regional service address
  * `api_version`: The API version to query. Can be `v1alpha`, `v1beta`, or `v1`.
  * `project_id`: Your project ID (same project as you defined for your IAM permissions)
  * `location`: The location of your project (region); same as the regional endpoints
  * `instance_id`: Your Google Security Operations SIEM customer ID.



Regional addresses:

  * africa-south1: `https://chronicle.africa-south1.rep.googleapis.com`

  * asia-northeast1: `https://chronicle.asia-northeast1.rep.googleapis.com`

  * asia-south1: `https://chronicle.asia-south1.rep.googleapis.com`

  * asia-southeast1: `https://chronicle.asia-southeast1.rep.googleapis.com`

  * asia-southeast2: `https://chronicle.asia-southeast2.rep.googleapis.com`

  * australia-southeast1: `https://chronicle.australia-southeast1.rep.googleapis.com`

  * europe-west12: `https://chronicle.europe-west12.rep.googleapis.com`

  * europe-west2: `https://chronicle.europe-west2.rep.googleapis.com`

  * europe-west3: `https://chronicle.europe-west3.rep.googleapis.com`

  * europe-west6: `https://chronicle.europe-west6.rep.googleapis.com`

  * europe-west9: `https://chronicle.europe-west9.rep.googleapis.com`

  * me-central1: `https://chronicle.me-central1.rep.googleapis.com`

  * me-central2: `https://chronicle.me-central2.rep.googleapis.com`

  * me-west1: `https://chronicle.me-west1.rep.googleapis.com`

  * northamerica-northeast2: `https://chronicle.northamerica-northeast2.rep.googleapis.com`

  * southamerica-east1: `https://chronicle.southamerica-east1.rep.googleapis.com`

  * us: `https://chronicle.us.rep.googleapis.com`

  * eu: `https://chronicle.eu.rep.googleapis.com`




For example, to get a list of all cases on a project in the US:
    
    
    GET 
      https://chronicle.us.rep.googleapis.com/v1alpha/projects/my-project-name-or-id/locations/us/instances/408bfb7b-5746-4a50-885a-50a323023529/cases
    

### Update the authentication method

The new API uses Google Cloud IAM for authentication. You'll need to update your application or response integration to implement this new authentication flow. Make sure the user who runs the script has the correct permissions for the endpoints they're trying to access. To implement this new flow, you must update your response integrations or applications. Ensure that the user executing the script possesses the necessary permissions for the targeted endpoints. For detailed instructions, see the [Authenticate to Chronicle API page](https://docs.cloud.google.com/chronicle/docs/reference/authentication).

### Map the service account or workload identity to SOAR parameters

If you are using a service account or workload identity federation to authenticate to the Chronicle API, you must authorize it within the platform to ensure it can successfully communicate with Google SecOps. This mapping is required to provide the service account or workload identity with the necessary access to SOC Roles and Environments.

To grant a _service account access_ or _workload identity federation access_ to Google SecOps, you must map the identity to the platform's access control parameters. This mapping is a mandatory step to provide the identity with the necessary access to **SOC Roles** , and **Environments** required to perform automated tasks or API operations.

  1. Go to **SOAR Settings > Advanced > Group Mapping**.
  2. Click add **Add**.
  3. Complete the fields in the **Add Mapping** dialog to map the identity to the platform's access control parameters.

     1. In the **IdP / User group** field, enter one of the following: 
        * The full email address of your service account, if identity was set up using Cloud Identity.
        * The Workload Identity principal string, if identity was set up using Workforce Identity Federation.
     2. Configure the following access control fields:

Field | Description  
---|---  
**Permission groups** | Select the permission groups to define which modules and submodules the identity can access.  
**SOC roles** | Select the SOC roles to define the identity's role (such as Tier 1).  
**Environments** | Select the environments or environment groups the identity can access (such as **All Environments**).  
**Group members** | Enter the required user emails if applicable. Press **Enter** after adding each email.  
**Restricted actions** | Select the restricted actions to limit specific operations within modules.  
  4. Click **Add**.




For more detailed information on mapping users and service accounts, see [Map users in the platform using third-party identity](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-secops/map-users-in-the-secops-platform) or [Map users in the platform using Cloud Identity](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-secops/map-users-in-the-secops-platform-first-party).

### Update API logic

Analyze the new data models and endpoint structures provided in the API reference. Not all methods have changed significantly, and some existing code can be reused. The primary objective is to review the new reference documentation and, for each specific use case, identify and implement necessary changes to field names and data structures within your application's logic.

### Test your integration

Test your updated application in a staging integration before deploying to production:

  1. Create a test plan: Define test cases that cover all migrated functionalities.
  2. Execute tests: Run automated and manual tests to confirm accuracy and validity.
  3. Monitor performance: Assess the performance of your application with the new API.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
