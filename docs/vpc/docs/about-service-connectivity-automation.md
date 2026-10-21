---
url: https://docs.cloud.google.com/vpc/docs/about-service-connectivity-automation/
title: About service connectivity automation \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:18.605939+00:00
---

# About service connectivity automation  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/about-service-connectivity-automation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# About service connectivity automation

Service connectivity automation lets service consumers automate the deployment of connectivity to managed services.

Consider a database administrator who deploys a database instance and wants to let service consumers to reach that database through a Private Service Connect endpoint. The database administrator might not have the required Identity and Access Management (IAM) credentials or expertise to deploy networking resources.

If a managed service supports service connectivity automation, the service instance configuration and the networking configuration can be delegated to the appropriate administrators:

  * _Service instance administrators_ can control which networks can access their services.

  * _Network administrators_ can control which services they want to allow connections to.




When these configurations match, service connectivity automation creates an endpoint in the appropriate networks, providing connectivity to the managed service instance.

## Overview of service connectivity automation

The following section describes a basic configuration in a single VPC network that uses service connectivity automation. For information about other configurations, see Shared VPC and Google services with custom service instance scope.

Deploying an instance of a managed service that supports service connectivity automation involves the following steps:

  1. A network administrator [creates a service connection policy](https://docs.cloud.google.com/vpc/docs/configure-service-connection-policies#create-policy) for their VPC network.

The service connection policy references a service class—a globally unique resource that identifies a specific producer service. A single service connection policy is scoped to a single service class and a single consumer VPC network, delegating the ability to configure connectivity within that scope.

  2. A service instance administrator [deploys a managed service instance](https://docs.cloud.google.com/vpc/docs/deploy-service-instance-service-connection-policies#deploy-service) by using the service's administrative API or UI. The service instance configuration specifies which networks can access the service through service connectivity automation.

  3. Service connectivity automation creates an endpoint in the consumer VPC network. This endpoint can be used to send requests to the service instance.


[ ![](https://docs.cloud.google.com/static/vpc/images/service-connectivity-automation-overview.svg)](https://docs.cloud.google.com/static/vpc/images/service-connectivity-automation-overview.svg) Service connectivity automation lets service consumers automate the deployment of connectivity to managed services (click to enlarge).

## Producer configuration

The following sections describe resources that are used by service producers to configure service connectivity automation.

### Service classes

A service class is a globally unique representation of a managed service type. Each producer exclusively owns their service class. Consumers reference the service class in their service connection policies, which authorizes deployment and delegates connectivity to the producer.

Service connection policies can only be created for services that have a service class.

Service classes are available only for Google published services. For more information, see Supported services.

### Service connection maps

A service connection map is a producer-managed resource that stores details for authorizing and establishing Private Service Connect connections between consumer VPC networks and producer managed service instances. This map defines the allowed relationships between producer service instances (represented by service attachments) and the consumer projects and VPC networks that are authorized to connect to the service instances.

## Authorization model

Service connection policies let consumers delegate the deployment of connectivity to managed services. The service producer doesn't have direct access or IAM privileges for the consumer project. Instead, the producer configures a service connection map in their own project.

When the service connection map is created or updated, typically in response to a request from a consumer service administrator to the managed service's administrative API or UI, service connectivity automation performs a series of authorization checks. If all of the checks pass, Private Service Connect endpoints are created as specified in the request.

  * Network configuration (service connection policy):

    * **Network authorization**. The consumer VPC network must have a valid service connection policy that authorizes the VPC network, region, and service class that is specified by the request. This check helps to ensure that a consumer network administrator with IAM permissions on the VPC network explicitly delegates the ability to create Private Service Connect endpoints for the specified service type.
    * **Service instance scope**. If the managed service instance is a Google service and the service connection policy specifies a custom service instance scope (`custom-resource-hierarchy-levels`), then service connectivity automation checks the list of [Resource Manager nodes](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) that are provided (`--allowed-google-producers-resource-hierarchy-level`). The project that the service instance administrator specified in the managed service's UI or API for deploying and managing the service instance must be within the allowed scope defined by this list. The scope can be a mix of organizations, folders, and projects.
    * **Endpoint project validation**. The project where the connection policy is created must be associated with the VPC network where the endpoint is to be created. The project must either contain the VPC network or be a service project that is attached to the Shared VPC network.
  * Service instance configuration:

    * **Service administrator IAM authorization**. The consumer service administrator must have the IAM permissions that are necessary to create or update the producer service instance. These permissions vary based on the service that is being deployed.

    * **Service instance administrator authorization**. In the service's administrative API, the service instance administrator who created the service instance must have configured the instance to allow connections from the VPC network that requests the connection.

  * Producer configuration:

    * **Producer IAM permissions**. The producer service administrator who creates or updates the service connection map must have IAM permissions on the associated service class. This check helps prevent false representations of a public service class.



If each condition is met, the [Network Connectivity Service Account](https://docs.cloud.google.com/iam/docs/service-agents#network-connectivity-service-account) creates the requested endpoints in the authorized networks. The Network Connectivity Service Account is a [service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents).

## Automatic retries for endpoint failures

Service connectivity automation fully manages the creation and deletion of your Private Service Connect endpoints.

If service connectivity automation fails to create or delete an authorized endpoint—for example, due to quota limitations or the service connection policy's subnet being out of IP addresses—an automated process periodically retries the operation until the blocking issue is resolved. However, if endpoint creation or deletion fails due to [authorization checks](https://docs.cloud.google.com/vpc/docs/about-service-connectivity-automation#authorization), the operation is not retried.

You can view errors that block endpoint creation by [describing the service connection policy](https://docs.cloud.google.com/vpc/docs/configure-service-connection-policies#describe-policy) and checking the `pscConnections` field. For information about troubleshooting failures with endpoint creation or deletion, see [Troubleshooting](https://docs.cloud.google.com/vpc/docs/deploy-service-instance-service-connection-policies#troubleshooting).

## Shared VPC

Service connectivity automation can be used to automatically create Private Service Connect endpoints in Shared VPC networks. Because the endpoint is configured with an IP address from the Shared VPC network, the endpoint is accessible from the host project and all attached service projects.

To create the configuration shown in the following diagram, the following tasks are completed:

  1. The network administrator creates a service connection policy for the `vpc1` network in the `project1` host project, and allows connectivity to service instances that use the `google-cloud-sql` service class. Endpoint IP addresses are allocated from the `endpoint-subnet` subnet.

  2. The service instance administrator deploys two managed service instances: `db-test` in the `service-project-test` project, and `db-prod` in the `service-project-prod` project. The administrator configures the service instance to let service connectivity automation deploy endpoints in network `vpc1` in `project1` that connect to the service instances.

  3. Because the authorization checks all pass, service connectivity automation creates two endpoints that are connected to `endpoint-subnet`, one for each service instance. All VMs that are connected to the `vm-subnet` subnet can access the endpoints because they are connected to the same Shared VPC network as the endpoints.


**Note:** In this example, the service instance configuration specifies that the endpoints are created in the host project. Specifying a service project is also supported.[ ![](https://docs.cloud.google.com/static/vpc/images/service-connectivity-automation-shared-vpc.svg)](https://docs.cloud.google.com/static/vpc/images/service-connectivity-automation-shared-vpc.svg) You can use a service connection policy in a Shared VPC network to create connectivity to service instances that are deployed in service projects (click to enlarge).

## Services with custom service instance scope support

By default, service connectivity automation requires that the service instance and the endpoints that connect to the service instance must be in the same project (or in the case of Shared VPC, in connected projects). If a service supports custom service instance scope, service instances and connecting endpoints can be in different projects or organizations.

To create the configuration shown in the following diagram, the following tasks are completed:

  1. The network administrators for `vpc-1`, `vpc-2`, and `vpc-3` create service connection policies in their respective VPC networks. They allow connectivity to service instances that use the `google-cloud-sql` service class and are deployed in project `project-1` in organization `org-1`.

  2. The service instance administrator deploys a managed service instance `db-1` in `project-1` by using the service's administrative API or UI. The administrator configures the service instance to let service connectivity automation deploy endpoints in `vpc-1` and `vpc-2` that connect to `db-1`.

  3. For `vpc-1` and `vpc-2`, the authorization checks all pass and service connectivity automation creates an endpoint in each network. VMs in those networks can send traffic to the service instance through the endpoints.

However, an endpoint isn't created in `vpc-3` because that network isn't configured for automatic connectivity in the `db-1` service instance configuration.

If `vpc-3` needs to access the `db-1` service instance, the network administrator can contact the database administrator and ask them to add `vpc-3` to the connectivity configuration for `db-1`.


[ ![](https://docs.cloud.google.com/static/vpc/images/service-connectivity-automation-custom-scope.svg)](https://docs.cloud.google.com/static/vpc/images/service-connectivity-automation-custom-scope.svg) You can automate connectivity to supported Google services from different projects, folders, or organizations (click to enlarge).

## Supported services

The following Google services support service connectivity automation.

Google service | Access provided  
---|---  
[AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/overview) | Lets you [ automate creating connections to AlloyDB for PostgreSQL instances](https://docs.cloud.google.com/alloydb/docs/configure-private-service-connect).  
[Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/introduction) | Lets you [ automate creating connections to Cloud SQL instances](https://docs.cloud.google.com/sql/docs/mysql/configure-private-service-connect#create-endpoint-automatically).  
[Memorystore for Redis Cluster](https://docs.cloud.google.com/memorystore/docs/cluster/overview) | Lets you [automate creating connections to Memorystore for Redis Cluster instances](https://docs.cloud.google.com/memorystore/docs/cluster/networking).  
[Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview) | Lets you [automate creating connections to Memorystore for Valkey instances](https://docs.cloud.google.com/memorystore/docs/valkey/networking).  
[Vertex AI Vector Search](https://docs.cloud.google.com/vertex-ai/docs/matching-engine/overview) | Lets you [automate creating connections to Vector Search endpoints](https://docs.cloud.google.com/vertex-ai/docs/vector-search/setup/private-service-connect).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
