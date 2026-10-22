---
url: https://docs.cloud.google.com/cluster-toolkit/docs/modules/managed-lustre-instance/
title: Create a Managed Lustre instance \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:42:17.363008+00:00
---

# Create a Managed Lustre instance  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/modules/managed-lustre-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Create a Managed Lustre instance Stay organized with collections  Save and categorize content based on your preferences. 

Use the `managed-lustre` module to create a [Managed Lustre](https://docs.cloud.google.com/managed-lustre/docs/overview) instance.

Google Cloud Managed Lustre is a high-performance network file system that you can mount to one or more Compute Engine instances.

You can mount this storage to other modules, such as the [`slurm-partition` module](https://docs.cloud.google.com/cluster-toolkit/docs/modules/slurm-partition), by using the `use` keyword. This keyword handles the client installation and monitoring processes for you.

For the complete list of inputs and outputs, see the [`managed-lustre` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/file-system/managed-lustre#inputs) in the Cluster Toolkit GitHub repository.

## Before you begin

Before you begin, verify that you meet the following requirements:

  * You have installed and configured Cluster Toolkit. For installation instructions, see [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  * You have an existing cluster blueprint. You can use and modify an existing blueprint or create one from scratch. For a working example of a blueprint configured for the `managed-lustre` module, see the [`examples/gke-managed-lustre.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-managed-lustre.yaml) file. For more information about creating and customizing blueprints, see [Cluster blueprint](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint).
  * To view a complete list of blueprints that support the `managed-lustre` module, go to the [Cluster blueprint catalog](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint-catalog) page, click the **Select storage type** menu and then select **Google Cloud Managed Lustre**.
  * The `managed-lustre` module does not create a continuous long-running workload or a full cluster. It provisions a [Managed Lustre](https://docs.cloud.google.com/managed-lustre/docs/overview) instance to provide high-performance network file storage for your cluster.



### Required roles

To get the permissions that you need to create and mount Google Cloud Managed Lustre instances, ask your administrator to grant you the following IAM roles on your project: 

  * [Managed Lustre Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/lustre#lustre.admin) (`roles/lustre.admin`)
  * [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)
  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
  * If importing data from Cloud Storage: [Storage Object Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To ensure that the service account has the necessary permissions to encrypt and decrypt data by using CMEK, ask your administrator to grant the [Cloud Key Management Service CryptoKey Encrypter/Decrypter ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.cryptoKeyEncrypterDecrypter) (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) IAM role to the service account on the Cloud Key Management Service key. **Important:** You must grant this role to the service account, _not_ to your user account. Failure to grant the role to the correct principal might result in permission errors.  For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

Your administrator might also be able to give the service account the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a Managed Lustre instance

To create a Managed Lustre instance, add the `managed-lustre` module to your blueprint.

When you add this module, you can choose one of the following options:

  * Create a new VPC
  * Use an existing VPC



### Create a new VPC

The following example creates a new Virtual Private Cloud (VPC) and configures private service access. Cluster Toolkit passes the VPC network and the private service access configuration to the [`managed-lustre` module](https://docs.cloud.google.com/cluster-toolkit/docs/modules/managed-lustre-instance) to help ensure the correct build order and network configuration.
    
    
      - id: network
        source: modules/network/vpc
    
      - id: private_service_access
        source: modules/network/private-service-access
        use: [network]
        settings:
          prefix_length: 24
    
      - id: lustre
        source: modules/file-system/managed-lustre
        use: [network, private_service_access]
    
    

### Use an existing VPC

If you are using an existing network with private service access already configured, then you must manually provide the peering name by using the `private_vpc_connection_peering` setting. You can find this information in the Google Cloud console on the **VPC network peering** page. For more information, see [Create a peering configuration](https://docs.cloud.google.com/vpc/docs/using-vpc-peering#creating_a_peering_configuration).
    
    
      - id: network
        source: modules/network/pre-existing-vpc
        settings:
          network_name: NETWORK_NAME
          subnetwork_name: SUBNETWORK_NAME
    
      - id: lustre
        source: modules/file-system/managed-lustre
        use: [network]
        settings:
          private_vpc_connection_peering: servicenetworking.googleapis.com
    

Replace the following:

  * `NETWORK_NAME`: the name of your existing VPC network.
  * `SUBNETWORK_NAME`: the name of the subnetwork within that VPC.



## Configure compatibility

You can configure Managed Lustre to be compatible with Slurm.

### Slurm integration

When you use Slurm, the configuration depends on your image type.

  * **Official images:** The official `schedmd-slurm-public` images include pre-installed Managed Lustre client modules.
        
        - id: managed_lustre
          source: modules/file-system/managed-lustre
          use: [network, private_service_access]
          settings:
            name: lustre-instance
            local_mount: /lustre
            remote_mount: lustrefs
            size_gib: 18000
        
        - id: slurm_controller
          source: community/modules/scheduler/schedmd-slurm-gcp-v6-controller
          use: [network, managed_lustre, slurm_login]
          settings:
            machine_type: n2-standard-4
        

The `local_mount` setting specifies the mount point directory for the Managed Lustre instance. If this setting is unspecified, then this value defaults to `/shared`.

  * **Custom images:** For custom images, you must install the modules during the image build. If you are using `slurm-gcp` version 6.10.0 or later, then add the `install_managed_lustre: true` setting to the Ansible playbook variables in your image builder.
        
        - type: data
          destination: /var/tmp/slurm_vars.json
          content: |
            {
              "reboot": false,
              "install_cuda": false,
              "install_gcsfuse": true,
              "install_lustre": false,
              "install_managed_lustre": true,
              "install_nvidia_repo": true,
              "install_ompi": true,
              "allow_kernel_upgrades": false,
              "monitoring_agent": "cloud-ops"
            }
        




## Use Customer-Managed Encryption Keys (CMEK)

Google Cloud Managed Lustre supports encryption with Customer-Managed Encryption Keys (CMEK). To use CMEK, add the `kms_key` setting to the `managed-lustre` module.
    
    
      - id: lustre
        source: modules/file-system/managed-lustre
        use: [network, private_service_access]
        settings:
          kms_key: projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the instance is deployed.
  * `LOCATION`: the region or zone of the instance.
  * `KEY_RING`: The name of the [key ring](https://docs.cloud.google.com/kms/docs/resource-hierarchy#key_rings) that contains the encryption key.
  * `KEY_NAME`: The name of the specific [encryption key](https://docs.cloud.google.com/kms/docs/resource-hierarchy#keys) that is used to encrypt and decrypt your data.



## Import data from Cloud Storage

You can import data from a Cloud Storage bucket when you create a Managed Lustre instance. To do this, use the `import_gcs_bucket_uri` setting to specify the source bucket. The module imports the data into the directory specified by `local_mount` (defaults to `/shared` if unspecified).

Before you import data from Cloud Storage, consider the following:

  * This operation is a one-way copy operation. The Managed Lustre instance does not sync with any subsequent changes made to the Cloud Storage bucket.
  * The copy process runs in the background after Terraform creates the Managed Lustre instance. Data might not appear in the mounted directory immediately after deployment completes.
  * Verify that you have [set up the correct IAM permissions](https://docs.cloud.google.com/managed-lustre/docs/transfer-data#required_permissions) for importing data from Cloud Storage to Managed Lustre. If you don't have the correct permissions, then the copy process might fail silently and leave you with an empty Managed Lustre instance.



### Example configuration

The following example imports data from a specified bucket to the `/lustre` mount point.
    
    
    - id: managed_lustre
      source: modules/file-system/managed-lustre
      use: [network, private_service_access]
      settings:
        name: lustre-instance
        local_mount: /lustre
        remote_mount: lustrefs
        size_gib: 18000
        import_gcs_bucket_uri: gs://BUCKET_NAME
    
    

Replace `BUCKET_NAME` with the name of your Cloud Storage bucket.

### Monitor the import status

If you request an import, then the [`gcluster` tool](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster) outputs a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.lustre.v1.ImportDataMetadata",
        "createTime": "START_TIME",
        "target": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_NAME",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    
    

This output includes the following values:

  * `PROJECT_ID`: the ID of the project where the instance is deployed.
  * `LOCATION`: the region or zone of the instance.
  * `OPERATION_ID`: the unique identifier for the import operation.
  * `START_TIME`: the timestamp when the operation began.
  * `INSTANCE_NAME`: the name of your Managed Lustre instance.



To check the status of the transfer or identify any errors, use the following command:
    
    
    gcloud lustre operations describe OPERATION_ID \
        --location LOCATION \
        --project PROJECT_ID
    

Replace the following:

  * `OPERATION_ID`: the operation ID from the JSON output.
  * `LOCATION`: the location from the JSON output.
  * `PROJECT_ID`: the project ID from the JSON output.



For more information, see [Get operation](https://docs.cloud.google.com/managed-lustre/docs/transfer-data#get_operation).

## What's next

  * For a complete list of input fields and output values, see the [`managed-lustre` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/file-system/managed-lustre#inputs) on GitHub.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
