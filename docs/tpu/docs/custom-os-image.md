---
url: https://docs.cloud.google.com/tpu/docs/custom-os-image/
title: Use a custom OS image \u00a0|\u00a0 Cloud TPU \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:13.588130+00:00
---

# Use a custom OS image  |  Cloud TPU  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/custom-os-image/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use a custom OS image

You can use a custom OS image for your TPU VMs to pre-load software, use a specific OS distribution, or apply custom kernel modifications. Creating a custom image involves making specific system modifications during the image creation process and configuring the image to handle boot-time tasks required for TPU functionality.

**Important:** The system modifications, scripts, and configuration steps listed in this document are validated **only** for the specific Ubuntu versions certified by Google. For a list of supported versions, see [Google-managed OS images](https://docs.cloud.google.com/tpu/docs/tpu-os-images#google-managed_os_images). These instructions are Ubuntu-specific and are **not** validated for other operating system distributions or other Ubuntu versions.

Keep the following disclaimers in mind if you use a custom OS image with TPUs:

  * Google provides default TPU-optimized Ubuntu long-term support (LTS) images. The OS changes listed on this page are only validated for the Google-supported, TPU-optimized Ubuntu LTS images.
  * You are responsible for extrapolating the required OS changes for any other OS distribution or custom images. Google doesn't guarantee that the modifications for Ubuntu listed on this page work with other OS distributions or another Ubuntu image with a custom kernel.
  * Google doesn't build or provide testing for any OS images other than the default TPU-optimized Ubuntu LTS images. You must build and test your custom OS image.



For more information about the default TPU-optimized Ubuntu LTS images, see [TPU OS images](https://docs.cloud.google.com/tpu/docs/tpu-os-images).

## Prerequisites

Your base image must have the following components installed:

  * Python 3
  * gcloud CLI



## Make modifications during image creation

Apply the following modifications while building your custom Ubuntu image.

### Bind TPU devices to VFIO

To allow the guest OS to access TPU hardware, you must bind TPU devices to the [`vfio-pci` driver](https://docs.kernel.org/driver-api/vfio.html).

  1. Create a udev rules file named `99-tpu-vfiopci.rules` in `/etc/udev/rules.d/`:
         
         # Rules for binding vfio-enabled TPU devices to vfio-pci.
         
         # v5p
         SUBSYSTEM=="pci", ACTION=="add", ATTRS{vendor}=="0x1ae0", ATTRS{device}=="0x0062", ATTRS{subsystem_vendor}=="0x1ae0", ATTRS{subsystem_device}=="0x00ad", DRIVER!="vfio-pci", TAG+="bind_to_vfio_pci"
         
         # v6e
         SUBSYSTEM=="pci", ACTION=="add", ATTRS{vendor}=="0x1ae0", ATTRS{device}=="0x006f", ATTRS{subsystem_vendor}=="0x1ae0", ATTRS{subsystem_device}=="0x00d1", DRIVER!="vfio-pci", TAG+="bind_to_vfio_pci"
         
         # TPU7x
         SUBSYSTEM=="pci", ACTION=="add", ATTRS{vendor}=="0x1ae0", ATTRS{device}=="0x0076", ATTRS{subsystem_vendor}=="0x1ae0", ATTRS{subsystem_device}=="0x00f2", DRIVER!="vfio-pci", TAG+="bind_to_vfio_pci"
         
         # Bind all 'bind_to_vfio_pci' tagged devices to vfio-pci.
         TAG=="bind_to_vfio_pci", RUN+="/lib/udev/bind_to_vfio_pci.sh $kernel"
         

  2. Create a script named `bind_to_vfio_pci.sh` in `/lib/udev/`:
         
         #!/bin/bash
         #!/usr/bin/env bash
         
         # Run ./bind_to_vfio_pci.sh <DBDF>
         # Binds the device at <DBDF> to vfio-pci.
         # If the device is already bound to a driver, unbinds it first.
         
         # Load the vfio-pci module into the kernel. No-op if already loaded.
         modprobe vfio-pci
         
         DBDF_REGEX="^[[:xdigit:]]{4}:[[:xdigit:]]{2}:[[:xdigit:]]{2}.[[:xdigit:]]$"
         
         unset BDF
         if [[ $1 =~ $DBDF_REGEX ]]; then
             BDF=$1
         else
             echo "Error: BDF arg ($1) is not in form dddd:bb:dd.f"
             exit 1
         fi
         
         PCI_PATH="/sys/bus/pci/devices/$BDF"
         
         echo "vfio-pci" > "$PCI_PATH/driver_override"
         
         PCI_DRIVER_PATH="$PCI_PATH/driver"
         if [[ -d "$PCI_DRIVER_PATH" ]]; then
             curr_driver=$(readlink "$PCI_DRIVER_PATH")
                 curr_driver=${curr_driver##*/}
             if [[ $curr_driver == "vfio-pci" ]]; then
                 echo "$BDF already bound to vfio-pci"
                 exit 0
             else
                 echo "$BDF" > "$PCI_DRIVER_PATH/unbind"
                 if [[ -d "$PCI_DRIVER_PATH" ]]; then
                     echo "Error: Unable to unbind $PCI_DRIVER_PATH"
                     exit 1
                 fi
                 echo "Unbound $BDF from driver $curr_driver"
             fi
         fi
         echo "$BDF" > /sys/bus/pci/drivers_probe
         echo "Bound $BDF to vfio-pci"
         
         # Grant read/write access on VFIO device to all users
         IOMMU_GROUP=$(readlink "$PCI_PATH/iommu_group" | xargs basename)
         VFIO_DEV="/dev/vfio/$IOMMU_GROUP"
         if [[ -c "$VFIO_DEV" ]]; then
             chmod 0666 "$VFIO_DEV"
         else
             echo "$VFIO_DEV not found"
             exit 1
         fi
         
         # Set allow_unsafe_interrupts for x86 platforms.
         (uname -a | grep -q x86_64) && echo 1 > /sys/module/vfio_iommu_type1/parameters/allow_unsafe_interrupts
         
         # This is only needed to avoid non-zero exit code from previous command.
         echo "All Done!"
         

  3. Make the script executable:
         
         chmod +x /lib/udev/bind_to_vfio_pci.sh
         

  4. Grant all users on the system access to the TPU device:
         
         echo 'KERNEL=="accel*" MODE="0666"' >> /etc/udev/rules.d/99-tpu.rules
         




### Modify the image to enhance performance

To ensure optimal performance, adjust the following system limits and parameters.

#### Memory limits

Allow a single process to lock unlimited memory by updating `/etc/security/limits.conf`:
    
    
    echo '*  hard  memlock  unlimited' >> /etc/security/limits.conf
    echo '*  soft  memlock  unlimited' >> /etc/security/limits.conf
    

#### File limits

Increase the number of open files by updating `/etc/security/limits.conf`:
    
    
    echo "*    soft    nofile       100000" >> /etc/security/limits.conf
    echo "*    hard    nofile       100000" >> /etc/security/limits.conf
    echo "root soft    nofile       100000" >> /etc/security/limits.conf
    echo "root hard    nofile       100000" >> /etc/security/limits.conf
    

#### Kernel parameters

Update your GRUB configuration (typically in `/etc/default/grub`) to include the following parameters in `GRUB_CMDLINE_LINUX`:

  * `idle=poll`: Prevents the CPU from entering low-power idle states.
  * `intel_iommu=on,sm_on`: Enables Intel Input-Output Memory Management Unit (IOMMU). Required for TPU7x and v5p architectures.
  * `transparent_hugepage=always`: Enables Transparent Huge Pages (THP).



The following steps show how to update these kernel parameters:

  1. Prevent the CPU from moving into a low power idle state by setting the following variable, which you will use in the next step.
         
         kernel_cmdline="idle=poll"
         

  2. Enable the Intel Input-Output Memory Management Unit (IOMMU). This step is required for TPU7x and TPU v5p. 
         
         kernel_cmdline="${kernel_cmdline} intel_iommu=on,sm_on";
         sed -i "s/GRUB_CMDLINE_LINUX=\"\"/GRUB_CMDLINE_LINUX=\"${kernel_cmdline}\"/" /etc/default/grub
         echo "Status: New kernel cmdline: $(cat /etc/default/grub | grep -e '^GRUB_CMDLINE_LINUX=')"
         
         update-grub
         

  3. Enable Transparent Huge Pages (THP):
         
         echo "Status: Enabling THP"
         sed -i -r 's/GRUB_CMDLINE_LINUX="[a-zA-Z0-9_= ]*/& transparent_hugepage=always/' /etc/default/grub
         
         update-grub
         




## Install vBar agent

The vBar agent is required for the inter-chip interconnect (ICI) network to function.

**Note:** Skip this section if you are building a custom OS image for use with Google Kubernetes Engine. GKE installs and manages the vBar agent for you, and installing it in the image can conflict with the version that GKE provides.

To install the vBar agent, run the following commands:

  1. Authenticate Docker with Artifact Registry:
         
         gcloud auth configure-docker us-docker.pkg.dev
         

  2. Pull the Docker image from Artifact Registry:
         
         docker pull gcr.io/cloud-tpu-v2-images/vbar_control_agent:0.0.1
         

  3. Run a container using the vBar agent image:
         
         docker run --privileged --net=host vbar_control_agent:0.0.1
         




## Optional: Install and run AI Telemetry Collector

The AI Telemetry Collector runs inside the TPU VM and lets you access runtime and infrastructure metrics through Cloud Monitoring or through your own Prometheus-based monitoring pipeline. You can use the AI Telemetry Collector with a custom OS by using the `ai-telemetry-collector` Docker image. You can install the image onto your custom OS and use a `config.yaml` file to dictate the collection intervals, enable or disable specific metrics, or change the export destinations.

**Note:** Skip this section if you are building a custom OS image for use with Google Kubernetes Engine. GKE installs and manages the AI Telemetry Collector for you.

To install the AI Telemetry Collector, run the following commands:

  1. Authenticate Docker with Artifact Registry:
         
         gcloud auth configure-docker us-docker.pkg.dev
         

  2. Pull the Docker image from Artifact Registry:
         
         docker pull gcr.io/cloud-tpu-v2-images/ai-telemetry-collector:latest
         

  3. Run a container using the AI Telemetry Collector image with the default configuration:
         
         docker run --privileged --net=host ai-telemetry-collector:latest
         

For information about using a custom configuration file or adding additional configuration files, see [AI Telemetry Collector](https://docs.cloud.google.com/tpu/docs/monitor-tpu#telemetry-collector).




## Make boot time modifications

Configure your image to perform the tasks in the following sections every time a VM boots. You can use the [`cloud-init`](https://docs.cloud-init.io/en/latest/index.html) tool to configure boot time tasks by passing metadata to your instances. The configurations in the following sections use modules such as [`write_files`](https://cloudinit.readthedocs.io/en/latest/reference/modules.html#write-files) and [`runcmd`](https://cloudinit.readthedocs.io/en/latest/reference/modules.html#runcmd). Snippets that define files to be written should be included under the `write_files:` key, and commands that should be run at boot time should be included under the `runcmd:` key in your `cloud-init` configuration.

### Start the vBar agent

**Note:** Skip this section if you are building a custom OS image for use with Google Kubernetes Engine. GKE runs and manages the vBar agent for you.

Initiate the vBar control agent with the appropriate user and group IDs:
    
    
    vbar_control_agent --logtostderr --gid= --uid=  --chroot= --census_enabled=false --loas_pwd_fallback_in_corp
    

### Configure environment variables

To ensure your environment is correctly initialized for TPU workloads, you must retrieve runtime configuration variables from the Compute Engine metadata server during the system boot process. To do this, add the following snippet to the `write_files:` section of your `cloud-init` configuration, which creates a script named `/var/scripts/configure-env-vars.sh`. This script automates retrieval of attributes from the `tpu-env` metadata key and saves them in `/${HOME}/tpu-env` to be used by the TPU software stack.
    
    
     - path: /var/scripts/configure-env-vars.sh
        permissions: 0444
        owner: root
        content: |
          grep -q CLOUDSDK_PYTHON /etc/environment || echo "CLOUDSDK_PYTHON=/usr/bin/python3" >> /etc/environment
    
          export HOME=/home/tpu-runtime
          curl -s 'http://metadata.google.internal/computeMetadata/v1/instance/attributes/tpu-env' -H 'Metadata-Flavor: Google' > /tmp/tpu-env.yaml
    
          eval $(python3 -c '''
          import yaml
          stream_in=open("/tmp/tpu-env.yaml", "r")
          for k,v in yaml.safe_load(stream_in).items():
            print("{var}=\"{value}\"".format(var = k, value = str(v)))
          ''' > "/${HOME}/tpu-env"
          )
    
          rm -f "/tmp/tpu-env.yaml"
    
          printenv
          cat ${HOME}/tpu-env
    

### Get VM metadata

The following snippet creates a script named `/var/scripts/get-vm-metadata.py`, a Python utility to programmatically query the metadata server for specific instance attributes and custom metadata tags. Add the following to the `write_files:` section of your `cloud-init` configuration:
    
    
     - path: /var/scripts/get-vm-metadata.py
        permissions: 0444
        owner: root
        content: |
          import sys, requests, os
    
          if len(sys.argv) < 2:
            sys.stderr.write('Must provide key')
            os._exit(1)
    
          key = sys.argv[1]
          default = None
          if len(sys.argv) > 2:
            default = sys.argv[2]
    
          attribute_type = 'attributes'
          if len(sys.argv) > 3:
            attribute_type = sys.argv[3]
    
          request = requests.get("http://metadata.google.internal/computeMetadata/v1/instance/{}/{}".format(attribute_type, key), headers={'Metadata-Flavor': 'Google'})
          if request.status_code == 200:
            print(request.content)
          elif request.status_code == 404 or request.status_code == '403':
            sys.stderr.write('Metadata key: {} does not exist\n'.format(key))
            if default:
              print(default)
          else:
            sys.stderr.write('Lookup failed with: {}'.format(request))
    

### Increase Cloud Storage timeouts

If your workload interacts with Cloud Storage, increase timeout durations by adding timeout values to `/etc/environment`. To do this, add the following snippet to the `write_files:` section of your `cloud-init` configuration, which creates a script named `/var/scripts/configure-gcs-timeouts.sh`.
    
    
     - path: /var/scripts/configure-gcs-timeouts.sh
        permissions: 0444
        owner: root
        content: |
          echo "GCS_RESOLVE_REFRESH_SECS=60" >> /etc/environment
          echo "GCS_REQUEST_CONNECTION_TIMEOUT_SECS=300" >> /etc/environment
          echo "GCS_METADATA_REQUEST_TIMEOUT_SECS=300" >> /etc/environment
          echo "GCS_READ_REQUEST_TIMEOUT_SECS=300" >> /etc/environment
          echo "GCS_WRITE_REQUEST_TIMEOUT_SECS=600" >> /etc/environment
    

## What's next

  * Review available [TPU OS images](https://docs.cloud.google.com/tpu/docs/tpu-os-images).
  * Learn how to [Manage TPU VMs](https://docs.cloud.google.com/tpu/docs/managing-tpus-compute).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
