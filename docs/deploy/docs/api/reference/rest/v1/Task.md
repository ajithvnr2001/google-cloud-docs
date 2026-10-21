---
url: https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/Task/
title: Task \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:15:03.740962+00:00
---

# Task  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/Task/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Reference ](https://docs.cloud.google.com/deploy/docs/api)



Send feedback 

#  Task Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * ContainerTask
    * JSON representation



A Task represents a unit of work that is executed as part of a Job.

JSON representation  
---  
      
    
    {
    
      // Union field type can be only one of the following:
      "container": {
        object ([ContainerTask](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/Task#ContainerTask))
      }
      // End of list of possible types for union field type.
    }  
  
Fields  
---  
Union field `type`. The type of Task. `type` can be only one of the following:  
`container` |  `object (`[ContainerTask](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/Task#ContainerTask)`)` Optional. This task is represented by a container that is executed in the Cloud Build execution environment.  
  
## ContainerTask

This task is represented by a container that is executed in the Cloud Build execution environment.

JSON representation  
---  
      
    
    {
      "image": string,
      "command": [
        string
      ],
      "args": [
        string
      ],
      "env": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`image` |  `string` Required. Image is the container image to use.  
`command[]` |  `string` Optional. Command is the container entrypoint to use. This overrides the default entrypoint defined in the container image.  
`args[]` |  `string` Optional. Args is the container arguments to use. This overrides the default arguments defined in the container image.  
`env` |  `map (key: string, value: string)` Optional. Environment variables that are set in the container.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-02 UTC."],[],[]] 
