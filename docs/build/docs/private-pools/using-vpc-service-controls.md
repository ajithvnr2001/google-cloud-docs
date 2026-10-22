---
url: https://docs.cloud.google.com/build/docs/private-pools/using-vpc-service-controls/
title: Use VPC Service Controls \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:11:49.475471+00:00
---

# Use VPC Service Controls  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/private-pools/using-vpc-service-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Use VPC Service Controls Stay organized with collections  Save and categorize content based on your preferences. 

[VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls) is a Google Cloud feature that lets you set up a secure perimeter to guard against data exfiltration. This page shows how to use VPC Service Controls with [Cloud Build private pools](https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview) to add additional security to your builds.

## Before you begin

  * To use the command-line examples in this guide, install and configure the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk).

**Note:** If you've installed gcloud CLI previously, make sure you have the latest available version by running `gcloud components update`.
  * Set up a private connection between your Virtual Private Cloud network and the VPC network where private pools reside. For instructions, see [set up your environment to create private pools](https://docs.cloud.google.com/build/docs/private-pools/set-up-private-pool-environment#setup-private-connection).

  * Builds run within the service perimeter won't have permissions to store [build logs in the default Cloud Storage logs bucket](https://docs.cloud.google.com/build/docs/securing-builds/store-manage-build-logs#store-default). Before you run your build, set up your build config file with one of the following options:

    * Choose to store your build logs in Cloud Logging by setting [`loggingMode` to `CLOUD_LOGGING_ONLY`](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds#loggingmode).
    * In your private project, create a Cloud Storage logs bucket to store your build logs. For more information, see [Storing build logs in a user-created bucket](https://docs.cloud.google.com/build/docs/securing-builds/store-manage-build-logs#store-custom-bucket).
    * Disable build logs by setting [`loggingMode` to `NONE`](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds#loggingmode).
  * If your builds push images and artifacts to Artifact Registry or Cloud Storage in a different Google Cloud project, then add that project to the same service perimeter as the project from which your builds originate.

  * Optional: Familiarize yourself with machine type configurations and regional availability. For more information, see [`workerconfig`](https://docs.cloud.google.com/build/docs/private-pools/private-pool-config-file-schema#workerconfig) in the private pool configuration file schema documentation.




To ensure that has the necessary permissions to set up a service perimeter, ask your administrator to grant the following IAM roles to on your service account: 

  * [Organization Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.organizationViewer) (`roles/resourcemanager.organizationViewer`)
  * [Access Context Manager Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyEditor) (`roles/accesscontextmanager.policyEditor`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

Your administrator might also be able to give the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Set up a private pool in the VPC Service Controls perimeter

To use VPC Service Controls with Cloud Build, you must first create and configure a service perimeter, which is done at the organization level. This setup ensures that VPC Service Controls checks are enforced when using Cloud Build and that developers can only run builds that comply with VPC Service Controls.

### Create a VPC Service Controls perimeter

Follow the [VPC Service Controls Quickstart](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-service-perimeter) to:

  1. Create a service perimeter.
  2. Add the project in which you're planning to create the private pool to the perimeter.

**Note:** If you are using [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc), make sure to add the host project and service projects to the same perimeter.
  3. Restrict the Cloud Build API.




After setting up your service perimeter, all calls to the Cloud Build API are checked to ensure that the calls originate from within the same perimeter.

### Granting the service account access to the VPC Service Controls perimeter

**Note:** We have introduced changes to the default service account used to run builds. As a best practice, we recommend that you [specify your own service account](https://docs.cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts) to run your builds. For more information see [Cloud Build default service account change](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates).

In the following cases, you must grant the legacy Cloud Build or Compute Engine service account access to the VPC Service Controls perimeter for your builds to access resources within the perimeter:

  * If you're using the legacy Cloud Build or Compute Engine service account to start builds using a [build trigger](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers), [Cloud Build API, or the command line](https://docs.cloud.google.com/build/docs/running-builds/start-build-command-line-api).

  * If you're using user-specified service accounts to start builds using a build trigger.




You don't need to grant the legacy Cloud Build or Compute Engine service account access to the VPC Service Controls perimeter if you're using user-specified service accounts to start builds using the [Cloud Build API, or the command line](https://docs.cloud.google.com/build/docs/running-builds/start-build-command-line-api).

Perform the following steps to grant the legacy Cloud Build or Compute Engine service account access to the VPC Service Controls perimeter:

  1. Note the email address of the legacy service account:

     1. Open the IAM page:

[ Open the IAM page](https://console.cloud.google.com/iam-admin/iam)

     2. Select the project that you added to the service perimeter.

     3. In the permissions table, locate the email address corresponding the legacy Cloud Build service account.

  2. Update the [ingress policy](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#ingress-rules-reference) of the service perimeter to allow the service account to call the Cloud Build APIs. This ingress rule allows the service account to make the `CreateBuild` API call. For more information about setting VPC Service Controls ingress policies, see [Configuring ingress and egress policies](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies#gcloud) and [Ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules).
         
         - ingressFrom:
             identities:
             - serviceAccount:SERVICE_ACCOUNT_EMAIL
             sources:
             - accessLevel: '*'
           ingressTo:
             operations:
             - serviceName: 'cloudbuild.googleapis.com'
               methodSelectors:
               - method: '*'
             resources:
             - 'projects/PROJECT_NUMBER'
         

  3. Update the perimeter policy by running the following command replacing variables with appropriate values:
         
         gcloud beta access-context-manager perimeters update PERIMETER_NAME \
             --set-ingress-policies=INGRESS-FILENAME \
             --policy=POLICY_ID
         




Where:

  * `SERVICE_ACCOUNT_EMAIL`: the email address of the service account.
  * `PROJECT_NUMBER`: the project number of the Google Cloud project that you added to the VPC Service Controls perimeter.
  * `PERIMETER_NAME`: the name of your VPC Service Controls perimeter.
  * `INGRESS-FILENAME`: the name of your ingress policy file.
  * `POLICY_ID`: the ID of the access policy.



### Optional: Enabling perimeter access for development machines

Because VPC Service Controls checks are enforced for the Cloud Build API, calls to the Cloud Build API fail unless they originate from within the service perimeter. Therefore, to manage builds with the Cloud Build API, the Cloud Build UI in the Google Cloud console, or the Google Cloud CLI, choose one of the following options:

  * **Use a machine inside the VPC Service Controls perimeter.** For example, you can use a Compute Engine VM or an on-premises machine connected to your VPC network using VPN.

  * **Grant developers access to the perimeter.** For example, you can create access levels that enable perimeter access based on IP address or user identity. For more information, see [Allowing access to protected resources from outside a perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/use-access-levels).




### Set up organization policy constraints

To ensure that VPC Service Controls checks are enforced correctly and you're restricting builds in a Google Cloud organization to only use the specified private pools, set the [`constraints/cloudbuild.allowedWorkerPools` organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints#constraints-for-specific-services). You can apply the organization policy to the entire organization, or to a project or a folder in the organization. For example, your organization policy can specify that:

  * All builds in the organization use the specified private pools.
  * All builds in a folder use the specified private pools.
  * All builds in a project use the specified private pools.



**IAM permissions** : To manage organization policies, you need the [Organization Policy Administrator](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#add-org-policy-admin) (`roles/orgpolicy.policyAdmin`) role. For instructions on granting a role, see [Configuring access to Cloud Build resources](https://docs.cloud.google.com/build/docs/securing-builds/configure-access-to-resources).

The [`gcloud resource-manager org-policies allow` command](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/allow) sets an organization policy that requires the builds in the organization to only use the specified private pool:
    
    
     gcloud resource-manager org-policies allow \
         cloudbuild.allowedWorkerPools \
         projects/PRIVATEPOOL_PROJECT_ID/locations/LOCATION/workerPools/PRIVATEPOOL_ID \
         --organization ORGANIZATION_ID
    

Where:

  * `PRIVATEPOOL_ID`: the ID of the private pool to run builds.

  * `PRIVATEPOOL_PROJECT_ID`: the ID of the Google Cloud project that contains the private pool.

  * `LOCATION`: the region that contains the private pool.

  * `ORGANIZATION_ID`: the ID of the Organization where you're running builds.




The command supports `under:` and `is` prefixes.

To set organization policy that requires all builds in the organization to use any private pool under that organization:
    
    
     gcloud resource-manager org-policies allow \
         cloudbuild.allowedWorkerPools under:organizations/ORGANIZATION_ID \
         --organization ORGANIZATION_ID
    

Where, `ORGANIZATION_ID` is the ID of the organization that contains the private pools.

To set an organization policy that requires all builds in the projects under a folder to use any private pool in the specified project:
    
    
     gcloud resource-manager org-policies allow \
         cloudbuild.allowedWorkerPools under:projects/PROJECT_ID \
         --folder FOLDER_ID
    

Where `PROJECT_ID` is the ID of the project that contains the private pools and FOLDER_ID contains the projects where you're running the builds.

To set an organization policy that requires all builds in a project to use any private pool in the specified project:
    
    
     gcloud resource-manager org-policies allow \
         cloudbuild.allowedWorkerPools under:projects/PRIVATEPOOL_PROJECT_ID \
         --project BUILD_PROJECT_ID
    

Where `PRIVATEPOOL_PROJECT_ID` is the ID of the project that contains the private pools and BUILD_PROJECT_ID is the ID of the project where you're running the builds.

Keep the following considerations in mind when enforcing the `constraints/cloudbuild.allowedWorkerPools` organization policy constraint:

  * If you apply this organization policy constraint to a Google Cloud project, ensure that all builds in the project use the private pool; builds attempting to use the default shared pool will fail.

  * If your Google Cloud organization contains services such as App Engine or Cloud Run functions that implicitly use Cloud Build, enforcing this the organization policy constraint may cause these services to not work as expected.




### Create a private pool in the service perimeter

###  Google Cloud console 

  1. Open the **Worker Pool** page in the Google Cloud console:

[ Open the Cloud Build worker pool page](https://console.cloud.google.com/cloud-build/settings/worker-pool)

  2. Click **Create private pool**.

The **Create private pool** page is displayed.

Enter the following information to create your private pool:

  3. **Name** : Enter a name for your private pool. This value can only contain alphanumeric characters `/[a-z][0-9]/` or dashes `-`. The name of your private pool must be between 1 and 63 characters.

  4. **Region** : Select the region in which you want the private pool to be created.

  5. **Machine configuration** : Configure the following:

     1. **Series** : Choose a machine series.

     2. **Machine type** : This setting shows the machine types, based on the machine series that you selected, that the worker pool can use. The available machine types vary by region.

     3. **Disk size** : Enter a disk size for your private pool. Specify a value greater than or equal to 100 and less than or equal to 4000. If you don't provide a value, then Cloud Build uses a disk size of 100.

     4. **Nested virtualization** : If you selected a C3 series machine, then you can enable [nested virtualization](https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/overview). This feature lets you run virtual machine (VM) instances inside of other VMs so you can create your own virtualization environments.

  6. Under **Network type** , select **Private network** , and then select the following:

     1. **Project** : Select your Google Cloud project ID.

     2. **Network** : Select your network from the drop-down menu. If you have not created a network, see [Create and manage VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#creating_networks) to learn how to create a network.

     3. **IP range** : Enter the internal IP range that the Cloud Build producer network can use to allocate to VMs maintaining a connection with private repositories.

You can specify the range using the Classless Inter-Domain Routing (CIDR) routing notation in the format `STARTING_IP_ADDRESS/SUBNET_PREFIX_SIZE`. For example, `192.0.2.0/24` has a prefix length of 24. The first 24 bits of the IP range are used as the subnet mask (`192.0.2.0`) while the possible hosts addresses range from `192.0.2.0` to `192.0.2.255`.

The value of your prefix length must not exceed `/29`. If no value is specified for the range, a default value of `/24` is automatically assigned. If no value is specified for the prefix length, IP addresses are automatically assigned within the peered VPC network. If no value is specified for the IP address, the IP address is automatically assigned a range within the peered VPC network.

**Note:** You can only specify an **IP range** if you've specified a **Network**. If you've specified a **Network** , the **IP range** is optional.
     4. Clear **Assign external IPs** to restrict access to your private network.

  7. Click **Create** to create your private pool.




###  gcloud 

  1. Create a [private pool config file](https://docs.cloud.google.com/build/docs/private-pools/worker-pool-config-file-schema) in the YAML or the JSON format, and set the `egressOption` flag to `NO_PUBLIC_EGRESS`:
         
         privatePoolV1Config:
           networkConfig:
             egressOption: NO_PUBLIC_EGRESS
             peeredNetwork: PEERED_NETWORK
           workerConfig:
             diskSizeGb: 'PRIVATE_POOL_DISK_SIZE'
             machineType: PRIVATE_POOL_MACHINE_TYPE
         

Where:

     * `PEERED_NETWORK` is the network resource URL of the network that is peered to the service provider network. `PEERED_NETWORK` must be of the format `projects/NETWORK_PROJECT_ID/global/networks/NETWORK_NAME`, where `NETWORK_PROJECT_ID` is the project ID of the Google Cloud project that holds your VPC network and `NETWORK_NAME` is the name of your VPC network.
     * `PRIVATE_POOL_MACHINE_TYPE` is the Compute Engine machine type for private pool instance. For supported machine types, see [Private pool config file schema](https://docs.cloud.google.com/build/docs/private-pools/worker-pool-config-file-schema#machinetype).
     * `PRIVATE_POOL_DISK_SIZE` is disk size for private pool instance in GB. Specify a value greater than or equal to 100 and less than or equal to 1000. If you specify `0`, Cloud Build uses the default value of 100.
     * `egressOption` is the flag to enable VPC Service Controls perimeter for your private pool. Set this to `NO_PUBLIC_EGRESS` to create your private pool within the VPC Service Controls perimeter.
  2. Run the following `gcloud` command, where `PRIVATEPOOL_ID` is a unique identifier for your private pool, `PRIVATEPOOL_CONFIG_FILE` is the name of your private pool config file, and `REGION` is the [region](https://docs.cloud.google.com/build/docs/locations) where you want to create your private pool:
         
         gcloud builds worker-pools create PRIVATEPOOL_ID --config-from-file PRIVATEPOOL_CONFIG_FILE --region REGION
         




### Optional: Enable public internet calls on the VPC network

To enable your VPC network to allow network connectivity to where your repository is hosted (e.g. github.com), configure both of the following settings:

  * The VPC network that your private pool runs on is defined as a [PeeredNetwork](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.workerPools#networkconfig). To allow calls to your repository host, ensure that this VPC network allows public egress to your repository host. For information on doing this, see [routes and firewall rules](https://docs.cloud.google.com/vpc/docs/vpc#affiliated_resources).

  * Do one of the following:

    * Set the `egressOption` field in your [private pool config file](https://docs.cloud.google.com/build/docs/private-pools/worker-pool-config-file-schema) to `PUBLIC_EGRESS`.

    * [Set up your private pools to use a static external IP](https://docs.cloud.google.com/build/docs/private-pools/access-external-resources-using-static-external-ip).




## Limitations

  * VPC Service Controls protection is available only for builds run in private pools; you cannot use VPC Service Controls with builds run in default pools.

  * Cloud Build Pub/Sub triggers aren't supported when VPC Service Controls is used.




## What's next

  * Learn how to [run builds in private pools](https://docs.cloud.google.com/build/docs/private-pools/run-builds-in-private-pool).
  * Learn how to [configure commonly used networking use cases](https://docs.cloud.google.com/build/docs/private-pools/use-in-private-network).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
