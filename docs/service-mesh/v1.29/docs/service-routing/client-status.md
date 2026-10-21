---
url: https://docs.cloud.google.com/service-mesh/v1.29/docs/service-routing/client-status/
title: Understand Cloud Service Mesh client status \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:09:49.970970+00:00
---

# Understand Cloud Service Mesh client status  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.29/docs/service-routing/client-status/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.29/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.29/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.29/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Understand Cloud Service Mesh client status

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.29/docs/overview).

When you use Cloud Service Mesh to handle your application networking, consider the following two primary components:

  * **The infrastructure layer.** The infrastructure layer, such as Envoy sidecar proxies or proxyless gRPC libraries, is configured to handle networking on behalf of your applications.
  * **The control plane, Cloud Service Mesh.** The control plane generates configuration for, and distributes configuration to, the infrastructure layer.



When an Envoy proxy or the gRPC library is initialized, it uses xDS APIs to connect to Cloud Service Mesh. The proxy or the library acts as a client to Cloud Service Mesh. After a connection is established between the client and Cloud Service Mesh, Cloud Service Mesh sends configuration information back to the client and updates the configuration as needed.

It is sometimes helpful to understand which clients are connected to Cloud Service Mesh or to inspect the configuration that Cloud Service Mesh generates for its clients. For example, you might want to debug an issue, or you might want to understand how the actions that you took when configuring Cloud Service Mesh affect the configuration that your clients see.

Cloud Service Mesh supports the [Client Status Discovery Service](https://www.envoyproxy.io/docs/envoy/latest/api-v3/service/status/v3/csds.proto.html) (CSDS) API. You use a CSDS client to query this API. This enables you to see which clients are connected to Cloud Service Mesh and to inspect the configuration that Cloud Service Mesh generates for its clients.

The CSDS client is an open source tool that you can obtain from the [Envoy repository](https://github.com/envoyproxy/envoy-tools/blob/master/csds-client/README.md). The following diagram illustrates how the CSDS client queries Cloud Service Mesh for information about Cloud Service Mesh's CSDS API.

[ ![Using the CSDS API to obtain configuration information about Cloud Service Mesh clients.](https://docs.cloud.google.com/static/service-mesh/v1.29/docs/images/td-client-status.svg)](https://docs.cloud.google.com/static/service-mesh/v1.29/docs/images/td-client-status.svg) Using the CSDS API to obtain configuration information about Cloud Service Mesh clients (click to enlarge)

The CSDS client connects to Cloud Service Mesh and presents a project number and network name, along with a set of credentials. Cloud Service Mesh can then respond with information about the various Cloud Service Mesh clients to which it is connected.

For more information about the CSDS client, see the [README file](https://github.com/envoyproxy/envoy-tools/blob/master/csds-client/README.md).

## Prerequisites

To connect to the CSDS API, you need a CSDS client. You can obtain the client in one of two ways:

  1. You can build the client by using Cloud Shell.
  2. You can build the client on a local development machine.



### Build the CSDS client by using Cloud Shell

To use Cloud Shell to build the CSDS client, do the following:

  1. Reset Cloud Shell by using the instructions in [Disabling or resetting Cloud Shell](https://docs.cloud.google.com/shell/docs/resetting-cloud-shell). This ensures that existing configurations do not interfere with your build.
  2. In the Google Cloud console, [open a new Cloud Shell session](https://docs.cloud.google.com/shell/docs/using-cloud-shell#starting_a_new_session).
  3. Run the following command to obtain the source code that you use to build the CSDS client:
         
         git clone https://github.com/envoyproxy/envoy-tools.git
         

  4. Navigate to the CSDS client directory and run the following commands:
         
         cd envoy-tools/csds-client/
         make init
         make build
         

  5. After the build is complete, test it with the following command:
         
         csds-client -help
         




If the build is successful, you see the help text for the client.

### Build the CSDS client on a local development machine

You can download and build a CSDS client on a local machine by following the instructions in the [README file](https://github.com/envoyproxy/envoy-tools/blob/master/csds-client/README.md) in the open source repository. To do this, you must also have Go and the `make` tool set up in your environment. If you prefer not to do this, use the preceding instructions for Cloud Shell, in which Go and the `make` tool are provided for you.

### Additional prerequisites

  1. Make sure that the [node ID](https://github.com/envoyproxy/envoy/blob/master/api/envoy/api/v2/core/base.proto#L139) of each client is unique within the service mesh. If multiple clients share the same node ID, only one configuration is returned—the configuration for the client that most recently connected to Cloud Service Mesh.

If you use Google's reference packages, you do not need to manually set the node ID in your bootstrap files; a node ID is generated for you. If you do not use the reference packages, you must manually set the node ID in each of your bootstrap files.

  2. Ensure that you have access to a user account that has the [Identity and Access Management (IAM) permissions required to configure Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.29/docs/onboarding/prepare-service-routing-envoy-proxyless#grant-permissions). The following instructions use the Google Cloud CLI to generate and automatically supply the credentials needed by the CSDS client. Alternatively, you can use the CSDS client and supply the credentials directly.




## Determine which clients are currently connected to Cloud Service Mesh

You can use the CSDS client to determine which clients are connected to your Cloud Service Mesh configuration.

To get this information, you need the following details:

  * The ID of the project from which the credentials were generated.

  * If you're using the service routing APIs, one of the following, depending on which resource the xDS client fetches:

    * The name of the [Mesh](https://docs.cloud.google.com/service-mesh/v1.29/docs/service-routing/service-routing-overview#mesh-resource) resource
    * The [scope](https://docs.cloud.google.com/service-mesh/v1.29/docs/service-routing/service-routing-overview#gateway-resource) parameter on the Gateway resource
  * If you're using the [older APIs](https://docs.cloud.google.com/service-mesh/v1.29/docs/service-routing/overview), the name of the VPC network that you specified when you configured Cloud Service Mesh. This network is the one specified by the [forwarding rule](https://docs.cloud.google.com/service-mesh/v1.29/docs/service-routing/forwarding-rules#forwarding_rule_properties) of the [routing rule map](https://docs.cloud.google.com/service-mesh/v1.29/docs/service-routing/routing-rule-maps).




###  Service routing APIs

  1. From an account that has the [correct permissions](https://docs.cloud.google.com/service-mesh/v1.29/docs/onboarding/prepare-service-routing-envoy-proxyless#grant-permissions), run the following command:
         
         gcloud auth application-default login \
          --billing-project=BILLING_PROJECT_ID
         

  2. Create a new file in the YAML format with the following content.
         
         node_matchers:
           - node_metadatas:
               - path:
                   - key: TRAFFICDIRECTOR_GCP_PROJECT_NUMBER
                 value:
                   string_match:
                     exact: "PROJECT_NUMBER"
               - path:
                   - key: TRAFFICDIRECTOR_MESH_SCOPE_NAME
                 value:
                   string_match:
                     exact: "MESH_OR_SCOPE"
         

Replace the following values:

     * `PROJECT_NUMBER`: the ID of the project
     * `MESH_OR_SCOPE`: if the xDS client fetches a Mesh resource, use a prefix of `mesh:` followed by the actual mesh name; if the xDS client fetches a Gateway resource, use a prefix of `scope:` followed by the name of the scope parameter

**Note:** A CSDS V3 request requires [node.id](https://github.com/envoyproxy/envoy/blob/main/api/envoy/service/status/v3/csds.proto#L87), which represents the node that is making the CSDS request. For Cloud Service Mesh the `node.id` must be in the form `projects/PROJECT_NUMBER/networks/MESH_OR_SCOPE/nodes/NODE_ID`. The CSDS client automatically includes `node.id` in the CSDS V3 request with a randomly generated `<node_id>` portion when the `-platform` option is set to `gcp`.

  1. Run the CSDS client, which uses the credentials generated by the gcloud CLI. Replace `PATH_TO_CSDS_REQUEST_YAML_FILE` with the path to the YAML file that you created in the previous step.
         
         csds-client \
           -service_uri trafficdirector.googleapis.com:443 \
           -platform gcp \
           -authn_mode auto \
           -api_version v3 \
           -request_file PATH_TO_CSDS_REQUEST_YAML_FILE
         

You should see output similar to the following:
         
         Client ID                                          xDS stream type    Config status
         603e3524-d1d6-4a9e-9b26-39bcd633a7cb~10.128.0.5    ADS                N/A
         603e3524-d1d6-4a9e-9b26-39bcd633a7cb~10.128.0.5    LRS                N/A
         8576d4bf-8f10-40b2-920b-bb6a7cf9f34a~10.168.0.3    ADS                N/A
         8576d4bf-8f10-40b2-920b-bb6a7cf9f34a~10.168.0.3    LRS                N/A
         d9577b61-fa3a-41d6-90bd-11c4fdd2f8c0~10.128.0.4    ADS                N/A
         d9577b61-fa3a-41d6-90bd-11c4fdd2f8c0~10.128.0.4    LRS                N/A
         f38a59c1-4428-42f1-be81-e02eb994f9dd~10.128.0.6    ADS                N/A
         f38a59c1-4428-42f1-be81-e02eb994f9dd~10.128.0.6    LRS                N/A
         

The `Client ID` column displays the client IDs of the clients that are connected to Cloud Service Mesh. These client IDs are provided by using the `node_id` field in the bootstrap file used by Envoy or proxyless gRPC when they connect to Cloud Service Mesh.




###  Older APIs

  1. From an account that has the [correct permissions](https://docs.cloud.google.com/service-mesh/v1.29/docs/onboarding/prepare-service-routing-envoy-proxyless#grant-permissions), run the following command:
         
         gcloud auth application-default login \
          --billing-project=BILLING_PROJECT_ID
         

  2. Create a new file in the YAML format with the following content.
         
         node_matchers:
           - node_metadatas:
               - path:
                   - key: TRAFFICDIRECTOR_GCP_PROJECT_NUMBER
                 value:
                   string_match:
                     exact: "PROJECT_NUMBER"
               - path:
                   - key: TRAFFICDIRECTOR_NETWORK_NAME
                 value:
                   string_match:
                     exact: "NETWORK_NAME"
         

Replace the following values:

     * `PROJECT_NUMBER`: the unique ID of the Google Cloud project
     * `NETWORK_NAME`: the VPC network specified by the [forwarding rule](https://docs.cloud.google.com/service-mesh/v1.29/docs/service-routing/forwarding-rules#forwarding_rule_properties) of the routing rule map
  3. Run the CSDS client, which uses the credentials generated by the gcloud CLI. Replace `PATH_TO_CSDS_REQUEST_YAML_FILE` with the path to the YAML file that you created in the previous step.
         
         csds-client \
           -service_uri trafficdirector.googleapis.com:443 \
           -platform gcp \
           -authn_mode auto \
           -api_version v3 \
           -request_file PATH_TO_CSDS_REQUEST_YAML_FILE
         

You should see output similar to the following:
         
         Client ID                                          xDS stream type    Config status
         603e3524-d1d6-4a9e-9b26-39bcd633a7cb~10.128.0.5    ADS                N/A
         603e3524-d1d6-4a9e-9b26-39bcd633a7cb~10.128.0.5    LRS                N/A
         8576d4bf-8f10-40b2-920b-bb6a7cf9f34a~10.168.0.3    ADS                N/A
         8576d4bf-8f10-40b2-920b-bb6a7cf9f34a~10.168.0.3    LRS                N/A
         d9577b61-fa3a-41d6-90bd-11c4fdd2f8c0~10.128.0.4    ADS                N/A
         d9577b61-fa3a-41d6-90bd-11c4fdd2f8c0~10.128.0.4    LRS                N/A
         f38a59c1-4428-42f1-be81-e02eb994f9dd~10.128.0.6    ADS                N/A
         f38a59c1-4428-42f1-be81-e02eb994f9dd~10.128.0.6    LRS                N/A
         

The `Client ID` column displays the client IDs of the clients that are connected to Cloud Service Mesh. These client IDs are provided by using the `node_id` field in the bootstrap file used by Envoy or proxyless gRPC when they connect to Cloud Service Mesh.




## Inspect the configuration for a specific Cloud Service Mesh client

You can inspect the configuration that Cloud Service Mesh sends to a particular client by using the client ID, which you obtained in the previous section.

You can examine the detailed configuration of the resource proto to determine which xDS API version that specific client is using. For example, if you see `envoy.api.v2.Cluster` in the config, it means the client is using the v2 API. If you see `envoy.api.v3.Cluster` in the configuration, it means the client is using the v3 API. Only xDS v3 is supported. For information about how to migrate from v2 to v3, see [Migrate from xDS v2 to xDS v3](https://docs.cloud.google.com/service-mesh/v1.29/docs/service-routing/xds-control-plane-apis#migrate_from_xds_v2_to_xds_v3).

###  Service routing APIs

  1. Update the YAML file that you created in Determine which clients are currently connected to Cloud Service Mesh. Add a `node-id` field that uses the client ID as its value.
         
         node_matchers:
           - node_id:
               exact: "CLIENT_ID"
             node_metadatas:
               - path:
                   - key: TRAFFICDIRECTOR_GCP_PROJECT_NUMBER
                 value:
                   string_match:
                     exact: "PROJECT_NUMBER"
               - path:
                   - key: TRAFFICDIRECTOR_MESH_SCOPE_NAME
                 value:
                   string_match:
                     exact: "MESH_OR_SCOPE_NAME"
         

Replace the following values:

     * `CLIENT_ID`: the ID of the client whose configuration you're inspecting—for example, `projects/000000/networks/mesh:mesh1/nodes/00000000-0000-0000-0000-00000000~127.0.0.1`
     * `PROJECT_NUMBER`: the unique ID of the Google Cloud project
     * `MESH_OR_SCOPE`: if the xDS client fetches a Mesh resource, use a prefix of `mesh:` followed by the actual mesh name; if the xDS client fetches a Gateway resource, use a prefix of `scope:` followed by the name of the scope parameter
  2. Run the CSDS client. Running the client generates a JSON file. This file contains the configuration that is sent to the Cloud Service Mesh client.
         
         csds-client \
          -service_uri trafficdirector.googleapis.com:443 \
          -platform gcp \
          -authn_mode auto \
          -api_version v3 \
          -request_file PATH_TO_CSDS_REQUEST_YAML_FILE \
          -output_file FILENAME.JSON
         

Replace the following values:

     * `PATH_TO_CSDS_REQUEST_YAML_FILE`: the path to your YAML file
     * `FILENAME.JSON`: a name for the file that holds the output of the CSDS client

You should see output similar to the following:
    
    Client ID                                          xDS stream type    Config status
    8576d4bf-8f10-40b2-920b-bb6a7cf9f34a~10.168.0.3    ADS                LDS  SYNCED
                                                                          RDS  SYNCED
                                                                          CDS  STALE
    Config has been saved to FILENAME.JSON
    

You can inspect a detailed xDS configuration by looking at the JSON file. This output contains the status of individual xDS configurations sent by Cloud Service Mesh to the client by using an aggregated gRPC stream ([ADS](https://www.envoyproxy.io/docs/envoy/latest/api-docs/xds_protocol#aggregated-discovery-service)).




###  Older APIs

  1. Update the YAML file that you created in Determine which clients are currently connected to Cloud Service Mesh. Add a `node-id` field that uses the client ID as its value.
         
         node_matchers:
           - node_id:
               exact: "CLIENT_ID"
             node_metadatas:
               - path:
                   - key: TRAFFICDIRECTOR_GCP_PROJECT_NUMBER
                 value:
                   string_match:
                     exact: "PROJECT_NUMBER"
               - path:
                   - key: TRAFFICDIRECTOR_NETWORK_NAME
                 value:
                   string_match:
                     exact: "NETWORK_NAME"
         

Replace the following values:

     * `CLIENT_ID`: the ID of the client whose configuration you're inspecting—for example, `f38a59c1-4428-42f1-be81-e02eb994f9dd~10.128.0.6`
     * `PROJECT_NUMBER`: the unique ID of the Google Cloud project
     * `NETWORK_NAME`: The VPC network specified by the [forwarding rule](https://docs.cloud.google.com/service-mesh/v1.29/docs/service-routing/forwarding-rules#forwarding_rule_properties) of the routing rule map
  2. Run the CSDS client. Running the client generates a JSON file. This file contains the configuration that is sent to the Cloud Service Mesh client.
         
         csds-client \
          -service_uri trafficdirector.googleapis.com:443 \
          -platform gcp \
          -authn_mode auto \
          -api_version v3 \
          -request_file PATH_TO_CSDS_REQUEST_YAML_FILE \
          -output_file FILENAME.JSON
         

Replace the following values:

     * `PATH_TO_CSDS_REQUEST_YAML_FILE`: the path to your YAML file
     * `FILENAME.JSON`: a name for the file that holds the output of the CSDS client

You should see output similar to the following:
    
    Client ID                                          xDS stream type    Config status
    8576d4bf-8f10-40b2-920b-bb6a7cf9f34a~10.168.0.3    ADS                LDS  SYNCED
                                                                          RDS  SYNCED
                                                                          CDS  STALE
    Config has been saved to FILENAME.JSON
    

You can inspect a detailed xDS configuration by looking at the JSON file. This output contains the status of individual xDS configurations sent by Cloud Service Mesh to the client by using an aggregated gRPC stream ([ADS](https://www.envoyproxy.io/docs/envoy/latest/api-docs/xds_protocol#aggregated-discovery-service)).




### Status values

The following table lists the xDS configuration status values that you might see.

Value | Description  
---|---  
`UNKNOWN` | (Default) ⁣Status information is not available or is unknown.  
`SYNCED` | Cloud Service Mesh sent the configuration to the client and received an `ACK` from the client.  
`ERROR` | ⁣Cloud Service Mesh sent the configuration to the client and received a `NACK` from the client.  
`STALE` | Cloud Service Mesh sent the configuration to the client but did not receive an `ACK` or a `NACK` from the client.  
`NOT_SENT` | The configuration was not sent.  
`N/A` | The CSDS client did not include the node ID. All of the connected streams are returned, but the configuration status is not available.  
  
## Visualization and monitoring

The CSDS client open source tool has additional features that you might want to use, such as visualization and continued monitoring. For more information about these features, see the [README file](https://github.com/envoyproxy/envoy-tools/blob/master/csds-client/README.md) in the open source repository.

## Error message

You might see the following error message from the CSDS client when you enable the Cloud Service Mesh API in only your project:
    
    
    rpc error: code = NotFound desc = Requested entity was not found.
    

This is expected behavior. Cloud Service Mesh configuration is scoped per network. If you haven't created a network yet and you run the CSDS client, you see this error message.

## Limitations

  * Endpoint information is not included in the CSDS response because this information is not available in the CSDS v3 API.
  * The [node ID](https://github.com/envoyproxy/envoy/blob/master/api/envoy/api/v2/core/base.proto#L139) of each client must be unique within the service mesh. If multiple clients share the same node ID, only one configuration is returned—the configuration for the client that most recently connected to Cloud Service Mesh.
  * You might sometimes see a backslash (\\) in the node ID field in the YAML file. If this happens, escape the backslash by using an additional backslash when you query the CSDS API for configuration information. This is a known issue.



## What's next

  * To find general Cloud Service Mesh troubleshooting information, see [Troubleshooting deployments that use Envoy](https://docs.cloud.google.com/service-mesh/v1.29/docs/service-routing/troubleshooting).
  * To resolve configuration issues when you deploy proxyless gRPC services, see [Troubleshooting deployments that use proxyless gRPC](https://docs.cloud.google.com/service-mesh/v1.29/docs/service-routing/troubleshooting-proxyless).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
