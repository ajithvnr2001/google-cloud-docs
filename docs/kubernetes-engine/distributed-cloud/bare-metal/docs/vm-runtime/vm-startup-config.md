---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/vm-startup-config/
title: Configure VM startup routines \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:31.295057+00:00
---

# Configure VM startup routines  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/vm-startup-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Configure VM startup routines Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

When you use Google Distributed Cloud version 1.13.0 and later, you can specify startup routines to customize the initialization of your VM on startup. You can configure your VM to create SSH keys, add users and passwords, install packages, write files, configure network settings, and more.

These startup tasks are configured with either the cloud-init API or with startup scripts API (not both). These startup directives are specified in the `VirtualMachine` YAML manifest file and execute automatically each time your VM starts.

## Prerequisites

In order to configure a VM with startup directives, you must meet the following prerequisites:

  * [Enable VM Runtime on GDC](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/enable-disable).

  * Use a [verified Linux guest OS](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/guest-os) and set `osType` to `Linux` in the VM manifest. Windows guest OSes aren't supported for this capability, since they don't support cloud-init.

  * Ensure that the guest OS has cloud-init installed. Most recent Linux OSes include cloud-init.




The following sections describe how to specify startup routines in the VM manifest with either the cloud-init API or startup scripts.

## Use the cloud-init API to initialize VMs

[Cloud-init](https://cloudinit.readthedocs.io/en/latest/) is commonly used for cloud instance initialization and for customizing VMs during startup. VM initialization typically involves tasks like package installations, repository setup, SSH key creation, writing data out to files, and setting up other aspects of your VM. You incorporate cloud-init configuration YAML into the `VirtualMachine` custom resource with the `spec.cloudInit` field. When your VM instance starts, cloud-init reads the provided data and initializes the VM accordingly.

Note the following details of our cloud-init implementation:

  * You specify cloud-init data in the `VirtualMachine` YAML manifest when you create or update a VM. For instructions to create a VM by applying a manifest, see [Tutorial: Create and manage a Linux VM in VM Runtime on GDC](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/tutorial-create-vm).

  * We use the [`NoCloud` data source](https://cloudinit.readthedocs.io/en/latest/reference/datasources/nocloud.html), `spec.cloudInit.noCloud`, in our VM spec.

  * You specify user data and network data in separate sections in the `VirtualMachine` manifest. The section naming and structure depend upon the data format you decide to use.

  * You can specify cloud-init configuration information in the following data formats:

    * Clear text
    * Base64-encoded string
    * Kubernetes Secret

**Note:** You can't specify both cloud-init API directives (`spec.cloudInit`) and startup scripts (`spec.startupScripts`) in the same `VirtualMachine` manifest.

To help you get started, we've provided some configuration examples for common VM initialization tasks.

### Cloud-init user data

VM Runtime on GDC supports cloud-init user data in [cloud-config syntax](https://cloudinit.readthedocs.io/en/latest/topics/format.html#cloud-config-data), so begin your user data with `#cloud-config`. You can format the user data as clear text, a base64-encoded string, or a Kubernetes Secret.

**Note:** When using clear text or a base64-encoded string, the maximum size allowed is 2048 bytes. If the user data size is near or greater than 2048 bytes, specify it as a Kubernetes Secret.

For more information about user data syntax and module reference, see the [cloud-init documentation](https://cloudinit.readthedocs.io/en/latest/topics/modules.html).

#### Cloud-init user data as clear text

The following example manifest shows how to specify user data as clear text. In this case, cloud-init executes a command when the VM starts:
    
    
    apiVersion: vm.cluster.gke.io/v1
    kind: VirtualMachine
    metadata:
      name: "my-vm"
    spec:
      ...
      cloudInit:
        noCloud:**      userData: |
            #cloud-config
            runcmd:
              - echo hello**
    

#### Cloud-init user data as a base64-encoded string

The following example shows how to specify user data in base64-encoded format. In this example, the user data consists of the same `echo hello` command as in the clear text example:
    
    
    apiVersion: vm.cluster.gke.io/v1
    kind: VirtualMachine
    metadata:
      name: "my-vm"
    spec:
      ...
      cloudInit:
        noCloud:**      userDataBase64: I2Nsb3VkLWNvbmZpZwpydW5jbWQ6CiAgLSBlY2hvIGhlbGxvCg==**
    

#### Cloud-init user data as a Kubernetes Secret

The following example shows a YAML manifest for both a `VirtualMachine` and a `Secret`. The `spec.cloudInit.noCloud.secretRef` section in the `VirtualMachine` configuration indicates that the cloud-init user data is in a Kubernetes Secret named `my-sec`. The corresponding `Secret` configuration specifies the user data as a key-value pair. The base64-encoded value in this case is the cloud-init user data in cloud-config syntax.

In the referenced Secret, use the data key `userData` (shown) or `userdata` to specify the cloud-init user data.

In this example, the user data consists of the same `echo hello` command as in the clear text example:
    
    
    apiVersion: vm.cluster.gke.io/v1
    kind: VirtualMachine
    metadata:
      name: "my-vm"
    spec:
      ...
      cloudInit:
        noCloud:**      secretRef:
            name: my-sec**
    ---
    apiVersion: v1
    kind: Secret
    type: Opaque
    metadata:
      name: my-sec
    data:
      **userData : I2Nsb3VkLWNvbmZpZwpydW5jbWQ6CiAgLSBlY2hvIGhlbGxvCg==**
    

If the referenced Secret isn't found or the data key `userData` or `userdata` doesn't exist in the Secret, note the following VM startup behavior:

  * For VM creation, the VM is put in an `ErrorConfiguration` state with a detailed reason and message.

  * In other cases, the VM continues to use the old cloud-init user data until the VM is correctly configured. As a result, guest agent enable or disable updates don't take effect until the VM is correctly configured.




To retrieve VM information, including what cloud-init user data was used, use the following command:
    
    
    kubectl get vm VM_NAME -o yaml --kubeconfig KUBECONFIG_PATH
    

Replace the following:

  * `VM_NAME`: the name of your VM.

  * `KUBECONFIG_PATH`: the path to the kubeconfig file for the cluster containing your VM.




To retrieve the related Kubernetes warning event, use either `kubectl get event` or `kubectl describe gvm`.

### Cloud-init network data

Similar to user data, you can format the network data as clear text, a base64-encoded string, or a Kubernetes Secret. Unlike user data, network data doesn't use cloud-config syntax.

When using clear text or a base64-encoded string, the maximum size allowed is 2048 bytes. If the user data size is near or greater than 2048 bytes, specify it as a Kubernetes Secret.

For more information about network data syntax and related details, see the [Networking Config Version 2](https://cloudinit.readthedocs.io/en/latest/reference/network-config-format-v2.html) in the cloud-init documentation.

**Tip:** The following sections illustrate how to specify cloud-init network data in the `VirtualMachine` configuration in different formats. The example network data enables DHCP for all ethernet devices with names that start with an "e". This specific cloud-init directive to enable DHCP is automatically embedded in the VM for you, so you don't need to specify it yourself.

#### Cloud-init network data as clear text

The following example manifest shows how to specify network data as clear text. In this case, cloud-init enables DHCP for all ethernet devices with names that start with an "e" (`e*`):
    
    
    apiVersion: vm.cluster.gke.io/v1
    kind: VirtualMachine
    metadata:
      name: "my-vm"
    spec:
      ...
      cloudInit:
        noCloud:
          userData: |
            #cloud-config
            runcmd:
              - echo hello**      networkData: |
            version: 2
            ethernets:
              alleths:
                match:
                  name: e*
                dhcp4: true**
    

#### Cloud-init network data as a base64-encoded string

The following example shows how to specify network data in base64-encoded format. In this example, the network data consists of the same DHCP configuration specified in the clear text example:
    
    
    apiVersion: vm.cluster.gke.io/v1
    kind: VirtualMachine
    metadata:
      name: "my-vm"
    spec:
      ...
      cloudInit:
        noCloud:
          **networkDataBase64 : dmVyc2lvbjogMgpldGhlcm5ldHM6CiAgYWxsZXRoczoKICAgIG1hdGNoOgogICAgICBuYW1lOiBlKgogICAgZGhjcDQ6IHRydWUK**
    

#### Cloud-init network data as a Kubernetes Secret

The following example shows a YAML manifest for both a `VirtualMachine` and a `Secret`. The `spec.cloudInit.noCloud.networkDataSecretRef` section in the `VirtualMachine` configuration indicates that the cloud-init network data is in a Kubernetes Secret named `my-sec`. The corresponding `Secret` configuration specifies the network data as a key-value pair. The base64-encoded value in this case is the cloud-init network data.

In the referenced Secret, use the data key `networkData` (shown) or `networkdata` to specify the cloud-init network data.

In this example, the network data consists of the same DHCP configuration specified in the clear text example:
    
    
    apiVersion: vm.cluster.gke.io/v1
    kind: VirtualMachine
    metadata:
      name: "my-vm"
    spec:
      ...
      cloudInit:
        noCloud:**      networkDataSecretRef:
            name: my-sec**
    ---
    apiVersion: v1
    kind: Secret
    type: Opaque
    metadata:
      name: my-sec
    data:
      **networkData : dmVyc2lvbjogMgpldGhlcm5ldHM6CiAgYWxsZXRoczoKICAgIG1hdGNoOgogICAgICBuYW1lOiBlKgogICAgZGhjcDQ6IHRydWUK**
    

### Cloud-init examples

The following sections contain clear text examples of some common use cases for VM initialization with cloud-init:

  * Configure authorized SSH keys
  * Add a new user
  * Run commands on the first startup
  * Write files



#### Configure authorized SSH keys

The following user data example assigns the authorized SSH key `ssh-rsa AAAAB3NzaK8L93bWxnyp` to the default user.
    
    
    apiVersion: vm.cluster.gke.io/v1
    kind: VirtualMachine
    metadata:
      name: "my-vm"
    spec:
      ...**  cloudInit:
        noCloud:
          userData: |
            #cloud-config
            ssh_authorized_keys:
              - ssh-rsa AAAAB3NzaK8L93bWxnyp**
    

#### Add a new user

The following user data example creates a user `test` and gives `test` full sudo access. This example assigns the user a non-expiring password of `pwd`.
    
    
    apiVersion: vm.cluster.gke.io/v1
    kind: VirtualMachine
    metadata:
      name: "my-vm"
    spec:
      ...**  cloudInit:
        noCloud:
          userData: |
            #cloud-config
            users:
            - default
            - name: test
              sudo: ALL=(ALL) NOPASSWD:ALL
            chpasswd:
              list: |
                test:pwd
              expire: False**
    

#### Run commands on the first startup

The following user data example runs an `echo` command and an `ls` command. You can use commands to install packages and more when your VM starts.
    
    
    apiVersion: vm.cluster.gke.io/v1
    kind: VirtualMachine
    metadata:
      name: "my-vm"
    spec:
      ...**  cloudInit:
        noCloud:
          userData: |
            #cloud-config
            runcmd:
              - [ echo, hello ]
              - [ ls, -l, / ]**
    

#### Write files

The following user data example writes a bash script to the file `test` in the `/var/lib/google` directory of your VM. The cloud-init directives set the file permissions to read, write, and execute (`0744`) for the file owner.
    
    
    apiVersion: vm.cluster.gke.io/v1
    kind: VirtualMachine
    metadata:
      name: "my-vm"
    spec:
      ...**  cloudInit:
        noCloud:
          userData: |
            #cloud-config
            write_files:
            - path: /var/lib/google/test
              permissions: 0744
              content: |
                #!/bin/bash
                echo hello**
    

### Troubleshooting cloud-init

If you encounter issues with your VM initialization and you're using cloud-init, check the following cloud-init logs in your VM:

  * `/var/log/cloud-init.log`: By default, cloud-init writes all events with a level of `DEBUG` or higher to this log.

  * `/var/log/cloud-init-output.log`: By default, cloud-init directs both stdout and stderr from all cloud-init stages to this log.




## Use startup scripts to initialize VMs

Startup scripts perform tasks during the startup process of a virtual machine (VM) instance. You can specify one or more scripts in the `spec.startupScripts` section of the `VirtualMachine` spec. Startup scripts can be used to initialize your VM. VM initialization typically involves tasks like package installations, repository setup, SSH key creation, writing data out to files, and setting up other aspects of your VM.

Note the following details for startup scripts:

  * You specify startup scripts in the `VirtualMachine` YAML manifest when you create or update a VM. For instructions to create a VM by applying a manifest, see [Tutorial: Create and manage a Linux VM in VM Runtime on GDC](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/tutorial-create-vm).

  * Specified scripts run every time the VM starts.

  * Include `#!/bin/...` at the top of the script to indicate the script interpreter. For example, include `#!/bin/bash` to execute the script with the Bash shell.

  * You can't specify both cloud-init API directives (`spec.cloudInit`) and startup scripts (`spec.startupScripts`) in the same `VirtualMachine` manifest.


**Note:** If you're using Google Distributed Cloud version 1.13.0, you must start the VM twice for startup scripts to take effect under specific circumstances. This VM start behavior applies only when you update an existing VM that has no startup scripts to include startup scripts. This issue is fixed in Google Distributed Cloud release 1.13.1 and higher.

### Script formats

You can specify startup scripts in the following data formats:

  * Clear text
  * Base64-encoded string
  * Kubernetes Secret



Note the following rules for working with different script formats:

  * When using clear text or a base64-encoded string, the maximum size allowed for script contents is 2048 bytes. If your script content size is near or greater than 2048 bytes, specify scripts as a Kubernetes Secret.

  * When using a Kubernetes Secret, use the data key `script` in the referenced Secret to specify the script content.

  * If a referenced Secret isn't found or the data key `script` doesn't exist in the referenced Secret, the VM continues to run the script. The VM doesn't, however, write or update the script content. In this case, you can find the Kubernetes warning event with either `kubectl get event` or `kubectl describe gvm`.




The following sample `VirtualMachine` YAML manifest contains three scripts, one in each of the supported formats. In this case, each script runs the `echo hello` command shown in `myscript1`, the clear text example.
    
    
    apiVersion: vm.cluster.gke.io/v1
    kind: VirtualMachine
    metadata:
      name: "my-vm"
    spec:
      ...
      startupScripts:
      - name: myscript1
        script: |
          #!/bin/bash
          echo hello
      - name: myscript2
        scriptBase64: IyEvYmluL2Jhc2gKICAgICAgZWNobyBoZWxsbwo=
      - name: myscript3
        scriptSecretRef:
          name: my-sec
    ---
    apiVersion: v1
    kind: Secret
    type: Opaque
    metadata:
      name: my-sec
    data:
      script: IyEvYmluL2Jhc2gKICAgICAgZWNobyBoZWxsbwo=
    

### Script troubleshooting

To check the script results or logs, run the following command:
    
    
    journalctl -u cloud-final
    

The startup script log entries begin with the following text:
    
    
    started to run the command /var/lib/google/startup-scripts/SCRIPT_NAME ...
    

The log entry includes `SCRIPT_NAME`, the name of the startup script.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
