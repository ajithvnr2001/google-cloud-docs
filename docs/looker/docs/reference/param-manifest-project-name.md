---
url: https://docs.cloud.google.com/looker/docs/reference/param-manifest-project-name/
title: project_name \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:16.944424+00:00
---

# project_name  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-manifest-project-name/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  project_name Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    
    project_name: "my_project_name"
    

Hierarchy [Project Manifest File](https://docs.cloud.google.com/looker/docs/reference/param-project-manifest) `project_name` |  Default Value None Accepts A string specifying the current project name   
---|---  
  
## Definition

`project_name` specifies the current project name in a manifest file. This is required when using a [manifest file](https://docs.cloud.google.com/looker/docs/importing-projects#creating_a_project_manifest_file) to [import files from other projects](https://docs.cloud.google.com/looker/docs/importing-projects).

## Example

In a manifest file, specify the current project name as "thelook":
    
    
    project_name: "thelook"
    
    local_dependency: {
       project: "other_project"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
