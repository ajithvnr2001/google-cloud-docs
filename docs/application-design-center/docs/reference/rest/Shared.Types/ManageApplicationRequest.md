---
url: https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ManageApplicationRequest/
title: ManageApplicationRequest \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:52:48.744820+00:00
---

# ManageApplicationRequest  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ManageApplicationRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Reference ](https://docs.cloud.google.com/application-design-center/docs/apis)



Send feedback 

#  ManageApplicationRequest Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Request message for ManageApplication. This request is used by an agent via an MCP tool to perform operations on application resources. The agent should populate fields based on the operation being performed.

JSON representation  
---  
      
    
    {
      "parent": string,
      "applicationId": string,
      "application": {
        object ([Application](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Application))
      },
      "updateMask": string,
      "serviceAccount": string,
      "operation": enum ([ApplicationOperation](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ApplicationOperation)),
      "artifactLocation": {
        object ([ArtifactLocation](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ArtifactLocation))
      },
      "applicationTemplateUri": string,
      "applicationTemplateRevisionUri": string,
      "deploymentRegion": string
    }  
  
Fields  
---  
`parent` |  `string` Required. The parent resource. Format: projects/{project}/locations/{location}/spaces/{space}  
`applicationId` |  `string` Required. The ID of application. For APPLICATION_CREATE, this is the ID of application to create. For other operations like UPDATE, PREVIEW, DEPLOY, this is used to identify the application.  
`application` |  `object (`[Application](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Application)`)` Optional. The application resource. Required for APPLICATION_CREATE and APPLICATION_UPDATE operations.  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Optional. Field mask for APPLICATION_UPDATE operation.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
`serviceAccount` |  `string` Optional. The service account for APPLICATION_PREVIEW or APPLICATION_DEPLOY operations. Format: projects/{PROJECT}/serviceAccounts/{EMAIL_ADDRESS} If a service account is provided, the system will attempt to grant it the necessary roles. The caller must have the `resourcemanager.projects.setIamPolicy` permission on the deployment projects to allow these role assignments.  
`operation` |  `enum (`[ApplicationOperation](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ApplicationOperation)`)` Required. The operation to perform on the application.  
`artifactLocation` |  `object (`[ArtifactLocation](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ArtifactLocation)`)` Optional. The location of the artifact for the application. Required for APPLICATION_GENERATE_IAC operation.  
`applicationTemplateUri` |  `string` Optional. The URI of the application template. Required for creating an application from an application template.  
`applicationTemplateRevisionUri` |  `string` Optional. The URI of the application template revision. Required for creating an application from an application template revision.  
`deploymentRegion` |  `string` Optional. The deployment region of the application. Required for creating an application during deployment.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-13 UTC."],[],[]] 
