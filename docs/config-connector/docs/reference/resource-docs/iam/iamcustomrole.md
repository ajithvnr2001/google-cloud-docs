---
url: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/iam/iamcustomrole/
title: IAMCustomRole \u00a0|\u00a0 Config Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:11:20.142422+00:00
---

# IAMCustomRole  |  Config Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/iam/iamcustomrole/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ API and reference ](https://docs.cloud.google.com/config-connector/docs/reference/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# IAMCustomRole

**Property** | **Value**  
---|---  
Google Cloud Service Name | IAM  
Google Cloud Service Documentation | [/iam/docs/](https://docs.cloud.google.com/iam/docs)  
Google Cloud REST Resource Name | v1.projects.roles  
Google Cloud REST Resource Documentation | [/iam/docs/reference/rest/v1/projects.roles](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.roles)  
Config Connector Resource Short Names | gcpiamcustomrole  
gcpiamcustomroles  
iamcustomrole  
Config Connector Service Name | iam.googleapis.com  
Config Connector Resource Fully Qualified Name | iamcustomroles.iam.cnrm.cloud.google.com  
Can Be Referenced by IAMPolicy/IAMPolicyMember | No  
Config Connector Default Average Reconcile Interval In Seconds | 600  
  
## Custom Resource Definition Properties

### Annotations

Fields  
---  
`cnrm.cloud.google.com/organization-id`  
`cnrm.cloud.google.com/project-id`  
  
### Spec

#### Schema
    
    
    description: string
    permissions:
    - string
    resourceID: string
    stage: string
    title: string
    

Fields  
---  
`description` _Optional_ |  `string` A human-readable description for the role.  
`permissions` _Required_ |  `list (string)` The names of the permissions this role grants when bound in an IAM policy. At least one permission must be specified.  
`permissions[]` _Required_ |  `string`  
`resourceID` _Optional_ |  `string` Immutable. Optional. The roleId of the resource. Used for creation and acquisition. When unset, the value of `metadata.name` is used as the default.  
`stage` _Optional_ |  `string` The current launch stage of the role. Defaults to GA.  
`title` _Required_ |  `string` A human-readable title for the role.  
  
### Status

#### Schema
    
    
    conditions:
    - lastTransitionTime: string
      message: string
      reason: string
      status: string
      type: string
    deleted: boolean
    name: string
    observedGeneration: integer
    

Fields  
---  
`conditions` |  `list (object)` Conditions represent the latest available observation of the resource's current state.  
`conditions[]` |  `object`  
`conditions[].lastTransitionTime` |  `string` Last time the condition transitioned from one status to another.  
`conditions[].message` |  `string` Human-readable message indicating details about last transition.  
`conditions[].reason` |  `string` Unique, one-word, CamelCase reason for the condition's last transition.  
`conditions[].status` |  `string` Status is the status of the condition. Can be True, False, Unknown.  
`conditions[].type` |  `string` Type is the type of the condition.  
`deleted` |  `boolean` The current deleted state of the role.  
`name` |  `string` The full name of the role.  
`observedGeneration` |  `integer` ObservedGeneration is the generation of the resource that was most recently observed by the Config Connector controller. If this is equal to metadata.generation, then that means that the current reported status reflects the most recent desired state of the resource.  
  
## Sample YAML(s)

### Organization Role
    
    
    # Copyright 2020 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    apiVersion: iam.cnrm.cloud.google.com/v1beta1
    kind: IAMCustomRole
    metadata:
      annotations:
        # Replace "${ORG_ID?}" with your organization ID
        cnrm.cloud.google.com/organization-id: "${ORG_ID?}"
      name: iamcustomrolesampleorganization
    spec:
      title: Example Organization-Level Custom Role Created by Config Connector
      description: This role only contains two permissions - publish and update
      permissions:
        - pubsub.topics.publish
        - pubsub.topics.update
      stage: GA
    

### Project Role
    
    
    # Copyright 2020 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    # Replace ${PROJECT_ID?} below with your desired project ID.
    apiVersion: iam.cnrm.cloud.google.com/v1beta1
    kind: IAMCustomRole
    metadata:
      annotations:
        cnrm.cloud.google.com/project-id: ${PROJECT_ID?}
      name: iamcustomrolesampleproject
    spec:
      title: Example Project-Level Custom Role
      description: This role only contains two permissions - publish and update
      permissions:
        - pubsub.topics.publish
        - pubsub.topics.update
      stage: GA
    ---
    # Replace ${PROJECT_ID?} below with your desired project ID.
    apiVersion: iam.cnrm.cloud.google.com/v1beta1
    kind: IAMPolicyMember
    metadata:
      name: iampolicymember-sample-projectrole
    spec:
      member: serviceAccount:iamcustomrole-dep-project@${PROJECT_ID?}.iam.gserviceaccount.com
      role: projects/${PROJECT_ID?}/roles/iamcustomrolesampleproject
      resourceRef:
        kind: PubSubTopic
        name: iamcustomrole-dep-project
    ---
    # Replace ${PROJECT_ID?} below with your desired project ID.
    apiVersion: iam.cnrm.cloud.google.com/v1beta1
    kind: IAMServiceAccount
    metadata:
      annotations:
        cnrm.cloud.google.com/project-id: ${PROJECT_ID?}
      name: iamcustomrole-dep-project
    ---
    apiVersion: pubsub.cnrm.cloud.google.com/v1beta1
    kind: PubSubTopic
    metadata:
      name: iamcustomrole-dep-project
    

**Note:** If you have any trouble with instantiating the resource, refer to [Troubleshoot Config Connector](https://docs.cloud.google.com/config-connector/docs/troubleshooting).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
