---
url: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.Feature
title: Class Feature (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:26:41.208441+00:00
---

# Class Feature (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.Feature

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Feature (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0  1.153.1  1.152.0  1.151.0  1.150.0  1.149.0  1.148.1  1.147.0  1.146.0  1.145.0  1.144.0  1.143.0  1.142.0  1.141.0  1.140.0  1.139.0  1.138.0  1.137.0  1.136.0  1.135.0  1.134.0  1.133.0  1.132.0  1.131.0  1.130.0  1.129.0  1.122.0  1.121.0  1.120.0  1.119.0  1.118.0  1.117.0  1.116.0  1.115.0  1.114.0  1.113.0  1.112.0  1.111.0  1.110.0  1.109.0  1.108.0  1.107.0  1.106.0  1.105.0  1.104.0  1.103.0  1.102.0  1.101.0  1.100.0  1.99.0  1.98.0  1.97.0  1.96.0  1.95.1  1.94.0  1.93.1  1.92.0  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.1  1.70.0  1.69.0  1.68.0  1.67.1  1.66.0  1.65.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.1  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.39.0  1.38.1  1.37.0  1.36.4  1.35.0  1.34.0  1.33.1  1.32.0  1.31.1  1.30.1  1.29.0  1.28.1  1.27.1  1.26.1  1.25.0  1.24.1  1.23.0  1.22.1  1.21.0  1.20.0  1.19.1  1.18.3  1.17.1  1.16.1  1.15.1  1.14.0  1.13.1  1.12.1  1.11.0  1.10.0  1.9.0  1.8.1  1.7.1  1.6.2  1.5.0  1.4.3  1.3.0  1.2.0  1.1.1  1.0.1  0.9.0  0.8.0  0.7.1  0.6.0  0.5.1  0.4.0  0.3.1 
    
    
    Feature(
        feature_name: str,
        featurestore_id: typing.Optional[str] = None,
        entity_type_id: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    )

Managed feature resource for Vertex AI.

## Properties 

### create_time

Time this resource was created.

### display_name

Display name of this resource.

### encryption_spec

Customer-managed encryption key options for this Vertex AI resource.

If this is set, then all resources created by this Vertex AI resource will be encrypted with the provided encryption key.

### entity_type_name

Full qualified resource name of the managed entityType in which this Feature is.

### featurestore_name

Full qualified resource name of the managed featurestore in which this Feature is.

### gca_resource

The underlying resource proto representation.

### labels

User-defined labels containing metadata about this resource.

Read more about labels at <https://goo.gl/xmQnxf>

### name

Name of this resource.

### resource_name

Full qualified resource name.

### update_time

Time this resource was last updated.

## Methods 

### Feature
    
    
    Feature(
        feature_name: str,
        featurestore_id: typing.Optional[str] = None,
        entity_type_id: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    )

Retrieves an existing managed feature given a feature resource name or a feature ID.

Example Usage:
    
    
    my_feature = aiplatform.Feature(
        feature_name='projects/123/locations/us-central1/featurestores/my_featurestore_id/                entityTypes/my_entity_type_id/features/my_feature_id'
    )
    or
    my_feature = aiplatform.Feature(
        feature_name='my_feature_id',
        featurestore_id='my_featurestore_id',
        entity_type_id='my_entity_type_id',
    )
    

**Parameters**  
---  
**Name** | **Description**  
`feature_name` |  `str`   
Required. A fully-qualified feature resource name or a feature ID. Example: "projects/123/locations/us-central1/featurestores/my_featurestore_id/entityTypes/my_entity_type_id/features/my_feature_id" or "my_feature_id" when project and location are initialized or passed, with featurestore_id and entity_type_id passed.  
`featurestore_id` |  `str`   
Optional. Featurestore ID of an existing featurestore to retrieve feature from, when feature_name is passed as Feature ID.  
`entity_type_id` |  `str`   
Optional. EntityType ID of an existing entityType to retrieve feature from, when feature_name is passed as Feature ID. The EntityType must exist in the Featurestore if provided by the featurestore_id.  
`project` |  `str`   
Optional. Project to retrieve feature from. If not set, project set in aiplatform.init will be used.  
`location` |  `str`   
Optional. Location to retrieve feature from. If not set, location set in aiplatform.init will be used.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials to use to retrieve this Feature. Overrides credentials set in aiplatform.init.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If only one of featurestore_id or entity_type_id is provided.  
  
### create
    
    
    create(
        feature_id: str,
        value_type: str,
        entity_type_name: str,
        featurestore_id: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        labels: typing.Optional[typing.Dict[str, str]] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        request_metadata: typing.Optional[typing.Sequence[typing.Tuple[str, str]]] = (),
        sync: bool = True,
        create_request_timeout: typing.Optional[float] = None,
    ) -> google.cloud.aiplatform.featurestore.feature.Feature

Creates a Feature resource in an EntityType.

Example Usage:
    
    
    my_feature = aiplatform.Feature.create(
        feature_id='my_feature_id',
        value_type='INT64',
        entity_type_name='projects/123/locations/us-central1/featurestores/my_featurestore_id/                entityTypes/my_entity_type_id'
    )
    or
    my_feature = aiplatform.Feature.create(
        feature_id='my_feature_id',
        value_type='INT64',
        entity_type_name='my_entity_type_id',
        featurestore_id='my_featurestore_id',
    )
    

### delete
    
    
    delete(sync: bool = True) -> None

Deletes this Vertex AI resource. WARNING: This deletion is permanent.

### get_entity_type
    
    
    get_entity_type() -> google.cloud.aiplatform.featurestore.entity_type.EntityType

Retrieves the managed entityType in which this Feature is.

### get_featurestore
    
    
    get_featurestore() -> (
        google.cloud.aiplatform.featurestore.featurestore.Featurestore
    )

Retrieves the managed featurestore in which this Feature is.

### list
    
    
    list(
        entity_type_name: str,
        featurestore_id: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    ) -> typing.List[google.cloud.aiplatform.featurestore.feature.Feature]

Lists existing managed feature resources in an entityType, given an entityType resource name or an entity_type ID.

Example Usage:
    
    
    my_features = aiplatform.Feature.list(
        entity_type_name='projects/123/locations/us-central1/featurestores/my_featurestore_id/                entityTypes/my_entity_type_id'
    )
    or
    my_features = aiplatform.Feature.list(
        entity_type_name='my_entity_type_id',
        featurestore_id='my_featurestore_id',
    )
    

**Parameters**  
---  
**Name** | **Description**  
`entity_type_name` |  `str`   
Required. A fully-qualified entityType resource name or an entity_type ID of an existing entityType to list features in. The EntityType must exist in the Featurestore if provided by the featurestore_id. Example: "projects/123/locations/us-central1/featurestores/my_featurestore_id/entityTypes/my_entity_type_id" or "my_entity_type_id" when project and location are initialized or passed, with featurestore_id passed.  
`featurestore_id` |  `str`   
Optional. Featurestore ID of an existing featurestore to list features in, when entity_type_name is passed as entity_type ID.  
`filter` |  `str`   
Optional. Lists the Features that match the filter expression. The following filters are supported: - `value_type`: Supports = and != comparisons. - `create_time`: Supports =, !=, <, >, >=, and <= comparisons. Values must be in RFC 3339 format. - `update_time`: Supports =, !=, <, >, >=, and <= comparisons. Values must be in RFC 3339 format. - `labels`: Supports key-value equality as well as key presence. Examples: - `value_type = DOUBLE` \--> Features whose type is DOUBLE. - `create_time > "2020-01-31T15:30:00.000000Z" OR update_time > "2020-01-31T15:30:00.000000Z"` \--> EntityTypes created or updated after 2020-01-31T15:30:00.000000Z. - `labels.active = yes AND labels.env = prod` \--> Features having both (active: yes) and (env: prod) labels. - `labels.env: *` \--> Any Feature which has a label with 'env' as the key.  
`order_by` |  `str`   
Optional. A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending. Supported fields: - `feature_id` \- `value_type` \- `create_time` \- `update_time`  
`project` |  `str`   
Optional. Project to list features in. If not set, project set in aiplatform.init will be used.  
`location` |  `str`   
Optional. Location to list features in. If not set, location set in aiplatform.init will be used.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials to use to list features. Overrides credentials set in aiplatform.init.  
  
### search
    
    
    search(
        query: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    ) -> typing.List[google.cloud.aiplatform.featurestore.feature.Feature]

Searches existing managed Feature resources.

Example Usage:
    
    
    my_features = aiplatform.Feature.search()
    

**Parameters**  
---  
**Name** | **Description**  
`query` |  `str`   
Optional. Query string that is a conjunction of field-restricted queries and/or field-restricted filters. Field-restricted queries and filters can be combined using `AND` to form a conjunction. A field query is in the form FIELD:QUERY. This implicitly checks if QUERY exists as a substring within Feature's FIELD. The QUERY and the FIELD are converted to a sequence of words (i.e. tokens) for comparison. This is done by: - Removing leading/trailing whitespace and tokenizing the search value. Characters that are not one of alphanumeric `[a-zA-Z0-9]`, underscore `_`, or asterisk `__`are treated as delimiters for tokens.`` is treated as a wildcard that matches characters within a token. - Ignoring case. - Prepending an asterisk to the first and appending an asterisk to the last token in QUERY. A QUERY must be either a singular token or a phrase. A phrase is one or multiple words enclosed in double quotation marks ("). With phrases, the order of the words is important. Words in the phrase must be matching in order and consecutively. Supported FIELDs for field-restricted queries: - `feature_id` \- `description` \- `entity_type_id` Examples: - `feature_id: foo` \--> Matches a Feature with ID containing the substring `foo` (eg. `foo`, `foofeature`, `barfoo`). - `feature_id: foo _feature_` \--> Matches a Feature with ID containing the substring `foofeature` (eg. `foobarfeature`). - `feature_id: foo AND description: bar` \--> Matches a Feature with ID containing the substring `foo` and description containing the substring `bar`. Besides field queries, the following exact-match filters are supported. The exact-match filters do not support wildcards. Unlike field-restricted queries, exact-match filters are case-sensitive. - `feature_id`: Supports = comparisons. - `description`: Supports = comparisons. Multi-token filters should be enclosed in quotes. - `entity_type_id`: Supports = comparisons. - `value_type`: Supports = and != comparisons. - `labels`: Supports key-value equality as well as key presence. - `featurestore_id`: Supports = comparisons. Examples: - `description = "foo bar"` \--> Any Feature with description exactly equal to `foo bar` \- `value_type = DOUBLE` \--> Features whose type is DOUBLE. - `labels.active = yes AND labels.env = prod` \--> Features having both (active: yes) and (env: prod) labels. - `labels.env: *` \--> Any Feature which has a label with `env` as the key. This corresponds to the `query` field on the `request` instance; if `request` is provided, this should not be set.  
`page_size` |  `int`   
Optional. The maximum number of Features to return. The service may return fewer than this value. If unspecified, at most 100 Features will be returned. The maximum value is 100; any value greater than 100 will be coerced to 100.  
`project` |  `str`   
Optional. Project to list features in. If not set, project set in aiplatform.init will be used.  
`location` |  `str`   
Optional. Location to list features in. If not set, location set in aiplatform.init will be used.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials to use to list features. Overrides credentials set in aiplatform.init.  
  
### to_dict
    
    
    to_dict() -> typing.Dict[str, typing.Any]

Returns the resource proto as a dictionary.

### update
    
    
    update(
        description: typing.Optional[str] = None,
        labels: typing.Optional[typing.Dict[str, str]] = None,
        request_metadata: typing.Optional[typing.Sequence[typing.Tuple[str, str]]] = (),
        update_request_timeout: typing.Optional[float] = None,
    ) -> google.cloud.aiplatform.featurestore.feature.Feature

Updates an existing managed feature resource.

Example Usage:
    
    
    my_feature = aiplatform.Feature(
        feature_name='my_feature_id',
        featurestore_id='my_featurestore_id',
        entity_type_id='my_entity_type_id',
    )
    my_feature.update(
        description='update my description',
    )
    

**Parameters**  
---  
**Name** | **Description**  
`description` |  `str`   
Optional. Description of the Feature.  
`labels` |  `Dict[str, str]`   
Optional. The labels with user-defined metadata to organize your Features. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See <https://goo.gl/xmQnxf> for more information on and examples of labels. No more than 64 user labels can be associated with one Feature (System labels are excluded)." System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable.  
`request_metadata` |  `Sequence[Tuple[str, str]]`   
Optional. Strings which should be sent along with the request as metadata.  
`update_request_timeout` |  `float`   
Optional. The timeout for the update request in seconds.  
  
### wait
    
    
    wait()

Helper method that blocks until all futures are complete.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
