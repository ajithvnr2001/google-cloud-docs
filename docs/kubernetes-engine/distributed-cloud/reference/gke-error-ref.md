---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/gke-error-ref/
title: Errors for Google Distributed Cloud software \u00a0|\u00a0 GKE On-Prem API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:22.996872+00:00
---

# Errors for Google Distributed Cloud software  |  GKE On-Prem API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/gke-error-ref/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ GKE On-Prem API ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api-overview)



Send feedback 

#  Errors for Google Distributed Cloud software Stay organized with collections  Save and categorize content based on your preferences. 

This is an error catalog for Google Distributed Cloud software only products, bare metal and VMware.

Each error entry consists of the following information:

  * Error ID: a short, unique identifier in the format E######, where ###### is a unique number.

  * Error title: a brief human-readable description for the error.

  * Error description: detailed information to help you troubleshoot and resolve the cause of the error.




## E000000: Kubeconfig File Not Specified

The `bmctl` command is executed without specifying the kubeconfig file.

To proceed, ensure that you provide the kubeconfig file by using the `--kubeconfig` flag.

Example:
    
    
    bmctl [command] --kubeconfig [kubeconfig-file]
    

## E000001: Invalid Kubeconfig File

The provided kubeconfig file isn't in regular file mode.

Ensure that you specify a valid kubeconfig file and try again.

## E000002: `Bootstrap.Run` Function Already Called

The `Bootstrap.Run` function executes the workflow to initialize logging directories and files and possibly create a bootstrap cluster if necessary.

This function is designed to be called only once during the execution of the `bmctl` command to prevent the creation of multiple bootstrap clusters.

This error occurs if the `Bootstrap.Run` function is invoked more than once, which isn't the intended behavior.

Wait for any existing `bmctl` processes to complete and try the operation again.

## E000003: No Matching Region or Zone Found

Check that the location provided in `spec.clusterOperations.location` in the cluster configuration file exists in your Google Cloud project.

You can find a list of all regions and zones in your project by running the following command:
    
    
    gcloud compute regions list
    

If the region or zone you provided exists in your project, make sure that you're using the correct capitalization. Regions and zones are case-sensitive.

## E000004: Secret Stored in Incorrect Namespace

For example, the returned error message might state:
    
    
    The secret 'x' should be stored in the namespace 'y'.
    Please remove 'x' from the path "p" in the configuration file of cluster 'c'.
    

To resolve this issue, remove the secret referenced in the wrong namespace from the cluster configuration file.

## E000005: HTTP Status Code Mismatch

Unexpected HTTP status code is returned while attempting to access the Google Cloud API or Google Container Registry API.

Ensure that your proxy configuration is correctly set up correctly with your Proxy URL, if applicable.

Ensure that a service account key is provided by doing one of the following:

  * Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of a file that contains your service account credentials.
  * Run the following command to authenticate with Google Cloud using your default credentials:
        
        gcloud auth application-default login
        




For more information, see <https://cloud.google.com/docs/authentication#adc>.

Check service account at Google Cloud console -> IAM & Admin -> Service Accounts. If your service account key has expired, update it by following the instructions outlined at <https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/update-secrets>.

Check the roles and permissions for the service account and try again. For information about the Google Cloud resources that you need to create and configure, see <https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/installing/configure-sa>.

## E000006: Can't Manage User Cluster Without Admin Cluster's Kubeconfig

We can't manage a user cluster without the admin cluster's kubeconfig path. The admin cluster's kubeconfig path is required for managing user clusters.

To resolve this error, ensure that you provide the admin cluster's kubeconfig path using the `--kubeconfig` flag when managing user clusters.

This ensures that necessary authentication and permissions are properly configured for managing the user cluster.

## E000007: Version Mismatch

The version specified under `spec.anthosBareMetalVersion` in the cluster configuration file doesn't match the `bmctl` binary version used to manage the cluster.

To resolve this error:

  * Update the `bmctl` binary to the appropriate version that matches the version of the cluster.
  * For upgrades, update the version specified in the cluster configuration to reflect the `bmctl` binary version.



## E000008: ClusterOperations Configuration Not Specified

The ClusterOperations configuration is required for a cluster.

Ensure that the ClusterOperations configuration is properly defined for the cluster under `spec.clusterOperations` in the cluster configuration file.

## E000009: ProjectID in ClusterOperations Not Specified

The ProjectID field is empty in the ClusterOperations configuration. The ProjectID is required for managing cluster operations.

Ensure that the ProjectID is properly defined under `spec.clusterOperations.projectID` in the cluster configuration file.

## E000010: Location in ClusterOperations Not Specified

The Location field is empty in the ClusterOperations configuration. Location is required for managing cluster operations.

Ensure that the location is properly defined under `spec.clusterOperations.location` in the cluster configuration file.

## E000011: Can't Use Service Account while Using Access Token

If your cluster is created using an access token, the specified service account key paths in the cluster configuration file need to be removed.

Ensure that:

  1. The environment variable `GCP_ACCESS_TOKEN_X` is set.
  2. Service account key paths referenced in the cluster configuration file are removed.



## E000012: Can't Use Service Account while Using Access Token

If your cluster is created using a service account key, ensure that:

  1. The environment variable `GCP_ACCESS_TOKEN_X` isn't set.
  2. All required service account key paths are set in the cluster configuration file.



## E000013: Bypass Google Cloud Preflight Failures Without `--force`

The flag `--bypass-gcp-preflight-errors` must be set together with `--force`.

Ensure both flags are used together to proceed.

## E000014: Docker Container Runtime Not Supported

The Docker container runtime is no longer supported.

Set the container runtime to `containerd` under `spec.nodeConfig.containerRuntime` in your cluster configuration file.

## E000015: Unenabled APIs

Some required APIs aren't enabled in your project.

Ensure that all required APIs are enabled in your project to proceed. For more information, see <https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/installing/configure-sa>.

## E000016: Kubeconfig File Stat Error

The provided kubeconfig file doesn't exist or is inaccessible.

Ensure that the kubeconfig file exists and the`bmctl` command has the necessary permissions to access it.

## E000017: IPV4 Forwarding Not Enabled

IPv4 forwarding isn't enabled on the admin workstation. IPv4 forwarding must be enabled.

To resolve this error, follow these steps:

  1. Ensure that the file `/proc/sys/net/ipv4/ip_forward` exists.
  2. Run the following command to enable IPv4 forwarding:


    
    
    echo '1' > /proc/sys/net/ipv4/ip_forward
    

## E000018: Unable to Parse Config File

We couldn't parse the configuration file for the cluster. Several problems might cause this issue.

Ensure that the configuration file `bmctl-workspace/[cluster-name]/[cluster-name].yaml` exists and that the `bmctl` command has the necessary permissions to access it.

Check configuration file for any syntax errors or missing fields.

Make sure to follow the correct format and structure if you need to update the configuration file. Form more information, see <https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/reference/cluster-config>.

## E000019: Control Plane Load Balancer Job Not Finished

This indicates that an error occurred while waiting for the control plane or load balancer jobs to finish.

Check the status of the control plane or load balancer jobss of your cluster:
    
    
    kubectl describe jobs -A
    

For more information about the specific error, review the wrapped error returned by the command.

## E000020: Unable to Create HTTP Client

We couldn't create an HTTP client to ensure that your workstation has reachability to Google Cloud APIs and the Container Registry.

Ensure that your proxy configuration is correctly set up with your Proxy URL if applicable.

## E000021: Unable to Reach Google APIs

We couldn't verify connectivity to the Google Cloud API or the Google Container Registry API.

Your workstation must be able to reach Google Cloud APIs and the Container Registry for proper operation.

Ensure that a service account key is provided by doing one of the following:

  * Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of a file that contains your service account credentials.
  * Run the following command to authenticate with Google Cloud using your default credentials:
        
        gcloud auth application-default login
        




For more information, see <https://cloud.google.com/docs/authentication#adc>.

Check service account at Google Cloud console -> IAM & Admin -> Service Accounts. If your service account key has expired, update it by following the instructions outlined at <https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/update-secrets>.

Check the roles and /permissions for the service account and try again. For information about the Google Cloud resources that you need to create and configure, see <https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/installing/configure-sa>.

## E000022: Unable to Parse Cluster Version

We couldn't parse the version from the cluster configuration file.

To resolve this error, ensure that the version specified under `spec.anthosBareMetalVersion` in the cluster configuration file is valid and follows the expected format.

## E000023: GKE Membership Client Error

We couldn't get the client for establishing GKE hub membership registration.

GKE membership is required if GKE connect is configured under `spec.gkeConnect` in your cluster configuration file.

Ensure that `gcpAccessToken` or `gkeConnectAgentServiceAccountKeyPath` is specified in your cluster configuration file.

## E000024: Unable to Create GKE Registration Check

We couldn't create a new GKE registration check.

This check is essential to verify that:

  * A GKE Connect registration doesn't already exist.
  * Your service account has enough permissions to perform mutation to GKE connect registration.



Ensure that there is no existing GKE connect membership for your cluster at Google Cloud console -> Kubernetes Engine -> Clusters. If a membership already exists for your cluster, do one of the following:

  * Choose a different cluster name.
  * Unregister the existing cluster from the Google Cloud console or run:
        
        gcloud container hub memberships unregister <CLUSTER_NAME> --gke-cluster=<LOCATION>/<CLUSTER_NAME>
        

Reference: https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/unregister




For more information about the specific error, review the wrapped error returned by the command.

## E000025: GKE Registration Check Failure

This indicates that a failure happened while performing the GKE registration check.

This check is essential to verify theat following:

  * A GKE Connect registration doesn't already exist.
  * Your service account has enough permission to perform mutation to GKE connect registration.



Ensure that there is no existing GKE connect membership for your cluster at Google Cloud console -> Kubernetes Engine -> Clusters. If a membership already exists for your cluster, do one of the following:

  * Choose a different cluster name.
  * Unregister the existing cluster from the Google Cloud console or run:
        
        gcloud container hub memberships unregister <CLUSTER_NAME> --gke-cluster=<LOCATION>/<CLUSTER_NAME>
        




Reference: https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/unregister

For more information about the specific error, review the wrapped error returned by the command.

## E000026: Unable to Retrieve Google Default Credentials

We couldn't retrieve Google Default Credentials. For information about, see <https://cloud.google.com/docs/authentication/production#automatically>.

For more information about the specific error, review the wrapped error returned by the command.

## E000027: Google Cloud Permission Denied

This indicates that the request to Google Cloud API was denied.

Ensure that a service account key is provided by doing one of the following:

  * Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of a file that contains your service account credentials.
  * Run the following command to authenticate with Google Cloud using your default credentials:
        
        gcloud auth application-default login
        




For more information, see <https://cloud.google.com/docs/authentication#adc>.

Check service account at Google Cloud console -> IAM & Admin -> Service Accounts. If your service account key has expired, update it by following the instructions outlined at <https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/update-secrets>.

Check the roles and /permissions for the service account and try again. For information about the Google Cloud resources that you need to create and configure, see <https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/installing/configure-sa>.

## E000028: Invalid Service Account Key

The service account key used for Google Default Credentials is invalid.

Check service account at Google Cloud console -> IAM & Admin -> Service Accounts. If your service account key has expired, update it by following the instructions outlined at <https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/update-secrets>.

For more information about the specific error, review the wrapped error returned by the command.

## E000029: Insufficient Permission to Google Cloud

We couldn't communicate with theto Google Cloud API due to insufficient permissions. A valid service account key is needed for successful communication.

Ensure that a service account key is provided by doing one of the following:

  * Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of a file that contains your service account credentials.
  * Run the following command to authenticate with Google Cloud using your default credentials:
        
        gcloud auth application-default login
        




For more information, see <https://cloud.google.com/docs/authentication#adc>.

Check service account at Google Cloud console -> IAM & Admin -> Service Accounts. If your service account key has expired, update it by following the instructions outlined at <https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/update-secrets>.

Check the roles and /permissions for the service account and try again. For information about the Google Cloud resources that you need to create and configure, see <https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/installing/configure-sa>.

## E000030: Unable to Create Compute Service

We couldn't create a compute service to retrieve information about your zone or location from your Google Cloud project, which is necessary to perform check against the location specified under spec.clusterOperations.location in your cluster configuration.

For more information about the specific error, review the wrapped error returned by the command.

## E000031: Unable to Create Service Account Check

We couldn't create a Service Account Check.

The service account key file specified in the cluster configuration file under `cloudOperationsServiceAccountKeyPath` is used to create a service account check.

Ensure that the service account file exists and that it's valid.

Check service account at Google Cloud console -> IAM & Admin -> Service Accounts. If your service account key has expired, update it by following the instructions outlined at <https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/update-secrets>.

For more information about the specific error, review the wrapped error returned by the command.

## E000032: Service Account Check Failure

This indicates that a failure happened while performing the Service Account Check.

This check runs validations against the service account key file referenced in the configuration file of cluster under cloudOperationsServiceAccountKeyPath.

Ensure that:

  * The `projectID` is valid. For more information see <https://cloud.google.com/resource-manager/docs/creating-managing-projects#before_you_begin>.
  * The service account key file exists and it is valid.



Check service account key at Google Cloud console -> IAM & Admin -> Service Accounts. If the service account key has expired, update it by following the instructions outlined at <https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/update-secrets>.

  * The permissions and APIs listed in <https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/installing/configure-sa> are enabled. For mapping, see <https://cloud.google.com/iam/docs/understanding-roles>.



For more information about the specific error, review the wrapped error returned by the command.

## E000033: Unable to Set Flag

We couldn't set a flag to a log directory or file.

The `bmctl` command uses the log directory or file to save logs while the command is running.

For more information about the specific error, review the wrapped error returned by the command.

## E000034: Directory Creation Failure

We couldn't create a directory.

This issue typically arises due to insufficient permissions to create directories or the path where the directory is created doesn't exist.

Ensure that you have the necessary permissions to create directories and the specified location exists.

For more information about the specific error, review the wrapped error returned by the command.

## E000035: Container Registry Permission Validation Failure

We encountered a failure while performing the Container Registry Permission Validation.

The service account key file referenced in the configuration file of cluster under `gcrServiceAccountKey` is used to run validations.

Ensure that the service account key file exists and it is valid. Check service account key at Google Cloud console -> IAM & Admin -> Service Accounts. If the service account key has expired, update it by following the instructions outlined at <https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/update-secrets>.

For more information about the specific error, review the wrapped error returned by the command.

To ignore validation failures, use the `--ignore-validation-errors` flag when running the command.

## E000036: Minimum Kernel Version Required

The validation for your workstation's minimum kernel version failed. Your workstation must meet a minimum kernel version requirement.

Ensure that your kernel version's numeric portion is equal to or greater than `4.15.0`. To check your kernel version, run the following command:
    
    
    uname -r
    

You can also find your kernel details in the file `/proc/version`.

For more information about the specific error, review the wrapped error returned by the command.

## E000037: Unable to Retrieve Service Account Name

We couldn't retrieve the service account needed for workload identity.

Provide one of the following in the cluster configuration file to fix the error:

  * Set the field `spec.gkeConnect.projectID` to your Google Cloud Project ID.
  * Set `baremetal.cluster.gke.io/gcr-service-account` under `metadata.annotations` to the name of the service account.



For more information about the specific error, review the wrapped error returned by the command.

## E000038: Unable to Create Bootstrap Cluster

We couldn't create the bootstrap cluster successfully. A bootstrap cluster is a temporary cluster that hosts the Kubernetes controllers needed to create or upgrade an a self-manage (admin, hybrid, or standalone) cluster.

To fix issues related to bootstrap cluster, consult <https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/troubleshooting/create-upgrade>.

For more information about the specific error, review the wrapped error returned by the command.

## E000039: Bootstrap Cluster Internet Failure

We couldn't verify the Bootstrap cluster Internet Connectivity with the following command:
    
    
    docker exec bmctl-control-plane curl https://oauth2.googleapis.com/$discovery/rest
    

For more information about the specific error, review the wrapped error returned by the command.

## E000040: Unable to Create REST Config from Kubeconfig File

We couldn't create a REST Config from the kubeconfig file. A REST Config is needed to establish a way to communicate with a Kubernetes API server.

Ensure that the provided kubeconfig file exists and is valid.

For more information about the specific error, review the wrapped error returned by the command.

## E000041: Bootstrap Cluster Dependencies Installation Failure

We couldn't apply all needed resources to the bootstrap cluster.

For more information about the specific error, review the wrapped error returned by the command.

## E000042: Bootstrap Cluster External Manifests Installation Failure

We couldn't install the manifests from the directory specified through the flag `--addon-manager-manifests-path`.

Ensure the provided manifests directory exists and valid.

For more information about the specific error, review the wrapped error returned by the command.

## E000043: Unable to Extract Manifest Files

We couldn't extract the manifest files successfully. The manifest files are expected to be extracted into the `.manifests` directory, which is created wherever the bmctl command is invoked.

Ensure that the `bmctl` command has the necessary permissions to create directories and files on your system, and that the `.manifests` directory is successfully created.

For more information about the specific error, review the wrapped error returned by the command.

## E000044: Unable to Create Kubernetes Client

We couldn't create a Kubernetes client to your cluster using the provided kubeconfig file.

Ensure that the kubeconfig file exists and valid.

For more information about the specific error, review the wrapped error returned by the command.

## E000045: Unable to Load Cluster Manifest Profile

The loading process transforms entries from the profile configuration into KusBuild and sets parameters with values from the cluster custom resource. The profile location is determined by the root directory of manifests, the profile name, and the environment.

For more information about the specific error, review the wrapped error returned by the command.

## E000046: Unable to Set Up Workload Identity

We couldn't successfully set up workload identity for your project.

For more information about the specific error, review the wrapped error returned by the command.

## E000047: Unable to Create or Update Debug Options

We couldn't create or update the debug options ConfigMap in the bootstrap cluster based on the flags provided to the `bmctl` command and the cluster configuration file's top section.

This ConfigMap is necessary for debugging purposes and contains relevant configuration data.

For more information about the specific error, review the wrapped error returned by the command.

## E000048: Unable to Create Usage Service

We couldn't create a service usage. This service is essential for accessing Google Cloud service usage APIs, which are necessary for tasks such as verifying that the required APIs are enabled.

For more information about the specific error, review the wrapped error returned by the command.

## E000049: API Enablement Check Failure

This indicates that an error occurred while performing the API enablement check. This ensures that all required APIs are enabled in your project, see <https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/installing/configure-sa>.

To bypass the APIs enablement check failures, use the flag `--skip-api-check`.

For more information about the specific error, review the wrapped error returned by the command.

## E000050: Unable to Perform Object Operation

This indicates that an error occurred while performing a Get, Patch, List, Update, Delete or Apply operation on Kubernetes or custom object.

Ensure that the Kubernetes cluster is accessible and the API server is responsive.

For more information about the specific error, review the wrapped error returned by the command.

## E000051: Unable to Marshal Object

We couldn't marshal an object to YAML format.

For more information about the specific error, review the wrapped error returned by the command.

## E000052: Unable to Generate Secret from Service Account

We couldn't generate the secret `gkeRegisterServiceAccountKey` to be stored in the namespace `gke-register` from the service account key path specified under `gkeRegisterServiceAccountKey` in the cluster configuration file.

Ensure that the specified secret file exists.

For more information about the specific error, review the wrapped error returned by the command.

## E000053: Unable to Read Cluster Configuration File

We couldn't read your cluster configuration file.

Ensure that the cluster configuration file exists and the `bmctl` command has the necessary permissions to access it.

For more information about the specific error, review the wrapped error returned by the command.

## E000054: Unable to Apply Preflight Dependency Resources

We couldn't successfully apply preflight check command dependencies.

For more information about the specific error, review the wrapped error returned by the command.

## E000055: Google Cloud Preflight Checks Failure

The Google Cloud preflight checks failed. Verify the preflight check resources for more details.

Check the preflight check resources:
    
    
    kubectl describe preflightcheck -A
    

To bypass the Google Cloud preflight checks failures, use the flags `--bypass-gcp-preflight-errors` and `--force`.

For more information about the specific error, review the wrapped error returned by the command.

## E000056: Preflight Checks Failure

The preflight checks failed. Verify the preflight check resources for more details.

Check the preflight check resources:
    
    
    kubectl describe preflightcheck -A
    

To bypass the preflight checks failures, use the flag `--force`.

For more information about the specific error, review the wrapped error returned by the command.

## E000057: Unable to Verify Preflight Check Status

We couldn't successfully verify the status of the preflight check resources.

Check the preflight check resources for more details:
    
    
    kubectl describe preflightcheck -A
    

For more information about the specific error, review the wrapped error returned by the command.

## E000058: Kubeconfig Secret Not Ready

This indicates that an error occurred while reading the kubeconfig secret or waiting for it to become ready.

Ensure that the secret `<CLUSTER_NAME>-kubeconfig` exists in the cluster namespace within the bootstrap cluster and the path `.data` isn't empty.

For more information about the specific error, review the wrapped error returned by the command.

## E000059: Unable to Write Kubeconfig File

We couldn't successfully write the kubeconifg file to the path `bmctl-workspace/<CLUSTER_NAME>/<CLUSTER_NAME>-kubeconfig`.

Ensure that the `bmctl` command has the necessary permissions to write to the directory of the kubeconfig file.

You canmay try resolving this issue by running the `bmctl reset` command and then attempting to create the cluster again.

For more information about the specific error, review the wrapped error returned by the command.

## E000060: Cluster Not Ready

This indicates that an error occurred while waiting for your cluster to become ready.

Check the status of your cluster for more details:
    
    
    kubectl describe cluster <CLUSTER_NAME> -A
    

For more information about the specific error, review the wrapped error returned by the command.

## E000061: NodePool Not Ready

This indicates that an error occurred while waiting for the node pools to become ready.

Check the status of the node pools:
    
    
    kubectl describe nodepool -A
    

For more information about the specific error, review the wrapped error returned by the command.

## E000062: SecretForwarder Not Ready

This indicates that an error occurred while waiting for the SecretForwarders to become ready.

Check the status of the SecretForwarders:
    
    
    kubectl describe secretforwarder -A
    

For more information about the specific error, review the wrapped error returned by the command.

## E000063: Unable to Convert Unstructured Object to Concrete Type

We couldn't convert an unstructured object to a concrete type.

For more information about the specific error, review the wrapped error returned by the command.

## E000064: Cluster API Provider Installation Failure

We couldn't verify the installation of the cluster API provider in the admin cluster.

To troubleshoot, log into the bootstrap cluster and check the `lifecycle-controllers-deployer` job and `lifecycle-controller-manager` pod logs.

For more information about the specific error, review the wrapped error returned by the command.

## E000065: Unable to Pivot

We couldn't successfully pivot the resources from the bootstrap cluster to the actual cluster.

For more information about the specific error, review the wrapped error returned by the command.

## E000066: Unable to Apply Resource

This indicates that an error occurred while applying a resource. This resource may be a customer resource specified in the cluster configuration file.

Ensure that every customer-specified resource is correctly formatted and valid.

For more information about the specific error, review the wrapped error returned by the command.

## E000067: Unable to Create Command

We couldn't create a placeholder command with the specified flags to be consumed by `bmctl` internal command.

For more information about the specific error, review the wrapped error returned by the command.

## E000068: Unable to Retrieve GKE Version

We couldn't retrieve the GKE version based on the cluster version specified with `spec.anthosBareMetalVersion` in the cluster configuration file.

For more information about the specific error, review the wrapped error returned by the command.

## E000069: Cluster Already at target Version

This indicates that the cluster is already at the target version. Ensure that the specified version under `spec.anthosBareMetalVersion` in the cluster configuration file is greater than the current cluster version try again.

## E000070: Cluster and NodePools Already at target Version

This indicates that both the cluster and its node pools are already at the target version. Ensure that the specified version under `spec.anthosBareMetalVersion` in the cluster configuration file of is greater than the current version and try again.

## E000071: Insufficient IP Addresses in CIDR

This indicates that the bootstrap cluster pod CIDR range doesn't have enough IP addresses to accommodate for the nodes.

Make sure to provide a CIDR range with the flag `--bootstrap-cluster-pod-cidr` that has sufficient IP addresses for the nodes.

For more information about the specific error, review the wrapped error returned by the command.

## E000072: Preview Feature Upgrade Policy Validation Failure

We couldn't validate that the supported enabled preview features specified in the cluster meet the requirements for upgrade.

For more information about the specific error, review the wrapped error returned by the command.

## E000073: Unable to Register Bootstrap to GKE Connect Membership

We couldn't register the bootstrap cluster to GKE Hub membership.

Ensure that there is no existing GKE connect membership for your bootstrap cluster name (either chosen by default or provided with the flag `--bootstrap-cluster`) at Google Cloud console -> Kubernetes Engine -> Clusters in your project.

If a membership already exists with the cluster name, do one of the following:

  * Provide a different name with the flag `--bootstrap-cluster`
  * Unregister the existing cluster from the Google Cloud console or run:
        
        gcloud container hub memberships unregister <CLUSTER_NAME>
        




For more information about the specific error, review the wrapped error returned by the command.

## E000074: Unable to Create Secret from Service Account

We couldn't create a secret using a service account file specified under in the cluster configuration file.

Ensure that the file exists and is accessible.

For more information about the specific error, review the wrapped error returned by the command.

## E000075: Unable to Retrieve GKE Hub URL

We couldn't to extract the GKE Hub endpoint URL.The GKE Hub endpoint is the URL endpoint used for GKE Hub API requests.

For more information about the specific error, review the wrapped error returned by the command.

## E000076: Upgrade Not Complete

An error occurred while waiting for the upgrade to complete successfully. For an upgrade to be determined complete, the cluster and the node pools must be at the target version.

Check the status of the node pools and the cluster:
    
    
    kubectl describe nodepool -n <NAMESPACE> --kubeconfig <KUBECONFIG_FILE>
    
    
    
    kubectl describe cluster -n <NAMESPACE> --kubeconfig <KUBECONFIG_FILE>
    

For more information about the specific error, review the wrapped error returned by the command.

## E000077: Unable to Create Workload Identity Stackdriver Secret

We couldn't create the workload identity stackdriver secret.

For more information about the specific error, review the wrapped error returned by the command.

## E000078: Unable to Bump NodePool Version

We couldn't bump the NodePool resource current version to the target version.

For more information about the specific error, review the wrapped error returned by the command.

## E000079: Unable to Bump Cluster Version

We couldn't bump the cluster resource current version to the target version.

Ensure that the target version is greater than the current version and is valid.

For more information about the specific error, review the wrapped error returned by the command.

## E000080: Unable to Update Kubeconfig Secret

We couldn't update the kubeconfig secret for your cluster.

For more information about the specific error, review the wrapped error returned by the command.

## E000081: Missing Secret Key

This indicates that the secret resource does not contain a specific key.

For more information about the specific error, review the returned error from the command.

## E000082: Unable to Print Upgrade Result

We couldn't print the cluster upgrade result.

Check the `BaremetalMachine` resources for any nodes that failed to upgrade:
    
    
    kubectl describe baremetalmachines -n <NAMESPACE> --kubeconfig <KUBECONFIG_FILE>
    

For more information about the specific error, review the wrapped error returned by the command.

## E000083: Missing GKEConnect Specification

The GKEConnect specification is not specified in the cluster configuration.

Ensure that the field `spec.gkeConnect` is provided in the cluster configuration file.

## E000084: Unable to Create Connect Agent Connectivity Check

We couldn't create a new Connect Agent connectivity check.

For more information about the specific error, review the returned error from the command.

## E000085: Connect Agent Connectivity Check Failure

An error occurred while performing the Connect Agent connectivity check.

For more information about the specific error, review the returned error from the command.

## E000086: Unable to Retrieve Custom Resource With Group Version Kind

This indicates that an error occurred while retrieving a custom resource using GroupVersionKind.

For more information about the specific error, review the wrapped error returned by the command.

## E000087: Unable to Construct Private Registry Configuration from Private Registry

We couldn't construct the registry configuration based on the cluster credential settings specified under `privateRegistries` in the cluster configuration file.

Ensure that the provided configuration under `privateRegistries` in the cluster configuration file is valid and try again.

For more information about the specific error, review the wrapped error returned by the command.

## E000088: Unable to Construct Private Registry Configuration from Registry Mirror

We couldn't construct the registry configuration based on the cluster credential settings specified under `registryMirrors` in the cluster configuration file.

Ensure that the provided configuration under `registryMirrors` in the cluster configuration file is valid and try again.

For more information about the specific error, review the wrapped error returned by the command.

## E000089: Unable to Update Node Access

This indicates that an error occurred while updating node access.

For more information about the specific error, review the wrapped error returned by the command.

## E000090: Unable to Calculate Diff in bmctl update

This indicates that an error occurred while calculating the diff between the YAML cluster configuration file and the live configuration in the cluster during `bmctl update` command.

As a workaround, you can run `bmctl get config` to get the live configuration in the cluster and perform the diff with the YAML cluster configuration file manually outside of `bmctl`.

For more information about the specific error, review the wrapped error returned by the command.

## E000091: Invalid Input to Console Prompt

Invalid input provided to the console prompt.

Enter `yes` or `no`.

For more information about the specific error, review the wrapped error returned by the command.

## E000092: Failed to create cluster specific namespace

As one of the first steps for cluster creation, we create a namespace specific to the new cluster. Almost all resources of the new cluster stored in this namespace.

This error denotes that the attempt to ensure that such a cluster specific namespace exists (either by creating a new namespace or by simply checking it's existence) failed.

For more information about the specific error, review the wrapped error returned by the command.

## E000097: Cluster Is Paused

This error indicates that an operation cannot proceed because the target cluster has the `cluster.x-k8s.io/paused` annotation.

To resolve this, either unpause the cluster by removing the annotation or use the `--skip-paused-annotation-check` flag to bypass this check.

For more information about the specific error, review the wrapped error returned by the command.

## E300000: Orphan Container(s) Detected

This indicates that we have detected orphan containers on a node through Node Problem Detector.

Orphan containers refer to container processes that are no longer actively running or functional but still persist in a partially cleaned-up or inconsistent state.

To view the full log, execute the following on the node in question:

`journalctl -u node-problem-detector`

Use the details of the orphan containers from the error message to retrieve the container IDs.

Use the following commands to remove the orphan containers from the node:

`crictl stop <container-id>`

`crictl rm <container-id>`

If the preceding commands don't remove the orphan containers, then the process of each container needs to be stopped. The following commands can be used to retrieve the process ID or PID of each container and stop it.

`crictl inspect <container-id> | grep pid`

`kill -9 <pid>`

## What's next?

If you've followed the guidance for corrective action and an error persists, [contact technical support](https://docs.cloud.google.com/support/docs#contacting_technical_support).

For more information to troubleshoot cluster problems, see the following resources:

**Google Distributed Cloud for bare metal**

  * [Known issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues)
  * [Understand the impact of failures in Google Distributed Cloud](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/failure-mode-analysis)



**Google Distributed Cloud for VMware**

  * [Known issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/known-issues)
  * [Diagnose cluster issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
