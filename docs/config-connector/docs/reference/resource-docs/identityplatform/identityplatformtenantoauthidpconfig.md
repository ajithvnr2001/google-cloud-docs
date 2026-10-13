---
url: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/identityplatform/identityplatformtenantoauthidpconfig/
title: IdentityPlatformTenantOAuthIDPConfig \u00a0|\u00a0 Config Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:19:02.569364+00:00
---

# IdentityPlatformTenantOAuthIDPConfig  |  Config Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/identityplatform/identityplatformtenantoauthidpconfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ API and reference ](https://docs.cloud.google.com/config-connector/docs/reference/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# IdentityPlatformTenantOAuthIDPConfig

**Note:** You must enable the Google Identity Platform in the marketplace prior to using this resource.**Note:** You must specify the resource's name in `metadata.name` or `spec.resourceID` starting with "oidc.".**Property** | **Value**  
---|---  
Google Cloud Service Name | Identity Platform  
Google Cloud Service Documentation | [/identity-platform/docs/](https://docs.cloud.google.com/identity-platform/docs)  
Google Cloud REST Resource Name | v2.projects.tenants.oauthIdpConfigs  
Google Cloud REST Resource Documentation | [/identity-platform/docs/reference/rest/v2/projects.tenants.oauthIdpConfigs](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants.oauthIdpConfigs)  
Config Connector Resource Short Names | IdentityPlatformTenantOAuthIDPConfig  
gcpidentityplatformtenantoauthidpconfig  
gcpidentityplatformtenantoauthidpconfigs  
identityplatformtenantoauthidpconfig  
Config Connector Service Name | identitytoolkit.googleapis.com  
Config Connector Resource Fully Qualified Name | identityplatformtenantoauthidpconfigs.identityplatform.cnrm.cloud.google.com  
Can Be Referenced by IAMPolicy/IAMPolicyMember | No  
Config Connector Default Average Reconcile Interval In Seconds | 600  
  
## Custom Resource Definition Properties

### Annotations

Fields  
---  
`cnrm.cloud.google.com/project-id`  
  
### Spec

#### Schema
    
    
    clientId: string
    clientSecret:
      value: string
      valueFrom:
        secretKeyRef:
          key: string
          name: string
    displayName: string
    enabled: boolean
    issuer: string
    resourceID: string
    responseType:
      code: boolean
      idToken: boolean
      token: boolean
    tenantRef:
      external: string
      name: string
      namespace: string
    

Fields  
---  
`clientId` _Optional_ |  `string` The client id of an OAuth client.  
`clientSecret` _Optional_ |  `object` The client secret of the OAuth client, to enable OIDC code flow.  
`clientSecret.value` _Optional_ |  `string` Value of the field. Cannot be used if 'valueFrom' is specified.  
`clientSecret.valueFrom` _Optional_ |  `object` Source for the field's value. Cannot be used if 'value' is specified.  
`clientSecret.valueFrom.secretKeyRef` _Optional_ |  `object` Reference to a value with the given key in the given Secret in the resource's namespace.  
`clientSecret.valueFrom.secretKeyRef.key` _Required*_ |  `string` Key that identifies the value to be extracted.  
`clientSecret.valueFrom.secretKeyRef.name` _Required*_ |  `string` Name of the Secret to extract a value from.  
`displayName` _Optional_ |  `string` The config's display name set by developers.  
`enabled` _Optional_ |  `boolean` True if allows the user to sign in with the provider.  
`issuer` _Optional_ |  `string` For OIDC Idps, the issuer identifier.  
`resourceID` _Optional_ |  `string` Immutable. Optional. The name of the resource. Used for creation and acquisition. When unset, the value of `metadata.name` is used as the default.  
`responseType` _Optional_ |  `object` The multiple response type to request for in the OAuth authorization flow. This can possibly be a combination of set bits (e.g.: {id\\_token, token}).  
`responseType.code` _Optional_ |  `boolean` If true, authorization code is returned from IdP's authorization endpoint.  
`responseType.idToken` _Optional_ |  `boolean` If true, ID token is returned from IdP's authorization endpoint.  
`responseType.token` _Optional_ |  `boolean` If true, access token is returned from IdP's authorization endpoint.  
`tenantRef` _Required_ |  `object` Immutable.  
`tenantRef.external` _Optional_ |  `string` The tenant for the resource Allowed value: The Google Cloud resource name of an `IdentityPlatformTenant` resource (format: `projects/{{project}}/tenants/{{name}}`).  
`tenantRef.name` _Optional_ |  `string` Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names  
`tenantRef.namespace` _Optional_ |  `string` Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/  
  
* Field is required when parent field is specified

### Status

#### Schema
    
    
    conditions:
    - lastTransitionTime: string
      message: string
      reason: string
      status: string
      type: string
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
`observedGeneration` |  `integer` ObservedGeneration is the generation of the resource that was most recently observed by the Config Connector controller. If this is equal to metadata.generation, then that means that the current reported status reflects the most recent desired state of the resource.  
  
## Sample YAML(s)

### Typical Use Case
    
    
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
    
    apiVersion: identityplatform.cnrm.cloud.google.com/v1beta1
    kind: IdentityPlatformTenantOAuthIDPConfig
    metadata:
      labels:
        foo: bar
      name: identityplatformtenantoauthidpconfig-sample
    spec:
      resourceID: "oidc.tenant-oauth-idp-config-sample" # Must start with 'oidc.'
      tenantRef:
        name: identityplatformtenantoauthidpconfig-dep
      displayName: "sample tenant oauth idp config"
      clientId: "client-id"
      issuer: "issuer"
      enabled: true
      clientSecret:
        valueFrom:
          secretKeyRef:
            key: clientSecret
            name: identityplatformtenantoauthidpconfig-dep
    ---
    apiVersion: identityplatform.cnrm.cloud.google.com/v1beta1
    kind: IdentityPlatformTenant
    metadata:
      name: identityplatformtenantoauthidpconfig-dep
    spec:
      displayName: "test-tenant"
      allowPasswordSignup: true
      enableAnonymousUser: false
      mfaConfig:
        state: "ENABLED"
      testPhoneNumbers:
        "+12345678901": "123451"
        "+16505550000": "123450"
    ---
    apiVersion: v1
    kind: Secret
    metadata:
      name: identityplatformtenantoauthidpconfig-dep
    stringData:
      clientSecret: "secret1"
    

**Note:** If you have any trouble with instantiating the resource, refer to [Troubleshoot Config Connector](https://docs.cloud.google.com/config-connector/docs/troubleshooting).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
