---
url: https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/list_environments/
title: MCP Tools Reference: composer.googleapis.com \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:44:52.432893+00:00
---

# MCP Tools Reference: composer.googleapis.com  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/list_environments/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Reference ](https://docs.cloud.google.com/composer/docs/apis)



Send feedback 

#  MCP Tools Reference: composer.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `list_environments`

Lists all Managed Airflow environments in a given project and location.

Use this tool to when you need to know which environments exist in a specific project and location.

Results are paginated; use `page_size` to control the number of results per page and `page_token` from a previous response to get the next page. If `page_token` is not present in the response, there are no more results.

The following code sample shows how to use `curl` to call the `list_environments` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://composer.{region}.rep.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "list_environments",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

List environments in a project and location.

### ListEnvironmentsRequest

JSON representation  
---  
      
    
    {
      "parent": string,
      "pageSize": integer,
      "pageToken": string
    }  
  
Fields  
---  
`parent` |  `string` List environments in the given project and location, in the form: "projects/{projectId}/locations/{locationId}"  
`pageSize` |  `integer` The maximum number of environments to return.  
`pageToken` |  `string` The next_page_token value returned from a previous List request, if any.  
  
## Output Schema

The environments in a project and location.

### ListEnvironmentsResponse

JSON representation  
---  
      
    
    {
      "environments": [
        {
          object ([Environment](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.Environment))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`environments[]` |  `object (`[Environment](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.Environment)`)` The list of environments returned by a ListEnvironmentsRequest.  
`nextPageToken` |  `string` The page token used to query for the next page if one exists.  
  
### Environment

JSON representation  
---  
      
    
    {
      "name": string,
      "config": {
        object ([EnvironmentConfig](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.EnvironmentConfig))
      },
      "uuid": string,
      "state": enum ([State](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.State)),
      "createTime": string,
      "updateTime": string,
      "labels": {
        string: string,
        ...
      },
      "satisfiesPzs": boolean,
      "satisfiesPzi": boolean,
      "storageConfig": {
        object ([StorageConfig](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.StorageConfig))
      },
      "mode": enum ([Mode](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.Mode))
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the environment, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}"EnvironmentId must start with a lowercase letter followed by up to 63 lowercase letters, numbers, or hyphens, and cannot end with a hyphen.  
`config` |  `object (`[EnvironmentConfig](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.EnvironmentConfig)`)` Optional. Configuration parameters for this environment.  
`uuid` |  `string` Output only. The UUID (Universally Unique IDentifier) associated with this environment. This value is generated when the environment is created.  
`state` |  `enum (`[State](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.State)`)` The current state of the environment.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which this environment was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which this environment was last modified.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Optional. User-defined labels for this environment. The labels map can contain no more than 64 entries. Entries of the labels map are UTF8 strings that comply with the following restrictions:

  * Keys must conform to regexp: [\p{Ll}\p{Lo}][\p{Ll}\p{Lo}\p{N}_-]{0,62}
  * Values must conform to regexp: [\p{Ll}\p{Lo}\p{N}_-]{0,63}
  * Both keys and values are additionally constrained to be <= 128 bytes in size.

  
`satisfiesPzs` |  `boolean` Output only. Reserved for future use.  
`satisfiesPzi` |  `boolean` Output only. Reserved for future use.  
`storageConfig` |  `object (`[StorageConfig](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.StorageConfig)`)` Optional. Storage configuration for this environment.  
`mode` |  `enum (`[Mode](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.Mode)`)` Optional. Selects the environment mode that determines what settings are customizable and what features are available in the environment.  
  
### EnvironmentConfig

JSON representation  
---  
      
    
    {
      "gkeCluster": string,
      "dagGcsPrefix": string,
      "nodeCount": integer,
      "softwareConfig": {
        object ([SoftwareConfig](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.SoftwareConfig))
      },
      "nodeConfig": {
        object ([NodeConfig](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.NodeConfig))
      },
      "privateEnvironmentConfig": {
        object ([PrivateEnvironmentConfig](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.PrivateEnvironmentConfig))
      },
      "webServerNetworkAccessControl": {
        object ([WebServerNetworkAccessControl](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.WebServerNetworkAccessControl))
      },
      "databaseConfig": {
        object ([DatabaseConfig](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.DatabaseConfig))
      },
      "webServerConfig": {
        object ([WebServerConfig](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.WebServerConfig))
      },
      "encryptionConfig": {
        object ([EncryptionConfig](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.EncryptionConfig))
      },
      "maintenanceWindow": {
        object ([MaintenanceWindow](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.MaintenanceWindow))
      },
      "workloadsConfig": {
        object ([WorkloadsConfig](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.WorkloadsConfig))
      },
      "environmentSize": enum ([EnvironmentSize](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.EnvironmentSize)),
      "airflowUri": string,
      "airflowByoidUri": string,
      "masterAuthorizedNetworksConfig": {
        object ([MasterAuthorizedNetworksConfig](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.MasterAuthorizedNetworksConfig))
      },
      "recoveryConfig": {
        object ([RecoveryConfig](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.RecoveryConfig))
      },
      "resilienceMode": enum ([ResilienceMode](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.ResilienceMode)),
      "dataRetentionConfig": {
        object ([DataRetentionConfig](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.DataRetentionConfig))
      }
    }  
  
Fields  
---  
`gkeCluster` |  `string` Output only. The Kubernetes Engine cluster used to run this environment.  
`dagGcsPrefix` |  `string` Output only. The Cloud Storage prefix of the DAGs for this environment. Although Cloud Storage objects reside in a flat namespace, a hierarchical file tree can be simulated using "/"-delimited object name prefixes. DAG objects for this environment reside in a simulated directory with the given prefix.  
`nodeCount` |  `integer` The number of nodes in the Kubernetes Engine cluster that will be used to run this environment.This field is supported for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*.  
`softwareConfig` |  `object (`[SoftwareConfig](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.SoftwareConfig)`)` Optional. The configuration settings for software inside the environment.  
`nodeConfig` |  `object (`[NodeConfig](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.NodeConfig)`)` Optional. The configuration used for the Kubernetes Engine cluster.  
`privateEnvironmentConfig` |  `object (`[PrivateEnvironmentConfig](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.PrivateEnvironmentConfig)`)` Optional. The configuration used for the Private IP Cloud Composer environment.  
`webServerNetworkAccessControl` |  `object (`[WebServerNetworkAccessControl](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.WebServerNetworkAccessControl)`)` Optional. The network-level access control policy for the Airflow web server. If unspecified, no network-level access restrictions will be applied.  
`databaseConfig` |  `object (`[DatabaseConfig](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.DatabaseConfig)`)` Optional. The configuration settings for Cloud SQL instance used internally by Apache Airflow software.  
`webServerConfig` |  `object (`[WebServerConfig](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.WebServerConfig)`)` Optional. The configuration settings for the Airflow web server App Engine instance.  
`encryptionConfig` |  `object (`[EncryptionConfig](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.EncryptionConfig)`)` Optional. The encryption options for the Cloud Composer environment and its dependencies. Cannot be updated.  
`maintenanceWindow` |  `object (`[MaintenanceWindow](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.MaintenanceWindow)`)` Optional. The maintenance window is the period when Cloud Composer components may undergo maintenance. It is defined so that maintenance is not executed during peak hours or critical time periods.The system will not be under maintenance for every occurrence of this window, but when maintenance is planned, it will be scheduled during the window.The maintenance window period must encompass at least 12 hours per week. This may be split into multiple chunks, each with a size of at least 4 hours.If this value is omitted, the default value for maintenance window is applied. By default, maintenance windows are from 00:00:00 to 04:00:00 (GMT) on Friday, Saturday, and Sunday every week.  
`workloadsConfig` |  `object (`[WorkloadsConfig](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.WorkloadsConfig)`)` Optional. The workloads configuration settings for the GKE cluster associated with the Cloud Composer environment. The GKE cluster runs Airflow scheduler, web server and workers workloads.This field is supported for Cloud Composer environments in versions composer-2.*.*-airflow-*.*.* and newer.  
`environmentSize` |  `enum (`[EnvironmentSize](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.EnvironmentSize)`)` Optional. The size of the Cloud Composer environment.This field is supported for Cloud Composer environments in versions composer-2.*.*-airflow-*.*.* and newer.  
`airflowUri` |  `string` Output only. The URI of the Apache Airflow Web UI hosted within this environment (see [Airflow web interface](https://docs.cloud.google.com/composer/docs/how-to/accessing/airflow-web-interface)).  
`airflowByoidUri` |  `string` Output only. The 'bring your own identity' variant of the URI of the Apache Airflow Web UI hosted within this environment, to be accessed with external identities using workforce identity federation (see [Access environments with workforce identity federation](https://docs.cloud.google.com/composer/docs/composer-2/access-environments-with-workforce-identity-federation)).  
`masterAuthorizedNetworksConfig` |  `object (`[MasterAuthorizedNetworksConfig](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.MasterAuthorizedNetworksConfig)`)` Optional. The configuration options for GKE cluster master authorized networks. By default master authorized networks feature is: - in case of private environment: enabled with no external networks allowlisted. - in case of public environment: disabled.  
`recoveryConfig` |  `object (`[RecoveryConfig](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.RecoveryConfig)`)` Optional. The Recovery settings configuration of an environment.This field is supported for Cloud Composer environments in versions composer-2.*.*-airflow-*.*.* and newer.  
`resilienceMode` |  `enum (`[ResilienceMode](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.ResilienceMode)`)` Optional. Resilience mode of the Cloud Composer Environment.This field is supported for Cloud Composer environments in versions composer-2.2.0-airflow-*.*.* and newer.  
`dataRetentionConfig` |  `object (`[DataRetentionConfig](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.DataRetentionConfig)`)` Optional. The configuration setting for Airflow database data retention mechanism.  
  
### SoftwareConfig

JSON representation  
---  
      
    
    {
      "imageVersion": string,
      "airflowConfigOverrides": {
        string: string,
        ...
      },
      "pypiPackages": {
        string: string,
        ...
      },
      "envVariables": {
        string: string,
        ...
      },
      "pythonVersion": string,
      "schedulerCount": integer,
      "cloudDataLineageIntegration": {
        object ([CloudDataLineageIntegration](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.CloudDataLineageIntegration))
      },
      "webServerPluginsMode": enum ([WebServerPluginsMode](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.WebServerPluginsMode)),
      "auditLogsReplicationMode": enum ([AuditLogsReplicationMode](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.AuditLogsReplicationMode)),
      "imageVersionRollbackTargets": [
        {
          object ([ImageVersionRollbackTarget](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.ImageVersionRollbackTarget))
        }
      ]
    }  
  
Fields  
---  
`imageVersion` |  `string` Optional. The version of the software running in the environment. This encapsulates both the version of Cloud Composer functionality and the version of Apache Airflow. It must match the regular expression `composer-([0-9]+(\.[0-9]+\.[0-9]+(-preview\.[0-9]+)?)?|latest)-airflow-([0-9]+(\.[0-9]+(\.[0-9]+)?)?)`. When used as input, the server also checks if the provided version is supported and denies the request for an unsupported version.The Cloud Composer portion of the image version is a full [semantic version](https://semver.org), or an alias in the form of major version number or `latest`. When an alias is provided, the server replaces it with the current Cloud Composer version that satisfies the alias.The Apache Airflow portion of the image version is a full semantic version that points to one of the supported Apache Airflow versions, or an alias in the form of only major or major.minor versions specified. When an alias is provided, the server replaces it with the latest Apache Airflow version that satisfies the alias and is supported in the given Cloud Composer version.In all cases, the resolved image version is stored in the same field.See also [version list](https://docs.cloud.google.com/composer/docs/concepts/versioning/composer-versions) and [versioning overview](https://docs.cloud.google.com/composer/docs/concepts/versioning/composer-versioning-overview).  
`airflowConfigOverrides` |  `map (key: string, value: string)` Optional. Apache Airflow configuration properties to override.Property keys contain the section and property names, separated by a hyphen, for example "core-dags_are_paused_at_creation". Section names must not contain hyphens ("-"), opening square brackets ("["), or closing square brackets ("]"). The property name must not be empty and must not contain an equals sign ("=") or semicolon (";"). Section and property names must not contain a period ("."). Apache Airflow configuration property names must be written in [snake_case](https://en.wikipedia.org/wiki/Snake_case). Property values can contain any character, and can be written in any lower/upper case format.Certain Apache Airflow configuration property values are [blocked](https://docs.cloud.google.com/composer/docs/concepts/airflow-configurations), and cannot be overridden.  
`pypiPackages` |  `map (key: string, value: string)` Optional. Custom Python Package Index (PyPI) packages to be installed in the environment.Keys refer to the lowercase package name such as "numpy" and values are the lowercase extras and version specifier such as "==1.12.0", "[devel,gcp_api]", or "[devel]>=1.8.2, <1.9.2". To specify a package without pinning it to a version specifier, use the empty string as the value.  
`envVariables` |  `map (key: string, value: string)` Optional. Additional environment variables to provide to the Apache Airflow scheduler, worker, and webserver processes.Environment variable names must match the regular expression `[a-zA-Z_][a-zA-Z0-9_]*`. They cannot specify Apache Airflow software configuration overrides (they cannot match the regular expression `AIRFLOW__[A-Z0-9_]+__[A-Z0-9_]+`), and they cannot match any of the following reserved names:

  * `AIRFLOW_HOME`
  * `C_FORCE_ROOT`
  * `CONTAINER_NAME`
  * `DAGS_FOLDER`
  * `GCP_PROJECT`
  * `GCS_BUCKET`
  * `GKE_CLUSTER_NAME`
  * `SQL_DATABASE`
  * `SQL_INSTANCE`
  * `SQL_PASSWORD`
  * `SQL_PROJECT`
  * `SQL_REGION`
  * `SQL_USER`

  
`pythonVersion` |  `string` Optional. The major version of Python used to run the Apache Airflow scheduler, worker, and webserver processes.Can be set to '2' or '3'. If not specified, the default is '3'. Cannot be updated.This field is only supported for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*. Environments in newer versions always use Python major version 3.  
`schedulerCount` |  `integer` Optional. The number of schedulers for Airflow.This field is supported for Cloud Composer environments in versions composer-1.*.*-airflow-2.*.*.  
`cloudDataLineageIntegration` |  `object (`[CloudDataLineageIntegration](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.CloudDataLineageIntegration)`)` Optional. The configuration for Cloud Data Lineage integration.  
`webServerPluginsMode` |  `enum (`[WebServerPluginsMode](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.WebServerPluginsMode)`)` Optional. Whether or not the web server uses custom plugins. If unspecified, the field defaults to `PLUGINS_ENABLED`.This field is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer.  
`auditLogsReplicationMode` |  `enum (`[AuditLogsReplicationMode](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.AuditLogsReplicationMode)`)` Optional. The selected mode of audit logs replication.This field is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer.  
`imageVersionRollbackTargets[]` |  `object (`[ImageVersionRollbackTarget](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.ImageVersionRollbackTarget)`)` Output only. The list of image versions the environment can be rolled back to, sorted by last_active_time in descending order (most recent first).This field is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer.  
  
### AirflowConfigOverridesEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### PypiPackagesEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### EnvVariablesEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### CloudDataLineageIntegration

JSON representation  
---  
      
    
    {
      "enabled": boolean
    }  
  
Fields  
---  
`enabled` |  `boolean` Optional. Whether or not Cloud Data Lineage integration is enabled.  
  
### ImageVersionRollbackTarget

JSON representation  
---  
      
    
    {
      "imageVersion": string,
      "lastActiveTime": string
    }  
  
Fields  
---  
`imageVersion` |  `string` Output only. The image version the environment can be rolled back to.  
`lastActiveTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The last time when the environment was running this image version.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### Timestamp

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be between -62135596800 and 253402300799 inclusive (which corresponds to 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z).  
`nanos` |  `integer` Non-negative fractions of a second at nanosecond resolution. This field is the nanosecond portion of the duration, not an alternative to seconds. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be between 0 and 999,999,999 inclusive.  
  
### NodeConfig

JSON representation  
---  
      
    
    {
      "location": string,
      "machineType": string,
      "network": string,
      "subnetwork": string,
      "diskSizeGb": integer,
      "oauthScopes": [
        string
      ],
      "serviceAccount": string,
      "tags": [
        string
      ],
      "ipAllocationPolicy": {
        object ([IPAllocationPolicy](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.IPAllocationPolicy))
      },
      "enableIpMasqAgent": boolean,
      "composerNetworkAttachment": string,
      "composerInternalIpv4CidrBlock": string
    }  
  
Fields  
---  
`location` |  `string` Optional. The Compute Engine [zone](https://docs.cloud.google.com/compute/docs/regions-zones) in which to deploy the VMs used to run the Apache Airflow software, specified as a [relative resource name](https://docs.cloud.google.com/apis/design/resource_names#relative_resource_name). For example: "projects/{projectId}/zones/{zoneId}".This `location` must belong to the enclosing environment's project and location. If both this field and `nodeConfig.machineType` are specified, `nodeConfig.machineType` must belong to this `location`; if both are unspecified, the service will pick a zone in the Compute Engine region corresponding to the Cloud Composer location, and propagate that choice to both fields. If only one field (`location` or `nodeConfig.machineType`) is specified, the location information from the specified field will be propagated to the unspecified field.This field is supported for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*.  
`machineType` |  `string` Optional. The Compute Engine [machine type](https://docs.cloud.google.com/compute/docs/machine-types) used for cluster instances, specified as a [relative resource name](https://docs.cloud.google.com/apis/design/resource_names#relative_resource_name). For example: "projects/{projectId}/zones/{zoneId}/machineTypes/{machineTypeId}".The `machineType` must belong to the enclosing environment's project and location. If both this field and `nodeConfig.location` are specified, this `machineType` must belong to the `nodeConfig.location`; if both are unspecified, the service will pick a zone in the Compute Engine region corresponding to the Cloud Composer location, and propagate that choice to both fields. If exactly one of this field and `nodeConfig.location` is specified, the location information from the specified field will be propagated to the unspecified field.The `machineTypeId` must not be a [shared-core machine type](https://docs.cloud.google.com/compute/docs/machine-types#sharedcore).If this field is unspecified, the `machineTypeId` defaults to "n1-standard-1".This field is supported for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*.  
`network` |  `string` Optional. The Compute Engine network to be used for machine communications, specified as a [relative resource name](https://docs.cloud.google.com/apis/design/resource_names#relative_resource_name). For example: "projects/{projectId}/global/networks/{networkId}".If unspecified, the "default" network ID in the environment's project is used. If a [Custom Subnet Network](https://docs.cloud.google.com/vpc/docs/vpc#vpc_networks_and_subnets) is provided, `nodeConfig.subnetwork` must also be provided. For [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) subnetwork requirements, see `nodeConfig.subnetwork`.  
`subnetwork` |  `string` Optional. The Compute Engine subnetwork to be used for machine communications, specified as a [relative resource name](https://docs.cloud.google.com/apis/design/resource_names#relative_resource_name). For example: "projects/{projectId}/regions/{regionId}/subnetworks/{subnetworkId}"If a subnetwork is provided, `nodeConfig.network` must also be provided, and the subnetwork must belong to the enclosing environment's project and location.  
`diskSizeGb` |  `integer` Optional. The disk size in GB used for node VMs. Minimum size is 30GB. If unspecified, defaults to 100GB. Cannot be updated.This field is supported for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*.  
`oauthScopes[]` |  `string` Optional. The set of Google API scopes to be made available on all node VMs. If `oauth_scopes` is empty, defaults to ["https://www.googleapis.com/auth/cloud-platform"]. Cannot be updated.This field is supported for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*.  
`serviceAccount` |  `string` Optional. The Google Cloud Platform Service Account to be used by the node VMs. If a service account is not specified, the "default" Compute Engine service account is used. Cannot be updated.  
`tags[]` |  `string` Optional. The list of instance tags applied to all node VMs. Tags are used to identify valid sources or targets for network firewalls. Each tag within the list must comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Cannot be updated.  
`ipAllocationPolicy` |  `object (`[IPAllocationPolicy](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.IPAllocationPolicy)`)` Optional. The configuration for controlling how IPs are allocated in the GKE cluster.  
`enableIpMasqAgent` |  `boolean` Optional. Deploys 'ip-masq-agent' daemon set in the GKE cluster and defines nonMasqueradeCIDRs equals to pod IP range so IP masquerading is used for all destination addresses, except between pods traffic.See: <https://cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent>  
`composerNetworkAttachment` |  `string` Optional. Network Attachment that Cloud Composer environment is connected to, which provides connectivity with a user's VPC network. Takes precedence over network and subnetwork settings. If not provided, but network and subnetwork are defined during environment, it will be provisioned. If not provided and network and subnetwork are also empty, then connectivity to user's VPC network is disabled. Network attachment must be provided in format projects/{project}/regions/{region}/networkAttachments/{networkAttachment}.This field is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer.  
`composerInternalIpv4CidrBlock` |  `string` Optional. The IP range in CIDR notation to use internally by Cloud Composer. IP addresses are not reserved - and the same range can be used by multiple Cloud Composer environments. In case of overlap, IPs from this range will not be accessible in the user's VPC network. Cannot be updated. If not specified, the default value of '100.64.128.0/20' is used.This field is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer.  
  
### IPAllocationPolicy

JSON representation  
---  
      
    
    {
      "useIpAliases": boolean,
    
      // Union field cluster_ip_allocation can be only one of the following:
      "clusterSecondaryRangeName": string,
      "clusterIpv4CidrBlock": string
      // End of list of possible types for union field cluster_ip_allocation.
    
      // Union field services_ip_allocation can be only one of the following:
      "servicesSecondaryRangeName": string,
      "servicesIpv4CidrBlock": string
      // End of list of possible types for union field services_ip_allocation.
    }  
  
Fields  
---  
`useIpAliases` |  `boolean` Optional. Whether or not to enable Alias IPs in the GKE cluster. If `true`, a VPC-native cluster is created.This field is only supported for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*. Environments in newer versions always use VPC-native GKE clusters.  
Union field `cluster_ip_allocation`. Configuration of allocating IP addresses for pods in the GKE cluster. `cluster_ip_allocation` can be only one of the following:  
`clusterSecondaryRangeName` |  `string` Optional. The name of the GKE cluster's secondary range used to allocate IP addresses to pods.For Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*, this field is applicable only when `use_ip_aliases` is true.  
`clusterIpv4CidrBlock` |  `string` Optional. The IP address range used to allocate IP addresses to pods in the GKE cluster.For Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*, this field is applicable only when `use_ip_aliases` is true.Set to blank to have GKE choose a range with the default size.Set to /netmask (e.g. `/14`) to have GKE choose a range with a specific netmask.Set to a [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation (e.g. `10.96.0.0/14`) from the RFC-1918 private networks (e.g. `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`) to pick a specific range to use.  
Union field `services_ip_allocation`. Configuration of allocating IP addresses for services in the GKE cluster. `services_ip_allocation` can be only one of the following:  
`servicesSecondaryRangeName` |  `string` Optional. The name of the services' secondary range used to allocate IP addresses to the GKE cluster.For Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*, this field is applicable only when `use_ip_aliases` is true.  
`servicesIpv4CidrBlock` |  `string` Optional. The IP address range of the services IP addresses in this GKE cluster.For Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*, this field is applicable only when `use_ip_aliases` is true.Set to blank to have GKE choose a range with the default size.Set to /netmask (e.g. `/14`) to have GKE choose a range with a specific netmask.Set to a [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation (e.g. `10.96.0.0/14`) from the RFC-1918 private networks (e.g. `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`) to pick a specific range to use.  
  
### PrivateEnvironmentConfig

JSON representation  
---  
      
    
    {
      "networkingType": enum ([NetworkingType](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.NetworkingType)),
      "enablePrivateEnvironment": boolean,
      "enablePrivateBuildsOnly": boolean,
      "privateClusterConfig": {
        object ([PrivateClusterConfig](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.PrivateClusterConfig))
      },
      "webServerIpv4CidrBlock": string,
      "cloudSqlIpv4CidrBlock": string,
      "webServerIpv4ReservedRange": string,
      "cloudComposerNetworkIpv4CidrBlock": string,
      "cloudComposerNetworkIpv4ReservedRange": string,
      "enablePrivatelyUsedPublicIps": boolean,
      "cloudComposerConnectionSubnetwork": string,
      "networkingConfig": {
        object ([NetworkingConfig](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.NetworkingConfig))
      }
    }  
  
Fields  
---  
`networkingType` |  `enum (`[NetworkingType](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.NetworkingType)`)` Optional. Networking type for the environment, either private or public.  
`enablePrivateEnvironment` |  `boolean` Optional. If `true`, a Private IP Cloud Composer environment is created. If this field is set to true, `IPAllocationPolicy.use_ip_aliases` must be set to true for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*.This field is going to be deprecated. Use `networking_type` instead.  
`enablePrivateBuildsOnly` |  `boolean` Optional. If `true`, builds performed during operations that install Python packages have only private connectivity to Google services (including Artifact Registry) and VPC network (if either `NodeConfig.network` and `NodeConfig.subnetwork` fields or `NodeConfig.composer_network_attachment` field are specified). If `false`, the builds also have access to the internet.This field is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer.  
`privateClusterConfig` |  `object (`[PrivateClusterConfig](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.PrivateClusterConfig)`)` Optional. Configuration for the private GKE cluster for a Private IP Cloud Composer environment.  
`webServerIpv4CidrBlock` |  `string` Optional. The CIDR block from which IP range for web server will be reserved. Needs to be disjoint from `private_cluster_config.master_ipv4_cidr_block` and `cloud_sql_ipv4_cidr_block`.This field is supported for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*.  
`cloudSqlIpv4CidrBlock` |  `string` Optional. The CIDR block from which IP range in tenant project will be reserved for Cloud SQL. Needs to be disjoint from `web_server_ipv4_cidr_block`.  
`webServerIpv4ReservedRange` |  `string` Output only. The IP range reserved for the tenant project's App Engine VMs.This field is supported for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*.  
`cloudComposerNetworkIpv4CidrBlock` |  `string` Optional. The CIDR block from which IP range for Cloud Composer Network in tenant project will be reserved. Needs to be disjoint from private_cluster_config.master_ipv4_cidr_block and cloud_sql_ipv4_cidr_block.This field is supported for Cloud Composer environments in versions composer-2.*.*-airflow-*.*.* and newer.  
`cloudComposerNetworkIpv4ReservedRange` |  `string` Output only. The IP range reserved for the tenant project's Cloud Composer network.This field is supported for Cloud Composer environments in versions composer-2.*.*-airflow-*.*.* and newer.  
`enablePrivatelyUsedPublicIps` |  `boolean` Optional. When enabled, IPs from public (non-RFC1918) ranges can be used for `IPAllocationPolicy.cluster_ipv4_cidr_block` and `IPAllocationPolicy.service_ipv4_cidr_block`.  
`cloudComposerConnectionSubnetwork` |  `string` Optional. When specified, the environment will use Private Service Connect instead of VPC peerings to connect to Cloud SQL in the Tenant Project, and the PSC endpoint in the Customer Project will use an IP address from this subnetwork.  
`networkingConfig` |  `object (`[NetworkingConfig](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.NetworkingConfig)`)` Optional. Configuration for the network connections configuration in the environment.  
  
### PrivateClusterConfig

JSON representation  
---  
      
    
    {
      "enablePrivateEndpoint": boolean,
      "masterIpv4CidrBlock": string,
      "masterIpv4ReservedRange": string
    }  
  
Fields  
---  
`enablePrivateEndpoint` |  `boolean` Optional. If `true`, access to the public endpoint of the GKE cluster is denied.  
`masterIpv4CidrBlock` |  `string` Optional. The CIDR block from which IPv4 range for GKE master will be reserved. If left blank, the default value of '172.16.0.0/23' is used.  
`masterIpv4ReservedRange` |  `string` Output only. The IP range in CIDR notation to use for the hosted master network. This range is used for assigning internal IP addresses to the GKE cluster master or set of masters and to the internal load balancer virtual IP. This range must not overlap with any other ranges in use within the cluster's network.  
  
### NetworkingConfig

JSON representation  
---  
      
    
    {
      "connectionType": enum ([ConnectionType](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.ConnectionType))
    }  
  
Fields  
---  
`connectionType` |  `enum (`[ConnectionType](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.ConnectionType)`)` Optional. Indicates the user requested specific connection type between Tenant and Customer projects. You cannot set networking connection type in public IP environment.  
  
### WebServerNetworkAccessControl

JSON representation  
---  
      
    
    {
      "allowedIpRanges": [
        {
          object ([AllowedIpRange](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.AllowedIpRange))
        }
      ]
    }  
  
Fields  
---  
`allowedIpRanges[]` |  `object (`[AllowedIpRange](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.AllowedIpRange)`)` A collection of allowed IP ranges with descriptions.  
  
### AllowedIpRange

JSON representation  
---  
      
    
    {
      "value": string,
      "description": string
    }  
  
Fields  
---  
`value` |  `string` IP address or range, defined using CIDR notation, of requests that this rule applies to. Examples: `192.168.1.1` or `192.168.0.0/16` or `2001:db8::/32` or `2001:0db8:0000:0042:0000:8a2e:0370:7334`.IP range prefixes should be properly truncated. For example, `1.2.3.4/24` should be truncated to `1.2.3.0/24`. Similarly, for IPv6, `2001:db8::1/32` should be truncated to `2001:db8::/32`.  
`description` |  `string` Optional. User-provided description. It must contain at most 300 characters.  
  
### DatabaseConfig

JSON representation  
---  
      
    
    {
      "machineType": string,
      "zone": string
    }  
  
Fields  
---  
`machineType` |  `string` Optional. Cloud SQL machine type used by Airflow database. It has to be one of: db-n1-standard-2, db-n1-standard-4, db-n1-standard-8 or db-n1-standard-16. If not specified, db-n1-standard-2 will be used. Supported for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*.  
`zone` |  `string` Optional. The Compute Engine zone where the Airflow database is created. If zone is provided, it must be in the region selected for the environment. If zone is not provided, a zone is automatically selected. The zone can only be set during environment creation. Supported for Cloud Composer environments in versions composer-2.*.*-airflow-*.*.*.  
  
### WebServerConfig

JSON representation  
---  
      
    
    {
      "machineType": string
    }  
  
Fields  
---  
`machineType` |  `string` Optional. Machine type on which Airflow web server is running. It has to be one of: composer-n1-webserver-2, composer-n1-webserver-4 or composer-n1-webserver-8. If not specified, composer-n1-webserver-2 will be used. Value custom is returned only in response, if Airflow web server parameters were manually changed to a non-standard values.  
  
### EncryptionConfig

JSON representation  
---  
      
    
    {
      "kmsKeyName": string
    }  
  
Fields  
---  
`kmsKeyName` |  `string` Optional. Customer-managed Encryption Key available through Google's Key Management Service. Cannot be updated. If not specified, Google-managed key will be used.  
  
### MaintenanceWindow

JSON representation  
---  
      
    
    {
      "startTime": string,
      "endTime": string,
      "recurrence": string
    }  
  
Fields  
---  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Required. Start time of the first recurrence of the maintenance window.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Required. Maintenance window end time. It is used only to calculate the duration of the maintenance window. The value for end-time must be in the future, relative to `start_time`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`recurrence` |  `string` Required. Maintenance window recurrence. Format is a subset of [RFC-5545](https://tools.ietf.org/html/rfc5545) `RRULE`. The only allowed values for `FREQ` field are `FREQ=DAILY` and `FREQ=WEEKLY;BYDAY=...` Example values: `FREQ=WEEKLY;BYDAY=TU,WE`, `FREQ=DAILY`.  
  
### WorkloadsConfig

JSON representation  
---  
      
    
    {
      "scheduler": {
        object ([SchedulerResource](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.SchedulerResource))
      },
      "webServer": {
        object ([WebServerResource](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.WebServerResource))
      },
      "worker": {
        object ([WorkerResource](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.WorkerResource))
      },
      "triggerer": {
        object ([TriggererResource](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.TriggererResource))
      },
      "dagProcessor": {
        object ([DagProcessorResource](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.DagProcessorResource))
      }
    }  
  
Fields  
---  
`scheduler` |  `object (`[SchedulerResource](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.SchedulerResource)`)` Optional. Resources used by Airflow schedulers.  
`webServer` |  `object (`[WebServerResource](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.WebServerResource)`)` Optional. Resources used by Airflow web server.  
`worker` |  `object (`[WorkerResource](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.WorkerResource)`)` Optional. Resources used by Airflow workers.  
`triggerer` |  `object (`[TriggererResource](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.TriggererResource)`)` Optional. Resources used by Airflow triggerers.  
`dagProcessor` |  `object (`[DagProcessorResource](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.DagProcessorResource)`)` Optional. Resources used by Airflow DAG processors.This field is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer.  
  
### SchedulerResource

JSON representation  
---  
      
    
    {
      "cpu": number,
      "memoryGb": number,
      "storageGb": number,
      "count": integer
    }  
  
Fields  
---  
`cpu` |  `number` Optional. CPU request and limit for a single Airflow scheduler replica.  
`memoryGb` |  `number` Optional. Memory (GB) request and limit for a single Airflow scheduler replica.  
`storageGb` |  `number` Optional. Storage (GB) request and limit for a single Airflow scheduler replica.  
`count` |  `integer` Optional. The number of schedulers.  
  
### WebServerResource

JSON representation  
---  
      
    
    {
      "cpu": number,
      "memoryGb": number,
      "storageGb": number
    }  
  
Fields  
---  
`cpu` |  `number` Optional. CPU request and limit for Airflow web server.  
`memoryGb` |  `number` Optional. Memory (GB) request and limit for Airflow web server.  
`storageGb` |  `number` Optional. Storage (GB) request and limit for Airflow web server.  
  
### WorkerResource

JSON representation  
---  
      
    
    {
      "cpu": number,
      "memoryGb": number,
      "storageGb": number,
      "minCount": integer,
      "maxCount": integer
    }  
  
Fields  
---  
`cpu` |  `number` Optional. CPU request and limit for a single Airflow worker replica.  
`memoryGb` |  `number` Optional. Memory (GB) request and limit for a single Airflow worker replica.  
`storageGb` |  `number` Optional. Storage (GB) request and limit for a single Airflow worker replica.  
`minCount` |  `integer` Optional. Minimum number of workers for autoscaling.  
`maxCount` |  `integer` Optional. Maximum number of workers for autoscaling.  
  
### TriggererResource

JSON representation  
---  
      
    
    {
      "count": integer,
      "cpu": number,
      "memoryGb": number
    }  
  
Fields  
---  
`count` |  `integer` Optional. The number of triggerers.  
`cpu` |  `number` Optional. CPU request and limit for a single Airflow triggerer replica.  
`memoryGb` |  `number` Optional. Memory (GB) request and limit for a single Airflow triggerer replica.  
  
### DagProcessorResource

JSON representation  
---  
      
    
    {
      "cpu": number,
      "memoryGb": number,
      "storageGb": number,
      "count": integer
    }  
  
Fields  
---  
`cpu` |  `number` Optional. CPU request and limit for a single Airflow DAG processor replica.  
`memoryGb` |  `number` Optional. Memory (GB) request and limit for a single Airflow DAG processor replica.  
`storageGb` |  `number` Optional. Storage (GB) request and limit for a single Airflow DAG processor replica.  
`count` |  `integer` Optional. The number of DAG processors. If not provided or set to 0, a single DAG processor instance will be created.  
  
### MasterAuthorizedNetworksConfig

JSON representation  
---  
      
    
    {
      "enabled": boolean,
      "cidrBlocks": [
        {
          object ([CidrBlock](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.CidrBlock))
        }
      ]
    }  
  
Fields  
---  
`enabled` |  `boolean` Optional. Whether or not master authorized networks feature is enabled.  
`cidrBlocks[]` |  `object (`[CidrBlock](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.CidrBlock)`)` Up to 50 external networks that could access Kubernetes master through HTTPS.  
  
### CidrBlock

JSON representation  
---  
      
    
    {
      "displayName": string,
      "cidrBlock": string
    }  
  
Fields  
---  
`displayName` |  `string` User-defined name that identifies the CIDR block.  
`cidrBlock` |  `string` CIDR block that must be specified in CIDR notation.  
  
### RecoveryConfig

JSON representation  
---  
      
    
    {
      "scheduledSnapshotsConfig": {
        object ([ScheduledSnapshotsConfig](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.ScheduledSnapshotsConfig))
      }
    }  
  
Fields  
---  
`scheduledSnapshotsConfig` |  `object (`[ScheduledSnapshotsConfig](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.ScheduledSnapshotsConfig)`)` Optional. The configuration for scheduled snapshot creation mechanism.  
  
### ScheduledSnapshotsConfig

JSON representation  
---  
      
    
    {
      "enabled": boolean,
      "snapshotLocation": string,
      "snapshotCreationSchedule": string,
      "timeZone": string
    }  
  
Fields  
---  
`enabled` |  `boolean` Optional. Whether scheduled snapshots creation is enabled.  
`snapshotLocation` |  `string` Optional. The Cloud Storage location for storing automatically created snapshots.  
`snapshotCreationSchedule` |  `string` Optional. The cron expression representing the time when snapshots creation mechanism runs. This field is subject to additional validation around frequency of execution.  
`timeZone` |  `string` Optional. Time zone that sets the context to interpret snapshot_creation_schedule.  
  
### DataRetentionConfig

JSON representation  
---  
      
    
    {
      "airflowMetadataRetentionConfig": {
        object ([AirflowMetadataRetentionPolicyConfig](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.AirflowMetadataRetentionPolicyConfig))
      },
      "taskLogsRetentionConfig": {
        object ([TaskLogsRetentionConfig](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.TaskLogsRetentionConfig))
      }
    }  
  
Fields  
---  
`airflowMetadataRetentionConfig` |  `object (`[AirflowMetadataRetentionPolicyConfig](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.AirflowMetadataRetentionPolicyConfig)`)` Optional. The retention policy for airflow metadata database.  
`taskLogsRetentionConfig` |  `object (`[TaskLogsRetentionConfig](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.TaskLogsRetentionConfig)`)` Optional. The configuration settings for task logs retention  
  
### AirflowMetadataRetentionPolicyConfig

JSON representation  
---  
      
    
    {
      "retentionMode": enum ([RetentionMode](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.RetentionMode)),
      "retentionDays": integer
    }  
  
Fields  
---  
`retentionMode` |  `enum (`[RetentionMode](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.RetentionMode)`)` Optional. Retention can be either enabled or disabled.  
`retentionDays` |  `integer` Optional. How many days data should be retained for.  
  
### TaskLogsRetentionConfig

JSON representation  
---  
      
    
    {
      "storageMode": enum ([TaskLogsStorageMode](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.TaskLogsStorageMode))
    }  
  
Fields  
---  
`storageMode` |  `enum (`[TaskLogsStorageMode](https://docs.cloud.google.com/composer/docs/reference/mcp/tools_list/get_environment#Output.Schema.TaskLogsStorageMode)`)` Optional. The mode of storage for Airflow workers task logs.  
  
### LabelsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### StorageConfig

JSON representation  
---  
      
    
    {
      "bucket": string
    }  
  
Fields  
---  
`bucket` |  `string` Optional. The name of the Cloud Storage bucket used by the environment. No `gs://` prefix.  
  
### WebServerPluginsMode

Web server plugins mode of the Cloud Composer environment.

Enums  
---  
`WEB_SERVER_PLUGINS_MODE_UNSPECIFIED` | Default mode.  
`PLUGINS_DISABLED` | Web server plugins are not supported.  
`PLUGINS_ENABLED` | Web server plugins are supported.  
  
### AuditLogsReplicationMode

Audit logs replication mode of the Cloud Composer environment.

Enums  
---  
`AUDIT_LOGS_REPLICATION_MODE_UNSPECIFIED` | The user's choice of logs replication mode is unspecified.  
`AUDIT_LOGS_REPLICATION_DISABLED` | The user opted out of audit logs replication.  
`AUDIT_LOGS_REPLICATION_ENABLED` | The user opted in to audit logs replication.  
  
### NetworkingType

Networking type for the environment, either private or public.

Enums  
---  
`NETWORKING_TYPE_UNSPECIFIED` | Default networking type.  
`PRIVATE` | Private IP Cloud Composer environment with no access to the internet.  
`PUBLIC` | Cloud Composer environment with access to the internet.  
  
### ConnectionType

Represents connection type between Composer environment in Customer Project and the corresponding Tenant project, from a predefined list of available connection modes.

Enums  
---  
`CONNECTION_TYPE_UNSPECIFIED` | No specific connection type was requested, so the environment uses the default value corresponding to the rest of its configuration.  
`VPC_PEERING` | Requests the use of VPC peerings for connecting the Customer and Tenant projects.  
`PRIVATE_SERVICE_CONNECT` | Requests the use of Private Service Connect for connecting the Customer and Tenant projects.  
  
### EnvironmentSize

The size of the Cloud Composer environment.

Enums  
---  
`ENVIRONMENT_SIZE_UNSPECIFIED` | The size of the environment is unspecified.  
`ENVIRONMENT_SIZE_SMALL` | The environment size is small.  
`ENVIRONMENT_SIZE_MEDIUM` | The environment size is medium.  
`ENVIRONMENT_SIZE_LARGE` | The environment size is large.  
`ENVIRONMENT_SIZE_EXTRA_LARGE` | The environment size is extra large.  
  
### ResilienceMode

Resilience mode of the Cloud Composer Environment.

Enums  
---  
`RESILIENCE_MODE_UNSPECIFIED` | Default mode doesn't change environment parameters.  
`HIGH_RESILIENCE` | Enabled High Resilience mode, including Cloud SQL HA.  
  
### RetentionMode

Describes retention policy.

Enums  
---  
`RETENTION_MODE_UNSPECIFIED` | Default mode doesn't change environment parameters.  
`RETENTION_MODE_ENABLED` | Retention policy is enabled.  
`RETENTION_MODE_DISABLED` | Retention policy is disabled.  
  
### TaskLogsStorageMode

The definition of task_logs_storage_mode.

Enums  
---  
`TASK_LOGS_STORAGE_MODE_UNSPECIFIED` | This configuration is not specified by the user.  
`CLOUD_LOGGING_AND_CLOUD_STORAGE` | Store task logs in Cloud Logging and in the environment's Cloud Storage bucket.  
`CLOUD_LOGGING_ONLY` | Store task logs in Cloud Logging only.  
  
### State

State of the environment.

Enums  
---  
`STATE_UNSPECIFIED` | The state of the environment is unknown.  
`CREATING` | The environment is in the process of being created.  
`RUNNING` | The environment is currently running and healthy. It is ready for use.  
`UPDATING` | The environment is being updated. It remains usable but cannot receive additional update requests or be deleted at this time.  
`HIBERNATED` | The environment is currently hibernated. It does not run any DAGs.  
`DELETING` | The environment is undergoing deletion. It cannot be used.  
`ERROR` | The environment has encountered an error and cannot be used.  
  
### Mode

Defines the environment mode that determines what settings are customizable and what features are available in the environment.

Enums  
---  
`MODE_UNSPECIFIED` | Represents the default mode, which allows full customization of the environment. It should be used for all production and customized test environments.  
`DEVELOPMENT` | Represents the development mode, which has constraints on the environment configuration, but offers an additional feature (environment hibernation). It should be used only for test environments.  
  
### Tool Annotations

[Tool annotations](https://modelcontextprotocol.io/specification/latest/schema#toolannotations) are sent to MCP clients to describe the basic risk of a given tool. Most clients treat these hints as untrusted, but they can be used to decide when a confirmation prompt might be sent to a user. 

Along with the title string, the following boolean hints are defined as follows: 

  * `readOnlyHint`: If true, the tool doesn't modify its environment. Default: false.
  * `destructiveHint`: If true, then the tool can perform destructive actions. If false, then the tool can only perform additive actions. Default: true.
  * `idempotentHint`: If true, then calling the tool repeatedly with the same arguments will have no additional effect on its environment. Default: false.
  * `openWorldHint`: If true, then the tool can interact with an 'open world' of external entities. If false, then the tool can only interact with internal entities. For example, a web search tool would be open world, while a memory tool would not be open world.



Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
