---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/kubectl/
title: Troubleshoot the kubectl command-line tool \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:25:02.209634+00:00
---

# Troubleshoot the kubectl command-line tool  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/kubectl/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Troubleshoot the kubectl command-line tool Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

When working with Google Kubernetes Engine (GKE), issues with the `kubectl` command-line tool can prevent you from deploying applications or managing cluster resources. These problems generally fall into two categories: authentication failures, where the cluster doesn't recognize your identity, and connectivity failures, where your tool can't reach the cluster's control plane.

Use this page to help you diagnose and resolve these issues. Find steps for troubleshooting various authentication problems and debugging connectivity issues between the `kubectl` tool and your cluster's control plane. Learn to check that the necessary plugins are installed and configured, and review network policy and firewall considerations for services like SSH and Konnectivity.

This information is important for anyone who uses `kubectl` commands to manage applications or cluster resources on GKE. It's particularly important for Application developers and Platform admins and operators who rely on `kubectl` commands for their core daily tasks. For more information about the common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

For related information, see the following resources:

  * For more information about problems not specific to GKE, see [Troubleshooting kubectl](https://kubernetes.io/docs/tasks/debug/debug-cluster/troubleshoot-kubectl/) in the Kubernetes documentation.
  * For more information about how to use `kubectl` commands to diagnose problems with your clusters and workloads, see [Investigate a cluster's state with `kubectl`](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/introduction-kubectl).



## Authentication and authorization errors

If you're experiencing errors related to authentication and authorization when using the `kubectl` command-line tool commands, read the following sections for advice.

### Error: 401 (Unauthorized)

When connecting to GKE clusters, you can get an authentication and authorization error with HTTP status code `401 (Unauthorized)`. This issue might occur when you try to run a `kubectl` command in your GKE cluster from a local environment. To learn more, see [Issue: Authentication and authorization errors](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/4xx-errors#unauthorized-cluster-access).

### Error: Insufficient authentication scopes

When you run `gcloud container clusters get-credentials`, you might receive the following error:
    
    
    ERROR: (gcloud.container.clusters.get-credentials) ResponseError: code=403, message=Request had insufficient authentication scopes.
    

This error occurs because you are attempting to access the GKE API from a Compute Engine VM that doesn't have the `cloud-platform` scope.

To resolve this error, grant the missing `cloud-platform` scope. For instructions on changing the scopes on your Compute Engine VM instance, see [Creating and enabling service accounts for instances](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#changeserviceaccountandscopes) in the Compute Engine documentation.

### Error: Executable gke-gcloud-auth-plugin not found

Error messages similar to the following can occur while trying to run `kubectl` commands or custom clients interacting with GKE:
    
    
    Unable to connect to the server: getting credentials: exec: executable gke-gcloud-auth-plugin not found
    
    It looks like you are trying to use a client-go credential plugin that is not installed.
    
    To learn more about this feature, consult the documentation available at:
          https://kubernetes.io/docs/reference/access-authn-authz/authentication/#client-go-credential-plugins
    
    Visit cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#install_plugin to install gke-gcloud-auth-plugin.
    
    
    
    Unable to connect to the server: getting credentials: exec: fork/exec /usr/lib/google-cloud-sdk/bin/gke-gcloud-auth-plugin: no such file or directory
    

To resolve the issue, install the `gke-gcloud-auth-plugin` as described in [Install required plugins](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#install_plugin).

### Error: No auth provider found

The following error occurs if `kubectl` or custom Kubernetes clients have been built with Kubernetes `client-go` version 1.26 or later:
    
    
    no Auth Provider found for name "gcp"
    

To resolve this issue, complete the following steps:

  1. Install `gke-gcloud-auth-plugin` as described in [Install required plugins](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#install_plugin).

  2. Update to the latest version of the gcloud CLI:
         
         gcloud components update
         

  3. Update the `kubeconfig` file:
         
         gcloud container clusters get-credentials CLUSTER_NAME \
             --location=CONTROL_PLANE_LOCATION
         

Replace the following:

     * `CLUSTER_NAME`: the name of your cluster.
     * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.



### Error: The gcp auth plugin is deprecated, use gcloud instead

You might see the following warning message after you [install the `gke-gcloud-auth-plugin`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#install_plugin) and run a `kubectl` command against a GKE cluster:
    
    
    WARNING: the gcp auth plugin is deprecated in v1.22+, unavailable in v1.25+; use gcloud instead.
    

This message appears if your client version is earlier than 1.26.

To resolve this issue, tell your client to use the `gke-gcloud-auth-plugin` authentication plugin instead:

  1. Open your shell login script in a text editor:

### Bash
         
         vi ~/.bashrc

### Zsh
         
         vi ~/.zshrc

If you're using PowerShell, skip this step.

  2. Set the following environment variable:

### Bash
         
         export USE_GKE_GCLOUD_AUTH_PLUGIN=True
         

### Zsh
         
         export USE_GKE_GCLOUD_AUTH_PLUGIN=True
         

### PowerShell
         
         [Environment]::SetEnvironmentVariable('USE_GKE_GCLOUD_AUTH_PLUGIN', True, 'Machine')
         

  3. Apply the variable in your environment:

### Bash
         
         source ~/.bashrc

### Zsh
         
         source ~/.zshrc
         

### PowerShell

Exit the terminal and open a new terminal session.

  4. Update the gcloud CLI:
         
         gcloud components update
         

  5. Authenticate to your cluster:
         
         gcloud container clusters get-credentials CLUSTER_NAME \
             --location=CONTROL_PLANE_LOCATION
         

Replace the following:

     * `CLUSTER_NAME`: the name of your cluster.
     * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.



## Issue: The `kubectl` command isn't found

If you receive a message that the `kubectl` command isn't found, reinstall the `kubectl` binary and set your `$PATH` environment variable:

  1. Install the `kubectl` binary:
         
         gcloud components update kubectl
         

  2. When the installer prompts you to modify your `$PATH` environment variable, enter `y` to proceed. Modifying this variable lets you use `kubectl` commands without typing their full path.

Alternatively, add the following line to wherever your shell stores environment variables, such as `~/.bashrc` (or `~/.bash_profile` in macOS):
         
         export PATH=$PATH:/usr/local/share/google/google-cloud-sdk/bin/
         

  3. Run the following command to load your updated file. The following example uses `.bashrc`:
         
         source ~/.bashrc
         

If you are using macOS, use `~/.bash_profile` instead of `.bashrc`.




## Issue: `kubectl` commands return "connection refused" error

If `kubectl` commands return a "connection refused" error, then you need to set the cluster context with the following command:
    
    
    gcloud container clusters get-credentials CLUSTER_NAME \
           --location=CONTROL_PLANE_LOCATION
    

Replace the following:

  * `CLUSTER_NAME`: the name of your cluster.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.



If you're unsure of what to enter for the cluster name or location, use the following command to list your clusters:
    
    
    gcloud container clusters list
    

## Error: `kubectl` command timed out

If you created a cluster and attempted to run a `kubectl` command against the cluster but the `kubectl` command times out, you'll see an error similar to the following:

  * `Unable to connect to the server: dial tcp IP_ADDRESS: connect: connection timed out`
  * `Unable to connect to the server: dial tcp IP_ADDRESS: i/o timeout`.



These errors indicate that `kubectl` is unable to communicate with the cluster control plane.

To resolve this issue, verify and set the context where the cluster is set and ensure connectivity to the cluster:

  1. Go to `$HOME/.kube/config` or run the command `kubectl config view` to verify that the config file contains the cluster context and the external IP address of the control plane.

  2. Set the cluster credentials:
         
         gcloud container clusters get-credentials CLUSTER_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --project=PROJECT_ID
         

Replace the following:

     * `CLUSTER_NAME`: the name of your cluster.
     * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.
     * `PROJECT_ID`: the ID of the project that the cluster was created in.
  3. If you've enabled authorized networks in the cluster, then ensure that its list of existing authorized networks includes the outgoing IP of the machine that you are attempting to connect from. You can find your existing authorized networks in the console or by running the following command:
         
         gcloud container clusters describe CLUSTER_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --project=PROJECT_ID \
             --format "flattened(controlPlaneEndpointsConfig.ipEndpointsConfig.authorizedNetwork
         sConfig.cidrBlocks[])"
         

If the outgoing IP of the machine is not included in the list of authorized networks from the output of the preceding command, then complete one of the following steps:

     * If you're using the console, follow the directions in [Can't reach control plane of a cluster with no external endpoint](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/network-isolation#cluster-no-external-endpoint).
     * If connecting from Cloud Shell, follow the directions in [Using Cloud Shell to access a cluster with external endpoint disabled](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation#cloud_shell).



## Error: `kubectl` commands return failed to negotiate an api version

If `kubectl` commands return a `failed to negotiate an API version` error, then you need to ensure `kubectl` has authentication credentials:
    
    
    gcloud auth application-default login
    

## Issue: `kubectl` `logs`, `attach`, `exec`, or `port-forward` command stops responding

If the `kubectl` `logs`, `attach`, `exec`, or `port-forward` commands stop responding, typically the API server is unable to communicate with the nodes.

First, check if your cluster has any nodes. If you've scaled down the number of nodes in your cluster to zero, the commands won't work. To resolve this issue, [resize your cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/resizing-a-container-cluster) to have at least one node.

If your cluster has at least one node, then check whether you are using SSH or [Konnectivity proxy](https://kubernetes.io/docs/concepts/architecture/control-plane-node-communication/#konnectivity-service) tunnels to enable secure communication. The following sections discuss the troubleshooting steps specific to each service:

  * SSH
  * Konnectivity proxy



### Troubleshoot SSH issues

If you're using SSH, GKE saves an SSH public key file in your Compute Engine project [metadata](https://docs.cloud.google.com/compute/docs/metadata). All Compute Engine VMs using Google-provided images regularly check their project's common metadata and their instance's metadata for SSH keys to add to the VM's list of authorized users. GKE also adds a firewall rule to your Compute Engine network for allowing SSH access from the control plane's IP address to each node in the cluster.

The following settings can cause issues with SSH communication:

  * Your network's firewall rules don't allow for SSH access from the control plane.

All Compute Engine networks are created with a firewall rule called `default-allow-ssh` that allows SSH access from all IP addresses (requiring a valid private key). GKE also inserts an SSH rule for each public cluster of the form `gke-CLUSTER_NAME-RANDOM_CHARACTERS-ssh` that allows SSH access specifically from the cluster's control plane to the cluster's nodes.

If neither of these rules exists, then the control plane can't open SSH tunnels.

To verify that this is the cause of the issue, check whether your configuration has these rules.

To resolve this issue, identify the tag that's on all of the cluster's nodes, then [re-add a firewall rule](https://docs.cloud.google.com/compute/docs/vpc/using-firewalls) allowing access to VMs with that tag from the IP address of the control plane.

  * Your project's common metadata entry for `ssh-keys` is full.

If the project's metadata entry named `ssh-keys` is close to its [maximum size limit](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata#custom_metadata_size_limitations), then GKE isn't able to add its own SSH key for opening SSH tunnels.

To verify that this is the issue, check the length of the list of `ssh-keys`. You can see your project's metadata by running the following command, optionally including the `--project` flag:
        
        gcloud compute project-info describe [--project=PROJECT_ID]
        

To resolve this issue, [delete some of the SSH keys](https://docs.cloud.google.com/compute/docs/connect/restrict-ssh-keys#remove-project-key) that are no longer needed.

  * You have set a metadata field with the key `ssh-keys` on the VMs in the cluster.

The node agent on VMs prefers per-instance SSH keys to project-wide SSH keys, so if you've set any SSH keys specifically on the cluster's nodes, then the control plane's SSH key in the project metadata won't be respected by the nodes.

To verify that this is the issue, run `gcloud compute instances describe VM_NAME` and look for an `ssh-keys` field in the metadata.

To resolve this issue, [delete the per-instance SSH keys](https://docs.cloud.google.com/compute/docs/connect/restrict-ssh-keys#remove-instance-key) from the instance metadata.




### Troubleshoot Konnectivity proxy issues

You can determine whether your cluster uses the Konnectivity proxy by checking for the following system Deployment:
    
    
    kubectl get deployments konnectivity-agent --namespace kube-system
    

If your cluster uses the Konnectivity proxy, the output is similar to the following:
    
    
    NAME                 READY   UP-TO-DATE   AVAILABLE   AGE
    konnectivity-agent   3/3     3            3           18d
    

After you've verified that you're using the Konnectivity proxy, make sure that the Konnectivity agents have the required firewall access and that your network policies are set up correctly.

#### Allow required firewall access

Check that your network's firewall rules allow access to the following ports:

  * **Control plane port** : On cluster creation, Konnectivity agents establish connections to the control plane on port 8132. When you run a `kubectl` command, the API server uses this connection to communicate with the cluster. Make sure you allow Egress traffic to the cluster control plane on port 8132 (for comparison, the API server uses 443). If you have rules that deny egress access, you might need to modify the rules or create exceptions.
  * **`kubelet` port**: Because Konnectivity agents are system Pods deployed on your cluster nodes, ensure that your firewall rules allow the following types of traffic:

    * Incoming traffic to your workloads at port 10250 from your Pod ranges.
    * Outgoing traffic from your Pod ranges.

If your firewall rules don't permit this type of traffic, [modify your rules](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/disable-kubelet-readonly-port#modify-firewalls).




#### Adjust network policy

The Konnectivity proxy might have issues if your cluster's [network policy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy) does either of the following:

  * _Blocks ingress_ from the `kube-system` namespace to the `workload` namespace
  * _Blocks egress_ to the cluster control plane on port 8132



When ingress is blocked by the network policy of workload Pods, the `konnectivity-agent` logs include an error message similar to the following:
    
    
    "error dialing backend" error="dial tcp POD_IP_ADDRESS:PORT: i/o timeout"
    

In the error message, `POD_IP_ADDRESS` is the IP address of the workload Pod.

When egress is blocked by network policy, the `konnectivity-agent` logs include an error message similar to the following:
    
    
    "cannot connect once" err="rpc error: code = Unavailable desc = connection error: desc = "transport: Error while dialing: dial tcp CP_IP_ADDRESS:8132: i/o timeout
    

In the error, `CP_IP_ADDRESS` is the cluster control plane's IP address.

These features are not required for the correct functioning of the cluster. If you prefer to keep your cluster's network locked down from all outside access, be aware that features like these won't work.

To verify that network policy ingress or egress rules are the cause of the issue, find the network policies in the affected namespace by running the following command:
    
    
    kubectl get networkpolicy --namespace AFFECTED_NAMESPACE
    

To resolve the issue with the ingress policy, add the following to the `spec.ingress` field of the network policies:
    
    
    ingress:
    - from:
      - namespaceSelector:
          matchLabels:
            kubernetes.io/metadata.name: kube-system
        podSelector:
          matchLabels:
            k8s-app: konnectivity-agent
    

To resolve the issue with the egress policy, add the following to the `spec.egress` field of the network policies:
    
    
    egress:
    - to:
      - ipBlock:
          cidr: CP_IP_ADDRESS/32
      ports:
      - protocol: TCP
        port: 8132
    

If your network policy uses a combination of ingress and egress rules, then consider adjusting both.

#### Adjust the IP masquerade agent

The cluster control plane accepts the traffic from the Konnectivity agents if the source IP address is in the Pod IP address ranges. If you modify the configuration of [ip-masq-agent](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ip-masquerade-agent) to masquerade the source IP address for the traffic to the cluster control plane, the Konnectivity agents might experience connectivity errors.

To resolve the issue and to help ensure that traffic from Konnectivity agents to the cluster control plane are not masqueraded to the node IP address, add the control plane IP address to the `nonMasqueradeCIDRs` list in the `ip-masq-agent` ConfigMap:
    
    
    nonMasqueradeCIDRs:
    - CONTROL_PLANE_IP_ADDRESS/32
    

For more information about this configuration, see [IP masquerade agent](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ip-masquerade-agent).

## Error: `kubectl` commands fail with no agent available error

When you run `kubectl` commands that need to connect from the GKE control plane to a Pod—for example, `kubectl exec`, `kubectl logs`, or `kubectl port-forward`—the command might fail with error messages similar to the following:
    
    
    Error from server: error dialing backend: No agent available
    
    
    
    failed to call webhook: Post "https://WEBHOOK_SERVICE.WEBHOOK_NAMESPACE.svc:PORT/PATH?timeout=10s": No agent available
    
    
    
    v1beta1.metrics.k8s.io failed with: failing or missing response from https://NODE_IP:10250/apis/metrics.k8s.io/v1beta1: Get "https://NODE_IP:10250/apis/metrics.k8s.io/v1beta1": No agent available
    

These errors indicate a problem with Konnectivity, the secure communication tunnel between the GKE control plane and your cluster's nodes. In particular, it means the `konnectivity-server` on the control plane cannot connect to any healthy `konnectivity-agent` Pods in the `kube-system` namespace.

To resolve this issue, try the following solutions:

  1. Verify the health of the `konnectivity-agent` Pods:

     1. Check if the `konnectivity-agent` Pods are running:
            
            kubectl get pods -n kube-system -l k8s-app=konnectivity-agent
            

The output is similar to the following:
            
            NAME                                   READY   STATUS    RESTARTS  AGE
            konnectivity-agent-abc123def4-xsy1a    2/2     Running   0         31d
            konnectivity-agent-abc123def4-yza2b    2/2     Running   0         31d
            konnectivity-agent-abc123def4-zxb3c    2/2     Running   0         31d
            

Review the value in the `Status` column. If the Pods have a status of `Running`, review logs for connection issues. Otherwise, investigate why the Pods aren't running.

     2. **Review logs for connection issues**. If the Pods have a status of `Running`, check logs for connection issues. Because the `kubectl logs` command depends on Konnectivity, use Logs Explorer in the Google Cloud console:

        1. In the Google Cloud console, go to **Logs Explorer**.

[Go to Logs Explorer](https://console.cloud.google.com/logs)

        2. In the query pane, enter the following query.
               
               resource.type="k8s_container"
               resource.labels.cluster_name="CLUSTER_NAME"
               resource.labels.namespace_name="kube-system"
               labels."k8s-pod/k8s-app"="konnectivity-agent"
               resource.labels.container_name="konnectivity-agent"
               

Replace `CLUSTER_NAME` with the name of your cluster.

        3. Click **Run query**.

        4. Review the output. When you review the `konnectivity-agent` logs, look for errors indicating why the agent can't connect. Authentication or permission errors often point to a misconfigured webhook blocking token reviews. "Connection refused" or "timeout" errors typically mean a firewall rule or Network Policy is blocking traffic to the control plane on TCP port 8132, or is blocking traffic between the Konnectivity agent and other nodes. Certificate errors suggest that a firewall or proxy is inspecting and interfering with the encrypted TLS traffic.

     3. **Investigate why the Pods aren't running**. If Pods have a status of `Pending` or another non-running state, investigate the cause. The `konnectivity-agent` runs as a Deployment, not a DaemonSet. Because it runs as a Deployment, the agent Pods only need to run on a subset of nodes. However, if that specific subset of nodes is unavailable, the entire service can fail.

Common causes of a non-running Pod include the following:

        * Custom node taints that prevent a Pod from being scheduled.
        * Insufficient node resources (CPU or memory).
        * Restrictive Binary Authorization policies that block GKE system images.

To get more details about why a specific Pod isn't running, use the `kubectl describe` command:
    
    kubectl describe pod POD_NAME -n kube-system
    

Replace `POD_NAME` with the name of the Pod that isn't running.

  2. Investigate your admission webhooks to ensure none are blocking `TokenReview` API requests. The `konnectivity-agent` relies on service account tokens, so interference with token reviews can prevent agents from connecting. If a webhook is the cause, Konnectivity _cannot_ recover until the faulty webhook is removed or repaired.

  3. Ensure your firewall rules allow TCP egress traffic from your GKE nodes to the control plane's IP address on port 8132. This connection is required for the `konnectivity-agent` to reach the Konnectivity service. For more information, see Allow required firewall access.

  4. Make sure that there are no [Network Policy rules](https://kubernetes.io/docs/concepts/services-networking/network-policies/) that restrict essential Konnectivity traffic. Network Policy rules should allow both intra-cluster traffic (Pod-to-Pod) within the `kube-system` namespace and egress traffic from the `konnectivity-agent` Pods to the GKE control plane.




## Troubleshoot `kubectl` client-side throttling

**Symptom:**

You might experience client-side throttling when using `kubectl`, with error messages that contain the following: `...Throttling request took 1.002582473s, request: GET:...` or `Waited for 1.183040416s due to client-side throttling, not priority and fairness, request: GET: ...`.

**Cause:**

When you run a `kubectl` command, it first caches a list of resources from the API server. This list corresponds to the Custom Resource Definitions (CRDs) available from the API server.

When a GKE cluster has a large number of CRDs, for example 300 or more, `kubectl` sends a large number of requests to the API server to build or refresh its cache. To avoid overloading the API server, `kubectl` throttles itself.

**Resolution:**

These types of throttling error messages are expected behavior and are caused by client-side throttling on the `kubectl` side. This issue should resolve on its own.

## What's next

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
