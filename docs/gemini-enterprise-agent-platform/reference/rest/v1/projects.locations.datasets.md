---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.datasets
title: REST Resource: projects.locations.datasets \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:20:02.681927+00:00
---

# REST Resource: projects.locations.datasets  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.datasets

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  REST Resource: projects.locations.datasets Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: Dataset

A collection of DataItems and Annotations on them.

Fields  
  
`name` `string` Output only. Identifier. The resource name of the Dataset. Format: `projects/{project}/locations/{location}/datasets/{dataset}` | `displayName` `string` Required. The user-defined name of the Dataset. The name can be up to 128 characters long and can consist of any UTF-8 characters. | `description` `string` The description of the Dataset. | `metadataSchemaUri` `string` Required. Points to a YAML file stored on Google Cloud Storage describing additional information about the Dataset. The schema is defined as an OpenAPI 3.0.2 Schema Object. The schema files that can be used here are found in gs://google-cloud-aiplatform/schema/dataset/metadata/. | `metadata` `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` Required. Additional information about the Dataset. | `dataItemCount` `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The number of DataItems in this Dataset. Only apply for non-structured Dataset. | `createTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. timestamp when this Dataset was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `updateTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. timestamp when this Dataset was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `etag` `string` Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens. | `labels` `map (key: string, value: string)` The labels with user-defined metadata to organize your Datasets.label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one Dataset (System labels are excluded).See <https://goo.gl/xmQnxf> for more information and examples of labels. System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable. Following system labels exist for each Dataset:

  * "aiplatform.googleapis.com/dataset_metadata_schema": output only, its value is the `[metadataSchema's](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.datasets#Dataset.FIELDS.metadata_schema_uri)` title.

| `savedQueries[]` `object (`[SavedQuery](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.datasets#SavedQuery)`)` All SavedQueries belong to the Dataset will be returned in List/Get Dataset response. The annotationSpecs field will not be populated except for UI cases which will only use `[annotationSpecCount](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.datasets#SavedQuery.FIELDS.annotation_spec_count)`. In datasets.create request, a SavedQuery is created together if this field is set, up to one SavedQuery can be set in CreateDatasetRequest. The SavedQuery should not contain any AnnotationSpec. | `encryptionSpec` `object (`[EncryptionSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/EncryptionSpec)`)` Customer-managed encryption key spec for a Dataset. If set, this Dataset and all sub-resources of this Dataset will be secured by this key. | `metadataArtifact` `string` Output only. The resource name of the Artifact that was created in MetadataStore when creating the Dataset. The Artifact resource name pattern is `projects/{project}/locations/{location}/metadataStores/{metadataStore}/artifacts/{artifact}`. | `modelReference` `string` Optional. Reference to the public base model last used by the dataset. Only set for prompt datasets. | `satisfiesPzs` `boolean` Output only. reserved for future use. | `satisfiesPzi` `boolean` Output only. reserved for future use. | JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "metadataSchemaUri": string,
      "metadata": value,
      "dataItemCount": string,
      "createTime": string,
      "updateTime": string,
      "etag": string,
      "labels": {
        string: string,
        ...
      },
      "savedQueries": [
        {
          object ([SavedQuery](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.datasets#SavedQuery))
        }
      ],
      "encryptionSpec": {
        object ([EncryptionSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/EncryptionSpec))
      },
      "metadataArtifact": string,
      "modelReference": string,
      "satisfiesPzs": boolean,
      "satisfiesPzi": boolean
    }  
  
## SavedQuery

A SavedQuery is a view of the dataset. It references a subset of annotations by problem type and filters.

Fields  
  
`name` `string` Output only. Resource name of the SavedQuery. | `displayName` `string` Required. The user-defined name of the SavedQuery. The name can be up to 128 characters long and can consist of any UTF-8 characters. | `metadata` `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` Some additional information about the SavedQuery. | `createTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. timestamp when this SavedQuery was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `updateTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. timestamp when SavedQuery was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `annotationFilter` `string` Output only. Filters on the Annotations in the dataset. | `problemType` `string` Required. Problem type of the SavedQuery. Allowed values:

  * IMAGE_CLASSIFICATION_SINGLE_LABEL
  * IMAGE_CLASSIFICATION_MULTI_LABEL
  * IMAGE_BOUNDING_POLY
  * IMAGE_BOUNDING_BOX
  * TEXT_CLASSIFICATION_SINGLE_LABEL
  * TEXT_CLASSIFICATION_MULTI_LABEL
  * TEXT_EXTRACTION
  * TEXT_SENTIMENT
  * VIDEO_CLASSIFICATION
  * VIDEO_OBJECT_TRACKING

| `annotationSpecCount` `integer` Output only. Number of AnnotationSpecs in the context of the SavedQuery. | `etag` `string` Used to perform a consistent read-modify-write update. If not set, a blind "overwrite" update happens. | `supportAutomlTraining` `boolean` Output only. If the Annotations belonging to the SavedQuery can be used for AutoML training. | JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "metadata": value,
      "createTime": string,
      "updateTime": string,
      "annotationFilter": string,
      "problemType": string,
      "annotationSpecCount": integer,
      "etag": string,
      "supportAutomlTraining": boolean
    }  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.datasets/create)`

|  Creates a Dataset.  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.datasets/delete)`

|  Deletes a Dataset.  
  
### `[export](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.datasets/export)`

|  Exports data from a Dataset.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.datasets/get)`

|  Gets a Dataset.  
  
### `[import](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.datasets/import)`

|  Imports data into a Dataset.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.datasets/list)`

|  Lists Datasets in a Location.  
  
### `[patch](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.datasets/patch)`

|  Updates a Dataset.  
  
### `[searchDataItems](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.datasets/searchDataItems)`

|  Searches DataItems in a Dataset.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-06 UTC."],[],[]] 
