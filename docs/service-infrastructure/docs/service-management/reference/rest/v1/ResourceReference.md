---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/ResourceReference/
title: ResourceReference \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:30.412942+00:00
---

# ResourceReference  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/ResourceReference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  ResourceReference Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Defines a proto annotation that describes a string field that refers to an API resource.

JSON representation  
---  
      
    
    {
      "type": string,
      "childType": string
    }  
  
Fields  
---  
`type` |  `string` The resource type that the annotated field references.Example:
    
    
    message Subscription {
      string topic = 2 [(google.api.resource_reference) = {
        type: "pubsub.googleapis.com/Topic"
      }];
    }
    

Occasionally, a field may reference an arbitrary resource. In this case, APIs use the special value * in their resource reference.Example:
    
    
    message GetIamPolicyRequest {
      string resource = 2 [(google.api.resource_reference) = {
        type: "*"
      }];
    }
      
  
`childType` |  `string` The resource type of a child collection that the annotated field references. This is useful for annotating the `parent` field that doesn't have a fixed resource type.Example:
    
    
    message ListLogEntriesRequest {
      string parent = 1 [(google.api.resource_reference) = {
        childType: "logging.googleapis.com/LogEntry"
      };
    }
      
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
