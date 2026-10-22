---
url: https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-public/
title: Public network connectivity \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:28:36.207685+00:00
---

# Public network connectivity  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-public/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Public network connectivity

This page describes how Integration Connectors can connect to your publicly accessible backend applications.

The following are the two ways to connect to your public backend application:

  * Connect to your public backend application directly.
  * Connect to your public backend application through a firewall.



## Connect to your public backend application directly

If you can publicly connect to your backend application, you can configure your connection to use the public endpoint by specifying the endpoint in the `Hostname` field. Your connections will have direct access to your backend application.

## Connect to your public backend application through a firewall

In cases where you want to restrict access to your public endpoints with a firewall, you can configure Integration Connectors to use a set of static IP addresses for the traffic originating from the connections. After the configuration, all calls from a connection would originate from a set of static IP address, which you can allowlist in your firewall. To allow a connection to connect through a firewall, you must do the following high-level steps:

  1. Create a firewall, and route your egress traffic through the firewall.
  2. Assign a static IP address to your connection.
  3. Allowlist the assigned static IP address in your firewall.



Steps to create and configure a firewall are outside the scope of this page. This page only describes how you can assign static IP addresses to your connections.

By default, Integration Connectors allocates IP addresses automatically. However, you can configure Integration Connectors to generate static IP addresses instead of an automatic IP addresses. Integration Connectors assigns the static IP addresses at a region level. For example, the static IP addresses for the `us-east1` region will be different from the static IP addresses in the `us-west2` region.

To assign static IP addresses to your connection, do the following steps:

  1. Get the region of the connection for which you want to allocate the static IP address. You can view the connection region in the `Location` column of the Connections page. 

[ Go to the Connections page](https://console.cloud.google.com/connectors/connections)

  2. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

**Tip:** Even though this step mentions to open a Cloud Shell, you can run the commands even on your regular terminal, because you will be calling the Integration Connectors public APIs. 
  3. Configure the Integration Connectors to assign static IP address for the region that you got from step 1. Run the following command in your Cloud Shell. 
         
         curl -X PATCH -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -d '{"networkConfig": {"egressMode": "static_ip"}}' \
         https://connectors.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/regionalSettings?updateMask="networkConfig"

Set the LOCATION to the region that you got in step 1.

Running this command, returns a response similar to the following:
         
         {
         "name": "projects/test-01/locations/us-central1/operations/**operation-1696840994443-6074494b6d138-8215226d-516faaf8** ",
         "metadata": {
           "@type": "type.googleapis.com/google.cloud.connectors.v1.OperationMetadata",
           "createTime": "2023-10-09T08:43:14.467058513Z",
           "target": "projects/test-01/locations/us-central1/regionalSettings",
           "verb": "update",
           "requestedCancellation": false,
           "apiVersion": "v1"
          },
         "done": false
         }

This command returns an operation ID and starts a long-running operation (LRO) which may take some time to complete. Wait for the LRO to complete. You can track the progress of the operation by using the following command:
         
         curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         https://connectors.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID

If the static IP address allocation is successful, you will get a response similar to the following:
         
         ...
         ...
         "response": {
           "@type": "type.googleapis.com/google.cloud.connectors.v1.RegionalSettings",
           "name": "projects/test-01/locations/us-central1/regionalSettings",
           "networkConfig": {
            **"egressMode": "STATIC_IP",
             "egressIps": [
               "35.193.227.203",
               "34.133.63.9",
               "35.223.253.58",
               "34.170.27.253"**
             ]
           }
         }
         

In this sample response, four static IP addresses are allocated for the `us-central1` region, and the `egressMode` for the region is set to `STATIC_IP`.

**Note:** By default, Integration Connectors assigns auto IP addresses for the connections, and not static IP addresses.
  4. Allowlist the static IP addresses (got in step 4) in your firewall rules.



### Get static IP addresses of a region

If at anytime you want to get the static IP addresses allocated to a region (location), run the following command:
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      https://connectors.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/regionalSettings

Running this command returns a response similar to the following:
    
    
      "response": {
        "@type": "type.googleapis.com/google.cloud.connectors.v1.RegionalSettings",
        "name": "projects/test-01/locations/us-central1/regionalSettings",
        "networkConfig": {
         **"egressMode": "STATIC_IP",
          "egressIps": [
            "35.193.227.203",
            "34.133.63.9",
            "35.223.253.58",
            "34.170.27.253"**
          ]
        }
      }

### Assign auto IP addresses to a region

If you want to remove the static IP address configuration for a region, and auto assign the IP addresses, you must run the following command in your terminal:
    
    
    curl -X PATCH -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        -d '{"networkConfig": {"egressMode": "auto_ip"}}' \
        https://connectors.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/regionalSettings?updateMask="networkConfig"

Similar to the previous command for configuring static IP addresses, this command also returns an operation ID and starts a long-running operation (LRO) which may take some time to complete. Wait for the LRO to complete.

### Considerations

Consider the following points when allocating static IP addresses for a region:

  * The reserved set of static IP addresses are different for different regions within a project.
  * When you change the egress mode for a region from `STATIC_IP` to `AUTO_IP`, the original set of static IP addresses aren't retained, and therefore, when you again change the egress mode from `AUTO_IP` to `STATIC_IP`, a new set of static IP addresses are allocated.
  * When you change the egress mode from `AUTO_IP` to `STATIC_IP` or the other way around, you can expect a downtime in the order of seconds.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
