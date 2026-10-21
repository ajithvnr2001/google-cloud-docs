---
url: https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-serverless/
title: Connectivity to services hosted in serverless environment \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:41:33.621307+00:00
---

# Connectivity to services hosted in serverless environment  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-serverless/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Connectivity to services hosted in serverless environment

This page describes how you can configure Integration Connectors to connect to services hosted in serverless environments such as Cloud Run in Google Cloud. 

The following image shows a private network connectivity setup from Integration Connectors to a service hosted in the Cloud Run environment in Google Cloud:

![](https://docs.cloud.google.com/static/integration-connectors/images/serverless.png)

This page assumes that you are familiar with the following concepts: 

  * [Endpoint attachments](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private#endpoint-attachments)
  * [Managed zones](https://docs.cloud.google.com/dns/docs/zones)
  * [Private Service Connect (PSC)](https://docs.cloud.google.com/vpc/docs/private-service-connect)
  * [Google Cloud load balancer](https://docs.cloud.google.com/load-balancing)



### Considerations

When you create a PSC service attachment, consider the following key points:

  * The PSC service attachment and the load balancer are created in different subnets within the same VPC. And specifically, the service attachment is always created in a NAT subnet.
  * Traffic from load balancer and health check probe must be sent to the same port.
  * Configure the firewall rules to facilitate the traffic flow. 

**Ingress rules**

Traffic from the PSC service attachment's subnet must reach your backend service.

**Egress rules**

Egress traffic is enabled by default in a Google Cloud project, unless specific deny rules are configured.

  * All your Google Cloud components such as the PSC service attachment and the load balancer must be in the same region.



### Create a PSC service attachment

In order to establish private connectivity from Integration Connectors, your service must be exposed to Integration Connectors using a PSC service attachment. A service attachment always uses a load balancer. Therefore, if your service isn't behind a load balancer, a load balancer needs to be configured.

The steps described in this section assume that you already have your backend service installed and configured. 

  1. Create a load balancer. If you already have a load balancer, skip this step. 

Create an application load balancer using serverless NEG as the backend by following the instructions at [Set up a regional internal Application Load Balancer with Cloud Run](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal-serverless).

  2. Create the service attachment 
     1. Create a subnet for PSC NAT. The following command creates a subnet with the name `psc-nat-subnet1` and the purpose is `PRIVATE_SERVICE_CONNECT`. 
            
            gcloud compute networks subnets create psc-nat-subnet1 \
                      --network=VPC_NETWORK --range=SUBNET_RANGE_1 \
                      --purpose=PRIVATE_SERVICE_CONNECT

     2. Create a firewall rule to allow traffic from the PSC NAT to the load balancer. 
            
            gcloud compute network-firewall-policies rules create PRIORITY --firewall-policy FIREWALL_POLICY_NAME_SA \
                --direction=INGRESS  --network=VPC_NETWORK \
                --action=allow --allow=tcp:BACKEND_SERVER_PORT --src-ip-ranges=SUBNET_RANGE_1

     3. Create service attachment with [explicit approval](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#publish-service-explicit). 
            
            gcloud compute service-attachments create SERVICE_ATTACHMENT_NAME --producer-forwarding-rule=FORWARDING_RULE_NAME  --connection-preference=ACCEPT_MANUAL --consumer-accept-list=SERVICE_DIRECTORY_PROJECT_ID=LIMIT --nat-subnets=psc-nat-subnet1

In this command, LIMIT is the connection limit for the project. The connection limit is the number of consumer PSC endpoints that can connect to this service. To get the SERVICE_DIRECTORY_PROJECT_ID, do the following step:

        * You can create the PSC service attachment such that it accepts requests only from the specified Google Cloud projects. However, to do this, you need the project ID of the service directory associated with your Google Cloud project. To get the project ID of the service directory, you can use the [List Connections API](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections/list) as shown in the following example.

**Note:** Before getting the project ID, ensure that at least one connection is present in your project.

### Syntax
              
              curl -X GET \
                  -H "authorization: Bearer $(gcloud auth print-access-token)" \
                  -H "Content-Type: application/json" \
                  "https://connectors.googleapis.com/v1/projects/CONNECTORS_PROJECT_ID/locations/-/connections"

Replace the following: 

          * CONNECTORS_PROJECT_ID: The ID of your Google Cloud project where you created your connection.

### Example

This example gets the project ID of the service directory for the `connectors-test` Google Cloud project.
    
    curl -X GET \
        -H "authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://connectors.googleapis.com/v1/projects/connectors-test/locations/-/connections"

Running this command on the terminal displays an output similar to the following:
    
    .....
    {
      "connections": [
        {
          "name": "projects/connectors-test/locations/asia-northeast1/connections/big-query-iam-invalid-sa",
          "createTime": "2022-10-07T09:02:31.905048520Z",
          "updateTime": "2022-10-07T09:22:39.993778690Z",
          "connectorVersion": "projects/connectors-test/locations/global/providers/gcp/connectors/bigquery/versions/1",
          "status": {
            "state": "ACTIVE"
          },
          "configVariables": [
            {
              "key": "project_id",
              "stringValue": "**connectors-test** "
            },
            {
              "key": "dataset_id",
              "stringValue": "testDataset"
            }
          ],
          "authConfig": {},
          "serviceAccount": "564332356444-compute@developer.gserviceaccount.com",
          "serviceDirectory": "projects/**abcdefghijk-tp** /locations/asia-northeast1/namespaces/connectors/services/runtime",
          "nodeConfig": {
            "minNodeCount": 2,
            "maxNodeCount": 50
          }
        },
    ....
    

In the sample output, for the `connectors-test` Google Cloud project, the project ID of the service directory is `abcdefghijk-tp`.




### Create an endpoint attachment to consume the PSC service attachment

**Endpoint attachment as an IP address**

For instructions on how to create an endpoint attachment as an IP address, see [Create an endpoint attachment as an IP address](https://docs.cloud.google.com/integration-connectors/docs/create-endpoint-attachment#create-ep-ipaddr).

**Endpoint attachment as a hostname**

In certain cases such as TLS enabled backends, the destination requires you to use hostnames instead of private IPs to perform TLS validation. In those cases where a private DNS is used instead of an IP address for the host destination, in addition to creating an endpoint attachment as an IP address, you must also configure managed zones. For instructions on how to create an endpoint attachment as a hostname, see [Create an endpoint attachment as a hostname](https://docs.cloud.google.com/integration-connectors/docs/create-endpoint-attachment#create-ep-hostname). 

Later, when you configure your connection to use the endpoint attachment, you can select this endpoint attachment.

### Configure a connection to use the endpoint attachment

Now that you have created an endpoint attachment, use the endpoint attachment in your connection. When you create a new connection or update an existing connection, in the Destinations section, select **Endpoint attachment** as the **Destination Type** and select the endpoint attachment that you created from the **Endpoint Attachment** list.

If you created a managed zone, select **Host Address** as the **Destination Type** and use the A-record that you created while creating the managed zone.

## Troubleshooting tips

Follow the guidelines listed in this section to avoid common issues:

  * To verify that the endpoint attachment is set up correctly and the PSC connection is established, check the connection status. For more information, see [Verify the endpoint attachment connection](https://docs.cloud.google.com/integration-connectors/docs/create-endpoint-attachment#verify-ep-connection).
  * For information about troubleshooting Load Balancer issues, see [Troubleshoot issues with internal Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/l7-internal/troubleshooting-l7-ilb).
  * [Google Cloud Connectivity test](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview) can be used to identify any gaps in your network configuration. For more information, see [Create and run Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
