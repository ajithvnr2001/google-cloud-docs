---
url: https://docs.cloud.google.com/deployment-manager/docs/troubleshooting/
title: Tips and troubleshooting \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:03.454579+00:00
---

# Tips and troubleshooting  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/troubleshooting/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Support ](https://docs.cloud.google.com/deployment-manager/docs/support)



Send feedback 

#  Tips and troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

The following sections might help you if you run into problems while using Deployment Manager.

## Common errors during deployments

The errors that you see in your deployments are in the following format:
    
    
    - code: ERROR_CODE
      location: /path/to/template
      message: "{"Error message"}"
    

The types of errors you might commonly see are described in the following sections.

### Resource errors (code: `RESOURCE_ERROR`)

Resource errors are propagated from the underlying APIs for the resources that you are managing with Deployment Manager. For example, if your deployment has a Compute Engine VM instance, and there was an error creating the instance, you see that error as a resource error in Deployment Manager.

In the Deployment Manager response, you can see the error from the underlying API in the `message.ResourceErrorCode` and `message.ResourceErrorMessage` fields.

### Validation errors (code: `CONDITION_NOT_MET`)

You get a validation error when a field in your configuration fails validation, such as if it uses a string value when a boolean is expected.

### Dependency loops (code: `CYCLIC_REFERENCES`)

Indicates that your configuration has a dependency loop. For example, if resource A depends on resource B, B depends on C, and C depends on A.

The error message shows the resources that are in the dependency loop.

You might see dependencies in resources in the following scenarios:

  * A reference to a property of another resource. For example, if your deployment has an instance group manager that uses an instance template from the same deployment, the instance group manager implicitly depends on the instance template. Deployment Manager creates the instance template first, then creates the instance group manager.

  * An explicit `dependsOn` property, which indicates that the current resource must be created after the resource it depends on.




To resolve the error, change the references or `dependsOn` properties so that the loop is broken.

### Errors while expanding your templates

Your templates are limited in the amount of time and resources that Deployment Manager uses to expand the templates into a single configuration.

You might see one of the following errors:

  * `MANIFEST_EXPANSION_TOO_MUCH_CPU`: Expanding the configuration took too much CPU.
  * `MANIFEST_EXPANSION_TOO_MUCH_MEMORY`: Expanding the configuration took too much memory.
  * `MANIFEST_EXPANSION_TOO_MUCH_WALL_TIME`: Expanding the configuration took too much time.
  * `MANIFEST_EXPANSION_USER_ERROR`: There was an error in your configuration or one of your templates.



`MANIFEST_EXPANSION_TOO_MUCH_CPU` and `MANIFEST_EXPANSION_TOO_MUCH_MEMORY` might indicate that your templates might have complex structures involving recursion, or too many loops.

To resolve these errors, consider splitting your templates into smaller templates, or simplifying your templates.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
