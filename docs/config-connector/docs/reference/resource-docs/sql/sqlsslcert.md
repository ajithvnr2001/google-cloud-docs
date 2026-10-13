---
url: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/sql/sqlsslcert/
title: SQLSSLCert \u00a0|\u00a0 Config Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:31:11.517930+00:00
---

# SQLSSLCert  |  Config Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/sql/sqlsslcert/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ API and reference ](https://docs.cloud.google.com/config-connector/docs/reference/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# SQLSSLCert

**Property** | **Value**  
---|---  
Google Cloud Service Name | Cloud SQL  
Google Cloud Service Documentation | [/sql/docs/](https://docs.cloud.google.com/sql/docs)  
Google Cloud REST Resource Name | v1beta4.sslCerts  
Google Cloud REST Resource Documentation | [/sql/docs/postgres/admin-api/rest/v1beta4/sslCerts](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/sslCerts)  
Config Connector Resource Short Names | gcpsqlsslcert  
gcpsqlsslcerts  
sqlsslcert  
Config Connector Service Name | sqladmin.googleapis.com  
Config Connector Resource Fully Qualified Name | sqlsslcerts.sql.cnrm.cloud.google.com  
Can Be Referenced by IAMPolicy/IAMPolicyMember | No  
Config Connector Default Average Reconcile Interval In Seconds | 600  
  
## Custom Resource Definition Properties

### Annotations

Fields  
---  
`cnrm.cloud.google.com/project-id`  
  
### Spec

#### Schema
    
    
    commonName: string
    instanceRef:
      external: string
      name: string
      namespace: string
    resourceID: string
    

Fields  
---  
`commonName` _Required_ |  `string` Immutable. The common name to be used in the certificate to identify the client. Constrained to [a-zA-Z.-_ ]+. Changing this forces a new resource to be created.  
`instanceRef` _Required_ |  `object` The Cloud SQL instance.  
`instanceRef.external` _Optional_ |  `string` Allowed value: The `name` field of a `SQLInstance` resource.  
`instanceRef.name` _Optional_ |  `string` Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names  
`instanceRef.namespace` _Optional_ |  `string` Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/  
`resourceID` _Optional_ |  `string` Immutable. Optional. The service-generated sha1Fingerprint of the resource. Used for acquisition only. Leave unset to create a new resource.  
  
### Status

#### Schema
    
    
    cert: string
    certSerialNumber: string
    conditions:
    - lastTransitionTime: string
      message: string
      reason: string
      status: string
      type: string
    createTime: string
    expirationTime: string
    observedGeneration: integer
    privateKey: string
    serverCaCert: string
    sha1Fingerprint: string
    

Fields  
---  
`cert` |  `string` The actual certificate data for this client certificate.  
`certSerialNumber` |  `string` The serial number extracted from the certificate data.  
`conditions` |  `list (object)` Conditions represent the latest available observation of the resource's current state.  
`conditions[]` |  `object`  
`conditions[].lastTransitionTime` |  `string` Last time the condition transitioned from one status to another.  
`conditions[].message` |  `string` Human-readable message indicating details about last transition.  
`conditions[].reason` |  `string` Unique, one-word, CamelCase reason for the condition's last transition.  
`conditions[].status` |  `string` Status is the status of the condition. Can be True, False, Unknown.  
`conditions[].type` |  `string` Type is the type of the condition.  
`createTime` |  `string` The time when the certificate was created in RFC 3339 format, for example 2012-11-15T16:19:00.094Z.  
`expirationTime` |  `string` The time when the certificate expires in RFC 3339 format, for example 2012-11-15T16:19:00.094Z.  
`observedGeneration` |  `integer` ObservedGeneration is the generation of the resource that was most recently observed by the Config Connector controller. If this is equal to metadata.generation, then that means that the current reported status reflects the most recent desired state of the resource.  
`privateKey` |  `string` The private key associated with the client certificate.  
`serverCaCert` |  `string` The CA cert of the server this client cert was generated from.  
`sha1Fingerprint` |  `string` The SHA1 Fingerprint of the certificate.  
  
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
    
    apiVersion: sql.cnrm.cloud.google.com/v1beta1
    kind: SQLSSLCert
    metadata:
      name: sqlsslcert-sample
    spec:
      instanceRef:
        name: sqlsslcert-dep
      commonName: "client-name"
    ---
    apiVersion: sql.cnrm.cloud.google.com/v1beta1
    kind: SQLInstance
    metadata:
      name: sqlsslcert-dep
    spec:
      databaseVersion: MYSQL_5_7
      region: us-central1
      settings:
        tier: db-f1-micro
    

**Note:** If you have any trouble with instantiating the resource, refer to [Troubleshoot Config Connector](https://docs.cloud.google.com/config-connector/docs/troubleshooting).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
