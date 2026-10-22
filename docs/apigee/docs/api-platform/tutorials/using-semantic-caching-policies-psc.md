---
url: https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/using-semantic-caching-policies-psc/
title: Semantic caching with a private (Private Service Connect) endpoint \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:31:57.641222+00:00
---

# Semantic caching with a private (Private Service Connect) endpoint  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/using-semantic-caching-policies-psc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Semantic caching with a private (Private Service Connect) endpoint Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This page describes how to configure and use the Apigee semantic caching policies to enable intelligent response reuse based on semantic similarity. In this example, the policies run their similarity search against a Vector Search index that is deployed on a _private (Private Service Connect) endpoint_. Using these policies in your Apigee API proxy minimizes redundant backend API calls, reduces latency, and lowers operational costs.

This guide applies to both Apigee and Apigee Hybrid. The policy configuration is identical on both platforms—only how the runtime reaches the private endpoint differs, as described in Step 2: Connect to the service attachment. On Apigee Hybrid, semantic caching over a private (Private Service Connect) endpoint is supported in **version 1.17.0 and later**. For more information, see Set up on Apigee Hybrid.

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

  4. Enable the Compute Engine, AI Platform, and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,aiplatform.googleapis.com,storage.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Compute Engine, AI Platform, and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,aiplatform.googleapis.com,storage.googleapis.com)

  8. Enable and configure the Vertex AI [ Text embeddings API](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/embeddings/get-text-embeddings) in your Google Cloud project.
  9. Create (or have access to) a Vector Search index deployed on a _private (Private Service Connect)_ endpoint. This tutorial does not duplicate the Vector Search setup steps; see Vector Search index prerequisites for the SemanticCacheLookup-specific requirements and links to the Vector Search documentation.
  10. Confirm that you have an [Intermediate](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-overview#environment-types) or [Comprehensive](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-overview#environment-types) environment available in your Apigee instance. Semantic caching policies can only be deployed in **Intermediate** or **Comprehensive** environments.
  11. Confirm that you have a [environment group](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-overview) with a runtime hostname that you can use to send requests to your API proxy.



### Required roles

To get the permissions that you need to create and use the semantic caching policies, ask your administrator to grant you the [AI Platform User ](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.user) (`roles/aiplatform.user`) IAM role on the service account you use to deploy Apigee proxies. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** The identity deploying the proxy needs the `roles/iam.serviceAccountUser` (Service Account User) role on `SERVICE_ACCOUNT` (or at the project level). See Step 4: Import and deploy the API proxy.

### Set environment variables

In the Google Cloud project that contains your Apigee instance, use the following command to set environment variables: 
    
    
    export PROJECT_ID=PROJECT_ID
    export REGION=REGION
    export RUNTIME_HOSTNAME=RUNTIME_HOSTNAME

Where: 

  * `PROJECT_ID` is the ID of the project with your Apigee instance.
  * `REGION` is the Google Cloud region of your Apigee instance.
  * `RUNTIME_HOSTNAME` is the hostname of your Apigee runtime.



To confirm that the environment variables are set correctly, run the following command and review the output: 
    
    
    echo $PROJECT_ID $REGION $RUNTIME_HOSTNAME

### Set the project

Set the Google Cloud project in your development environment: 
    
    
        gcloud auth login
        gcloud config set project $PROJECT_ID

### Vector Search index prerequisites

This tutorial assumes that you already have (or will create) a Vector Search index deployed on a **private (Private Service Connect)** endpoint. Creating, formatting, and deploying a Vector Search index is documented in the Vector Search guides, so this tutorial does not duplicate those steps. Follow the Vector Search documentation to:

  * [Create and manage an index](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search/create-manage-index).
  * [Format and structure your input data](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search/format-structure).
  * [Create a Private Service Connect index endpoint and deploy your index to it](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search/deploy-index-vpc).



When you create the index, it must meet the following SemanticCacheLookup-specific requirements:

  * The index must use `STREAM_UPDATE` (`"indexUpdateMethod": "STREAM_UPDATE"`) so that the SemanticCachePopulate policy's `upsertDatapoints` calls become queryable in near real time.
  * The index `dimensions` must match the output dimensionality of the embeddings model you use in the SemanticCacheLookup policy. This tutorial uses `gemini-embedding-001`, which produces 3072-dimensional embeddings by default. If you truncate the output to a lower dimensionality (for example, 768 or 1536), set `dimensions` to the same value.
  * Create the index with the distance measure (`distanceMeasureType`) that matches your policy's `<DistanceMeasureType>`. The `<SimilaritySearch><VertexAI><DistanceMeasureType>` element in the SemanticCacheLookup policy is optional and defaults to `DOT_PRODUCT_DISTANCE`; `COSINE_DISTANCE` is also supported. The index distance measure and the policy `<DistanceMeasureType>` must be the same.



The following minimal example creates a compatible index. For the full request body and all available options, see [Create and manage an index](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search/create-manage-index):
    
    
    ACCESS_TOKEN=$(gcloud auth print-access-token) && curl -X POST \
      "https://$REGION-aiplatform.googleapis.com/v1/projects/$PROJECT_ID/locations/$REGION/indexes" \
      -H "Authorization: Bearer $ACCESS_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "displayName": "semantic-cache-index",
        "metadata": {
          "config": {
            "dimensions": 3072,
            "distanceMeasureType": "DOT_PRODUCT_DISTANCE"
          }
        },
        "indexUpdateMethod": "STREAM_UPDATE"
      }'

Note the numeric `INDEX_ID` returned in the response; you use it in the SemanticCachePopulate policy. After you create the index, create a Private Service Connect index endpoint and deploy the index to it.

When you create the Private Service Connect index endpoint, it must meet the following SemanticCacheLookup-specific requirements:

  * The `projectAllowlist` **must include the Apigee project that initiates the connection** : 
    * **Apigee:** Use the Apigee tenant project. Get the tenant project ID from the [Organizations API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/get) (`apigeeProjectId` field).
The `projectAllowlist` cannot be modified after the index endpoint is created. If you allowlist the wrong project, you must delete and re-create the index endpoint.



Note the numeric `INDEX_ENDPOINT_ID` of the index endpoint.

### Configure the service account for the Apigee proxy

The Apigee proxy uses a service account for its Vertex AI REST calls: the Embeddings API in the SemanticCacheLookup policy, `upsertDatapoints` in the SemanticCachePopulate policy, and the model target. Grant that service account the `AI Platform User` (`roles/aiplatform.user`) role:
    
    
    gcloud projects add-iam-policy-binding $PROJECT_ID \
      --member="serviceAccount:SERVICE_ACCOUNT" \
      --role="roles/aiplatform.user"

Where `SERVICE_ACCOUNT` is the email address of the service account that the proxy uses. You reference this service account when you deploy the proxy in Step 4: Import and deploy the API proxy.

**Note:** The identity that deploys the proxy needs the `roles/iam.serviceAccountUser` (Service Account User) role on `SERVICE_ACCOUNT` (or at the project level) to deploy a proxy with that service account attached. See Step 4: Import and deploy the API proxy.

### Additional prerequisites for Apigee Hybrid deployments

For Apigee Hybrid deployments, confirm the following additional requirements:

  * **A hybrid runtime on 1.17.0 or later** , installed in your own Kubernetes cluster. See the [Apigee Hybrid installation documentation](https://docs.cloud.google.com/apigee/docs/hybrid/latest/install-intro). This feature adds no cluster requirements of its own—any supported hybrid cluster works.
  * **An Intermediate or Comprehensive environment** and an environment group with a runtime hostname, the same as on Apigee. Semantic caching policies deploy only to Intermediate or Comprehensive environments.
  * **Network reachability from the runtime to the private endpoint.** The message processor must be able to open a plaintext gRPC connection to the Vector Search Private Service Connect endpoint on `TARGET_HOST:10000`.
  * **Egress for the REST calls.** The Embeddings, Populate, and model-target calls go to the public `REGION-aiplatform.googleapis.com` surface, so the runtime also needs a path to Google APIs—directly, or over a private path if your cluster has no public egress.



## Set up on Apigee Hybrid

Semantic caching over a private (Private Service Connect) endpoint is supported on Apigee Hybrid **version 1.17.0 and later**. The policy configuration and the Vector Search steps in this tutorial are identical to Apigee—the difference is that on hybrid you run the runtime and provide its connectivity yourself. Because hybrid deployments vary widely, this section is general guidance rather than exact commands. The only requirement this feature adds is that the runtime must be able to reach the private endpoint over plaintext gRPC.

### Provide network reachability

In hybrid deployments, you must manage connectivity manually because there is no Apigee-managed endpoint attachment. Create a [Private Service Connect endpoint](https://docs.cloud.google.com/vpc/docs/private-service-connect#endpoints) in your consumer VPC that points to the Vector Search `SERVICE_ATTACHMENT`, and use its internal IP address as the `TARGET_HOST` in the proxy. See Step 2: Connect to the service attachment for more information. The specific routing (e.g., Shared VPC or VPC-native GKE) depends on your cluster's configuration.

If your cluster lacks public internet egress, ensure the runtime has a private path to Google APIs, such as [Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access), to handle REST communication.

After establishing connectivity to `grpc://TARGET_HOST:10000`, follow the subsequent steps—creating and deploying the index, building the proxy, and testing—which are identical for both Apigee and Apigee Hybrid.

## Overview

The semantic caching policies help Apigee users with LLM models to intelligently serve identical or semantically similar prompts efficiently, minimizing backend API calls and reducing resource consumption. 

The [SemanticCacheLookup](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-lookup-policy) and [SemanticCachePopulate](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-populate-policy) policies attach to the request and response flows, respectively, of an Apigee API proxy. When the proxy receives a request, the SemanticCacheLookup policy extracts the user prompt from the request and converts the prompt into a numerical representation using the Text embeddings API. A semantic similarity search performs using Vector Search to find similar prompts. If a similar prompt data point is found, a cache lookup performs. If cached data is found, the cached response returns to the client.

If the similarity search does not return a similar previous prompt, the LLM model generates content in response to the user prompt and populates the Apigee cache with the response. A feedback loop creates to update the Vector Search index entries in preparation for future requests.

In this scenario, the Vector Search index is deployed on a _private_ (Private Service Connect) endpoint, over gRPC. See more details about Vector Search Private Service Connect support in [Query Private Services Access or Private Service Connect indexes](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search/query-index-vpc).

**Note:** This tutorial runs the similarity search against a Vector Search index deployed on a _private_ (Private Service Connect) endpoint, over gRPC. To run the similarity search against a _public_ Vector Search index over REST, see [Get started with semantic caching policies](https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/using-semantic-caching-policies).

The following sections describe the steps to create and configure the semantic caching policies: 

  1. Verify your resources and get the values Apigee needs.
  2. Connect to the service attachment.
  3. Build the API proxy bundle.
  4. Import and deploy the API proxy.
  5. Test the semantic caching policies.



## Step 1: Verify your resources and get the values Apigee needs

Before you configure Apigee, confirm that your Vector Search index endpoint is Private Service Connect-enabled and that your index is deployed. Then read the two values that the Apigee proxy consumes: the service attachment and the `DEPLOYED_INDEX_ID`.

Confirm that the index is deployed and that the endpoint exposes a Private Service Connect service attachment:
    
    
    gcloud ai index-endpoints describe INDEX_ENDPOINT_ID \
      --project=$PROJECT_ID --region=$REGION \
      --format="value(deployedIndexes.privateEndpoints.serviceAttachment)"

The command returns a service attachment resource name of the form `projects/TENANT_PROJECT/regions/REGION/serviceAttachments/SERVICE_ATTACHMENT_NAME`. This guide refers to that value as `SERVICE_ATTACHMENT`. If the command returns an empty value, the index is not yet deployed on a Private Service Connect endpoint. Return to Vector Search index prerequisites and finish deploying the index before you continue.

Read the `DEPLOYED_INDEX_ID` of the index deployed on the endpoint:
    
    
    gcloud ai index-endpoints describe INDEX_ENDPOINT_ID \
      --project=$PROJECT_ID --region=$REGION \
      --format="value(deployedIndexes.id)"

This guide refers to that value as `DEPLOYED_INDEX_ID`. You use it in the SemanticCacheLookup policy in Step 3: Build the API proxy bundle.

For more information on deploying and querying private index endpoints, see [Deploy an index to a Private Service Connect endpoint](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search/deploy-index-vpc) and [Query Private Services Access or Private Service Connect indexes](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search/query-index-vpc).

## Step 2: Connect to the service attachment

This step gives you the private **host** that the proxy's `<GrpcEndpoint>` calls. How you create it depends on your platform. The proxy configuration in the later steps is identical either way.

### Apigee: Create an endpoint attachment

On Apigee, create an Apigee endpoint attachment. The endpoint attachment is Apigee's Private Service Connect consumer side. It connects to the Vector Search service attachment and gives you a private host that the proxy calls.
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
            "location": "'"$REGION"'",
            "serviceAttachment": "SERVICE_ATTACHMENT"
          }' \
      "https://apigee.googleapis.com/v1/organizations/$PROJECT_ID/endpointAttachments?endpointAttachmentId=ENDPOINT_ATTACHMENT"

Poll until the attachment's `state` is `ACTIVE` and its `connectionState` is `ACCEPTED`, then note the host: 
    
    
    curl -s -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      "https://apigee.googleapis.com/v1/organizations/$PROJECT_ID/endpointAttachments/ENDPOINT_ATTACHMENT"

The response contains the host in the `host` field. This guide refers to that value as `TARGET_HOST`.

To connect to the Vector Search service attachment from your proxy, you can use either:

  * **The IP address:** Use the IP address returned in the `host` field directly as `TARGET_HOST` (for example, `7.0.3.4`).
  * **A private DNS record:** If you configured a private Cloud DNS zone in your Google Cloud project with DNS peering to Apigee, you can create an A record in your private zone pointing to the endpoint attachment IP address and use that domain name (such as `vectorsearch.example.com`) as `TARGET_HOST`. For more information, see [Use a DNS record](https://docs.cloud.google.com/apigee/docs/api-platform/architecture/southbound-networking-patterns-endpoints#use-a-dns-record) and [Connecting with private DNS peering zones](https://docs.cloud.google.com/apigee/docs/api-platform/architecture/southbound-networking-patterns-endpoints#connecting-with-private-dns-peering-zones).

**Note:** If `connectionState` stays `PENDING`, the Vector Search service attachment is not accepting the connection—usually because the tenant project is not allowlisted. Because the index endpoint's `projectAllowlist` cannot be modified after creation, return to Vector Search index prerequisites and re-create the index endpoint with the correct `privateServiceConnectConfig.projectAllowlist` value.

### Private Service Connect endpoint for Apigee Hybrid

In Apigee, Google provides an "endpoint attachment" resource that handles the Private Service Connect connection. However, in Apigee Hybrid you manage the runtime and the network environment. No matter where your cluster runs, it must be able to reach the Vector Search Private Service Connect endpoint over a plaintext gRPC connection to `host:10000`.

For Apigee Hybrid, create a Private Service Connect endpoint in a Google Cloud consumer VPC that points to the Vector Search `SERVICE_ATTACHMENT`. Use the endpoint's internal IP address as the `TARGET_HOST` in your proxy configuration. Ensure that the Google Cloud project hosting this endpoint is included in the Vector Search index endpoint's `projectAllowlist`. See Vector Search index prerequisites for more detail.

## Step 3: Build the API proxy bundle

### Create the proxy bundle

Create the following directory layout: 
    
    
    apiproxy/
    ├── PROXY_NAME.xml
    ├── proxies/default.xml
    ├── targets/default.xml
    └── policies/
        ├── SCL-1.xml
        └── SCP-1.xml

**`policies/SCL-1.xml`** —the SemanticCacheLookup policy. The `<SimilaritySearch>` block uses `<PrivateServiceConnect><GrpcEndpoint>` (no `<URL>`). **Note:** The `<PrivateServiceConnect>` transport is supported on Apigee, and on Apigee Hybrid **version 1.17.0 and later**.

Note: `<GrpcEndpoint>` rules: 

  * The format is `grpc://TARGET_HOST:PORT`; the scheme must be `grpc://`. `grpcs://` (TLS) is _not_ supported in this version.
  * The port is `10000` for Vector Search. Private Service Connect data-plane endpoints serve gRPC on port 10000, so the endpoint is always `grpc://TARGET_HOST:10000`.
  * `TARGET_HOST` can be either the endpoint attachment IP address (from Step 2) or a custom DNS record created in your private DNS zone.
  * The gRPC hop is plaintext and unauthenticated (secured by network isolation).


    
    
    <SemanticCacheLookup async="false" continueOnError="false" enabled="true" name="SCL-1">
      <DisplayName>SCL-1</DisplayName>
      <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
      <UserPromptSource>{jsonPath('$.contents[-1].parts[-1].text',request.content,true)}</UserPromptSource>
      <Embeddings>
        <VertexAI>
          <URL>https://REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/publishers/google/models/gemini-embedding-001:predict</URL>
        </VertexAI>
      </Embeddings>
      <SimilaritySearch>
        <VertexAI>
          <PrivateServiceConnect>
            <GrpcEndpoint>grpc://TARGET_HOST:10000</GrpcEndpoint>
          </PrivateServiceConnect>
          <DeployedIndexID>DEPLOYED_INDEX_ID</DeployedIndexID>
          <Threshold>0.95</Threshold>
        </VertexAI>
      </SimilaritySearch>
    </SemanticCacheLookup>

**`policies/SCP-1.xml`** —the SemanticCachePopulate policy. Populate is REST-only and must use `<URL>` (it rejects `<PrivateServiceConnect>` at deployment time): 
    
    
    <SemanticCachePopulate async="false" continueOnError="true" enabled="true" name="SCP-1">
      <DisplayName>SCP-1</DisplayName>
      <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
      <SimilaritySearch>
        <VertexAI>
          <URL>https://REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/indexes/INDEX_ID:upsertDatapoints</URL>
        </VertexAI>
      </SimilaritySearch>
      <TTLInSeconds>3600</TTLInSeconds>
    </SemanticCachePopulate>

**`targets/default.xml`** —the model target. The target calls a Google API, so it needs a token; `<GoogleAccessToken>` uses the deployment's service account: 
    
    
    <TargetEndpoint name="default">
      <PreFlow name="PreFlow"><Request/><Response/></PreFlow>
      <PostFlow name="PostFlow"><Request/><Response/></PostFlow>
      <HTTPTargetConnection>
        <Authentication>
          <GoogleAccessToken>
            <Scopes>
              <Scope>https://www.googleapis.com/auth/cloud-platform</Scope>
            </Scopes>
          </GoogleAccessToken>
        </Authentication>
        <URL>https://REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/publishers/google/models/gemini-2.5-flash:generateContent</URL>
      </HTTPTargetConnection>
    </TargetEndpoint>

**`proxies/default.xml`** —run the SemanticCacheLookup policy on the request and the SemanticCachePopulate policy on the response: 
    
    
    <ProxyEndpoint name="default">
      <PreFlow name="PreFlow">
        <Request><Step><Name>SCL-1</Name></Step></Request>
        <Response><Step><Name>SCP-1</Name></Step></Response>
      </PreFlow>
      <PostFlow name="PostFlow"><Request/><Response/></PostFlow>
      <HTTPProxyConnection>
        <BasePath>/PROXY_NAME</BasePath>
      </HTTPProxyConnection>
      <RouteRule name="default">
        <TargetEndpoint>default</TargetEndpoint>
      </RouteRule>
    </ProxyEndpoint>

**`PROXY_NAME.xml`**—the bundle descriptor: 
    
    
    <APIProxy name="PROXY_NAME">
      <BasePaths>/PROXY_NAME</BasePaths>
      <Policies><Policy>SCL-1</Policy><Policy>SCP-1</Policy></Policies>
      <ProxyEndpoints><ProxyEndpoint>default</ProxyEndpoint></ProxyEndpoints>
      <TargetEndpoints><TargetEndpoint>default</TargetEndpoint></TargetEndpoints>
    </APIProxy>

## Step 4: Import and deploy the API proxy

Zip the bundle, import it to create a new revision, and deploy the revision with your service account: 
    
    
    TOKEN=$(gcloud auth print-access-token)
    (cd BUNDLE_DIR && zip -r ../PROXY_NAME.zip apiproxy)
    curl -X POST -H "Authorization: Bearer $TOKEN" \
      -F "file=@PROXY_NAME.zip" \
      "https://apigee.googleapis.com/v1/organizations/$PROJECT_ID/apis?action=import&name=PROXY_NAME"
    curl -X POST -H "Authorization: Bearer $TOKEN" \
      "https://apigee.googleapis.com/v1/organizations/$PROJECT_ID/environments/ENV/apis/PROXY_NAME/revisions/REVISION/deployments?override=true&serviceAccount=SERVICE_ACCOUNT"

Where: 

  * `BUNDLE_DIR` is the directory that contains the `apiproxy/` folder. The archive must contain the `apiproxy/` folder at its root.
  * `ENV` is the Apigee environment where you deploy the proxy. The environment must be an **Intermediate** or **Comprehensive** environment.
  * `REVISION` is the revision number returned by the import call.
  * `SERVICE_ACCOUNT` is the email address of the service account you use to deploy the proxy.

**Note:** The identity deploying the proxy needs the `roles/iam.serviceAccountUser` (Service Account User) role on `SERVICE_ACCOUNT` (or at the project level) to deploy a proxy with that service account attached. Project Owners and Editors have this permission by default. If your deploying identity is not an Owner or Editor, grant the role on the service account using: 
    
    
    gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT \
      --member="user:DEPLOYER_EMAIL" \
      --role="roles/iam.serviceAccountUser"

Wait until the deployment reports `READY`: 
    
    
    curl -s -H "Authorization: Bearer $TOKEN" \
      "https://apigee.googleapis.com/v1/organizations/$PROJECT_ID/environments/ENV/apis/PROXY_NAME/revisions/REVISION/deployments" | jq .state

**Note:** You can also import and deploy the proxy from the Apigee UI or with [apigeecli](https://github.com/apigee/apigeecli).

## Step 5: Test the semantic caching policies

Send a _new_ prompt. This is a cache miss: the model is called and the answer is cached. 
    
    
    curl -X POST "https://$RUNTIME_HOSTNAME/PROXY_NAME" \
      -H "Content-Type: application/json" \
      -d '{"contents":[{"role":"user","parts":[{"text":"Explain in one sentence why the sky appears blue."}]}]}'

Send the same prompt again. This is a cache hit: the response is served from the cache and the model is _not_ called. 
    
    
    curl -i -X POST "https://$RUNTIME_HOSTNAME/PROXY_NAME" \
      -H "Content-Type: application/json" \
      -d '{"contents":[{"role":"user","parts":[{"text":"Explain in one sentence why the sky appears blue."}]}]}'

On the hit, the response includes the `Cached-content: true` header, the same answer, and a noticeably lower latency.

You can also verify caching with a [debug session](https://docs.cloud.google.com/apigee/docs/api-platform/debug/using-debug-tool). On a hit, the SemanticCacheLookup policy sets the following flow variables: 

Variable | Value on a hit  
---|---  
`SemanticCacheLookup.SCL-1.dense_embeddings` | The prompt's embedding vector.  
`SemanticCacheLookup.SCL-1.is_nearest_neighbor_hit` | `true`  
`SemanticCacheLookup.SCL-1.cache_hit` | `true`  
`SemanticCacheLookup.SCL-1.cached_llm_response` | The cached answer.  
  
On a hit, the model target is not invoked—the flow short-circuits and returns the cached response.

## Troubleshooting

For the full error reference, see the [SemanticCacheLookup policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-lookup-policy#errorreference). 

## Limitations

The following limitations apply to the semantic caching policies: 

  * The maximum cacheable text size is 256 KB. For more information, see the **Cache value size** on the Apigee [Limits](https://docs.cloud.google.com/apigee/docs/api-platform/reference/limits#cache) page.
  * Apigee ignores any cache-control headers it receives from the LLM model.
  * If the cache is not invalidated properly or if the semantic similarity algorithm is not sufficiently accurate to differentiate between inputs with very similar meanings, the response may return outdated or incorrect information. 
    * For more information on configuring TTL to manage data freshness, see the [Best practices](https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/using-semantic-caching-policies#best-practices) section.
    * For more information on configuring the semantic similarity threshold, see the [Configure the semantic caching policies](https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/using-semantic-caching-policies#configure-policies) section.
    * For more information on tuning the semantic similarity algorithm, see [Filter vector matches](https://docs.cloud.google.com/vertex-ai/docs/vector-search/filtering).
  * The Vector Search feature is not supported in all regions. For a list of supported regions, see the [ Feature availability](https://docs.cloud.google.com/vertex-ai/docs/general/locations#feature-availability) section of the Vertex AI Locations page. If your Apigee organization is in an unsupported region, you will have to create index endpoints in a different region than your Apigee organization.
  * The semantic caching policies are not supported for use with [API proxies using EventFlows for continuous response streaming of server-sent events (SSE)](https://docs.cloud.google.com/apigee/docs/api-platform/develop/server-sent-events).
  * The semantic caching policies use LLM APIs, which can result in higher latencies in the 100s of milliseconds.
  * In Apigee hybrid installations, support for the semantic caching policies is limited to installations on Google Cloud Platform.
  * When the SemanticCacheLookup policy is configured to use a private Vector Search endpoint through Private Service Connect (PSC), the similarity-search call is sent over a direct gRPC connection to the private endpoint and does not go through a configured forward proxy.



## What's next

  * Learn how to [query Private Services Access or Private Service Connect indexes](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search/query-index-vpc) in Vector Search.
  * Learn how to configure semantic caching against a public endpoint in [Get started with semantic caching policies](https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/using-semantic-caching-policies).
  * Learn how to [Get started with Model Armor policies](https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/using-model-armor-policies).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
