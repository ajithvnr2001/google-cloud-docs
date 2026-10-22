---
url: https://docs.cloud.google.com/functions/docs/securing/custom-constraints/
title: Manage function resources using custom constraints \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:50:04.971959+00:00
---

# Manage function resources using custom constraints  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/securing/custom-constraints/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Reference ](https://docs.cloud.google.com/functions/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage function resources using custom constraints

**Note:** If you've created or deployed functions using Cloud Run, see Cloud Run's [Manage custom constraints for projects](https://docs.cloud.google.com/run/docs/securing/custom-constraints) guide for a detailed description of how to use custom constraints.

This page provides supplemental information for setting custom constraints on functions created using the [Cloud Functions v2 API](https://docs.cloud.google.com/functions/docs/reference/rest), such as through the [`gcloud functions`](https://docs.cloud.google.com/sdk/gcloud/reference/functions) commands.

## Limitations

The following limitations apply to using custom organization policies for [Cloud Functions v2 API](https://docs.cloud.google.com/functions/docs/reference/rest) functions:

  * Only available on [Cloud Functions v2 API](https://docs.cloud.google.com/functions/docs/reference/rest).
  * They won't be applied to Cloud Run functions (1st gen).
  * Only protects functions when using the Cloud Functions v2 API. Cloud Run functions can also be modified from the Cloud Run API as well. For additional protection, you might need to also [apply custom constraints on Cloud Run](https://docs.cloud.google.com/run/docs/securing/custom-constraints) as well.



## Common organization policy examples

The following table provides the syntax of some custom organization policies that you might find useful:

Description | Constraint syntax  
---|---  
Prevent functions from being created with a specific language | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.cloudFunctionRuntimeBlock
        resource_types: cloudfunctions.googleapis.com/Function
        method_types:
          - CREATE
          - UPDATE
        condition: resource.buildConfig.runtime == "python312"
        action_type: DENY
        display_name: Deny functions using Python 3.12
        description: Functions cannot be created with Python 3.12 as the language runtime  
  
Require functions to use a specific worker pool | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.cloudFunctionsWorkerPool
        resource_types: cloudfunctions.googleapis.com/Function
        method_types:
          - CREATE
          - UPDATE
        condition: resource.buildConfig.workerPool == "WORKER_POOL"
        action_type: DENY
        display_name: Require worker pool
        description: Functions must use a worker pool

Replace WORKER_POOL with the name of your Cloud Build worker pool.   
Require that functions store all container images in a specific image repository | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.cloudFunctionsRepository
        resource_types: cloudfunctions.googleapis.com/Function
        method_types:
          - CREATE
          - UPDATE
        condition: resource.buildConfig.dockerRepository.startsWith("REPO_PATH")
        action_type: DENY
        display_name: Image repository constraint
        description: Functions must push images to a central image repository under REPO_PATH

Replace REPO_PATH with the URI of the image repository URL that you want all functions to store their container images in.   
  
## What's next

  * See [Introduction to the Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) to learn more about organization policies.
  * Learn more about how to [create and manage organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints).
  * See the full list of predefined [organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
