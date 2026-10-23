---
url: https://docs.cloud.google.com/vpc/docs/deploy-service-instance-service-connection-policies/
title: Deploy a managed service instance by using service connection policies \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:30.580273+00:00
---

# Deploy a managed service instance by using service connection policies  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/deploy-service-instance-service-connection-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Deploy a managed service instance by using service connection policies 

This page describes how a service instance administrator can deploy an instance of a managed service and configure connectivity by using service connection policies.

## Before you begin

  * Make sure that the managed service that you want to deploy supports service connection policies. For more information, see [Supported services](https://docs.cloud.google.com/vpc/docs/about-service-connectivity-automation#supported-services).

  * You need a [service connection policy](https://docs.cloud.google.com/vpc/docs/about-service-connection-policies) for the VPC network, region, and managed service that you want to deploy.




### Required roles

Service instance administrators don't need any IAM permissions for the VPC network because these permissions are delegated by the service connection policy. However, IAM permissions might be required for specific managed services that are deployed by using service connection policies. For information about IAM permissions that are required by a specific managed service, check the service's documentation.

## Deploy a managed service instance and configure connectivity

If a service connection policy exists for a service, a consumer service administrator can configure connectivity for the managed service instance that they are deploying directly through the administrative API or UI of the managed service.

To deploy managed service connectivity, follow these steps. The steps might vary depending on the managed service.

  1. Use the administrative API or UI of the managed service to deploy a service instance, specifying Private Service Connect as your connectivity type. The service might provide the option to specify the VPC network to deploy Private Service Connect endpoints in.

For example, you can [deploy and configure connectivity for a Cloud SQL instance](https://docs.cloud.google.com/sql/docs/mysql/configure-private-service-connect#create-cloud-sql-instance-psc-enabled-2).

**Note:** A service connection policy must exist for this VPC network, region, and service class. Otherwise, the service producer that's represented by the service class is not authorized to deploy connectivity on your behalf.
  2. If all [authorization checks](https://docs.cloud.google.com/vpc/docs/about-service-connectivity-automation#authorization) pass, then connectivity is deployed. The Network Connectivity Service Account creates an internal IP address and Private Service Connect endpoint in the specified VPC network.

The lifecycle of your endpoint matches the lifecycle of your managed service instance. The endpoint remains active and stable unless you reconfigure connectivity or decommission the service instance

  3. After the Network Connectivity Service Account creates your endpoint, the endpoint's forwarding rule is visible in the project that you configured in step 1. This forwarding rule indicates that the connection has been accepted by the producer and includes the IP address that was assigned to your endpoint.

The names of all forwarding rules that are created by using service connection policies start with `sca-auto-`. The following is an example of a forwarding rule that was created by using a service connection policy.
         
         
         kind: compute#forwardingRule
         name: sca-auto-ab3f45d
         IPAddress: 10.33.2.8
         allowPscGlobalAccess: true
         network: https://www.googleapis.com/compute/v1/projects/consumer-project/global/networks/vpc1
         pscConnectionStatus: ACCEPTED
         region: https://www.googleapis.com/compute/v1/projects/consumer-project/regions/us-central1
         selfLink: https://www.googleapis.com/compute/v1/projects/consumer-project/regions/us-central1/forwardingRules/sca-auto-ab3f45d
         serviceDirectoryRegistrations:
         -namespace: goog-psc-default
         target:
         https://www.googleapis.com/compute/v1/projects/producer-project/regions/us-central1/serviceAttachments/producer-sa
         
         

  4. Your service might provide information about how to connect to the new endpoint—for example, by providing an IP address. Use the provided IP address to communicate with your service through internal IP addresses within Google Cloud.

For more information about how to configure a specific service, see that service's documentation.


**Caution:** The managed service fully controls the lifecycle of Private Service Connect endpoints and IP addresses that are deployed by using service connection policies. Don't directly delete or update these Google Cloud resources or else you risk losing connectivity to your managed service instance. All actions to add, remove, or update connectivity for a managed service instance should be taken directly through the administrative API or UI of the managed service.

## Decommission service connectivity

To decommission service connectivity or decommission a managed service instance that's deployed by using service connection policies, use the administrative API or UI of the managed service. Delete each service instance that's associated with the managed service. When service instances are deleted, service connectivity automation deletes the associated connections and endpoints.

## Troubleshooting

This section contains information about troubleshooting connections that are created through service connectivity automation.

### Endpoint creation or deletion failure

If authorized endpoints are not created or deleted as you expect, [describe the service connection policy](https://docs.cloud.google.com/vpc/docs/configure-service-connection-policies#describe-policy). The `pscConnections` field contains details about any blocking errors and how you can resolve them.

After any issues are resolved, the endpoint is created or deleted the next time service connectivity automation automatically [retries the operation](https://docs.cloud.google.com/vpc/docs/about-service-connectivity-automation#endpoint-automation).

Alternatively, if you don't want to wait for the retry process, you can use the administrative API or UI of the managed service you are deploying to request deployment and connectivity for another service instance, using a valid configuration.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
