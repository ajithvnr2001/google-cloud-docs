---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/vm-runtime/tutorial-deploy-existing-vm/
title: Tutorial: Deploy an existing VM in a Google Distributed Cloud cluster using VM Runtime on GDC \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:47:07.414444+00:00
---

# Tutorial: Deploy an existing VM in a Google Distributed Cloud cluster using VM Runtime on GDC  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/vm-runtime/tutorial-deploy-existing-vm/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Tutorial: Deploy an existing VM in a Google Distributed Cloud cluster using VM Runtime on GDC Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/vm-runtime/tutorial-deploy-existing-vm)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/vm-runtime/tutorial-deploy-existing-vm)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



This document provides a step-by-step guide to deploy a virtual machine (VM) based workload into Google Distributed Cloud using VM Runtime on GDC. The workload used in this guide is the sample [point of sale application](https://github.com/GoogleCloudPlatform/point-of-sale). This application represents a typical [point of sale terminal](https://en.wikipedia.org/wiki/Point_of_sale) that runs on on-premises hardware at a retail store.

In this document, you migrate this application from a VM into a Google Distributed Cloud cluster and access the application's web frontend. To migrate an existing VM into the cluster, first a disk image of that VM must be created. Then, the image must be hosted in a repository that the cluster can access. Finally, the URL of that image can be used to create the VM. VM Runtime on GDC expects the images to be in `qcow2` format. If you provide a different image type, it's automatically converted into the `qcow2` format. To avoid repetitive conversion and to enable reuse, you can [convert a virtual disk image](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/vm-runtime/convert-image) and host the `qcow2` image.

This document uses a pre-prepared image of a Compute Engine VM instance where the workload runs as a [systemd](https://en.wikipedia.org/wiki/Systemd) service. You may follow these same steps to deploy your own application.

## Objectives

  * Enable VM Runtime on GDC and install the `virtctl` plugin
  * Deploy the VM-based workload
  * Log in to the VM and check the application status
  * Access the VM-based workload



## Before you begin

To complete this document you need the following resources:

  * Access to a Google Distributed Cloud version 1.12.0 or higher cluster that was created by following the [Running Google Distributed Cloud on Compute Engine VMs with Manual Load Balancer](https://github.com/GoogleCloudPlatform/anthos-samples/blob/main/anthos-bm-gcp-terraform/docs/manuallb_install.md) guide. This document sets up networking resources so that you can access the workload running inside the VM through a browser. If you don't need that behavior, you can follow this document using any Google Distributed Cloud.
  * A workstation that meets the following requirements: 
    * Has access to your cluster using the [bmctl](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/reference/bmctl) CLI.
    * Has access to your cluster using the [kubectl](https://kubernetes.io/docs/reference/kubectl/) CLI.



## Enable VM Runtime on GDC and install the `virtctl` plugin

The VM Runtime on GDC custom resource definition (CRD) is part of all Google Distributed Cloud clusters since version 1.10. An instance of the `VMRuntime` custom resource is already created upon installation. However, it is disabled by default.

  1. Enable VM Runtime on GDC:
         
         sudo bmctl enable vmruntime --kubeconfig KUBECONFIG_PATH
         

     * KUBECONFIG_PATH: Path to the Kubernetes configuration file of the GKE Enterprise **user cluster**
  2. Validate that the `VMRuntime` is enabled:
         
         kubectl wait --for=jsonpath='{.status.ready}'=true vmruntime vmruntime
         

It can take a few minutes for the `VMRuntime` to be ready. If it is not ready, then check a few times with short delays. The following example output shows the `VMRuntime` is ready:
         
         vmruntime.vm.cluster.gke.io/vmruntime condition met
         

  3. Install the [virtctl](https://kubevirt.io/user-guide/operations/virtctl_client_tool/) plugin for `kubectl`:
         
         sudo -E bmctl install virtctl
         

The following example output shows the `virtctl` plugin installation process is complete:
         
         Please check the logs at bmctl-workspace/log/install-virtctl-20220831-182135/install-virtctl.log
         [2022-08-31 18:21:35+0000] Install virtctl succeeded
         

  4. Verify installation of the `virtctl` plugin:
         
         kubectl virt
         

The following example output shows that the `virtctl` plugin is available for use with `kubectl`:
         
         Available Commands:
           addvolume         add a volume to a running VM
           completion        generate the autocompletion script for the specified shell
           config            Config subcommands.
           console           Connect to a console of a virtual machine instance.
           create            Create subcommands.
           delete            Delete  subcommands.
         ...
         




## Deploy the VM-based workload

When you deploy a VM into Google Distributed Cloud, VM Runtime on GDC expects a VM image. This image serves as the boot disk for the deployed VM.

In this tutorial, you migrate a Compute Engine VM-based workload into a Google Distributed Cloud cluster. This Compute Engine VM was created, and the sample point of sale (PoS) application was configured to run as a systemd service. A [disk image of this VM along with the PoS application workload was created](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#create_image) in Google Cloud. This image was then [exported into a Cloud Storage bucket as a `qcow2` image](https://docs.cloud.google.com/compute/docs/images/export-image#exporting_an_image). You use this pre-prepared `qcow2` image in the following steps.

**Note:** Although we use a Compute Engine VM in this document, the steps to create a disk image of a VM vary depending on the environment or platform in which your existing VM is running. You can create a disk image of your existing VMs if you want to follow the steps in this document with your own custom image.

The source code in this document is available in the [anthos-samples](https://github.com/GoogleCloudPlatform/anthos-samples) GitHub repository. You use resources from this repository to complete the steps that follow.

  1. Deploy a MySQL `StatefulSet`. The point of sale application expects to connect to a MySQL database to store inventory and payment information. The point of sale repository has a sample manifest that deploys a MySQL `StatefulSet`, configures an associated `ConfigMap`, and a Kubernetes `Service`. The `ConfigMap` defines the credentials for the MySQL instance, which are the [same credentials passed into the point of sale application](https://github.com/GoogleCloudPlatform/point-of-sale/blob/main/src/inventory/src/main/resources/application-database.properties).
         
         kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/point-of-sale/main/k8-manifests/common/mysql-db.yaml
         

  2. Deploy the VM workload using the pre-prepared `qcow2` image:
         
         kubectl virt create vm pos-vm \
             --boot-disk-size=80Gi \
             --memory=4Gi \
             --vcpu=2 \
             --image=https://storage.googleapis.com/pos-vm-images/pos-vm.qcow2
         

This command creates a YAML file named after the VM (`google-virtctl/pos-vm.yaml`). You can inspect the file to see the definition of the `VirtualMachine` and `VirtualMachineDisk`. Instead of using the `virtctl` plugin, you could have deployed the VM workload using [Kubernetes Resource Model (KRM) definitions](https://github.com/GoogleCloudPlatform/anthos-samples/blob/main/anthos-vmruntime/pos-vm.yaml), as seen in the created YAML file.

When the command runs successfully, it produces an output like the following example that explains the different resources that were created:
         
         Constructing manifest for vm "pos-vm":
         Manifest for vm "pos-vm" is saved to /home/tfadmin/google-virtctl/pos-vm.yaml
         Applying manifest for vm "pos-vm"
         Created gvm "pos-vm"
         

  3. Check the VM creation status.

The `VirtualMachine` resource is identified by the `vm.cluster.gke.io/v1.VirtualMachine` resource in VM Runtime on GDC. The short form for it is `gvm`.

When you create a VM, the following two resources are created:

     * A **VirtualMachineDisk** is the persistent disk where the contents of the VM image is imported into.
     * A **VirtualMachine** is the VM instance itself. The **DataVolume** is mounted into the **VirtualMachine** before the VM is booted up.

Check the status of the VirtualMachineDisk. VirtualMachineDisk internally creates a `DataVolume` resource. The VM image is imported into the DataVolume which is mounted into the VM:
    
    kubectl get datavolume
    

The following example output shows the start of the image import:
    
    NAME              PHASE             PROGRESS   RESTARTS   AGE
    pos-vm-boot-dv    ImportScheduled   N/A                   8s
    

  4. Check the status of the `VirtualMachine`. The `VirtualMachine` is in the `Provisioning` state until the `DataVolume` is imported completely:
         
         kubectl get gvm
         

The following example output shows the `VirtualMachine` being provisioned:
         
         NAME      STATUS         AGE     IP
         pos-vm    Provisioning   1m
         

  5. Wait for the VM image to be fully imported into the `DataVolume`. Continue to watch the progress while the image is imported:
         
         kubectl get datavolume -w
         

The following example output shows the disk image being imported:
         
         NAME              PHASE              PROGRESS   RESTARTS   AGE
         pos-vm-boot-dv   ImportInProgress   0.00%                 14s
         ...
         ...
         pos-vm-boot-dv   ImportInProgress   0.00%                 31s
         pos-vm-boot-dv   ImportInProgress   1.02%                 33s
         pos-vm-boot-dv   ImportInProgress   1.02%                 35s
         ...
         

When the import is complete and the `DataVolume` is created, the following example output shows the `PHASE` of `Succeeded` :
         
         kubectl get datavolume
         
         
         NAME              PHASE             PROGRESS   RESTARTS   AGE
         pos-vm-boot-dv    Succeeded         100.0%                14m18s
         

**Note:** The import time depends on the size of the VM image used. The Compute Engine VM image in this document is about 5 GB and takes up to 15 minutes to import.
  6. Confirm that the `VirtualMachine` has been created successfully:
         
         kubectl get gvm
         

If the creation was successful the `STATUS` shows `RUNNING`, as shown in the following example, along with the VM's IP address:
         
         NAME      STATUS    AGE     IP
         pos-vm    Running   40m     192.168.3.250
         




## Connect to the VM and check the application status

The image used for the VM includes the [point of sale sample application](https://github.com/GoogleCloudPlatform/point-of-sale). The application is configured to automatically start on boot as a systemd service. You can see the systemd services' configuration files in the [pos-systemd-services](https://github.com/GoogleCloudPlatform/anthos-samples/blob/main/anthos-vmruntime/pos-systemd-services) directory.

  1. Connect to the VM console. Run the following command and press **Enter⏎** after you see the `Successfully connected to pos-vm…` message:
         
         kubectl virt console pos-vm
         

This command produces the following example output that prompts you to input the login details:
         
         Successfully connected to pos-vm console. The escape sequence is ^]
         
         pos-from-public-image login:
         

Use the following user account and password. This account was set up inside the original VM from which the image for the VM Runtime on GDC VirtualMachine was created.

     * Login Username: `abmuser`
     * Password: `abmworks`
  2. Check the status of the point of sale application services. The point of sale application includes three services: API, Inventory, and Payments. These services all run as system services.

The three services all connect to each other through localhost. However, the application connects to the MySQL database using a [mysql-db Kubernetes Service](https://github.com/GoogleCloudPlatform/anthos-samples/blob/main/anthos-vmruntime/pos-systemd-services/pos_inventory.service#L27) that was created in the earlier step. This behavior means that the VM is automatically connected to the same network as the `Pods` and `Services`, enabling seamless communication between VM workloads and other containerized applications. You don't have to do anything extra to make the Kubernetes `Services` reachable from the VMs deployed using VM Runtime on GDC.
         
         sudo systemctl status pos*
         

The following example output shows the status of the three services and root system service, `pos.service`:
         
         ● pos_payments.service - Payments service of the Point of Sale Application
             Loaded: loaded (/etc/systemd/system/pos_payments.service; enabled; vendor >
             Active: active (running) since Tue 2022-06-21 18:55:30 UTC; 1h 10min ago
           Main PID: 750 (payments.sh)
               Tasks: 27 (limit: 4664)
             Memory: 295.1M
             CGroup: /system.slice/pos_payments.service
                     ├─750 /bin/sh /pos/scripts/payments.sh
                     └─760 java -jar /pos/jars/payments.jar --server.port=8083
         
         ● pos_inventory.service - Inventory service of the Point of Sale Application
             Loaded: loaded (/etc/systemd/system/pos_inventory.service; enabled; vendor>
             Active: active (running) since Tue 2022-06-21 18:55:30 UTC; 1h 10min ago
           Main PID: 749 (inventory.sh)
               Tasks: 27 (limit: 4664)
             Memory: 272.6M
             CGroup: /system.slice/pos_inventory.service
                     ├─749 /bin/sh /pos/scripts/inventory.sh
                     └─759 java -jar /pos/jars/inventory.jar --server.port=8082
         
         ● pos.service - Point of Sale Application
             Loaded: loaded (/etc/systemd/system/pos.service; enabled; vendor preset: e>
             Active: active (exited) since Tue 2022-06-21 18:55:30 UTC; 1h 10min ago
           Main PID: 743 (code=exited, status=0/SUCCESS)
               Tasks: 0 (limit: 4664)
             Memory: 0B
             CGroup: /system.slice/pos.service
         
         Jun 21 18:55:30 pos-vm systemd[1]: Starting Point of Sale Application...
         Jun 21 18:55:30 pos-vm systemd[1]: Finished Point of Sale Application.
         
         ● pos_apiserver.service - API Server of the Point of Sale Application
             Loaded: loaded (/etc/systemd/system/pos_apiserver.service; enabled; vendor>
             Active: active (running) since Tue 2022-06-21 18:55:31 UTC; 1h 10min ago
           Main PID: 751 (api-server.sh)
               Tasks: 26 (limit: 4664)
             Memory: 203.1M
             CGroup: /system.slice/pos_apiserver.service
                     ├─751 /bin/sh /pos/scripts/api-server.sh
                     └─755 java -jar /pos/jars/api-server.jar --server.port=8081
         

  3. Exit the VM. To exit the console connection, use escape sequence `^]` by pressing `Ctrl + ]`.




## Access the VM-based workload

If your cluster was set up by following the [Running Google Distributed Cloud on Compute Engine VMs with Manual Load Balancer](https://github.com/GoogleCloudPlatform/anthos-samples/blob/main/anthos-bm-gcp-terraform/docs/manuallb_install.md) guide, it has an `Ingress` resource called `pos-ingress` already created. This resource routes the traffic from the external IP address of the Ingress Load Balancer to the API server service of the point of sale sample application.

  1. If your cluster doesn't have this `Ingress` resource, create it by applying the following manifest:
         
         kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/anthos-samples/main/anthos-bm-gcp-terraform/resources/manifests/pos-ingress.yaml
         
         
         apiVersion: networking.k8s.io/v1
         kind: Ingress
         metadata:
           name: pos-ingress
         spec:
           rules:
           - http:
               paths:
               - path: /
                 pathType: Prefix
                 backend:
                   service:
                     name: api-server-svc
                     port:
                       number: 8080

  2. Create a Kubernetes `Service` that routes traffic to the VM. The `Ingress` resource routes traffic to this `Service`:
         
         kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/anthos-samples/main/anthos-vmruntime/pos-service.yaml
         

The following example output confirms the creation of a Service:
         
         service/api-server-svc created
         
         
         apiVersion: v1
         kind: Service
         metadata:
           name: api-server-svc
         spec:
           selector:
             kubevirt/vm: pos-vm
           ports:
           - protocol: TCP
             port: 8080
             targetPort: 8081

  3. Get the external IP address of the `Ingress` load balancer. The `Ingress` Loadbalancer routes traffic based on the `Ingress` resource rules. You already have a `pos-ingress` rule to forward requests to the API server `Service`. This `Service` forwards the requests to the VM:
         
         INGRESS_IP=$(kubectl get ingress/pos-ingress -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
         echo $INGRESS_IP
         

The following example output shows the IP address of the `Ingress` load balancer:
         
         172.29.249.159 # you might have a different IP address
         

  4. Access the application by using the Ingress Loadbalancer IP address in a browser. The following example screenshots shows the simple point of sale kiosk with two items. You can click the items, more than once if you want to order multiple of them, and place an order with the **Pay** button. This experience shows that you have successfully deployed a VM-based workload into a Google Distributed Cloud cluster using VM Runtime on GDC.


[ ![Point of sale application UI](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/images/pos-app.png)](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/images/pos-app.png) Point of sale application UI (click image to enlarge)

## Clean up

You may delete all the resources created in this tutorial or delete only the VM and keep reusable resources. [Delete a VM in Google Distributed Cloud](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/vm-runtime/delete) explains the available options in detail.

###  Delete All 

  * Delete the VM Runtime on GDC `VirtualMachine` along with all the resources:
        
        kubectl virt delete vm pos-vm --all
        

The following example output confirms the deletion:
        
        vm "pos-vm" used the following resources: 
            gvm: pos-vm
            VirtualMachineDisk: pos-vm-boot-dv
        Start deleting the resources:
            Deleted gvm "pos-vm".
            Deleted VirtualMachineDisk "pos-vm-boot-dv".
        




###  Delete only VM 

  * Deleting only the VM preserves the `VirtualMachineDisk` that gets created. This enables reuse of this VM image and saves time spent on importing the image when creating a new VM.
        
        kubectl virt delete vm pos-vm
        

The following example output confirms the deletion:
        
        vm "pos-vm" used the following resources: 
            gvm: pos-vm
            VirtualMachineDisk: pos-vm-boot-dv
        Start deleting the resources:
            Deleted gvm "pos-vm".
        




## What's next

  * The original VM used in this guide is a Compute Engine instance that runs Ubuntu 20.04 LTS. The image of this VM is publicly accessible through the [pos-vm-images](https://console.cloud.google.com/storage/browser/pos-vm-images;tab=objects?project=point-of-sale-ci) Cloud Storage bucket. For more information on how the VM was configured and its image was created, see the instructions in the point-of-sale repository.
  * When you create a VM in a Google Distributed Cloud cluster using the `kubectl virt create vm pos-vm` command, a YAML file named after the VM (`google-virtctl/pos-vm.yaml`) is created. You can inspect the file to see the definition of the `VirtualMachine` and `VirtualMachineDisk`. Instead of using the `virtctl` plugin, you can deploy a VM using [KRM definitions](https://github.com/GoogleCloudPlatform/anthos-samples/blob/main/anthos-vmruntime/pos-vm.yaml) as seen in the created YAML file.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
