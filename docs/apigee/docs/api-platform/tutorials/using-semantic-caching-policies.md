---
url: https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/using-semantic-caching-policies/
title: Get started with semantic caching policies \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:56:35.806541+00:00
---

# Get started with semantic caching policies  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/using-semantic-caching-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Get started with semantic caching policies Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This page describes how to configure and use the Apigee semantic caching policies to enable intelligent response reuse based on semantic similarity. Using these policies in your Apigee API proxy minimizes redundant backend API calls, reduces latency, and lowers operational costs.

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

  8. Set up and configure the Vertex AI [ Text embeddings API](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/embeddings/get-text-embeddings) and [Vector Search](https://docs.cloud.google.com/vertex-ai/docs/vector-search/overview) within your Google Cloud project.
  9. Confirm that you have an [Intermediate](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-overview#environment-types) or [Comprehensive](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-overview#environment-types) environment available in your Apigee instance. Semantic caching policies can only be deployed in **Intermediate** or **Comprehensive** environments.



### Required roles

To get the permissions that you need to create and use the semantic caching policies, ask your administrator to grant you the [AI Platform User ](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.user) (`roles/aiplatform.user`) IAM role on the service account you use to deploy Apigee proxies. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

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

## Overview

The semantic caching policies help Apigee users with LLM models to intelligently serve identical or semantically similar prompts efficiently, minimizing backend API calls and reducing resource consumption. 

The [SemanticCacheLookup](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-lookup-policy) and [SemanticCachePopulate](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-populate-policy) policies attach to the request and response flows, respectively, of an Apigee API proxy. When the proxy receives a request, the SemanticCacheLookup policy extracts the user prompt from the request and converts the prompt into a numerical representation using the Text embeddings API. A semantic similarity search performs using Vector Search to find similar prompts. If a similar prompt data point is found, a cache lookup performs. If cached data is found, the cached response returns to the client.

If the similarity search does not return a similar previous prompt, the LLM model generates content in response to the user prompt and populates the Apigee cache with the response. A feedback loop creates to update the Vector Search index entries in preparation for future requests.

**Note:** This tutorial runs the similarity search against a Vector Search index deployed on a _public_ endpoint, over REST. To run the similarity search against a _private_ Vector Search index over Private Service Connect (gRPC), see [Semantic caching with a private (Private Service Connect) endpoint](https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/using-semantic-caching-policies-psc).

The following sections describe the steps to create and configure the semantic caching policies: 

  1. Configure a service account for the Vector Search index.
  2. Create and deploy a Vector Search index.
  3. Create an API proxy to enable semantic caching.
  4. Configure the semantic caching policies.
  5. Test the semantic caching policies.



## Configure a service account for the Vector Search index

To configure a service account for the Vector Search index, complete the following steps:

  1. Create a service account using the following command: 
         
         gcloud iam service-accounts create SERVICE_ACCOUNT_NAME \
           --description="DESCRIPTION" \
           --display-name="SERVICE_ACCOUNT_DISPLAY_NAME"

Where: 

     * `SERVICE_ACCOUNT_NAME` is the name of the service account.
     * `DESCRIPTION` is a description of the service account.
     * `SERVICE_ACCOUNT_DISPLAY_NAME` is the display name of the service account.

For example: 
    
    gcloud iam service-accounts create **ai-client** \
      --description="**semantic cache client** " \
      --display-name="**ai-client** "

  2. Grant the service account the `AI Platform User` role using the following command: 
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
           --member="serviceAccount:SERVICE_ACCOUNT_NAME@$PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/aiplatform.user"

Replace `SERVICE_ACCOUNT_NAME` with the name of the service account created in the previous step.

  3. Assign the IAM `Service Account User` role to the service account using the following command: 
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
           --member="serviceAccount:SERVICE_ACCOUNT_NAME@$PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/iam.serviceAccountUser"

Replace `SERVICE_ACCOUNT_NAME` with the name of the service account created in the previous step.




## Create and deploy a Vector Search index

To create and deploy a Vector Search index:

  1. Create a Vector Search index that allows streaming updates: 
         
         ACCESS_TOKEN=$(gcloud auth print-access-token) && curl --location --request POST \
           "https://$REGION-aiplatform.googleapis.com/v1/projects/$PROJECT_ID/locations/$REGION/indexes" \
             --header "Authorization: Bearer $ACCESS_TOKEN" \
             --header 'Content-Type: application/json' \
             --data-raw \
             '{
               "displayName": "semantic-cache-index",
               "description": "semantic-cache-index",
               "metadata": {
                 "config": {
                   "dimensions": "768",
                   "approximateNeighborsCount": 150,
                   "distanceMeasureType": "DOT_PRODUCT_DISTANCE",
                   "featureNormType": "NONE",
                   "algorithmConfig": {
                     "treeAhConfig": {
                       "leafNodeEmbeddingCount": "10000",
                       "fractionLeafNodesToSearch": 0.05
                       }
                     },
                   "shardSize": "SHARD_SIZE_MEDIUM"
                   },
                 },
               "indexUpdateMethod": "STREAM_UPDATE"
             }'

The $REGION defines the region where the Vector Search index deploys. We recommend that you use the same region as your Apigee instance. This environment variable was set in a previous step.

When this operation completes, you should see a response similar to the following: 
         
         {
           "name": "projects/976063410430/locations/us-west1/indexes/5695338290484346880/operations/9084564741162008576",
           "metadata": {
             "@type": "type.googleapis.com/google.cloud.aiplatform.v1.CreateIndexOperationMetadata",
             "genericMetadata": {
               "createTime": "2025-04-25T18:45:27.996136Z",
               "updateTime": "2025-04-25T18:45:27.996136Z"
             }
           }
         }

For more information on creating Vector Search indexes, see [Create an index](https://docs.cloud.google.com/vertex-ai/docs/vector-search/create-manage-index).

  2. Create an `IndexEndpoint` using the following command: 
         
         gcloud ai index-endpoints create \
           --display-name=semantic-cache-index-endpoint \
           --public-endpoint-enabled \
           --region=$REGION \
           --project=$PROJECT_ID

This step may take several minutes to complete. When it completes, you should see a response similar to the following: 
         
         Waiting for operation [8278420407862689792]...done.
           Created Vertex AI index endpoint: projects/976063410430/locations/us-west1/indexEndpoints/7953875911424606208.

For more information on creating an `IndexEndpoint`, see [Create an `IndexEndpoint`](https://docs.cloud.google.com/vertex-ai/docs/vector-search/deploy-index-public#create-index-endpoint).

  3. Deploy the index to the endpoint using the following command: 
         
         INDEX_ENDPOINT_ID=$(gcloud ai index-endpoints list \
           --project=$PROJECT_ID \
           --region=$REGION \
           --format="json" | jq -c -r \
           '.[] | select(.displayName=="semantic-cache-index-endpoint") | .name | split("/") | .[5]' \
           ) && INDEX_ID=$(gcloud ai indexes list \
           --project=$PROJECT_ID \
           --region=$REGION \
           --format="json" | jq -c -r \
           '.[] | select(.displayName=="semantic-cache-index") | .name | split("/") | .[5]' \
           ) && gcloud ai index-endpoints deploy-index \
           $INDEX_ENDPOINT_ID \
           --deployed-index-id=semantic_cache \
           --display-name=semantic-cache \
           --index=$INDEX_ID \
           --region=$REGION \
           --project=$PROJECT_ID

**Note:** The command to deploy the index to the endpoint requires `jq`. If this JSON processing utility is not already installed in your development environment, you can install it using the following command: `$ sudo apt install jq`.



Initial deployment of an index to an endpoint can take between 20 and 30 minutes to complete. To check the status of the operation, use the following command: 
    
    
    gcloud ai operations describe OPERATION_ID \
      --project=$PROJECT_ID \
      --region=$REGION

Confirm that the index deployed: 
    
    
    gcloud ai operations describe OPERATION_ID \
      --index-endpoint=$INDEX_ENDPOINT_ID --region=$REGION --project=$PROJECT_ID

The command should return `$ done: true`.

## Create an API proxy to enable semantic caching

In this step, create a new API proxy using the **Proxy with Semantic Cache** template, if you have not done so already.

Before creating the API proxy, set the following environment variable: 
    
    
    export PUBLIC_DOMAIN_NAME=$(gcloud ai index-endpoints describe $INDEX_ENDPOINT_ID --region=$REGION --project=$PROJECT_ID | grep "publicEndpointDomainName" | awk '{print $2}')

To create a proxy for use with semantic caching: 

  1. Go to the **API proxies** page in the Google Cloud console. 

[Go to API proxies](https://console.cloud.google.com/apigee/proxies)

  2. Click the **\+ Create** to open the **Create API proxy** pane.
  3. In the **Proxy template** box, select **Proxy with Semantic Cache**.
  4. Enter the following details: 
     * **Proxy name** : Enter the name of the proxy.
     * **Description** : (Optional) Enter a description of the proxy.
     * **Target (Existing API)** : Enter the URL of the backend service that the proxy calls. This is the LLM model endpoint that generates content. 

For this tutorial, set the **Target (Existing API)** to: 
           
           REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/publishers/google/models/gemini-2.0-flash-001:generateContent

  5. Enter the following **Semantic Cache URLs** : **Note:** You can also add these URLs to the XML configuration in the **Proxy editor** on the **Develop** tab.
     * **Generate Embeddings URL** : This Vertex AI service converts text input into a numerical form for semantic analysis. 

For this tutorial, set this URL to the following: 
           
           REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/publishers/google/models/text-embedding-004:predict

     * **Query Nearest Neighbor URL** : This Vertex AI service searches for similar text input from previous requests in the Vector Search index to avoid reprocessing. 

For this tutorial, set this URL to the following: 
           
           PUBLIC_DOMAIN_NAME/v1/projects/PROJECT_ID/locations/REGION/indexEndpoints/INDEX_ENDPOINT_ID:findNeighbors

The `PUBLIC_DOMAIN_NAME` and `INDEX_ENDPOINT_ID` values were set in an earlier step. To obtain these values, use the following commands: 
           
           echo $PUBLIC_DOMAIN_NAME
             echo $INDEX_ENDPOINT_ID

     * **Upsert index URL** : This Vertex AI service updates the index with new or modified entries. 

For this tutorial, set this URL to the following: 
           
           REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/indexes/INDEX_ID:upsertDatapoints

  6. Click **Next**.
  7. Click **Create**.



The API proxy's XML configuration appears in the **Develop** tab. SemanticCacheLookup and SemanticCachePopulate policies containing default values are already attached to the proxy request and response flows.

**Note** : The SemanticCachePopulate and SemanticCacheLookup policies support the use of URL templating for these elements. If you wish, you can provide a variable in this element to hold the value of the URL, as shown in the following example: 
    
    
    <URL>https://{URL_VARIABLE}</URL>

## Configure the semantic caching policies

View the XML configuration of each policy by clicking on the policy name in the **Detail** view of the API proxy's **Develop** tab. Edit the policy XML directly in the **Code view** of the **Develop** tab.

Edit the policies: 

  * SemanticCacheLookup policy: 
    * Remove the `<UserPromptSource>` element to use the default value.
    * Update the `<DeployedIndexId>` element to use the value `semantic_cache`.
    * Check that the `<DistanceMeasureType>` element matches the measure your index was built with. The index you created above uses `DOT_PRODUCT_DISTANCE`, which is also the default, so no change is needed here. See [DistanceMeasureType](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-lookup-policy#distancemeasuretype).
    * Configure the semantic similarity `<Threshold>` value to determine when two prompts are considered a match. The default is 0.9, but you can adjust this value based on your application's sensitivity. With `DOT_PRODUCT_DISTANCE`, the bigger the number, the more closely prompts have to be related to be considered a cache hit; the other measures reverse that direction. See [Choosing a threshold for your distance measure](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-lookup-policy#choosing-a-threshold). For this tutorial, we recommend setting this value to **0.95**.
    * Click **Save**.
  * SemanticCachePopulate policy: 
    * Set the `<TTLInSeconds>` element to specify the number of seconds until the cache expires, in seconds. The default value is **60s**. Note that Apigee ignores any cache-control headers it receives from the LLM model.
    * Click **Save**.



### Add Google authentication to the API proxy

You must also add Google authentication to the API proxy's target endpoint to enable proxy calls to the target.

To add the Google access token: 

  1. In the **Develop** tab, click **default** under the **Target endpoints** folder. The **Code view** displays the XML configuration of the **< TargetEndpoint>** element.
  2. Edit the XML to add the following configuration under **< HTTPTargetConnection>**: 
         
         <Authentication>
           <GoogleAccessToken>
             <Scopes>
               <Scope>https://www.googleapis.com/auth/cloud-platform</Scope>
             </Scopes>
           </GoogleAccessToken>
         </Authentication>

  3. Click **Save**.



### Deploy the API proxy

To deploy the API proxy:

  1. Click **Deploy** to open the **Deploy API proxy** pane.
  2. The **Revision** field should be set to **1**. If not, click **1** to select it.
  3. In the **Environment** list, select the environment where you want to deploy the proxy. The environment must be an **Intermediate** or **Comprehensive** environment.
  4. Enter the **Service account** you created in an earlier step.
  5. Click **Deploy**.



## Test the semantic caching policies

To test the semantic caching policies: 

  1. Send a request to the proxy using the following command: 
         
         curl https://$RUNTIME_HOSTNAME/PROXY_NAME -H 'Content-Type: application/json' --data '{
           "contents": [
               {
                   "role": "user",
                   "parts": [
                       {
                           "text": "Why is the sky blue?"
                       }
                   ]
               }
           ]
         }'

Replace `PROXY_NAME` with the basepath of the API proxy you deployed in the previous step.

Repeat the API call, substituting the prompt string with the following semantically similar prompt strings: 
     * Why is the sky blue?
     * What makes the sky blue?
     * Why is the sky blue colored?
     * Can you explain why the sky is blue?
     * The sky is blue, why is that?
  2. Compare the response time for each call once a similar prompt has been cached.



To verify that your calls are being served from cache, check the response headers. A `Cached-Content: true` header attaches.

## Best practices

We recommend incorporating the following best practices to your API management program when using the semantic caching policies: 

  * Prevent caching of sensitive data with Model Armor. 

To prevent caching of sensitive data, we recommend using Model Armor for content filtering. Model Armor can flag responses as non-cacheable if it detects sensitive information. For more information, see the [Model Armor overview](https://docs.cloud.google.com/security-command-center/docs/model-armor-overview). 

  * Manage data freshness with Vertex AI data point invalidation and Time-to-Live (TTL). 

We recommend implementing appropriate data point invalidation strategies to ensure that cached responses are up-to-date and reflect the latest information from your backend systems. To learn more, see [ Update and rebuild an active index](https://docs.cloud.google.com/vertex-ai/docs/vector-search/update-rebuild-index). 

You can also adjust the TTL for cached responses based on the data's volatility and frequency of updates. For more information on using TTL in the SemanticCachePopulate policy, see [<TTLInSeconds>](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-populate-policy#ttl).

  * Use predefined caching strategies to ensure the most accurate response data. 

We recommend implementing predefined caching strategies similar to the following: 

    * **Generic AI responses** : Configure a long TTL (for example, one hour) for non-user-specific responses.
    * **User-specific responses** : Do not implement caching, or set a short TTL (for example, five minutes) for responses that contain user-specific information.
    * **Time-sensitive responses** : Configure a short TTL (for example, five minutes) for responses that require real-time or frequent updates.



## Increase quotas for dependent services

If you experience performance bottlenecks resulting from higher queries per second (QPS), you may need to increase the following quotas for dependent services in your Google Cloud project:

  * **Online prediction requests per minute per region** (select by region)
  * **Regional online prediction requests per base model per minute per region** (select by region and the `textembedding-gecko` model)
  * **Matching Engine stream update requests per minute per region** (select by region)



To increase a quota for one of these services:

  1. Go to the **Quota & System Limits** page: 

[Go to Quota & System Limits](https://console.cloud.google.com/iam-admin/quotas)

  2. In the filter bar, enter name of the specific quota you want to increase, along with the **region** and **model** , name if relevant. 

For example, filter by **Regional online prediction requests per base model per minute per region** and **textembedding-gecko** and **us-west1**.

  3. Click the  more_vert  menu for the service you want to increase and then select **Edit quota**.
  4. Enter a new, higher value for the quota.
  5. Click **Done**.
  6. Click **Submit request**.



After submitting your request, the quota increase processes. You can monitor the status on the **Quotas & System Limits** page using the **Increase requests** tab.

## Limitations

The following limitations apply to the semantic caching policies: 

  * The maximum cacheable text size is 256 KB. For more information, see the **Cache value size** on the Apigee [Limits](https://docs.cloud.google.com/apigee/docs/api-platform/reference/limits#cache) page.
  * Apigee ignores any cache-control headers it receives from the LLM model.
  * If the cache is not invalidated properly or if the semantic similarity algorithm is not sufficiently accurate to differentiate between inputs with very similar meanings, the response may return outdated or incorrect information. 
    * For more information on configuring TTL to manage data freshness, see the Best practices section.
    * For more information on configuring the semantic similarity threshold, see the Configure the semantic caching policies section.
    * For more information on tuning the semantic similarity algorithm, see [Filter vector matches](https://docs.cloud.google.com/vertex-ai/docs/vector-search/filtering).
  * The Vector Search feature is not supported in all regions. For a list of supported regions, see the [ Feature availability](https://docs.cloud.google.com/vertex-ai/docs/general/locations#feature-availability) section of the Vertex AI Locations page. If your Apigee organization is in an unsupported region, you will have to create index endpoints in a different region than your Apigee organization.
  * The semantic caching policies are not supported for use with [API proxies using EventFlows for continuous response streaming of server-sent events (SSE)](https://docs.cloud.google.com/apigee/docs/api-platform/develop/server-sent-events).
  * The semantic caching policies use LLM APIs, which can result in higher latencies in the 100s of milliseconds.
  * In Apigee hybrid installations, support for the semantic caching policies is limited to installations on Google Cloud Platform.
  * When the SemanticCacheLookup policy is configured to use a private Vector Search endpoint through Private Service Connect (PSC), the similarity-search call is sent over a direct gRPC connection to the private endpoint and does not go through a configured forward proxy.



## What's next

Learn how to [Get started with Model Armor policies](https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/using-model-armor-policies).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
