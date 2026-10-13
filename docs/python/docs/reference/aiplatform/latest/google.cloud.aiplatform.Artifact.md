---
url: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.Artifact
title: Class Artifact (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:26:24.792903+00:00
---

# Class Artifact (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.Artifact

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Artifact (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0  1.153.1  1.152.0  1.151.0  1.150.0  1.149.0  1.148.1  1.147.0  1.146.0  1.145.0  1.144.0  1.143.0  1.142.0  1.141.0  1.140.0  1.139.0  1.138.0  1.137.0  1.136.0  1.135.0  1.134.0  1.133.0  1.132.0  1.131.0  1.130.0  1.129.0  1.122.0  1.121.0  1.120.0  1.119.0  1.118.0  1.117.0  1.116.0  1.115.0  1.114.0  1.113.0  1.112.0  1.111.0  1.110.0  1.109.0  1.108.0  1.107.0  1.106.0  1.105.0  1.104.0  1.103.0  1.102.0  1.101.0  1.100.0  1.99.0  1.98.0  1.97.0  1.96.0  1.95.1  1.94.0  1.93.1  1.92.0  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.1  1.70.0  1.69.0  1.68.0  1.67.1  1.66.0  1.65.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.1  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.39.0  1.38.1  1.37.0  1.36.4  1.35.0  1.34.0  1.33.1  1.32.0  1.31.1  1.30.1  1.29.0  1.28.1  1.27.1  1.26.1  1.25.0  1.24.1  1.23.0  1.22.1  1.21.0  1.20.0  1.19.1  1.18.3  1.17.1  1.16.1  1.15.1  1.14.0  1.13.1  1.12.1  1.11.0  1.10.0  1.9.0  1.8.1  1.7.1  1.6.2  1.5.0  1.4.3  1.3.0  1.2.0  1.1.1  1.0.1  0.9.0  0.8.0  0.7.1  0.6.0  0.5.1  0.4.0  0.3.1 
    
    
    Artifact(
        artifact_name: str,
        *,
        metadata_store_id: str = "default",
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None
    )

Metadata Artifact resource for Vertex AI

## Properties 

### create_time

Time this resource was created.

### display_name

Display name of this resource.

### encryption_spec

Customer-managed encryption key options for this Vertex AI resource.

If this is set, then all resources created by this Vertex AI resource will be encrypted with the provided encryption key.

### gca_resource

The underlying resource proto representation.

### labels

User-defined labels containing metadata about this resource.

Read more about labels at <https://goo.gl/xmQnxf>

### lineage_console_uri

Cloud console uri to view this Artifact Lineage.

### name

Name of this resource.

### resource_name

Full qualified resource name.

### state

The State for this Artifact.

### update_time

Time this resource was last updated.

### uri

Uri for this Artifact.

## Methods 

### Artifact
    
    
    Artifact(
        artifact_name: str,
        *,
        metadata_store_id: str = "default",
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None
    )

Retrieves an existing Metadata Artifact given a resource name or ID.

**Parameters**  
---  
**Name** | **Description**  
`artifact_name` |  `str`   
Required. A fully-qualified resource name or resource ID of the Artifact. Example: "projects/123/locations/us-central1/metadataStores/default/artifacts/my-resource". or "my-resource" when project and location are initialized or passed.  
`metadata_store_id` |  `str`   
Optional. MetadataStore to retrieve Artifact from. If not set, metadata_store_id is set to "default". If artifact_name is a fully-qualified resource, its metadata_store_id overrides this one.  
`project` |  `str`   
Optional. Project to retrieve the artifact from. If not set, project set in aiplatform.init will be used.  
`location` |  `str`   
Optional. Location to retrieve the Artifact from. If not set, location set in aiplatform.init will be used.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials to use to retrieve this Artifact. Overrides credentials set in aiplatform.init.  
  
### create
    
    
    create(
        schema_title: str,
        *,
        resource_id: typing.Optional[str] = None,
        uri: typing.Optional[str] = None,
        display_name: typing.Optional[str] = None,
        schema_version: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict] = None,
        state: google.cloud.aiplatform_v1.types.artifact.Artifact.State = State.LIVE,
        metadata_store_id: typing.Optional[str] = "default",
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None
    ) -> google.cloud.aiplatform.metadata.artifact.Artifact

Creates a new Metadata Artifact.

**Parameters**  
---  
**Name** | **Description**  
`schema_title` |  `str`   
Required. schema_title identifies the schema title used by the Artifact. Please reference <https://cloud.google.com/vertex-ai/docs/ml-metadata/system-schemas>.  
`resource_id` |  `str`   
Optional. The <resource_id> portion of the Artifact name with the format. This is globally unique in a metadataStore: projects/123/locations/us-central1/metadataStores/<metadata_store_id>/artifacts/<resource_id>.  
`uri` |  `str`   
Optional. The uniform resource identifier of the artifact file. May be empty if there is no actual artifact file.  
`display_name` |  `str`   
Optional. The user-defined name of the Artifact.  
`schema_version` |  `str`   
Optional. schema_version specifies the version used by the Artifact. If not set, defaults to use the latest version.  
`description` |  `str`   
Optional. Describes the purpose of the Artifact to be created.  
`metadata` |  `Dict`   
Optional. Contains the metadata information that will be stored in the Artifact.  
`state` |  `google.cloud.gapic.types.Artifact.State`   
Optional. The state of this Artifact. This is a property of the Artifact, and does not imply or capture any ongoing process. This property is managed by clients (such as Vertex AI Pipelines), and the system does not prescribe or check the validity of state transitions.  
`metadata_store_id` |  `str`   
Optional. The <metadata_store_id> portion of the resource name with the format: projects/123/locations/us-central1/metadataStores/<metadata_store_id>/artifacts/<resource_id> If not provided, the MetadataStore's ID will be set to "default".  
`project` |  `str`   
Optional. Project used to create this Artifact. Overrides project set in aiplatform.init.  
`location` |  `str`   
Optional. Location used to create this Artifact. Overrides location set in aiplatform.init.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials used to create this Artifact. Overrides credentials set in aiplatform.init.  
**Returns**  
---  
**Type** | **Description**  
`Artifact` | Instantiated representation of the managed Metadata Artifact.  
  
### delete
    
    
    delete(sync: bool = True) -> None

Deletes this Vertex AI resource. WARNING: This deletion is permanent.

### get
    
    
    get(
        resource_id: str,
        metadata_store_id: str = "default",
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    ) -> google.cloud.aiplatform.metadata.resource._Resource

Retrieves a Metadata resource.

**Parameters**  
---  
**Name** | **Description**  
`resource_id` |  `str`   
Required. The <resource_id> portion of the resource name with the format: projects/123/locations/us-central1/metadataStores/<metadata_store_id>/<resource_noun>/<resource_id>.  
`metadata_store_id` |  `str`   
The <metadata_store_id> portion of the resource name with the format: projects/123/locations/us-central1/metadataStores/<metadata_store_id>/<resource_noun>/<resource_id> If not provided, the MetadataStore's ID will be set to "default".  
`project` |  `str`   
Project used to retrieve or create this resource. Overrides project set in aiplatform.init.  
`location` |  `str`   
Location used to retrieve or create this resource. Overrides location set in aiplatform.init.  
`credentials` |  `auth_credentials.Credentials`   
Custom credentials used to retrieve or create this resource. Overrides credentials set in aiplatform.init.  
**Returns**  
---  
**Type** | **Description**  
`resource (_Resource)` | Instantiated representation of the managed Metadata resource or None if no resource was found.  
  
### get_or_create
    
    
    get_or_create(
        resource_id: str,
        schema_title: str,
        display_name: typing.Optional[str] = None,
        schema_version: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict] = None,
        metadata_store_id: str = "default",
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    ) -> google.cloud.aiplatform.metadata.resource._Resource

Retrieves or Creates (if it does not exist) a Metadata resource.

**Parameters**  
---  
**Name** | **Description**  
`resource_id` |  `str`   
Required. The <resource_id> portion of the resource name with the format: projects/123/locations/us-central1/metadataStores/<metadata_store_id>/<resource_noun>/<resource_id>.  
`schema_title` |  `str`   
Required. schema_title identifies the schema title used by the resource.  
`display_name` |  `str`   
Optional. The user-defined name of the resource.  
`schema_version` |  `str`   
Optional. schema_version specifies the version used by the resource. If not set, defaults to use the latest version.  
`description` |  `str`   
Optional. Describes the purpose of the resource to be created.  
`metadata` |  `Dict`   
Optional. Contains the metadata information that will be stored in the resource.  
`metadata_store_id` |  `str`   
The <metadata_store_id> portion of the resource name with the format: projects/123/locations/us-central1/metadataStores/<metadata_store_id>/<resource_noun>/<resource_id> If not provided, the MetadataStore's ID will be set to "default".  
`project` |  `str`   
Project used to retrieve or create this resource. Overrides project set in aiplatform.init.  
`location` |  `str`   
Location used to retrieve or create this resource. Overrides location set in aiplatform.init.  
`credentials` |  `auth_credentials.Credentials`   
Custom credentials used to retrieve or create this resource. Overrides credentials set in aiplatform.init.  
**Returns**  
---  
**Type** | **Description**  
`resource (_Resource)` | Instantiated representation of the managed Metadata resource.  
  
### get_with_uri
    
    
    get_with_uri(
        uri: str,
        *,
        metadata_store_id: typing.Optional[str] = "default",
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None
    ) -> google.cloud.aiplatform.metadata.artifact.Artifact

Get an Artifact by it's uri.

If more than one Artifact with this uri is in the metadata store then the Artifact with the latest create_time is returned.

**Parameters**  
---  
**Name** | **Description**  
`uri` |  `str`   
Required. Uri of the Artifact to retrieve.  
`metadata_store_id` |  `str`   
Optional. MetadataStore to retrieve Artifact from. If not set, metadata_store_id is set to "default". If artifact_name is a fully-qualified resource, its metadata_store_id overrides this one.  
`project` |  `str`   
Optional. Project to retrieve the artifact from. If not set, project set in aiplatform.init will be used.  
`location` |  `str`   
Optional. Location to retrieve the Artifact from. If not set, location set in aiplatform.init will be used.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials to use to retrieve this Artifact. Overrides credentials set in aiplatform.init.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If no Artifact exists with the provided uri.  
**Returns**  
---  
**Type** | **Description**  
`Artifact` | Artifact with given uri.  
  
### list
    
    
    list(
        filter: typing.Optional[str] = None,
        metadata_store_id: str = "default",
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        order_by: typing.Optional[str] = None,
    ) -> typing.List[google.cloud.aiplatform.metadata.resource._Resource]

List resources that match the list filter in target metadataStore.

**Parameters**  
---  
**Name** | **Description**  
`filter` |  `str`   
Optional. A query to filter available resources for matching results.  
`metadata_store_id` |  `str`   
The <metadata_store_id> portion of the resource name with the format: projects/123/locations/us-central1/metadataStores/<metadata_store_id>/<resource_noun>/<resource_id> If not provided, the MetadataStore's ID will be set to "default".  
`project` |  `str`   
Project used to create this resource. Overrides project set in aiplatform.init.  
`location` |  `str`   
Location used to create this resource. Overrides location set in aiplatform.init.  
`credentials` |  `auth_credentials.Credentials`   
Custom credentials used to create this resource. Overrides credentials set in aiplatform.init.  
`order_by` |  `str`   
Optional. How the list of messages is ordered. Specify the values to order by and an ordering operation. The default sorting order is ascending. To specify descending order for a field, users append a " desc" suffix; for example: "foo desc, bar". Subfields are specified with a `.` character, such as foo.bar. see <https://google.aip.dev/132#ordering> for more details.  
**Returns**  
---  
**Type** | **Description**  
`resources (sequence[_Resource])` | a list of managed Metadata resource.  
  
### sync_resource
    
    
    sync_resource()

Syncs local resource with the resource in metadata store.

### to_dict
    
    
    to_dict() -> typing.Dict[str, typing.Any]

Returns the resource proto as a dictionary.

### update
    
    
    update(
        metadata: typing.Optional[typing.Dict] = None,
        description: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        location: typing.Optional[str] = None,
    )

Updates an existing Metadata resource with new metadata.

**Parameters**  
---  
**Name** | **Description**  
`metadata` |  `Dict`   
Optional. metadata contains the updated metadata information.  
`description` |  `str`   
Optional. Description describes the resource to be updated.  
`credentials` |  `auth_credentials.Credentials`   
Custom credentials to use to update this resource. Overrides credentials set in aiplatform.init.  
  
### wait
    
    
    wait()

Helper method that blocks until all futures are complete.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
