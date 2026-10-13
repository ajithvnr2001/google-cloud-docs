---
url: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/essentialcontacts/essentialcontactscontact/
title: EssentialContactsContact \u00a0|\u00a0 Config Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:29:23.892558+00:00
---

# EssentialContactsContact  |  Config Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/essentialcontacts/essentialcontactscontact/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ API and reference ](https://docs.cloud.google.com/config-connector/docs/reference/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# EssentialContactsContact

**Property** | **Value**  
---|---  
Google Cloud Service Name | Essential Contacts  
Google Cloud Service Documentation | [/resource-manager/docs/managing-notification-contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts)  
Google Cloud REST Resource Name | projects.contacts  
Google Cloud REST Resource Documentation | [/resource-manager/docs/reference/essentialcontacts/rest/v1/projects.contacts](https://docs.cloud.google.com/resource-manager/docs/reference/essentialcontacts/rest/v1/projects.contacts)  
Config Connector Resource Short Names | essentialcontactscontact  
gcpessentialcontactscontact  
gcpessentialcontactscontacts  
Config Connector Service Name | essentialcontacts.googleapis.com  
Config Connector Resource Fully Qualified Name | essentialcontactscontacts.essentialcontacts.cnrm.cloud.google.com  
Can Be Referenced by IAMPolicy/IAMPolicyMember | No  
Config Connector Default Average Reconcile Interval In Seconds | 600  
  
## Custom Resource Definition Properties

### Spec

#### Schema
    
    
    email: string
    folderRef:
      external: string
      name: string
      namespace: string
    languageTag: string
    notificationCategorySubscriptions:
    - string
    organizationRef:
      external: string
    projectRef:
      external: string
      kind: string
      name: string
      namespace: string
    resourceID: string
    

Fields  
---  
`email` _Required_ |  `string` Required. The email address to send notifications to. The email address does not need to be a Google Account.  
`folderRef` _Optional_ |  `object` The Folder that contains this resource.  
`folderRef.external` _Optional_ |  `string` The 'name' field of a folder, when not managed by Config Connector. This field must be set when 'name' field is not set.  
`folderRef.name` _Optional_ |  `string` The 'name' field of a 'Folder' resource. This field must be set when 'external' field is not set.  
`folderRef.namespace` _Optional_ |  `string` The 'namespace' field of a 'Folder' resource. If unset, the namespace is defaulted to the namespace of the referencer resource.  
`languageTag` _Required_ |  `string` Required. The preferred language for notifications, as an ISO 639-1 language code. See [Supported languages](https://cloud.google.com/resource-manager/docs/managing-notification-contacts#supported-languages) for a list of supported languages.  
`notificationCategorySubscriptions` _Required_ |  `list (string)` Required. The categories of notifications that the contact will receive communications for.  
`notificationCategorySubscriptions[]` _Required_ |  `string`  
`organizationRef` _Optional_ |  `object` OrganizationRef represents the Organization that this resource belongs to.  
`organizationRef.external` _Required*_ |  `string` The 'name' field of an organization, when not managed by Config Connector.  
`projectRef` _Optional_ |  `object` The Project that this resource belongs to.  
`projectRef.external` _Optional_ |  `string` The `projectID` field of a project, when not managed by Config Connector.  
`projectRef.kind` _Optional_ |  `string` The kind of the Project resource; optional but must be `Project` if provided.  
`projectRef.name` _Optional_ |  `string` The `name` field of a `Project` resource.  
`projectRef.namespace` _Optional_ |  `string` The `namespace` field of a `Project` resource.  
`resourceID` _Optional_ |  `string` Immutable. Optional. The service-generated name of the resource. Used for acquisition only. Leave unset to create a new resource.  
  
* Field is required when parent field is specified

### Status

#### Schema
    
    
    conditions:
    - lastTransitionTime: string
      message: string
      reason: string
      status: string
      type: string
    externalRef: string
    observedGeneration: integer
    observedState:
      validateTime: string
      validationState: string
    

Fields  
---  
`conditions` |  `list (object)` Conditions represent the latest available observations of the object's current state.  
`conditions[]` |  `object`  
`conditions[].lastTransitionTime` |  `string` Last time the condition transitioned from one status to another.  
`conditions[].message` |  `string` Human-readable message indicating details about last transition.  
`conditions[].reason` |  `string` Unique, one-word, CamelCase reason for the condition's last transition.  
`conditions[].status` |  `string` Status is the status of the condition. Can be True, False, Unknown.  
`conditions[].type` |  `string` Type is the type of the condition.  
`externalRef` |  `string` A unique specifier for the EssentialContactsContact resource in Google Cloud.  
`observedGeneration` |  `integer` ObservedGeneration is the generation of the resource that was most recently observed by the Config Connector controller. If this is equal to metadata.generation, then that means that the current reported status reflects the most recent desired state of the resource.  
`observedState` |  `object` ObservedState is the state of the resource as most recently observed in Google Cloud.  
`observedState.validateTime` |  `string` The last time the validation_state was updated, either manually or automatically. A contact is considered stale if its validation state was updated more than 1 year ago.  
`observedState.validationState` |  `string` Output only. The validity of the contact. A contact is considered valid if it is the correct recipient for notifications for a particular resource.  
  
## Sample YAML(s)

**Note:** If you have any trouble with instantiating the resource, refer to [Troubleshoot Config Connector](https://docs.cloud.google.com/config-connector/docs/troubleshooting).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
