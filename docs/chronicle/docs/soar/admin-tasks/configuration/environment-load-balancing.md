---
url: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/configuration/environment-load-balancing/
title: Manage environment load balancing \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:24:33.602056+00:00
---

# Manage environment load balancing  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/configuration/environment-load-balancing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage environment load balancing

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document explains how you can use environment load balancing to help maintain platform stability and ensure fair resource distribution, especially in multi-tenant environments. It aims to prevent any single, heavy-loaded environment from consuming excessive system resources over a short period of time.

The system uses a lottery algorithm to randomly select environments for resource allocation. Each active environment receives a number of tickets, and the system randomly selects winning tickets to process tasks. By default, all environments receive an equal number of tickets, but administrators can assign higher weights to certain environments to prioritize them.

## Configure environment load balancing

**Note:** Environment load balancing is managed through REST API endpoints. Some existing APIs are transitioning to new Chronicle API endpoints, but some Legacy API endpoints are still available. Administrative users must use these APIs to enable and configure load balancing at a basic or advanced configuration level. For more information about the migration, see [Migrate to Google Cloud](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp).

Once enabled, the system uses a lottery algorithm to allocate resources. Each active environment receives tickets. By default, all environments receive an equal number of tickets. The system randomly selects winning tickets, and the corresponding environments are granted access to system resources for task processing.

This randomized approach ensures fair and balanced resource distribution across all environments.

### Basic configuration

You can enable or disable environment load balancing using the following legacy API endpoint:
    
    
    POST /api/external/v1/settings/toggle-environment-load-balancing

### Advanced configuration

The following APIs are used to manage the weights assigned to individual environments:

#### Chronicle API endpoints (recommended)

  * To reset the weights of all environments to their default: 
        
        POST /projects/{project}/locations/{location}/instances/{instance}/environments:resetWeights

  * To view the weights of all environments: 
        
        GET /projects/{project}/locations/{location}/instances/{instance}/environments

  * To view the weight of a specific environment: 
        
        GET /projects/{project}/locations/{location}/instances/{instance}/environments/{environment}

  * To set the weight of a specific environment, replace `{environment}` with the `environment_ID`, and adjust the `weight` value in the request body: 
        
        PATCH /projects/{project}/locations/{location}/instances/{instance}/environments/{environment}

Request Body example:
        
        {
          "weight": 5
        }
        




#### Legacy API endpoints (deprecated)

  * To reset the weights of all environments to their default (equal weight), use the following API: 
        
        POST /api/external/v1/settings/reset-environment-priorities

  * To view the weight of all environments, use the following API: 
        
        GET /api/external/v1/settings/environment-priorities

  * To view the weight of a specific environment, replace `{environment}` with the `environment_ID`, and use the following API: 
        
        GET /api/external/v1/settings/environment-priorities/{environment}

  * To set the weight of a specific environment, replace `{environment}` with the `environment_ID`, update the `weight` value in the request body, and use the following API: 
        
        PATCH /api/external/v1/settings/environment-priorities/{environment}

Request Body example:
        
        {
          "weight": 3
        }
        




**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
