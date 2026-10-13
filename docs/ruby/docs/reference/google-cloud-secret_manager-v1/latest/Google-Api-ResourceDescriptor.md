---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Api-ResourceDescriptor/
title: Secret Manager V1 API - Class Google::Api::ResourceDescriptor (v1.9.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:04:37.511428+00:00
---

# Secret Manager V1 API - Class Google::Api::ResourceDescriptor (v1.9.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Api-ResourceDescriptor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Secret Manager V1 API - Class Google::Api::ResourceDescriptor (v1.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.1 (latest)  1.9.0  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.21.0  0.20.0  0.19.2  0.18.0  0.17.2  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.3 

Reference documentation and code samples for the Secret Manager V1 API class Google::Api::ResourceDescriptor.

A simple descriptor of a resource type.

ResourceDescriptor annotates a resource message (either by means of a protobuf annotation or use in the service config), and associates the resource's schema, the resource type, and the pattern of the resource name.

Example:
    
    
    message Topic {
      // Indicates this message defines a resource schema.
      // Declares the resource type in the format of {service}/{kind}.
      // For Kubernetes resources, the format is {api group}/{kind}.
      option (google.api.resource) = {
        type: "pubsub.googleapis.com/Topic"
        pattern: "projects/{project}/topics/{topic}"
      };
    }
    

The ResourceDescriptor Yaml config will look like:
    
    
    resources:
    - type: "pubsub.googleapis.com/Topic"
      pattern: "projects/{project}/topics/{topic}"
    

Sometimes, resources have multiple patterns, typically because they can live under multiple parents.

Example:
    
    
    message LogEntry {
      option (google.api.resource) = {
        type: "logging.googleapis.com/LogEntry"
        pattern: "projects/{project}/logs/{log}"
        pattern: "folders/{folder}/logs/{log}"
        pattern: "organizations/{organization}/logs/{log}"
        pattern: "billingAccounts/{billing_account}/logs/{log}"
      };
    }
    

The ResourceDescriptor Yaml config will look like:
    
    
    resources:
    - type: 'logging.googleapis.com/LogEntry'
      pattern: "projects/{project}/logs/{log}"
      pattern: "folders/{folder}/logs/{log}"
      pattern: "organizations/{organization}/logs/{log}"
      pattern: "billingAccounts/{billing_account}/logs/{log}"
    

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #history
    
    
    def history() -> ::Google::Api::ResourceDescriptor::History

**Returns**

  * ([::Google::Api::ResourceDescriptor::History](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Api-ResourceDescriptor-History)) — 

Optional. The historical or future-looking state of the resource pattern.

Example:
        
        // The InspectTemplate message originally only supported resource
        // names with organization, and project was added later.
        message InspectTemplate {
          option (google.api.resource) = {
            type: "dlp.googleapis.com/InspectTemplate"
            pattern:
            "organizations/{organization}/inspectTemplates/{inspect_template}"
            pattern: "projects/{project}/inspectTemplates/{inspect_template}"
            history: ORIGINALLY_SINGLE_PATTERN
          };
        }
        




### #history=
    
    
    def history=(value) -> ::Google::Api::ResourceDescriptor::History

**Parameter**

  * **value** ([::Google::Api::ResourceDescriptor::History](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Api-ResourceDescriptor-History)) — 

Optional. The historical or future-looking state of the resource pattern.

Example:
        
        // The InspectTemplate message originally only supported resource
        // names with organization, and project was added later.
        message InspectTemplate {
          option (google.api.resource) = {
            type: "dlp.googleapis.com/InspectTemplate"
            pattern:
            "organizations/{organization}/inspectTemplates/{inspect_template}"
            pattern: "projects/{project}/inspectTemplates/{inspect_template}"
            history: ORIGINALLY_SINGLE_PATTERN
          };
        }
        




**Returns**

  * ([::Google::Api::ResourceDescriptor::History](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Api-ResourceDescriptor-History)) — 

Optional. The historical or future-looking state of the resource pattern.

Example:
        
        // The InspectTemplate message originally only supported resource
        // names with organization, and project was added later.
        message InspectTemplate {
          option (google.api.resource) = {
            type: "dlp.googleapis.com/InspectTemplate"
            pattern:
            "organizations/{organization}/inspectTemplates/{inspect_template}"
            pattern: "projects/{project}/inspectTemplates/{inspect_template}"
            history: ORIGINALLY_SINGLE_PATTERN
          };
        }
        




### #name_field
    
    
    def name_field() -> ::String

**Returns**

  * (::String) — Optional. The field on the resource that designates the resource name field. If omitted, this is assumed to be "name". 



### #name_field=
    
    
    def name_field=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The field on the resource that designates the resource name field. If omitted, this is assumed to be "name". 



**Returns**

  * (::String) — Optional. The field on the resource that designates the resource name field. If omitted, this is assumed to be "name". 



### #pattern
    
    
    def pattern() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Optional. The relative resource name pattern associated with this resource type. The DNS prefix of the full resource name shouldn't be specified here.

The path pattern must follow the syntax, which aligns with HTTP binding syntax:
        
        Template = Segment { "/" Segment } ;
        Segment = LITERAL | Variable ;
        Variable = "{" LITERAL "}" ;
        

Examples:
        
        - "projects/\\{project}/topics/\\{topic}"
        - "projects/\\{project}/knowledgeBases/\\{knowledge_base}"
        

The components in braces correspond to the IDs for each resource in the hierarchy. It is expected that, if multiple patterns are provided, the same component name (e.g. "project") refers to IDs of the same type of resource. 




### #pattern=
    
    
    def pattern=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Optional. The relative resource name pattern associated with this resource type. The DNS prefix of the full resource name shouldn't be specified here.

The path pattern must follow the syntax, which aligns with HTTP binding syntax:
        
        Template = Segment { "/" Segment } ;
        Segment = LITERAL | Variable ;
        Variable = "{" LITERAL "}" ;
        

Examples:
        
        - "projects/\\{project}/topics/\\{topic}"
        - "projects/\\{project}/knowledgeBases/\\{knowledge_base}"
        

The components in braces correspond to the IDs for each resource in the hierarchy. It is expected that, if multiple patterns are provided, the same component name (e.g. "project") refers to IDs of the same type of resource. 




**Returns**

  * (::Array<::String>) — Optional. The relative resource name pattern associated with this resource type. The DNS prefix of the full resource name shouldn't be specified here.

The path pattern must follow the syntax, which aligns with HTTP binding syntax:
        
        Template = Segment { "/" Segment } ;
        Segment = LITERAL | Variable ;
        Variable = "{" LITERAL "}" ;
        

Examples:
        
        - "projects/\\{project}/topics/\\{topic}"
        - "projects/\\{project}/knowledgeBases/\\{knowledge_base}"
        

The components in braces correspond to the IDs for each resource in the hierarchy. It is expected that, if multiple patterns are provided, the same component name (e.g. "project") refers to IDs of the same type of resource. 




### #plural
    
    
    def plural() -> ::String

**Returns**

  * (::String) — The plural name used in the resource name and permission names, such as 'projects' for the resource name of 'projects/{project}' and the permission name of 'cloudresourcemanager.googleapis.com/projects.get'. One exception to this is for Nested Collections that have stuttering names, as defined in [AIP-122](https://google.aip.dev/122#nested-collections), where the collection ID in the resource name pattern does not necessarily directly match the `plural` value.

It is the same concept of the `plural` field in k8s CRD spec https://kubernetes.io/docs/tasks/access-kubernetes-api/custom-resources/custom-resource-definitions/

Note: The plural form is required even for singleton resources. See https://aip.dev/156 




### #plural=
    
    
    def plural=(value) -> ::String

**Parameter**

  * **value** (::String) — The plural name used in the resource name and permission names, such as 'projects' for the resource name of 'projects/{project}' and the permission name of 'cloudresourcemanager.googleapis.com/projects.get'. One exception to this is for Nested Collections that have stuttering names, as defined in [AIP-122](https://google.aip.dev/122#nested-collections), where the collection ID in the resource name pattern does not necessarily directly match the `plural` value.

It is the same concept of the `plural` field in k8s CRD spec https://kubernetes.io/docs/tasks/access-kubernetes-api/custom-resources/custom-resource-definitions/

Note: The plural form is required even for singleton resources. See https://aip.dev/156 




**Returns**

  * (::String) — The plural name used in the resource name and permission names, such as 'projects' for the resource name of 'projects/{project}' and the permission name of 'cloudresourcemanager.googleapis.com/projects.get'. One exception to this is for Nested Collections that have stuttering names, as defined in [AIP-122](https://google.aip.dev/122#nested-collections), where the collection ID in the resource name pattern does not necessarily directly match the `plural` value.

It is the same concept of the `plural` field in k8s CRD spec https://kubernetes.io/docs/tasks/access-kubernetes-api/custom-resources/custom-resource-definitions/

Note: The plural form is required even for singleton resources. See https://aip.dev/156 




### #singular
    
    
    def singular() -> ::String

**Returns**

  * (::String) — The same concept of the `singular` field in k8s CRD spec https://kubernetes.io/docs/tasks/access-kubernetes-api/custom-resources/custom-resource-definitions/ Such as "project" for the `resourcemanager.googleapis.com/Project` type. 



### #singular=
    
    
    def singular=(value) -> ::String

**Parameter**

  * **value** (::String) — The same concept of the `singular` field in k8s CRD spec https://kubernetes.io/docs/tasks/access-kubernetes-api/custom-resources/custom-resource-definitions/ Such as "project" for the `resourcemanager.googleapis.com/Project` type. 



**Returns**

  * (::String) — The same concept of the `singular` field in k8s CRD spec https://kubernetes.io/docs/tasks/access-kubernetes-api/custom-resources/custom-resource-definitions/ Such as "project" for the `resourcemanager.googleapis.com/Project` type. 



### #style
    
    
    def style() -> ::Array<::Google::Api::ResourceDescriptor::Style>

**Returns**

  * (::Array<[::Google::Api::ResourceDescriptor::Style](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Api-ResourceDescriptor-Style)>) — Style flag(s) for this resource. These indicate that a resource is expected to conform to a given style. See the specific style flags for additional information. 



### #style=
    
    
    def style=(value) -> ::Array<::Google::Api::ResourceDescriptor::Style>

**Parameter**

  * **value** (::Array<[::Google::Api::ResourceDescriptor::Style](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Api-ResourceDescriptor-Style)>) — Style flag(s) for this resource. These indicate that a resource is expected to conform to a given style. See the specific style flags for additional information. 



**Returns**

  * (::Array<[::Google::Api::ResourceDescriptor::Style](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Api-ResourceDescriptor-Style)>) — Style flag(s) for this resource. These indicate that a resource is expected to conform to a given style. See the specific style flags for additional information. 



### #type
    
    
    def type() -> ::String

**Returns**

  * (::String) — The resource type. It must be in the format of {service_name}/{resource_type_kind}. The `resource_type_kind` must be singular and must not include version numbers.

Example: `storage.googleapis.com/Bucket`

The value of the resource_type_kind must follow the regular expression /[A-Za-z][a-zA-Z0-9]+/. It should start with an upper case character and should use PascalCase (UpperCamelCase). The maximum number of characters allowed for the `resource_type_kind` is 100. 




### #type=
    
    
    def type=(value) -> ::String

**Parameter**

  * **value** (::String) — The resource type. It must be in the format of {service_name}/{resource_type_kind}. The `resource_type_kind` must be singular and must not include version numbers.

Example: `storage.googleapis.com/Bucket`

The value of the resource_type_kind must follow the regular expression /[A-Za-z][a-zA-Z0-9]+/. It should start with an upper case character and should use PascalCase (UpperCamelCase). The maximum number of characters allowed for the `resource_type_kind` is 100. 




**Returns**

  * (::String) — The resource type. It must be in the format of {service_name}/{resource_type_kind}. The `resource_type_kind` must be singular and must not include version numbers.

Example: `storage.googleapis.com/Bucket`

The value of the resource_type_kind must follow the regular expression /[A-Za-z][a-zA-Z0-9]+/. It should start with an upper case character and should use PascalCase (UpperCamelCase). The maximum number of characters allowed for the `resource_type_kind` is 100. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
