---
url: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.MatchingEngineIndexEndpoint
title: Class MatchingEngineIndexEndpoint (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:26:44.585996+00:00
---

# Class MatchingEngineIndexEndpoint (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.MatchingEngineIndexEndpoint

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class MatchingEngineIndexEndpoint (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0  1.153.1  1.152.0  1.151.0  1.150.0  1.149.0  1.148.1  1.147.0  1.146.0  1.145.0  1.144.0  1.143.0  1.142.0  1.141.0  1.140.0  1.139.0  1.138.0  1.137.0  1.136.0  1.135.0  1.134.0  1.133.0  1.132.0  1.131.0  1.130.0  1.129.0  1.122.0  1.121.0  1.120.0  1.119.0  1.118.0  1.117.0  1.116.0  1.115.0  1.114.0  1.113.0  1.112.0  1.111.0  1.110.0  1.109.0  1.108.0  1.107.0  1.106.0  1.105.0  1.104.0  1.103.0  1.102.0  1.101.0  1.100.0  1.99.0  1.98.0  1.97.0  1.96.0  1.95.1  1.94.0  1.93.1  1.92.0  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.1  1.70.0  1.69.0  1.68.0  1.67.1  1.66.0  1.65.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.1  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.39.0  1.38.1  1.37.0  1.36.4  1.35.0  1.34.0  1.33.1  1.32.0  1.31.1  1.30.1  1.29.0  1.28.1  1.27.1  1.26.1  1.25.0  1.24.1  1.23.0  1.22.1  1.21.0  1.20.0  1.19.1  1.18.3  1.17.1  1.16.1  1.15.1  1.14.0  1.13.1  1.12.1  1.11.0  1.10.0  1.9.0  1.8.1  1.7.1  1.6.2  1.5.0  1.4.3  1.3.0  1.2.0  1.1.1  1.0.1  0.9.0  0.8.0  0.7.1  0.6.0  0.5.1  0.4.0  0.3.1 
    
    
    MatchingEngineIndexEndpoint(
        index_endpoint_name: str,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    )

Matching Engine index endpoint resource for Vertex AI.

## Properties 

### create_time

Time this resource was created.

### deployed_indexes

Returns a list of deployed indexes on this endpoint.

### description

Description of the index endpoint.

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

### name

Name of this resource.

### private_service_access_network

"Private service access network.

### private_service_connect_ip_address

"Private service connect ip address.

### public_endpoint_domain_name

Public endpoint DNS name.

### resource_name

Full qualified resource name.

### update_time

Time this resource was last updated.

## Methods 

### MatchingEngineIndexEndpoint
    
    
    MatchingEngineIndexEndpoint(
        index_endpoint_name: str,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    )

Retrieves an existing index endpoint given a name or ID.

Example Usage:
    
    
    my_index_endpoint = aiplatform.MatchingEngineIndexEndpoint(
        index_endpoint_name='projects/123/locations/us-central1/index_endpoint/my_index_id'
    )
    or
    my_index_endpoint = aiplatform.MatchingEngineIndexEndpoint(
        index_endpoint_name='my_index_endpoint_id'
    )
    

**Parameters**  
---  
**Name** | **Description**  
`index_endpoint_name` |  `str`   
Required. A fully-qualified index endpoint resource name or a index ID. Example: "projects/123/locations/us-central1/index_endpoints/my_index_id" or "my_index_id" when project and location are initialized or passed.  
`project` |  `str`   
Optional. Project to retrieve index endpoint from. If not set, project set in aiplatform.init will be used.  
`location` |  `str`   
Optional. Location to retrieve index endpoint from. If not set, location set in aiplatform.init will be used.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials to use to retrieve this IndexEndpoint. Overrides credentials set in aiplatform.init.  
  
### create
    
    
    create(
        display_name: str,
        network: typing.Optional[str] = None,
        public_endpoint_enabled: bool = False,
        description: typing.Optional[str] = None,
        labels: typing.Optional[typing.Dict[str, str]] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        request_metadata: typing.Optional[typing.Sequence[typing.Tuple[str, str]]] = (),
        sync: bool = True,
        enable_private_service_connect: bool = False,
        project_allowlist: typing.Optional[typing.Sequence[str]] = None,
        encryption_spec_key_name: typing.Optional[str] = None,
        create_request_timeout: typing.Optional[float] = None,
    ) -> (
        google.cloud.aiplatform.matching_engine.matching_engine_index_endpoint.MatchingEngineIndexEndpoint
    )

Creates a MatchingEngineIndexEndpoint resource.

Example Usage:
    
    
    my_index_endpoint = aiplatform.IndexEndpoint.create(
        display_name='my_endpoint',
    )
    

**Parameters**  
---  
**Name** | **Description**  
`display_name` |  `str`   
Required. The display name of the IndexEndpoint. The name can be up to 128 characters long and can be consist of any UTF-8 characters.  
`network` |  `str`   
Optional. The full name of the Google Compute Engine `network <https://cloud.google.com/compute/docs/networks-and-firewalls#networks>`__ to which the IndexEndpoint should be peered. Private services access must already be configured for the network. If left unspecified, the network set with aiplatform.init will be used. Format: 'projects/{project}/global/networks/{network}', where {project} is a project number, as in '12345', and {network} is network name.  
`public_endpoint_enabled` |  `bool`   
Optional. If true, the deployed index will be accessible through public endpoint.  
`description` |  `str`   
Optional. The description of the IndexEndpoint.  
`labels` |  `Dict[str, str]`   
Optional. The labels with user-defined metadata to organize your IndexEndpoint. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See <https://goo.gl/xmQnxf> for more information on and examples of labels. No more than 64 user labels can be associated with one IndexEndpoint (System labels are excluded)." System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable.  
`project` |  `str`   
Optional. Project to create IndexEndpoint in. If not set, project set in aiplatform.init will be used.  
`location` |  `str`   
Optional. Location to create IndexEndpoint in. If not set, location set in aiplatform.init will be used.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials to use to create IndexEndpoints. Overrides credentials set in aiplatform.init.  
`request_metadata` |  `Sequence[Tuple[str, str]]`   
Optional. Strings which should be sent along with the request as metadata.  
`sync` |  `bool`   
Optional. Whether to execute this creation synchronously. If False, this method will be executed in concurrent Future and any downstream object will be immediately returned and synced when the Future has completed.  
`enable_private_service_connect` |  `bool`   
If true, expose the index endpoint via private service connect.  
`project_allowlist` |  `Sequence[str]`   
Optional. List of projects from which the forwarding rule will target the service attachment.  
`encryption_spec_key_name` |  `str`   
Optional. The Cloud KMS resource identifier of the customer managed encryption key used to protect the index endpoint. Has the form: `projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key`. The key needs to be in the same region as where the compute resource is created. If set, this index endpoint and all sub-resources of this index endpoint will be secured by this key. The key needs to be in the same region as where the index endpoint is created.  
`create_request_timeout` |  `float`   
Optional. The timeout for the request in seconds.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | A network must be instantiated when creating a IndexEndpoint.  
  
### delete
    
    
    delete(force: bool = False, sync: bool = True) -> None

Deletes this MatchingEngineIndexEndpoint resource. If force is set to True, all indexes on this endpoint will be undeployed prior to deletion.

**Parameters**  
---  
**Name** | **Description**  
`force` |  `bool`   
Required. If force is set to True, all deployed indexes on this endpoint will be undeployed first. Default is False.  
`sync` |  `bool`   
Whether to execute this method synchronously. If False, this method will be executed in concurrent Future and any downstream object will be immediately returned and synced when the Future has completed.  
**Exceptions**  
---  
**Type** | **Description**  
`FailedPrecondition` | If indexes are deployed on this MatchingEngineIndexEndpoint and force = False.  
  
### deploy_index
    
    
    deploy_index(
        index: google.cloud.aiplatform.matching_engine.matching_engine_index.MatchingEngineIndex,
        deployed_index_id: str,
        display_name: typing.Optional[str] = None,
        machine_type: typing.Optional[str] = None,
        min_replica_count: typing.Optional[int] = None,
        max_replica_count: typing.Optional[int] = None,
        enable_access_logging: typing.Optional[bool] = None,
        reserved_ip_ranges: typing.Optional[typing.Sequence[str]] = None,
        deployment_group: typing.Optional[str] = None,
        auth_config_audiences: typing.Optional[typing.Sequence[str]] = None,
        auth_config_allowed_issuers: typing.Optional[typing.Sequence[str]] = None,
        request_metadata: typing.Optional[typing.Sequence[typing.Tuple[str, str]]] = (),
        sync: bool = True,
        deploy_request_timeout: typing.Optional[float] = None,
        psc_automation_configs: typing.Optional[
            typing.Sequence[typing.Tuple[str, str]]
        ] = None,
        deployment_tier: typing.Optional[str] = None,
    ) -> (
        google.cloud.aiplatform.matching_engine.matching_engine_index_endpoint.MatchingEngineIndexEndpoint
    )

Deploys an existing index resource to this endpoint resource.

**Parameters**  
---  
**Name** | **Description**  
`index` |  `MatchingEngineIndex`   
Required. The Index this is the deployment of. We may refer to this Index as the DeployedIndex's "original" Index.  
`deployed_index_id` |  `str`   
Required. The user specified ID of the DeployedIndex. The ID can be up to 128 characters long and must start with a letter and only contain letters, numbers, and underscores. The ID must be unique within the project it is created in.  
`display_name` |  `str`   
The display name of the DeployedIndex. If not provided upon creation, the Index's display_name is used.  
`machine_type` |  `str`   
Optional. The type of machine. Not specifying machine type will result in model to be deployed with automatic resources.  
`min_replica_count` |  `int`   
Optional. The minimum number of machine replicas this deployed model will be always deployed on. If traffic against it increases, it may dynamically be deployed onto more replicas, and as traffic decreases, some of these extra replicas may be freed. If this value is not provided, the value of 2 will be used.  
`max_replica_count` |  `int`   
Optional. The maximum number of replicas this deployed model may be deployed on when the traffic against it increases. If requested value is too large, the deployment will error, but if deployment succeeds then the ability to scale the model to that many replicas is guaranteed (barring service outages). If traffic against the deployed model increases beyond what its replicas at maximum may handle, a portion of the traffic will be dropped. If this value is not provided, the larger value of min_replica_count or 2 will be used. If value provided is smaller than min_replica_count, it will automatically be increased to be min_replica_count.  
`enable_access_logging` |  `bool`   
Optional. If true, private endpoint's access logs are sent to StackDriver Logging. These logs are like standard server access logs, containing information like timestamp and latency for each MatchRequest. Note that Stackdriver logs may incur a cost, especially if the deployed index receives a high queries per second rate (QPS). Estimate your costs before enabling this option.  
`reserved_ip_ranges` |  `Sequence[str]`   
Optional. A list of reserved ip ranges under the VPC network that can be used for this DeployedIndex. If set, we will deploy the index within the provided ip ranges. Otherwise, the index might be deployed to any ip ranges under the provided VPC network. The value sohuld be the name of the address (<https://cloud.google.com/compute/docs/reference/rest/v1/addresses>) Example: 'vertex-ai-ip-range'.  
`deployment_group` |  `str`   
Optional. The deployment group can be no longer than 64 characters (eg: 'test', 'prod'). If not set, we will use the 'default' deployment group. Creating `deployment_groups` with `reserved_ip_ranges` is a recommended practice when the peered network has multiple peering ranges. This creates your deployments from predictable IP spaces for easier traffic administration. Also, one deployment_group (except 'default') can only be used with the same reserved_ip_ranges which means if the deployment_group has been used with reserved_ip_ranges: [a, b, c], using it with [a, b] or [d, e] is disallowed. Note: we only support up to 5 deployment groups(not including 'default').  
`auth_config_audiences` |  `Sequence[str]`   
The list of JWT `audiences <https://tools.ietf.org/html/draft-ietf-oauth-json-web-token-32#section-4.1.3>`__. that are allowed to access. A JWT containing any of these audiences will be accepted. auth_config_audiences and auth_config_allowed_issuers must be passed together.  
`auth_config_allowed_issuers` |  `Sequence[str]`   
A list of allowed JWT issuers. Each entry must be a valid Google service account, in the following format: `service-account-name@project-id.iam.gserviceaccount.com` auth_config_audiences and auth_config_allowed_issuers must be passed together.  
`request_metadata` |  `Sequence[Tuple[str, str]]`   
Optional. Strings which should be sent along with the request as metadata.  
`sync` |  `bool`   
Whether to execute this method synchronously. If False, this method will be executed in a concurrent Future and any downstream object will be immediately returned and synced when the Future has completed.  
`deploy_request_timeout` |  `float`   
Optional. The timeout for the request in seconds.  
`psc_automation_configs` |  `Sequence[Tuple[str, str]]`   
Optional. A list of (project_id, network) pairs for Private Service Connection endpoints to be setup for the deployed index. The project_id is the project number of the project that the network is in, and network is the name of the network. Network is the full name of the Google Compute Engine `network <https://cloud.google.com/compute/docs/networks-and-firewalls#networks>`__ to which the index should be deployed to. Format:{projects/{project}/global/networks/{network}. Where {project} is a project number, as in '12345', and {network} is network name. For example: [(project_id_1, network_1), (project_id_1, network_2))] will enable PSC automation for the index to be deployed to project_id_1's network_1 and network_2 and can be queried within these networks.  
`deployment_tier` |  `str`   
Optional. The deployment tier that the index is deployed to.  
  
### find_neighbors
    
    
    find_neighbors(
        *,
        deployed_index_id: str,
        queries: typing.Optional[
            typing.Union[
                typing.List[typing.List[float]],
                typing.List[
                    google.cloud.aiplatform.matching_engine.matching_engine_index_endpoint.HybridQuery
                ],
            ]
        ] = None,
        num_neighbors: int = 10,
        filter: typing.Optional[
            typing.List[
                google.cloud.aiplatform.matching_engine.matching_engine_index_endpoint.Namespace
            ]
        ] = None,
        per_crowding_attribute_neighbor_count: typing.Optional[int] = None,
        approx_num_neighbors: typing.Optional[int] = None,
        fraction_leaf_nodes_to_search_override: typing.Optional[float] = None,
        return_full_datapoint: bool = False,
        numeric_filter: typing.Optional[
            typing.List[
                google.cloud.aiplatform.matching_engine.matching_engine_index_endpoint.NumericNamespace
            ]
        ] = None,
        embedding_ids: typing.Optional[typing.List[str]] = None,
        signed_jwt: typing.Optional[str] = None,
        psc_network: typing.Optional[str] = None
    ) -> typing.List[
        typing.List[
            google.cloud.aiplatform.matching_engine.matching_engine_index_endpoint.MatchNeighbor
        ]
    ]

Retrieves nearest neighbors for the given embedding queries on the specified deployed index which is deployed to either public or private endpoint.
    
    
    Example usage:
        my_index_endpoint = aiplatform.MatchingEngineIndexEndpoint(
            index_endpoint_name='projects/123/locations/us-central1/index_endpoint/my_index_endpoint_id'
        )
        my_index_endpoint.find_neighbors(deployed_index_id="deployed_index_id", queries= [[1, 1]],)
    

**Parameters**  
---  
**Name** | **Description**  
`deployed_index_id` |  `str`   
Required. The ID of the DeployedIndex to match the queries against.  
`queries` |  `Union[List[List[float]], List[HybridQuery]]`   
Optional. A list of queries. For regular dense-only queries, each query is a list of floats, representing a single embedding. For hybrid queries, each query is a hybrid query of type aiplatform.matching_engine.matching_engine_index_endpoint.HybridQuery.  
`num_neighbors` |  `int`   
Required. The number of nearest neighbors to be retrieved from database for each query.  
`filter` |  `List[Namespace]`   
Optional. A list of Namespaces for filtering the matching results. For example, [Namespace("color", ["red"], []), Namespace("shape", [], ["squared"])] will match datapoints that satisfy "red color" but not include datapoints with "squared shape". Please refer to <https://cloud.google.com/vertex-ai/docs/matching-engine/filtering#json> for more detail.  
`per_crowding_attribute_neighbor_count` |  `int`   
Optional. Crowding is a constraint on a neighbor list produced by nearest neighbor search requiring that no more than some value k' of the k neighbors returned have the same value of crowding_attribute. It's used for improving result diversity. This field is the maximum number of matches with the same crowding tag.  
`approx_num_neighbors` |  `int`   
Optional. The number of neighbors to find via approximate search before exact reordering is performed. If not set, the default value from scam config is used; if set, this value must be > 0.  
`fraction_leaf_nodes_to_search_override` |  `float`   
Optional. The fraction of the number of leaves to search, set at query time allows user to tune search performance. This value increase result in both search accuracy and latency increase. The value should be between 0.0 and 1.0.  
`return_full_datapoint` |  `bool`   
Optional. If set to true, the full datapoints (including all vector values and of the nearest neighbors are returned. Note that returning full datapoint will significantly increase the latency and cost of the query.  
`numeric_filter` |  `List[NumericNamespace]`   
Optional. A list of NumericNamespaces for filtering the matching results. For example: [NumericNamespace(name="cost", value_int=5, op="GREATER")] will match datapoints that its cost is greater than 5.  
`embedding_ids` |  `str`   
Optional. If `queries` is set, will use `queries` to do nearest neighbor search. If `queries` isn't set, will first use `embedding_ids` to lookup embedding values from dataset, if embedding with `embedding_ids` exists in the dataset, do nearest neighbor search.  
`signed_jwt` |  `str`   
Optional. A signed JWT for accessing the private endpoint.  
`psc_network` |  `Optional[str]`   
Optional. Required for private service automation enabled deployed index. This network is the PSC network the match query is executed in. This (project, network) pair must already be specified for psc automation when the index is deployed. The format is `projects/{project_id}/global/networks/{network_name}`. An alternative is to set the `private_service_connect_ip_address` field for this MatchingEngineIndexEndpoint instance, if the ip address is already known.  
  
### list
    
    
    list(
        filter: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        parent: typing.Optional[str] = None,
    ) -> typing.List[google.cloud.aiplatform.base.VertexAiResourceNoun]

List all instances of this Vertex AI Resource.

Example Usage:

aiplatform.BatchPredictionJobs.list( filter='state="JOB_STATE_SUCCEEDED" AND display_name="my_job"', )

aiplatform.Model.list(order_by="create_time desc, display_name")

**Parameters**  
---  
**Name** | **Description**  
`filter` |  `str`   
Optional. An expression for filtering the results of the request. For field names both snake_case and camelCase are supported.  
`order_by` |  `str`   
Optional. A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending. Supported fields: `display_name`, `create_time`, `update_time`  
`project` |  `str`   
Optional. Project to retrieve list from. If not set, project set in aiplatform.init will be used.  
`location` |  `str`   
Optional. Location to retrieve list from. If not set, location set in aiplatform.init will be used.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials to use to retrieve list. Overrides credentials set in aiplatform.init.  
`parent` |  `str`   
Optional. The parent resource name if any to retrieve list from.  
  
### match
    
    
    match(
        deployed_index_id: str,
        queries: typing.Optional[
            typing.Union[
                typing.List[typing.List[float]],
                typing.List[
                    google.cloud.aiplatform.matching_engine.matching_engine_index_endpoint.HybridQuery
                ],
            ]
        ] = None,
        num_neighbors: int = 1,
        filter: typing.Optional[
            typing.List[
                google.cloud.aiplatform.matching_engine.matching_engine_index_endpoint.Namespace
            ]
        ] = None,
        per_crowding_attribute_num_neighbors: typing.Optional[int] = None,
        approx_num_neighbors: typing.Optional[int] = None,
        fraction_leaf_nodes_to_search_override: typing.Optional[float] = None,
        low_level_batch_size: int = 0,
        numeric_filter: typing.Optional[
            typing.List[
                google.cloud.aiplatform.matching_engine.matching_engine_index_endpoint.NumericNamespace
            ]
        ] = None,
        signed_jwt: typing.Optional[str] = None,
        psc_network: typing.Optional[str] = None,
    ) -> typing.List[
        typing.List[
            google.cloud.aiplatform.matching_engine.matching_engine_index_endpoint.MatchNeighbor
        ]
    ]

Retrieves nearest neighbors for the given embedding queries on the specified deployed index for private endpoint only.

**Parameters**  
---  
**Name** | **Description**  
`deployed_index_id` |  `str`   
Required. The ID of the DeployedIndex to match the queries against.  
`queries` |  `Union[List[List[float]], List[HybridQuery]]`   
Optional. A list of queries. For regular dense-only queries, each query is a list of floats, representing a single embedding. For hybrid queries, each query is a hybrid query of type aiplatform.matching_engine.matching_engine_index_endpoint.HybridQuery.  
`num_neighbors` |  `int`   
Required. The number of nearest neighbors to be retrieved from database for each query.  
`filter` |  `List[Namespace]`   
Optional. A list of Namespaces for filtering the matching results. For example, [Namespace("color", ["red"], []), Namespace("shape", [], ["squared"])] will match datapoints that satisfy "red color" but not include datapoints with "squared shape". Please refer to <https://cloud.google.com/vertex-ai/docs/matching-engine/filtering#json> for more detail.  
`per_crowding_attribute_num_neighbors` |  `int`   
Optional. Crowding is a constraint on a neighbor list produced by nearest neighbor search requiring that no more than some value k' of the k neighbors returned have the same value of crowding_attribute. It's used for improving result diversity. This field is the maximum number of matches with the same crowding tag.  
`approx_num_neighbors` |  `int`   
The number of neighbors to find via approximate search before exact reordering is performed. If not set, the default value from scam config is used; if set, this value must be > 0.  
`fraction_leaf_nodes_to_search_override` |  `float`   
Optional. The fraction of the number of leaves to search, set at query time allows user to tune search performance. This value increase result in both search accuracy and latency increase. The value should be between 0.0 and 1.0.  
`low_level_batch_size` |  `int`   
Optional. Selects the optimal batch size to use for low-level batching. Queries within each low level batch are executed sequentially while low level batches are executed in parallel. This field is optional, defaults to 0 if not set. A non-positive number disables low level batching, i.e. all queries are executed sequentially.  
`numeric_filter` |  `Optional[list[NumericNamespace]]`   
Optional. A list of NumericNamespaces for filtering the matching results. For example: [NumericNamespace(name="cost", value_int=5, op="GREATER")] will match datapoints that its cost is greater than 5.  
`signed_jwt` |  `str`   
Optional. A signed JWT for accessing the private endpoint.  
`psc_network` |  `Optional[str]`   
Optional. Required for private service automation enabled deployed index. This network is the PSC network the match query is executed in. This (project, network) pair must already be specified for psc automation when the index is deployed. The format is `projects/{project_id}/global/networks/{network_name}`. An alternative is to set the `private_service_connect_ip_address` field for this MatchingEngineIndexEndpoint instance, if the ip address is already known.  
  
### mutate_deployed_index
    
    
    mutate_deployed_index(
        deployed_index_id: str,
        min_replica_count: int = 1,
        max_replica_count: int = 1,
        request_metadata: typing.Optional[typing.Sequence[typing.Tuple[str, str]]] = (),
        mutate_request_timeout: typing.Optional[float] = None,
    )

Updates an existing deployed index under this endpoint resource.

**Parameters**  
---  
**Name** | **Description**  
`index_id` |  `str`   
Required. The ID of the MatchingEnginIndex associated with the DeployedIndex.  
`deployed_index_id` |  `str`   
Required. The user specified ID of the DeployedIndex. The ID can be up to 128 characters long and must start with a letter and only contain letters, numbers, and underscores. The ID must be unique within the project it is created in.  
`min_replica_count` |  `int`   
Optional. The minimum number of machine replicas this deployed model will be always deployed on. If traffic against it increases, it may dynamically be deployed onto more replicas, and as traffic decreases, some of these extra replicas may be freed.  
`max_replica_count` |  `int`   
Optional. The maximum number of replicas this deployed model may be deployed on when the traffic against it increases. If requested value is too large, the deployment will error, but if deployment succeeds then the ability to scale the model to that many replicas is guaranteed (barring service outages). If traffic against the deployed model increases beyond what its replicas at maximum may handle, a portion of the traffic will be dropped. If this value is not provided, the larger value of min_replica_count or 1 will be used. If value provided is smaller than min_replica_count, it will automatically be increased to be min_replica_count.  
`request_metadata` |  `Sequence[Tuple[str, str]]`   
Optional. Strings which should be sent along with the request as metadata.  
`timeout` |  `float`   
Optional. The timeout for the request in seconds.  
  
### read_index_datapoints
    
    
    read_index_datapoints(
        *,
        deployed_index_id: str,
        ids: typing.List[str] = [],
        signed_jwt: typing.Optional[str] = None,
        psc_network: typing.Optional[str] = None
    ) -> typing.List[google.cloud.aiplatform_v1beta1.types.index.IndexDatapoint]

Reads the datapoints/vectors of the given IDs on the specified deployed index which is deployed to public or private endpoint.
    
    
    Example Usage:
        my_index_endpoint = aiplatform.MatchingEngineIndexEndpoint(
            index_endpoint_name='projects/123/locations/us-central1/index_endpoint/my_index_id'
        )
        my_index_endpoint.read_index_datapoints(deployed_index_id="public_test1", ids= ["606431", "896688"],)
    

**Parameters**  
---  
**Name** | **Description**  
`deployed_index_id` |  `str`   
Required. The ID of the DeployedIndex to match the queries against.  
`ids` |  `List[str]`   
Required. IDs of the datapoints to be searched for.  
`signed_jwt` |  `str`   
Optional. A signed JWT for accessing the private endpoint.  
`psc_network` |  `Optional[str]`   
Optional. Required for private service automation enabled deployed index. This network is the PSC network the match query is executed in. This (project, network) pair must already be specified for psc automation when the index is deployed. The format is `projects/{project_id}/global/networks/{network_name}`. An alternative is to set the `private_service_connect_ip_address` field for this MatchingEngineIndexEndpoint instance, if the ip address is already known.  
  
### to_dict
    
    
    to_dict() -> typing.Dict[str, typing.Any]

Returns the resource proto as a dictionary.

### undeploy_all
    
    
    undeploy_all(
        sync: bool = True,
    ) -> (
        google.cloud.aiplatform.matching_engine.matching_engine_index_endpoint.MatchingEngineIndexEndpoint
    )

Undeploys every index deployed to this MatchingEngineIndexEndpoint.

**Parameter**  
---  
**Name** | **Description**  
`sync` |  `bool`   
Whether to execute this method synchronously. If False, this method will be executed in concurrent Future and any downstream object will be immediately returned and synced when the Future has completed.  
  
### undeploy_index
    
    
    undeploy_index(
        deployed_index_id: str,
        request_metadata: typing.Optional[typing.Sequence[typing.Tuple[str, str]]] = (),
        undeploy_request_timeout: typing.Optional[float] = None,
    ) -> (
        google.cloud.aiplatform.matching_engine.matching_engine_index_endpoint.MatchingEngineIndexEndpoint
    )

Undeploy a deployed index endpoint resource.

**Parameters**  
---  
**Name** | **Description**  
`deployed_index_id` |  `str`   
Required. The ID of the DeployedIndex to be undeployed from the IndexEndpoint.  
`request_metadata` |  `Sequence[Tuple[str, str]]`   
Optional. Strings which should be sent along with the request as metadata.  
`undeploy_request_timeout` |  `float`   
Optional. The timeout for the request in seconds.  
  
### update
    
    
    update(
        display_name: str,
        description: typing.Optional[str] = None,
        labels: typing.Optional[typing.Dict[str, str]] = None,
        request_metadata: typing.Optional[typing.Sequence[typing.Tuple[str, str]]] = (),
        update_request_timeout: typing.Optional[float] = None,
    ) -> (
        google.cloud.aiplatform.matching_engine.matching_engine_index_endpoint.MatchingEngineIndexEndpoint
    )

Updates an existing index endpoint resource.

**Parameters**  
---  
**Name** | **Description**  
`display_name` |  `str`   
Required. The display name of the IndexEndpoint. The name can be up to 128 characters long and can be consist of any UTF-8 characters.  
`description` |  `str`   
Optional. The description of the IndexEndpoint.  
`labels` |  `Dict[str, str]`   
Optional. The labels with user-defined metadata to organize your Indexs. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See <https://goo.gl/xmQnxf> for more information on and examples of labels. No more than 64 user labels can be associated with one IndexEndpoint (System labels are excluded)." System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable.  
`request_metadata` |  `Sequence[Tuple[str, str]]`   
Optional. Strings which should be sent along with the request as metadata.  
`update_request_timeout` |  `float`   
Optional. The timeout for the request in seconds.  
  
### wait
    
    
    wait()

Helper method that blocks until all futures are complete.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
