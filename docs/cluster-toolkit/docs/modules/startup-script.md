---
url: https://docs.cloud.google.com/cluster-toolkit/docs/modules/startup-script/
title: Use startup scripts \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:32:43.537160+00:00
---

# Use startup scripts  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/modules/startup-script/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Use startup scripts Stay organized with collections  Save and categorize content based on your preferences. 

The `startup-script` module lets you run a sequence of runners during Compute Engine instance initialization. You can automate software installation, configure local environments, and stage data consistently across your cluster.

The module copies the runners to a Cloud Storage bucket during deployment. When the compute instance starts, the module downloads the runners from the bucket and runs them in the order that you specify.

For the complete list of inputs and outputs for this module, see the [`startup-script` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/scripts/startup-script#inputs) page in the Cluster Toolkit GitHub repository.

## Before you begin

Before you begin, verify that you meet the following requirements:

  * You have installed and configured Cluster Toolkit. For installation instructions, see [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  * You have an existing cluster blueprint. You can use and modify an existing blueprint or create one from scratch. For a working example of a blueprint configured for startup scripts, see the [`examples/image-builder.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/image-builder.yaml) file. For more information about creating and customizing blueprints, see [Cluster blueprint](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint).



### Required roles

To get the permissions that you need to deploy the startup scripts and create the storage bucket, ask your administrator to grant you the [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To ensure that the compute instance service account has the necessary permissions to read the startup scripts from Cloud Storage, ask your administrator to grant the [Storage Object Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`) IAM role to the compute instance service account on your project. **Important:** You must grant this role to the compute instance service account, _not_ to your user account. Failure to grant the role to the correct principal might result in permission errors.  For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

Your administrator might also be able to give the compute instance service account the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Configure runners

When you define a runner, you configure specific attributes to determine its behavior:

  * **`destination`:** The destination path on the compute instance. If you provide an absolute path, the module copies the file to that path. Otherwise, the module creates the file in a temporary folder and deletes the file after the startup script runs.
  * **`type`:** The runner type. Use `shell` for shell scripts, `ansible-local` for Ansible playbooks, or `data` to stage files without executing them.
  * **`content`:** The text content to upload. You must specify either the `content` attribute or the `source` attribute.
  * **`source`:** The path to the local file or data to upload. Use the `ghpc_stage` function to ensure correct relative paths to the deployment group directory (for example, `source: $(ghpc_stage("path/to/file"))`). To reference any other source file, use an absolute path.
  * **`args`:** Arguments to pass to `shell` or `ansible-local` runners. For `ansible-local` runners, the module appends these arguments to the default `ansible-playbook` command. Don't include arguments that alter the connection or inventory behavior, such as `--connection` or `--limit`.



### Set Ansible dependencies

The `ansible-local` runners require Ansible on the compute instance. If you configure an `ansible-local` runner, the module automatically prepends a script that installs Ansible and its dependencies in a virtual environment at `/usr/local/ghpc-venv`. You can disable this behavior by setting the `install_ansible` variable to `false`.

To interact with this environment manually, you can activate it by running the following command on the compute instance:
    
    
    source /usr/local/ghpc-venv/bin/activate
    

If you call `ansible-playbook` manually, you must specify the Python interpreter inside the virtual environment by appending the following flag:
    
    
    -e ansible_python_interpreter=/usr/local/ghpc-venv/bin/activate
    

## Stage the runners

By default, the module creates a new Cloud Storage bucket to host the uploaded scripts. To reuse an existing bucket or folder instead, specify the `gcs_bucket_path` setting in your blueprint.

### Configure Cloud Storage access

The compute instances require read access to the Cloud Storage bucket that contains the runners. Ensure that the service account attached to the compute instance has the `https://www.googleapis.com/auth/devstorage.read_only` access scope.

**Note:** The `vm-instance`, `schedmd-slurm-gcp-v6-login`, and `schedmd-slurm-gcp-v6-controller` modules include this scope by default.

## Install monitoring agents

You can configure the `startup-script` module to install a Google monitoring agent by using the `install_stackdriver_agent` setting and the `install_cloud_ops_agent` setting.

Google recommends that you use the `install_stackdriver_agent` setting because the legacy Cloud Monitoring Agent provides better performance for specific high performance computing (HPC) workloads.

To verify that the agent is running, run the corresponding command on your compute instance:
    
    
    # Verify the Cloud Ops Agent
    sudo systemctl is-active google-cloud-ops-agent"*"
    
    # Verify the legacy Cloud Monitoring Agent
    sudo service stackdriver-agent status
    

If you need to switch between the agents manually, see [Troubleshoot Ops Agent installation and start-up](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/troubleshoot-install-startup).

## Create the startup script module

The following example demonstrates how to configure multiple runners, including shell scripts, Ansible playbooks, and data staging. It also demonstrates how to override the default bucket creation by specifying a custom `gcs_bucket_path` value.
    
    
      - id: startup
        source: modules/scripts/startup-script
        settings:
          gcs_bucket_path: gs://user-test-bucket/folder1/folder2
          install_stackdriver_agent: true
          runners:
            - type: ansible-local
              destination: "modules/filestore/scripts/mount.yaml"
              source: "modules/filestore/scripts/mount.yaml"
            - type: data
              source: /tmp/foo.tgz
              destination: /tmp/bar.tgz
            - type: shell
              destination: "decompress.sh"
              content: |
                #!/bin/sh
                echo $2
                tar zxvf /tmp/$1 -C /
              args: "bar.tgz 'Expanding file'"
    
      - id: compute-cluster
        source: modules/compute/vm-instance
        use: [homefs, startup]
    

## Track and debug execution

Debug the startup script on a Linux compute instance:
    
    
    sudo DEBUG=1 google_metadata_script_runner startup
    

View the output logs from the startup script:
    
    
    sudo journalctl -u google-startup-scripts.service
    

## Enable additional environment configurations

The `startup-script` module provides built-in settings to streamline the configuration of dependencies and hardware on your compute instances.

### Install Docker

To install and configure the Docker daemon on your compute instances during initialization, set the `docker` setting to `true`.
    
    
    - id: startup
      source: modules/scripts/startup-script
      settings:
        docker: true
    

### Mount and format local SSDs

To automatically format and mount local SSDs attached to your compute instances, set the `local_ssd_filesystem` setting with your preferred storage parameters.
    
    
    - id: startup
      source: modules/scripts/startup-script
      settings:
        local_ssd_filesystem:
          mount_point: /mnt/local_ssd
          fs_type: ext4
    

### Automate SSH setup

To simplify the secure shell (SSH) configuration between cluster nodes and authorize internal connections without manual intervention, specify target hostnames or wildcard patterns in the `configure_ssh_host_patterns` setting.
    
    
    - id: startup
      source: modules/scripts/startup-script
      settings:
        configure_ssh_host_patterns:
          - "*.internal"
    

### Install Cloud RDMA drivers

If you require Remote Direct Memory Access (RDMA) networking but don't use the pre-configured high performance computing (HPC) VM image, set the `install_cloud_rdma_drivers` setting to `true` to install the necessary network drivers automatically.
    
    
    - id: startup
      source: modules/scripts/startup-script
      settings:
        install_cloud_rdma_drivers: true
    

## What's next

  * For the complete list of inputs and outputs for this module, see the [`startup-script` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/scripts/startup-script#inputs) page in the Cluster Toolkit GitHub repository.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
