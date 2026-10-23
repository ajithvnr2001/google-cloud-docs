---
url: https://docs.cloud.google.com/load-balancing/docs/https/setup-cross-project-backend-service-backend-bucket/
title: Set up a global external Application Load Balancer with a cross-project backend service and backend bucket \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:25:39.406760+00:00
---

# Set up a global external Application Load Balancer with a cross-project backend service and backend bucket  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/https/setup-cross-project-backend-service-backend-bucket/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Set up a global external Application Load Balancer with a cross-project backend service and backend bucket Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to create a global external Application Load Balancer with a backend service and a backend bucket that are located in a project that is different from where the load balancer's frontend and the URL map are located. This deployment model is known as [cross-project service referencing](https://docs.cloud.google.com/load-balancing/docs/https#cross-project).

The example used in this document does not use a Shared VPC environment to configure cross-project service referencing. To learn more about how to configure cross-project service referencing in a Shared VPC environment, see [Set up a global external Application Load Balancer with Shared VPC](https://docs.cloud.google.com/load-balancing/docs/https/set-up-global-ext-https-shared-vpc).

## Before you begin

Make sure that your setup meets the following prerequisites.

### IAM roles and permissions required

To follow this guide, you must have the following IAM roles:

Task | Required role  
---|---  
Create a project | [Project Creator role](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectCreator) (`roles/resourcemanager.projectCreator`)   
Create compute resources | [Compute Network Admin role](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin) (`roles/compute.networkAdmin`)   
Create Cloud Storage buckets | [Storage Object Admin role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) (`roles/storage.objectAdmin`)   
Use a resource from a different project (In this example, project A references the backend service and backend bucket that are located in project B.) |  In this example, an administrator of project B must grant the [Compute Load Balancer Services User role](https://docs.cloud.google.com/compute/docs/access/iam#compute.loadBalancerServiceUser) (`roles/compute.loadBalancerServiceUser`) to the administrator of project A to allow access to the backend service and backend bucket in project B. This role can be granted at the project level or at the resource level. To learn more about how to assign this role, see [Grant permissions to the Compute Load Balancer Admin to use the backend service](https://docs.cloud.google.com/load-balancing/docs/https/set-up-global-ext-https-shared-vpc#grant-bs-user).  
  
### Create Google Cloud projects

For the example in this document, follow the instructions two times to create two Google Cloud projects.

### Console

To create a new project, do the following:

  1. Go to the **Manage resources** page in the Google Cloud console. 

[Go to Manage Resources](https://console.cloud.google.com/cloud-resource-manager?walkthrough_id=resource-manager--create-project&start_index=1#step_index=1)

The remaining steps appear in the Google Cloud console.

  2. Click **Create project**. 
  3. In the **New project** window that appears, enter a project name and select a billing account as applicable. A project name can contain only letters, numbers, single quotes, hyphens, spaces, or exclamation points, and must be between 4 and 30 characters. **Note:** A billing account is available for selection only if you have the [Billing Account User](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.user) role (`roles/billing.user`) on the organization or billing account. When granted in combination with the Project Creator role (`roles/resourcemanager.projectCreator`), these roles let you create new projects linked to that billing account. When granted in combination with the Project Billing Manager role (`roles/billing.projectManager`), these roles let you link and unlink projects on the billing account. 
  4. Enter the parent organization or folder resource in the **Parent resource** box. That resource will be the hierarchical parent of the new project. If **No organization** is an option, you can select it to create your new project as the top level of its own resource hierarchy. 
  5. When you're finished entering new project details, click **Create**.



###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To create a new project, use the [`gcloud projects create`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/create) command:
         
         gcloud projects create PROJECT_ID
         

Where PROJECT_ID is the ID for the project you want to create. A project ID must start with a lowercase letter, and can contain only ASCII letters, digits, and hyphens, and must be between 6 and 30 characters.




## Setup overview

As depicted in the following diagram, a global external Application Load Balancer's frontend and URL map are created in a project that is different from the load balancer's backend service and backend bucket. This type of cross-project deployment doesn't use a Shared VPC environment.

In this configuration, the URL map routes requests for static content (`/images/*`) to a backend bucket whereas all other requests are routed to the default backend service.

[ ![A cross-region internal Application Load Balancer sends traffic to a Cloud Storage backend service and a backend bucket that are located in a different project.](https://docs.cloud.google.com/static/load-balancing/images/cross-project-backend-service-backend-bucket.svg)](https://docs.cloud.google.com/static/load-balancing/images/cross-project-backend-service-backend-bucket.svg) Cross-project deployment (click to enlarge).

The following table provides an overview of the resources that are created in _project A_ and _project B_. The load balancer's frontend and URL map are created in project A whereas the backend components are created in project B.

Resources created in project A | Resources created in project B | 

  * IP address
  * SSL certificate
  * URL map
  * Target proxy
  * Forwarding rule

| 

  * VPC network
  * Subnet
  * Backend service  
The backend service references the backend instances in an instance group. The following resources are used to create the backend instances. For the purpose of this example, the backend instances are created in a subnet named `lb-backend-subnet` in the `us-west1` region.
    * Instance template
    * Instance group
    * Health check
    * Firewall rule
  * Backend bucket  

    * The backend bucket references a Cloud Storage bucket.

  
---|---  
  
In the following sections, we will configure the different resources listed in the preceding table, starting with configuring a VPC network and a subnet for the load balancer's backend VMs in project B.

## Configure a network and a subnet for the load balancer's backend VMs in project B

For the purpose of this example, the backend VMs are created in the following network and subnet:

  * **Network.** The network is a [custom mode VPC network](https://docs.cloud.google.com/vpc/docs/vpc#subnet-ranges) named `lb-network`.

  * **Subnet for load balancer's backends VMs** A subnet named `lb-backend-subnet` in the `us-west1` region uses `10.1.2.0/24` for its primary IP range. A subnet's primary and secondary IPv4 address ranges are regional internal IPv4 addresses. For more information, see [Valid IPv4 ranges](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges).




###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click **Create VPC network**.

  3. For **Name** , enter `lb-network`.

  4. In the **Subnets** section, set the **Subnet creation mode** to **Custom**.

  5. In the **New subnet** section, enter the following information:

     * **Name** : `lb-backend-subnet`
     * Select a **Region** : `us-west1`
     * **IP address range** : `10.1.2.0/24`
  6. Click **Done**.

  7. Click **Create**.




###  gcloud 

  1. Create a custom VPC network, named `lb-network`, with the [`gcloud compute networks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/create).
         
         gcloud compute networks create lb-network \
             --subnet-mode=custom \
             --project=PROJECT_B_ID
         

  2. Create a subnet in the `lb-network` VPC network in the `us-west1` region with the [`gcloud compute networks subnets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create).
         
         gcloud compute networks subnets create lb-backend-subnet \
             --network=lb-network \
             --range=10.1.2.0/24 \
             --region=us-west1 \
             --project=PROJECT_B_ID
         




## Configure a backend service in project B

To configure a backend service, you need to do the following:

  1. Create an instance template.
  2. Create an instance group.
  3. Create a health check.
  4. Create a firewall rule.
  5. Create a backend service.



### Create an instance template

The precursor to creating a managed instance group is the creation of an instance template, which is a resource that you can use to create virtual machine (VM) instances. Traffic from clients is load balanced to VMs in an instance group. The managed instance group provides VMs that run the backend servers of an external Application Load Balancer. In this example, the backends serve their own hostnames.

###  Console 

  1. In the Google Cloud console, go to the Compute Engine **Instance templates** page.

[Go to Instance templates](https://console.cloud.google.com/compute/instanceTemplates/list)

  2. Click **Create instance template**.

  3. For **Name** , enter `backend-template`.

  4. In the **Boot disk** section, ensure that the boot disk is set to a Debian image, such as **Debian GNU/Linux 12 (bookworm)**. Click **Change** to change the image if necessary.

  5. Expand the **Advanced options** section.

  6. Expand **Networking** and configure the following fields:

     1. For **Network tags** , enter `load-balanced-backend`.
     2. In the **Network interfaces** section, configure the following fields: 
        * **Network** : `lb-network`
        * **Subnet** : `lb-backend-subnet`
        * **IP stack type** : **IPv4**
     3. Click **Done**
  7. Expand **Management**. In the **Startup script** field, enter the following script:
         
         #! /bin/bash
         apt-get update
         apt-get install apache2 -y
         a2ensite default-ssl
         a2enmod ssl
         # Retrieve the instance name from metadata
         vm_hostname="$(curl -H "Metadata-Flavor:Google" \
         http://metadata.google.internal/computeMetadata/v1/instance/name)"
         # Create an index file
         echo "Page served from: $vm_hostname" | \
         tee /var/www/html/index.html
         # Restart Apache to apply changes
         systemctl restart apache2' \
         

  8. Click **Create**.




###  gcloud 

  1. Create an instance template.
         
         gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
             --region=us-west1 \
             --network=projects/PROJECT_B_ID/global/networks/lb-network \
             --subnet=projects/PROJECT_B_ID/regions/us-west1/subnetworks/lb-backend-subnet \
             --tags=load-balanced-backend \
             --image-family=debian-12 \
             --image-project=debian-cloud \
             --metadata=startup-script='#! /bin/bash
             apt-get update
             apt-get install apache2 -y
             a2ensite default-ssl
             a2enmod ssl
             # Retrieve the instance name from metadata
             vm_hostname="$(curl -H "Metadata-Flavor:Google" \
             http://metadata.google.internal/computeMetadata/v1/instance/name)"
             # Create an index file
             echo "Page served from: $vm_hostname" | \
             tee /var/www/html/index.html
             # Restart Apache to apply changes
             systemctl restart apache2' \
             --project=PROJECT_B_ID
         




### Create a managed instance group

Create a managed instance group to provide the backend servers that handle requests distributed by the global external Application Load Balancer's backend service.

###  Console 

  1. In the Google Cloud console, go to the Compute Engine **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups/list)

  2. Click **Create Instance Group**.

  3. From the options, select **New managed instance group (stateless)**.

  4. For the name of the instance group, enter `lb-backend`.

  5. In the **Instance template** list, select the instance template `backend-template` that you created in the previous step.

  6. In the **Location** section, select **Single zone** , and enter the following values:

     * For **Region** , select `us-west1`.

     * For **Zone** , select `us-west1-a`.

  7. In the **Autoscaling** section, enter the following values:

     * For **Autoscaling mode** , select **On: add and remove instances to the group**.

     * For **Minimum number of instances** , select `2`.

     * For **Maximum number of instances** , select `3`.

  8. In the **Port mapping** section, click **Add port** , and enter the following values:

     * For **Port name** , enter `http`.

     * For **Port number** , enter `80`.

  9. Click **Create**.




###  gcloud 

  1. Create a managed instance group and select the instance template that you created in the preceding step:
         
         gcloud compute instance-groups managed create INSTANCE_GROUP_NAME \
             --zone=us-west1-a \
             --size=2 \
             --template=INSTANCE_TEMPLATE_NAME \
             --project=PROJECT_B_ID
         

  2. Add a named port to the instance group:
         
         gcloud compute instance-groups set-named-ports INSTANCE_GROUP_NAME \
             --named-ports=http:80 \
             --zone=us-west1-a \
             --project=PROJECT_B_ID
         




### Create a health check

Health checks are tests that confirm the availability of backends. Create a health check that uses the HTTP protocol and probes on port 80. Later, you'll attach this health check to the backend service referenced by the load balancer.

###  Console 

  1. In the Google Cloud console, go to the Compute Engine **Health checks** page.

[Go to Health checks](https://console.cloud.google.com/compute/healthChecks)

  2. For the name of the health check, enter `lb-health-check`.

  3. Set the protocol to **HTTP**.

  4. Click **Create**.




###  gcloud 

Create an HTTP health check.
    
    
    gcloud compute health-checks create http lb-health-check \
      --use-serving-port \
      --project=PROJECT_B_ID
    

### Create a firewall rule

For the health check probes, you must create an ingress allow firewall rule at the network level, which for the purpose of this example is `lb-network`. This firewall rule allows health check probes to reach your backend instances. This example uses the following firewall rule:

  * **`fw-allow-health-check`.** An ingress rule, applicable to the instances being load balanced, that allows all TCP traffic from the [Google Cloud health checking systems](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges). This example uses the target tag `load-balanced-backend` to identify the instances to which it should apply.




###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. Click **Create firewall rule** to create the rule to allow incoming SSH connections on the client VM:

     * **Name** : `fw-allow-health-check`
     * **Network** : `lb-network`
     * **Direction of traffic** : **Ingress**
     * **Action on match** : **Allow**
     * **Targets** : **Specified target tags**
     * **Target tags** : `load-balanced-backend`
     * **Source filter** : **IPv4 ranges**
     * **Source IPv4 ranges** : `35.191.0.0/16`
     * **Protocols and ports** : 
       * Choose **Specified protocols and ports**.
       * Select the **TCP** checkbox, and then enter `80` for the port number. As a best practice, limit this rule to just the protocols and ports that match those used by your health check. If you use tcp:80 for the protocol and port, Google Cloud can use HTTP on port 80 to contact your VMs, but it cannot use HTTPS on port 443 to contact them.
  3. Click **Create**.




###  gcloud 

  1. Create the `fw-allow-health-check` firewall rule to allow Google Cloud health checks. This example allows all TCP traffic from health check probers. However, you can configure a narrower set of ports to meet your needs.
         
         gcloud compute firewall-rules create FIREWALL_RULE_NAME \
            --network=lb-network \
            --action=allow \
            --direction=ingress \
            --source-ranges=35.191.0.0/16 \
            --target-tags=load-balanced-backend \
            --rules=tcp \
            --project=PROJECT_B_ID
         




### Create a backend service

Create a global backend service to distribute traffic among backends. As a part of this step, you need to assign the health check that you created to the backend service and add the instance group as the backend to the backend service.

###  Console 

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/list/backends)

  2. Go to the **Backends** section.

  3. Click **Create backend service**.

  4. For **Global backend service** , click the **Create** button next to it.

  5. For the name of the backend service, enter `cross-ref-backend-service`.

  6. For **Backend type** , select **Instance group**.

  7. Set **Protocol** to **HTTP**.

  8. In the **Named port** field, enter `http`. This is the same port name that you entered while creating the managed instance group.

  9. To add _backends_ to the backend service, do the following:

     1. In the **Backends** section, set the **Instance group** to `lb-backend`, which is the managed instance group that you created in an earlier step.

     2. For **Port numbers** , enter `80`.

     3. To add the backend, click **Done**.

  10. To add a health check, in the **Health check** list, select `lb-health-check`, which is the health check that you created earlier.

  11. To create the backend service, click **Create**.




###  gcloud 

  1. Create a global backend service to distribute traffic among backends:
         
         gcloud compute backend-services create BACKEND_SERVICE_NAME \
             --load-balancing-scheme=EXTERNAL_MANAGED \
             --protocol=HTTP \
             --port-name=http \
             --health-checks=HEALTH_CHECK_NAME \
             --global \
             --project=PROJECT_B_ID
         

  2. Add your instance group as the backend to the backend service:
         
         gcloud compute backend-services add-backend BACKEND_SERVICE_NAME \
             --instance-group=INSTANCE_GROUP_NAME \
             --instance-group-zone=us-west1-a \
             --global \
             --project=PROJECT_B_ID
         




## Configure a backend bucket in project B

To create a backend bucket, you need to do the following:

  1. Create the Cloud Storage bucket.
  2. Copy content to the bucket.
  3. Make the bucket publicly accessible.
  4. Create a backend bucket and point it to the Cloud Storage bucket.



### Create a Cloud Storage bucket

###  Console 

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click add_box**Create**.

  3. In the **Name your bucket** box, enter a globally unique name that follows the [naming guidelines](https://docs.cloud.google.com/storage/docs/buckets#naming).

  4. Click **Choose where to store your data**.

  5. Set **Location type** to **Region**.

  6. From the list of regions, select **us-east1**.

  7. Click **Create**.




###  gcloud 

  1. Create a bucket in the `us-east1` region with the [`gcloud storage buckets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/create).
         
         gcloud storage buckets create gs://BUCKET_NAME \
             --default-storage-class=standard \
             --location=us-east1 \
             --uniform-bucket-level-access \
             --project=PROJECT_B_ID
         




Replace the variable BUCKET_NAME with your Cloud Storage bucket name.

### Copy a graphic file to your Cloud Storage bucket

Run the following command in Cloud Shell, replacing the bucket name variables with your unique Cloud Storage bucket name, to copy the graphic file from a public Cloud Storage bucket to the `images/` folder in your own Cloud Storage bucket:
    
    
    gcloud storage cp gs://gcp-external-http-lb-with-bucket/three-cats.jpg gs://BUCKET_NAME/images/
    

### Make your Cloud Storage bucket publicly readable

To make all objects in a bucket readable to everyone on the public internet, grant the principal `allUsers` the Storage Object Viewer role (`roles/storage.objectViewer`).

###  Console 

To grant all users access to view objects in your buckets, repeat the following procedure for each bucket:

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket that you want to make public.

  3. Select the **Permissions** tab near the top of the page.

  4. In the **Permissions** section, click the person_add**Grant access** button. The **Grant access** dialog appears.

  5. In the **New principals** field, enter `allUsers`.

  6. In the **Select a role** field, enter `Storage Object Viewer` in the filter box and select the **Storage Object Viewer** from the filtered results.

  7. Click **Save**.

  8. Click **Allow public access**.




###  gcloud 

To grant all users access to view objects in your buckets, run the [`buckets add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/add-iam-policy-binding).
    
    
    gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME --member=allUsers --role=roles/storage.objectViewer

Replace the bucket name variables with your unique Cloud Storage bucket names.

### Create a backend bucket

Backend buckets serve as a wrapper to the Cloud Storage buckets that you created earlier. They direct incoming traffic to Cloud Storage buckets.

###  Console 

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/list/backends)

  2. Go to the **Backends** section.

  3. Click **Create backend bucket**.

  4. Enter a name for your backend bucket.

  5. Select a Cloud Storage bucket to point your backend bucket to.

  6. Click **Create**.




###  gcloud 

Create a backend bucket with the [`gcloud compute backend-buckets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/create) in project B.
    
    
    gcloud compute backend-buckets create BACKEND_BUCKET_NAME \
      --gcs-bucket-name=BUCKET_NAME \
      --project=PROJECT_B_ID
    

## Configure the load balancer frontend components in project A

This section shows you how to configure the following load balancer frontend components in project A:

  * IP address
  * SSL certificate
  * URL map
  * Target proxy
  * Forwarding rule



### Reserve the load balancer's IP address

Reserve a global static external IP address that can be assigned to the forwarding rule of the load balancer.

###  Console 

  1. In the Google Cloud console, go to the VPC **IP addresses** page.

[Go to IP addresses](https://console.cloud.google.com/networking/addresses/list)

  2. Click **Reserve external**.

  3. On the **Reserve external static IP address** page, for **Name** , enter `cross-ref-ip-address`.

  4. Set **Network Service Tier** to **Premium**.

  5. Set **IP version** to **IPv4**.

  6. Set **Type** to **Global**.

  7. Click **Reserve**.




###  gcloud 

Create a global static external IP address.
    
    
    gcloud compute addresses create IP_ADDRESS_NAME \
        --ip-version=IPV4 \
        --network-tier=PREMIUM \
        --global \
        --project=PROJECT_A_ID
    

### Set up an SSL certificate resource

To create the load balancer, you must have an [SSL certificate resource](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates) that can be attached to the target proxy. The SSL certificate resource can be either a certificate map or a Compute Engine SSL certificate (classic certificate).

#### Certificate map

You can create a certificate map as described in one of the following documents:

  * [Deploy a global Google-managed certificate with load balancer authorization](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-lb-auth)
  * [Deploy a global Google-managed certificate with DNS authorization](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-dns-auth)
  * [Deploy a global Google-managed certificate with Certificate Authority Service](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-cas)
  * [Deploy a global self-managed certificate](https://docs.cloud.google.com/certificate-manager/docs/deploy-self-managed)



#### Compute Engine SSL certificate

For an HTTPS load balancer, create a Compute Engine SSL certificate resource as described in one of the following documents:

  * [Use self-managed SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs)
  * [Use Google-managed SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs)



We recommend using a Google-managed certificate.

**Warning:** Don't use a self-signed certificate for production purposes.

### Configure the components of a global external Application Load Balancer

###  Console 

#### Select the load balancer type

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/list)

  2. Click **Create load balancer**.
  3. For **Type of load balancer** , select **Application Load Balancer (HTTP/HTTPS)** and click **Next**.
  4. For **Public facing or internal** , select **Public facing (external)** and click **Next**.
  5. For **Global or single region deployment** , select **Best for global workloads** and click **Next**.
  6. For **Load balancer generation** , select **Global external Application Load Balancer** and click **Next**.
  7. Click **Configure**.



#### Basic configuration

  1. Enter a name for your load balancer.
  2. Keep the page open to continue.



#### Configure the frontend

**For HTTP:**

  1. Click **Frontend configuration**.
  2. Enter a name for the forwarding rule.
  3. Set the **Protocol** to `HTTP`.
  4. Select the **IP address** that you created in Reserve the load balancer's IP address.
  5. Set the **Port** to `80`.
  6. Click **Done**.



**For HTTPS:**

If you are using HTTPS between the client and the load balancer, you need one or more SSL certificate resources to configure the proxy.

  1. Click **Frontend configuration**.
  2. Enter a name for the forwarding rule.
  3. In the **Protocol** field, select `HTTPS (includes HTTP/2)`.
  4. Select the **IP address** that you created in Reserve the load balancer's IP address.
  5. Ensure that the **Port** is set to `443` to allow HTTPS traffic.
  6. For **Choose certificate repository** , select **Use certificate map** or **Use classic certificates**.
  7. Depending on your selection, select a certificate map or a classic certificate.
  8. Click **Done**.



#### Configure the backend

  1. Click **Backend configuration**.
  2. Click **Cross-project backend services**.
  3. For **Project ID** , enter the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) for project B.
  4. From the **Select backend services** list, select the backend service from project B that you want to use.
  5. Click **OK**.

**Note:** You cannot reference a backend bucket, located in a different project, in the **Backend configuration** section of the Google Cloud console. However, you can create and reference a backend bucket in the **Routing rules** section.

#### Configure the routing rules

  1. Click **Routing rules**.

  2. For mode, select **Advanced host and path rule**.

  3. Select **Add host and path rule**.

  4. In the **Hosts** field, enter `*` to match all hostnames.

  5. In the **Path matcher** section, enter the following YAML configuration.
         
         defaultService: projects/PROJECT_B_ID/global/backendServices/BACKEND_SERVICE_NAME
         name: PATH_MATCHER_NAME
         pathRules:
         - paths:
           - /images/*
           service: projects/PROJECT_B_ID/global/backendBuckets/BACKEND_BUCKET_NAME
         

The path matcher, in this example, is comprised of a path rule and a default service. The path rule routes all requests to `/images/*` to a backend bucket. All other requests are routed to the default backend service.

  6. Click **Done**.




For information about traffic management, see [Traffic management overview](https://docs.cloud.google.com/load-balancing/docs/https/traffic-management-global).

#### Review and finalize the configuration

  1. Review the different components of the load balancer that you have configured in the preceding steps. You will notice that the **Backends** section has reference to both the backend service and the backend bucket.

  2. Click **Create**.




###  gcloud 

To create the aforementioned load balancing components using the gcloud CLI, follow these steps:

  1. Create a URL map with the [`gcloud compute url-maps create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/create).
         
         gcloud compute url-maps create URL_MAP_NAME \
           --default-service=projects/PROJECT_B_ID/global/backendServices/BACKEND_SERVICE_NAME \
           --global \
           --project=PROJECT_A_ID
         

  2. Add a path matcher for the URL map. The path matcher, in this example, is comprised of a path rule and a default service. The path rule routes all requests to `/images/*` to a backend bucket. All other requests are routed to the default backend service.
         
         gcloud compute url-maps add-path-matcher URL_MAP_NAME \
           --path-matcher-name=PATH_MATCHER_NAME \
           --default-service=projects/PROJECT_B_ID/global/backendServices/BACKEND_SERVICE_NAME  \
           --backend-bucket-path-rules=/images/*=projects/PROJECT_B_ID/global/backendBuckets/BACKEND_BUCKET_NAME
         

  3. Create a target proxy with the [`gcloud compute target-http-proxies create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-http-proxies/create).

**For HTTP traffic** , create a target HTTP proxy to route requests to the URL map:
         
         gcloud compute target-http-proxies create TARGET_HTTP_PROXY_NAME \
           --url-map=URL_MAP_NAME \
           --global \
           --project=PROJECT_A_ID
         

**For HTTPS traffic** , create a target HTTPS proxy to route requests to the URL map. The proxy is the part of the load balancer that holds the SSL certificate for an HTTPS load balancer. After you create the certificate, you can attach the certificate to the HTTPS target proxy.
         
         gcloud compute target-https-proxies create TARGET_HTTPS_PROXY_NAME \
           --url-map=URL_MAP_NAME \
           --ssl-certificates=CERTIFICATE_NAME \
           --global \
           --project=PROJECT_A_ID
         

Replace `CERTIFICATE_NAME` with the name of the SSL certificate.

  4. Create a global forwarding rule with the [`gcloud compute forwarding-rules create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create).

**For HTTP traffic** , create the global forwarding rules to route incoming requests to the HTTP target proxy:
         
         gcloud compute forwarding-rules create HTTP_FORWARDING_RULE_NAME \
           --load-balancing-scheme=EXTERNAL_MANAGED \
           --address=IP_ADDRESS_NAME \
           --global \
           --target-http-proxy=TARGET_HTTP_PROXY_NAME \
           --ports=80 \
           --project=PROJECT_A_ID
         

**For HTTPS traffic** , create the global forwarding rules to route incoming requests to the HTTPS target proxy:
         
         gcloud compute forwarding-rules create HTTPS_FORWARDING_RULE_NAME \
           --load-balancing-scheme=EXTERNAL_MANAGED \
           --address=IP_ADDRESS_NAME \
           --global \
           --target-https-proxy=TARGET_HTTPS_PROXY_NAME \
           --ports=443 \
           --project=PROJECT_A_ID
         




## Test the load balancer

It can take a few minutes for your load balancer to be configured following which you can send a request to the load balancer. In this example, the request is sent to the HTTP forwarding rule of the load balancer.

Get the IP address of the load balancer's HTTP forwarding rule.
    
    
    gcloud compute forwarding-rules describe HTTP_FORWARDING_RULE_NAME \
        --global
    

If you were to point your browser to http://IP_ADDRESS, the request is routed to the backend service, which returns a page with minimal information about the backend instance.

However, if you were to point your browser to http://IP_ADDRESS/images/three-cats.jpg, the request to `/images/*` is routed to the backend bucket, which returns the graphic file.

## What's next

  * [External Application Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/https)
  * [SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates)
  * [Clean up a load balancing setup](https://docs.cloud.google.com/load-balancing/docs/cleaning-up-lb-setup)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
