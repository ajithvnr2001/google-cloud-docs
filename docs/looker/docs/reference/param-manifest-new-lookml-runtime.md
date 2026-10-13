---
url: https://docs.cloud.google.com/looker/docs/reference/param-manifest-new-lookml-runtime/
title: new_lookml_runtime \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:18.732637+00:00
---

# new_lookml_runtime  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-manifest-new-lookml-runtime/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  new_lookml_runtime Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    new_lookml_runtime: yes
    

Hierarchy [Manifest File](https://docs.cloud.google.com/looker/docs/reference/param-project-manifest) `new_lookml_runtime` |  Default Value Yes  
---|---  
  
## Definition

**Caution:** Using the legacy LookML runtime is highly discouraged, especially for [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview) instances.

The new LookML runtime provides faster [LookML validation](https://docs.cloud.google.com/looker/docs/lookml-validation#validating_your_lookml) and [content validation](https://docs.cloud.google.com/looker/docs/content-validation), more performant loading of [Explores](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores) and [dashboards](https://docs.cloud.google.com/looker/docs/viewing-dashboards), and faster SQL query writing, among other performance improvements.

You can use the `new_lookml_runtime` parameter to override your Looker instance's default LookML runtime. The default runtime for projects on your instance is configured with the [**Use Legacy LookML Runtime**](https://docs.cloud.google.com/looker/docs/legacy-feature-schedule#new_lookml_runtime) legacy toggle:

  * If the **Use Legacy LookML Runtime** legacy feature is enabled, projects on the instance will use the legacy LookML runtime by default. LookML developers can add `new_lookml_runtime: yes` to a project to override the instance default and enable the new LookML runtime for the project.
  * If the **Use Legacy LookML Runtime** legacy feature is disabled, projects on the instance will use the new LookML runtime by default. LookML developers can add `new_lookml_runtime: no` to a project to override the instance default and use the legacy LookML runtime.



For example, if the **Use Legacy LookML Runtime** legacy feature is disabled for your instance, you can add the `new_lookml_runtime: no` statement to the project's [manifest file](https://docs.cloud.google.com/looker/docs/reference/param-project-manifest) to use the legacy LookML runtime for the project:
    
    
    new_lookml_runtime: no
    

If your project does not have a manifest file, you can [create one](https://docs.cloud.google.com/looker/docs/other-project-files#creating_a_manifest_file) using the Looker IDE.

## Considerations

When the new LookML runtime is enabled for a project, the LookML validator may catch previously overlooked errors. See the [Error: Unknown or Inaccessible Field](https://docs.cloud.google.com/looker/docs/best-practices/error-unknown-or-inaccessible-field) Best Practices page for more information on how to resolve these errors.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
