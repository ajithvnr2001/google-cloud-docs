---
url: https://docs.cloud.google.com/apigee/docs/api-platform/service-extensions/extension-processor-agent-gateway/
title: Connect the Apigee extension processor to an Agent Gateway \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:35:44.705667+00:00
---

# Connect the Apigee extension processor to an Agent Gateway  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/service-extensions/extension-processor-agent-gateway/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Connect the Apigee extension processor to an Agent Gateway Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This page describes how to connect the Apigee extension processor to an [Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview), so that Apigee policies are applied to the calls an AI agent makes to its model, its tools, and the Model Context Protocol (MCP) servers it uses—without changing the agent.

An Agent Gateway is the network entry and exit point for an agent's traffic. It isn't a load balancer, so it doesn't use a traffic extension. Instead, the gateway [delegates authorization](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/delegate-authorization) to an **authorization extension** , and you configure the extension processor as that extension. Once connected, the gateway sends each agent request and response to Apigee for processing, and Apigee returns a verdict.

The following figure shows the resources you create on this page, and the path a single agent request takes through them:

![An agent request is held at the Agent Gateway, sent to Apigee over Private Service Connect for a verdict, then forwarded on.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/ext-proc-agent-gateway.svg)**Figure 1.** Components and request flow when the Apigee extension processor is the authorization extension for an Agent Gateway.

In figure 1, a request is handled as follows: 

  1. The agent makes an ordinary HTTPS request to its model, a tool, or an MCP server. The agent is bound to the gateway when it is created, and needs no changes.
  2. The gateway holds the request and calls the authorization extension for a verdict.
  3. The callout leaves through the network attachment, so it originates inside your VPC network.
  4. Your private DNS zone resolves the callout hostname to the internal IP address of the Private Service Connect endpoint.
  5. The endpoint forwards the callout to the service attachment of your Apigee instance.
  6. The environment group routes the callout by its hostname to the no-target proxy, where your policies run.
  7. The proxy returns a verdict to the gateway. Apigee never forwards the agent's traffic—the proxy has no target.
  8. If the verdict allows the request, the gateway sends the original request on to its destination.



The `AuthzPolicy` and `AuthzExtension` in figure 1 are configuration rather than traffic: the policy attaches the extension to the gateway, and the extension names the extension processor proxy that runs. You create both in Configure the authorization extension.

To connect the extension processor to a load balancer instead, see [Get started with the Apigee extension processor](https://docs.cloud.google.com/apigee/docs/api-platform/service-extensions/extension-processor-quickstart).

The following sections guide you through the steps: 

  * Configure the Apigee extension processor.
  * Connect the Agent Gateway to Apigee.
  * Configure the authorization extension.
  * Verify the connection.



## Before you begin

Before you begin, complete the following tasks: 

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Apigee, Compute Engine, Network Services, Network Security, and Cloud DNS APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=apigee.googleapis.com,compute.googleapis.com,networkservices.googleapis.com,networksecurity.googleapis.com,dns.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Apigee, Compute Engine, Network Services, Network Security, and Cloud DNS APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=apigee.googleapis.com,compute.googleapis.com,networkservices.googleapis.com,networksecurity.googleapis.com,dns.googleapis.com)

  8. Install the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

After you install the Google Cloud CLI, run the `gcloud components update` command to get the latest gcloud components.

  9. Provision an [Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/provisioning-intro) instance, if you have not already done so.

In the Google Cloud console, go to the **Apigee Instances** page.

[Go to Apigee Instances](https://console.cloud.google.com/apigee/instances)

  10. Deploy an Agent Gateway in the same region as your Apigee instance, with `governedAccessPath` set to `AGENT_TO_ANYWHERE` so that the gateway governs the agent's outbound traffic. For more information, see [Configure Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/set-up-agent-gateway).

You update this gateway's network configuration later, in Update the Agent Gateway, after the DNS zone exists.

  11. Confirm that you have a VPC and subnet that both the Agent Gateway and the Private Service Connect endpoint can use.

[Go to VPC Networks](https://console.cloud.google.com/networking/networks/list)




### Required roles

To get the permissions that you need to connect the Apigee extension processor to an Agent Gateway, ask your administrator to grant you the following IAM roles: 

  * Create and manage Apigee resources: [Apigee Org Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`) on organization 
  * Create and manage service extensions: [Service Extensions Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/networkservices#networkservices.serviceExtensionsAdmin) (`roles/networkservices.serviceExtensionsAdmin`) on organization 
  * Create and manage authorization policies: [Network Security Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.admin) (`roles/networksecurity.admin`) on organization 
  * Create and manage networking resources, including Private Service Connect endpoints and DNS: [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) on organization 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Set environment variables

Set the following environment variables to identify the resources you created in **Before you begin**. Each later section on this page defines the additional variables it needs, at the point where you create the resource they name.
    
    
    export PROJECT_ID=PROJECT_ID
    export ORG_NAME=$PROJECT_ID
    export REGION=REGION
    export INSTANCE=INSTANCE
    export VPC_NETWORK_NAME=VPC_NETWORK_NAME
    export SUBNET=SUBNET
    export GATEWAY=GATEWAY

Where: 

  * `PROJECT_ID` is the ID of the project that contains your Apigee instance.
  * `REGION` is the Google Cloud region of your Apigee instance.
  * `INSTANCE` is the name of your Apigee instance.
  * `VPC_NETWORK_NAME` and `SUBNET` are the VPC network and subnet that the Agent Gateway and the Private Service Connect endpoint use.
  * `GATEWAY` is the name of the Agent Gateway you deployed.



To confirm that the environment variables are set correctly, run the following command and review the output:
    
    
    echo $PROJECT_ID $ORG_NAME $REGION $INSTANCE $VPC_NETWORK_NAME $SUBNET $GATEWAY

### Choose the callout hostname

The gateway reaches Apigee at a private hostname that you choose. You choose it now, before creating anything, because the first resource you create—the Apigee environment group—uses it as its hostname, while the DNS zone that resolves it is not created until Create a private DNS zone.
    
    
    export DNS_DOMAIN=DNS_DOMAIN
    export EXTPROC_HOST=apigee-extproc.$DNS_DOMAIN

Where `DNS_DOMAIN` is a private DNS domain that does not have to be resolvable on the public internet, written **without** a trailing dot, for example `internal.example.com`. This gives an `EXTPROC_HOST` of `apigee-extproc.internal.example.com`. You can use a label other than `apigee-extproc`, as long as the hostname stays inside `DNS_DOMAIN`.

**Important:** `EXTPROC_HOST` is used in three places: the Apigee environment group hostname, the private DNS record, and the authorization extension's `authority` and `service` fields. All three must be identical, or the callout never reaches Apigee. The hostname must also sit inside `DNS_DOMAIN`, which is why the command above derives it from that variable.

### Configure an authentication token
    
    
    export TOKEN=$(gcloud auth print-access-token)
    echo $TOKEN

**Note:** If your organization uses data residency, replace `apigee.googleapis.com` in the commands on this page with the regional endpoint for your organization. For more information, see [Use regional endpoints for data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#drz-regional-endpoint).

## Configure the Apigee extension processor

Name the Apigee resources that this section creates:
    
    
    export EXTPROC_ENV=EXTPROC_ENV
    export EXTPROC_ENVGROUP=EXTPROC_ENVGROUP
    export PROXY_NAME=PROXY_NAME

Where: 

  * `EXTPROC_ENV` and `EXTPROC_ENVGROUP` are names you choose for an Apigee environment and environment group dedicated to the extension processor, for example `extproc-env` and `extproc-envgroup`. Each name must be 2 to 32 characters of lowercase letters, numbers or hyphens, must begin with a letter, and cannot end with a hyphen. The environment name must differ from every other environment name in your organization.
  * `PROXY_NAME` is a name you choose for the extension processor proxy, for example `extproc-authz`.



The Apigee side of the configuration is the same as for a load balancer. Follow [Configure the Apigee extension processor](https://docs.cloud.google.com/apigee/docs/api-platform/service-extensions/extension-processor-quickstart#configure-ext-proc) in the quickstart to:

  1. Create an Apigee environment with the property `apigee-service-extension-enabled` set to `true`, attach it to your instance, and create an environment group whose hostname is `$EXTPROC_HOST`.
  2. Create and deploy a **no-target** extension processor proxy to that environment.

**Note:** The quickstart names these resources `ENV_NAME`, `ENV_GROUP_NAME` and `ENV_GROUP_HOSTNAME`. Use `$EXTPROC_ENV`, `$EXTPROC_ENVGROUP` and `$EXTPROC_HOST` respectively.**Note:** If any policy in the proxy calls a Google Cloud API, deploy the proxy with a service account by appending `?serviceAccount=SERVICE_ACCOUNT_EMAIL` to the deployment request. Otherwise the deployment fails with `MISSING_SERVICE_ACCOUNT`.

Then list the deployments in the environment:
    
    
    curl -s -H "Authorization: Bearer $TOKEN" \
      "https://apigee.googleapis.com/v1/organizations/$ORG_NAME/environments/$EXTPROC_ENV/deployments"

The environment can have more than one proxy deployed, so in the response, find the entry whose `apiProxy` is `$PROXY_NAME` and note its `revision`.

You can review the proxy in the Google Cloud console:

[Go to API Proxies](https://console.cloud.google.com/apigee/proxies)

Set the following variable to that revision, which you need in Verify the connection:
    
    
    export REVISION=REVISION

## Connect the Agent Gateway to Apigee

The gateway reaches Apigee over a [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) endpoint in your VPC, which it finds by resolving `$EXTPROC_HOST` on a private DNS zone.

### Find the service attachment

Find the service attachment of your Apigee instance:
    
    
    curl -s -H "Authorization: Bearer $TOKEN" \
      "https://apigee.googleapis.com/v1/organizations/$ORG_NAME/instances"

Set the following variable to the `serviceAttachment` value of the instance in your region:
    
    
    export SERVICE_ATTACHMENT=SERVICE_ATTACHMENT

### Create a network attachment

The Agent Gateway egresses into your VPC through a network attachment. Choose a name for it, for example `agent-gateway-attachment`, and create it:
    
    
    export NETWORK_ATTACHMENT=NETWORK_ATTACHMENT
    gcloud compute network-attachments create $NETWORK_ATTACHMENT \
        --region=$REGION --subnets=$SUBNET --connection-preference=ACCEPT_AUTOMATIC

### Create the Private Service Connect endpoint

Reserve an internal IP address and create the Private Service Connect endpoint:
    
    
    gcloud compute addresses create apigee-extproc-psc-ip \
        --region=$REGION --subnet=$SUBNET --purpose=GCE_ENDPOINT
    gcloud compute forwarding-rules create apigee-extproc-psc-endpoint \
        --region=$REGION --network=$VPC_NETWORK_NAME \
        --address=apigee-extproc-psc-ip \
        --target-service-attachment=$SERVICE_ATTACHMENT

In the Google Cloud console, go to the **Private Service Connect** page.

[Go to Private Service Connect](https://console.cloud.google.com/net-services/psc/list/consumers)

Confirm that the endpoint reports `pscConnectionStatus: ACCEPTED`, and set the following variable to its IP address:
    
    
    gcloud compute forwarding-rules describe apigee-extproc-psc-endpoint \
        --region=$REGION --format="value(pscConnectionStatus,IPAddress)"
    export PSC_IP=PSC_IP

If the status is `PENDING`, your project is not in the Apigee instance's `consumerAcceptList`, and the connection cannot be accepted.

### Create a private DNS zone

Create a private DNS zone for `$DNS_DOMAIN` and an `A` record that resolves `$EXTPROC_HOST` to the endpoint's IP address:
    
    
    gcloud dns managed-zones create extproc-zone \
        --dns-name=$DNS_DOMAIN. --visibility=private --networks=$VPC_NETWORK_NAME \
        --description="Apigee extension processor callout host"
    gcloud dns record-sets create $EXTPROC_HOST. --type=A --ttl=300 \
        --rrdatas=$PSC_IP --zone=extproc-zone

### Update the Agent Gateway

Update the Agent Gateway from **Before you begin** so that it egresses through your network attachment and can resolve the zone you created.

**Caution:** Importing an Agent Gateway replaces the entire resource. Always start from the exported configuration and edit it, rather than writing a new file, or fields that you omit—such as `protocols` and `registries`—are removed from the gateway.

  1. Export the current configuration:
         
         gcloud network-services agent-gateways export $GATEWAY \
             --location=$REGION --destination=agent-gateway.yaml

  2. In `agent-gateway.yaml`, add the following `networkConfig` block, replacing each placeholder with the value of the corresponding environment variable. The file is edited directly, so shell variables are not substituted here:
         
         networkConfig:
           egress:
             networkAttachment: projects/PROJECT_ID/regions/REGION/networkAttachments/NETWORK_ATTACHMENT
           dnsPeeringConfig:
             domains: [ DNS_DOMAIN. ]
             targetProject: PROJECT_ID
             targetNetwork: projects/PROJECT_ID/global/networks/VPC_NETWORK_NAME

Leave the rest of the file, including `googleManaged.governedAccessPath`, `protocols` and `registries`, as exported.

  3. Import the edited configuration:
         
         gcloud network-services agent-gateways import $GATEWAY \
             --location=$REGION --source=agent-gateway.yaml




For the full set of Agent Gateway fields, see [Configure Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/set-up-agent-gateway).

## Configure the authorization extension

Two resources connect the gateway to your extension processor proxy: an authorization extension that points at Apigee, and an authorization policy that attaches the extension to the gateway.

### Create the authorization extension

Choose a name for the authorization extension, for example `apigee-authz-extension`. The `metadata` fields select which Apigee proxy runs and whether the message bodies are sent to it:
    
    
    export AUTHZ_EXT=AUTHZ_EXT
    cat > authz-extension.yaml <<EOF
    name: projects/$PROJECT_ID/locations/$REGION/authzExtensions/$AUTHZ_EXT
    authority: $EXTPROC_HOST
    service: $EXTPROC_HOST
    timeout: 5s
    metadata:
      apigee-extension-processor: $PROXY_NAME
      apigee-request-body: 'true'
      apigee-response-body: 'true'
    EOF
    gcloud service-extensions authz-extensions import $AUTHZ_EXT \
        --source=authz-extension.yaml --location=$REGION

Where: 

  * `apigee-extension-processor` selects the extension processor proxy that processes the traffic.
  * `apigee-request-body` and `apigee-response-body` make the request and response bodies available in the proxy as `request.content` and `response.content`. Without them, policies that inspect the payload find nothing.



### Create the authorization policy

Choose a name for the authorization policy, for example `apigee-content-authz-policy`. The policy attaches the extension to the gateway and determines which traffic is sent to Apigee:
    
    
    export AUTHZ_POLICY=AUTHZ_POLICY
    cat > authz-policy.yaml <<EOF
    name: projects/$PROJECT_ID/locations/$REGION/authzPolicies/$AUTHZ_POLICY
    action: CUSTOM
    policyProfile: CONTENT_AUTHZ
    customProvider:
      authzExtension:
        resources:
        - projects/$PROJECT_ID/locations/$REGION/authzExtensions/$AUTHZ_EXT
    httpRules:
    - to:
        operations:
        - paths:
          - prefix: "/"
    target:
      resources:
      - projects/$PROJECT_ID/locations/$REGION/agentGateways/$GATEWAY
    EOF
    gcloud beta network-security authz-policies import $AUTHZ_POLICY \
        --source=authz-policy.yaml --location=$REGION

Use `policyProfile: CONTENT_AUTHZ` so that the message bodies are inspected. A `REQUEST_AUTHZ` policy evaluates request headers only.

**Important:** The example above matches every request with `prefix: "/"`, which sends all of the agent's traffic to Apigee—including its session, telemetry, and tool calls. Narrow the scope with `to.operations.paths`, or with a [Common Expression Language (CEL)](https://docs.cloud.google.com/service-extensions/docs/cel-matcher-language-reference) expression in a `when` field, so that only the traffic you intend to govern is processed.

## Verify the connection

To generate traffic, you need an agent whose egress is governed by this gateway. An agent is bound to a gateway when the agent is created, by setting its Agent Gateway configuration to `$GATEWAY`; you cannot exercise the connection with a direct HTTP request to the gateway. For more information, see [Configure Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/set-up-agent-gateway).

Start an Apigee [debug session](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace) on the extension processor proxy, then send one request through the agent:
    
    
    curl -s -X POST -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
      "https://apigee.googleapis.com/v1/organizations/$ORG_NAME/environments/$EXTPROC_ENV/apis/$PROXY_NAME/revisions/$REVISION/debugsessions?timeout=600" \
      -d '{"count":15,"tracesize":5120,"filter":"(request.uri Like \"*generateContent*\")"}'

**Note:** A single agent turn produces several transactions, because the agent's session and telemetry calls also pass through the gateway. Use the `filter` field to capture only the traffic you want to inspect, or the buffer may fill before the request you are looking for arrives.

In the captured transactions, confirm that: 

  * the request URL is the address the _agent_ called, such as the model endpoint or a tool host, rather than an Apigee base path;
  * `request.content` and `response.content` are populated, which confirms that the body metadata on the authorization extension is working.



If no transactions appear, check that the environment group hostname, the DNS record, and the extension's `authority` and `service` fields are all `$EXTPROC_HOST`, that the Private Service Connect endpoint reports `ACCEPTED`, and that the gateway's `governedAccessPath` is `AGENT_TO_ANYWHERE`.

## What's next

  * Read the [Apigee extension processor overview](https://docs.cloud.google.com/apigee/docs/api-platform/service-extensions/extension-processor-overview).
  * Get started with the [Apigee extension processor on a load balancer](https://docs.cloud.google.com/apigee/docs/api-platform/service-extensions/extension-processor-quickstart).
  * [Configure Apigee policies with the extension processor](https://docs.cloud.google.com/apigee/docs/api-platform/service-extensions/extension-processor-policies), which covers the policy configuration that is specific to the extension processor.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
