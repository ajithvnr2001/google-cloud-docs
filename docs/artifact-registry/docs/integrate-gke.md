---
url: https://docs.cloud.google.com/artifact-registry/docs/integrate-gke/
title: Deploying to Google Kubernetes Engine \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:48:27.930244+00:00
---

# Deploying to Google Kubernetes Engine  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/integrate-gke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Deploying to Google Kubernetes Engine Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes how to pull images from Artifact Registry to deploy to Google Kubernetes Engine. If you want to deploy to self-hosted or third-party Kubernetes services, you must configure authentication to Google Cloud before pulling images from Artifact Registry. To authenticate to Google Cloud from Kubernetes workloads outside Google Cloud, see [Configure Workload Identity Federation with Kubernetes](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-kubernetes).

Google Kubernetes Engine can pull images directly from Docker repositories. Some versions include pre-configured support for pulling images from Artifact Registry Docker repositories.

## Requirements

This section describes requirements to integrate with GKE.

### Permissions

GKE uses the following defaults when you create node pools or clusters:

  * The [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) is the identity for nodes.
  * Depending on your organization policy configuration, the default service account might automatically be granted the [Editor role](https://docs.cloud.google.com/iam/docs/roles-overview#basic) on your project. We strongly recommend that you disable the automatic role grant by [ enforcing the `iam.automaticIamGrantsForDefaultServiceAccounts` organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants). If you created your organization after May 3, 2024, this constraint is enforced by default. 

If you disable the automatic role grant, you must decide which roles to grant to the default service accounts, and then [grant these roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) yourself. 

If the default service account already has the Editor role, we recommend that you replace the Editor role with less permissive roles.To safely modify the service account's roles, use [Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/simulate-iam-policies) to see the impact of the change, and then [grant and revoke the appropriate roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

  * Nodes that you create with the default service account have the Compute Engine [default access scopes](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_scopes), including read-only access to storage. You cannot change access scopes on existing nodes.



If you have [disabled granting the basic Editor role](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants), then grant the Compute Engine default service account the Artifact Registry Reader role (`roles/artifactregistry.reader`).

If you use these defaults and grant the Compute Engine default service account the Artifact Registry Reader role (`roles/artifactregistry.reader`), then GKE can pull images from Artifact Registry repositories in the same Google Cloud project. If you need to push images from nodes, pull or push images across projects, use a user-provided service account, or have other needs that the default settings don't support, then see the [access control](https://docs.cloud.google.com/artifact-registry/docs/access-control#gke) documentation for information about configuring access.

If you encounter "permission denied" errors, see [4xx errors](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting#gke_service_account_deleted).

### GKE version

The following table lists the minimum required GKE versions to create clusters that have default permissions to pull containers from Docker repositories in the same project.

Version | Minimum required patch  
---|---  
1.14 | 1.14.10-gke.22  
1.15 | 1.15.9-gke.8  
  
If your version of GKE is earlier than the minimum version, you must configure [Kubernetes imagePullSecrets](https://docs.cloud.google.com/artifact-registry/docs/access-control#pullsecrets) to enable GKE to pull images.

If GKE is in a different project than Artifact Registry, [grant](https://docs.cloud.google.com/artifact-registry/docs/access-control#grant) Artifact Registry permissions to the service account that your GKE node use. By default, nodes use the Compute Engine [default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account).

## Running an image

You can run a Artifact Registry image on a Google Kubernetes Engine cluster using the following command:
    
    
    kubectl run [NAME] --image=LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY/IMAGE:TAG
    

**Tip:** If you use [image streaming](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming), you can [prewarm your images](https://docs.cloud.google.com/artifact-registry/docs/prewarm-images) to further reduce cold-start latency.

where:

  * `LOCATION` is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository. 
  * `PROJECT` is your Google Cloud console [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). If your project ID contains a colon (`:`), see [Domain-scoped projects](https://docs.cloud.google.com/artifact-registry/docker/names#domain).
  * `REPOSITORY` is the name of the repository where the image is stored.
  * `IMAGE` is the name of the image in the repository.
  * `TAG` is the tag for the image version that you want to pull.



For more information about Kubernetes commands, see [Overview of kubectl](https://kubernetes.io/docs/reference/kubectl/overview/).

## Troubleshooting containerd node images

Starting with GKE node version 1.19, the default node image for Linux nodes is the Container-Optimized OS with containerd (`cos_containerd`) variant instead of the Container-Optimized OS with Docker (`cos`) variant.

While the Docker binary is available on Linux nodes that use containerd as a runtime, we don't recommend using it. Docker does not manage the containers Kubernetes runs on containerd nodes, thus you cannot use it to view or interact with running Kubernetes containers using Docker commands or the Docker API.

For debugging or troubleshooting on Linux nodes, you can interact with containerd using the portable command-line tool built for Kubernetes container runtimes: `crictl`. `crictl` supports common functionalities to view containers and images, read logs, and execute commands in the containers.

For more information, refer to the [crictl user guide](https://github.com/kubernetes-sigs/cri-tools/blob/master/docs/crictl.md) and the GKE documentation on [containerd](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/using-containerd).

For Windows Server nodes, the containerd daemon runs as a Windows service named `containerd`. Logs are available in the following logs directory: `C:\etc\kubernetes\logs\containerd.log` and are shown in [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface) under `LOG NAME: "container-runtime"`.

**Warning:** Docker cannot view or access containers for Linux and Windows node pools that use containerd as a runtime.

### Pulling from a public Artifact Registry repository

Once you have deployed and image to a GKE cluster with containerd nodes, you can connect to a VM instance using SSH and run `crictl` commands for troubleshooting.

Public Artifact Registry repositories don't require authentication. `crictl` can also be used to pull images in private Artifact Registry repositories.

### Console

  1. In the Google Cloud console, go to the **VM Instances** page.

[Go to VM Instances](https://console.cloud.google.com/compute/instances)

  2. In the list of virtual machine instances, click the arrow next to **SSH** in the row of the instance that you want to connect to. 

![SSH button next to instance name.](https://docs.cloud.google.com/static/artifact-registry/docs/images/establish-ssh-connection-1.png)

**Note:** When you connect to VMs using the Google Cloud console, Compute Engine creates an ephemeral SSH key for you. For more information about SSH keys, see [SSH connections to Linux VMs](https://docs.cloud.google.com/compute/docs/instances/ssh)
  3. Select "Open in browser window" or the connection method of your choice from the drop-down options.

  4. Google Cloud console opens a new terminal window. Use `crictl` to pull an image from Artifact Registry:
         
         crictl pull IMAGE_LOCATION:TAG
         

The output looks like the following:
         
         Image is up to date for sha256:0f25067aa9c180176967b4b50ed49eed096d43fa8c17be9a5fa9bff05933bee5

When you pull an image from an Artifact Registry private repository, you must authenticate to the repository. You can use an access token to provide your credentials.




### gcloud

  1. Ensure that you have the latest version of the Google Cloud CLI
         
         gcloud components update
         

  2. Connect to the VM:
         
         gcloud compute ssh --project=PROJECT_ID \
          --zone=ZONE \
          VM_NAME
         

Replace the following:

     * `PROJECT_ID`: the ID of the project that contains the VM
     * `ZONE`: the name of the zone in which the VM is located
     * `VM_NAME`: the name of the VM

If you have [set default properties](https://docs.cloud.google.com/compute/docs/gcloud-compute#default-properties) for the Google Cloud CLI, you can omit the `--project` and `--zone` flags from this command. For example:
    
    gcloud compute ssh VM_NAME
    

  3. If you have not already created a SSH key, SSH keygen will generate one for you. Enter a passphrase or leave empty when prompted.

  4. Use `crictl` to pull an image from Artifact Registry:
         
         crictl pull IMAGE_LOCATION:TAG
         

  5. The output looks like the following:
         
         Image is up to date for sha256:0f25067aa9c180176967b4b50ed49eed096d43fa8c17be9a5fa9bff05933bee5

When you pull an image from an Artifact Registry private repository, you must authenticate to the repository. You can use an access token to provide your credentials.




### Pulling from a private Artifact Registry repository

### Console

  1. In the Google Cloud console, go to the **VM Instances** page.

[Go to VM Instances](https://console.cloud.google.com/compute/instances)

  2. In the list of virtual machine instances, click the arrow next to **SSH** in the row of the instance that you want to connect to. 

![SSH button next to instance name.](https://docs.cloud.google.com/static/artifact-registry/docs/images/establish-ssh-connection-1.png)

**Note:** When you connect to VMs using the Google Cloud console, Compute Engine creates an ephemeral SSH key for you. For more information about SSH keys, see [SSH connections to Linux VMs](https://docs.cloud.google.com/compute/docs/instances/ssh)
  3. Select "Open in browser window" from the drop-down options.

  4. Google Cloud console opens a new terminal window. Generate a Compute Engine service account access token using `curl`.
         
         curl -s "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token" -H "Metadata-Flavor: Google"
         

The output looks like the following example:
         
         "access_token":"**ya29.c.KpkBCQgdwv6LrZ2tjrCpG6snWwPMX29LzMeUmAV_Hq_XaxUurfXcCfGZfASGh_KbdmUYTvkuV3sh-WaSBplEskdP6Tc
         HDsTv4B9hMyvoL4M9HrzKHuKTa1ZGj_3iQ1lwq_dAMxAPGjxEVKexatwN2KP0EAWyb6R55Cuu8ItgLf9f4pm9lC5zH4Qo0fkxPUsnCGRBe4AYxEpN6T
         sh** ","expires_in":3526,"token_type":"Bearer"}

  5. Copy the value of the `access_token` from the returned output without the quotation marks.

  6. Pull the image using `crictl pull --creds` and the `access_token` value copied in the previous step.
         
         crictl pull --creds "oauth2accesstoken:ACCESS_TOKEN" IMAGE_LOCATION:TAG

The output looks like the following:
         
         Image is up to date for sha256:0f25067aa9c180176967b4b50ed49eed096d43fa8c17be9a5fa9bff05933bee5




### gcloud

  1. Ensure that you have the latest version of the Google Cloud CLI
         
         gcloud components update
         

  2. Connect to the VM:
         
         gcloud compute ssh --project=PROJECT_ID \
          --zone=ZONE \
          VM_NAME
         

Replace the following variables:

     * `PROJECT_ID`: the ID of the project that contains the VM
     * `ZONE`: the name of the zone in which the VM is located
     * `VM_NAME`: the name of the VM

If you have [set default properties](https://docs.cloud.google.com/compute/docs/gcloud-compute#default-properties) for the Google Cloud CLI, you can omit the `--project` and `--zone` flags from this command. For example:
    
    gcloud compute ssh VM_NAME
    

  3. If you have not already created a SSH key, SSH keygen will generate one for you. Enter a passphrase or leave empty when prompted.

  4. Generate a Compute Engine service account access token using `curl`.
         
         curl -s "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token" -H "Metadata-Flavor: Google"
         

The output looks like the following:
         
         "access_token":"**ya29.c.KpkBCQgdwv6LrZ2tjrCpG6snWwPMX29LzMeUmAV_Hq_XaxUurfXcCfGZfASGh_KbdmUYTvkuV3sh-WaSBplEskdP6Tc
         HDsTv4B9hMyvoL4M9HrzKHuKTa1ZGj_3iQ1lwq_dAMxAPGjxEVKexatwN2KP0EAWyb6R55Cuu8ItgLf9f4pm9lC5zH4Qo0fkxPUsnCGRBe4AYxEpN6T
         sh** ","expires_in":3526,"token_type":"Bearer"}

  5. Copy the value of the `access_token` from the returned output without the quotation marks.

  6. Pull the image using `crictl pull --creds` and the `access_token` value copied in the previous step.
         
         crictl pull --creds "oauth2accesstoken:ACCESS_TOKEN" IMAGE_LOCATION:TAG

The output looks like the following:
         
         Image is up to date for sha256:0f25067aa9c180176967b4b50ed49eed096d43fa8c17be9a5fa9bff05933bee5




`crictl` lets developers debug their runtime without needing to set up Kubernetes components. For a full list of commands, see the [`crictl` docs](https://github.com/kubernetes-sigs/cri-tools/blob/master/docs/crictl.md) and the [Kubernetes debugging docs](https://kubernetes.io/docs/tasks/debug-application-cluster/crictl/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
