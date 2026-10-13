---
url: https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/enable-mcp/
title: Enable Model Context Protocol (MCP) in Apigee hybrid \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:56:55.768860+00:00
---

# Enable Model Context Protocol (MCP) in Apigee hybrid  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/enable-mcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Enable Model Context Protocol (MCP) in Apigee hybrid Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This page describes how to enable Model Context Protocol (MCP) in an existing Apigee hybrid cluster running version `1.17.0` or later. After you complete this procedure, your cluster runs a new in-cluster MCP data plane and your Message Processor is ready to route MCP tool calls to it. You can then deploy your first MCP Discovery Proxy by following the shared [MCP quickstart](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/apigee-mcp-quickstart).

For MCP concepts, architecture, and feature details shared between Apigee and Apigee hybrid, see the [MCP in Apigee overview](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/apigee-mcp-overview).

## What this procedure does

Enabling MCP on a Apigee hybrid cluster makes the following changes:

  1. **Grants the`apigee-watcher` identity access to MCP configuration on the Apigee control plane.** You add the `apigee-watcher` service account to the `watcher_identities` list on your Apigee organization's `controlPlaneAccess` resource so the MCP sidecar can pull MCP configuration bundles from the Apigee control plane. This is a control-plane change, scoped to the Apigee organization, and is a one-time step per organization regardless of how many clusters serve that organization.
  2. **Adds a new in-cluster MCP data plane.** A new set of MCP pods is created in the same Kubernetes namespace where Apigee hybrid is installed (default `apigee`), along with the supporting Kubernetes resources (Service, Horizontal Pod Autoscaler, and RBAC) needed to run them. MCP tool calls are handled by these pods.
  3. **Configures your Message Processor to reach the MCP data plane.** The Apigee operator updates your Message Processor pod spec so that MP routes MCP tool calls to the new in-cluster MCP data plane. Applying this change triggers a staged canary release of Message Processor (managed by the `ApigeeDeployment` controller); the previous pod continues to serve traffic until the new pod is `Ready`. The release fires only on the enable and disable transitions, not on ongoing MCP activity or steady-state MCP traffic. Run this procedure in an approved maintenance window and wait for the release to complete before proceeding.

**Placeholder conventions on this page.** Every `kubectl` and `helm` command on this page uses the following placeholders. Replace them with values from your installation: 

  * `APIGEE_NAMESPACE` — the Kubernetes namespace where Apigee hybrid is installed (default `apigee`). Look up the `namespace` field in your `overrides.yaml`.
  * `APIGEE_OPERATOR_RELEASE_NAME` — the Helm release name for the `apigee-operator` chart in your cluster (typical: `operator` or `apigee-operator`; but customer-chosen). Confirm with `helm list -n APIGEE_NAMESPACE | grep apigee-operator`.
  * `APIGEE_ORG_RELEASE_NAME` — the Helm release name for the `apigee-org` chart in your cluster (typical: your organization name or `apigee-org`; but customer-chosen). Confirm with `helm list -n APIGEE_NAMESPACE | grep apigee-org`.



## Step 1: Edit `overrides.yaml`

Open the `overrides.yaml` file you use for your Apigee hybrid Helm charts. At the top level of the file, add:
    
    
    enableMcpServer: true

This is the minimum configuration required to enable MCP. It uses the built-in defaults from the `apigee-org` chart: two MCP data plane replicas that auto-scale to ten at 70% CPU utilization, with resource requests of 500m CPU and 512Mi memory and limits of 2000m CPU and 1Gi memory on the MCP data plane container. To customize replica counts, resource requests, or the MCP service account, see Reference: MCP fields in overrides.yaml later on this page.

Complete examples of a merged `overrides.yaml` follow, one for each authentication style. Use the example that matches how your existing base installation is configured; the MCP-specific lines are highlighted with comments and are the same in all three variants.

**Recommendation: Reuse the`apigee-watcher` identity.** You do not need to create a dedicated Google Cloud service account for the MCP data plane. When you leave `mcpServer.gsa` and `mcpServer.serviceAccountPath` unset (as the following two variant examples do), MCP uses the identity that `apigee-watcher` already uses in your cluster: 

  * **Workload Identity:** MCP uses `watcher.gsa`. If `watcher.gsa` is unset, MCP uses `gcp.workloadIdentity.gsa`.
  * **File-based service account keys:** MCP uses `watcher.serviceAccountPath`. MCP does not use `envs[].serviceAccountPaths.runtime` or any other key file. If you set neither `mcpServer.serviceAccountPath` nor `watcher.serviceAccountPath`, `helm upgrade` fails with the error `mcpServer.serviceAccountPath or watcher.serviceAccountPath is required!!`. For Vault and Kubernetes secrets, see Other identity mechanisms.

The `apigee-watcher` identity already holds the `roles/apigee.runtimeAgent` role and the read permissions the MCP sidecar needs, so reusing it works without additional IAM configuration and keeps your Identity and Access Management (IAM) footprint minimal. Set the `mcpServer.gsa` or `mcpServer.serviceAccountPath` override only if your organization requires per-component identity separation for audit reasons.

Pick the tab that matches how your base installation authenticates Apigee components to Google Cloud. The selection applies to every variant-scoped code block on this page.

### Workload Identity (GKE)

Use this variant if your base installation authenticates Apigee components to Google Cloud through GKE Workload Identity (no service account key files on disk).
    
    
    instanceID: "my-hybrid-instance"
    namespace: APIGEE_NAMESPACE
    gcp:
      region: us-central1
      projectID: my-hybrid-project
      workloadIdentity:
        enabled: true
        gsa: apigee-non-prod@my-hybrid-project.iam.gserviceaccount.com
    k8sCluster:
      name: my-cluster
      region: us-central1
    org: my-org
    envs:
    - name: my-env
    
    # ---- MCP: minimum required -------------------------------------------------
    enableMcpServer: true
    
    # ---- MCP: optional customization (all fields default when omitted) ---------
    # mcpServer:
    #   replicaCountMin: 2
    #   replicaCountMax: 10
    #   targetCPUUtilizationPercentage: 70
    #   resources:
    #     requests: { cpu: 500m,  memory: 512Mi }
    #     limits:   { cpu: 2000m, memory: 1Gi }
    #   sidecar:
    #     resources:
    #       requests: { cpu: 200m, memory: 128Mi }
    #       limits:   { cpu: 500m, memory: 512Mi }
    #   annotations: {}
    # ----------------------------------------------------------------------------

### File-based service account keys

Use this variant if your base installation authenticates Apigee components to Google Cloud through service account key files that you distribute to each cluster.
    
    
    instanceID: "my-hybrid-instance"
    namespace: APIGEE_NAMESPACE
    gcp:
      region: us-central1
      projectID: my-hybrid-project
    k8sCluster:
      name: my-cluster
      region: us-central1
    org: my-org
    guardrails:
      serviceAccountPath: ./service-accounts/apigee-non-prod.json
    mart:
      serviceAccountPath: ./service-accounts/apigee-non-prod.json
    connectAgent:
      serviceAccountPath: ./service-accounts/apigee-non-prod.json
    watcher:
      serviceAccountPath: ./service-accounts/apigee-non-prod.json  # MCP also uses this key file
    envs:
    - name: my-env
      serviceAccountPaths:
        synchronizer: ./service-accounts/apigee-non-prod.json
        runtime:      ./service-accounts/apigee-non-prod.json
    
    # ---- MCP: minimum required -------------------------------------------------
    enableMcpServer: true
    
    # ---- MCP: optional customization (all fields default when omitted) ---------
    # mcpServer:
    #   replicaCountMin: 2
    #   replicaCountMax: 10
    #   targetCPUUtilizationPercentage: 70
    #   resources:
    #     requests: { cpu: 500m,  memory: 512Mi }
    #     limits:   { cpu: 2000m, memory: 1Gi }
    #   sidecar:
    #     resources:
    #       requests: { cpu: 200m, memory: 128Mi }
    #       limits:   { cpu: 500m, memory: 512Mi }
    #   annotations: {}
    # ----------------------------------------------------------------------------

### Workload Identity Federation (AKS/EKS)

Use this variant if your base installation is on AKS or EKS and authenticates to Google Cloud through [Workload Identity Federation](https://docs.cloud.google.com/apigee/docs/hybrid/latest/enable-workload-identity-federation). MCP uses the credential configuration file that `apigee-watcher` already uses, from `watcher.serviceAccountPath`, so you do not add any MCP-specific identity configuration. If you store the credential configuration in a Kubernetes secret instead, see Other identity mechanisms.

Add the MCP top-level key to your existing WIF `overrides.yaml`:
    
    
    # ---- MCP: minimum required -------------------------------------------------
    enableMcpServer: true
    
    # ---- MCP: optional customization (all fields default when omitted) ---------
    # mcpServer:
    #   replicaCountMin: 2
    #   replicaCountMax: 10
    #   targetCPUUtilizationPercentage: 70
    #   resources:
    #     requests: { cpu: 500m,  memory: 512Mi }
    #     limits:   { cpu: 2000m, memory: 1Gi }
    #   sidecar:
    #     resources:
    #       requests: { cpu: 200m, memory: 128Mi }
    #       limits:   { cpu: 500m, memory: 512Mi }
    #   annotations: {}
    # ----------------------------------------------------------------------------

Leave `mcpServer.gsa` and `mcpServer.serviceAccountPath` unset. The MCP sidecar uses the same credential configuration file as `apigee-watcher`, from `watcher.serviceAccountPath`.

**Note:** `enableMcpServer` is a top-level key. When adding it to an existing `overrides.yaml`, use the same indentation level as `instanceID`, `gcp`, and `org` — do not nest it under `mcpServer` or any other stanza.**Other identity mechanisms.** If your base installation stores service account credentials in HashiCorp Vault through the CSI driver (with `serviceAccountSecretProviderClass`), MCP uses that same mechanism automatically—you do not add any MCP-specific configuration. If your base installation stores service account keys in Kubernetes secrets (with `watcher.serviceAccountRef` and the `serviceAccountRef` property of each other component), MCP does not use the `apigee-watcher` secret. Set `mcpServer.serviceAccountRef` to the same secret name as `watcher.serviceAccountRef`. If you do not, `helm upgrade` fails with the error `mcpServer.serviceAccountPath or watcher.serviceAccountPath is required!!`. See [Storing service account keys in a Kubernetes secret](https://docs.cloud.google.com/apigee/docs/hybrid/latest/storing-sa-keys-in-k8s-secrets) and [Storing service account secrets in HashiCorp Vault](https://docs.cloud.google.com/apigee/docs/hybrid/latest/storing-sa-keys-in-vault) for setup of the base mechanism.

## Step 2: Grant the watcher identity access to the MCP configuration on the control plane

The MCP sidecar fetches its configuration bundle from the Apigee control plane using the `apigee-watcher` component's Google Cloud service account (the identity you selected in Step 1). Before the MCP pods start, add that service account to the `watcher_identities` list on your Apigee organization's `controlPlaneAccess` resource. Without this grant, the MCP sidecar's calls to `apigee.googleapis.com` to retrieve the MCP configuration reference return `404 Not Found` and the MCP data plane never becomes ready to serve tool traffic.

This is a one-time-per-organization step (it is not per-cluster). Skip this step if you have already granted access for a previous cluster in the same Apigee organization.

**Note:** This grant is separate from the `synchronizer_identities` and `analytics_publisher_identities` grants you configured for other Apigee hybrid components; the MCP sidecar uses a distinct identity slot and does not inherit permissions from those grants. For background on the underlying API, see [Enable synchronizer access](https://docs.cloud.google.com/apigee/docs/hybrid/latest/install-enable-control-plane-access) (same API, different identity slot).

  1. Set the shell variables you use for the API call. Reuse the values from your installation: 
         
         export ORG_NAME=YOUR_ORG_NAME
         export PROJECT_ID=YOUR_GCP_PROJECT_ID
         export WATCHER_SA=apigee-watcher@${PROJECT_ID}.iam.gserviceaccount.com
         export TOKEN=$(gcloud auth print-access-token)

Where:

     * `YOUR_ORG_NAME` is the name of your Apigee hybrid organization.
     * `YOUR_GCP_PROJECT_ID` is the Google Cloud project that hosts your Apigee hybrid organization.
     * `WATCHER_SA` is the email address of the `apigee-watcher` service account. If you overrode `watcher.gsa` in `overrides.yaml`, use that value instead of the default `apigee-watcher@${PROJECT_ID}.iam.gserviceaccount.com`.
  2. Call the [updateControlPlaneAccess](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/updateControlPlaneAccess) API to add the watcher service account to the `watcher_identities` list: 

### No data residency
         
         curl -X PATCH -H "Authorization: Bearer $TOKEN" \
           -H "Content-Type: application/json" \
           "https://apigee.googleapis.com/v1/organizations/${ORG_NAME}/controlPlaneAccess?update_mask=watcher_identities" \
           -d "{\"watcher_identities\": [\"serviceAccount:${WATCHER_SA}\"]}"
         

### Data residency
         
         curl -X PATCH -H "Authorization: Bearer $TOKEN" \
           -H "Content-Type: application/json" \
           "https://${CONTROL_PLANE_LOCATION}-apigee.googleapis.com/v1/organizations/${ORG_NAME}/controlPlaneAccess?update_mask=watcher_identities" \
           -d "{\"watcher_identities\": [\"serviceAccount:${WATCHER_SA}\"]}"
         

Where `CONTROL_PLANE_LOCATION` is the location for your control plane data if your Apigee hybrid installation uses [data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts). For the list of available locations, see [Available Apigee API control plane regions](https://docs.cloud.google.com/apigee/docs/locations#available-apigee-api-control-plane-regions).

The call returns a long-running operation. Wait for it to complete before running the verification step below.

  3. Verify the grant landed. Call [getControlPlaneAccess](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/getControlPlaneAccess) and confirm the watcher service account appears in the `watcherIdentities` field of the response: 

### No data residency
         
         curl -X GET -H "Authorization: Bearer $TOKEN" \
           -H "Content-Type: application/json" \
           "https://apigee.googleapis.com/v1/organizations/${ORG_NAME}/controlPlaneAccess"
         

### Data residency
         
         curl -X GET -H "Authorization: Bearer $TOKEN" \
           -H "Content-Type: application/json" \
           "https://${CONTROL_PLANE_LOCATION}-apigee.googleapis.com/v1/organizations/${ORG_NAME}/controlPlaneAccess"
         

The response should include a `watcherIdentities` array containing your watcher service account. For example:
         
         {
           "synchronizerIdentities": [ ... ],
           "analyticsPublisherIdentities": [ ... ],
           "watcherIdentities": [
             "serviceAccount:apigee-watcher@YOUR_GCP_PROJECT_ID.iam.gserviceaccount.com"
           ]
         }

If `watcherIdentities` is absent from the response or does not contain your watcher service account, re-run the PATCH command and check the operation status for errors before proceeding.




## Step 3: Upgrade the `apigee-operator` chart

**Note:** Before you run `helm upgrade`, make sure your local `apigee-operator/` and `apigee-org/` chart directories are on version `1.17.0` or later. If your local charts are still on `1.16.x` or lower, this step reports success but does not install the MCP resource schema, and the rest of the procedure silently no-ops. See the [Apigee hybrid upgrade guide](https://docs.cloud.google.com/apigee/docs/hybrid/latest/upgrade) for how to fetch the correct chart revision.

Upgrade the operator chart **first**. The operator chart owns the schema for the new MCP resources; the organization chart references them. Upgrading in the wrong order results in a successful `helm upgrade` that creates no MCP pods.
    
    
    helm upgrade APIGEE_OPERATOR_RELEASE_NAME apigee-operator/ \
      --namespace APIGEE_NAMESPACE \
      --atomic \
      -f overrides.yaml

The command completes in under a minute. Confirm that the operator Deployment is fully rolled out with the new image (the `apigee-controller-manager` `Deployment` is a vanilla Kubernetes resource, not an `ApigeeDeployment`, so `kubectl rollout status deploy` is the correct command here):
    
    
    kubectl rollout status deploy -n APIGEE_NAMESPACE apigee-controller-manager --timeout=2m

Expected output:
    
    
    deployment "apigee-controller-manager" successfully rolled out

## Step 4: Upgrade the `apigee-org` chart
    
    
    helm upgrade APIGEE_ORG_RELEASE_NAME apigee-org/ \
      --namespace APIGEE_NAMESPACE \
      --atomic \
      -f overrides.yaml

Two reconciliation loops now run in parallel:

  * The Apigee operator creates the MCP Deployment, Service, HPA, ServiceAccount, Role, and RoleBinding. MCP pods come up two at a time (subject to Kubernetes scheduling); the sidecar container in each pod performs its first configuration fetch from the Apigee control plane shortly after startup.
  * The Apigee operator injects the `hostAliases` entry into the Message Processor pod spec, which triggers a release of the `apigee-runtime` `ApigeeDeployment`.



## Step 5: Verify the installation

### Verify the MCP data plane is running

Inspect the four MCP-related resources the operator created. Resource names include an organization-derived suffix; the samples that follow use `ORG_CR_SUFFIX` as the placeholder for that suffix, and pod suffixes and the Service ClusterIP will differ in your environment.

**MCP pods** (two by default; auto-scale to ten under load):
    
    
    kubectl get pod -n APIGEE_NAMESPACE -l app=apigee-mcp-server
    
    
    NAME                                                READY   STATUS    RESTARTS   AGE
    apigee-mcp-server-default-ORG_CR_SUFFIX-6d4c8-abc12   2/2     Running   0          2m
    apigee-mcp-server-default-ORG_CR_SUFFIX-6d4c8-def34   2/2     Running   0          2m

Every pod must show `2/2` in the `READY` column. The two containers in each pod are:

  * `apigee-mcp-server` — the MCP data plane container that MP pods connect to.
  * `apigee-mcp-server-config` — the configuration sidecar (a mode of the `apigee-watcher` binary) that fetches configuration bundles from the Apigee control plane and writes them to a shared volume that the MCP data plane container reads.



**MCP`ApigeeDeployment`** (a Kubernetes custom resource, not a vanilla `Deployment`):
    
    
    kubectl get apigeedeployment -n APIGEE_NAMESPACE -l app=apigee-mcp-server
    
    
    NAME                              STATE     NESTEDSTATE   AGE
    apigee-mcp-server-default-ORG_CR_SUFFIX   running                 2m

Expected state is `running`. Also verify the underlying pod is `2/2 Running`:
    
    
    kubectl get pod -n APIGEE_NAMESPACE -l app=apigee-mcp-server
    
    
    NAME                                    READY   STATUS    RESTARTS   AGE
    apigee-mcp-server-default-ORG_CR_SUFFIX-REV-POD_HASH   2/2     Running   0          2m

**MCP Service** :
    
    
    kubectl get svc -n APIGEE_NAMESPACE -l app=apigee-mcp-server
    
    
    NAME                              TYPE        CLUSTER-IP    EXTERNAL-IP   PORT(S)                              AGE
    apigee-mcp-server-default-ORG_CR_SUFFIX   ClusterIP   10.96.42.17   <none>        80/TCP,443/TCP,15021/TCP,15000/TCP   2m

**Note:** The MCP Service manifest lists four ports: 

  * `443/TCP` is the port used by MCP request traffic from Message Processor. Every MCP tool call to the in-cluster MCP data plane arrives on this port over TLS.
  * `15021/TCP` exposes the MCP data plane readiness endpoint at `/healthz/ready` over plain HTTP. Kubelet uses this endpoint (reached directly on each pod IP) to decide whether an MCP pod is `Ready`.
  * `80/TCP` and `15000/TCP` are also declared on the Service manifest. In `1.17.0`, no in-cluster MCP client should send traffic to these ports through the Service; MCP tool traffic uses `443/TCP` only.



**MCP HorizontalPodAutoscaler** :
    
    
    kubectl get hpa -n APIGEE_NAMESPACE | grep apigee-mcp-server

Confirm that `MINPODS` matches `mcpServer.replicaCountMin` from your `overrides.yaml` (default `2`) and `MAXPODS` matches `mcpServer.replicaCountMax` (default `10`). The `TARGETS`, `REPLICAS`, and `AGE` columns depend on live metrics and cluster state.

### Verify Message Processor pods received the `hostAliases` entry

Every MP pod must show the injected entry — if even one pod is missing it, that pod cannot route MCP tool calls. List all MP pods and their `hostAliases`:
    
    
    kubectl get pods -n APIGEE_NAMESPACE -l app=apigee-runtime \
      -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.spec.hostAliases}{"\n"}{end}'

Expected output: every MP pod lists a `hostAliases` array containing one entry with two hostnames pointing at the MCP Service ClusterIP from the previous step (the second hostname uses your lowercased org name). Message Processor pod names follow the template `apigee-runtime-TRUNCATED_ORG-ENV_GROUP_HASH-REV-POD_HASH`, where TRUNCATED_ORG is your organization name (truncated to fit the Kubernetes 63-character name limit if your org name is long), ENV_GROUP_HASH is a per-environment deployment-group hash, REV is the current release revision number (four digits, for example `1170`), and POD_HASH is a per-pod random suffix. For example:
    
    
    apigee-runtime-myorg-env1-abc12-1170-def34   [map[hostnames:[mcp.apigee.internal myorg.mcp.apigee.internal] ip:10.96.42.17]]
    apigee-runtime-myorg-env1-abc12-1170-ghi56   [map[hostnames:[mcp.apigee.internal myorg.mcp.apigee.internal] ip:10.96.42.17]]

If any pod shows an empty `hostAliases` value, the Message Processor `ApigeeDeployment` did not fully pick up the updated pod spec. Force a fresh staged canary release by deleting the current Message Processor pods; the `ApigeeDeployment` controller will re-render them from the current spec (which now includes the `hostAliases` entry):
    
    
    kubectl delete pod -n APIGEE_NAMESPACE -l app=apigee-runtime

The `ApigeeDeployment` controller will recreate the pods within a minute. Note that `kubectl rollout restart deploy` (the vanilla Kubernetes command) does not work on Message Processor because Message Processor is deployed as an `ApigeeDeployment` custom resource, not a `Deployment`.

**Internal-only hostnames.** `mcp.apigee.internal` and `ORG_NAME.mcp.apigee.internal` are resolvable only from Message Processor pods inside your cluster, through the `hostAliases` entry injected in this procedure. Do not use them as client-facing MCP endpoint URLs. External MCP clients reach your MCP data plane through your Apigee ingress hostname, the same way they reach any other Apigee proxy.**Note:** At this point in the procedure, no MCP Discovery Proxy has been deployed, so the sidecar has not yet loaded a listener on the MCP request port. An end-to-end MCP `initialize` request will not succeed until you complete the [MCP quickstart](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/apigee-mcp-quickstart). The full end-to-end `initialize` verification is part of the [quickstart](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/apigee-mcp-quickstart), not this page.

### Install complete

Together, the previous three checks confirm your MCP data plane is running and MP-addressable:

  * Every MCP pod is `2/2 Running`. The MCP data plane container fails its Kubernetes readiness probe on port `15021` if the operator-issued TLS certificate is not loaded and the sidecar has not yet loaded its initial MCP configuration, so `Ready` pods have both those preconditions in place.
  * Every MP pod's spec contains the `hostAliases` entry pinning `mcp.apigee.internal` and `ORG_NAME.mcp.apigee.internal` to the MCP Service ClusterIP. MP pods can therefore resolve MCP proxy target endpoints to your in-cluster MCP data plane.
  * An MP pod resolves `mcp.apigee.internal` to the MCP Service ClusterIP through the injected `hostAliases` entry.



You verify end-to-end MCP tool traffic (an actual MCP `initialize` or `tools/list` call through your Apigee ingress) as part of the shared [MCP quickstart](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/apigee-mcp-quickstart), after you deploy your first MCP Discovery Proxy.

If any of the previous three checks fails, consult [Troubleshoot MCP deployments](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/troubleshoot-mcp-deployments#hybrid-cluster-side-diagnosis) before proceeding to the [quickstart](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/apigee-mcp-quickstart).

## Step 6: Enable MCP on remaining clusters

MCP requests for a given hostname can route to any cluster serving the corresponding Apigee environment group. If MCP is enabled on some clusters and not others in the same environment group, MCP requests that route to a cluster without MCP enabled fail (typically returned to the client as `503 Service Unavailable`).

**Enable MCP uniformly on every cluster that serves the same environment group.** For each additional cluster, repeat Steps 1, 3, 4, and 5. You do not need to repeat Step 2 (grant watcher identity access): that grant is scoped to the Apigee organization and applies to all clusters in the same organization.

## Rollback

To disable MCP on a cluster, set `enableMcpServer: false` (or remove the field entirely) in `overrides.yaml`, then upgrade the `apigee-org` chart:
    
    
    helm upgrade APIGEE_ORG_RELEASE_NAME apigee-org/ \
      --namespace APIGEE_NAMESPACE --atomic -f overrides.yaml

The `enableMcpServer` field is consumed by the `apigee-org` chart only, so the operator chart does not need to be upgraded during a disable. The Apigee operator (unchanged) picks up the config change from the `ApigeeOrganization` custom resource, deletes the MCP resources, and removes the `hostAliases` entry from the Message Processor pod spec, which triggers a release of the `apigee-runtime` `ApigeeDeployment`. Roll back in an approved maintenance window.

After rollback, the MCP Discovery Proxies you deployed to the Apigee environment are still present in the Apigee control plane, but no cluster in that environment group serves MCP traffic. Undeploy the MCP Discovery Proxies to fully unwind the feature, or leave them deployed and re-enable MCP on the clusters later.

## Reference: MCP fields in `overrides.yaml`

The following table lists every Apigee hybrid `overrides.yaml` field that controls MCP behavior in version `1.17.0`. Only `enableMcpServer` is required; all other fields have safe defaults that suit most installations.

Field definitions match the `apigee-org` Helm chart defaults for hybrid `1.17.0`.

Field | Type | Default | Recommended tuning  
---|---|---|---  
`enableMcpServer` | boolean | `false` | **Required.** Set to `true` to enable MCP on this cluster. Toggling this field triggers a staged canary release of Message Processor. Toggle only in a maintenance window and wait for the release to complete before proceeding.  
`mcpServer.replicaCountMin` | integer | `2` | Keep at `2` for HA. Increase only if you have a baseline of high MCP traffic; the HPA scales up automatically under CPU pressure. Signal: sustained HPA at `replicaCountMax` and CPU above target.  
`mcpServer.replicaCountMax` | integer | `10` | Increase if you observe the HPA capped at `10` during peak. Signal: `kubectl top pods -l app=apigee-mcp-server` shows all pods near their CPU limit at peak. If `metrics-server` is not installed, use `kubectl get hpa -n APIGEE_NAMESPACE | grep apigee-mcp-server` and check whether the `REPLICAS` column is at the `MAXPODS` ceiling.  
`mcpServer.targetCPUUtilizationPercentage` | integer | `70` | Lower to `50`–`60` for latency-sensitive workloads (scales earlier). Raise to `80`–`85` to reduce replica count in cost-sensitive clusters. Signal: p95 request latency correlates with per-pod CPU.  
`mcpServer.resources.requests` | ResourceList | `cpu: 500m, memory: 512Mi` | Increase requests if pods are frequently OOMKilled or CPU-throttled at steady state. Signal: `kubectl describe pod` shows OOMKilled or throttled conditions.  
`mcpServer.resources.limits` | ResourceList | `cpu: 2000m, memory: 1Gi` | Raise the CPU limit before raising replica count when p95 latency is high but overall QPS is low (few, expensive requests). Raise the memory limit only if you see OOMKills.  
`mcpServer.sidecar.resources.requests` | ResourceList | `cpu: 200m, memory: 128Mi` | Rarely needs tuning. The sidecar periodically composes and writes configuration bundles; steady-state CPU is minimal.  
`mcpServer.sidecar.resources.limits` | ResourceList | `cpu: 500m, memory: 512Mi` | Rarely needs tuning. Increase memory only if you deploy an unusually large number of MCP tools in a single Discovery Proxy.  
`mcpServer.terminationGracePeriodSeconds` | integer | `30` | Rarely needs tuning. Increase if long-lived in-flight MCP requests need more time to complete during a pod drain.  
`mcpServer.annotations` | map | `{}` | Add extra pod annotations if your cluster requires them.  
`mcpServer.serviceAccountPath` | string | _unset_ | **Leave unset unless you need per-component identity separation.** When unset, MCP uses `watcher.serviceAccountPath`. MCP does not use `envs[].serviceAccountPaths.runtime`. The `apigee-watcher` identity already holds the permissions the MCP sidecar needs. If you override this field, specify the path to a Google Cloud service account key JSON file. Mutually exclusive with `mcpServer.gsa`.   
  
If Workload Identity is not enabled, and you set neither `mcpServer.serviceAccountRef` nor `serviceAccountSecretProviderClass`, you must set `mcpServer.serviceAccountPath` or `watcher.serviceAccountPath`. If you set neither, `helm upgrade` fails with the error `mcpServer.serviceAccountPath or watcher.serviceAccountPath is required!!`.   
  
**Prefer Workload Identity (GKE) or Workload Identity Federation (AKS/EKS) whenever possible.** File-based service account keys must be rotated, stored securely, distributed to every cluster, and are the most common source of leaks into support artifacts (see [Support cases](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/troubleshoot-mcp-deployments#support-cases)).  
`mcpServer.gsa` | string | _unset_ | **Leave unset unless you need per-component identity separation.** When unset, MCP falls back to `watcher.gsa`, then to `gcp.workloadIdentity.gsa`. The `apigee-watcher` identity already holds the permissions the MCP sidecar needs, so reusing it is the recommended path. Override with a dedicated Google Cloud service account email only if your organization requires a distinct identity for the MCP sidecar for audit reasons.  
`mcpServer.serviceAccountRef` | string | _unset_ | Advanced. Name of an existing Kubernetes Secret in the Apigee namespace that holds a Google Cloud service account key for the MCP sidecar. Use this only if you manage service account key Secrets outside of the Apigee Helm charts. Mutually exclusive with `mcpServer.serviceAccountPath` and `mcpServer.gsa`.   
  
MCP does not use `watcher.serviceAccountRef`. If your base installation stores the `apigee-watcher` key in a Kubernetes secret with `watcher.serviceAccountRef`, set this property to the same secret name.  
`mcpServer.podDisruptionBudget` | map | _unset_ | Optional PodDisruptionBudget for the MCP pods. Accepts `minAvailable` or `maxUnavailable` (integer or percentage string). Set one, not both. Leave unset unless your cluster has strict voluntary disruption policies that require an explicit budget.  
`mcpServer.tolerations` | list | _unset_ (falls back to top-level `tolerations`) | Standard Kubernetes tolerations for MCP pods. Set only if MCP pods must tolerate taints that other Apigee components do not.  
`mcpServer.image.pullPolicy` | string | `IfNotPresent` | Image pull policy for the MCP server container. Rarely changed.  
`mcpServer.sidecar.image.pullPolicy` | string | `IfNotPresent` | Image pull policy for the MCP sidecar container. Rarely changed.  
**Note:** The MCP Service and container ports are fixed in the operator and are not configurable through `overrides.yaml` in version `1.17.0`. See Verify the MCP data plane is running for the full breakdown of the four Service ports. In summary: port `443` carries MCP tool traffic from Message Processor and remaps to pod port `8443`; port `15021` exposes the MCP data plane readiness endpoint used by kubelet; ports `80` and `15000` are also declared on the Service manifest and are not used by MCP tool traffic in `1.17.0`.

## Estimate MCP tool capacity

Apigee hybrid does not enforce a fixed maximum number of MCP tools per organization. Instead, tool capacity is bounded by four hard size limits enforced at deploy or request time. Whether a specific number of tools fits depends on the size of each tool, which is derived from the OpenAPI specification that defines the tool.

### Typical capacity

For most OpenAPI specifications — a mix of tools with varying parameter counts, request-body sizes, and description lengths, with the majority of tools falling into the small-to-medium size range — you can typically expect to fit 10,000 MCP tools per organization at the default `tools/list` response size limit.

Actual capacity varies with the specific shape of your OpenAPI specification. Organizations whose specifications are dominated by tools with many parameters, large request bodies, or long descriptions fit proportionally fewer tools before reaching one of the four hard limits below. To validate capacity for your specific specifications, follow Estimate capacity for your specification below.

### Hard limits

Four size limits apply in Apigee hybrid version `1.17.0`. The lowest applicable limit is what binds; raising one does not raise the others.

Limit | Value | Scope | Failure mode  
---|---|---|---  
OpenAPI specification file size | 3 MiB | per `.yaml` file | `400` at proxy validate  
MCP proxy bundle size (decompressed) | 50 MiB | per MCP Discovery Proxy | `400` at proxy validate  
`tools/list` response size | 10 MiB (default) | per hostname | `502` with `TooBigBody`  
Hostnames per environment group | 100 | per environment group | `400` at environment-group update  
  
### What drives per-tool size

Per-tool size is composed almost entirely of the tool's `inputSchema`, which is derived from the OpenAPI specification's `parameters` and `requestBody` for the operation. Three properties matter most:

  * **Number of parameters.** Each parameter entry contributes roughly 100 bytes to the tool's size in the `tools/list` response.
  * **Number of request-body properties.** Each request-body property contributes roughly 100 bytes. Operations with a request body (typically `POST` and `PUT`) are therefore substantially larger than operations without one (typically `GET` and `DELETE`).
  * **Description length.** Operation descriptions are copied almost verbatim into the tool, so a longer description directly increases the tool's size.



**Response schemas do not count against the size budget.** Only `parameters` and `requestBody` reach the MCP configuration. Sizing capacity by OpenAPI file size alone therefore tends to overestimate cost, because most real OpenAPI specifications include response-schema definitions that do not affect tool size.

### Estimate capacity for your specification

The most reliable way to estimate tool capacity for your OpenAPI specifications is to measure a representative subset:

  1. Deploy an MCP Discovery Proxy that references a small representative subset of the tools you plan to publish (for example, 50 to 100 tools that reflect the mix of parameter counts, request-body sizes, and description lengths in your full specification).
  2. Call `tools/list` against the deployed proxy and record the response size in bytes and the number of tools returned.
  3. Divide response size by tool count to get the average size per tool for your specification.
  4. Divide the applicable `tools/list` response size limit (10 MiB by default) by that average to estimate the maximum number of tools that fit on one hostname for a specification of this shape.

**Note:** The average size per tool depends on the specific shape of your OpenAPI specification, not just the tool count. Re-measure whenever you make structural changes to your specification (for example, adding request-body properties to many operations or lengthening operation descriptions), and re-measure when you upgrade to a later Apigee hybrid version.

### Increasing capacity

Two mechanisms increase tool capacity beyond the defaults:

  * **Shard tools across hostnames.** The `tools/list` response cap is per hostname. Splitting tools across multiple hostnames within the same environment group multiplies per-hostname headroom (subject to the 100-hostnames-per-environment-group limit). Sharding does not raise the per-proxy bundle limit; the 50 MiB bundle cap continues to apply across all hostnames on a single MCP Discovery Proxy.
  * **Raise the`tools/list` response size limit.** The default limit is 10 MiB per hostname. You can raise it up to 30 MiB. At a minimum, this involves setting `envs.components.runtime.resources.limits.memory`, `envs.components.runtime.resources.requests.memory`, and `envs.components.runtime.cwcAppend.bin_setenv_max_mem` in your `overrides.yaml`, then running `helm upgrade` on the `apigee-org` chart. See [Configure large message payload support in Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/latest/configure-large-payload-support) for the complete procedure, including per-environment versus whole-installation variants, Message Processor heap sizing guidance, and full `overrides.yaml` examples. Raising the response limit does not affect the 50 MiB MCP proxy bundle size limit; if your capacity is constrained by that limit instead, this change won't help.

**Version note:** The four hard limits above apply to Apigee hybrid version `1.17.0`. If you upgrade to a later version, re-check these limits and re-run the estimation for your specifications before making capacity commitments.

## Security

### Trust boundary

The MCP data plane runs inside your own Kubernetes cluster. Google has no runtime access to the data plane. The Apigee control plane serves you MCP configuration derived from your OpenAPI Specification; it does not observe MCP request traffic. Configuration data at rest is stored in an Apigee-managed Cloud Storage bucket scoped to your Apigee tenant project, fetched by the MCP sidecar using its ambient Google Cloud service account.

The Apigee operator provisions an MCP-scoped Kubernetes `Role` and `RoleBinding` in your Apigee namespace (`APIGEE_NAMESPACE`) for the MCP data plane ServiceAccount. The Role grants read-only access:

  * `get`, `list`, `watch` on `services` in the core API group.
  * `get`, `list`, `watch` on `apigeeroutes` in the `apigee.cloud.google.com` API group.



The Role grants no write verbs and no access to `Secrets`, `ConfigMaps`, or pod status. Your auditor can verify the exact rules directly from the cluster with:
    
    
    APIGEE_ORG_CR=$(kubectl get apigeeorganization -n APIGEE_NAMESPACE \
      -o jsonpath='{.items[0].metadata.name}')
    kubectl get role,rolebinding -n APIGEE_NAMESPACE \
      --field-selector metadata.name=apigee-mcp-server-$APIGEE_ORG_CR -o yaml

The `apigee-mcp-server-APIGEE_ORG_CR` Role and RoleBinding are the MCP-scoped RBAC resources; their names include the full name of your `ApigeeOrganization` custom resource (which is derived from your Apigee organization name and a short hash). They do not carry an `app=apigee-mcp-server` label at the resource level (only the pods do), so a label-based lookup returns no results. If the field-selector command above returns nothing, list every MCP-related RBAC resource in the namespace with:
    
    
    kubectl get role,rolebinding -n APIGEE_NAMESPACE | grep apigee-mcp-server

### TLS between Message Processor and MCP data plane

Message Processor pods dial the MCP data plane at `https://mcp.apigee.internal/` or `https://ORG_NAME.mcp.apigee.internal/`. These hostnames resolve to the MCP Service ClusterIP through the injected `hostAliases` entry. The MCP data plane container presents a TLS certificate signed by the Apigee-operator-provisioned issuer (the ClusterIssuer named `apigee-ca-issuer`). The certificate's Subject Alternative Names include both hostnames.

### Restrict inbound access to the MCP Service

In Apigee hybrid `1.17.0`, the MCP data plane does not independently authenticate its callers. It trusts that requests reaching it have already been authenticated by an Apigee MCP proxy running in Message Processor. The only intended caller of the MCP Service is Message Processor. Any other in-cluster workload that can reach the MCP Service ClusterIP on TCP `443` can invoke MCP tools without an authentication check.

**Restrict inbound access to the MCP pods to Message Processor pods only** , using your platform's cluster ingress policy engine (Kubernetes NetworkPolicy, Cilium, Calico, Istio AuthorizationPolicy, or equivalent). The restriction:

  * Allows ingress to pods with label `app=apigee-mcp-server` in namespace `APIGEE_NAMESPACE` on TCP `443` from pods with label `app=apigee-runtime` in the same namespace only.
  * Denies all other ingress on TCP `443` to pods with label `app=apigee-mcp-server`.
  * Denies all in-cluster ingress on TCP `15021` to pods with label `app=apigee-mcp-server`. Port `15021` serves an unauthenticated plain-HTTP `/healthz/ready` endpoint used by kubelet for readiness probing; kubelet reaches it directly on the pod IP, so no other in-cluster workload should reach the MCP pods on `15021`.



Apply this restriction before you complete the [MCP quickstart](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/apigee-mcp-quickstart) and deploy your first MCP Discovery Proxy in a non-development environment.

### Configuration freshness contract

When the MCP sidecar completes a successful configuration pull, the MCP data plane container loads the fetched bundle and continues serving it until the next successful pull. If subsequent pulls fail (Apigee control plane unreachable, Cloud Storage unreachable, IAM permission removed on the watcher service account, or an error at any other stage of the pull pipeline), the sidecar keeps serving the last-known-good bundle indefinitely. There is no built-in staleness ceiling in `1.17.0`: the pod stays `Ready` and MCP tool traffic continues to be served against the stale bundle. The signal that configuration has stopped refreshing is a sidecar log line at `ERROR` level that carries a `consecutive_failures` counter (see [Troubleshoot MCP deployments](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/troubleshoot-mcp-deployments#hybrid-cluster-side-diagnosis) for the specific messages the sidecar emits per failure stage).

**For regulated production environments, page on repeated increments of this counter.** A minimum viable alert is: page when any MCP sidecar container emits an `ERROR`-level log line with `consecutive_failures` reaching a threshold you set based on your staleness tolerance. Rising values indicate that the sidecar has stopped refreshing configuration; the sidecar continues to serve the last-successful bundle in the meantime.

If the sidecar has stopped refreshing configuration, investigate the failure mode from the sidecar logs; see [Troubleshoot MCP deployments](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/troubleshoot-mcp-deployments#hybrid-cluster-side-diagnosis). Bouncing the MCP pods does not resolve the underlying fetch problem because newly created pods hit the same fetch path.

### Outbound network requirements

The MCP sidecar (the configuration container inside each MCP pod) needs outbound network access to the following endpoints on TCP `443`. Pick the tab that matches whether your Apigee organization uses data residency; the required endpoints differ.

### No data residency

Endpoint | Used for  
---|---  
`apigee.googleapis.com` | Retrieve the current MCP configuration reference for your organization from the Apigee control plane on each configuration refresh.  
`storage.googleapis.com` | Download your organization's MCP configuration from Google Cloud Storage.  
  
### Data residency

If your Apigee organization uses [data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts), the MCP sidecar hits your regional Apigee control-plane endpoint (the same endpoint your other Apigee hybrid components use, configured via the `contractProvider` chart value in your `overrides.yaml`). Replace CONTROL_PLANE_LOCATION with your organization's control-plane location (for example, `us`, `eu`).

Endpoint | Used for  
---|---  
`CONTROL_PLANE_LOCATION-apigee.googleapis.com` | Retrieve the current MCP configuration reference for your organization from your regional Apigee control-plane endpoint on each configuration refresh.  
`storage.googleapis.com` | Download your organization's MCP configuration from Google Cloud Storage. The bucket is located in your organization's region; Cloud Storage routes to it automatically.  
  
In addition, the sidecar must be able to obtain Google Cloud access tokens for the ambient credentials the pod runs as (through Workload Identity or a file-based service account key). The specific token-exchange endpoints depend on your authentication path and are the same ones that other Apigee hybrid components already use in your cluster. If existing Apigee hybrid traffic to Google Cloud APIs succeeds from this namespace, the MCP sidecar's token exchange also succeeds.

Additionally, the sidecar needs in-cluster access to the Kubernetes API server (through the standard in-cluster service address) to publish its liveness and readiness state. This traffic never leaves your cluster.

**Do not allowlist only`apigee.googleapis.com`.** If your egress controls permit the Apigee control-plane call but block `storage.googleapis.com`, the sidecar completes its configuration reference fetch successfully but fails on the subsequent bundle fetch. The MCP data plane container continues serving stale or empty configuration and the failure mode is subtle: the MCP data plane appears healthy but never picks up new MCP Discovery Proxy deployments. Allowlist both endpoints in the table above (and preserve the token-exchange egress your other Apigee hybrid components already rely on).

## Troubleshooting

For a full diagnostic checklist, see [Troubleshoot MCP deployments](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/troubleshoot-mcp-deployments), which includes a [ cluster-side diagnostic checklist](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/troubleshoot-mcp-deployments#hybrid-cluster-side-diagnosis) for Apigee hybrid.

### Common install failures

Symptom | Cause and fix  
---|---  
`helm upgrade` completes but no MCP resources appear. | The organization chart was upgraded before the operator chart. Run `helm upgrade APIGEE_OPERATOR_RELEASE_NAME apigee-operator/` first, then re-run `helm upgrade APIGEE_ORG_RELEASE_NAME apigee-org/`.  
MCP pods stuck in `ContainerCreating` or `1/2 Ready`. | Two common causes: the cert-manager `Certificate` for MCP has not yet been issued, or the container image pull is failing. Run `kubectl describe pod` on the affected pod for the exact reason.  
Sidecar (`apigee-mcp-server-config`) logs report `no MCP config from CP yet; skipping tick, pod stays Ready via seed` on every poll. | Expected steady state when no MCP Discovery Proxy has been deployed for your organization yet. The Apigee control plane returns an empty configuration reference and the MCP data plane has only the Kubernetes readiness listener loaded on port `15021`; the MCP request port `8443` has no listener yet, and requests to `https://mcp.apigee.internal/mcp` receive a connection refused. To transition into the serving state, follow the [MCP quickstart](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/apigee-mcp-quickstart) to deploy an MCP Discovery Proxy to an environment in the environment group served by this cluster.  
Sidecar logs report `CP fetch failed` with an embedded HTTP `403` or `PermissionDenied`. | The Apigee watcher Google Cloud service account has lost the `roles/apigee.runtimeAgent` role (which grants the `apigee.runtimeconfigs.get` permission the sidecar needs) in your Apigee tenant project. Base Apigee hybrid installation grants this role automatically; if it has been removed by an IAM automation sweep, re-apply it on the `apigee-watcher` Google Cloud service account.  
Sidecar logs report `CP fetch failed` with `context deadline exceeded`, DNS errors, or TLS errors. | The sidecar cannot reach `apigee.googleapis.com` or `storage.googleapis.com` from inside your cluster. Verify egress against the three endpoints listed in Outbound network requirements above.  
Message Processor pods did not restart after `helm upgrade`. | Verify the `hostAliases` entry is present on every MP pod: `kubectl get pods -n APIGEE_NAMESPACE -l app=apigee-runtime -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.spec.hostAliases}{"\n"}{end}'`. If any pod shows empty, force a fresh render by deleting the pod (`kubectl delete pod -n APIGEE_NAMESPACE -l app=apigee-runtime`). The `ApigeeDeployment` controller will recreate it from the current spec, which includes the `hostAliases` entry. Do not use `kubectl rollout restart deploy`; it does not apply to `ApigeeDeployment`.  
MP pod logs show TLS handshake errors dialing `https://mcp.apigee.internal/` or `https://ORG_NAME.mcp.apigee.internal/` after MCP tool traffic starts flowing through the [quickstart](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/apigee-mcp-quickstart). | The MCP data plane container is serving a certificate whose Subject Alternative Names (SANs) do not include the hostname the MP dialed. Verify the certificate: `kubectl get cert -n APIGEE_NAMESPACE | grep apigee-mcp-server`, then `kubectl get cert -n APIGEE_NAMESPACE CERT_NAME -o yaml`. The certificate’s `dnsNames` must include both `mcp.apigee.internal` and the lowercased `ORG_NAME.mcp.apigee.internal`. If they do not, delete the MCP `Certificate` resource and let `cert-manager` reissue.  
  
## What's next

  * Follow the [MCP quickstart](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/apigee-mcp-quickstart) to deploy your first MCP Discovery Proxy and call an MCP tool from an MCP client.
  * Learn how to [manage MCP tool access with API products](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/manage-mcp-tool-access).
  * Learn how to [monitor and analyze MCP traffic](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/monitor-analyze-mcp-traffic).
  * Consult the [MCP troubleshooting guide](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/troubleshoot-mcp-deployments) for advanced diagnostics.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
