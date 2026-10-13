---
url: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/bigqueryanalyticshub/bigqueryanalyticshublisting/
title: BigQueryAnalyticsHubListing \u00a0|\u00a0 Config Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:50:01.569540+00:00
---

# BigQueryAnalyticsHubListing  |  Config Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/bigqueryanalyticshub/bigqueryanalyticshublisting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ API and reference ](https://docs.cloud.google.com/config-connector/docs/reference/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# BigQueryAnalyticsHubListing

**Property** | **Value**  
---|---  
Google Cloud Service Name | Analytics Hub  
Google Cloud Service Documentation | [/bigquery/docs/query-overview](https://docs.cloud.google.com/bigquery/docs/query-overview)  
Google Cloud REST Resource Name | v1.projects.locations.dataExchanges.listings  
Google Cloud REST Resource Documentation | [/bigquery/docs/reference/analytics-hub/rest/v1/projects.locations.dataExchanges.listings](https://docs.cloud.google.com/bigquery/docs/reference/analytics-hub/rest/v1/projects.locations.dataExchanges.listings)  
Config Connector Resource Short Names | bigqueryanalyticshublisting  
gcpbigqueryanalyticshublisting  
gcpbigqueryanalyticshublistings  
Config Connector Service Name | analyticshub.googleapis.com  
Config Connector Resource Fully Qualified Name | bigqueryanalyticshublistings.bigqueryanalyticshub.cnrm.cloud.google.com  
Can Be Referenced by IAMPolicy/IAMPolicyMember | No  
Config Connector Default Average Reconcile Interval In Seconds | 600  
  
## Custom Resource Definition Properties

### Spec

#### Schema
    
    
    categories:
    - string
    dataExchangeRef:
      external: string
      name: string
      namespace: string
    dataProvider:
      name: string
      primaryContact: string
    description: string
    discoveryType: string
    displayName: string
    documentation: string
    location: string
    primaryContact: string
    projectRef:
      external: string
      kind: string
      name: string
      namespace: string
    publisher:
      name: string
      primaryContact: string
    requestAccess: string
    resourceID: string
    source:
      bigQueryDatasetSource:
        datasetRef:
          external: string
          name: string
          namespace: string
        restrictedExportPolicy:
          enabled: boolean
          restrictDirectTableAccess: boolean
          restrictQueryResult: boolean
        selectedResources:
        - tableRef:
            external: string
            name: string
            namespace: string
    

Fields  
---  
`categories` _Optional_ |  `list (string)` Optional. Categories of the listing. Up to two categories are allowed.  
`categories[]` _Optional_ |  `string`  
`dataExchangeRef` _Required*_ |  `object` BigQueryAnalyticsHubDataExchangeRef is a reference to a BigQueryAnalyticsHubDataExchange.  
`dataExchangeRef.external` _Optional_ |  `string` A reference to an externally managed BigQueryAnalyticsHubDataExchange resource. Should be in the format "projects/{{projectID}}/locations/{{location}}/dataExchanges/{{dataExchangeID}}".  
`dataExchangeRef.name` _Optional_ |  `string` The name of a BigQueryAnalyticsHubDataExchange resource.  
`dataExchangeRef.namespace` _Optional_ |  `string` The namespace of a BigQueryAnalyticsHubDataExchange resource.  
`dataProvider` _Optional_ |  `object` Optional. Details of the data provider who owns the source data.  
`dataProvider.name` _Optional_ |  `string` Optional. Name of the data provider.  
`dataProvider.primaryContact` _Optional_ |  `string` Optional. Email or URL of the data provider. Max Length: 1000 bytes.  
`description` _Optional_ |  `string` Optional. Short description of the listing. The description must contain only Unicode characters or tabs (HT), new lines (LF), carriage returns (CR), and page breaks (FF). Default value is an empty string. Max length: 2000 bytes.  
`discoveryType` _Optional_ |  `string` Optional. Type of discovery of the listing on the discovery page.  
`displayName` _Required*_ |  `string` Required. Human-readable display name of the listing. The display name must contain only Unicode letters, numbers (0-9), underscores (_), dashes (-), spaces ( ), ampersands (&) and can't start or end with spaces. Default value is an empty string. Max length: 63 bytes.  
`documentation` _Optional_ |  `string` Optional. Documentation describing the listing.  
`location` _Required*_ |  `string` Immutable. The name of the location this data exchange.  
`primaryContact` _Optional_ |  `string` Optional. Email or URL of the primary point of contact of the listing. Max Length: 1000 bytes.  
`projectRef` _Required*_ |  `object` The Project that this resource belongs to.  
`projectRef.external` _Optional_ |  `string` The `projectID` field of a project, when not managed by Config Connector.  
`projectRef.kind` _Optional_ |  `string` The kind of the Project resource; optional but must be `Project` if provided.  
`projectRef.name` _Optional_ |  `string` The `name` field of a `Project` resource.  
`projectRef.namespace` _Optional_ |  `string` The `namespace` field of a `Project` resource.  
`publisher` _Optional_ |  `object` Optional. Details of the publisher who owns the listing and who can share the source data.  
`publisher.name` _Optional_ |  `string` Optional. Name of the listing publisher.  
`publisher.primaryContact` _Optional_ |  `string` Optional. Email or URL of the listing publisher. Max Length: 1000 bytes.  
`requestAccess` _Optional_ |  `string` Optional. Email or URL of the request access of the listing. Subscribers can use this reference to request access. Max Length: 1000 bytes.  
`resourceID` _Optional_ |  `string` Immutable. The BigQueryAnalyticsHubDataExchangeListing name. If not given, the metadata.name will be used.  
`source` _Required*_ |  `object`  
`source.bigQueryDatasetSource` _Optional_ |  `object` One of the following fields must be set.  
`source.bigQueryDatasetSource.datasetRef` _Required*_ |  `object` Resource name of the dataset source for this listing. e.g. `projects/myproject/datasets/123`  
`source.bigQueryDatasetSource.datasetRef.external` _Optional_ |  `string` A reference to an externally-managed BigQueryDataset resource. Should be in the format "projects/{{projectID}}/datasets/{{datasetID}}".  
`source.bigQueryDatasetSource.datasetRef.name` _Optional_ |  `string` The name of a BigQueryDataset resource.  
`source.bigQueryDatasetSource.datasetRef.namespace` _Optional_ |  `string` The namespace of a BigQueryDataset resource.  
`source.bigQueryDatasetSource.restrictedExportPolicy` _Optional_ |  `object` Optional. If set, restricted export policy will be propagated and enforced on the linked dataset.  
`source.bigQueryDatasetSource.restrictedExportPolicy.enabled` _Optional_ |  `boolean` Optional. If true, enable restricted export.  
`source.bigQueryDatasetSource.restrictedExportPolicy.restrictDirectTableAccess` _Optional_ |  `boolean` Optional. If true, restrict direct table access (read api/tabledata.list) on linked table.  
`source.bigQueryDatasetSource.restrictedExportPolicy.restrictQueryResult` _Optional_ |  `boolean` Optional. If true, restrict export of query result derived from restricted linked dataset table.  
`source.bigQueryDatasetSource.selectedResources` _Optional_ |  `list (object)` Optional. Resources in this dataset that are selectively shared. If this field is empty, then the entire dataset (all resources) are shared. This field is only valid for data clean room exchanges.  
`source.bigQueryDatasetSource.selectedResources[]` _Optional_ |  `object`  
`source.bigQueryDatasetSource.selectedResources[].tableRef` _Optional_ |  `object` Optional. A reference to a BigQueryTable. Format: `projects/{projectId}/datasets/{datasetId}/tables/{tableId}` Example:"projects/test_project/datasets/test_dataset/tables/test_table"  
`source.bigQueryDatasetSource.selectedResources[].tableRef.external` _Optional_ |  `string` A reference to an externally-managed BigQueryTable resource. Should be in the format "projects/{{projectID}}/datasets/{{datasetID}}/tables/{{tableID}}".  
`source.bigQueryDatasetSource.selectedResources[].tableRef.name` _Optional_ |  `string` The name of a BigQueryTable resource.  
`source.bigQueryDatasetSource.selectedResources[].tableRef.namespace` _Optional_ |  `string` The namespace of a BigQueryTable resource.  
  
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
      state: string
    

Fields  
---  
`conditions` |  `list (object)` Conditions represent the latest available observations of the object's current state.  
`conditions[]` |  `object`  
`conditions[].lastTransitionTime` |  `string` Last time the condition transitioned from one status to another.  
`conditions[].message` |  `string` Human-readable message indicating details about last transition.  
`conditions[].reason` |  `string` Unique, one-word, CamelCase reason for the condition's last transition.  
`conditions[].status` |  `string` Status is the status of the condition. Can be True, False, Unknown.  
`conditions[].type` |  `string` Type is the type of the condition.  
`externalRef` |  `string` A unique specifier for the BigQueryAnalyticsHubDataExchangeListing resource in Google Cloud.  
`observedGeneration` |  `integer` ObservedGeneration is the generation of the resource that was most recently observed by the Config Connector controller. If this is equal to metadata.generation, then that means that the current reported status reflects the most recent desired state of the resource.  
`observedState` |  `object` ObservedState is the state of the resource as most recently observed in Google Cloud.  
`observedState.state` |  `string` Output only. Current state of the listing.  
  
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
    
    apiVersion: bigqueryanalyticshub.cnrm.cloud.google.com/v1beta1
    kind: BigQueryAnalyticsHubListing
    metadata:
      name: bigqueryanalyticshublistingsample
    spec:
      displayName: my_listing
      location: US
      source:
        bigQueryDatasetSource:
          datasetRef:
            name: bigqueryanalyticshublisting-dep
      dataExchangeRef:
        name: bigqueryanalyticshublistingdep
      projectRef:
        external: ${PROJECT_ID?}
    ---
    apiVersion: bigquery.cnrm.cloud.google.com/v1beta1
    kind: BigQueryDataset
    metadata:
      name: bigqueryanalyticshublisting-dep
    spec:
      friendlyName: my-bigquerydataset
    ---
    apiVersion: bigqueryanalyticshub.cnrm.cloud.google.com/v1beta1
    kind: BigQueryAnalyticsHubDataExchange
    metadata:
      name: bigqueryanalyticshublistingdep
    spec:
      displayName: my_data_exchange
      location: US
      projectRef:
        external: ${PROJECT_ID?}
    

**Note:** If you have any trouble with instantiating the resource, refer to [Troubleshoot Config Connector](https://docs.cloud.google.com/config-connector/docs/troubleshooting).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
