---
url: https://docs.cloud.google.com/app-hub/docs/supported-resources/
title: App Hub supported resources \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:16:37.097469+00:00
---

# App Hub supported resources  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-hub/docs/supported-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ App Hub ](https://docs.cloud.google.com/app-hub)
  * [ Guides ](https://docs.cloud.google.com/app-hub/docs/overview)



Send feedback 

#  App Hub supported resources Stay organized with collections  Save and categorize content based on your preferences. 

App Hub supports the global and regional Google Cloud resources listed on this page that you can register as services or workloads in App Hub applications. To programmatically register these underlying Google Cloud resources, you must use the correct Uniform Resource Identifier (URI) format as defined in the [Cloud Asset Inventory documentation](https://docs.cloud.google.com/asset-inventory/docs/asset-names).

You can monitor your applications, services, and workloads. For more information on this telemetry data, see [View application telemetry](https://docs.cloud.google.com/monitoring/docs/application-monitoring).

**Important:** When infrastructure resources with App Hub support are created or destroyed, the resource's `Service` metadata, specifically the [resource URIs](https://docs.cloud.google.com/app-hub/docs/reference/rest/v1/ServiceReference), are automatically ingested into App Hub. This process lets App Hub maintain up-to-date information and improves the application creation and management experience. This metadata ingestion is an always-on process, and the ingested metadata is only accessible when you explicitly enable App Hub.

## Services

This section lists all the Google Cloud resources that App Hub supports as application components and that you can register as [services](https://docs.cloud.google.com/app-hub/docs/key-concepts#service) in your applications.

Google Cloud product |  Infrastructure resource |  Registration type |  URI format  
---|---|---|---  
Client App Manager | 

  * `clientappmanager.googleapis.com/ClientApp` ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|  Exclusive |   
Firebase | 

  * `firebaseapphosting.googleapis.com/Backend` ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|  Exclusive |   
Mesh Configuration | 

  * `networking.istio.io/VirtualService`

|  Exclusive |   
agentregistry.googleapis.com | 

  * `agentregistry.googleapis.com/GoogleMcpServer` ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|  Shared |   
  
  * `agentregistry.googleapis.com/Service` ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|  Exclusive |   
Vertex AI [API reference](https://aiplatform.googleapis.com/$discovery/rest?version=v1) | 

  * [`aiplatform.googleapis.com/Dataset`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.datasets)

|  Exclusive |  `//aiplatform.googleapis.com/projects/PROJECT_NUMBER/locations/LOCATION/datasets/DATASET`  
  
  * [`aiplatform.googleapis.com/Endpoint`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.endpoints)

|  Exclusive |  `//aiplatform.googleapis.com/projects/PROJECT_NUMBER/locations/LOCATION/endpoints/ENDPOINT`  
  
  * [`aiplatform.googleapis.com/FeatureOnlineStore`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featureOnlineStores) ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|  Exclusive |  `//aiplatform.googleapis.com/projects/PROJECT_NUMBER/locations/LOCATION/featureOnlineStores/FeatureOnlineStore`  
  
  * [`aiplatform.googleapis.com/Featurestore`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featurestores)

|  Exclusive |  `//aiplatform.googleapis.com/projects/PROJECT_NUMBER/locations/LOCATION/featurestores/FEATURESTORE`  
  
  * [`aiplatform.googleapis.com/MetadataStore`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.metadataStores)

|  Exclusive |  `//aiplatform.googleapis.com/projects/PROJECT_NUMBER/locations/LOCATION/metadataStores/METADATA_STORE`  
  
  * [`aiplatform.googleapis.com/Model`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.models)

|  Exclusive |  `//aiplatform.googleapis.com/projects/PROJECT_NUMBER/locations/LOCATION/models/MODEL`  
  
  * [`aiplatform.googleapis.com/NotebookExecutionJob`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.notebookExecutionJobs)

|  Exclusive |  `//aiplatform.googleapis.com/projects/PROJECT_NUMBER/locations/LOCATION/notebookExecutionJobs/NOTEBOOK_EXECUTION_JOB`  
  
  * [`aiplatform.googleapis.com/NotebookRuntime`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.notebookRuntimes)

|  Exclusive |  `//aiplatform.googleapis.com/projects/PROJECT_NUMBER/locations/LOCATION/notebookRuntimes/NOTEBOOK_RUNTIME`  
  
  * `aiplatform.googleapis.com/PersistentResource` ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|  Exclusive |   
  
  * [`aiplatform.googleapis.com/Tensorboard`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.tensorboards) ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|  Exclusive |  `//aiplatform.googleapis.com/projects/PROJECT_NUMBER/locations/LOCATION/tensorboards/TENSORBOARD`  
AlloyDB for PostgreSQL [API reference](https://alloydb.googleapis.com/$discovery/rest?version=v1) | 

  * [`alloydb.googleapis.com/Cluster`](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters)

|  Exclusive |  `//alloydb.googleapis.com/projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER`  
  
  * [`alloydb.googleapis.com/Instance`](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.instances)

|  Exclusive |  `//alloydb.googleapis.com/projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER/instances/INSTANCE`  
API Gateway [API reference](https://apigateway.googleapis.com/$discovery/rest?version=v1) | 

  * [`apigateway.googleapis.com/Api`](https://docs.cloud.google.com/api-gateway/docs/reference/rest/v1/projects.locations.apis) ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|  Exclusive |  `//apigateway.googleapis.com/projects/PROJECT_ID/locations/LOCATION/apis/API`  
  
  * [`apigateway.googleapis.com/Gateway`](https://docs.cloud.google.com/api-gateway/docs/reference/rest/v1/projects.locations.gateways) ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|  Exclusive |  `//apigateway.googleapis.com/projects/PROJECT_ID/locations/LOCATION/gateways/GATEWAY`  
Apigee API hub | 

  * `apihub.googleapis.com/Deployment` ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|  Exclusive |   
BigQuery [API reference](https://bigquery.googleapis.com/$discovery/rest?version=v2) | 

  * [`bigquery.googleapis.com/Dataset`](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/datasets) ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|  Exclusive |  `//bigquery.googleapis.com/projects/PROJECT_ID/datasets/DATA_SET`  
Bigtable [API reference](https://bigtableadmin.googleapis.com/$discovery/rest?version=v2) | 

  * [`bigtableadmin.googleapis.com/AuthorizedView`](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.tables.authorizedViews) ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|  Exclusive |  `//bigtable.googleapis.com/projects/PROJECT_ID/instances/INSTANCE/tables/TABLE/authorizedViews/AUTHORIZED_VIEW`  
  
  * [`bigtableadmin.googleapis.com/Cluster`](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.clusters)

|  Exclusive |  `//bigtable.googleapis.com/projects/PROJECT_ID/instances/INSTANCE/clusters/CLUSTER`  
  
  * [`bigtableadmin.googleapis.com/Instance`](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances)

|  Exclusive |  `//bigtable.googleapis.com/projects/PROJECT_ID/instances/INSTANCE`  
  
  * [`bigtableadmin.googleapis.com/LogicalView`](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.logicalViews) ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|  Exclusive |  `//bigtable.googleapis.com/projects/PROJECT_ID/instances/INSTANCE/logicalViews/LOGICAL_VIEW`  
  
  * [`bigtableadmin.googleapis.com/Table`](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.tables) ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|  Exclusive |  `//bigtable.googleapis.com/projects/PROJECT_ID/instances/INSTANCE/tables/TABLE`  
Cloud Build [API reference](https://cloudbuild.googleapis.com/$discovery/rest?version=v1) | 

  * [`cloudbuild.googleapis.com/Connection`](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections)

|  Exclusive |  `//cloudbuild.googleapis.com/projects/PROJECT_ID/locations/LOCATION/connections/CONNECTION`  
  
  * `cloudbuild.googleapis.com/Installation` ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|  Exclusive |   
Certificate Manager [API reference](https://certificatemanager.googleapis.com/$discovery/rest?version=v1) | 

  * [`certificatemanager.googleapis.com/Certificate`](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rest/v1/projects.locations.certificates) ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|  Exclusive |  `//certificatemanager.googleapis.com/projects/PROJECT_ID/locations/REGION/certificates/CERTIFICATE_NAME`  
  
  * [`certificatemanager.googleapis.com/CertificateMap`](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rest/v1/projects.locations.certificateMaps) ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|  Exclusive |  `//certificatemanager.googleapis.com/projects/PROJECT_ID/locations/global/certificateMaps/CERTIFICATE_MAP_NAME`  
Cloud Run [API reference](https://run.googleapis.com/$discovery/rest?version=v1) | 

  * [`run.googleapis.com/Service`](https://docs.cloud.google.com/run/docs/reference/rest/v1/namespaces.services)

|  Exclusive |  `//run.googleapis.com/projects/PROJECT_ID/locations/LOCATION/services/SERVICE`  
Cloud Tasks [API reference](https://cloudtasks.googleapis.com/$discovery/rest?version=v2) | 

  * [`cloudtasks.googleapis.com/Queue`](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues) ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|  Exclusive |  `//cloudtasks.googleapis.com/projects/PROJECT_NUMBER/locations/LOCATION/queues/QUEUE`  
Cloud Data Fusion [API reference](https://datafusion.googleapis.com/$discovery/rest) | 

  * [`datafusion.googleapis.com/Instance`](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances)

|  Exclusive |  `//datafusion.googleapis.com/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE`  
Dataform [API reference](https://dataform.googleapis.com/$discovery/rest?version=v1beta1) | 

  * [`dataform.googleapis.com/Repository`](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories) ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|  Exclusive |  `//dataform.googleapis.com/projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY`  
Dataproc Metastore [API reference](https://metastore.googleapis.com/$discovery/rest?version=v1) | 

  * [`metastore.googleapis.com/Service`](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services)

|  Exclusive |  `//metastore.googleapis.com/projects/PROJECT_ID/locations/LOCATION/services/SERVICE`  
Managed Service for Apache Spark [API reference](https://dataproc.googleapis.com/$discovery/rest?version=v1) | 

  * [`dataproc.googleapis.com/Cluster`](https://docs.cloud.google.com/dataproc/docs/reference/rest/v1/projects.regions.clusters) ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|  Exclusive |  `//dataproc.googleapis.com/projects/PROJECT_ID/regions/REGION/clusters/CLUSTER`  
Datastream [API reference](https://datastream.googleapis.com/$discovery/rest) | 

  * [`datastream.googleapis.com/Stream`](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.streams) ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|  Exclusive |  `//datastream.googleapis.com/projects/PROJECT_ID/locations/LOCATION/streams/STREAM`  
Cloud Deploy [API reference](https://clouddeploy.googleapis.com/$discovery/rest?version=v1) | 

  * [`clouddeploy.googleapis.com/CustomTargetType`](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.customTargetTypes)

|  Exclusive |  `//clouddeploy.googleapis.com/projects/PROJECT_ID/locations/LOCATION/customTargetTypes/CUSTOM_TARGET_TYPE`  
  
  * [`clouddeploy.googleapis.com/DeliveryPipeline`](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines)

|  Exclusive |  `//clouddeploy.googleapis.com/projects/PROJECT_ID/locations/LOCATION/deliveryPipelines/DELIVERY_PIPELINE`  
  
  * [`clouddeploy.googleapis.com/Release`](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases)

|  Exclusive |  `//clouddeploy.googleapis.com/projects/PROJECT_ID/locations/LOCATION/deliveryPipelines/DELIVERY_PIPELINE/releases/RELEASE`  
Discovery Engine | 

  * `discoveryengine.googleapis.com/DataConnector` ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|  Shared |   
Eventarc [API reference](https://eventarc.googleapis.com/$discovery/rest?version=v1) | 

  * [`eventarc.googleapis.com/Channel`](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.channels) ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|  Exclusive |  `//eventarc.googleapis.com/projects/PROJECT_ID/locations/LOCATION/channels/CHANNEL`  
  
  * [`eventarc.googleapis.com/Trigger`](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.triggers) ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|  Exclusive |  `//eventarc.googleapis.com/projects/PROJECT_ID/locations/LOCATION/triggers/TRIGGER`  
Financial Services [API reference](https://financialservices.googleapis.com/$discovery/rest?version=v1) | 

  * `financialservices.googleapis.com/Dataset` ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|  Exclusive |  `//financialservices.googleapis.com/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE/datasets/DATASET`  
  
  * `financialservices.googleapis.com/Instance`

|  Exclusive |  `//financialservices.googleapis.com/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE`  
  
  * `financialservices.googleapis.com/Model` ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|  Exclusive |  `//financialservices.googleapis.com/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE/models/MODEL`  
Firestore [API reference](https://firestore.googleapis.com/$discovery/rest?version=v1) | 

  * [`firestore.googleapis.com/Database`](https://docs.cloud.google.com/firestore/docs/reference/rest/v1/projects.databases)

|  Exclusive |  `//firestore.googleapis.com/projects/PROJECT_NUMBER/databases/DATABASE`  
Cloud Run functions (1st gen) [API reference](https://cloudfunctions.googleapis.com/$discovery/rest) | 

  * [`cloudfunctions.googleapis.com/CloudFunction`](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions) ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|  Exclusive |  `//cloudfunctions.googleapis.com/projects/PROJECT_ID/locations/LOCATION/functions/CLOUD_FUNCTION`  
  
  * [`cloudfunctions.googleapis.com/Function`](https://docs.cloud.google.com/functions/docs/reference/rest/v2/projects.locations.functions)

|  Exclusive |  `//cloudfunctions.googleapis.com/projects/PROJECT_ID/locations/LOCATION/functions/FUNCTION`  
Compute Engine [API reference](https://www.googleapis.com/discovery/v1/apis/compute/v1/rest?version=v1) | 

  * [`compute.googleapis.com/BackendService`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices)

|  Exclusive |  `//compute.googleapis.com/projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE`  
  
  * [`compute.googleapis.com/ForwardingRule`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules)

|  Exclusive |  `//compute.googleapis.com/projects/PROJECT_ID/regions/REGION/forwardingRules/FORWARDING_RULE` `//compute.googleapis.com/projects/PROJECT_ID/global/forwardingRules/FORWARDING_RULE`  
  
  * [`compute.googleapis.com/ServiceAttachment`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/serviceAttachments) ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|  Exclusive |  `//compute.googleapis.com/projects/PROJECT_ID/regions/REGION/serviceAttachments/SERVICE_ATTACHMENT`  
GKE Hub [API reference](https://gkehub.googleapis.com/$discovery/rest?version=v1) | 

  * [`gkehub.googleapis.com/Fleet`](https://docs.cloud.google.com/anthos/fleet-management/docs/reference/rest/v1/projects.locations.fleets) ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|  Exclusive |  `//gkehub.googleapis.com/projects/PROJECT_ID/locations/LOCATION/fleets/FLEET`  
Google Kubernetes Engine [API reference](https://container.googleapis.com/$discovery/rest?version=v1) | 

  * [`container.googleapis.com/Cluster`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters) ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|  Shared |  `//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER` `//container.googleapis.com/projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER`  
  
  * [`gateway.networking.k8s.io/Gateway`](https://kubernetes.io/docs/concepts/services-networking/gateway/)

|  Exclusive |  `//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER/k8s/namespaces/NAMESPACE/apis/gateway.networking.k8s.io/gateways/GATEWAY` `//container.googleapis.com/projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER/k8s/namespaces/NAMESPACE/apis/gateway.networking.k8s.io/gateways/GATEWAY`  
  
  * [`k8s.io/Service`](https://kubernetes.io/docs/reference/kubernetes-api/service-resources/service-v1/)

|  Exclusive |  `//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER/k8s/namespaces/NAMESPACE/services/SERVICE` `//container.googleapis.com/projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER/k8s/namespaces/NAMESPACE/services/SERVICE`  
  
  * [`networking.k8s.io/Ingress`](https://kubernetes.io/docs/reference/kubernetes-api/service-resources/ingress-v1/) ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|  Exclusive |  `//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER/k8s/namespaces/NAMESPACE/networking.k8s.io/ingresses/INGRESS` `//container.googleapis.com/projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER/k8s/namespaces/NAMESPACE/networking.k8s.io/ingresses/INGRESS`  
GKE On-Prem API [API reference](https://gkeonprem.googleapis.com/$discovery/rest?version=v1) | 

  * [`gkeonprem.googleapis.com/VmwareAdminCluster`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters) ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|  Exclusive |  `//gkeonprem.googleapis.com/projects/PROJECT_ID/locations/LOCATION/vmwareAdminClusters/VMWARE_ADMIN_CLUSTER`  
  
  * [`gkeonprem.googleapis.com/VmwareCluster`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters) ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|  Exclusive |  `//gkeonprem.googleapis.com/projects/PROJECT_ID/locations/LOCATION/vmwareClusters/VMWARE_CLUSTER`  
Integration Connectors [API reference](https://connectors.googleapis.com/$discovery/rest?version=v1) | 

  * [`connectors.googleapis.com/Connection`](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections) ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|  Exclusive |  `//connectors.googleapis.com/projects/PROJECT_ID/locations/LOCATION/connections/CONNECTION`  
Live Stream API [API reference](https://livestream.googleapis.com/$discovery/rest?version=v1) | 

  * [`livestream.googleapis.com/Asset`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.assets) ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|  Exclusive |  `//livestream.googleapis.com/projects/PROJECT_ID/locations/LOCATION/assets/ASSET`  
Cloud Logging [API reference](https://logging.googleapis.com/$discovery/rest?version=v2) | 

  * [`logging.googleapis.com/LogBucket`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.buckets)

|  Exclusive |  `//logging.googleapis.com/projects/PROJECT_NUMBER/locations/LOCATION/buckets/BUCKET` `//logging.googleapis.com/organizations/ORGANIZATION_ID/locations/LOCATION/buckets/BUCKET` `//logging.googleapis.com/folders/FOLDER_ID/locations/LOCATION/buckets/BUCKET` `//logging.googleapis.com/billingAccounts/BILLING_ACCOUNT_ID/locations/LOCATION/buckets/BUCKET` `//logging.googleapis.com/accessPolicies/ACCESS_POLICY_ID/locations/LOCATION/buckets/BUCKET`  
Managed Service for Microsoft Active Directory [API reference](https://managedidentities.googleapis.com/$discovery/rest) | 

  * [`managedidentities.googleapis.com/Domain`](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains)

|  Exclusive |  `//managedidentities.googleapis.com/projects/PROJECT_ID/locations/global/domains/DOMAIN`  
Memorystore | 

  * [`memorystore.googleapis.com/Instance`](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances)

|  Exclusive |  `//memorystore.googleapis.com/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE`  
Memorystore for Memcached [API reference](https://memcache.googleapis.com/$discovery/rest?version=v1) | 

  * [`memcache.googleapis.com/Instance`](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1/projects.locations.instances) ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|  Exclusive |  `//memcache.googleapis.com/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE`  
Memorystore for Redis [API reference](https://redis.googleapis.com/$discovery/rest?version=v1) | 

  * [`redis.googleapis.com/Cluster`](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters)

|  Exclusive |  `//redis.googleapis.com/projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER`  
  
  * [`redis.googleapis.com/Instance`](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances)

|  Exclusive |  `//redis.googleapis.com/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE`  
Network Connectivity [API reference](https://networkconnectivity.googleapis.com/$discovery/rest?version=v1) | 

  * [`networkconnectivity.googleapis.com/Group`](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs.groups) ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|  Exclusive |  `//networkconnectivity.googleapis.com/projects/PROJECT_ID/locations/global/hubs/HUB/groups/GROUP`  
  
  * [`networkconnectivity.googleapis.com/Hub`](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs) ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|  Exclusive |  `//networkconnectivity.googleapis.com/projects/PROJECT_ID/locations/global/hubs/HUB`  
  
  * [`networkconnectivity.googleapis.com/InternalRange`](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.internalRanges)

|  Exclusive |  `//networkconnectivity.googleapis.com/projects/PROJECT_ID/locations/LOCATION/internalRanges/INTERNAL_RANGE`  
  
  * `networkconnectivity.googleapis.com/PolicyBasedRoute`

|  Exclusive |   
  
  * [`networkconnectivity.googleapis.com/Spoke`](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.spokes) ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|  Exclusive |  `//networkconnectivity.googleapis.com/projects/PROJECT_ID/locations/LOCATION/spokes/SPOKE`  
Pub/Sub [API reference](https://pubsub.googleapis.com/$discovery/rest?version=v1) | 

  * [`pubsub.googleapis.com/Subscription`](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions)

|  Exclusive |  `//pubsub.googleapis.com/projects/PROJECT_ID/subscriptions/SUBSCRIPTION`  
  
  * [`pubsub.googleapis.com/Topic`](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.topics)

|  Exclusive |  `//pubsub.googleapis.com/projects/PROJECT_ID/topics/TOPIC` `//pubsub.googleapis.com/_deleted-topic_`  
Secret Manager [API reference](https://secretmanager.googleapis.com/$discovery/rest?version=v1) | 

  * [`secretmanager.googleapis.com/Secret`](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets)

|  Exclusive |  `//secretmanager.googleapis.com/projects/PROJECT_NUMBER/secrets/SECRET` `//secretmanager.googleapis.com/projects/PROJECT_NUMBER/locations/LOCATION/secrets/SECRET`  
Spanner [API reference](https://spanner.googleapis.com/$discovery/rest?version=v1) | 

  * [`spanner.googleapis.com/Database`](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases)

|  Exclusive |  `//spanner.googleapis.com/projects/PROJECT_ID/instances/INSTANCE/databases/DATABASE`  
  
  * [`spanner.googleapis.com/Instance`](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances)

|  Exclusive |  `//spanner.googleapis.com/projects/PROJECT_ID/instances/INSTANCE`  
Cloud SQL [API reference](https://sqladmin.googleapis.com/$discovery/rest?version=v1beta4) | 

  * [`sqladmin.googleapis.com/Instance`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances)

|  Exclusive |  `//cloudsql.googleapis.com/projects/PROJECT_ID/instances/INSTANCE`  
Cloud Storage [API reference](https://storage.googleapis.com/$discovery/rest?version=v1) | 

  * [`storage.googleapis.com/Bucket`](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets)

|  Exclusive |  `//storage.googleapis.com/BUCKET`  
Service Usage [API reference](https://serviceusage.googleapis.com/$discovery/rest?version=v1) | 

  * [`serviceusage.googleapis.com/Service`](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1/services) ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|  Exclusive |  `//serviceusage.googleapis.com/projects/PROJECT_NUMBER/services/SERVICE`  
Workflows [API reference](https://workflows.googleapis.com/$discovery/rest?version=v1) | 

  * [`workflows.googleapis.com/Workflow`](https://docs.cloud.google.com/workflows/docs/reference/rest/v1/projects.locations.workflows) ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|  Exclusive |  `//workflows.googleapis.com/projects/PROJECT_ID/locations/LOCATION/workflows/WORKFLOW`  
  
## Workloads

This section lists all the Google Cloud resources that App Hub supports as application components and that you can register as [workloads](https://docs.cloud.google.com/app-hub/docs/key-concepts#workload) in your applications.

Google Cloud product |  Infrastructure resource |  URI format  
---|---|---  
geminidataanalytics.googleapis.com | 

  * `geminidataanalytics.googleapis.com/DataAgent` ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|   
Vertex AI [API reference](https://aiplatform.googleapis.com/$discovery/rest?version=v1) | 

  * [`aiplatform.googleapis.com/BatchPredictionJob`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.batchPredictionJobs) ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|  `//aiplatform.googleapis.com/projects/PROJECT_NUMBER/locations/LOCATION/batchPredictionJobs/BATCH_PREDICTION_JOB`  
  
  * [`aiplatform.googleapis.com/ReasoningEngine`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.reasoningEngines)

|  `//aiplatform.googleapis.com/projects/PROJECT_NUMBER/locations/LOCATION/reasoningEngines/REASONING_ENGINE`  
  
  * [`aiplatform.googleapis.com/TuningJob`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.tuningJobs) ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|  `//aiplatform.googleapis.com/projects/PROJECT_NUMBER/locations/LOCATION/tuningJobs/TUNING_JOB`  
Cloud Build [API reference](https://cloudbuild.googleapis.com/$discovery/rest?version=v1) | 

  * [`cloudbuild.googleapis.com/WorkerPool`](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.workerPools)

|  `//cloudbuild.googleapis.com/projects/PROJECT_NUMBER/locations/LOCATION/workerPools/WORKER_POOL`  
Cloud Run [API reference](https://run.googleapis.com/$discovery/rest?version=v1) | 

  * [`run.googleapis.com/Job`](https://docs.cloud.google.com/run/docs/reference/rest/v1/namespaces.jobs)

|  `//run.googleapis.com/projects/PROJECT_ID/locations/LOCATION/jobs/JOB`  
  
  * [`run.googleapis.com/WorkerPool`](https://docs.cloud.google.com/run/docs/reference/rest/v1/projects.locations.workerpools) ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|  `//run.googleapis.com/projects/PROJECT_ID/locations/LOCATION/workerPools/WORKER_POOL`  
Cloud Config Manager API [API reference](https://config.googleapis.com/$discovery/rest?version=v1) | 

  * [`config.googleapis.com/Deployment`](https://docs.cloud.google.com/infrastructure-manager/docs/reference/rest/v1/projects.locations.deployments) ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|  `//config.googleapis.com/projects/PROJECT_ID/locations/LOCATION/deployments/DEPLOYMENT`  
Discovery Engine | 

  * `discoveryengine.googleapis.com/Agent` ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|   
  
  * [`discoveryengine.googleapis.com/Assistant`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.assistants) ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|  `//discoveryengine.googleapis.com/projects/PROJECT_NUMBER/locations/LOCATION/collections/COLLECTION/engines/ENGINE/assistants/ASSISTANT`  
Compute Engine [API reference](https://www.googleapis.com/discovery/v1/apis/compute/v1/rest?version=v1) | 

  * [`compute.googleapis.com/InstanceGroup`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroups)

|  `//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instanceGroups/INSTANCE_GROUP` `//compute.googleapis.com/projects/PROJECT_ID/regions/REGION/instanceGroups/INSTANCE_GROUP`  
Google Kubernetes Engine [API reference](https://container.googleapis.com/$discovery/rest?version=v1) | 

  * [`apps.k8s.io/DaemonSet`](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/)

|  `//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER/k8s/namespaces/NAMESPACE/apps/daemonsets/DAEMONSET` `//container.googleapis.com/projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER/k8s/namespaces/NAMESPACE/apps/daemonsets/DAEMONSET`  
  
  * [`apps.k8s.io/Deployment`](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/deployment-v1/)

|  `//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER/k8s/namespaces/NAMESPACE/apps/deployments/DEPLOYMENT` `//container.googleapis.com/projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER/k8s/namespaces/NAMESPACE/apps/deployments/DEPLOYMENT`  
  
  * [`apps.k8s.io/StatefulSet`](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)

|  `//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER/k8s/namespaces/NAMESPACE/apps/statefulsets/STATEFULSET` `//container.googleapis.com/projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER/k8s/namespaces/NAMESPACE/apps/statefulsets/STATEFULSET`  
  
  * [`batch.k8s.io/CronJob`](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/)

|  `//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER/k8s/namespaces/NAMESPACE/batch/cronjobs/CRONJOB` `//container.googleapis.com/projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER/k8s/namespaces/NAMESPACE/batch/cronjobs/CRONJOB`  
Cloud Scheduler | 

  * `cloudscheduler.googleapis.com/Job` ([Preview](https://cloud.google.com/products#product-launch-stages)) 

|   
  
## What's next

  * [Choose your application setup model](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub)
  * [Learn more about App Hub](https://docs.cloud.google.com/app-hub/docs/overview)
  * [Identify App Hub roles and permissions](https://docs.cloud.google.com/app-hub/docs/roles-permissions)
  * [Learn more about Cloud Asset Inventory asset names](https://docs.cloud.google.com/asset-inventory/docs/asset-names)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
