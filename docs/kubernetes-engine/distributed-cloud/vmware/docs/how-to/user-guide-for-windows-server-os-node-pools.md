---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-guide-for-windows-server-os-node-pools/
title: User guide for Windows Server OS node pools \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:19:47.022989+00:00
---

# User guide for Windows Server OS node pools  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-guide-for-windows-server-os-node-pools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  User guide for Windows Server OS node pools Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** The Windows Server OS node pools feature is deprecated in Google Distributed Cloud version 1.32 and will be unavailable in version 1.33 and higher. Support for Windows Server node pools ends on May 5, 2026. We recommend that you don't use "windows" as the OS image type on new clusters.

With Google Distributed Cloud, you can create a node pool of Windows Server OS nodes. The user cluster that runs the Windows Server OS node pools can also run node pools that contain nodes using Ubuntu or Container-Optimized OS.

## Requirements for a Windows Server OS node pool

The nodes in a node pool must all use the same operating system, indicated by the `osImageType` parameter.

Before you create, in your user cluster, a node pool that has Windows Server OS nodes, make sure you meet these requirements:

  * An admin cluster must already be in place before you can create a Windows node pool, because a Windows node pool is only supported in the user cluster.
  * The user cluster must run at least one Linux node pool, because the Linux node pool is required to create a Windows node pool.
  * A user cluster with Windows node pools must have the [`enabledataplanev2`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enabledataplanev2-field) field set to `true` in the user cluster configuration file. This enables Dataplane V2 on the Linux nodes in that cluster.
  * By default, Windows Dataplane V2 is enabled for the Windows node pools for new user clusters.

  * You have downloaded a Windows Server 2019 ISO from Microsoft to create a VM template specific for Windows node pools. The language/region tag for the ISO must be en-US.

  * Your vSphere environment must be vSphere 6.7, Update 3 or later.

  * Windows Server OS node pools have the following limitations:

    * IPv6 isn't supported.
    * Windows nodes pools aren't supported on [advanced clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enable-advanced-cluster-field).



## Create a Windows node pool in a user cluster

**Note:** The Windows container images are not available as a bundle with the base layer, also known as a foreign layer, coming from the Microsoft registry. This is because the base layer image from the Microsoft registry can't be re-distributed. Thus, you must pull the base layer image from Artifact Registry.

### Step 1: Create the Windows VM Template for Google Distributed Cloud

Before you begin, make sure that you have already [created an admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-cluster).

**Note:** For the admin workstation, you must allow the admin workstation and the jump host to access the ESXi host IP on which the Windows VM runs, so that you can run `gkectl prepare windows`.

  1. Create a base Windows VM template from the Windows Server 2019 ISO.

     * The initial network adapter type for the Windows VM to install Windows Server 2019 ISO should be E1000E.
     * Follow these steps: [Create a VMware vSphere template for Windows Server 2019](https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/manage/hybrid/server/best-practices/vmware-windows-template).
     * Take note of the initial password that is set when you run the Windows ISO installer, to use it in the future.
     * Make sure you are using the latest qualified patch version for Windows Server 2019, check our [release notes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/release-notes) to find out the latest qualified Windows OS image version for a given Anthos release version. See Security patch process.
     * You can't attach any device that uses the IDE controller to the base VM template.
  2. Install VMware Tools on the base Windows VM template if not already installed. See [Manually Install VMware Tools on Windows](https://docs.vmware.com/en/VMware-Tools/12.0.0/com.vmware.vsphere.vmwaretools.doc/GUID-391BE4BF-89A9-4DC3-85E7-3D45F5124BC7.html) in the VMware documentation.

  3. Create a Windows VM template:
         
         gkectl prepare windows \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
             --base-vm-template BASE_WINDOWS_VM_TEMPLATE \
             --bundle-path BUNDLE \
             [--skip-sysprep]
         

Replace the following:

     * ADMIN_CLUSTER_KUBECONFIG: The path to the admin cluster kubeconfig file.

     * BASE_WINDOWS_VM_TEMPLATE: The path to the base Windows VM template

     * BUNDLE: The path to the Google Distributed Cloud bundle file

As part of building the base Windows VM template, `gkectl prepare windows` runs Windows `sysprep`. This generalizes the VM template and cleans up network settings for the VM, and thus helps to avoid IP address conflicts when VMs are cloned from the same template. However, Windows `sysprep` runs as a closed box, so it is hard to handle certain `sysprep` failures.

If you want to build a base Windows VM template without running Windows `sysprep`, include the `--skip-sysprep` in the `gkectl prepare windows` command.

  4. In the last line of the command output, you can find the name of the generated Windows VM template. Make a note of the name for future use. The name has the following format:
         
         Successfully created Anthos Windows VM template "gke-on-prem-windows-server-2019-VERSION"
         


**Note:** The created VM template will be used as the OS image for the Windows node pools and is prepared to trigger a script at first startup, which is required for the node to function correctly. Therefore we recommend that you not do manupulations on this VM template (For example, convert it to a VM, perform some actions and convert it back to a VM template).

### Step 2: Upload Windows container images to a private registry

Omit this step if you are not using a private registry.

You can automate the upload of Windows container images to a private registry using containerd on a Linux admin workstation. But containerd cannot push the Windows container image base layer, which means the base layers must be pulled from the Microsoft registry when pulling the image. To push the base layers, follow the Option 2 steps.

Option 1: If you don't need to manually push the Windows base layer images to the private registry:
    
    
    gkectl prepare --config <var class="edit">ADMIN_CLUSTER_CONFIG</var> --upload-windows-images
    

Replace ADMIN_CLUSTER_CONFIG with the path to the admin cluster configuration file.

The flag `--upload-windows-images` specifies that Windows Container images will be pushed. Only Linux container images will be pushed to the private registry without specifying this flag.

Option 2: If you need to manually push the Windows base layer images to the private registry: 

  * Use a Windows machine with Docker installed, and with access to `gcr.io`, before attempting these steps. You can only pull Windows container images to a Windows machine.
  * Run `docker login` to authenticate to your private registry.
  * Upload the Windows Container images together with their base layers to your private registry, following these steps:

    * Go to the Docker `daemon.json` file on your Windows machine: 
          
          PS C:> cat C:\ProgramData\docker\config\daemon.json
          

    * Add the following lines to configure your Docker `daemon.json` file to allow pushing foreign layers to your private registry:
    
    {
      "allow-nondistributable-artifacts": ["PRIVATE_REGISTRY_NAME"]
    }
    

    * Download the required Windows Container images to your local Windows machine, and then tag and push them to your private registry. The changes you made to the `daemon.json` Docker configuration file mean that the base layer can be pushed to the private registry. To complete these tasks, run the following commands:


    
    
    # Pull the Windows container images
    docker pull gcr.io/gke-on-prem-release/pause-win:gke_windows_pause_20210302_RC00_2019
    docker pull gcr.io/gke-on-prem-release/fluent-bit-win:v1.8.3-gke.1_ltsc2019
    docker pull gcr.io/gke-on-prem-release/gke-metrics-agent-windows:0.3.10-gke.0_2019
    
    # Tag the images to use private registry
    docker tag gcr.io/gke-on-prem-release/pause-win:gke_windows_pause_20210302_RC00_2019 $PRIVATE_REGISTRY_URL/pause-win:gke_windows_pause_20210302_RC00_2019
    docker tag gcr.io/gke-on-prem-release/fluent-bit-win:v1.8.3-gke.1_ltsc2019 $PRIVATE_REGISTRY_URL/fluent-bit-win:v1.8.3-gke.1_ltsc2019
    docker tag gcr.io/gke-on-prem-release/gke-metrics-agent-windows:0.3.10-gke.0_2019 $PRIVATE_REGISTRY_URL/gke-metrics-agent-windows:0.3.10-gke.0_2019
    
    # Push to private registry
    docker push PRIVATE_REGISTRY_URL/pause-win:gke_windows_pause_20210302_RC00_2019
    docker push PRIVATE_REGISTRY_URL/fluent-bit-win:v1.8.3-gke.1_ltsc2019
    docker push PRIVATE_REGISTRY_URL/gke-metrics-agent-windows:0.3.10-gke.0_2019
    

### Step 3: (Required if using proxy) Allowlisting URLs for creating Windows node pools

If your cluster is behind a proxy server, add these URLs to your proxy server allowlist in addition to the [other addresses](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/firewall-rules) that Google Distributed Cloud requires.
    
    
    # Microsoft registry URLs, needed by every Windows node if using GCR
    mcr.microsoft.com
    .data.mcr.microsoft.com
    go.microsoft.com
    winlayers.cdn.mscr.io
    
    # Microsoft WSUS server URLs, needed by `gkectl prepare windows` on the Windows VM
    windowsupdate.microsoft.com
    .windowsupdate.microsoft.com
    .windowsupdate.microsoft.com
    .update.microsoft.com
    .windowsupdate.com
    download.windowsupdate.com
    download.microsoft.com
    .download.windowsupdate.com
    wustat.windows.com
    ntservicepack.microsoft.com
    go.microsoft.com
    dl.delivery.mp.microsoft.com
    
    # Cloudbase-Init URL, needed by `gkectl prepare windows` on the Windows VM
    https://cloudbase.it
    
    # Powershell Gallery URLs, needed by `gkectl prepare windows` on the Windows VM
    psg-prod-eastus.azureedge.net
    az818661.vo.msecnd.net
    devopsgallerystorage.blob.core.windows.net
    .powershellgallery.com
    
    # Windows Update Service, needed by `gkectl prepare windows` on the Windows VM
    onegetcdn.azureedge.net
    sws.update.microsoft.com
    tsfe.trafficshaping.dsp.mp.microsoft.com
    fe3.delivery.mp.microsoft.com
    .prod.do.dsp.mp.microsoft.com
    emdl.ws.microsoft.com
    adl.windows.com
    activation-v2.sls.microsoft.com
    crl.microsoft.com
    ocsp.digicert.com
    ctldl.windowsupdate.com
    login.live.com
    licensing.mp.microsoft.com
    www.msftconnecttest.com
    settings-win.data.microsoft.com
    wdcp.microsoft.com
    smartscreen-prod.microsoft.com
    checkappexec.microsoft.com
    arc.msn.com
    ris.api.iris.microsoft.com
    .tlu.dl.delivery.mp.microsoft.com
    .au.windowsupdate.com
    www.microsoft.com
    fe3.delivery.dsp.mp.microsoft.com.nsatc.net
    cs9.wac.phicdn.net
    geo-prod.do.dsp.mp.microsoft.com
    slscr.update.microsoft.com
    v10.events.data.microsoft.com
    
    # Access for Installing docker, needed by `gkectl prepare windows` on the Windows VM
    dockermsft.azureedge.net
    

**Note:** See a [full list of URLs used by Windows Server](https://docs.microsoft.com/en-us/windows/privacy/manage-windows-1909-endpoints).

### Step 4: Add a Windows node pool to the user cluster configuration file

  1. [Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enabledataplanev2) must be enabled in your user cluster to use Windows node pools. Add the following line to your user cluster configuration file to enable Dataplane V2:
         
         enableDataplaneV2: true
         

  2. Add a Windows node pool to your `nodePools` section in the user cluster configuration file. At least one Linux node pool is required in addition to your Windows node pools. Set the `osImage` and `osImageType` fields to create Windows node pools:



  * `osImage`: Replace WINDOWS_VM_TEMPLATE_NAME with the name of your prepared Windows VM template in step 1, which should be in the same vCenter datastore specified in the user cluster configuration file.
  * `osImageType`: Specify the OS image type to be `windows`.


    
    
    # user-cluster.yaml
    
    nodePools:
    - name: windows-nodepool-1
      cpus: 8
      memoryMB: 16384
      replicas: 3
      bootDiskSizeGB: 100
      osImage: WINDOWS_VM_TEMPLATE_NAME
      osImageType: windows
    

**Note:** Windows Server nodes require more resources than Linux nodes. We recommend the CPU and memory values shown in the preceding example.

### Step 5: Create Windows node pools

Before you create Windows node pools, run a list of preflight validators for Windows. Skip this step if you already have a user cluster. \- (Optional) Run either or both the fast and slow preflight checks, which create a test VM for Windows and validate the Windows VM template:
    
    
    gkectl check-config --config USER_CLUSTER_CONFIG --kubeconfig ADMIN_CLUSTER_KUBECONFIG
    

  * This command is intended for you to run before creating a user cluster. If you already have a user cluster, certain checks might fail. For example, the IP addresses in the `hostconfig.yaml` file might already be in use by existing nodes in your user cluster.
  * Although not recommended, you can skip the Windows preflight checks with the `--skip-validation-windows` flag.
  * Managing Windows node pools is the same as it is for Linux node pools. See [User guide for Windows Server OS node pools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-guide-for-windows-server-os-node-pools). The commands for creating, updating, and upgrading clusters and node pools also remain the same and are listed here.


    
    
    # Create a new cluster
    gkectl create cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config USER_CLUSTER_CONFIG
    
    # Update an existing cluster with the new Windows node pool
    gkectl update cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config USER_CLUSTER_CONFIG
    
    # Upgrade an existing cluster with the new Windows node pool
    gkectl upgrade cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config USER_CLUSTER_CONFIG
    

### Step 6: Validate Windows nodes are running

  1. Check that your Windows nodes have been created and are `Ready`.
         
         kubectl --kubeconfig USER_KUBECONFIG get nodes
         

  2. Diagnose the user cluster to check whether it's healthy.
         
         gkectl diagnose cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG  --cluster-name CLUSTER_NAME
         




## Deploy a Windows Pod

Windows Server nodes are [tainted](https://cloud.google.com/kubernetes-engine/docs/how-to/node-taints) with this key-value pair: `node.kubernetes.io/os=windows:NoSchedule`.

This taint ensures that the GKE scheduler does not attempt to run Linux containers on Windows Server nodes. To schedule Windows Server containers on Windows Server nodes, your manifest file must include this `nodeSelector` section:
    
    
    nodeSelector:
        kubernetes.io/os: windows
    

With `nodeSelector` configured, an admission webhook running in the cluster checks new workloads for the presence of this Windows node selector and when found, applies the following toleration to the workload which allows it to run on the tainted Windows Server nodes:
    
    
    tolerations:
    - key: "node.kubernetes.io/os"
      operator: "Equal"
      value: "windows"
      effect: "NoSchedule"
    

### Step 1: Create an Internet Information Services (IIS) deployment file

Here is a sample configuration, which deploys Microsoft's official IIS image to a single Pod.

Create an IIS file named `iis.yaml` with the following content:
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: iis
      labels:
        app: iis
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: iis
      template:
        metadata:
          labels:
            app: iis
        spec:
          nodeSelector:
            kubernetes.io/os: windows
          containers:
          - name: iis-server
            image: mcr.microsoft.com/windows/servercore/iis
            ports:
            - containerPort: 80
    ---
    apiVersion: v1
    kind: Service
    metadata:
      labels:
        app: iis
      name: iis
    spec:
      ports:
      - port: 80
        protocol: TCP
        targetPort: 80
      selector:
        app: iis
      sessionAffinity: None
      type: LoadBalancer
      loadBalancerIP: [Fill in with an available IP address]
    

### Step 2: Create the deployment and expose it via a service
    
    
    # Create the deployment
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG create -f iis.yaml
    

### Step 3: Validate the Pod

Check the status of the Pod using `kubectl`.
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG get pods
    

Wait until the returned output shows that the Pod has a status of "Running".
    
    
    NAME                   READY     STATUS    RESTARTS   AGE
    iis-5c997657fb-w95dl   1/1       Running   0          28s
    

Get the status of the service, and wait until the external IP field is populated.
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG  get service iis
    

Expected output:
    
    
    NAME   TYPE           CLUSTER-IP    EXTERNAL-IP   PORT(S)        AGE
    iis    LoadBalancer   10.44.2.112   35.x.x.x     80:32233/TCP   17s
    

You can use your browser to open http://EXTERNAL_IP to see the IIS web page!

**Note:** Remember that your Windows container images must be built on Windows Server 2019 to run on the Windows node pools. See [Matching container host version with container image versions](https://docs.microsoft.com/en-us/virtualization/windowscontainers/deploy-containers/version-compatibility?tabs=windows-server-20H2%2Cwindows-10-20H2#matching-container-host-version-with-container-image-versions).

## Upgrade user cluster with Windows node pools

The upgrade process for a user cluster with Windows node pools is similar to that for upgrading Linux-only user clusters, except that you must create a Windows VM template from a base VM template before upgrading.

**Warning:** The base VM template should be an empty Windows Server 2019 VM template. Do not reuse the existing Windows VM template used by the current node pools to build a new VM template.

You can update the patch build version of the base VM template during upgrade by downloading a newer patch version of Windows Server 2019 from Microsoft as a security patch. See Security patch process.
    
    
    gkectl prepare windows --base-vm-template $BASE_WINDOWS_VM_TEMPLATE_NAME --bundle-path BUNDLE_PATH --kubeconfig ADMIN_CLUSTER_KUBECONFIG
    

**Note:** The command prints the new prepared VM template name.

Update the node pool's `osImage` field at the config file with the new VM template name. Run the command below for upgrading the user cluster:
    
    
    gkectl upgrade cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config USER_CLUSTER_CONFIG
    

Replace the following:

  * ADMIN_CLUSTER_KUBECONFIG with the path of your admin kubeconfig file
  * ADMIN_CLUSTER_CONFIG with the path of your admin cluster configuration file



## Accessing Windows nodes

The standard way to access Windows nodes is with a username and password, which differs from Linux nodes, which are typically accessed via ssh key pairs for authentication.

For Windows nodes on vSphere, the username is `Administrator`. The password is generated by the `clusterapi-controller` and stored in the `windows-node-password` secret in the admin cluster's user namespace. The command for getting the password from that secret is:
    
    
    kubectl get secret windows-node-password -n [USER_CLUSTER_NAME] --kubeconfig admin-kubeconfig.yaml -o jsonpath={.data.*} | base64 -d
    

You can also use get the password using the vCenter user interface. Navigate to the VM that you want to log into, and then you can find the password at the `password` vApp property of that VM.

Once you have the username and password, you can access your Windows VM using any of the following approaches:

### Using Remote Desktop Protocol

**Note:** the RDP (Remote Desktop Protocol) access is enabled during the Windows VM template build in `gkectl prepare windows`. You will also need to ensure your firewall rules allow RDP access on TCP port 3389.

Because the RDP has been enabled during the template build, you can access your Windows VM by using a RDP client.

### Using SSH

**Note:** the SSH server is installed during the Windows VM template build in `gkectl prepare windows`. Therefore, you can use ssh to your Windows VM using that SSH server.

To ssh into a Windows VM:
    
    
    ssh Administrator@[VM_IP_ADDRESS]
    

Follow the prompt to type in the password to connect to your VM.

### Transferring files from and to your Windows VM

You can transfer files from and to your Windows VM with the `scp` command:

Upload files to Windows VM:
    
    
    scp [LOCAL_FILE_PATH] Administrator@[VM_IP_ADDRESS]:/[REMOTE_FILE_PATH]
    

Download files from Windows VM:
    
    
    scp Administrator@[VM_IP_ADDRESS]:/[REMOTE_FILE_PATH] [LOCAL_FILE_PATH]
    

Type the password when prompted.

Alternatively, you can also transfer files by using Cloud Storage or using RDP, as described in [Transferring files to Windows VMs](https://cloud.google.com/compute/docs/instances/transfer-files-windows).

## Updating your Windows Server configuration

Containerd and Windows Dataplane V2 are now general availability as of version 1.11.

Docker and Flannel for Windows nodes will be deprecated in a subsequent release. We recommend that you update your configuration now, if applicable, to use containerd and Windows Dataplane V2 instead. See [Update Windows Server configuration](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/updating-general#docker-deprecate).

### Cannot SSH/RDP to the Windows VM

Check if the VM has a network connection by running `Test-NetConnection` on your vCenter web console.

The result should contain `PingSucceeded: true` if there is a network connection. If the VM does not have a network connection, check the network adapter used for this VM. Make sure that the network allows inbound connections to the VM from your workstation where you want to run the SSH/RDP.

### Verify that the kubelet, kube-proxy, and CNI service are running on the Windows VM

Connect to your VM following the steps here and run the following commands, depending on your setup:

  1. For all configurations, run these commands:
         
         # Check that kubelet and kube-proxy services have status 'Running'
         Get-Service kubelet
         Get-Service kube-proxy
         

  2. If your cluster is configured with `windowsDataplaneV2` set to `true`, check that the antrea-agent, ovsdb-server and ovs-vswitchd services are 'Running'.
         
         # Check that CNI services have the status of 'Running'
         Get-Service antrea-agent
         Get-Service ovsdb-server
         Get-Service ovs-vswitchd
         

  3. Otherwise, check that the flanneld process is 'Running':
         
         # Check that the flanneld process exists
         Get-Process flanneld
         




### Using the snapshot tool

Use the snapshot tool to grab the snapshot tarball. This tarball contains the log files on nodes as well as outputs for troubleshooting commands running on the node.
    
    
    gkectl diagnose snapshot --scenario system-with-logs --cluster-name [USER_CLUSTER_NAME] --kubeconfig [PATH_TO_KUBECONFIG]
    

### Windows VM creation fails

Check the logs from the vsphere-controller-manager container in the clusterapi-controllers Pod in the user namespace of the admin cluster.
    
    
    kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG -n USER_CLUSTER_NAME logs clusterapi-controllers-POD_NAME_SUFFIX vsphere-controller-manager
    

Ensure that your VM template is located in the same datacenter and datastore as specified in your user cluster configuration file.

### Windows VM is created, but the node fails to start properly or show up

  * Check the startup logs on the node located at `C:\var\log\startup.log` to see if anything failed to start.

    * If flanneld is not running, try to rerun the startup script located at `C:\etc\startup\startup-script.ps1`
    * If kubelet is not running, check the kubelet logs under `C:\var\log`.
    * If kube-proxy is not running, check the kube-proxy logs under `C:\var\log`.
  * Check if the cloudbase-init has already executed the `UserDataPlugin` before running the startup script.




To check this, get an SSH connection to the Windows VM and run the following command:
    
    
    ls "HKLM:\\Software\Cloudbase Solutions\Cloudbase-Init\id-ovf\"
    

If you find `UserDataPlugin: 1` in the output, that means the cloudbase-init has already executed that plugin, which will cause the startup script execution to be skipped, and windows node won't be bootstrapped at all.

This is usually caused by converting the VM template generated by `gkectl prepare windows` back to an VM and powering it on.

To resolve this, create a new VM template by running `gkectl prepare windows` again and use it for create/upgrade/update windows node pool.

## Logging and Monitoring

Google Distributed Cloud supports [logging and monitoring](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/logging-and-monitoring) for Windows nodes and Pods, as it does for Linux nodes and Pods.

When logging and monitoring are configured, agents are deployed on Windows nodes. These agents collect, process, and export the node's logs and metrics.

### Windows logging Agent

The Windows logging agent collects the following logs:

  * Pod resource type: system and user application workloads.

Note that Windows user application workloads logs are collected by default. To disable application logs:

    * Edit the `fluent-bit-windows-config` configmap and comment out the `[Input]` item that collects the application logs (the first `[Input]` item): 
          
          kubectl --kubeconfig KUBECONFIG edit configmap fluent-bit-windows-config -n kube-system
          

Make sure to comment out all fields under this item. For example: 
          
          #    [INPUT]
          #      # https://docs.fluentbit.io/manual/input/tail
          #      Name               tail
          #      Tag_Regex          var.log.containers.(?<pod _name >[a-z0-9](?:[-a-z0-9]_[a-z0-9])?(?:.[a-z0-9]([-a-z0-9]_[a-z0-9])?)*)_(?<namespace _name >[^_]+)_(?<container_name>.+)-(?<docker_id>[a-z0-9]{64}).log$
          #      Tag                k8s_container.<namespace_name>.<pod_name>.<container_name>
          #      Path               C:\var\log\containers\*.log
          #      Exclude_Path       __kube-system__.log,__gke-connect__.log,__knative-serving__.log,__gke-system__.log,__istio-system__.log,__monitoring-system__.log,__config-management-system__.log,__gatekeeper-system__.log,__cnrm-system__.log
          #      DB                 C:\var\log\fluent-bit-k8s-container-application.db
          #      Mem_Buf_Limit      30MB
          #      Skip_Long_Lines    On
          #      Refresh_Interval   10
          #      # storage.type       filesystem
          #      Buffer_Chunk_Size  512KB
          #      Buffer_Max_Size    5M
          #      Rotate_Wait        30
          #      Ignore_Older       4h
          

    * Run the `rollout restart` command to restart the `fluent-bit-windows` daemonset: 
          
          kubectl --kubeconfig KUBECONFIG rollout restart daemonset fluent-bit-windows -n kube-system
          

  * Node resource type: kubelet, kube-proxy and Windows event-logs




You can access logs using the [Logs Explorer](https://console.cloud.google.com/logs/) in the console. See [Access logs](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/logging-and-monitoring#access_logs) for more information.

### Windows monitoring Agent

The Windows monitoring agent collect a different set of CPU and memory usage metrics than the Linux monitoring agent. To monitor the Windows nodes and Pods status, use the prepared dashboards. From the console, select Monitoring > Dashboards, and then select "GKE on-prem Windows node status" and "GKE on-prem Windows pod status" from the **All Dashboards** list.

These dashboards are automatically created during admin cluster installation if Cloud Monitoring is enabled. If you already have an admin cluster running, follow [these instructions](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/logging-and-monitoring#dashboards) to create these dashboards, using the following json files:

  * [windows_pod_status.json](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/vmware/docs/windows_pod_status.json)
  * [windows_node_status.json](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/vmware/docs/windows_node_status.json)



See the [full list of metrics](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/windows-agent-metrics) collected by the Windows agents.

## Windows persistent storage

When working with Windows Server containers with persistent storage, you must create a `StorageClass` object, and specify the name of that object in the `storageClassName` field of the [`PersistentVolumeClaim`](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) object, because the default `StorageClass` in on-prem user cluster uses `ext4` as the file system type, which only works for Linux containers. For Windows, we need to set the file system type to `ntfs`.

Example Windows storage class:
    
    
    kind: StorageClass
    apiVersion: storage.k8s.io/v1
    metadata:
      name: my-storage-class
    provisioner: kubernetes.io/vsphere-volume
    parameters:
      datastore: my-datastore
      diskformat: thin
      fstype: ntfs
    

CSI proxy is deployed automatically onto Windows nodes. You can [install and use a Windows CSI driver](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/install-csi-driver) of your choice, such as the [SMB CSI driver](https://github.com/kubernetes-csi/csi-driver-smb/blob/master/deploy/example/e2e_usage.md).

## Node Problem Detector on Windows nodes

The [Node Problem Detector daemon](https://kubernetes.io/docs/tasks/debug-application-cluster/monitor-node-health/) is available on Windows nodes. If you have upgraded to version 1.9, Node Problem Detector is enabled automatically. Node Problem Detector helps with quick detection of some common node problems. Node Problem Detector keeps checking for possible problems and reports them as events and conditions on the node. When a node misbehaves, you can use the `kubectl` command to find corresponding events and conditions.

The following monitor configurations are enabled for Node Problem Detector:

  * [windows-health-checker-kubelet](https://github.com/kubernetes/node-problem-detector/blob/master/config/windows-health-checker-kubelet.json)
  * [windows-health-checker-kubeproxy](https://github.com/kubernetes/node-problem-detector/blob/master/config/windows-health-checker-kubeproxy.json)
  * [windows-health-checker-docker](https://github.com/kubernetes/node-problem-detector/blob/master/config/windows-health-checker-docker.json)
  * [windows-health-checker-containerd](https://github.com/kubernetes/node-problem-detector/blob/master/config/windows-health-checker-containerd.json)
  * [windows-defender-monitor](https://github.com/kubernetes/node-problem-detector/blob/master/config/windows-defender-monitor.json)



To get events and conditions on a node:
    
    
    kubectl --kubeconfig KUBECONFIG describe nodes NODE_NAME
    

Replace:

  * KUBECONFIG with the path of the kubeconfig file for the cluster that contains the node.
  * NODE_NAME with the name of the node.



To identify the events generated by the Node Problem Detector monitors, look for the monitor name in the `reason` field of a rule specified in the `rules` section.

Node Problem Detector monitors also generate the following conditions on the node. Each of these is set to `true` if Node Problem Detector detects the corresponding failure scenario on the node.

  * `KubeletUnhealthy`
  * `KubeProxyUnhealthy`
  * `ContainerRuntimeUnhealthy`



Whenever one of the conditions is set to `true`, the node's Ready condition will become `false`, which prevents new Pods from being scheduled on the node.

When an unhealthy condition is found, Node Problem Detector attempts to auto-repair the node by restarting the relevant system service.

**Note:** For containerd, Node Problem Detector only surfaces problems to the API server and does not attempt to auto-repair the node by restarting the containerd service.

Node Problem Detector logs are located in the node's `C:\var\log\node-problem-detector` folder. If logging and monitoring are enabled, the log is exported to Cloud Logging and you can view them in the Logs Explorer.

Use this filter to get Node Problem Detector logs in Logs Explorer:
    
    
    resource.type="k8s_node"
    log_name="projects/PROJECT_NAME/logs/node-problem-detector"
    

Replace PROJECT_NAME with the project name.

## Security patch process

Besides the regular patch releases for the supported Anthos versions, the Anthos team also continuously qualifies newer Windows patch updates during non-release time periods, and publishes the results for your reference. If an urgent security patch update is needed between Anthos patch releases, you can build a new VM template using the latest version, and then perform a rolling update for the existing Windows node pools to use the new template.

The security patch process includes these steps:

  * Microsoft releases a new security patch for Windows Server 2019.
  * Anthos qualifies the latest security patch version and announces the qualification result.
  * If qualified, users will: 
    * Download the latest patch version from Microsoft
    * Build a new Windows VM template using this patch version following the steps here.
    * Update the Windows node pools to use the new template by running:


    
    
    gkectl update cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config USER_CLUSTER_CONFIG
    

  * If the new version requires changes from Anthos's side, you must wait for the next monthly Anthos patch release and upgrade the clusters.

  * If the new Windows version is not compatible with Anthos at all, the Anthos team will skip that version and wait for the next security update from Microsoft.




## Active Directory domain join

Active Directory domain join requires the length of the VM hostname to be <= 15 characters. For IPAM mode, because the VM hostname is set in the user cluster configuration file, you must ensure the length is <= 15 characters. These instructions are based on the instructions for creating Windows node pools, with the additional step of supplying a customized script during the Windows VM template build.

### Verify the Active Domain DNS server is reachable

Active Directory Domain Services (AD DS) uses Domain Name System (DNS) name resolution services to make it possible for clients to locate domain controllers and for the domain controllers that host the directory service to communicate with each other.

The DNS server was created when the AD DS role installed the root forest. For any Windows VM to join the AD domain, it must be able to reach the DNS server. Configure the DNS and firewall configurations following the guidance of the DNS service provider that you are using. You can verify whether the Windows VMs in the current network can contact the AD domain DNS server by running this command:
    
    
    PS C:\> nslookup DOMAIN_NAME DOMAIN_SERVER_IP
    Server:  example-1-2-3-4.anthos
    Address:  1.2.3.4
    Name:    example.org
    Address:  1.2.3.4
    

### Step 1: Create Windows VM template with a customized script

  1. Execute a customized script before the Windows node joins the user cluster for Active Directory domain join. Store this script to a local path on your admin workstation. Note that:

     * You can replace the script with your own script for doing the Active Directory domain join.
     * It is recommended that you use a user account with the minimum permissions required for an Active Directory domain join, instead of using an Administrator user.
     * (Optional) To avoid storing the password as cleartext in this script, place the password in a file on the VM template, let the script read from that password file, then delete the file after the domain join.
    
    $domain = "[DOMAIN_NAME]"
    $password = "[PASSWORD]" | ConvertTo-SecureString -asPlainText -Force
    $username = "$domain\[USERNAME]"
    $credential = New-Object System.Management.Automation.PSCredential($username,$password)
    Add-Computer -DomainName $domain -Credential $credential -restart –force
    

  2. Create a Windows VM template with a customized script:
         
         gkectl prepare windows --base-vm-template BASE_WINDOWS_VM_TEMPLATE_NAME --bundle-path BUNDLE_PATH --kubeconfig ADMIN_CLUSTER_KUBECONFIG --customized-script CUSTOMIZED_SCRIPT_PATH
         




Replace BUNDLE_PATH with the path to the bundle.

### Step 2: Create a Windows node pool

Proceed with the standard instructions in Steps 2-6 to create a Windows node pool using the customized Windows VM template.

### Step 3: Verify the Active Domain joining for the Windows nodes

On the AD domain controller VM, run the following command:
    
    
    PS C:\> Get-ADComputer -Filter 'Name -like "user-host-prefix*"'
    
    DistinguishedName : CN=AD-VM-1,CN=Computers,DC=example,DC=org
    DNSHostName       : ad-vm-1.example.org
    Enabled           : True
    Name              : AD-VM-1
    ObjectClass       : computer
    ObjectGUID        : b3609717-d24b-4df6-bccb-26ca8e8b9eb0
    SamAccountName    : AD-VM-1$
    SID               : S-1-5-21-3236879623-1561052741-2808297733-1103
    

### Step 4: Configure Group Managed Service Accounts (optional)

Follow these instructions: [Configure GMSA for Windows Pods and containers](https://kubernetes.io/docs/tasks/configure-pod-container/configure-gmsa/). You can configure GMSA for Windows pods and containers after the nodes are domain joined.

### Troubleshooting

Logs for the customized script execution of cloudbase-init are located at `C:\Program Files\Cloudbase Solutions\Cloudbase-Init\log\cloudbase-init.log`. Look for `LocalScriptPlugin` in the log file, and check the related logs. \- Build a new Windows VM template. \- Update the Windows node pools to use the new template by running:
    
    
    gkectl update cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config USER_CLUSTER_CONFIG
    

## Considerations for Windows containers

Some notable differences between Windows and Linux containers are:

  * Version compatibility of Windows container images and the host/node OS images. 
    * The Windows Server OS version tuple has four parts: major, minor, build, and revision.
    * The Windows server container base image must match the first three parts of the version tuple of the host OS image. The revision need not match, although it is recommended that you update both the host and container base images.
    * Users need to rebuild their container images whenever the OS image version changes
  * Privileged containers and host namespaces are not supported. 
    * Users cannot configure/change nodes by deploying containers, such as Daemonsets.



### Limitations for Google Distributed Cloud on vSphere Windows

  * User clusters must contain at least one Linux node pool.

    * You cannot create a cluster with only a Windows node pool
    * The Linux node pools are required to run critical add-ons.
  * Because 1.5 times more resources are reserved for Windows nodes than Linux nodes, the [allocatable resources](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#node_allocatable) for Windows are lower.

  * The use of Windows nodes might require a larger minimum machine size than the Google Distributed Cloud Linux minimum machine size. Windows nodes typically require more resources because of the higher overhead of running node components/services.




## Known Issues

This section lists known issues with Windows nodes used with Google Distributed Cloud, along with workarounds to avoid or recover from these issues.

### Windows Pods cannot talk to external IP addresses

**Note:** This issue only applies to Flannel (with WindowsDataplaneV2 disabled). This issue does not occur with WindowsDataplaneV2 enabled.

This issue is described in [Microsoft documentation](https://docs.microsoft.com/en-us/virtualization/windowscontainers/kubernetes/common-problems#my-windows-pods-cannot-ping-external-resources), which states "You need to exclude the external IP you are trying to query from the ExceptionList."

Contact Google Cloud Support to proceed with a workaround solution.

### Windows containers are not cleaned up after removing Windows Pods

This is a known issue, in which docker `RemoveContainer` also tries to call `CreateFile` on Windows. As a workaround, log in to the Windows node that has the issue, run `Restart-Service docker` and the issue should be mitigated. From Google Distributed Cloud 1.9, the fluent-bit-win container image version and docker version have been updated to pick up the upstream fixes for this issue, this shouldn't reproduce any more. If you encounter this issue, contact Google Cloud Support.

### Windows nodes having IP address conflicts

This is a known issue that happens very rarely, if you encounter this during Windows node pool creation, you can mitigate this following the steps:

  * If you are using IPAM mode, you can manually remove the VMs that having IP conflicts from vCenter, new VMs will be created automatically which should have correct IP allocations. Or you could just wait for the node auto repair to detect this issue and recreate the Windows nodes.

  * If you are using DHCP mode, the newly created VMs are likely to have duplicated IPs again since the DHCP server is encountering issues for IP allocation, you can delete the pending Windows node pool by running `gkectl update cluster`, and add it back in user-cluster.yaml, run `gkectl update cluster` again for creating it, the newly created node pool should have correct IP allocations.




### Windows node becomes NotReady after rebooting the VM

Currently, the node startup script only runs the first time the VM is powered on, so if you reboot the VM, the startup script does not run again. This will cause some Windows services to stop running, including the kubelet, kube-proxy services, and so forth. This causes the node to be in `NotReady` status. If you are using Windows Dataplane V2, the stale network also needs to be cleaned up before the Dataplane V2 services can restart, and it will require running a script for cleanup, which might cause complications. Therefore, re-create the node instead. As a workaround, you can delete the node by running the command below and wait for the controller to automatically recreate it.
    
    
    kubectl --kubeconfig USER_KUBECONFIG delete node NODE_NAME
    

### Diagnose command fails when Windows VM hardware versions are lower than expected

When the Windows VM template is using an old hardware version, the `gkectl diagnose cluster` command fails with the following message:
    
    
    Checking storage...FAILURE
        Reason: 1 storage error(s).
        Unhealthy Resources:
        CSIPrerequisites [VM Hardware]: The current VM hardware versions are lower than vmx-15 which is unexpected. Please contact Anthos support to resolve this issue. Use --detailed=true for the list of VMs.
        Debug Information:
        {
          "NODE_NAME": "vmx-XX",
        }

To fix this issue, follow these steps:

  1. Rename the VM template currently in use.

This is needed to be able to create a new VM template in the next steps.

  2. Convert the Windows **base VM template** to a VM.

  3. Follow the steps in [Upgrading a virtual machine to the latest hardware version](https://kb.vmware.com/s/article/1010675) to upgrade the hardware version of the VM.

  4. Convert the VM back to a VM template.

  5. Run the following command to prepare a new VM template, using the upgraded VM template from previous steps as the **base VM template**.
         
         gkectl prepare windows
         

The new generated VM template name should match the windows node pool `osImage` field value in the user cluster config file. If the values match, continue to the next step to recreate the Windows node.

If the template name doesn't match the `osImage` field value, update the `osImage` value to match the new generated VM template name and run the following command:
         
         gkectl update cluster
         

  6. Re-create the Windows node by running the following command:
         
         kubectl --kubeconfig USER_KUBECONFIG delete node NODE_NAME
         

Wait for the controller to automatically recreate the node.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
