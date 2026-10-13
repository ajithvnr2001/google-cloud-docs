---
url: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates.components
title: REST Resource: projects.locations.spaces.applicationTemplates.components \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:30:26.089738+00:00
---

# REST Resource: projects.locations.spaces.applicationTemplates.components  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates.components

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Reference ](https://docs.cloud.google.com/application-design-center/docs/apis)



Send feedback 

#  REST Resource: projects.locations.spaces.applicationTemplates.components Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Component
    * JSON representation
  * Methods



## Resource: Component

Component resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "sharedTemplateRevisionUri": string,
      "parameters": [
        {
          object (Parameter)
        }
      ],
      "createTime": string,
      "updateTime": string,
      "roles": [
        string
      ],
      "apis": [
        string
      ],
      "displayName": string,
      "connectionsParameters": [
        {
          object (ConnectionParameters)
        }
      ],
      "componentParameterSchema": [
        {
          object (ComponentParameterSchema)
        }
      ],
      "applicationInfo": {
        object (ComponentApplicationInfo)
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. The component name.  
`sharedTemplateRevisionUri` |  `string` Required. Immutable. The shared template used to generate the component.  
`parameters[]` |  `object (`Parameter`)` Optional. The component parameters.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The component creation timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The component update timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`roles[]` |  `string` Output only. IAM roles required by the service account to deploy the component.  
`apis[]` |  `string` Output only. APIs required to be enabled to deploy the component, in the form of "*.googleapis.com".  
`displayName` |  `string` Optional. The component display name.  
`connectionsParameters[]` |  `object (`ConnectionParameters`)` Output only. The connection parameters of the component.  
`componentParameterSchema[]` |  `object (`ComponentParameterSchema`)` Output only. The component parameter schema, which includes possible parameter values. values.  
`applicationInfo` |  `object (`ComponentApplicationInfo`)` Optional. The application associated with the component.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates.components/create)`

|  Creates a component.  
  
### `[delete](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates.components/delete)`

|  Deletes a component.  
  
### `[get](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates.components/get)`

|  Gets details about a Component.  
  
### `[list](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates.components/list)`

|  Lists components in an application template.  
  
### `[patch](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates.components/patch)`

|  Updates a component.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-13 UTC."],[],[]] 
