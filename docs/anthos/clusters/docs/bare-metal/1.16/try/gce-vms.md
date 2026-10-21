---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/try/gce-vms/
title: Create a Google Distributed Cloud hybrid cluster on Compute Engine VMs \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:46:17.078873+00:00
---

# Create a Google Distributed Cloud hybrid cluster on Compute Engine VMs  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/try/gce-vms/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Create a Google Distributed Cloud hybrid cluster on Compute Engine VMs Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/try/gce-vms)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/try/gce-vms)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



This page shows you how to set up a Google Distributed Cloud hybrid cluster in High Availability (HA) mode using Virtual Machines (VMs) running on Compute Engine.

**Important:** This deployment is for evaluation purposes only. Don't run Google Distributed Cloud on Compute Engine VMs in production. For production, follow the steps in our [Quickstart](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/quickstart) to install Google Distributed Cloud on your hardware.

You can try out Google Distributed Cloud quickly and without having to prepare any hardware. Completing the steps on this page provides you with a working Google Distributed Cloud test environment that runs on Compute Engine.

To try Google Distributed Cloud on Compute Engine VMs, complete the following steps:

  1. Create six VMs in Compute Engine
  2. Create a `vxlan` network between all VMs with L2 connectivity
  3. Install prerequisites for Google Distributed Cloud
  4. Deploy a Google Distributed Cloud hybrid cluster

  5. Verify your cluster




## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Make a note of the project ID because you need it to set an environment variable that is used in the scripts and commands on this page. If you selected an existing project, make sure that you are either a project owner or editor. 
  7. On your Linux workstation, make sure you have installed the latest [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install), the command line tool for interacting with Google Cloud. If you already have gcloud CLI installed, update its components by running the following command: 
         
         gcloud components update

Depending on how the gcloud CLI was installed, you might see the following message: "You cannot perform this action because the Google Cloud CLI component manager is disabled for this installation. You can run the following command to achieve the same result for this installation:" Follow the instructions to copy and paste the command to update the components.




The steps in this guide are taken from the installation script in the [anthos-samples](https://github.com/GoogleCloudPlatform/anthos-samples/tree/main/anthos-bm-gcp-bash) repository. The [FAQ section](https://github.com/GoogleCloudPlatform/anthos-samples/blob/main/anthos-bm-gcp-bash/docs/faq.md#frequently-asked-questions-faq) has more information on how to customize this script to work with some popular variations.

## Create six VMs in Compute Engine

Complete these steps to create the following VMs:

  * One VM for the admin workstation. An admin workstation hosts command-line interface (CLI) tools and configuration files to provision clusters during installation, and CLI tools for interacting with provisioned clusters post-installation. The admin workstation will have access to all the other nodes in the cluster via SSH.
  * Three VMs for the three control plane nodes needed to run the Google Distributed Cloud control plane.
  * Two VMs for the two worker nodes needed to run workloads on the Google Distributed Cloud cluster.


  1. Setup environment variables:
         
         export PROJECT_ID=PROJECT_ID
         export ZONE=ZONE
         export CLUSTER_NAME=CLUSTER_NAME
         export BMCTL_VERSION=1.16.8
         

For the `ZONE`, you can use `us-central1-a` or any of the other [Compute Engine zones](https://docs.cloud.google.com/compute/docs/regions-zones#available) .

  2. Run the following commands to log in with your Google account and set your project as the default:
         
         gcloud auth login
         gcloud config set project $PROJECT_ID
         gcloud config set compute/zone $ZONE
         

  3. Create the `baremetal-gcr` service account:
         
         gcloud iam service-accounts create baremetal-gcr
         
         gcloud iam service-accounts keys create bm-gcr.json \
             --iam-account=baremetal-gcr@"${PROJECT_ID}".iam.gserviceaccount.com

  4. Enable Google Cloud APIs and services:
         
         gcloud services enable \
             anthos.googleapis.com \
             anthosaudit.googleapis.com \
             anthosgke.googleapis.com \
             cloudresourcemanager.googleapis.com \
             connectgateway.googleapis.com \
             container.googleapis.com \
             gkeconnect.googleapis.com \
             gkehub.googleapis.com \
             serviceusage.googleapis.com \
             stackdriver.googleapis.com \
             monitoring.googleapis.com \
             logging.googleapis.com \
             opsconfigmonitoring.googleapis.com \
             compute.googleapis.com \
             gkeonprem.googleapis.com \
             iam.googleapis.com \
             kubernetesmetadata.googleapis.com

  5. Give the `baremetal-gcr` service account additional permissions to avoid needing multiple service accounts for different APIs and services:
         
         gcloud projects add-iam-policy-binding "$PROJECT_ID" \
           --member="serviceAccount:baremetal-gcr@$PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/gkehub.connect" \
           --no-user-output-enabled
         
         gcloud projects add-iam-policy-binding "$PROJECT_ID" \
           --member="serviceAccount:baremetal-gcr@$PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/gkehub.admin" \
           --no-user-output-enabled
         
         gcloud projects add-iam-policy-binding "$PROJECT_ID" \
           --member="serviceAccount:baremetal-gcr@$PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/logging.logWriter" \
           --no-user-output-enabled
         
         gcloud projects add-iam-policy-binding "$PROJECT_ID" \
           --member="serviceAccount:baremetal-gcr@$PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/monitoring.metricWriter" \
           --no-user-output-enabled
         
         gcloud projects add-iam-policy-binding "$PROJECT_ID" \
           --member="serviceAccount:baremetal-gcr@$PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/monitoring.dashboardEditor" \
           --no-user-output-enabled
         
         gcloud projects add-iam-policy-binding "$PROJECT_ID" \
           --member="serviceAccount:baremetal-gcr@$PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/stackdriver.resourceMetadata.writer" \
           --no-user-output-enabled
         
         gcloud projects add-iam-policy-binding "$PROJECT_ID" \
           --member="serviceAccount:baremetal-gcr@$PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/opsconfigmonitoring.resourceMetadata.writer" \
           --no-user-output-enabled
         
         gcloud projects add-iam-policy-binding "$PROJECT_ID" \
             --member="serviceAccount:baremetal-gcr@$PROJECT_ID.iam.gserviceaccount.com" \
             --role="roles/kubernetesmetadata.publisher" \
             --no-user-output-enabled
         
         gcloud projects add-iam-policy-binding "$PROJECT_ID" \
           --member="serviceAccount:baremetal-gcr@$PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/monitoring.viewer" \
           --no-user-output-enabled
         
         gcloud projects add-iam-policy-binding "$PROJECT_ID" \
           --member="serviceAccount:baremetal-gcr@$PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/serviceusage.serviceUsageViewer" \
           --no-user-output-enabled

  6. Create the variables and arrays needed for all the commands on this page:
         
         MACHINE_TYPE=n1-standard-8
         VM_PREFIX=abm
         VM_WS=$VM_PREFIX-ws
         VM_CP1=$VM_PREFIX-cp1
         VM_CP2=$VM_PREFIX-cp2
         VM_CP3=$VM_PREFIX-cp3
         VM_W1=$VM_PREFIX-w1
         VM_W2=$VM_PREFIX-w2
         declare -a VMs=("$VM_WS" "$VM_CP1" "$VM_CP2" "$VM_CP3" "$VM_W1" "$VM_W2")
         declare -a IPs=()

  7. Use the following loop to create six VMs:

**Note:** If you intend to [deploy VMs](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/vm-workloads) using the Anthos VM Runtime, for better performance enable hardware virtualization by adding `--enable-nested-virtualization` to the following `gcloud` command.
         
         for vm in "${VMs[@]}"
         do
             gcloud compute instances create "$vm" \
               --image-family=ubuntu-2204-lts --image-project=ubuntu-os-cloud \
               --zone="${ZONE}" \
               --boot-disk-size 200G \
               --boot-disk-type pd-ssd \
               --can-ip-forward \
               --network default \
               --tags http-server,https-server \
               --min-cpu-platform "Intel Haswell" \
               --enable-nested-virtualization \
               --scopes cloud-platform \
               --machine-type "$MACHINE_TYPE" \
               --metadata "cluster_id=${CLUSTER_NAME},bmctl_version=${BMCTL_VERSION}"
             IP=$(gcloud compute instances describe "$vm" --zone "${ZONE}" \
                  --format='get(networkInterfaces[0].networkIP)')
             IPs+=("$IP")
         done

This command creates VM instances with the following names:

     * **abm-ws** : The VM for the admin workstation.
     * **abm-cp1** , **abm-cp2** , **abm-cp3** : The VMs for the control plane nodes.
     * **abm-w1** , **abm-w2** : The VMs for the nodes that run workloads.
  8. Use the following loop to verify that SSH is ready on all VMs:
         
         for vm in "${VMs[@]}"
         do
             while ! gcloud compute ssh root@"$vm" --zone "${ZONE}" --command "printf 'SSH to $vm succeeded\n'"
             do
                 printf "Trying to SSH into %s failed. Sleeping for 5 seconds. zzzZZzzZZ" "$vm"
                 sleep  5
             done
         done




## Create a `vxlan` network with L2 connectivity between VMs

Use the standard `vxlan` functionality of Linux to create a network that connects all the VMs with L2 connectivity.

The following command contains two loops that perform the following actions:

  1. SSH into each VM.
  2. Update and install needed packages.
  3. Execute the required commands to configure the network with `vxlan`.
         
         i=2 # We start from 10.200.0.2/24
         for vm in "${VMs[@]}"
         do
             gcloud compute ssh root@"$vm" --zone "${ZONE}" << EOF
                 apt-get -qq update > /dev/null
                 apt-get -qq install -y jq > /dev/null
                 set -x
                 ip link add vxlan0 type vxlan id 42 dev ens4 dstport 0
                 current_ip=\$(ip --json a show dev ens4 | jq '.[0].addr_info[0].local' -r)
                 printf "VM IP address is: \$current_ip"
                 for ip in ${IPs[@]}; do
                     if [ "\$ip" != "\$current_ip" ]; then
                         bridge fdb append to 00:00:00:00:00:00 dst \$ip dev vxlan0
                     fi
                 done
                 ip addr add 10.200.0.$i/24 dev vxlan0
                 ip link set up dev vxlan0
         
         EOF
             i=$((i+1))
         done




You now have L2 connectivity within the 10.200.0.0/24 network. The VMs have the following IP addresses:

  * Admin workstation VM: 10.200.0.2
  * VMs running the control plane nodes: 
    * 10.200.0.3
    * 10.200.0.4
    * 10.200.0.5
  * VMs running the worker nodes: 
    * 10.200.0.6
    * 10.200.0.7



## Install prerequisites for Google Distributed Cloud

You need to install the following tools on the admin workstation before installing Google Distributed Cloud:

  * `bmctl`
  * `kubectl`
  * Docker



To install the tools and prepare for Google Distributed Cloud installation:

  1. Run the following commands to download the service account key to the admin workstation and install the required tools:
         
         gcloud compute ssh root@$VM_WS --zone "${ZONE}" << EOF
         set -x
         
         export PROJECT_ID=\$(gcloud config get-value project)
         BMCTL_VERSION=\$(curl http://metadata.google.internal/computeMetadata/v1/instance/attributes/bmctl_version -H "Metadata-Flavor: Google")
         export BMCTL_VERSION
         
         gcloud iam service-accounts keys create bm-gcr.json \
           --iam-account=baremetal-gcr@\${PROJECT_ID}.iam.gserviceaccount.com
         
         curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl"
         
         chmod +x kubectl
         mv kubectl /usr/local/sbin/
         mkdir baremetal && cd baremetal
         gcloud storage cp gs://anthos-baremetal-release/bmctl/$BMCTL_VERSION/linux-amd64/bmctl .
         chmod a+x bmctl
         mv bmctl /usr/local/sbin/
         
         cd ~
         printf "Installing docker"
         curl -fsSL https://get.docker.com -o get-docker.sh
         sh get-docker.sh
         EOF

  2. Run the following commands to ensure that `root@10.200.0.x` works. The commands perform these tasks:

     1. Generate a new SSH key on the admin workstation.
     2. Add the public key to all the other VMs in the deployment.
    
    gcloud compute ssh root@$VM_WS --zone "${ZONE}" << EOF
    set -x
    ssh-keygen -t rsa -N "" -f /root/.ssh/id_rsa
    sed 's/ssh-rsa/root:ssh-rsa/' ~/.ssh/id_rsa.pub > ssh-metadata
    for vm in ${VMs[@]}
    do
        gcloud compute instances add-metadata \$vm --zone ${ZONE} --metadata-from-file ssh-keys=ssh-metadata
    done
    EOF




## Deploy a Google Distributed Cloud hybrid cluster

The following code block contains all commands and configurations needed to complete the following tasks:

  1. Create the configuration file for the needed hybrid cluster.
  2. Run the preflight checks.
  3. Deploy the cluster.


    
    
    gcloud compute ssh root@$VM_WS --zone "${ZONE}" <<EOF
    set -x
    export PROJECT_ID=$(gcloud config get-value project)
    CLUSTER_NAME=\$(curl http://metadata.google.internal/computeMetadata/v1/instance/attributes/cluster_id -H "Metadata-Flavor: Google")
    BMCTL_VERSION=\$(curl http://metadata.google.internal/computeMetadata/v1/instance/attributes/bmctl_version -H "Metadata-Flavor: Google")
    export CLUSTER_NAME
    export BMCTL_VERSION
    bmctl create config -c \$CLUSTER_NAME
    cat > bmctl-workspace/\$CLUSTER_NAME/\$CLUSTER_NAME.yaml << EOB
    ---
    gcrKeyPath: /root/bm-gcr.json
    sshPrivateKeyPath: /root/.ssh/id_rsa
    gkeConnectAgentServiceAccountKeyPath: /root/bm-gcr.json
    gkeConnectRegisterServiceAccountKeyPath: /root/bm-gcr.json
    cloudOperationsServiceAccountKeyPath: /root/bm-gcr.json
    ---
    apiVersion: v1
    kind: Namespace
    metadata:
      name: cluster-\$CLUSTER_NAME
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: \$CLUSTER_NAME
      namespace: cluster-\$CLUSTER_NAME
    spec:
      type: hybrid
      anthosBareMetalVersion: \$BMCTL_VERSION
      gkeConnect:
        projectID: \$PROJECT_ID
      controlPlane:
        nodePoolSpec:
          clusterName: \$CLUSTER_NAME
          nodes:
          - address: 10.200.0.3
          - address: 10.200.0.4
          - address: 10.200.0.5
      clusterNetwork:
        pods:
          cidrBlocks:
          - 192.168.0.0/16
        services:
          cidrBlocks:
          - 172.26.232.0/24
      loadBalancer:
        mode: bundled
        ports:
          controlPlaneLBPort: 443
        vips:
          controlPlaneVIP: 10.200.0.49
          ingressVIP: 10.200.0.50
        addressPools:
        - name: pool1
          addresses:
          - 10.200.0.50-10.200.0.70
      clusterOperations:
        # might need to be this location
        location: us-central1
        projectID: \$PROJECT_ID
      storage:
        lvpNodeMounts:
          path: /mnt/localpv-disk
          storageClassName: node-disk
        lvpShare:
          numPVUnderSharedPath: 5
          path: /mnt/localpv-share
          storageClassName: local-shared
      nodeConfig:
        podDensity:
          maxPodsPerNode: 250
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: NodePool
    metadata:
      name: node-pool-1
      namespace: cluster-\$CLUSTER_NAME
    spec:
      clusterName: \$CLUSTER_NAME
      nodes:
      - address: 10.200.0.6
      - address: 10.200.0.7
    EOB
    
    bmctl create cluster -c \$CLUSTER_NAME
    EOF

## Verify your cluster

You can find your cluster's `kubeconfig` file on the admin workstation in the `bmctl-workspace` directory of the root account. To verify your deployment, complete the following steps.

  1. SSH into the admin workstation as root:
         
         gcloud compute ssh root@abm-ws --zone ${ZONE}
         

You can ignore any messages about updating the VM and complete this tutorial. If you plan to keep the VMs as a test environment, you might want to update the OS or upgrade to the next release as described in the [Ubuntu documentation](https://ubuntu.com/server/docs/upgrade-introduction).

  2. Set the `KUBECONFIG` environment variable with the path to the cluster's configuration file to run `kubectl` commands on the cluster.
         
         export clusterid=CLUSTER_NAME
         export KUBECONFIG=$HOME/bmctl-workspace/$clusterid/$clusterid-kubeconfig
         kubectl get nodes
         

  3. Set the current context in an environment variable:
         
         export CONTEXT="$(kubectl config current-context)"
         

  4. Run the following `gcloud` command. This command:

     * Grants your user account the Kubernetes `clusterrole/cluster-admin` role on the cluster.
     * Configures the cluster so that you can run `kubectl` commands on your local computer without having to SSH to the admin workstation.

Replace `GOOGLE_ACCOUNT_EMAIL` with the email address that is associated with your Google Cloud account. For example: `--users=alex@example.com`.
    
    gcloud container fleet memberships generate-gateway-rbac  \
        --membership=CLUSTER_NAME \
        --role=clusterrole/cluster-admin \
        --users=GOOGLE_ACCOUNT_EMAIL \
        --project=PROJECT_ID \
        --kubeconfig=$KUBECONFIG \
        --context=$CONTEXT\
        --apply
    

The output of this command is similar to the following, which is truncated for readability:
    
    Validating input arguments.
    Specified Cluster Role is: clusterrole/cluster-admin
    Generated RBAC policy is:
    --------------------------------------------
    ...
    
    Applying the generate RBAC policy to cluster with kubeconfig: /root/bmctl-workspace/CLUSTER_NAME/CLUSTER_NAME-kubeconfig, context: CLUSTER_NAME-admin@CLUSTER_NAME
    Writing RBAC policy for user: GOOGLE_ACCOUNT_EMAIL to cluster.
    Successfully applied the RBAC policy to cluster.
    

  5. When you are finished exploring, enter **exit** to log out of the admin workstation.

  6. Get the `kubeconfig` entry that can access the cluster through the [Connect gateway](https://docs.cloud.google.com/anthos/multicluster-management/gateway).
         
         gcloud container fleet memberships get-credentials CLUSTER_NAME
         

The output is similar to the following:
         
         Starting to build Gateway kubeconfig...
         Current project_id: PROJECT_ID
         A new kubeconfig entry "connectgateway_PROJECT_ID_global_CLUSTER_NAME" has been generated and set as the current context.
         

  7. You can now run `kubectl` commands through the Connect gateway:
         
         kubectl get nodes
         kubectl get namespaces
         




## Log in to your cluster from Google Cloud console

To observe your workloads on Google Distributed Cloud in the Google Cloud console, you need to log in to the cluster. Before you log in to the console for the first time, you need to configure an authentication method. The easiest authentication method to configure is Google identity. This authentication method lets you log in using the email address associated with your Google Cloud account.

The `gcloud container fleet memberships generate-gateway-rbac` command that you ran in the previous section configures the cluster so that you can log in with your Google identity.

  1. In the Google Cloud console, go to the **GKE Clusters** page.

[Go to GKE clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Click more_vert **Actions** next to the registered cluster, then click **Login**.

  3. Select **Use your Google identity to log in**.

  4. Click **Login**.




## Clean up

  1. Connect to the admin workstation to reset the cluster VMs to their state prior to installation and unregister the cluster from your Google Cloud project:
         
         gcloud compute ssh root@abm-ws --zone ${ZONE} << EOF
         set -x
         export clusterid=CLUSTER_NAME
         bmctl reset -c \$clusterid
         EOF
         

  2. List all VMs that have `abm` in their name:
         
         gcloud compute instances list | grep 'abm'
         

  3. Verify that you're fine with deleting all VMs that contain `abm` in the name.

After you've verified, you can delete `abm` VMs by running the following command:
         
         gcloud compute instances list --format="value(name)" | grep 'abm'  | xargs gcloud \
             --quiet compute instances delete
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
