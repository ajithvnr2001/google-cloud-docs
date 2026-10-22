---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/agent-sandbox/
title: Isolate AI code execution with Agent Sandbox on GKE \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:37:29.454261+00:00
---

# Isolate AI code execution with Agent Sandbox on GKE  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/agent-sandbox/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Isolate AI code execution with Agent Sandbox on GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

You can deploy a developer environment to use the Agent Sandbox Python client on a Google Kubernetes Engine (GKE) cluster. This setup helps you safely execute and test AI-generated code by isolating untrusted code within a sandboxed Python environment. This isolation is crucial for protecting your system from potential vulnerabilities in AI-generated code, increasing development velocity, and ensuring secure deployments. For an overview of how Agent Sandbox on GKE isolates untrusted AI-generated code, see [About Agent Sandbox on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/agent-sandbox).

## Costs

Agent Sandbox on GKE is offered at no extra charge. [GKE pricing](https://cloud.google.com/kubernetes-engine/pricing) applies to the resources that you create.

## Before you begin

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  3. Enable the Artifact Registry, Kubernetes Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com,container.googleapis.com)

  4. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  5. Verify that you have the permissions required to complete this document.
  6. You must have a GKE cluster with Agent Sandbox on GKE enabled. If you don't have one, follow the instructions in [Enable Agent Sandbox on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/how-install-agent-sandbox) to create a new cluster or update an existing one.



### Required roles

To get the permissions that you need to create and manage sandboxes, ask your administrator to grant you the [Kubernetes Engine Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.admin) (`roles/container.admin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Define environment variables

To simplify the commands that you run in this document, you can set environment variables in Cloud Shell. In Cloud Shell, define the following useful environment variables by running the following commands:
    
    
    export PROJECT_ID=$(gcloud config get project)
    export CLUSTER_NAME="agent-sandbox-cluster"
    export LOCATION="us-central1"
    export NODE_POOL_NAME="agent-sandbox-node-pool"
    export MACHINE_TYPE="e2-standard-2"
    

Here's an explanation of these environment variables:

  * `PROJECT_ID`: the ID of your current Google Cloud project. Defining this variable helps ensure that all resources, like your GKE cluster, are created in the correct project.
  * `CLUSTER_NAME`: the name of your GKE cluster—for example, `agent-sandbox-cluster`.
  * `LOCATION`: the Google Cloud region or zone where your GKE cluster is located. Set this to the region (for example, `us-central1`) if you are using an Autopilot cluster, or the zone (for example, `us-central1-a`) if you are using a Standard cluster.
  * `NODE_POOL_NAME`: the name of the node pool that will run sandboxed workloads—for example, `agent-sandbox-node-pool`.
  * `MACHINE_TYPE`: the machine type of the nodes in your node pool—for example, `e2-standard-2`. For details about different machine series and choosing between different options, see the [Machine families resource and comparison guide](https://docs.cloud.google.com/compute/docs/machine-resource).



## Deploy a sandboxed environment

This section shows you how to create the sandbox blueprint (`SandboxTemplate`), deploy the necessary networking router, and install the Python client you will use to interact with the sandbox.

The recommended way to create and interact with your sandbox is by using the [Agentic Sandbox Python client](https://github.com/kubernetes-sigs/agent-sandbox/tree/main/clients/python/agentic-sandbox-client). This client provides an interface that simplifies the entire lifecycle of a sandbox, from creation to cleanup. It's a Python library you can use to programmatically create, use, and delete sandboxes.

The client uses a Sandbox Router as a central entry point for all traffic. In the example described in this document, the client creates a tunnel to this router using the command `kubectl port-forward`, so that you don't need to expose any public IP addresses. Be aware that making use of `kubectl port-forward` isn't a secure solution and its use should be limited to development environments.

### Create a `SandboxTemplate` and `SandboxWarmPool`

You now define the configuration for your sandbox by creating a `SandboxTemplate` and a `SandboxWarmPool` resource. The `SandboxTemplate` acts as a reusable blueprint that the Agent Sandbox controller uses to create consistent, pre-configured sandbox environments. The `SandboxWarmPool` resource helps ensure that a specified number of _pre-warmed_ Pods are always running and ready to be claimed. A pre-warmed sandbox is a running Pod that's already initialized. This pre-initialization enables new sandboxes to be created in under a second, and avoids the startup latency of launching a regular sandbox:

  1. In Cloud Shell, create a file named `sandbox-template-and-pool.yaml` with the following content:
         
         apiVersion: extensions.agents.x-k8s.io/v1beta1
         kind: SandboxTemplate
         metadata:
           name: python-runtime-template
           namespace: default
         spec:
           podTemplate:
             metadata:
               labels:
                 sandbox: python-sandbox-example
             spec:
               runtimeClassName: gvisor
               automountServiceAccountToken: false # Required
               securityContext:
                 runAsNonRoot: true # Required
               nodeSelector:
                 sandbox.gke.io/runtime: gvisor # Required
               tolerations:
               - key: "sandbox.gke.io/runtime"
                 value: "gvisor"
                 effect: "NoSchedule" # Required
               containers:
               - name: python-runtime
                 image: registry.k8s.io/agent-sandbox/python-runtime-sandbox:v0.1.0
                 ports:
                 - containerPort: 8888
                 readinessProbe:
                   httpGet:
                     path: "/"
                     port: 8888
                   initialDelaySeconds: 0
                   periodSeconds: 1
                 resources:
                   requests:
                     cpu: "250m"
                     memory: "512Mi"
                   limits:
                     cpu: "500m"
                     memory: "1Gi" # Required
                 securityContext:
                   capabilities:
                     drop: ["ALL"] # Required
               restartPolicy: "OnFailure"
         ---
         apiVersion: extensions.agents.x-k8s.io/v1beta1
         kind: SandboxWarmPool
         metadata:
           name: python-sandbox-warmpool
           namespace: default
         spec:
           replicas: 2
           sandboxTemplateRef:
             name: python-runtime-template
         

  2. Apply the `SandboxTemplate` and `SandboxWarmPool` manifest:
         
         kubectl apply -f sandbox-template-and-pool.yaml
         




### Deploy the Sandbox Router

The Python client that you will use to create and interact with sandboxed environments uses a component called the Sandbox Router to communicate with the sandboxes.

For this example, you use the client's _developer mode_ for testing. This mode is intended for local development, and uses the command `kubectl port-forward` to establish a direct tunnel from your local machine to the Sandbox Router service running in the cluster. This tunneling approach avoids the need for a public IP address or complex ingress setup, and simplifies interacting with sandboxes from your local environment.

Follow these steps to deploy the Sandbox Router:

  1. In Cloud Shell, create a file named `sandbox-router.yaml` with the following content:
         
         # A ClusterIP Service to provide a stable endpoint for the router pods.
         apiVersion: v1
         kind: Service
         metadata:
           name: sandbox-router-svc
           namespace: default
         spec:
           type: ClusterIP
           selector:
             app: sandbox-router
           ports:
           - name: http
             protocol: TCP
             port: 8080 # The port the service will listen on
             targetPort: 8080 # The port the router container listens on (from the sandbox_router/Dockerfile)
         ---
         # The Deployment to manage and run the router pods.
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: sandbox-router-deployment
           namespace: default
         spec:
           replicas: 1
           selector:
             matchLabels:
               app: sandbox-router
           template:
             metadata:
               labels:
                 app: sandbox-router
             spec:
               # Ensure pods are spread across different zones for HA
               topologySpreadConstraints:
                 - maxSkew: 1
                   topologyKey: topology.kubernetes.io/zone
                   whenUnsatisfiable: ScheduleAnyway
                   labelSelector:
                     matchLabels:
                       app: sandbox-router
               containers:
               - name: router
                 image: us-central1-docker.pkg.dev/k8s-staging-images/agent-sandbox/sandbox-router:latest-main
                 ports:
                 - containerPort: 8080
                 readinessProbe:
                   httpGet:
                     path: /healthz
                     port: 8080
                   initialDelaySeconds: 5
                   periodSeconds: 5
                 livenessProbe:
                   httpGet:
                     path: /healthz
                     port: 8080
                   initialDelaySeconds: 10
                   periodSeconds: 10
                 resources:
                   requests:
                     cpu: "100m"
                     memory: "512Mi"
                   limits:
                     cpu: "1000m"
                     memory: "1Gi"
               securityContext:
                 runAsUser: 1000
                 runAsGroup: 1000
         

**Best Practice** : 

This example uses the `latest-main` image tag, which always points to the most recent build. For stability in production, pull a specific image version by using that version's SHA-256 image digest. For example, `sandbox-router@sha256:b158ea22b405af60fe4d00abfca12caea5465fd30b5f30a4b6184c8115925f51`. Specifying the image digest in the image name pins the code that you run, so that a change in the repository won't result in an update to the image in your cluster.

  2. Apply the manifest to deploy the router to your cluster:
         
         kubectl apply -f sandbox-router.yaml
         

  3. Verify that the Sandbox Router deployment is running correctly:
         
         kubectl get deployment sandbox-router-deployment
         

Wait for the deployment to show 2/2 or 1/1 in the `READY` column.




### Install the Python client

Now that the in-cluster components like the Sandbox Router are deployed, the final preparatory step is to install the [Agentic Sandbox Python client](https://pypi.org/project/k8s-agent-sandbox/) on your local machine. Recall that this client is a Python library that lets you programmatically create, use, and delete sandboxes. You use it in the next section to test the environment:

  1. Create and activate a Python virtual environment:
         
         python3 -m venv .venv
         source .venv/bin/activate
         

  2. Install the client package:
         
         pip install k8s-agent-sandbox
         




## Test the sandbox

With all the setup components in place, you can now create and interact with a sandbox using the Agentic Sandbox Python client.

  1. In your `agent-sandbox` directory, create a Python script named `test_sandbox.py` with the following content:
         
         from k8s_agent_sandbox import SandboxClient
         from k8s_agent_sandbox.models import SandboxLocalTunnelConnectionConfig
         
         # Automatically tunnels to svc/sandbox-router-svc
         client = SandboxClient(
             connection_config=SandboxLocalTunnelConnectionConfig()
         )
         
         sandbox = client.create_sandbox(template="python-runtime-template", namespace="default")
         try:
             print(sandbox.commands.run("echo 'Hello from the sandboxed environment!'").stdout)
         except Exception as e:
             print(f"An error occurred: {e}")
         

  2. From your terminal (with the virtual environment still active), run the test script:
         
         python3 test_sandbox.py
         




You should see the message "Hello from the sandboxed environment!" which is output from the sandbox.

Congratulations! You have successfully run a shell command inside a secure sandbox. Using the `sandbox.run()` method, you can execute any shell command, and Agent Sandbox on GKE runs the command within a secure barrier that protects your cluster's nodes and other workloads from untrusted code. This provides a safe and reliable way for an AI agent or any automated workflow to execute tasks.

When you run the script, the `SandboxClient` handles all the steps for you. It creates the `SandboxClaim` resource to start the sandbox, waits for the sandbox to be ready, and then uses the `sandbox.run()` method to execute bash shell commands inside the secure container. The client then captures and prints the `stdout` from that command. The sandbox is automatically deleted after the program runs.

When a `SandboxClaim` resource is created, an available Pod is assigned from the warm pool to the Sandbox object and the claim is marked ready. The `SandboxWarmPool` then automatically replenishes itself to maintain the configured number of replicas.

To verify if a specific sandbox is claimed or available, check the `ownerReferences` in sandbox pod's metadata - if the value of the `kind` field is `Sandbox`, the pod is in use. If the value of the `kind` field is `SandboxWarmPool`, the Pod is idle and waiting to be claimed.

## Run sandboxes in production

In this document, you interact with sandboxes from outside of the cluster by using Cloud Shell. The Python client uses your user credentials to authenticate to the cluster and manage sandbox resources, and uses the `kubectl port-forward` command to establish a connection with sandboxes. These steps work well for development scenarios.

In a production scenario, a controller application (like an AI orchestrator) is responsible for creating and managing sandbox resources. To use Agent Sandbox on GKE in production, consider the following:

  * **Authentication** : your controller application must authenticate to the cluster API server to run sandboxes. How you configure authentication depends on where the controller application runs, as follows:

    * If the controller application runs as a Pod in the same cluster, use [Kubernetes RBAC](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control) or [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) with IAM policies to grant the Pod's Kubernetes ServiceAccount the necessary permissions to watch sandboxes or discover network endpoints.
    * If the controller application runs outside of the cluster, use [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation), or IAM service accounts to give the application an identity that you can reference in allow policies.
  * **Routing** : requests from the Python client in your controller application must reach the Sandbox Router in your cluster. In production, use one of the following methods to establish a network connection:

    * If the controller application runs in the same cluster, use the `SandboxDirectConnectionConfig` function to target the URL and port that the Sandbox Router service uses.
    * If the controller application runs outside of the cluster, use the [GKE Gateway API](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api) to create an internal or external load balancer. In your client code, use the `SandboxGatewayConnectionConfig` function to reference your Gateway.

For more information about these routing methods, see the [usage examples on GitHub](https://github.com/kubernetes-sigs/agent-sandbox/blob/main/clients/python/agentic-sandbox-client/README.md#usage-examples) and the [Gateway deployment steps for the router](https://github.com/kubernetes-sigs/agent-sandbox/blob/main/clients/python/agentic-sandbox-client/sandbox-router/README.md).

  * **Sandbox access to Google Cloud resources** : if your sandbox code needs to send requests to Google Cloud APIs, such as Cloud Storage, use an IAM policy with [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) to give the Kubernetes ServiceAccount that the sandbox Pod uses the permissions that are required for that access. Because the default network policy blocks access to the Google Cloud metadata server (`169.254.169.254`), you must customize the network policy to allow this traffic.

  * **Network Policy restrictions** : by default, Agent Sandbox on GKE enforces a strict _Secure-by-Default_ network posture (`networkPolicyManagement: Managed`). The following restrictions apply under this posture:

    * **Ingress** is blocked from all sources except the designated Sandbox Router.
    * **Egress** is allowed to the public internet, but egress to private LAN ranges (RFC 1918), internal cluster DNS (CoreDNS), and the Cloud Provider Metadata Server (`169.254.0.0/16`) is explicitly blocked.

To use Workload Identity Federation for GKE or access other private resources, you must define custom network policies in the `SandboxTemplate`. For detailed configuration details and customizable templates (such as air-gapped sandboxes or Workload Identity Federation for GKE integration), see [Agent Sandbox Network Policy Management](https://github.com/kubernetes-sigs/agent-sandbox/blob/main/examples/policy/network-policy-management/README.md).




## Sandbox security policies

To help ensure a Secure-by-Default environment, the Agent Sandbox on GKE addon uses Kubernetes Validating Admission Policies (VAPs) to enforce security constraints on `Sandbox` and `SandboxTemplate` resources. These policies are applied automatically.

**Note:** The policy split is supported in cluster version `1.36.0-gke.2459000` or later. To update the VAP for an existing cluster, upgrade the cluster version to `1.36.0-gke.2459000` or later before following the steps to modify the policy.

The addon divides security enforcement into a two-tier policy model for better flexibility. The following sections describe these policies: the strictly managed core policy and the customizable hardening policy.

### Core security policy (`sandbox-core-policy`)

The core security policy enforces isolation requirements that help protect the sandbox's integrity. This policy includes rules that require the use of gVisor, network isolation such as disabling `hostNetwork`, and file system isolation such as blocking `hostPath`. Because GKE manages this policy through the `addonmanager.kubernetes.io/mode: Reconcile` setting, you can't modify or override these core rules.

### Hardening security policy (`sandbox-hardening-policy`)

The hardening security policy provides additional security best practices and management options. It enforces constraints such as dropping all capabilities, preventing the addition of new capabilities, and requiring containers to run as non-root with resource limits. GKE deploys this policy in `EnsureExists` mode through the `addonmanager.kubernetes.io/mode: EnsureExists` setting. This setting means GKE creates the policy if it's missing, but you can modify or delete the policy or its binding if needed.

#### Modify or remove hardening constraints

Because the hardening policy is deployed in `EnsureExists` mode, GKE creates the policy if it's missing, but does not overwrite your modifications. If your workloads require exemptions from these hardening rules, you can modify the policy to remove specific constraints or delete the policy binding entirely.

To modify the hardening policy and remove a specific constraint (for example, to allow containers to run as root or omit resource limits), edit the `ValidatingAdmissionPolicy` resource:
    
    
    kubectl edit validatingadmissionpolicy sandbox-hardening-policy
    

In the text editor that opens, locate the `validations` section and remove or modify the constraint expression that blocks your workload.

Alternatively, if you want to disable the hardening policy entirely for your cluster, delete the policy binding:
    
    
    kubectl delete validatingadmissionpolicybinding sandbox-hardening-binding
    

## Known issues

This section describes known issues when using Agent Sandbox on GKE, and how to resolve or work around them.

### Security policy blocks capabilities when using a service mesh

If you attempt to deploy a sandbox that integrates with a service mesh sidecar (for example, Envoy or Istio), the creation of the sandbox might be blocked by the hardening security policy with an error like the following:
    
    
    sandbox create error: sandboxes.agents.x-k8s.io "claude-cli-claim-managed" is forbidden:
    ValidatingAdmissionPolicy 'sandbox-hardening-policy' with binding 'sandbox-hardening-binding'
    denied request: Security Violation: Capabilities.add must be empty. You cannot add capabilities.
    

  * **Cause** : Service mesh sidecars often use an init container, such as `istio-init` or `proxy-init`. These init containers require capabilities like `NET_ADMIN` or `NET_RAW` to configure `iptables` rules for transparent egress routing. By default, the GKE `sandbox-hardening-policy` blocks all capability additions in all container types.
  * **Workaround** : because the GKE hardening policy is deployed in `EnsureExists` mode, you can modify the `ValidatingAdmissionPolicy` to allow specific trusted init containers to request `NET_ADMIN` and `NET_RAW` capabilities. For instructions about how to modify or remove these hardening constraints, see Modify or remove hardening constraints. For example, you can update the policy's validation expressions or variables to exempt trusted container names from the capabilities rule.



### Egress latency or timeout when connecting to Google APIs over IPv6

Workloads inside the sandbox might experience connection timeouts or high latency, as high as two minutes, when attempting to connect to external resources or Google APIs (such as Vertex AI or Cloud Storage).

  * **Cause** : if your GKE cluster has dual-stack IPv6 enabled, DNS resolution for Google APIs returns both IPv4 (A) and IPv6 (AAAA) addresses. Some algorithms in runtime engines, such as Node.js, attempt to connect over IPv6 first. If your GKE VPC doesn't have a valid IPv6 egress route, such as a Cloud NAT or an internet gateway for IPv6, the TCP connection stops responding until the TCP SYN timeout expires. Then, the TCP connection falls back to IPv4.
  * **Resolution** : to resolve this issue, do one of the following:

    * **Configure IPv6 egress** : to allow outbound IPv6 traffic to return to the cluster, configure a valid IPv6 Cloud NAT or internet gateway in your VPC network.
    * **Prefer IPv4 in the workload** : to prefer IPv4 DNS resolution, configure your workload's runtime. For example, in a Node.js application, you can set the following environment variables in your `SandboxTemplate` definition:
          
          env:
          - name: NODE_OPTIONS
            value: "--dns-result-order=ipv4first --no-network-family-autoselection"
          




## Clean up resources

To avoid incurring charges to your Google Cloud account, you should delete the GKE cluster that you created:
    
    
    gcloud container clusters delete $CLUSTER_NAME --location=$LOCATION --quiet
    

## What's next

  * Learn how to [Save and restore Agent Sandbox on GKE environments with Pod snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/agent-sandbox-pod-snapshots).
  * Learn more about the Agent Sandbox open-source project on [GitHub](https://github.com/kubernetes-sigs/agent-sandbox).
  * Learn how to use open source [Kata Containers with Agent Sandbox on GKE](https://github.com/kubernetes-sigs/agent-sandbox/tree/main/examples/kata-gke-sandbox). Kata Containers isn't a Google Cloud product. If you install and use this software, then you're responsible for management and troubleshooting. Google's support and SLAs don't apply to Kata Containers.
  * To understand the underlying technology that provides security isolation for your workloads, see [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods).
  * For more information about enhancing security for your clusters and workloads, see [GKE security overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
