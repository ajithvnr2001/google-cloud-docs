---
url: https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections
title: REST Resource: projects.locations.connections \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:07:18.765204+00:00
---

# REST Resource: projects.locations.connections  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Reference ](https://docs.cloud.google.com/integration-connectors/docs/reference/rest)



Send feedback 

#  REST Resource: projects.locations.connections Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Connection
    * JSON representation
  * ConnectionStatus
    * JSON representation
  * State
  * LockConfig
    * JSON representation
  * NodeConfig
    * JSON representation
  * LogConfig
    * JSON representation
  * LogLevel
  * SslConfig
    * JSON representation
  * TrustModel
  * SubscriptionType
  * EventingEnablementType
  * EventingConfig
    * JSON representation
  * DeadLetterConfig
    * JSON representation
  * EnrichmentConfig
    * JSON representation
  * EventingRuntimeData
    * JSON representation
  * EventingStatus
    * JSON representation
  * State
  * WebhookData
    * JSON representation
  * WebhookSubscriptions
    * JSON representation
  * ConnectorVersionInfraConfig
    * JSON representation
  * DeploymentModel
  * DeploymentModelMigrationState
  * TLSMigrationState
  * BillingConfig
    * JSON representation
  * BillingCategory
  * TrafficShapingConfig
    * JSON representation
  * Methods



## Resource: Connection

Connection represents an instance of connector.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "labels": {
        string: string,
        ...
      },
      "description": string,
      "connectorVersion": string,
      "status": {
        object ([ConnectionStatus](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#ConnectionStatus))
      },
      "configVariables": [
        {
          object ([ConfigVariable](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/ConfigVariable))
        }
      ],
      "authConfig": {
        object ([AuthConfig](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/AuthConfig))
      },
      "lockConfig": {
        object ([LockConfig](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#LockConfig))
      },
      "destinationConfigs": [
        {
          object ([DestinationConfig](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/DestinationConfig))
        }
      ],
      "imageLocation": string,
      "serviceAccount": string,
      "serviceDirectory": string,
      "envoyImageLocation": string,
      "suspended": boolean,
      "nodeConfig": {
        object ([NodeConfig](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#NodeConfig))
      },
      "logConfig": {
        object ([LogConfig](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#LogConfig))
      },
      "sslConfig": {
        object ([SslConfig](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#SslConfig))
      },
      "subscriptionType": enum ([SubscriptionType](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#SubscriptionType)),
      "connectionRevision": string,
      "eventingEnablementType": enum ([EventingEnablementType](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#EventingEnablementType)),
      "eventingConfig": {
        object ([EventingConfig](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#EventingConfig))
      },
      "connectorVersionLaunchStage": enum ([LaunchStage](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/LaunchStage)),
      "eventingRuntimeData": {
        object ([EventingRuntimeData](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#EventingRuntimeData))
      },
      "connectorVersionInfraConfig": {
        object ([ConnectorVersionInfraConfig](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#ConnectorVersionInfraConfig))
      },
      "isTrustedTester": boolean,
      "authOverrideEnabled": boolean,
      "billingConfig": {
        object ([BillingConfig](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#BillingConfig))
      },
      "asyncOperationsEnabled": boolean,
      "host": string,
      "tlsServiceDirectory": string,
      "trafficShapingConfigs": [
        {
          object ([TrafficShapingConfig](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#TrafficShapingConfig))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Output only. Resource name of the Connection. Format: projects/{project}/locations/{location}/connections/{connection}  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Created time.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Updated time.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Optional. Resource labels to represent user-provided metadata. Refer to cloud documentation on labels for more details. <https://cloud.google.com/compute/docs/labeling-resources>An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`description` |  `string` Optional. Description of the resource.  
`connectorVersion` |  `string` Required. Connector version on which the connection is created. The format is: projects/*/locations/*/providers/*/connectors/*/versions/* Only global location is supported for ConnectorVersion resource.  
`status` |  `object (`[ConnectionStatus](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#ConnectionStatus)`)` Output only. Current status of the connection.  
`configVariables[]` |  `object (`[ConfigVariable](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/ConfigVariable)`)` Optional. Configuration for configuring the connection with an external system.  
`authConfig` |  `object (`[AuthConfig](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/AuthConfig)`)` Optional. Configuration for establishing the connection's authentication with an external system.  
`lockConfig` |  `object (`[LockConfig](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#LockConfig)`)` Optional. Configuration that indicates whether or not the Connection can be edited.  
`destinationConfigs[]` |  `object (`[DestinationConfig](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/DestinationConfig)`)` Optional. Configuration of the Connector's destination. Only accepted for Connectors that accepts user defined destination(s).  
`imageLocation` |  `string` Output only. GCR location where the runtime image is stored. formatted like: gcr.io/{bucketName}/{imageName}  
`serviceAccount` |  `string` Optional. Service account needed for runtime plane to access Google Cloud resources.  
`serviceDirectory` |  `string` Output only. The name of the Service Directory service name. Used for Private Harpoon to resolve the ILB address. e.g. "projects/cloud-connectors-e2e-testing/locations/us-central1/namespaces/istio-system/services/istio-ingressgateway-connectors"  
`envoyImageLocation` |  `string` Output only. GCR location where the envoy image is stored. formatted like: gcr.io/{bucketName}/{imageName}  
`suspended` |  `boolean` Optional. Suspended indicates if a user has suspended a connection or not.  
`nodeConfig` |  `object (`[NodeConfig](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#NodeConfig)`)` Optional. Node configuration for the connection.  
`logConfig` |  `object (`[LogConfig](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#LogConfig)`)` Optional. Log configuration for the connection.  
`sslConfig` |  `object (`[SslConfig](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#SslConfig)`)` Optional. Ssl config of a connection  
`subscriptionType` |  `enum (`[SubscriptionType](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#SubscriptionType)`)` Output only. This subscription type enum states the subscription type of the project.  
`connectionRevision` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Connection revision. This field is only updated when the connection is created or updated by User.  
`eventingEnablementType` |  `enum (`[EventingEnablementType](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#EventingEnablementType)`)` Optional. Eventing enablement type. Will be nil if eventing is not enabled.  
`eventingConfig` |  `object (`[EventingConfig](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#EventingConfig)`)` Optional. Eventing config of a connection  
`connectorVersionLaunchStage` |  `enum (`[LaunchStage](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/LaunchStage)`)` Output only. Flag to mark the version indicating the launch stage.  
`eventingRuntimeData` |  `object (`[EventingRuntimeData](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#EventingRuntimeData)`)` Output only. Eventing Runtime Data.  
`connectorVersionInfraConfig` |  `object (`[ConnectorVersionInfraConfig](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#ConnectorVersionInfraConfig)`)` Output only. Infra configs supported by Connector Version.  
`isTrustedTester` |  `boolean` Output only. Is trusted tester program enabled for the project.  
`authOverrideEnabled` |  `boolean` Optional. Auth override enabled for the connection. If Auth Override is enabled, Connection allows the backend service auth to be overridden in the entities/actions API.  
`billingConfig` |  `object (`[BillingConfig](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#BillingConfig)`)` Output only. Billing config for the connection.  
`asyncOperationsEnabled` |  `boolean` Optional. Async operations enabled for the connection. If Async Operations is enabled, Connection allows the customers to initiate async long running operations using the actions API.  
`host` |  `string` Output only. The name of the Hostname of the Service Directory service with TLS.  
`tlsServiceDirectory` |  `string` Output only. The name of the Service Directory service with TLS.  
`trafficShapingConfigs[]` |  `object (`[TrafficShapingConfig](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#TrafficShapingConfig)`)` Optional. Traffic shaping configuration for the connection.  
  
## ConnectionStatus

ConnectionStatus indicates the state of the connection.

JSON representation  
---  
      
    
    {
      "state": enum ([State](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#State)),
      "description": string,
      "status": string
    }  
  
Fields  
---  
`state` |  `enum (`[State](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#State)`)` State.  
`description` |  `string` Description.  
`status` |  `string` Status provides detailed information for the state.  
  
## State

All the possible Connection State.

Enums  
---  
`STATE_UNSPECIFIED` | Connection does not have a state yet.  
`CREATING` | Connection is being created.  
`ACTIVE` | Connection is running and ready for requests.  
`INACTIVE` | Connection is stopped.  
`DELETING` | Connection is being deleted.  
`UPDATING` | Connection is being updated.  
`ERROR` | Connection is not running due to an error.  
`AUTHORIZATION_REQUIRED` | Connection is not running because the authorization configuration is not complete.  
  
## LockConfig

Determines whether or no a connection is locked. If locked, a reason must be specified.

JSON representation  
---  
      
    
    {
      "locked": boolean,
      "reason": string
    }  
  
Fields  
---  
`locked` |  `boolean` Indicates whether or not the connection is locked.  
`reason` |  `string` Describes why a connection is locked.  
  
## NodeConfig

Node configuration for the connection.

JSON representation  
---  
      
    
    {
      "minNodeCount": integer,
      "maxNodeCount": integer
    }  
  
Fields  
---  
`minNodeCount` |  `integer` Minimum number of nodes in the runtime nodes.  
`maxNodeCount` |  `integer` Maximum number of nodes in the runtime nodes.  
  
## LogConfig

Log configuration for the connection.

JSON representation  
---  
      
    
    {
      "enabled": boolean,
      "level": enum ([LogLevel](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#LogLevel))
    }  
  
Fields  
---  
`enabled` |  `boolean` Enabled represents whether logging is enabled or not for a connection.  
`level` |  `enum (`[LogLevel](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#LogLevel)`)` Optional. Log configuration level.  
  
## LogLevel

Log configuration level enum for the connection.

Enums  
---  
`LOG_LEVEL_UNSPECIFIED` | Log level unspecified.  
`ERROR` | Only error logs are enabled.  
`INFO` | Info and error logs are enabled.  
`DEBUG` | Debug and high verbosity logs are enabled.  
  
## SslConfig

SSL Configuration of a connection

JSON representation  
---  
      
    
    {
      "type": enum ([SslType](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/SslType)),
      "trustModel": enum ([TrustModel](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#TrustModel)),
      "privateServerCertificate": {
        object ([Secret](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/Secret))
      },
      "clientCertificate": {
        object ([Secret](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/Secret))
      },
      "clientPrivateKey": {
        object ([Secret](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/Secret))
      },
      "clientPrivateKeyPass": {
        object ([Secret](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/Secret))
      },
      "serverCertType": enum ([CertType](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/CertType)),
      "clientCertType": enum ([CertType](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/CertType)),
      "useSsl": boolean,
      "additionalVariables": [
        {
          object ([ConfigVariable](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/ConfigVariable))
        }
      ]
    }  
  
Fields  
---  
`type` |  `enum (`[SslType](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/SslType)`)` Optional. Controls the ssl type for the given connector version.  
`trustModel` |  `enum (`[TrustModel](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#TrustModel)`)` Optional. Trust Model of the SSL connection  
`privateServerCertificate` |  `object (`[Secret](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/Secret)`)` Optional. Private Server Certificate. Needs to be specified if trust model is `PRIVATE`.  
`clientCertificate` |  `object (`[Secret](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/Secret)`)` Optional. Client Certificate  
`clientPrivateKey` |  `object (`[Secret](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/Secret)`)` Optional. Client Private Key  
`clientPrivateKeyPass` |  `object (`[Secret](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/Secret)`)` Optional. Secret containing the passphrase protecting the Client Private Key  
`serverCertType` |  `enum (`[CertType](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/CertType)`)` Optional. Type of Server Cert (PEM/JKS/.. etc.)  
`clientCertType` |  `enum (`[CertType](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/CertType)`)` Optional. Type of Client Cert (PEM/JKS/.. etc.)  
`useSsl` |  `boolean` Optional. Bool for enabling SSL  
`additionalVariables[]` |  `object (`[ConfigVariable](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/ConfigVariable)`)` Optional. Additional SSL related field values  
  
## TrustModel

Enum for Ttust Model

Enums  
---  
`PUBLIC` | Public Trust Model. Takes the Default Java trust store.  
`PRIVATE` | Private Trust Model. Takes custom/private trust store.  
`INSECURE` | Insecure Trust Model. Accept all certificates.  
  
## SubscriptionType

Subscription Types

Enums  
---  
`SUBSCRIPTION_TYPE_UNSPECIFIED` | Unspecified subscription type.  
`PAY_G` | PayG subscription.  
`PAID` | Paid Subscription.  
  
## EventingEnablementType

Eventing Enablement Type enum.

Enums  
---  
`EVENTING_ENABLEMENT_TYPE_UNSPECIFIED` | Eventing Enablement Type Unspecifeied.  
`EVENTING_AND_CONNECTION` | Both connection and eventing.  
`ONLY_EVENTING` | Only Eventing.  
  
## EventingConfig

Eventing Configuration of a connection

JSON representation  
---  
      
    
    {
      "registrationDestinationConfig": {
        object ([DestinationConfig](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/DestinationConfig))
      },
      "authConfig": {
        object ([AuthConfig](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/AuthConfig))
      },
      "listenerAuthConfig": {
        object ([AuthConfig](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/AuthConfig))
      },
      "additionalVariables": [
        {
          object ([ConfigVariable](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/ConfigVariable))
        }
      ],
      "enrichmentEnabled": boolean,
      "privateConnectivityEnabled": boolean,
      "eventsListenerIngressEndpoint": string,
      "deadLetterConfig": {
        object ([DeadLetterConfig](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#DeadLetterConfig))
      },
      "proxyDestinationConfig": {
        object ([DestinationConfig](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/DestinationConfig))
      },
      "enrichmentConfig": {
        object ([EnrichmentConfig](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#EnrichmentConfig))
      }
    }  
  
Fields  
---  
`registrationDestinationConfig` |  `object (`[DestinationConfig](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/DestinationConfig)`)` Optional. Registration endpoint for auto registration.  
`authConfig` |  `object (`[AuthConfig](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/AuthConfig)`)` Optional. Auth details for the webhook adapter.  
`listenerAuthConfig` |  `object (`[AuthConfig](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/AuthConfig)`)` Optional. Auth details for the event listener.  
`additionalVariables[]` |  `object (`[ConfigVariable](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/ConfigVariable)`)` Optional. Additional eventing related field values  
`enrichmentEnabled` |  `boolean` Optional. Enrichment Enabled.  
`privateConnectivityEnabled` |  `boolean` Optional. Private Connectivity Enabled.  
`eventsListenerIngressEndpoint` |  `string` Optional. Ingress endpoint of the event listener. This is used only when private connectivity is enabled.  
`deadLetterConfig` |  `object (`[DeadLetterConfig](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#DeadLetterConfig)`)` Optional. Dead letter configuration for eventing of a connection.  
`proxyDestinationConfig` |  `object (`[DestinationConfig](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/DestinationConfig)`)` Optional. Proxy for Eventing auto-registration.  
`enrichmentConfig` |  `object (`[EnrichmentConfig](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#EnrichmentConfig)`)` Optional. Data enrichment configuration.  
  
## DeadLetterConfig

Dead Letter configuration details provided by the user.

JSON representation  
---  
      
    
    {
      "topic": string,
      "projectId": string
    }  
  
Fields  
---  
`topic` |  `string` Optional. Topic to push events which couldn't be processed.  
`projectId` |  `string` Optional. Project which has the topic given.  
  
## EnrichmentConfig

Data enrichment configuration.

JSON representation  
---  
      
    
    {
      "appendAcl": boolean
    }  
  
Fields  
---  
`appendAcl` |  `boolean` Optional. Append ACL to the event.  
  
## EventingRuntimeData

Eventing runtime data has the details related to eventing managed by the system.

JSON representation  
---  
      
    
    {
      "status": {
        object ([EventingStatus](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#EventingStatus))
      },
      "eventsListenerEndpoint": string,
      "eventsListenerPscSa": string,
    
      // Union field eventing_setup_data can be only one of the following:
      "webhookData": {
        object ([WebhookData](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#WebhookData))
      },
      "webhookSubscriptions": {
        object ([WebhookSubscriptions](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#WebhookSubscriptions))
      }
      // End of list of possible types for union field eventing_setup_data.
    }  
  
Fields  
---  
`status` |  `object (`[EventingStatus](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#EventingStatus)`)` Output only. Current status of eventing.  
`eventsListenerEndpoint` |  `string` Output only. Events listener endpoint. The value will populated after provisioning the events listener.  
`eventsListenerPscSa` |  `string` Output only. Events listener PSC Service attachment. The value will be populated after provisioning the events listener with private connectivity enabled.  
Union field `eventing_setup_data`. Setup data for eventing type enabled. `eventing_setup_data` can be only one of the following:  
`webhookData` |  `object (`[WebhookData](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#WebhookData)`)` Output only. Webhook data.  
`webhookSubscriptions` |  `object (`[WebhookSubscriptions](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#WebhookSubscriptions)`)` Output only. Webhook subscriptions.  
  
## EventingStatus

EventingStatus indicates the state of eventing.

JSON representation  
---  
      
    
    {
      "state": enum ([State](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#State_1)),
      "description": string
    }  
  
Fields  
---  
`state` |  `enum (`[State](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#State_1)`)` Output only. State.  
`description` |  `string` Output only. Description of error if State is set to "ERROR".  
  
## State

All the possible Eventing States.

Enums  
---  
`STATE_UNSPECIFIED` | Default state.  
`ACTIVE` | Eventing is enabled and ready to receive events.  
`ERROR` | Eventing is not active due to an error.  
`INGRESS_ENDPOINT_REQUIRED` | Ingress endpoint required.  
  
## WebhookData

WebhookData has details of webhook configuration.

JSON representation  
---  
      
    
    {
      "name": string,
      "id": string,
      "additionalVariables": [
        {
          object ([ConfigVariable](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/ConfigVariable))
        }
      ],
      "createTime": string,
      "updateTime": string,
      "nextRefreshTime": string
    }  
  
Fields  
---  
`name` |  `string` Output only. Name of the Webhook  
`id` |  `string` Output only. ID to uniquely identify webhook.  
`additionalVariables[]` |  `object (`[ConfigVariable](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/ConfigVariable)`)` Output only. Additional webhook related field values.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the webhook was created.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the webhook was last updated.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`nextRefreshTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Next webhook refresh time. Will be null if refresh is not supported.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## WebhookSubscriptions

WebhookSubscriptions has details of webhook subscriptions.

JSON representation  
---  
      
    
    {
      "webhookData": [
        {
          object ([WebhookData](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#WebhookData))
        }
      ]
    }  
  
Fields  
---  
`webhookData[]` |  `object (`[WebhookData](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#WebhookData)`)` Output only. Webhook data.  
  
## ConnectorVersionInfraConfig

This configuration provides infra configs like rate limit threshold which need to be configurable for every connector version

JSON representation  
---  
      
    
    {
      "ratelimitThreshold": string,
      "internalclientRatelimitThreshold": string,
      "hpaConfig": {
        object ([HPAConfig](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/HPAConfig))
      },
      "resourceRequests": {
        object ([ResourceRequests](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/ResourceRequests))
      },
      "resourceLimits": {
        object ([ResourceLimits](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/ResourceLimits))
      },
      "sharedDeployment": string,
      "connectionRatelimitWindowSeconds": string,
      "deploymentModel": enum ([DeploymentModel](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#DeploymentModel)),
      "deploymentModelMigrationState": enum ([DeploymentModelMigrationState](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#DeploymentModelMigrationState)),
      "maxInstanceRequestConcurrency": integer,
      "tlsMigrationState": enum ([TLSMigrationState](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#TLSMigrationState))
    }  
  
Fields  
---  
`ratelimitThreshold` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Max QPS supported by the connector version before throttling of requests.  
`internalclientRatelimitThreshold` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Max QPS supported for internal requests originating from Connd.  
`hpaConfig` |  `object (`[HPAConfig](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/HPAConfig)`)` Output only. HPA autoscaling config.  
`resourceRequests` |  `object (`[ResourceRequests](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/ResourceRequests)`)` Output only. System resource requests.  
`resourceLimits` |  `object (`[ResourceLimits](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/ResourceLimits)`)` Output only. System resource limits.  
`sharedDeployment` |  `string` Output only. The name of shared connector deployment.  
`connectionRatelimitWindowSeconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The window used for ratelimiting runtime requests to connections.  
`deploymentModel` |  `enum (`[DeploymentModel](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#DeploymentModel)`)` Output only. Indicates whether connector is deployed on GKE/CloudRun  
`deploymentModelMigrationState` |  `enum (`[DeploymentModelMigrationState](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#DeploymentModelMigrationState)`)` Output only. Status of the deployment model migration.  
`maxInstanceRequestConcurrency` |  `integer` Output only. Max instance request concurrency.  
`tlsMigrationState` |  `enum (`[TLSMigrationState](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#TLSMigrationState)`)` Output only. Status of the TLS migration.  
  
## DeploymentModel

Enum for different deployment models

Enums  
---  
`DEPLOYMENT_MODEL_UNSPECIFIED` | Deployment model is not specified.  
`GKE_MST` | Default model gke mst.  
`CLOUD_RUN_MST` | Cloud run mst.  
  
## DeploymentModelMigrationState

State of the deployment model migration.

Enums  
---  
`DEPLOYMENT_MODEL_MIGRATION_STATE_UNSPECIFIED` | Deployment model migration state is not specified.  
`IN_PROGRESS` | Deployment model migration is in progress.  
`COMPLETED` | Deployment model migration is completed.  
`ROLLEDBACK` | Deployment model migration rolledback.  
`ROLLBACK_IN_PROGRESS` | Deployment model migration rollback in progress.  
  
## TLSMigrationState

State of the TLS migration.

Enums  
---  
`TLS_MIGRATION_STATE_UNSPECIFIED` | TLS migration state is not specified.  
`TLS_MIGRATION_NOT_STARTED` | TLS migration is in progress.  
`TLS_MIGRATION_COMPLETED` | TLS migration is completed.  
  
## BillingConfig

Billing config for the connection.

JSON representation  
---  
      
    
    {
      "billingCategory": enum ([BillingCategory](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#BillingCategory))
    }  
  
Fields  
---  
`billingCategory` |  `enum (`[BillingCategory](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#BillingCategory)`)` Output only. Billing category for the connector.  
  
## BillingCategory

BillingCategory is an enum to indicate billing category.

Enums  
---  
`BILLING_CATEGORY_UNSPECIFIED` | Billing category is not specified.  
`GCP_AND_TECHNICAL_CONNECTOR` | GCP/Technical connector.  
`NON_GCP_CONNECTOR` | Non-GCP connector.  
  
## TrafficShapingConfig

  * TrafficShapingConfig defines the configuration for shaping API traffic by specifying a quota limit and the duration over which this limit is enforced. This configuration helps to control and manage the rate at which API calls are made on the client side, preventing service overload on the backend.



For example: - if the quota limit is 100 calls per 10 seconds, then the message would be: { quotaLimit: 100 duration: { seconds: 10 } }

  * if the quota limit is 100 calls per 5 minutes, then the message would be: { quotaLimit: 100 duration: { seconds: 300 } }

  * if the quota limit is 10000 calls per day, then the message would be: { quotaLimit: 10000 duration: { seconds: 86400 } and so on.


JSON representation  
---  
      
    
    {
      "quotaLimit": string,
      "duration": string
    }  
  
Fields  
---  
`quotaLimit` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. Maximum number of api calls allowed.  
`duration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Required. * The duration over which the API call quota limits are calculated.This duration is used to define the time window for evaluating if the number of API calls made by a user is within the allowed quota limits.For example: - To define a quota sampled over 16 seconds, set `seconds` to 16 - To define a quota sampled over 5 minutes, set `seconds` to 300 (5 * 60) - To define a quota sampled over 1 day, set `seconds` to 86400 (24 * 60 * 60) and so on.It is important to note that this duration is not the time the quota is valid for, but rather the time window over which the quota is evaluated.For example, if the quota is 100 calls per 10 seconds, then this duration field would be set to 10 seconds.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections/create)`

|  Creates a new Connection in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections/delete)`

|  Deletes a single Connection.  
  
### `[get](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections/get)`

|  Gets details of a single Connection.  
  
### `[getConnectionSchemaMetadata](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections/getConnectionSchemaMetadata)`

|  Gets schema metadata of a connection.  
  
### `[getIamPolicy](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections/list)`

|  Lists Connections in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections/patch)`

|  Updates the parameters of a single Connection.  
  
### `[repairEventing](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections/repairEventing)`

|  RepaiEventing tries to repair eventing related event subscriptions.  
  
### `[search](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections/search)`

|  Returns Top matching Connections for a given query.  
  
### `[setIamPolicy](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
