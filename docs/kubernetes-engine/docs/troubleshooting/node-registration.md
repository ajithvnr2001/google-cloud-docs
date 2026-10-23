---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/node-registration/
title: Troubleshoot node registration \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:25:01.430806+00:00
---

# Troubleshoot node registration  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/node-registration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Troubleshoot node registration Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

When a new node joins your Google Kubernetes Engine (GKE) Standard cluster, it must register with the control plane to receive workloads. If this process fails, the node won't be usable, which can prevent your cluster from creating, repairing, or scaling correctly.

Use this page to resolve issues that prevent node registration. Learn about the prerequisites for successful node registration, how to use the Node Registration Checker utility to find failures, and manual troubleshooting steps for network, resource, and permission issues.

This information is primarily for Platform admins and operators who are responsible for managing and scaling the node infrastructure of GKE Standard clusters. It can also be useful for Application developers who need to understand why a cluster might not be scaling up to meet their application's resource demands. For more information about the common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

For resolving issues with GKE Autopilot clusters, refer to [Troubleshooting Autopilot clusters](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/troubleshooting-autopilot-clusters).

## About node registration

[Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#nodes) are Compute Engine VM instances that GKE creates on your behalf. When a new node is added to a GKE cluster, it must be registered with the cluster's control plane. This process, called _node registration_ or _node bootstrapping_ , occurs when a node is created.

#### When node registration occurs

Node registration occurs whenever nodes are created, including the following scenarios:

  * You create a cluster.
  * You [create a node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools#add).
  * GKE creates a node pool with [node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning).
  * [Cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler) scales up the cluster.
  * You [resize the cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/resizing-a-cluster).
  * [Node auto-repair](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-repair) creates a new node.



The node registration process follows these steps:

  1. The node count set for the node pool is replicated to the managed instance groups (MIGs).
  2. The MIGs create the required number of VM instances.
  3. For each VM instance that is created:

     1. The VM instance boots.
     2. The VM instance configures and installs the necessary packages to run as a Kubernetes node.
     3. The kubelet now running on the VM instance communicates with the control plane's API server to register as a node.



## Node registration error message

When GKE attempts to add nodes to your cluster, the following error appears in the Google Cloud console if node registration failed:
    
    
      All cluster resources were brought up, but: only 0 nodes out of * have
      registered; this is likely due to the Nodes failing to start correctly; try
      re-creating the cluster or contact support if that doesn't work.
    

This error message indicates that the nodes did not successfully register with the cluster. The following sections describe some of the potential causes of this error.

## Prerequisites for successful node registration

Successful node registration to a GKE cluster depends on factors such as the following:

  * Network connectivity.
  * Resource availability.
  * Service account permissions.



### Prerequisites for instance creation

When GKE creates a node for your cluster, the first step is creating a new Compute Engine VM instance.

Instance creation might fail for one of the following reasons:

  * [Insufficient quota](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-vm-creation#insufficient_quota)
  * [Resource availability](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-vm-creation#resource_availability)
  * [Insufficient IP address space](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips#not_enough_space)



Failed instance creation means that in the time range during which GKE attempted to create the instance to register as a GKE node, there are missing logs for instance creation as the instances were never created. To check for missing logs, refer to the instructions to find an instance that failed node registration.

### Service account permissions

GKE nodes have an IAM service account associated with them. By default, this service account is the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account). We recommend, to harden your cluster, using a custom IAM service account that has the [minimum required permissions](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#permissions).

This service account needs to have the correct permissions for the VM instances to be initialized as GKE nodes. If you delete the service account, disable it, or don't give it the correct permissions, node registration might fail.

### Prerequisites for network connection to Google APIs and services

The VM instance downloads packages to prepare to run as a GKE node, and a connection timeout might mean that your cluster has not met the networking requirements necessary to connect to Google APIs and services, such as `storage.googleapis.com`. If an instance cannot connect to these services, it cannot download the Kubernetes distribution and complete the node registration process.

Depending on your network connection, allowing this connection might mean [configuring Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#config), or having [firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) and [routes](https://docs.cloud.google.com/vpc/docs/routes) in your cluster's Virtual Private Cloud (VPC) network that allow the connection.

### Prerequisites for network connection with control plane

Connectivity between the control plane and the nodes is critical for node registration and regular function. This communication is allowed by default. Ensure that when putting VPC firewall rules in place, communication is still allowed between the nodes and the control plane.

For more information, refer to [Allow control plane connectivity](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/networking#allow-cp-connectivity).

**Caution:** If you expand the primary IPv4 address range of a subnet used by a Google Kubernetes Engine (GKE) cluster, you must [add the expanded IP address range to the cluster's control plane authorized networks](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation#how_authorized_networks_work).

## Use the Node Registration Checker to troubleshoot node registration

The Node Registration Checker utility runs on newly created instances and checks if the instance has successfully completed the node registration steps.

When node registration fails, the utility generates a summary report where you can see what prerequisites were not met based on where in the process the instance failed.

Use the instructions in the following section to find an instance that failed node registration and use the Node Registration Checker summary to learn why it failed.

### Find an instance that failed node registration

When one or more instances fail to register as nodes with your GKE cluster's control plane, you can see the number of instances that failed from the error message shown in the **Cluster Details** page of the Google Cloud console. When multiple instances fail to register at once, it might be for the same underlying reason. Because of this, you can use one of the failed instances to investigate why all instances failed.

However, because the instances didn't register as GKE nodes, you must use the following instructions to find the names of the underlying Compute Engine VMs that failed to register.

  1. In the Google Cloud console, go to the **Logs Explorer** page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Use the following log filter to find the logs of VM instance creation:
         
         resource.type="gce_instance"
         logName="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity"
         protoPayload.requestMetadata.callerSuppliedUserAgent="GCE Managed Instance Group for GKE"
         protoPayload.response.status="RUNNING"
         

Replace `PROJECT_ID` with the project ID for your cluster.

  3. Use the histogram below the log filter to narrow down the time range to when node creation should have occurred.

  4. Click one of the logs that appear under **Query results** , then click **Expand nested fields** to show more details.

  5. Find the field `protoPayload.resourceName`. The final part of the path listed there is the instance name. Instance names follow a format that starts with the name of the cluster and the name of the node pool, for example:

`gke-cluster-1-default-pool-b0ac62d3-9g1v` is an instance for the `default-pool` node pool in `gke-cluster-1`.

  6. In the Google Cloud console, go to the Compute Engine **VM instances** page:

[Go to VM instances](https://console.cloud.google.com/compute/instances)

Find the name of the VM instance using the filter. Click for more details.




### Troubleshoot an instance with the Node Registration Checker

After you find the name of the instance that failed to register, you can investigate why it failed using the Node Registration Checker.

In the VM instance **Details** tab, in the **Logs** section, click **Serial port 1 (console)**.

The output for newly created instances includes the following, indicating that the Node Registration Checker has started:
    
    
    ** Starting Node Registration Checker **
    ** Loading variables from kube-env **
    ** Sleeping for 7m to allow registration to complete  **
    

If node registration succeeds, the output includes the following messages:
    
    
    ** Node ready and registered. **
    ** Completed running Node Registration Checker **
    

If you don't see these messages, node registration failed and the Node Registration Checker generated a report summarizing why registration failed. Look for the following additional message to see the summary:
    
    
    ** Here is a summary of the checks performed: **
    

Below this message, look for a table similar to the following:
    
    
    ------------------------------
    Service    DNS      Reachable
    ------------------------------
    LOGGING    true     true
    GCR        true     true
    GCS        true     true
    Master     N/A      false
    ------------------------------
    

If `LOGGING`, `GCR`, or `GCS` are listed as not reachable, check the Service account permissions for node registration and Network connection to Google APIs and services for node registration.

If `Master` is listed as not reachable, check the prerequisites for Network connection with control plane for node registration.

After you resolve all issues preventing successful node registration, refer to Complete node registration after fixing the root cause.

If the preceding steps don't tell you why node registration failed, refer to Gather information for further investigation.

## Troubleshoot node registration without the Node Registration Checker

Use these steps only as a last resort if you have already checked the Prerequisites for successful node registration and tried the Node Registration Checker.

**Note:** Some of the following investigation steps require SSH access to the underlying VM instance.

After you resolve all issues preventing successful node registration, complete node registration after fixing the root cause.

If none of the investigation steps on this page tell you why node registration failed, refer to Gather information for further investigation.

### Check service account permissions for node registration

The service account that your nodes use must have the prerequisite permissions for node registration. Use the following instructions to check that you have met these prerequisites:

  1. Find an instance that failed node registration.

  2. In the VM instance **Details** tab, in the **API and identity management** section, find the name of the service account in the **Service account** field. If the node used the Compute Engine default service account, the name follows the format `PROJECT_NUMBER-compute@developer.gserviceaccount.com`. This service account must have the [minimum required permissions](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#use_least_privilege_sa).

  3. Check for indicators of successful registration in the serial console output. In the VM instance **Details** tab, in the **Logs** section, click **Serial port 1 (console)**.

If the instance used a service account with the correct permissions, the output includes the following:

     * `Started Download and install k8s binaries and configurations`
     * `Started Docker Application Container Engine.`
     * `Started Configure kubernetes node.`
     * `Reached target Kubernetes.`

These messages will be found in different places in this output. They may also have timestamps or other artifacts interrupting them, like this: `Starting [0;1;39mConfigure kubernetes node`. If you see all of these messages, the service account prerequisites were met.

If you don't see these messages, the service account assigned to the VM instance might be deleted, be disabled, or not have [the correct permissions](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#permissions).




### Check network connection to Google APIs and services for node registration

#### Check connection with SSH access

If you have [SSH access to VM instances](https://docs.cloud.google.com/compute/docs/instances/access-overview) in your project, you can also check that the VM instance has a network connection to Google APIs and services.

  1. Find an instance that failed node registration.

  2. In the VM instance **Details** tab, click **SSH**.

  3. After you connect to the command line for your VM instance, run the following command to check for connection to Google APIs and services:
         
         curl -m 5 -v https://storage.googleapis.com/generate_204
         

If the connection is successful, the output is similar to the following:
         
         *   Trying 142.250.148.128:443...
         * Connected to storage.googleapis.com (142.250.148.128) port 443 (#0)
         
         ...
         
         < HTTP/1.1 204 No Content
         < Content-Length: 0
         < Cross-Origin-Resource-Policy: cross-origin
         < Date: Wed, 04 Jan 2023 00:58:41 GMT
         <
         * Connection #0 to host storage.googleapis.com left intact
         

If the connection is not successful, the output is similar to the following:
         
         *   Trying 142.250.148.128:443...
         * Connection timed out after 5000 milliseconds
         * Closing connection 0
         curl: (28) Connection timed out after 5000 milliseconds
         

If the connection times out and the IP address returned is within the `199.36.153.0/24` IP address range, check that your cluster has met the [networking requirements](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#config) for connecting to Google APIs and services. If the connection times out and the IP address returned is not within the mentioned IP address range, check for [firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) blocking outgoing traffic or misconfigured [routes](https://docs.cloud.google.com/vpc/docs/routes) in your cluster's VPC network.

Keep the SSH connection to the VM instance open and proceed to the next section.




#### Check connection without SSH access using Connectivity Tests

If you don't have [SSH access to VM instances](https://docs.cloud.google.com/compute/docs/instances/access-overview), use [Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview) to check that the VM instance has a connection to Google APIs and services.

  1. Find an instance that failed node registration.

  2. [Create and Run Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests) with the VM instance as the **Source** and `storage.googleapis.com TCP/443` as the **Destination**.

Use the test results to check your cluster's networking configuration.




### Check network connection with control plane for node registration

If you have [SSH access to VM instances](https://docs.cloud.google.com/compute/docs/instances/access-overview) in your project, you can check whether the VM instance has a networking connection to the cluster's control plane.

  1. Find an instance that failed node registration.

  2. In the VM instance **Details** tab, click **SSH**.

  3. After you connect to the command line for your VM instance, save the cluster's control plane endpoint as an environment variable:
         
         source <(sudo grep KUBERNETES_MASTER_NAME /home/kubernetes/kube-env)
         

  4. Send a `GET` request to the control plane endpoint:
         
         curl -k -m 5  https://${KUBERNETES_MASTER_NAME}/version
         

If the output is similar to the following, then the VM instance can establish a connection with the control plane:
         
         {
         "major": "1",
         "minor": "24",
         "gitVersion": "v1.24.7-gke.900",
         "gitCommit": "e35c4457f66187eff006dda6d2c0fe12144ef2ec",
         "gitTreeState": "clean",
         "buildDate": "2022-10-26T09:25:34Z",
         "goVersion": "go1.18.7b7",
         "compiler": "gc",
         "platform": "linux/amd64"
         }
         

If the output is similar to the following, then the VM instance cannot establish a connection with the control plane:
         
         curl: (28) Connection timed out after 5000 milliseconds
         




If the VM instance cannot establish a connection with the control plane, see the section about allowing control plane connectivity in the [GKE networking best practices](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/networking#allow-cp-connectivity).

## Complete node registration after fixing the root cause

After you resolve the issue that is blocking node registration, how you proceed depends on the context for the failure:

  * If node registration failed on cluster creation, [delete the cluster](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/delete) and try again.
  * If node registration failed during scale up with cluster autoscaler, wait for the VM instances to try and register again.
  * If node registration failed on node pool creation: 
    * If the VM instances were created, wait for the VM instances to try and register again.
    * If the VM instances were not created, [delete the node pool](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/delete) and try again.
  * If node registration failed on cluster resize, re-run the command to [increase the size of your cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/resizing-a-cluster#increase).
  * If node registration failed outside the scope of an operation, such as during a repair operation, wait for the VM instances to try and register again.



### Gather information for further investigation

If you are unable to resolve the node registration issue, you can gather additional information to aid Cloud Customer Care's investigation with the following instructions. These steps require [SSH access to VM instances](https://docs.cloud.google.com/compute/docs/instances/access-overview) in your project and use the `sosreport` utility, which is included in COS images.

  1. Find an instance that failed node registration.

  2. [Collect debugging information using sosreport](https://docs.cloud.google.com/container-optimized-os/docs/how-to/sosreport).

Alternatively, if your nodes don't have the `sosreport` utility downloaded and it cannot be installed, collect debugging information manually by running the following commands:
         
         # Check cloud-init logs for issues during early VM boot
          sudo journalctl -u cloud-init-local --no-pager
          sudo journalctl -u cloud-init --no-pager
          sudo journalctl -u cloud-final --no-pager
          sudo journalctl -u cloud-config --no-pager
         
          # Check kubelet status and logs
          sudo systemctl status kubelet
          sudo journalctl -u kubelet --no-pager
         
          # Check GKE node installation service status and logs
          sudo systemctl status kube-node-installation.service
          sudo journalctl -u kube-node-installation.service --no-pager
         
          # Check GKE node configuration service status and logs
          sudo systemctl status kube-node-configuration.service
          sudo journalctl -u kube-node-configuration.service --no-pager
         

  3. Package this information into a zip file and include it when you [submit a support case to Cloud Customer Care](https://cloud.google.com/support-hub).




## What's next

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
