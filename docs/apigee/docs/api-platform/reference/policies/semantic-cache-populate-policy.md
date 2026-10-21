---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-populate-policy/
title: SemanticCachePopulate policy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:56:52.206140+00:00
---

# SemanticCachePopulate policy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-populate-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  SemanticCachePopulate policy Stay organized with collections  Save and categorize content based on your preferences. 

[Extensible policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types)

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

**Note:** This policy is supported on Apigee, and on Apigee hybrid **version 1.15.1 and later**.

The SemanticCachePopulate policy is an advanced caching policy designed to optimize the performance of AI workloads, particularly those involving Large Language Models (LLMs).

The policy uses the Vertex AI [Text embeddings API](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/text-embeddings-api) to generate embeddings for text and [Vector Search](https://docs.cloud.google.com/vertex-ai/docs/vector-search/overview) to cache API responses based on semantic similarity, rather than exact matches.

The SemanticCachePopulate policy can reduce response times for repeated queries and optimize costs by reducing call volume to LLMs.

This policy works in conjunction with the [SemanticCacheLookup policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-lookup-policy).

This policy is an _Extensible policy_ and use of this policy might have cost or utilization implications, depending on your Apigee license. For information on policy types and usage implications, see [Policy types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types).

**Note:** If you have configured a forward proxy for your environment, the outbound calls this policy makes to Vertex AI are routed through the proxy. No policy-level configuration is required. This is applicable for Apigee and Apigee Hybrid 1.16.10 and later, and 1.17.0 and later. For more information, see [Configure forward proxying](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-overview#forward-proxying) (Apigee) or [Configure forward proxying for API proxies](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/forward-proxy) (Apigee Hybrid).

## Before you begin

Before you use the SemanticCachePopulate policy, complete the following tasks:

  * Create a Vertex AI project.
  * Create a Vector Search index.
  * Create a Vertex AI endpoint for the index.
  * Create a SemanticCachePopulate policy.



For more information on completing these tasks, see [Get started with Semantic Caching policies](https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/using-semantic-caching-policies).

### Roles and permissions

To get the permissions that you need to apply and use the SemanticCachePopulate policy, ask your administrator to grant you the [AI Platform User ](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.user) (`roles/aiplatform.user`) IAM role on the service account you use to deploy Apigee proxies. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Enable APIs

Enable the Compute Engine, Vertex AI, and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,aiplatform.googleapis.com,storage.googleapis.com)

## `<SemanticCachePopulate>` element

Defines a SemanticCachePopulate policy.

**Default Value** | See **Default Policy** tab, below  
---|---  
**Required?** | Required  
**Type** | Complex object  
**Parent Element** |  N/A   
**Child Elements** |  [`<DisplayName>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-populate-policy#displayname)  
[`<IgnoreUnresolvedVariables>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-populate-policy#ignoreunresolvedvariables)  
[`<SimilaritySearch>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-populate-policy#similaritysearch)  
[`<TTLInSeconds>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-populate-policy#ttl)  
  
  
The `<SemanticCachePopulate>` element uses the following syntax:

### Syntax

The `<SemanticCachePopulate>` element uses the following syntax:
    
    
    <SemanticCachePopulate async="false" continueOnError="false"enabled="true" name="SCP-populate">
      <DisplayName>SCP-populate</DisplayName>
      <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
      <SimilaritySearch>
        <VertexAI>
          <URL>https://{LOCATION}-aiplatform.googleapis.com/v1/projects/{PROJECT_ID}/locations/{LOCATION}/indexes/{INDEX_ID}:upsertDatapoints</URL>
        </VertexAI>
      </SimilaritySearch>
      <TTLInSeconds>{EXPIRATION_TIME_IN_SECONDS}</TTLInSeconds>
    </SemanticCachePopulate>

### Default Policy

The following example shows the default settings when you add a SemanticCachePopulate policy to your API proxy in the Apigee UI:
    
    
    <SemanticCachePopulate async="false" continueOnError="false"enabled="true" name="SCP-populate">
      <DisplayName>SCP-populate</DisplayName>
      <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
      <SimilaritySearch>
        <VertexAI>
          <URL>https://{LOCATION}-aiplatform.googleapis.com/v1/projects/{PROJECT_ID}/locations/{LOCATION}/indexes/{INDEX_ID}:upsertDatapoints</URL>
        </VertexAI>
      </SimilaritySearch>
      <TTLInSeconds>60</TTLInSeconds>
    </SemanticCachePopulate>

When you insert a new SemanticCachePopulate policy in the Apigee UI, the template contains stubs for all possible operations. See below for information on required elements.

This element has the following attributes that are common to all policies:

**Attribute** | **Default** | **Required?** | **Description**  
---|---|---|---  
`name` | N/A | **Required** |  The internal name of the policy. The value of the `name` attribute can contain letters, numbers, spaces, hyphens, underscores, and periods. This value cannot exceed 255 characters. Optionally, use the `<DisplayName>` element to label the policy in the management UI proxy editor with a different, natural-language name.  
`continueOnError` | false | Optional | Set to `false` to return an error when a policy fails. This is expected behavior for most policies. Set to `true` to have flow execution continue even after a policy fails. See also: 

  * [Fault rules are triggered ONLY in an error state (about continueOnError)](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#multiplefaultrulesandexecutionlogic-faultrulesaretriggeredonlyinanerrorstateaboutcontinueonerror)
  * [Handling faults within the current flow](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#continueonerror)

  
`enabled` | true | Optional | Set to `true` to enforce the policy. Set to `false` to _turn off_ the policy. The policy will not be enforced even if it remains attached to a flow.  
`async` not_interested | false | Deprecated | This attribute is deprecated.  
  
The following table provides a high level description of the child elements of [`<SemanticCachePopulate>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-populate-policy#semanticcachepopulate):

Child Element | Required? | Description  
---|---|---  
[`<DisplayName>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-populate-policy#displayname) | Optional | The name of the policy.   
[`<IgnoreUnresolvedVariables>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-populate-policy#ignoreunresolvedvariables) | Optional | Determines whether processing stops when a property set is unresolved.  
[`<SimilaritySearch>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-populate-policy#similaritysearch) | Required | Element containing the information required to update the vector index. For more information, see [Upsert datapoints](https://docs.cloud.google.com/vertex-ai/docs/vector-search/update-rebuild-index#upsert). The expiration time for data points is <TTLInSeconds> from the time of entry.   
[`<TTLInSeconds>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-populate-policy#ttl) | Optional | The time to live (TTL) for the cached responses, in seconds. The default value is `60`.  
  
## Example

This section provides an example using [`<SemanticCachePopulate>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-populate-policy#semanticcachepopulate).
    
    
    <SemanticCachePopulate async="false" continueOnError="false"enabled="true" name="SCP-populate">
      <DisplayName>SCP-populate</DisplayName>
      <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
      <SimilaritySearch>
        <VertexAI>
          <URL>https://{LOCATION}-aiplatform.googleapis.com/v1/projects/{PROJECT_ID}/locations/{LOCATION}/indexes/{INDEX_ID}:upsertDatapoints</URL>
        </VertexAI>
      </SimilaritySearch>
      <TTLInSeconds>60</TTLInSeconds>
    </SemanticCachePopulate>

## Child element reference

This section describes the child elements of [`<SemanticCachePopulate>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-populate-policy#semanticcachepopulate).

### `<DisplayName>`

Use in addition to the `name` attribute to label the policy in the management UI proxy editor with a different, more natural-sounding name.

The `<DisplayName>` element is common to all policies.

**Default Value** | N/A  
---|---  
**Required?** | Optional. If you omit `<DisplayName>`, the value of the policy's `name` attribute is used.  
**Type** | String  
**Parent Element** |  <PolicyElement>  
**Child Elements** |  None   
  
The `<DisplayName>` element uses the following syntax:

### Syntax
    
    
    <_PolicyElement_ >
      **< DisplayName>POLICY_DISPLAY_NAME</DisplayName>**
      ...
    </_PolicyElement_ >

### Example
    
    
    <_PolicyElement_ >
      **< DisplayName>My Validation Policy</DisplayName>**
    </_PolicyElement_ >

The `<DisplayName>` element has no attributes or child elements.

### `<IgnoreUnresolvedVariables>`

Determines whether processing stops when a variable is unresolved. Set to `true` to ignore unresolved variables and continue processing.

`IgnoreUnresolvedVariables` is not applicable when [`<DefaultValue>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-populate-policy#default-policy) is provided.

**Default Value** | False  
---|---  
**Required?** | Optional  
**Type** | Boolean  
**Parent Element** |  [`<SemanticCachePopulate>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-populate-policy#semanticcachepopulate)  
**Child Elements** |  None   
  
### `<SimilaritySearch>`

Element containing the information required to update the vector index.

For more information, see [Upsert datapoints](https://docs.cloud.google.com/vertex-ai/docs/vector-search/update-rebuild-index#upsert).

The expiration time for data points is `<TTLInSeconds>` from the time of entry.

**Default Value** | N/A  
---|---  
**Required?** | Required  
**Type** | String  
**Parent Element** |  [`<SemanticCachePopulate>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-populate-policy#semanticcachepopulate)  
**Child Elements** |  [`<VertexAI>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-populate-policy#vertexai)  
  
  
The `<SimilaritySearch>` element uses the following syntax:
    
    
    <SimilaritySearch>
      <VertexAI>
        <URL>https://{LOCATION}-aiplatform.googleapis.com/v1/projects/{PROJECT_ID}/locations/{LOCATION}/indexes/{INDEX_ID}:upsertDatapoints</URL>
      </VertexAI>
    </SimilaritySearch>

#### <VertexAI> (child of [`<SimilaritySearch>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-populate-policy#similaritysearch))

Contains the <URL> element for Vertex AI-specific attributes.

**Default Value** | N/A  
---|---  
**Required?** | Required  
**Type** | String  
**Parent Element** |  [`<SimilaritySearch>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-populate-policy#similaritysearch)  
**Child Elements** |  [`<URL>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-populate-policy#url)  
  
  
The `VertexAI` element uses the following syntax:
    
    
    <VertexAI>
      <URL>https://{LOCATION}-aiplatform.googleapis.com/v1/projects/{PROJECT_ID}/locations/{LOCATION}/indexes/{INDEX_ID}:upsertDatapoints</URL>
    </VertexAI>

#### <URL> (child of [`<VertexAI>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-populate-policy#vertexai))

The URL used to upsert datapoints in the vector index.

**Default Value** | N/A  
---|---  
**Required?** | Required  
**Type** | String  
**Parent Element** |  [`<VertexAI>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-populate-policy#vertexai)  
**Child Elements** |  None  
  
  
The `URL` element uses the following syntax:
    
    
    <URL>https://{LOCATION}-aiplatform.googleapis.com/v1/projects/{PROJECT_ID}/locations/{LOCATION}/indexes/{INDEX_ID}:upsertDatapoints</URL>

The `URL` element supports the use of URL templating. If you wish, provide a variable in this element to hold the value of the URL, as shown in the following example:
    
    
    <URL>https://{URL_VARIABLE}</URL>

### `<TTLInSeconds>`

Element specifying the time to live (TTL) for the cached responses, in seconds. The default value is 60.

For more information, see [ Update and rebuild an active index](https://docs.cloud.google.com/vertex-ai/docs/vector-search/update-rebuild-index).

**Default Value** | N/A  
---|---  
**Required?** | Optional  
**Type** | String  
**Parent Element** |  [`<SemanticCachePopulate>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-populate-policy#semanticcachepopulate)  
**Child Elements** |  None  
  
  
## Flow variables

Flow variables configure dynamic runtime behavior for policies and flows, based on HTTP headers or message content, or the context available in the Flow. For more information about flow variables, see [Flow variables reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference).

This policy provides the following set of _read-only_ flow variables during execution. You can use these flow variables with the [DataCapture policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/data-capture-policy) to create custom analytics reports. For more information, see [Collecting customer data with the Data Capture policy](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/using-data-capture).

Variable name | Description  
---|---  
`response.content` | Contains the full content of the API response.  
`SemanticCachePopulate.policy_name.upsert_index_request` | Contains the request payload sent to the Vertex AI Vector Search API to update the vector index with new embeddings and metadata.  
`SemanticCachePopulate.policy_name.upsert_index_response` | Contains the response from the Vertex AI Vector Search API, indicating the success or failure of the index update operation.  
  
## Error reference

This section describes the fault codes and error messages that are returned and fault variables that are set by Apigee specific to the `<SemanticCachePopulate>` policy. This information is important to know if you are developing fault rules to handle faults. To learn more, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors) and [Handling faults](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling).

### Runtime errors

These errors can occur when the policy executes.

Fault code | HTTP status | Cause  
---|---|---  
`steps.semanticcachepopulate.VectorSearchUpsertServiceUnavailable ` | `400` |  This error occurs if the Vector Search Upsert Datapoints API is unavailable.  
`steps.semanticcache.populate.VectorSearchUpsertAPIFailed` | `500` |  This error occurs if the Vector Search Upsert Datapoints API service fails.  
`steps.semanticcache.populate.AuthenticationFailure` | `500` |  This error occurs if the service account does not have the required permissions.  
`steps.semanticcache.populate.CalloutError` | `500` | The Vertex AI service call failed.  
`steps.semanticcache.populate.InternalError` | `500` |  This error occurs in the event of an unexpected error within the `<SemanticCachePopulate>` policy.  
  
### Deployment errors

These errors can occur when you deploy a proxy containing this policy.

Error name | Cause  
---|---  
`The SimilaritySearch/VertexAI/PrivateServiceConnect element is not supported in SemanticCachePopulate.` | Occurs if the <PrivateServiceConnect> element is used in <SemanticCachePopulate>.  
`The SimilaritySearch/VertexAI/URL element is required.` | Occurs if the <URL> element in <SimilaritySearch> is empty.  
`The SimilaritySearch URL {url} is invalid.` | Occurs if the <URL> element in <SimilaritySearch> is empty or invalid.  
`The scheme {http-scheme} of SimilaritySearch URL {url} must be one of http, https.` | Occurs if the SimilaritySearch <URL> element's `http` scheme is invalid.  
`The TTLInSeconds element must be >= 0.` | If the value is set to zero or a negative number, then deployment of the API proxy fails.  
  
### Fault variables

These variables are set when this policy triggers an error at runtime. For more information, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors).

Variables | Where | Example  
---|---|---  
`fault.name="FAULT_NAME"` | FAULT_NAME is the name of the fault, as listed in the Runtime errors table above. The fault name is the last part of the fault code. | `fault.name Matches "UnresolvedVariable"`  
`semanticcachepopulate.POLICY_NAME.failed` | POLICY_NAME is the user-specified name of the policy that threw the fault. | `semanticcachepopulate.SC-populate.failed = true`  
  
### Example error response

**Note:** For error handling, the best practice is to trap the `errorcode` part of the error response. Do not rely on the text in the `faultstring`, because it could change.
    
    
    {
    "fault": {
      "faultstring": "SemanticCacheLookup[SC-populate]: unable to resolve variable [variable_name]",
      "detail": {
        "errorcode": "steps.semanticcachepopulate.UnresolvedVariable"
      }
    }
    }

### Example fault rule
    
    
    <FaultRule name="SemanticCacheLookup Faults">
      <Step>
          <Name>SCL-CustomSetVariableErrorResponse</Name>
          <Condition>(fault.name = "SetVariableFailed")</Condition>
      </Step>
      <Condition>(semanticcachelookup.failed = true)</Condition>
    </FaultRule>

## Schemas

Each policy type is defined by an XML schema (`.xsd`). For reference, [policy schemas](https://github.com/apigee/api-platform-samples/tree/master/schemas/policy) are available on GitHub.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
