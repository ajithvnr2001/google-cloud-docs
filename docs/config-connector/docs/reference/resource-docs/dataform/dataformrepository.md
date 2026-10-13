---
url: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/dataform/dataformrepository/
title: DataformRepository \u00a0|\u00a0 Config Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:53:06.387601+00:00
---

# DataformRepository  |  Config Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/dataform/dataformrepository/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ API and reference ](https://docs.cloud.google.com/config-connector/docs/reference/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# DataformRepository

**Property** | **Value**  
---|---  
Google Cloud Service Name | Dataform  
Google Cloud Service Documentation | [/dataform/docs/](https://docs.cloud.google.com/dataform/docs)  
Google Cloud REST Resource Name | v1beta1.projects.locations.repositories  
Google Cloud REST Resource Documentation | [/dataform/reference/rest/v1beta1/projects.locations.repositories](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories)  
Config Connector Resource Short Names | dataformrepository  
gcpdataformrepositories  
gcpdataformrepository  
Config Connector Service Name | dataform.googleapis.com  
Config Connector Resource Fully Qualified Name | dataformrepositories.dataform.cnrm.cloud.google.com  
Can Be Referenced by IAMPolicy/IAMPolicyMember | No  
Config Connector Default Average Reconcile Interval In Seconds | 600  
  
## Custom Resource Definition Properties

### Spec

#### Schema
    
    
    displayName: string
    gitRemoteSettings:
      authenticationTokenSecretVersionRef:
        external: string
        name: string
        namespace: string
      defaultBranch: string
      sshAuthenticationConfig:
        hostPublicKey: string
        userPrivateKeySecretVersionRef:
          external: string
          name: string
          namespace: string
      url: string
    npmrcEnvironmentVariablesSecretVersionRef:
      external: string
      name: string
      namespace: string
    projectRef:
      external: string
      kind: string
      name: string
      namespace: string
    region: string
    resourceID: string
    serviceAccountRef:
      external: string
      name: string
      namespace: string
    setAuthenticatedUserAdmin: boolean
    workspaceCompilationOverrides:
      defaultDatabase: string
      schemaSuffix: string
      tablePrefix: string
    

Fields  
---  
`displayName` _Optional_ |  `string` Optional. The repository's user-friendly name.  
`gitRemoteSettings` _Optional_ |  `object` Optional. If set, configures this repository to be linked to a Git remote.  
`gitRemoteSettings.authenticationTokenSecretVersionRef` _Optional_ |  `object` The name of the Secret Manager secret version to use as an authentication token for Git operations. Must be in the format projects/* /secrets/* /versions/*.  
`gitRemoteSettings.authenticationTokenSecretVersionRef.external` _Optional_ |  `string` If provided must be in the format `projects/*/secrets/*/versions/*`.  
`gitRemoteSettings.authenticationTokenSecretVersionRef.name` _Optional_ |  `string` The `name` field of a `SecretManagerSecretVersion` resource.  
`gitRemoteSettings.authenticationTokenSecretVersionRef.namespace` _Optional_ |  `string` The `metadata.namespace` field of a `SecretManagerSecretVersion` resource.  
`gitRemoteSettings.defaultBranch` _Required*_ |  `string` The Git remote's default branch name.  
`gitRemoteSettings.sshAuthenticationConfig` _Optional_ |  `object` Authentication fields for remote uris using SSH protocol.  
`gitRemoteSettings.sshAuthenticationConfig.hostPublicKey` _Required*_ |  `string` Content of a public SSH key to verify an identity of a remote Git host.  
`gitRemoteSettings.sshAuthenticationConfig.userPrivateKeySecretVersionRef` _Required*_ |  `object` The name of the Secret Manager secret version to use as a ssh private key for Git operations. Must be in the format projects/*/secrets/*/versions/* .  
`gitRemoteSettings.sshAuthenticationConfig.userPrivateKeySecretVersionRef.external` _Optional_ |  `string` If provided must be in the format `projects/*/secrets/*/versions/*`.  
`gitRemoteSettings.sshAuthenticationConfig.userPrivateKeySecretVersionRef.name` _Optional_ |  `string` The `name` field of a `SecretManagerSecretVersion` resource.  
`gitRemoteSettings.sshAuthenticationConfig.userPrivateKeySecretVersionRef.namespace` _Optional_ |  `string` The `metadata.namespace` field of a `SecretManagerSecretVersion` resource.  
`gitRemoteSettings.url` _Required*_ |  `string` The Git remote's URL.  
`npmrcEnvironmentVariablesSecretVersionRef` _Optional_ |  `object` Optional. The name of the Secret Manager secret version to be used to interpolate variables into the .npmrc file for package installation operations.  
`npmrcEnvironmentVariablesSecretVersionRef.external` _Optional_ |  `string` If provided must be in the format `projects/*/secrets/*/versions/*`.  
`npmrcEnvironmentVariablesSecretVersionRef.name` _Optional_ |  `string` The `name` field of a `SecretManagerSecretVersion` resource.  
`npmrcEnvironmentVariablesSecretVersionRef.namespace` _Optional_ |  `string` The `metadata.namespace` field of a `SecretManagerSecretVersion` resource.  
`projectRef` _Required_ |  `object` The project that this resource belongs to.  
`projectRef.external` _Optional_ |  `string` The `projectID` field of a project, when not managed by Config Connector.  
`projectRef.kind` _Optional_ |  `string` The kind of the Project resource; optional but must be `Project` if provided.  
`projectRef.name` _Optional_ |  `string` The `name` field of a `Project` resource.  
`projectRef.namespace` _Optional_ |  `string` The `namespace` field of a `Project` resource.  
`region` _Required_ |  `string` Immutable. A reference to the region.  
`resourceID` _Optional_ |  `string` Immutable. Optional. The name of the resource. Used for creation and acquisition. When unset, the value of `metadata.name` is used as the default.  
`serviceAccountRef` _Optional_ |  `object` Optional. The service account reference to run workflow invocations under.  
`serviceAccountRef.external` _Optional_ |  `string` The `email` field of an `IAMServiceAccount` resource.  
`serviceAccountRef.name` _Optional_ |  `string` Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names  
`serviceAccountRef.namespace` _Optional_ |  `string` Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/  
`setAuthenticatedUserAdmin` _Optional_ |  `boolean` Optional. Input only. If set to true, the authenticated user will be granted the roles/dataform.admin role on the created repository.  
`workspaceCompilationOverrides` _Optional_ |  `object` Optional. If set, fields of workspaceCompilationOverrides override the default compilation settings that are specified in dataform.json when creating workspace-scoped compilation results.  
`workspaceCompilationOverrides.defaultDatabase` _Optional_ |  `string` Optional. The default database (Google Cloud project ID).  
`workspaceCompilationOverrides.schemaSuffix` _Optional_ |  `string` Optional. The suffix that should be appended to all schema (BigQuery dataset ID) names.  
`workspaceCompilationOverrides.tablePrefix` _Optional_ |  `string` Optional. The prefix that should be prepended to all table names.  
  
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
    observedState: {}
    

Fields  
---  
`conditions` |  `list (object)` Conditions represent the latest available observations of the DataformRepository's current state.  
`conditions[]` |  `object`  
`conditions[].lastTransitionTime` |  `string` Last time the condition transitioned from one status to another.  
`conditions[].message` |  `string` Human-readable message indicating details about last transition.  
`conditions[].reason` |  `string` Unique, one-word, CamelCase reason for the condition's last transition.  
`conditions[].status` |  `string` Status is the status of the condition. Can be True, False, Unknown.  
`conditions[].type` |  `string` Type is the type of the condition.  
`externalRef` |  `string` A unique specifier for the DataformReposity resource in Google Cloud.  
`observedGeneration` |  `integer` ObservedGeneration is the generation of the resource that was most recently observed by the Config Connector controller. If this is equal to metadata.generation, then that means that the current reported status reflects the most recent desired state of the resource.  
`observedState` |  `object` ObservedState is the state of the resource as most recently observed in Google Cloud.  
  
## Sample YAML(s)

### Typical Use Case
    
    
    # Copyright 2024 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #      http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    apiVersion: dataform.cnrm.cloud.google.com/v1beta1
    kind: DataformRepository
    metadata:
      name: dataformrepository-sample
    spec:
      projectRef:
        external: ${PROJECT_ID?}
      region: us-west2
    

**Note:** If you have any trouble with instantiating the resource, refer to [Troubleshoot Config Connector](https://docs.cloud.google.com/config-connector/docs/troubleshooting).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
