---
url: https://docs.cloud.google.com/sap/docs/sap-ibm-db2-ha-deployment-guide/
title: IBM Db2 high-availability cluster for SAP deployment guide \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:01:48.950438+00:00
---

# IBM Db2 high-availability cluster for SAP deployment guide  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/sap-ibm-db2-ha-deployment-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  IBM Db2 high-availability cluster for SAP deployment guide Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows you how to set up Google Cloud resources to run IBM Db2, version 11.5 or earlier, in a high-availability (HA) cluster for SAP on the Linux operating system.

**Note:** To run IBM Db2 version **11.5.8 or later** , you can configure a two-host HADR Pacemaker cluster by using the IBM provided clustering solution for Db2. For more information, see [HA for IBM Db2 versions later than 11.5](https://docs.cloud.google.com/sap/docs/sap-ibm-db2-planning-guide#ibm-db2-ha-recommended).

The instructions in this guide are complementary to the instructions provided by SAP and IBM in [IBM Db2 High Availability Solution: IBM Tivoli System Automation for Multiplatforms](https://help.sap.com/doc/a7ba6b8cc8dc46309c2f93bcfc417133/CURRENT_VERSION/en-US/DB6_SAMP_Guide.pdf) (TSAMP). While installing and configuring an IBM Db2 HA cluster on Google Cloud, always refer to the latest documentation provided by SAP and IBM.

This guide is intended for experienced SAP and IBM Db2 users who are familiar with high-availability clusters.

## System deployed by this guide

The IBM Db2 HA cluster that you deploy by following this guide includes the following components:

  * A primary IBM Db2 server and a secondary or standby IBM Db2 server, each of which are deployed on a separate Compute Engine instance.
  * IBM TSAMP, to monitor the system and initiate appropriate action if the system becomes unresponsive.
  * IBM Db2 high-availability disaster recovery (HADR) function to replicate logged data changes to the standby database.
  * A floating IP address that is implemented by Google Cloud with either a Google Cloud static route or an alias IP address. In this context, the term "floating IP address" is synonymous with the term "virtual IP address", which is used in the SAP documentation.



## Required SAP documentation

The instructions for installing and configuring the SAP and IBM components are provided by SAP in [IBM Db2 High Availability Solution: IBM Tivoli System Automation for Multiplatforms](https://help.sap.com/doc/a7ba6b8cc8dc46309c2f93bcfc417133/CURRENT_VERSION/en-US/DB6_SAMP_Guide.pdf).

Read both the SAP and Google Cloud documentation before you start the procedures in these instructions. At various stages of deployment, you might need to refer to both the SAP and Google Cloud documentation.

## Prerequisites

Before you create the IBM Db2 high-availability cluster, make sure that the following prerequisites are met:

  * You or your organization has a Google Cloud account and you have created a project for the IBM Db2 HA cluster deployment. For information about creating Google Cloud projects, see [Prerequisites](https://docs.cloud.google.com/sap/docs/sap-ibm-db2-deployment-guide#prerequisites) in the IBM Db2 for SAP deployment guide.
  * If you require your SAP workload to run in compliance with data residency, access control, support personnel, or regulatory requirements, then you must create the required Assured Workloads folder. For more information, see [Compliance and sovereign controls for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/compliance-and-sovereign-controls). 
  * You have a Virtual Private Cloud network on Google Cloud. For instructions on configuring a VPC network and firewall rules, as well as instructions for setting up a NAT gateway or bastion host for IBM Db2 for SAP, see [IBM Db2 for SAP deployment guide](https://docs.cloud.google.com/sap/docs/sap-ibm-db2-deployment-guide).

  * If [OS login](https://docs.cloud.google.com/compute/docs/instances/access-overview#oslogin) is enabled in your project metadata, then you need to disable OS login temporarily until your deployment is complete. For deployment purposes, this procedure configures SSH keys in instance metadata. When OS login is enabled, metadata-based SSH key configurations are disabled. After deployment is complete, you can enable OS login again.

For more information, see:

    * [Enabling or disabling OS Login](https://docs.cloud.google.com/compute/docs/instances/managing-instance-access#enable_oslogin)
    * [Add SSH keys to VMs that use metadata-based SSH keys](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys#metadata)



## Deploying an IBM Db2 high-availability cluster on Google Cloud

These instructions show you how to deploy two VMs, define a floating IP address, and configure the alias IP address or Google Cloud routes that support the floating IP address. When you need to install the IBM components, you are referred to the SAP documentation.

The main Google Cloud services that you need to set up for an IBM Db2 high-availability cluster are:

  * A VPC network and subnetwork
  * Firewall rules (if you don't use another form of network access control)
  * Compute Engine VMs and persistent disk storage



You also download and use a Google Cloud helper script when you define the custom resource that TSAMP uses to manage switching the floating IP address between hosts. The script enables TSAMP to interact with Google Cloud APIs.

### About Deployment Manager

In these instructions, you define the resource options for your installation in a Deployment Manager configuration file template.

Deployment Manager treats all of the resources that are created for your SAP system as a single entity called a _deployment_. You can view and work with all of the deployments for your project on the [Deployments](https://console.cloud.google.com/dm/deployments) page in the Google Cloud console.

Be aware of the following behaviors when using Deployment Manager:

  * Deleting a deployment deletes all of the resources associated with the deployment, including the VMs, the persistent disks, and any SAP systems that are installed on the VM.
  * By default, Deployment Manager uses the `ACQUIRE` resource creation policy. If you specify a VM name that is already in use by another VM in your project, Deployment Manager doesn't create a new VM, but instead adds the existing VM to your new deployment. If your original VM was created by a previous run of Deployment Manager, the VM is associated with two deployments.

If you then delete the new deployment, the acquired VM is deleted from the deployment that originally created it. To avoid such a scenario, either set the Deployment Manager resource policy to `CREATE`, or make sure that you use unique resource names in your new deployment.

For information about the policies you can use while creating resources with Deployment Manager and how to specify them, see the [Deployment Manager documentation](https://docs.cloud.google.com/deployment-manager/docs/deployments#create-policy).




### Deploying the VMs for an IBM Db2 HA cluster with Deployment Manager

  1. In Cloud Shell, download the `template_ha.yaml` configuration file template to your working directory:
         
         wget https://storage.googleapis.com/cloudsapdeploy/deploymentmanager/latest/dm-templates/sap_db2/template_ha.yaml

  2. To open the Cloud Shell code editor, click the pencil (_edit_) icon in the upper-right corner of the Cloud Shell terminal window.

  3. Optionally, rename the `template_ha.yaml` file to identify the configuration it defines. For example, `db2_ha_s123_dh1.yaml`.

  4. To open the `template_ha.yaml` in the code editor, double-click it.

  5. Define the VMs and persistent disks in the `template_ha.yaml` file. The `template_ha.yaml` file contains two sections: `sap_db2_primary` and `sap_db2_secondary`. Each section contains a set of property-value pairs followed by comments that include less-frequently used properties.

When you fill out each section, except for the `instanceName`, `zone`, and `otherHost` properties, the definitions for each VM must be identical.

The following table describes the properties included in each section. To use a property, replace the placeholder text and brackets with the values for your installation.

Property | Data type | Description  
---|---|---  
type | String |  Specifies the location, type, and version of the Deployment Manager template to use during deployment.  The YAML file includes two `type` specifications, one of which is commented out. The `type` specification that is active by default specifies the template version as `latest`. The `type` specification that is commented out specifies a specific template version with a timestamp.  If you need all of your deployments to use the same template version, use the `type` specification that includes the timestamp.   
`instanceName` | String | The name of the VM instance on which you install IBM Db2. The name must be 13 characters or less, specified in lowercase letters, numbers, or hyphens.   
`instanceType` | String | The type of Compute Engine [virtual machine](https://docs.cloud.google.com/compute/docs/machine-types) on which you install IBM Db2. Specify a machine type with two or more vCPUs. For example, `n1-standard-4`.   
`zone` | String | The zone in which you are deploying the IBM Db2 instance. It must be in the same region that you selected for your subnetwork.   
`subnetwork` | String | The name of the subnetwork that you created in a previous step. If you are deploying to a shared VPC, specify this value as `shared-vpc-project/SUBNETWORK`. For example, `myproject/network1`.  
`linuxImage` | String | The name of the Linux operating- system image or image family that you are using with IBM Db2. To specify an image family, add the prefix `family/` to the family name. For example, `family/rhel-7-sap-apps` or `family/sles-12-sp3-sap`. To specify an image, enter only the image name. For the list of available image families, see the [Images](https://console.cloud.google.com/compute/images) page in the Google Cloud console.  
`linuxImageProject` | String | The Google Cloud project that contains the image you are going to use. This project might be your own project or a Google Cloud image project, such as `rhel-sap-cloud` or `suse-sap-cloud`. For a list of Google Cloud image projects, see the [Images](https://docs.cloud.google.com/compute/docs/images) page in the Compute Engine documentation.  
`db2SID` | String | The database instance ID.   
`db2sidSize` | Integer | The size in GB of **/db2/ DBSID**, which is the root directory of the database instance. The minimum and default values for `db2sidSize` are both 8 GB.   
`db2homeSize` | Integer | The size in GB of **/db2/db2 db2sid**, which is the home directory of the database instance. The minimum and default values for `db2homeSize` are both 8 GB.   
`db2dumpSize` | Integer | The size in GB of **/db2/ DBSID/db2dump**, which holds the dump files from DB2 that are used for diagnosing problems. The minimum and default values for `db2dumpSize` are both 8 GB.   
`db2saptmpSize` | Integer | The size in GB of **/db2/ DBSID/saptmp**, which holds the database temporary table space. The minimum and default values for `db2saptmpSize` are both 8 GB.   
`db2sapdataSize` | Integer | The size of **/sapdb/ DBSID/sapdata**, which holds the database data files. The minimum and default values for `db2sapdataSize` are both 30 GB.   
`db2logSize` | Integer | The size of **/db2/ DBSID/logdir**, which holds the database transaction logs. The minimum and default values for `db2logSize` are both 8 GB.   
`db2backupSize` | Integer | The size of the **/db2backup** volume. This property is optional. If you set to `0` or omit, no disk is created.   
`db2sapdataSSD` | boolean | Specifies whether the data drive uses an SSD persistent disk (`Yes`) or an HDD persistent disk (`No`). `Yes` is the default.   
`db2logSSD` | boolean | Specifies whether the log drive uses an SSD persistent disk (`Yes`) or an HDD persistent disk (`No`). `Yes` is the default. SSD is recommended for the log drive.   
`usrsapSize` | Integer | Required only if you are installing IBM Db2 to run with SAP NetWeaver on the same VM instance.   
`sapmntSize` | Integer | Required only if you are installing IBM Db2 to run with SAP NetWeaver on the same VM instance.   
`swapSize` | Integer | Required only if you are installing IBM Db2 to run with SAP NetWeaver on the same VM instance.   
`otherHost` | String | The name of the other VM instance in the IBM Db2 HA cluster. The VM instance must be defined in the other set of properties in the same `template_ha.yaml` file.   
`networkTag` | String | Optional. A network tag that represents your VM instance for firewall or routing purposes. If you specify `publicIP: No` and don't use a network tag, be sure to provide another means of access to the internet.   
`publicIP` | boolean | Optional. Determines whether a public IP address is added to your VM instance. The default is `Yes`. **Note** : Don't enter `No` unless you have a NAT gateway configured with a network tag defined for the VM or you have provided the VM with another route to the internet. If there is no route to the internet, the installation fails.   
`serviceAccount` | String | Optional. If you create your own service account with locked down permissions, enter the name of the account here. By default, VMs are deployed using the default project service account. Note that an incorrectly defined service account prevents a successful deployment. The following is an example of a custom service account: `myserviceuser@myproject.iam.gserviceaccount.com`  
`sap_deployment_debug` | boolean | Optional. If this value is set to `Yes`, the deployment generates verbose deployment logs. Don't turn this setting on unless a Google support engineer asks you to enable debugging.   
`post_deployment_script` | String | Optional. Specifies the location of a script to run after the deployment is complete. The script should be hosted on a web server or in a Cloud Storage bucket. The URL should begin with `http://`, `https://`, or `gs://`. Note that this script is executed on all VMs that the template creates. To run it on the primary instance only, add a check at the top of your script.   
  
The following example VM definitions from a `template_ha.yaml` configuration file create two VMs for an IBM Db2 HA cluster. For each VM, the configuration file directs Deployment Manager to deploy an `n1-standard-4` VM that is running an operating system from the SLES 12 SP3 image family. The VM includes all of the directories that are required to run an IBM Db2 HA cluster. Deployment Manager doesn't create the SAP NetWeaver directories, because the directory sizes are set to `0`.
         
         resources:
         - name: sap_db2_primary
           type: https://storage.googleapis.com/cloudsapdeploy/deploymentmanager/latest/dm-templates/sap_db2/sap_db2.py
           #
           # By default, this configuration file uses the latest release of the deployment
           # scripts for SAP on Google Cloud.  To fix your deployments to a specific release
           # of the scripts, comment out the type property above and uncomment the type property below.
           #
           # type: https://storage.googleapis.com/cloudsapdeploy/deploymentmanager/202103310846/dm-templates/sap_db2/sap_db2.py
           #
           properties:
             instanceName: db2-ha-s1
             instanceType: n1-standard-4
             zone: us-central1-c
             subnetwork: example-sap-subnetwork
             linuxImage: family/sles-12-sp3-sap
             linuxImageProject: suse-sap-cloud
             db2SID: DH1
             db2sidSize: 16
             db2dumpSize: 16
             db2saptmpSize: 16
             db2sapdataSize: 50
             db2logSize: 16
             db2backupSize: 50
             db2sapdataSSD: Yes
             db2logSSD: Yes
             usrsapSize: 0
             sapmntSize: 0
             swapSize: 0
             otherHost: db2-ha-s2
         #
         # (Comment section omitted from example)
         #
         - name: sap_db2_secondary
           type: https://storage.googleapis.com/cloudsapdeploy/deploymentmanager/latest/dm-templates/sap_db2/sap_db2.py
           #
           # By default, this configuration file uses the latest release of the deployment
           # scripts for SAP on Google Cloud.  To fix your deployments to a specific release
           # of the scripts, comment out the type property above and uncomment the type property below.
           #
           # type: https://storage.googleapis.com/cloudsapdeploy/deploymentmanager/202103310846/dm-templates/sap_db2/sap_db2.py
           #
           properties:
             instanceName: db2-ha-s2
             instanceType: n1-standard-4
             zone: us-central1-f
             subnetwork: example-sap-subnetwork
             linuxImage: family/sles-12-sp3-sap
             linuxImageProject: suse-sap-cloud
             db2SID: DH1
             db2sidSize: 16
             db2dumpSize: 16
             db2saptmpSize: 16
             db2sapdataSize: 50
             db2logSize: 16
             db2backupSize: 50
             db2sapdataSSD: Yes
             db2logSSD: Yes
             usrsapSize: 0
             sapmntSize: 0
             swapSize: 0
             otherHost: db2-ha-s1

  6. Deploy the VM instance with Deployment Manager.
         
         gcloud deployment-manager deployments create DEPLOYMENT-NAME --config TEMPLATE-NAME.yaml
         

Where:

     * `DEPLOYMENT-NAME` represents a name of your choosing for the current deployment. This name is used to identify this deployment on the [Deployments](https://console.cloud.google.com/dm/deployments) page of the Google Cloud console.
     * `TEMPLATE-NAME` represents the name that you gave to the configuration file or, if you didn't change the name of the default file, `template_ha.yaml`.

Deployment Manager reads the specifications in the `template_ha.yaml` file and configures the VM and persistent disks accordingly. The process might take a few minutes. To check the progress of your deployment, follow the steps in the next section.




### Verifying deployment

To verify deployment, you check the deployment logs in Cloud Logging and check the configuration of the VM.

#### Check the logs

  1. In the Google Cloud console, open Cloud Logging to monitor installation progress and check for errors.

**Note:** You might incur costs when completing this step in Cloud Logging. For more information, see [Cloud Logging pricing](https://cloud.google.com/stackdriver/pricing).

[Go to Cloud Logging](https://console.cloud.google.com/logs/query)

  2. Filter the logs:

     1. In the **Logs Explorer** page, go to the **Query** pane.

     2. From the **Resource** drop-down menu, select **Global** , and then click **Add**.

If you don't see the **Global** option, then in the query editor, enter the following query:
            
            resource.type="global"
            "Deployment"
            

     3. Click **Run query**.

  3. Analyze the filtered logs:

     * If `"--- Finished"` is displayed, then the deployment processing is complete and you can proceed to the next step.
     * If you see a quota error:

       1. On the IAM & Admin [Quotas](https://console.cloud.google.com/iam-admin/quotas) page, increase any of your quotas that do not meet the IBM DB2 requirements that are listed in the [IBM DB2 for SAP planning guide](https://docs.cloud.google.com/sap/docs/sap-ibm-db2-planning-guide#pricing-and-quotas).

       2. On the Deployment Manager [Deployments](https://console.cloud.google.com/dm/deployments) page, delete the deployment to clean up the VMs and persistent disks from the failed installation.

       3. Rerun your deployment.




#### Check the configuration of the VM

  1. After VM deployment is complete, connect to each VM by using `ssh`. From the Compute Engine [VM instances page](https://console.cloud.google.com/compute/instances), you can click the SSH button for each VM instance, or you can use your preferred SSH method.

![SSH button on Compute Engine VM instances page.](https://docs.cloud.google.com/static/sap/docs/images/db2-ha-ssh-button.png)

  2. Change to the root user.
         
         sudo su -

  3. At the command prompt, enter `df -h`. Ensure that you see output similar to the following:
         
         db2-ha-s1:~ # df -h
         Filesystem                     Size  Used Avail Use% Mounted on
         devtmpfs                       7.4G     0  7.4G   0% /dev
         tmpfs                           12G     0   12G   0% /dev/shm
         tmpfs                          7.4G   18M  7.4G   1% /run
         tmpfs                          7.4G     0  7.4G   0% /sys/fs/cgroup
         /dev/sda1                       30G  2.2G   26G   8% /
         /dev/mapper/vg_db2sid-vol       16G   33M   16G   1% /db2/DH1
         /dev/mapper/vg_db2dump-vol      16G   33M   16G   1% /db2/DH1/db2dump
         /dev/mapper/vg_db2sapdata-vol   50G   33M   50G   1% /db2/DH1/sapdata
         /dev/mapper/vg_db2saptmp-vol    16G   33M   16G   1% /db2/DH1/saptmp
         /dev/mapper/vg_db2log-vol       16G   33M   16G   1% /db2/DH1/log_dir
         /dev/mapper/vg_db2home-vol      16G   33M   16G   1% /db2/db2dh1
         /dev/mapper/vg_db2backup-vol    50G   33M   50G   1% /db2backup
         tmpfs                          1.5G     0  1.5G   0% /run/user/1001




If any of the validation steps show that the installation failed:

  1. Correct the error.
  2. On the [Deployments](https://console.cloud.google.com/dm/deployments) page, delete the deployment to clean up the VMs and persistent disks from the failed installation.
  3. Rerun your deployment.



### Reserving a floating IP address

You need to select an IP address to use as the floating IP address. You need this IP address when you set the host VM instance metadata and when you install and configure IBM db2 and the HA cluster.

Depending on whether you choose a [route or alias IP implementation type](https://docs.cloud.google.com/sap/docs/sap-ibm-db2-planning-guide#db2_ha_floating_ip) for your floating IP address, the requirements for the floating IP address are different.

If you are using the static route implementation for your floating IP address, the IP address must be outside of your subnetwork IP address range and cannot be used by anything else in your organization's extended networks. Consult with your network admin to determine an appropriate IP address to use.

If you are using the alias IP address implementation for your floating IP address, you must reserve an IP address from the IP address range of the subnetwork that the hosts are using.

**For alias IP address implementations only,** reserve an alias IP address:

  1. Open a terminal on a host VM or open Cloud Shell.

[Go to Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. Reserve an IP address.
         
         gcloud compute addresses create vip-name --region region --subnet subnet-name \
           --addresses ip-addr-optional

Specifying the addresses property is optional. If you don't enter an IP address, Compute Engine selects an IP address from your subnetwork for you.

  3. Display and make a note the reserved IP address to use when you install the database server and configure the HA cluster.
         
         gcloud compute addresses describe vip-name --region=region

For example: 
         
         db2-ha-s1:~ # gcloud compute addresses describe db2-ha-vip-dh1 --region=us-central1
         **address: 10.1.0.30**
         addressType: INTERNAL
         creationTimestamp: '2018-11-28T11:34:14.478-08:00'
         description: ''
         id: '6558342813288977241'
         kind: compute#address
         **name: db2-ha-vip-dh1**
         region: https://www.googleapis.com/compute/v1/projects/solutions-writers/regions/us-central1
         selfLink: https://www.googleapis.com/compute/v1/projects/solutions-writers/regions/us-central1/addresses/db2-ha-vip-dh1
         **status: RESERVED**
         subnetwork: https://www.googleapis.com/compute/v1/projects/solutions-writers/regions/us-central1/subnetworks/example-sap-   subnetwork




### Adding the floating IP address to the metadata for each host VM instance

You specify information about your floating IP address, including your chosen route or alias IP implementation type, as custom metadata for each VM instance in the cluster. For more information about choosing an implementation type for your floating IP address, see [Floating IP addresses for IBM Db2 HA clusters on Google Cloud](https://docs.cloud.google.com/sap/docs/sap-ibm-db2-planning-guide#db2_ha_floating_ip).

Depending on your implementation type, the metadata parameters that you set are different. In the following two sections, follow the instructions in the section that applies to your floating IP address implementation

#### Setting metadata for a route implementation of the floating IP address

If you are using a route implementation for your floating IP address, use the parameters in the following table and the procedure that follows the table to set the instance metadata.

Parameter | Value | Purpose  
---|---|---  
`sap_ibm_vip_solution` | `route` | Indicates that this is a multi-zone deployment that uses a Google Cloud static route to support switching the floating IP address between hosts.  
`sap_ibm_db2_vip` | ip-address | Specifies the floating IP address that you reserved in the previous step.  
`sap_ibm_db2_routename` | route-name | Specifies an arbitrary name for the static route. For example, you could use `db2-dh1-vip-route`  
`sap_ibm_db2_routenet` | vpc-network-name | Specifies the VPC network that contains the IBM Db2 HA cluster.  
  
To set your instance metadata for a static route implementation of your floating IP address:

  1. Open a terminal on a host VM or open Cloud Shell.

[Go to Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. For each host VM instance in the cluster, specify the same metadata for the route implementation of the floating IP address.
         
         gcloud compute instances add-metadata instance-name \
         --metadata sap_ibm_vip_solution=route,sap_ibm_db2_vip=ip-address,\
         sap_ibm_db2_routename=route-name,sap_ibm_db2_routenet=vpc-network-name \
         --zone instance-zone




#### Setting metadata for an alias IP address implementation of the floating IP address

If you are using an alias IP address implementation for your floating IP address, use the parameters in the following table and the procedure that follows the table to set the instance metadata.

Parameter | Value | Purpose  
---|---|---  
`sap_ibm_vip_solution` | `alias` | Indicates that this is a single-zone deployment that uses a Google Cloud alias IP address to support switching the floating IP address between hosts.  
`sap_ibm_db2_vip` | ip-address | Specifies the floating IP address that you reserved in the previous step.  
`sap_ibm_db2_vip_range` | alias-ip-range-name | Optionally, specifies an arbitrary name for the alias IP range. For example, you could use `db2-dh1-vip-alias` The default value is the subnetwork name.  
  
To set your instance metadata for an alias IP implementation of your floating IP address:

  1. Open a terminal on a host VM or open Cloud Shell.

[Go to Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. For each host VM instance in the cluster, specify the same metadata for the alias IP address implementation of the floating IP address.
         
         gcloud compute instances add-metadata instance-name \
         --metadata sap_ibm_vip_solution=alias,sap_ibm_db2_vip=ip-address,\
         sap_ibm_db2_vip_range=alias-ip-range-name --zone instance-zone




#### Reviewing or changing your instance metadata

To review the instance metadata that you set.
    
    
    gcloud compute instances describe instance-name --zone instance-zone

If you need to change your custom metadata.
    
    
    gcloud compute instances add-metadata instance-name --metadata  parm-name=parm-value

### Adding host names and IP addresses to `/etc/hosts`

During cluster setup, the SAP cluster setup tool validates the host names and internal IP addresses of each host VM and of the floating IP address. To ensure that the validation is successful, add the IP address, host name, and the VPC [internal DNS name](https://cloud.google.com/compute/docs/internal-dns) for each host VM and the floating IP address to the `/etc/hosts` file on each host VM by using your preferred editor.

For example, as root, the following example updates `/etc/hosts`:
    
    
    echo "#Db2 HA floating IP additions" >> /etc/hosts
    echo 10.2.0.24 db2-ha-vip-dh1 db2-ha-vip-dh1.c.solutions-writers.internal >> /etc/hosts
    echo 10.1.0.3 db2-ha-s1 db2-ha-s1.us-central1-c.c.db2-ha-project.internal >> /etc/hosts
    echo 10.1.0.2 db2-ha-s2 db2-ha-s2.us-central1-f.c.db2-ha-project.internal >> /etc/hosts
    

In the preceding example, the string between the host name and `>>` on each line is a VPC internal DNS name, which is used by the VPC internal DNS service.

The host VMs use a _zonal_ internal DNS name, which includes a field for the zone. The floating IP address uses a _global_ internal DNS name, which doesn't include a zone field.

For a VM host, you can retrieve the internal DNS name by entering the following command from a terminal on the host VM:
    
    
    curl "http://metadata.google.internal/computeMetadata/v1/instance/hostname" \
    -H "Metadata-Flavor: Google"

For a floating IP address, you can enter it yourself by using the following format.
    
    
    vip-host-name.c.project-name.internal

After you update the `/etc/hosts` file, the relevant information in the `/etc/hosts` file should look similar to the following example:
    
    
    #Db2 HA floating IP additions
    10.2.0.24 db2-ha-vip-dh1 db2-ha-vip-dh1.c.solutions-writers.internal
    10.1.0.3 db2-ha-s1 db2-ha-s1.us-central1-c.c.db2-ha-project.internal
    10.1.0.2 db2-ha-s2 db2-ha-s2.us-central1-f.c.db2-ha-project.internal

## Preparing the operating system

After you have created your VM, prepare the operating system for the IBM Db2 HA cluster.

The requirements are defined by SAP and IBM. The SAP documentation calls for installing software, such as Perl and Korn Shell, that might not be pre-installed on your Compute Engine host VMs.

Check the following documents for the latest requirements:

  * [IBM Db2 high availability solution: IBM Tivoli System Automation for Multiplatforms](https://help.sap.com/doc/a7ba6b8cc8dc46309c2f93bcfc417133/CURRENT_VERSION/en-US/DB6_SAMP_Guide.pdf)

  * SAP note [1984787 - SUSE LINUX Enterprise Server 12: Installation notes](https://launchpad.support.sap.com/#/notes/1984787)

**Note:** On SLES 12 SP2, you must use `zypper update` to update the OS packages. Otherwise, some software that runs on Java, such as JDBC, might core dump.
  * SAP note [3562909 - Red Hat Enterprise Linux 10.x: Installation and Configuration](https://me.sap.com/notes/3562909)

  * SAP note [3108316 - Red Hat Enterprise Linux 9.x: Installation and Configuration](https://me.sap.com/notes/3108316)

  * SAP note [2772999 - Red Hat Enterprise Linux 8.x: Installation and Configuration](https://me.sap.com/notes/2772999)

  * SAP note [2002167 - Red Hat Enterprise Linux 7.x: Installation and Upgrade](https://me.sap.com/notes/2002167)




## Installing the database server and creating the IBM Db2 HA cluster

Before you start following the instructions in [IBM Db2 High availability solution: IBM Tivoli System Automation for Multiplatforms](https://help.sap.com/doc/a7ba6b8cc8dc46309c2f93bcfc417133/CURRENT_VERSION/en-US/DB6_SAMP_Guide.pdf) to install and configure IBM Db2 and the HA cluster, review the overview of the following procedure, paying particular attention to the notes.

To install SAP NetWeaver and the primary application server, see the Google Cloud [SAP NetWeaver documentation](https://docs.cloud.google.com/sap/docs/netweaver-guides) and the applicable SAP installation guides available from the [SAP Help Portal](https://help.sap.com/viewer/index).

The following steps are an overview of the installation procedure. Refer to the SAP documentation for details.

  1. Establish key-based SSH connectivity between the primary and secondary instances and between each instance and itself as described in the SAP documentation. SSH is used by the SAP cluster setup tool. Test all connections on each host. For example, on `db2-ha-s1` test both of the following.

     * ssh db2-ha-s1

     * ssh db2-ha-s2

**Note:** Each Compute Engine VM comes with its own `id_rsa` and `id_rsa.pub` files already generated. For Db2 HA clusters, the rsa key from the `id_rsa.pub` file of each host VM is added for you to the `authorized_keys` file of every other host VM in the cluster.
  2. Download or copy the complete SAP media set for Db2 to your VM from the [SAP support portal](http://support.sap.com/swdc).

  3. On the primary host VM, use the SAP Software Provisioning Manager (SWPM) to install the IBM Db2 database server.

**Note:** On the **Cluster Configuration - Network** panel in SWPM you specify the floating IP address that you reserved and specify the tiebreaker IP address. For information about what you can use as a tiebreaker, see [The network tiebreaker](https://docs.cloud.google.com/sap/docs/sap-ibm-db2-planning-guide#the_network_tiebreaker).

  4. On the secondary host VM, set up the standby database by using a method such as SAP homogeneous system copy.

  5. On both host VMs, install the license files for IBM Db2 and IBM TSAMP. For more information about installing the IBM licenses that you obtained from SAP, see the SAP note [816773 - DB6: Installing the Application-Specific Db2 License from SAP](https://me.sap.com/notes/816773).

  6. On both host VMs, install the latest version of TSAMP, as supported by your database version and operating system version.

  7. On the primary host VM, use the latest version of the SAP cluster setup tool `sapdb2cluster.sh` to configure and create the IBM Db2 HA cluster.

**Note:** Before you create the Db2 HA cluster, you need to configure the SAP cluster setup tool to bypass the creation of the standard `IBM.ServiceIP` resource by specifying `DB2_NO_SERVICE_IP=true` in the `sapdb2cluster.sh` setup dialog. The cluster uses the `IBM.Application` resource instead. 

For more information, see [Best practices for floating IP addresses](https://cloud.google.com/solutions/best-practices-floating-ip-addresses).

  8. After the cluster is created, on the primary host, use the DB2 high-availability instance configuration utility (db2haicu) utility to test that the cluster can failover.

     1. Exit the SAP cluster setup tool and the Korn shell.

     2. On the primary instance, confirm that the primary database server is online.
            
            lssam

In the following example excerpt from the `lssam` output, the primary database instance is online:
            
            Online IBM.ResourceGroup:**db2_db2dh1_db2dh1_DH1-rg** Nominal=Online
                    '- Online IBM.Application:db2_db2dh1_db2dh1_DH1-rs
                            |- **Online** IBM.Application:db2_db2dh1_db2dh1_DH1-rs:**db2-ha-s1**
                            '- Offline IBM.Application:db2_db2dh1_db2dh1_DH1-rs:db2-ha-s2

     3. Switch to the database instance user.
            
            sudo su - db2sid

     4. Start the db2haicu utility.
            
            db2haicusid

     5. In the db2haicu interface, select option **5** and follow the prompts.

     6. Exit the db2haicu utility.

     7. On the primary host, check that the secondary host is now online.
            
            lssam

In the following example excerpt from the lssam output, the secondary database instance is online:
            
            Online IBM.ResourceGroup:**db2_db2dh1_db2dh1_DH1-rg** Nominal=Online
                    '- Online IBM.Application:db2_db2dh1_db2dh1_DH1-rs
                            |- Offline IBM.Application:db2_db2dh1_db2dh1_DH1-rs:db2-ha-s1
                            '- **Online** IBM.Application:db2_db2dh1_db2dh1_DH1-rs:**db2-ha-s2**




To complete the cluster configuration, follow the instructions in the next section to create a custom TSAMP resource for the floating IP address and associate it in TSAMP with the IBM Db2 instance resource.

## Creating a TSAMP custom resource for the floating IP address

To enable TSAMP to manage the floating IP address, you need to create a TSAMP custom resource for it. To enable TSAMP to interact with Google Cloud while managing the floating IP address resource, you need to download and configure a helper script from Google Cloud.

### Download the Google Cloud helper script

On each host in the cluster, download the Google Cloud helper script and set its permissions.

  1. On both the primary and standby hosts, as the root user from the `/root` directory on the primary VM, download the script.

For instances not using a shared VPC configuration: 
         
         wget https://storage.googleapis.com/cloudsapdeploy/terraform/latest/terraform/sap_db2/utility/gcp_floating_ip.sh -O gcp_floating_ip.sh

For instances using a shared VPC configuration: 
         
         wget https://storage.googleapis.com/cloudsapdeploy/terraform/latest/terraform/sap_db2/utility/gcp_floating_ip_svpc.sh -O gcp_floating_ip.sh

  2. On both hosts, set the permissions on the script.
         
         chmod 744 gcp_floating_ip.sh




### Create and configure a TSAMP custom resource for your floating IP address

On any one host in the cluster, create and configure a TSAMP custom resources for the floating IP address.

  1. On any one host, use your preferred method to create a configuration file called `cluster_res.conf` and paste the following text in it after you update the NodeNameList parameter with your host names.
         
         PersistentResourceAttributes::
           Name="gcp_floating_ip-rs"
           ResourceType=1
           StartCommand="/root/gcp_floating_ip.sh start"
           StopCommand="/root/gcp_floating_ip.sh stop"
           MonitorCommand="/root/gcp_floating_ip.sh status"
           MonitorCommandPeriod=30
           MonitorCommandTimeout=30
           StartCommandTimeout=600
           StopCommandTimeout=600
           UserName="root"
           RunCommandsSync=1
           ProtectionMode=0
           NodeNameList={"host-1","host-2"}

  2. On the primary host as the root user, create the TSAMP custom resource with the following commands.
         
         export CT_MANAGEMENT_SCOPE=2
         mkrsrc -f cluster_res.conf IBM.Application
         mkrg -l None gcp_floating_ip-rg
         chrg -o Online gcp_floating_ip-rg
         addrgmbr -g gcp_floating_ip-rg -m F IBM.Application:gcp_floating_ip-rs
         rgreq -o start gcp_floating_ip-rg

  3. On the primary host as the root user, confirm that the Db2 instance resource that is online is on the same host as the online floating IP resource.
         
         lssam

In the output, the online resources should all be on the same host VMs:
         
         Online IBM.ResourceGroup:db2_db2dh1_db2dh1_DH1-rg Nominal=Online
                 '- Online IBM.Application:db2_db2dh1_db2dh1_DH1-rs
                         |- **Online IBM.Application:db2_db2dh1_db2dh1_DH1-rs:db2-ha-s1**
                         '- Offline IBM.Application:db2_db2dh1_db2dh1_DH1-rs:db2-ha-s2
         Online IBM.ResourceGroup:gcp_floating_ip.sh_rg Nominal=Online
                 '- Online IBM.Application:gcp_floating_ip.sh_rs
                         |- **Online IBM.Application:gcp_floating_ip.sh_rs:db2-ha-s1**
                         '- Offline IBM.Application:gcp_floating_ip.sh_rs:db2-ha-s2

If the floating IP address resource isn't online on the same host that the database instance is, move the floating IP address resource.
         
         rgreq -o move -n host-to-move-from gcp_floating_ip-rg

  4. As the root user on the primary host, establish a relationship in TSAMP between the database instance resource and the floating IP address resource.
         
         rgreq -o lock gcp_floating_ip-rg
         rgreq -o lock db2_db2sid_db2sid_SID-rg
         mkrel -o NoCondition -p Collocated \
           -S IBM.Application:gcp_floating_ip-rs -G IBM.Application:db2_db2sid_db2sid_SID-rs \
           db2hadr_colo_gcp_floating_ip
         rgreq -o unlock db2_db2sid_db2sid_SID-rg
         rgreq -o unlock gcp_floating_ip-rg

After you establish a relationship between the database instance resource and the floating IP address resource, you can test failover again, as described in the next section.




## Verifying the deployment of your Db2 HA cluster for SAP on Google Cloud

To confirm that the IBM Db2 HA cluster is configured correctly, trigger a failover and check that all of the online resources move from one host VM to the other.

To perform a failover test.

  1. On the primary host as the root user, note which host VM the online resources are currently on.
         
         lssam

  2. On the primary host, change to the db2 instance user.
         
         sudo su - db2sid

  3. Start the db2haicu utility.
         
         db2haicu

  4. In the db2haicu utility interface, trigger a failover by selecting option **5** and following the prompts.

  5. After the db2haicu utility finishes processing, exit the utility.

  6. Switch to the root user.
         
         sudo su -

  7. Confirm that the online resources have moved to the other host VM.




## Validate your installation of Google Cloud's Agent for SAP

After you have deployed a VM and installed your SAP system, validate that Google Cloud's Agent for SAP is functioning properly.

### Verify that Google Cloud's Agent for SAP is running

To verify that the agent is running, follow these steps:

  1. Establish an SSH connection with your Compute Engine instance. 

  2. Run the following command: 
         
         systemctl status google-cloud-sap-agent

If the agent is functioning properly, then the output contains `active (running)`. For example: 
         
         google-cloud-sap-agent.service - Google Cloud Agent for SAP
         Loaded: loaded (/usr/lib/systemd/system/google-cloud-sap-agent.service; enabled; vendor preset: disabled)
         Active: **active (running)** since Fri 2022-12-02 07:21:42 UTC; 4 days ago
         Main PID: 1337673 (google-cloud-sa)
         Tasks: 9 (limit: 100427)
         Memory: 22.4 M (max: 1.0G limit: 1.0G)
         CGroup: /system.slice/google-cloud-sap-agent.service
                └─1337673 /usr/bin/google-cloud-sap-agent
         




If the agent isn't running, then [restart the agent](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/operations#agent4sap-restart).

### Verify that SAP Host Agent is receiving metrics

To verify that the infrastructure metrics are collected by Google Cloud's Agent for SAP and sent correctly to the SAP Host Agent, follow these steps:

  1. In your SAP system, enter transaction `ST06`.
  2. In the overview pane, check the availability and content of the following fields for the correct end-to-end setup of the SAP and Google monitoring infrastructure:

     * **Cloud Provider** : `Google Cloud Platform`
     * **Enhanced Monitoring Access** : `TRUE`
     * **Enhanced Monitoring Details** : `ACTIVE`



## Performing post-deployment tasks

Before using your IBM Db2 high-availability system on Google Cloud, we recommend that you complete all of the post-installation activities that are documented in [IBM Db2 High Availability Solution: IBM Tivoli System Automation for Multiplatforms](https://help.sap.com/doc/a7ba6b8cc8dc46309c2f93bcfc417133/CURRENT_VERSION/en-US/DB6_SAMP_Guide.pdf), including.

  1. Validating the database cluster.

  2. Backing up the TSAMP core policy.

  3. Updating the database fix packs.

  4. Updating Db2 client connections to use the host name and IP address of the floating IP address. For example, update the `db2cli.ini` file on the SAP ABAP application servers.




If you are using a NAT gateway with your DB2 HA cluster, complete the NAT gateway setup as described in [Completing the NAT gateway installation](https://docs.cloud.google.com/sap/docs/sap-ibm-db2-deployment-guide#complete_nat_gateway_db2) in the IBM Db2 for SAP deployment guide.

## Get support

If you need help deploying or resolving a problem with HA clusters that run IBM Db2 with SAP systems on Google Cloud, then contact Cloud Customer Care with the relevant diagnostic information, as described in the following guides:

  * [High-availability clusters on RHEL diagnostic information](https://docs.cloud.google.com/sap/docs/getting-support-diag-info-ha-rhel)
  * [High-availability clusters on SLES diagnostic information](https://docs.cloud.google.com/sap/docs/getting-support-diag-info-ha-sles)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
