---
url: https://docs.cloud.google.com/workflows/docs/invoke-private-endpoint-vpc/
title: Invoke a private endpoint using Service Directory's service registry \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:30:11.198079+00:00
---

# Invoke a private endpoint using Service Directory's service registry  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/invoke-private-endpoint-vpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback 

#  Invoke a private endpoint using Service Directory's service registry Stay organized with collections  Save and categorize content based on your preferences. 

You can target a private endpoint for HTTP calls from your workflow execution by using Service Directory's service registry with Workflows. This lets you provide your workflow with a Service Directory service name. Your workflow execution uses the information retrieved from the service registry to send the appropriate HTTP request, without egressing to a public network.

This document shows you how to register a virtual machine (VM) in a Virtual Private Cloud (VPC) network as a Service Directory endpoint:

  * [A VPC network](https://docs.cloud.google.com/vpc/docs/overview) provides connectivity for your VM instances, and lets you create private endpoints within your VPC network by using internal IP addresses. HTTP calls to a VPC network resource are sent over a private network while enforcing Identity and Access Management (IAM) and VPC Service Controls.

  * [Service Directory](https://docs.cloud.google.com/service-directory/docs/overview) is a _service registry_ that stores information about registered network services, including their names, locations, and attributes. Regardless of their infrastructure, you can register services automatically, and capture their details. This lets you discover, publish, and connect services at scale for all your service endpoints.


**Note:** By creating a private endpoint within a VPC network, the endpoint can also be VPC Service Controls-compliant. After following the steps in this guide, you can [set up a service perimeter](https://docs.cloud.google.com/workflows/docs/use-vpc-service-controls) and use VPC Service Controls with Workflows to mitigate data exfiltration risks.

This diagram provides an overview:

![Sending an HTTP request to a port number on a VM instance using information from Service Directory](https://docs.cloud.google.com/static/workflows/images/private-endpoint.svg)

At a high level, you must do the following:

  1. Grant permissions to the Cloud Workflows service agent so that the service agent can view Service Directory resources and access VPC networks using Service Directory.
  2. Create a VPC network to provide networking functionality.
  3. Create a VPC firewall rule so that you can allow or deny traffic to or from VM instances in your VPC network.
  4. Create a VM instance in the VPC network. A Compute Engine VM instance is a virtual machine that is hosted on Google's infrastructure. The terms _Compute Engine instance_ , _VM instance_ , and _VM_ are synonymous and are used interchangeably.
  5. Deploy an application on the VM. You can run an app on your VM instance and confirm that traffic is being served as expected.
  6. Configure Service Directory so that your workflow execution can invoke a Service Directory endpoint.

**Note:** Make sure to configure only one endpoint per Service Directory service. If more than one endpoint is configured, Workflows arbitrarily chooses an endpoint.
  7. Create and deploy your workflow. The `private_service_name` value in your workflow specifies the Service Directory endpoint that you registered in the previous step.




## Grant permissions to the Cloud Workflows service agent

Some Google Cloud services have [_service agents_](https://docs.cloud.google.com/iam/docs/service-agents) that allow the services to access your resources. If an API requires a service agent, then Google creates the service agent after you activate and use the API.

  1. When you first [deploy a workflow](https://docs.cloud.google.com/sdk/gcloud/reference/workflows/deploy), the Cloud Workflows service agent is automatically created with the following format:

`service-PROJECT_NUMBER@gcp-sa-workflows.iam.gserviceaccount.com`

You can manually create the service account in a project without any workflows with this command:
         
         gcloud beta services identity create \
             --service=workflows.googleapis.com \
             --project=PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project ID.

  2. To view Service Directory resources, grant the [Service Directory Viewer role](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.viewer) (`servicedirectory.viewer`) on the project to the Workflows service agent:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-workflows.iam.gserviceaccount.com \
             --role=roles/servicedirectory.viewer

Replace `PROJECT_NUMBER` with your Google Cloud project number. You can find your project number on the [Welcome](https://console.cloud.google.com/welcome) page of the Google Cloud console or by running the following command:
         
         gcloud projects describe PROJECT_ID --format='value(projectNumber)'

  3. To access VPC networks using Service Directory, grant the [Private Service Connect Authorized Service role](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.pscAuthorizedService) (`roles/servicedirectory.pscAuthorizedService`) on the project to the Workflows service agent:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-workflows.iam.gserviceaccount.com \
             --role=roles/servicedirectory.pscAuthorizedService




## Create a VPC network

A VPC network is a virtual version of a physical network that is implemented inside of Google's production network. It provides connectivity for your Compute Engine VM instances.

You can create an [auto mode or custom mode](https://docs.cloud.google.com/vpc/docs/vpc#subnet-ranges) VPC network. Each new network that you create must have a unique name within the same project.

For example, the following command creates an auto mode VPC network:
    
    
    gcloud compute networks create NETWORK_NAME \
        --subnet-mode=auto

Replace `NETWORK_NAME` with a name for the VPC network.

For more information, see [Create and manage VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks).

## Create a VPC firewall rule

VPC firewall rules let you allow or deny traffic to or from VM instances in a VPC network based on port number, tag, or protocol.

VPC firewall rules are defined at the network level, and only apply to the network where they are created; however, the name you choose for a rule must be unique to the project.

For example, the following command creates a firewall rule for the VPC network you previously created.
    
    
    gcloud compute firewall-rules create RULE_NAME \
        --network=projects/PROJECT_ID/global/networks/NETWORK_NAME \
        --direction=INGRESS \
        --action=ALLOW \
        --source-ranges=IP_ADDRESS_RANGE \
        --rules=all

Replace the following:

  * `RULE_NAME`: a name for the firewall rule.

  * `IP_ADDRESS_RANGE`: one or more IPv4 or IPv6 address ranges. As a best practice, specify the specific IP address ranges needed to allow access. Note the following:

    * Private network access for Service Directory uses `35.199.192.0/19` as an internal-only range with next hops that are entirely within Google's network. For more information, see [Paths for Cloud DNS and Service Directory](https://docs.cloud.google.com/vpc/docs/routes#cloud-dns).

    * Including `35.235.240.0/20` in the source ranges allows SSH connections using Identity-Aware Proxy (IAP) TCP forwarding if all other prerequisites are met. For more information, see [Using IAP for TCP forwarding](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding).

    * If you are using the SSH-in-browser tool to connect to your Compute Engine VM from within the Google Cloud console, there are [specific requirements](https://docs.cloud.google.com/compute/docs/ssh-in-browser#supported_environments).

  * The `--rules` flag value of `all` makes the firewall rule applicable to all protocols and all destination ports. You can narrow the scope by specifying [protocols and ports](https://docs.cloud.google.com/firewall/docs/firewalls#protocols_and_ports).

  * Optionally, you can use the `--target-tags` and `--target-service-accounts` flags to define [targets](https://docs.cloud.google.com/firewall/docs/firewalls#rule_assignment); otherwise, the rule applies to all targets in the network.




For more information, see [Use VPC firewall rules](https://docs.cloud.google.com/firewall/docs/using-firewalls).

## Create a VM instance in the VPC network

VM instances include Google Kubernetes Engine (GKE) clusters, App Engine flexible environment instances, and other Google Cloud products built on Compute Engine VMs. To support private network access, a VPC network resource can be a VM instance or other supported destination. For more information, see [Private network access overview](https://docs.cloud.google.com/service-directory/docs/private-network-access-overview).

Compute Engine instances can run public images for Linux and Windows Server that Google provides, as well as private custom images that you can create or import from your existing systems. You can also deploy Docker containers.

You can choose the machine properties of your instances, such as the number of virtual CPUs and the amount of memory, by using a set of predefined machine types or by creating your own custom machine types.

For example, the following command creates a Linux VM instance from a public image with a network interface attached to the VPC network you created previously.

  1. Create and start a VM instance:
         
         gcloud compute instances create VM_NAME \
             --image-family=debian-11 \
             --image-project=debian-cloud \
             --machine-type=e2-micro \
             --network-interface network=projects/PROJECT_ID/global/networks/NETWORK_NAME

Replace `VM_NAME` with a name for the VM.

  2. If you are prompted to confirm the zone for the instance, type `y`.

After you create the VM instance, note the `INTERNAL_IP` address that is returned.

  3. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  4. In the **Name** column, click the name of the appropriate VM instance.

  5. If the VM is running, to stop the VM, click stop **Stop**.

  6. To edit the VM, click edit **Edit**.

  7. In the **Networking** > **Firewalls** section, to permit HTTP or HTTPS traffic to the VM, select **Allow HTTP traffic** or **Allow HTTPS traffic**.

For this example, select the **Allow HTTP traffic** checkbox.

Compute Engine adds a network tag to your VM which associates the firewall rule with the VM. It then creates the corresponding ingress firewall rule that allows all incoming traffic on `tcp:80` (HTTP) or `tcp:443` (HTTPS).

  8. To save your changes, click **Save**.

  9. To restart the VM, click **Start/Resume**.




For more information, see [Create and start a VM instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).

## Deploy an application on the VM

To test the network configuration and to confirm that traffic is being served as expected, you can deploy a basic app on your VM that listens on a port.

For example, the following commands create a Node.js web service that listens on port 3000.

  1. Establish an [SSH connection](https://docs.cloud.google.com/compute/docs/instances/ssh) to your VM instance.

  2. Update your package repositories:
         
         sudo apt update

  3. Install [NVM](https://github.com/creationix/nvm), [Node.js](https://nodejs.org/en/download/package-manager/), and [npm](https://www.npmjs.com/).

For more information, see [Setting up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup).

  4. Interactively create a `package.json` file:
         
         npm init

For example:
         
         {
         "name": "test",
         "version": "1.0.0",
         "description": "",
         "main": "index.js",
         "scripts": {
         "test": "hello"
         },
         "author": "",
         "license": "ISC"
         }

  5. Install [Express](https://expressjs.com/), a web application framework for Node.js:
         
         npm install express

  6. Write the code for the test app:
         
         vim app.js

The following sample creates an app that responds to `GET` requests to the root path (`/`) with the text "Hello, world!"
         
         const express = require('express');
         const app = express();
         
         app.get('/', (req, res) => {
           res.status(200).send('Hello, world!').end();
         });
         
         app.listen(3000, () => {
           console.log('Sample app listening on port 3000.');
         });

Note the port that the app is listening on. The same port number must be used when configuring the endpoint for the Service Directory service.

  7. Confirm that the app is listening on port 3000:
         
         node app.js




Compute Engine offers a range of deployment options. For more information, see [Choose a Compute Engine deployment strategy for your workload](https://docs.cloud.google.com/compute/docs/choose-compute-deployment-option).

## Configure Service Directory

To support invoking a private endpoint from a workflow execution, you must set up a Service Directory namespace, register a service in the namespace, and add an endpoint to the service.

For example, the following commands create a namespace, a service, and an endpoint that specifies the VPC network and internal IP address of your VM instance.

  1. Create a namespace:
         
         gcloud service-directory namespaces create NAMESPACE \
             --location=REGION

Replace the following:

     * `NAMESPACE`: the ID of the namespace or fully qualified identifier for the namespace.
     * `REGION`: the Google Cloud region that contains the namespace; for example, `us-central1`.
  2. Create a service:
         
         gcloud service-directory services create SERVICE \
             --namespace=NAMESPACE \
             --location=REGION

Replace `SERVICE` with the name of the service that you are creating.

  3. Configure an endpoint.

**Note:** Make sure to configure only one endpoint per Service Directory service. If more than one endpoint is configured, Workflows arbitrarily chooses an endpoint.
         
         gcloud service-directory endpoints create ENDPOINT \
             --namespace=NAMESPACE \
             --service=SERVICE \
             --network=projects/PROJECT_NUMBER/locations/global/networks/NETWORK_NAME \
             --port=PORT_NUMBER \
             --address=IP_ADDRESS \
             --location=REGION

Replace the following:

     * `ENDPOINT`: the name of the endpoint that you are creating.
     * `PORT_NUMBER`: the port that the endpoint is running on; for example, `3000`.
     * `IP_ADDRESS`: the IPv6 or IPv4 address of the endpoint; this is the internal IP address that you noted previously.



For more information, see [Configure Service Directory](https://docs.cloud.google.com/service-directory/docs/configuring-service-directory) and [Configure private network access](https://docs.cloud.google.com/service-directory/docs/configuring-private-network-access).

## Create and deploy your workflow

Calling or invoking a private endpoint from Workflows is done through an HTTP request. The most common HTTP request methods have a call shortcut (such as [http.get](https://docs.cloud.google.com/workflows/docs/reference/stdlib/http/get) and [http.post](https://docs.cloud.google.com/workflows/docs/reference/stdlib/http/post)), but you can make any type of HTTP request by setting the `call` field to `http.request` and specifying the type of request using the `method` field. For more information, see [Make an HTTP request](https://docs.cloud.google.com/workflows/docs/http-requests).

  1. Create a source code file for your workflow:
         
         touch call-private-endpoint.JSON_OR_YAML

Replace `JSON_OR_YAML` with `yaml` or `json` depending on the format of your workflow.

  2. In a text editor, copy the following workflow (which in this case uses an HTTP protocol for the `url` value) to your source code file:

### YAML
         
         main:
           steps:
             - checkHttp:
                 call: http.get
                 args:
                   url: http://IP_ADDRESS
                   private_service_name: "projects/PROJECT_ID/locations/REGION/namespaces/NAMESPACE/services/SERVICE"
                 result: res
             - ret:
                 return: ${res}

### JSON
         
         {
           "main": {
             "steps": [
               {
                 "checkHttp": {
                   "call": "http.get",
                   "args": {
                     "url": "http://IP_ADDRESS",
                     "private_service_name": "projects/PROJECT_ID/locations/REGION/namespaces/NAMESPACE/services/SERVICE"
                   },
                   "result": "res"
                 }
               },
               {
                 "ret": {
                   "return": "${res}"
                 }
               }
             ]
           }
         }

The `private_service_name` value must be a string that specifies a registered Service Directory service name with the following format:

`projects/PROJECT_ID/locations/LOCATION/namespaces/NAMESPACE_NAME/services/SERVICE_NAME`

  3. Deploy the workflow. For test purposes, you can attach the [Compute Engine default service account](https://docs.cloud.google.com/iam/docs/service-account-types#default) to the workflow to represent its identity:
         
         gcloud workflows deploy call-private-endpoint \
             --source=call-private-endpoint.JSON_OR_YAML \
             --location=REGION \
             --service-account=PROJECT_NUMBER-compute@developer.gserviceaccount.com

**Caution:** We recommend that you use the Compute Engine default service account for test purposes only. For production environments, we strongly recommend [creating a new service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) and granting it one or more IAM roles that contain the minimum permissions required and follow the principle of [least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege).
  4. Execute the workflow:
         
         gcloud workflows run call-private-endpoint \
             --location=REGION

You should see a result similar to the following:
         
         argument: 'null'
         duration: 0.650784403s
         endTime: '2023-06-09T18:19:52.570690079Z'
         name: projects/968807934019/locations/us-central1/workflows/call-private-endpoint/executions/4aac88d3-0b54-419b-b364-b6eb973cc932
         result: '{"body":"Hello, world!","code":200,"headers":{"Connection":"keep-alive","Content-Length":"21","Content-Type":"text/html;
         charset=utf-8","Date":"Fri, 09 Jun 2023 18:19:52 GMT","Etag":"W/\"15-NFaeBgdti+9S7zm5kAdSuGJQm6Q\"","Keep-Alive":"timeout=5","X-Powered-By":"Express"}}'
         startTime: '2023-06-09T18:19:51.919905676Z'
         state: SUCCEEDED




## What's next

  * [Learn more about Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect).
  * [Configure Service Directory for GKE](https://docs.cloud.google.com/service-directory/docs/configuring-sd-for-gke).
  * [Set up a service perimeter using VPC Service Controls](https://docs.cloud.google.com/workflows/docs/use-vpc-service-controls).
  * [Invoke an IAP-secured endpoint](https://docs.cloud.google.com/workflows/docs/invoke-iap-secured-endpoints).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
