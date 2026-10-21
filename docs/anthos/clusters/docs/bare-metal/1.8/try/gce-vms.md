---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.8/try/gce-vms/
title: Try Google Distributed Cloud on Compute Engine VMs \u00a0|\u00a0 Anthos on bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:25:45.456962+00:00
---

# Try Google Distributed Cloud on Compute Engine VMs  |  Anthos on bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.8/try/gce-vms/

**Version 1.8**. This version is no longer supported. For information about how to upgrade to version 1.9, see [ Upgrading Anthos on bare metal](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.9/how-to/upgrade) in the 1.9 documentation. For more information about supported and unsupported versions, see the [Version history](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on bare metal 1.8 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.8)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.8/concepts/about-bare-metal)



Send feedback 

#  Try Google Distributed Cloud on Compute Engine VMs Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.8 (unsupported)keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/try/gce-vms)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/try/gce-vms)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.8/getting-support#version-support)



This page shows you how to try Google Distributed Cloud in High Availability (HA) mode using Virtual Machines (VMs) running on Compute Engine.

**Important:** This deployment is for evaluation purposes only. Don't run Google Distributed Cloud on Compute Engine VMs in production. To deploy Google Distributed Cloud in production, follow the steps in our [quickstart](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.8/quickstart).

You can try out Google Distributed Cloud quickly and without having to prepare any hardware. Completing the steps on this page provides you with working test environment running on Compute Engine for your Google Distributed Cloud environment.

To try Google Distributed Cloud on Compute Engine VMs, complete the following steps:

  1. Create six VMs in Compute Engine
  2. Create a `vxlan` network between all VMs with L2 connectivity
  3. Install prerequisites for Google Distributed Cloud
  4. Deploy an Google Distributed Cloud cluster
  5. Verify your cluster



## Before you begin

The deployment requires the following resources:

  * Six VMs to deploy Google Distributed Cloud
  * One workstation that is logged into `gcloud` with owner or editor permissions for your project

**Note:** All the commands are run on a machine that is logged into gcloud with project owner or editor credentials in the project.

## Create six VMs in Compute Engine

Complete these steps to create the following VMs:

  * One admin VM used to deploy Google Distributed Cloud to the other machines.
  * Three VMs for the three control plane nodes needed to run the Google Distributed Cloud control plane.
  * Two VMs for the two worker nodes needed to run workloads on the Google Distributed Cloud cluster.


  1. Create the `baremetal-gcr` service account:
         
         export PROJECT_ID=$(gcloud config get-value project)
         export ZONE=us-central1-a
         
         gcloud iam service-accounts create baremetal-gcr
         
         gcloud iam service-accounts keys create bm-gcr.json \
         --iam-account=baremetal-gcr@${PROJECT_ID}.iam.gserviceaccount.com
         

  2. Give the `baremetal-gcr` service account additional permissions to avoid needing multiple service accounts for different APIs and services:
         
         gcloud services enable \
             anthos.googleapis.com \
             anthosaudit.googleapis.com \
             anthosgke.googleapis.com \
             cloudresourcemanager.googleapis.com \
             container.googleapis.com \
             gkeconnect.googleapis.com \
             gkehub.googleapis.com \
             serviceusage.googleapis.com \
             stackdriver.googleapis.com \
             monitoring.googleapis.com \
             logging.googleapis.com \
             opsconfigmonitoring.googleapis.com
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
           --member="serviceAccount:baremetal-gcr@$PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/gkehub.connect"
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
           --member="serviceAccount:baremetal-gcr@$PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/gkehub.admin"
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
           --member="serviceAccount:baremetal-gcr@$PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/logging.logWriter"
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
           --member="serviceAccount:baremetal-gcr@$PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/monitoring.metricWriter"
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
           --member="serviceAccount:baremetal-gcr@$PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/monitoring.dashboardEditor"
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
           --member="serviceAccount:baremetal-gcr@$PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/stackdriver.resourceMetadata.writer"
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
           --member="serviceAccount:baremetal-gcr@$PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/opsconfigmonitoring.resourceMetadata.writer"
         

  3. Create the variables and arrays needed for all the commands on this page:
         
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
         

  4. Use the following loop to create six VMs:
         
         for vm in "${VMs[@]}"
         do
             gcloud compute instances create $vm \
                       --image-family=ubuntu-2004-lts --image-project=ubuntu-os-cloud \
                       --zone=${ZONE} \
                       --boot-disk-size 200G \
                       --boot-disk-type pd-ssd \
                       --can-ip-forward \
                       --network default \
                       --tags http-server,https-server \
                       --min-cpu-platform "Intel Haswell" \
                       --scopes cloud-platform \
                       --machine-type $MACHINE_TYPE
             IP=$(gcloud compute instances describe $vm --zone ${ZONE} \
                  --format='get(networkInterfaces[0].networkIP)')
             IPs+=("$IP")
         done
         

**Note:** If you intend to [deploy VMs](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.8/how-to/vm-workloads) using the Anthos VM Runtime, for better performance enable hardware virtualization by adding `--enable-nested-virtualization` to the preceding `gcloud` command.
  5. Use the following loop to verify that SSH is ready on all VMs:
         
         for vm in "${VMs[@]}"
         do
             while ! gcloud compute ssh root@$vm --zone ${ZONE} --command "echo SSH to $vm succeeded"
             do
                 echo "Trying to SSH into $vm failed. Sleeping for 5 seconds. zzzZZzzZZ"
                 sleep  5
             done
         done
         




## Create a `vxlan` network with L2 connectivity between VMs

Use the standard `vxlan` functionality of Linux to create a network that connects all the VMs with L2 connectivity.

The following command contains two loops that perform the following actions:

  1. SSH into each VM
  2. Update and install needed packages
  3. Execute the required commands to configure the network with `vxlan`
         
         i=2 # We start from 10.200.0.2/24
         for vm in "${VMs[@]}"
         do
             gcloud compute ssh root@$vm --zone ${ZONE} << EOF
                 apt-get -qq update > /dev/null
                 apt-get -qq install -y jq > /dev/null
                 set -x
                 ip link add vxlan0 type vxlan id 42 dev ens4 dstport 0
                 current_ip=\$(ip --json a show dev ens4 | jq '.[0].addr_info[0].local' -r)
                 echo "VM IP address is: \$current_ip"
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
         

**Note:** Starting with Google Distributed Cloud 1.8.2, you aren't required to disable AppArmor. If you use previous releases, add the following commands to the list above:
         
         systemctl stop apparmor.service
             systemctl disable apparmor.service
         




You now have L2 connectivity within the 10.200.0.0/24 network. The VMs have the following IP addresses:

  * Admin VM: 10.200.0.2
  * VMs running the control plane nodes: 
    * 10.200.0.3
    * 10.200.0.4
    * 10.200.0.5
  * VMs running the worker nodes: 
    * 10.200.0.6
    * 10.200.0.7



## Install prerequisites for Google Distributed Cloud

The following tools are needed on the admin machine before installing Google Distributed Cloud:

  * `bmctl`
  * `kubectl`
  * Docker


  1. Run the following command to install the needed tools:
         
         gcloud compute ssh root@$VM_WS --zone ${ZONE} << EOF
         set -x
         
         export PROJECT_ID=\$(gcloud config get-value project)
         gcloud iam service-accounts keys create bm-gcr.json \
         --iam-account=baremetal-gcr@\${PROJECT_ID}.iam.gserviceaccount.com
         
         curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl"
         
         chmod +x kubectl
         mv kubectl /usr/local/sbin/
         mkdir baremetal && cd baremetal
         gcloud storage cp gs://anthos-baremetal-release/bmctl/1.8.9/linux-amd64/bmctl .
         chmod a+x bmctl
         mv bmctl /usr/local/sbin/
         
         cd ~
         echo "Installing docker"
         curl -fsSL https://get.docker.com -o get-docker.sh
         sh get-docker.sh
         EOF
         

  2. Run the following commands to ensure that `root@10.200.0.x` works. The commands perform these tasks:

     1. Generate a new SSH key on the admin machine.
     2. Add the public key to all the other VMs in the deployment.
    
    gcloud compute ssh root@$VM_WS --zone ${ZONE} << EOF
    set -x
    ssh-keygen -t rsa -N "" -f /root/.ssh/id_rsa
    sed 's/ssh-rsa/root:ssh-rsa/' ~/.ssh/id_rsa.pub > ssh-metadata
    for vm in ${VMs[@]}
    do
        gcloud compute instances add-metadata \$vm --zone ${ZONE} --metadata-from-file ssh-keys=ssh-metadata
    done
    EOF
    




## Deploy an Google Distributed Cloud cluster

The following code block contains all commands and configurations needed to complete the following tasks:

  1. Create the configuration file for the needed hybrid cluster.
  2. Run the preflight checks.
  3. Deploy the cluster.

**Note:** Copy the entire code block into the console. If you copy only parts of it, the cluster creation won't succeed.
    
    
    gcloud compute ssh root@$VM_WS --zone ${ZONE} << EOF
    set -x
    export PROJECT_ID=$(gcloud config get-value project)
    export clusterid=cluster-1
    bmctl create config -c \$clusterid
    cat > bmctl-workspace/\$clusterid/\$clusterid.yaml << EOB
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
      name: cluster-\$clusterid
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: \$clusterid
      namespace: cluster-\$clusterid
    spec:
      type: hybrid
      anthosBareMetalVersion: 1.8.9
      gkeConnect:
        projectID: \$PROJECT_ID
      controlPlane:
        nodePoolSpec:
          clusterName: \$clusterid
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
        containerRuntime: containerd
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: NodePool
    metadata:
      name: node-pool-1
      namespace: cluster-\$clusterid
    spec:
      clusterName: \$clusterid
      nodes:
      - address: 10.200.0.6
      - address: 10.200.0.7
    EOB
    
    bmctl create cluster -c \$clusterid
    EOF
    

## Verify your cluster

You can find your cluster's `kubeconfig` file on the admin machine in the `bmctl-workspace` directory. To verify your deployment, complete the following steps.

  1. SSH into the admin workstation:
         
         gcloud compute ssh root@$VM_WS --zone ${ZONE}
         

  2. Set the `KUBECONFIG` environment variable with the path to the cluster's configuration file to run `kubectl` commands on the cluster.
         
         export clusterid=cluster-1
         export KUBECONFIG=$HOME/bmctl-workspace/$clusterid/$clusterid-kubeconfig
         kubectl get nodes
         


**Note:** Replace `$clusterid` with your actual cluster name. The command uses `cluster-1` because that's the value set in the previous code block when you created the cluster.

## Log in to your cluster from Google Cloud console

To observe your workloads on Google Distributed Cloud in the Google Cloud console, you must log in to your admin machine where the cluster's `kubeconfig` file is stored.

Go to [Logging in to a cluster from Google Cloud console](https://docs.cloud.google.com/anthos/multicluster-management/console/logging-in) to learn more.

## Clean up

  1. Connect to the admin machine to reset the cluster VMs to their state prior to installation and unregister the cluster from your Google Cloud Project:
         
         gcloud compute ssh root@$VM_WS --zone ${ZONE} << EOF
         set -x
         export clusterid=cluster-1
         bmctl reset -c \$clusterid
         EOF
         

**Note:** Replace `cluster-1` with your actual cluster name. The command uses `cluster-1` because that's the value set in the earlier code block when you created the cluster.
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
