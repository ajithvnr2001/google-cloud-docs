---
url: https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/troubleshoot-mcp-deployments/
title: Troubleshoot MCP deployments in Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:56:58.061194+00:00
---

# Troubleshoot MCP deployments in Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/troubleshoot-mcp-deployments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Troubleshoot MCP deployments in Apigee Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This page describes how to troubleshoot and resolve issues with the deployment of MCP discovery proxies. You can use this page to understand the asynchronous provisioning lifecycle of MCP deployments, resolve error codes, and verify runtime connectivity.

**Note (Apigee hybrid):** All error status codes, response body semantics, CORS behavior, and API-style constraints on this page apply identically to Apigee hybrid. Apigee hybrid also has cluster-side failure modes that require in-cluster diagnosis with `kubectl`. See Cluster-side diagnosis (Apigee hybrid only) below.

## Understand MCP deployment

The deployment of an MCP Discovery Proxy is an asynchronous, multi-step process that ensures the configuration is fully propagated across the Apigee and Google Cloud infrastructure before proxy deployment is complete.

While these downstream provisioning steps are taking place, the UI shows the proxy in a **Provisioning** status. When the process is complete, the status changes to **Deployed**. This status confirms that all downstream components are fully provisioned and the proxy is ready to handle traffic.

**Note (Apigee hybrid):** In Apigee hybrid, the "downstream components" include the in-cluster `apigee-mcp-server` pods and the `apigee-mcp-server-config` sidecar that pulls the MCP configuration from the Apigee control plane. If your MCP Discovery Proxy does not reach **Deployed** , or the endpoint does not respond, use Cluster-side diagnosis to check the in-cluster components.

## Troubleshooting

The following sections describe errors and known issues you might encounter while using MCP in Apigee.

### Error response status codes for tool calls and metadata

Apigee MCP endpoints return HTTP status codes that follow the [Model Context Protocol (MCP) specification](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#error-handling) and related OAuth standards. Understanding this behavior helps you correctly handle errors in your MCP client or AI agent.

The following table summarizes the status codes returned by Apigee MCP endpoints:

Scenario | HTTP status code | Response body  
---|---|---  
A tool execution fails on `tools/call` (for example, the backend API returns a `4xx` or `5xx` error, such as a validation error or a missing required field). | `200 OK` | A `CallToolResult` with `result.isError` set to `true` and the error details in `content`. This lets the MCP client and the LLM agent read the error and recover (for example, by re-prompting for missing input and retrying) instead of terminating the session.  
The OAuth Protected Resource Metadata (PRM) is not configured or cannot be found at `/.well-known/oauth-protected-resource/mcp`. | `404 Not Found` | Indicates that no protected resource metadata is available at the requested location.  
The access token is missing, invalid, or expired. | `401 Unauthorized` | Includes a `WWW-Authenticate` challenge to drive the OAuth discovery flow.  
The access token has insufficient scope. | `403 Forbidden` | Includes a `WWW-Authenticate` challenge to drive the step-up authorization flow.  
  
#### Example: tool execution error response body

When a tool call fails, Apigee MCP returns `HTTP 200 OK` and reports the failure in the JSON-RPC `result` object, with `isError` set to `true`. The original error returned by your backend is **preserved** : the backend response body is placed verbatim (as a string) in `result.content[].text`. For example, if the backend returns `HTTP 404` with the body `{"error":"User 42 not found"}`, the MCP response is:
    
    
    {
      "jsonrpc": "2.0",
      "id": 1,
      "result": {
        "content": [
          {
            "type": "text",
            "text": "{\"error\":\"User 42 not found\"}"
          }
        ],
        "isError": true
      }
    }

The `id` matches the `id` of your `tools/call` request. If the backend returns no response body, `text` contains a generated summary instead, such as `Operation failed (HTTP 500).`

Your MCP client should inspect `result.isError` (not the HTTP status code) to detect a failed tool call. **If your client code specifically expects a`4xx` or `5xx` HTTP status to signal a tool execution error, it does not detect the error**, because the response is `HTTP 200 OK`. Update such clients to read `result.isError` and the `content` array.

Protocol-level errors (for example, a malformed JSON-RPC request) are distinct from tool execution errors: they continue to be returned in the JSON-RPC `error` object (for example, `{"jsonrpc": "2.0", "error": {"code": -32700, ...}}`) rather than in `result.isError`.

**Recommendation:** Standards-compliant MCP clients handle these status codes through their default logic, so no changes are required. If you previously added a client-side workaround to handle non-standard status codes—for example, parsing a non-`2xx` response body for `tools/call` errors, or treating a `500` response from the PRM endpoint as "metadata not configured"—we recommend removing that workaround. Otherwise, your client might continue to use obsolete handling logic instead of processing the corrected status codes normally.

### CORS policy for browser-based MCP calls

A Cross-Origin Resource Sharing (CORS) policy is necessary when Apigee MCP calls are made directly from a browser (for example, when the MCP inspector uses the "Direct" setting instead of "Via Proxy"). The MCP Discovery Proxy template includes the Apigee [CORS policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/cors-policy) in the Proxy Endpoint **Request PreFlow** of the proxy bundle by default to enable browser-based calls.

If you encounter CORS-related issues when making calls directly from a browser, you may need to adjust the CORS policy settings in the Proxy Endpoint **Request PreFlow** of your MCP Discovery proxy bundle.

### JSON parse error when sending request to MCP endpoint

You may receive an error message similar to the following (or with a different error code and message) when sending a request to your MCP endpoint: 
    
    
    {
      "error": {
        "code": -32700,
        "message": "JSON parse error"
      },
      "id": null,
      "jsonrpc": "2.0"
    }

In that case, we recommend confirming the following information: 

  * You have entered the correct MCP endpoint URL.
  * Your request is formatted correctly.
  * You are accessing a supported method.
  * You enabled and configured your MCP Discovery Proxy in a [ supported region](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/apigee-mcp-overview#limitations). For a list of regions that may have capacity limits, see deployment failures.



### Deployment failures

If deployment of your MCP Discovery Proxy fails with a **Failed** status in the UI, check the error message for more details. Common failures include:

  * **Networking configuration failed** or **Unsupported Schema in OAS** : These errors typically indicate a problem with your OpenAPI specification. Ensure your specification is valid and uses a [supported version](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/apigee-mcp-overview#limitations).
  * **Region capacity limits (Apigee only)** : If you see an error related to load balancer provisioning failure, or the provisioning status never changes to **Deployed** , it might be due to temporary infrastructure capacity limits in one of the following regions: 
    * `asia-east2`
    * `asia-northeast3`
    * `asia-southeast2`
    * `australia-southeast1`
    * `europe-central2`
    * `europe-west12`
    * `europe-west9`
    * `me-central2`
    * `us-central2`

To resolve the error, try deploying the proxy to an environment in a different region. This failure mode does not apply to Apigee hybrid, where the runtime infrastructure is your own cluster.

  * **MCP not enabled in cluster (Apigee hybrid only)** : If your MCP proxy deployment stays in **Provisioning** status indefinitely and never reaches **Deployed** , verify that MCP is enabled in your cluster. See Cluster-side diagnosis below.



### Cluster-side diagnosis (Apigee hybrid only)

Because the Apigee hybrid MCP data plane runs inside your own Kubernetes cluster, in-cluster failure modes are diagnosed with `kubectl` against the cluster. Work through the following diagnostic checklist in order.

**Placeholder conventions in this section.** Every `kubectl` and `helm` command below uses the following placeholders. Replace them with values from your installation: 

  * `APIGEE_NAMESPACE` — the Kubernetes namespace where Apigee hybrid is installed (default `apigee`). Look up the `namespace` field in your `overrides.yaml`.
  * `APIGEE_ORG_RELEASE_NAME` — the Helm release name for the `apigee-org` chart in your cluster (customer-chosen at install time). Confirm with `helm list -n APIGEE_NAMESPACE | grep apigee-org`. The **NAME** column of the matching row is the value to use, for example: 
        
        NAME                        NAMESPACE  REVISION  ...  CHART
        my-hybrid-org               apigee     3         ...  apigee-org-1.17.0

Here, `APIGEE_ORG_RELEASE_NAME` is `my-hybrid-org`.
  * `ORG_CR_SUFFIX` — the suffix that the Apigee operator appends to MCP resource names. The suffix is a truncated form of your Apigee organization name followed by a short hash (for example, `my-org-abc12de`). Look up the exact suffix from the `ApigeeOrganization` custom resource: `kubectl get apigeeorganization -n APIGEE_NAMESPACE -o jsonpath='{.items[0].metadata.name}'`. The trailing token after `apigee-organization-` is the suffix.



#### Step 1: Verify MCP is enabled in the cluster

MCP is deployed as an `ApigeeDeployment` custom resource (managed by the Apigee operator), not as a vanilla Kubernetes `Deployment`. Check for the MCP `ApigeeDeployment`:
    
    
    kubectl -n APIGEE_NAMESPACE get apigeedeployment -l app=apigee-mcp-server

Expected output (resource names include an organization-derived suffix, shown here as `ORG_CR_SUFFIX`):
    
    
    NAME                                     STATE     NESTEDSTATE   AGE
    apigee-mcp-server-default-ORG_CR_SUFFIX       running                 1h

If the command returns `No resources found in APIGEE_NAMESPACE namespace.`, MCP is not enabled. Return to [Enable MCP in Apigee hybrid](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/enable-mcp) and verify that `enableMcpServer: true` is set as a top-level key in your `overrides.yaml`, and that you upgraded the `apigee-operator` Helm release before the `apigee-org` release. See [Step 3](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/enable-mcp#step-3-helm-upgrade-operator) and [Step 4](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/enable-mcp#step-4-helm-upgrade-org) of the enable procedure for the correct `helm` commands.

**Caution:** Do not use `kubectl get deploy -l app=apigee-mcp-server`. That command returns no results because MCP is not a vanilla Kubernetes `Deployment`; it is an `ApigeeDeployment` custom resource. Use the `kubectl get apigeedeployment` command shown above. 

#### Step 2: Verify MCP pods are running
    
    
    kubectl -n APIGEE_NAMESPACE get pods -l app=apigee-mcp-server

Expected output (pod suffixes will differ):
    
    
    NAME                                                              READY   STATUS    RESTARTS   AGE
    apigee-mcp-server-default-ORG_CR_SUFFIX-1170-abcd1234   2/2     Running   0          1h
    apigee-mcp-server-default-ORG_CR_SUFFIX-1170-efgh5678   2/2     Running   0          1h

Pod names follow the template `apigee-mcp-server-default-ORG_CR_SUFFIX-REV-POD_HASH`, where REV is the four-digit hybrid release revision (for example, `1170` for hybrid 1.17.0) and POD_HASH is an eight-character alphanumeric suffix that differs for each pod.

Every pod must show `2/2` in the `READY` column and `Running` in the `STATUS` column. If pods are not `Running`, `kubectl -n APIGEE_NAMESPACE describe pod POD_NAME` shows the reason. Common causes are image-pull failures (verify egress from your cluster to the image registry configured in your `overrides.yaml`) and insufficient CPU or memory headroom (raise `mcpServer.resources.requests` in `overrides.yaml`).

#### Step 3: Check the sidecar configuration pull status

The `apigee-mcp-server-config` sidecar container in each MCP pod periodically pulls MCP configuration from the Apigee control plane. Each pull retrieves the current configuration reference from `apigee.googleapis.com`, then fetches the referenced configuration bundle from Cloud Storage. The MCP data plane starts serving MCP tool traffic on `https://mcp.apigee.internal/mcp` once a pull completes successfully with a valid configuration.

Before that first successful pull with a valid configuration (either because no MCP Discovery Proxy has been deployed for your organization yet, or because the sidecar cannot reach the control plane), the MCP pods stay `Ready` but requests to `https://mcp.apigee.internal/mcp` fail with **connection refused**.

Inspect the sidecar logs to determine which case you are in:
    
    
    kubectl -n APIGEE_NAMESPACE logs -l app=apigee-mcp-server -c apigee-mcp-server-config --tail=100

  * **Repeating`info` line indicating no MCP configuration from the control plane:**
        
        {"level":"info","ts":1787582542.68,"caller":"mcpsidecar/sidecar.go:397","msg":"mcpsidecar: no MCP config from CP yet; skipping tick, pod stays Ready via seed","org":"YOUR_ORG","mcp_server_id":"default"}

The Apigee control plane returned a successful response but no MCP Discovery Proxy has been deployed for your organization yet. This is the expected steady state during onboarding. To transition the MCP data plane into serving state, deploy an MCP Discovery Proxy per the [MCP quickstart](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/apigee-mcp-quickstart). 
  * **`error` line with a `consecutive_failures` counter:**
        
        {"level":"error","ts":1787613247.74,"caller":"mcpsidecar/sidecar.go:...","msg":"mcpsidecar: ...","org":"YOUR_ORG","mcp_server_id":"default","consecutive_failures":185,"error":"<wrapped error text>"}

Sidecar logs are structured JSON. When you see `"level":"error"` with a rising `consecutive_failures` counter, the sidecar could not complete a configuration pull. The sidecar retries automatically with backoff and resets the counter to 0 on the next successful pull. 

Common root causes to check when this counter keeps rising:

    * The `apigee-watcher` Google Cloud service account is not in the `watcher_identities` list on your Apigee organization's `controlPlaneAccess` resource. See [Step 2: Grant the watcher identity access to the MCP configuration on the control plane](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/enable-mcp#step-2-grant-watcher-cp-access) in the enable procedure to add the grant and verify it landed.
    * Egress from your cluster to `apigee.googleapis.com` or `storage.googleapis.com` is blocked. Both endpoints must be reachable from the MCP pods (see [Outbound network requirements](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/enable-mcp#outbound-network) in the enable procedure).
    * The `apigee-watcher` service account cannot obtain Google Cloud access tokens from this cluster. If existing Apigee hybrid components in the same namespace are also reporting authentication failures, address the shared authentication problem first.
    * A transient Apigee control-plane or Cloud Storage error. If the counter keeps rising for an extended period after ruling out the causes above, contact [Apigee Support](https://cloud.google.com/apigee/docs/api-platform/contact-support).



#### Step 4: Verify Message Processor hostAliases were injected

When you enable MCP, the Apigee operator injects one `hostAliases` entry into the Message Processor (MP) pod spec. The entry contains one IP (the MCP Service ClusterIP) and two hostnames: `mcp.apigee.internal` and the lowercased `ORG_NAME.mcp.apigee.internal`. Verify the injection succeeded:
    
    
    kubectl -n APIGEE_NAMESPACE get pods -l app=apigee-runtime \
      -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.spec.hostAliases}{"\n"}{end}'

Every listed MP pod must have a `hostAliases` entry containing both `mcp.apigee.internal` and the lowercased `ORG_NAME.mcp.apigee.internal` pointing at the MCP Service ClusterIP. Any MP pod that shows an empty or missing entry was created before MCP was enabled. Delete the affected MP pod so the `ApigeeDeployment` controller recreates it from the current pod spec (which includes the injected `hostAliases` entry):
    
    
    kubectl -n APIGEE_NAMESPACE delete pod -l app=apigee-runtime

**Caution:** Message Processor is deployed as an `ApigeeDeployment` custom resource, not a vanilla Kubernetes `Deployment`. Do not use `kubectl rollout restart deploy -l app=apigee-runtime`; the command silently does nothing on an `ApigeeDeployment`. Use `kubectl delete pod` as shown above so the `ApigeeDeployment` controller recreates the pod from the current pod spec. 

#### Step 5: End-to-end verification

For an end-to-end test that sends an actual MCP `initialize` request through the MCP data plane, deploy an MCP Discovery Proxy and follow the [MCP quickstart](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/apigee-mcp-quickstart). Before an MCP Discovery Proxy is deployed for your organization, requests to `https://mcp.apigee.internal/mcp` fail with **connection refused** regardless of whether Message Processor can reach the MCP pods (see Step 3).

#### Support cases

If you open a support case that involves the Apigee hybrid MCP data plane, attach the following output to accelerate diagnosis:

  * `kubectl -n APIGEE_NAMESPACE logs -l app=apigee-mcp-server --all-containers --tail=1000`
  * `kubectl -n APIGEE_NAMESPACE describe pod -l app=apigee-mcp-server`
  * `kubectl -n APIGEE_NAMESPACE get pods -l app=apigee-mcp-server -o wide` and `kubectl -n APIGEE_NAMESPACE get svc -l app=apigee-mcp-server`.
  * Recent `overrides.yaml` and `helm history APIGEE_ORG_RELEASE_NAME -n APIGEE_NAMESPACE` output (where `APIGEE_ORG_RELEASE_NAME` is the Helm release name for the `apigee-org` chart; find it with `helm list -n APIGEE_NAMESPACE | grep apigee-org`). Before sharing `overrides.yaml`, redact secret material, including: 
    * Any inline service account keys under `gcp.workloadIdentity`, `envs[].serviceAccountPaths`, or `mcpServer.serviceAccountPath`.
    * Any TLS certificates or private keys under `virtualhosts`.
    * The `cassandra.auth` password fields.
    * Any inline credentials that your overrides pass to the operator.
  * The full `curl` command and response reproducing the issue.



### Cannot change API style to MCP in API Hub

If an API resource with existing API operations is already present in Apigee API hub, you cannot change the **API style** attribute for that resource to **MCP**. To register an API with Apigee API hub as an MCP API, you must select the **MCP** style when first registering the API, or ensure no operations are present on the API resource before changing the style to MCP.

If you encounter any other issues, see [Using debug](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace) for detailed information on using the Debug tool in the Google Cloud console to analyze requests and responses to and from your MCP Discovery Proxy.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
