---
url: https://docs.cloud.google.com/load-balancing/docs/https/migrate-from-classic-global/
title: Migrate resources from classic to global external Application Load Balancer \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:41.508264+00:00
---

# Migrate resources from classic to global external Application Load Balancer  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/https/migrate-from-classic-global/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Migrate resources from classic to global external Application Load Balancer Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to migrate classic Application Load Balancer infrastructure resources to the global external Application Load Balancer infrastructure.

## Before you begin

Ensure your setup meets the following prerequisites.

### Set a default project

###  Console 

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 




###  gcloud 
    
    
    gcloud config set project PROJECT_ID
    

Replace `PROJECT_ID` with the project that you are using for this guide.

### Permissions

To follow this document, you must have permissions to create Compute Engine virtual machine (VM) instances, firewall rules, reserved IP addresses, and Cloud Storage buckets in a Google Cloud project. You must be either a project [owner or editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic), or you must have the following [Compute Engine IAM roles](https://docs.cloud.google.com/compute/docs/access/iam):

Task | Required role  
---|---  
Create instances | [Compute Instance Admin role](https://docs.cloud.google.com/compute/docs/access/iam#compute.instanceAdmin) (`roles/compute.instanceAdmin`)   
Add and remove firewall rules | [Compute Security Admin role](https://docs.cloud.google.com/compute/docs/access/iam#compute.securityAdmin) (`roles/compute.securityAdmin`)   
Create load balancer components | [Compute Network Admin role](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin) (`roles/compute.networkAdmin`)   
Create a project (optional) | [Project Creator role](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project) (`roles/resourcemanager.projectCreator`)   
Create Cloud Storage buckets | [Storage Object Admin role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) (`roles/storage.objectAdmin`)   
  
For more information, see the following guides:

  * [Managing access control for Cloud Load Balancing using IAM](https://docs.cloud.google.com/load-balancing/docs/access-control#managing-iam)
  * [IAM Conditions for forwarding rules](https://docs.cloud.google.com/load-balancing/docs/access-control/iam-conditions)



## Create classic Application Load Balancer resources

In this document, you create the following classic Application Load Balancer resources and then migrate them to the global external Application Load Balancer infrastructure.

  * A managed instance group with VMs.
  * A Cloud Storage bucket.
  * An HTTP classic Application Load Balancer with the managed instance group and the Cloud Storage bucket as backends.



### Create a managed instance group

This section describes how to create a managed instance group with Linux VMs that have Apache running. A managed instance group creates each of its managed instances based on the instance templates that you specify.

#### Create an instance template

###  Console 

  1. In the Google Cloud console, go to the **Instance templates** page.

[Go to Instance templates](https://console.cloud.google.com/compute/instanceTemplates/list)

  2. Click **Create instance template**.

  3. For **Name** , enter `lb-backend-template`.

  4. For **Region** , select `REGION`.

  5. In the **Boot disk** section, ensure that **Image** of the boot disk is set to a Debian image, such as **Debian GNU/Linux 12 (bookworm)**. These instructions use commands that are only available on Debian, such as `apt-get`.

  6. Click **Advanced options**.

  7. Click **Networking** , and in the **Network tags** field, enter `allow-health-check`.

  8. Click **Management** , and enter the following script into the **Startup script** field.
         
         #! /bin/bash
         apt-get update
         apt-get install apache2 -y
         a2ensite default-ssl
         a2enmod ssl
         vm_hostname="$(curl -H "Metadata-Flavor:Google" \
         http://metadata.google.internal/computeMetadata/v1/instance/name)"
         echo "Page served from: $vm_hostname" | \
         tee /var/www/html/index.html
         systemctl restart apache2
         

  9. Click **Create**.




###  gcloud 

Run the [`gcloud compute instance-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create) to create the template.
    
    
    gcloud compute instance-templates create lb-backend-template \
        --region=REGION \
        --network=default \
        --subnet=default \
        --tags=allow-health-check \
        --image-family=debian-12 \
        --image-project=debian-cloud \
        --metadata=startup-script='#! /bin/bash
          apt-get update
          apt-get install apache2 -y
          a2ensite default-ssl
          a2enmod ssl
          vm_hostname="$(curl -H "Metadata-Flavor:Google" \
        http://metadata.google.internal/computeMetadata/v1/instance/name)"
        echo "Page served from: $vm_hostname" | \
        tee /var/www/html/index.html
        systemctl restart apache2'
    

#### Create the managed instance group

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click **Create instance group**.

  3. Select **New managed instance group (stateless)**.

  4. For **Name** , enter `lb-backend-example`.

  5. For **Instance template** , select the instance template `lb-backend-template`.

  6. Under **Location** , select **Single zone**.

  7. For **Region** , select `REGION`.

  8. For **Zone** , select `ZONE`.

  9. For **Autoscaling mode** , select **On: add and remove instances to the group**.

Set **Minimum number of instances** and **Maximum number of instances** to `2`.

  10. In the **Port mapping** section, click **Add port**.

  11. For the port name, enter `http`. For the port number, enter `80`.

  12. Click **Create**.




###  gcloud 

Run the [`gcloud compute instance-groups managed create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/create) to create the managed instance group based on the template.
    
    
    gcloud compute instance-groups managed create lb-backend-example \
        --template=lb-backend-template \
        --size=2 --zone=ZONE
    

Run the following command to add a named port to the instance group:
    
    
    gcloud compute instance-groups set-named-ports lb-backend-example \
        --named-ports http:80 \
        --zone ZONE
    

### Configure a firewall rule

In this section, you create the `fw-allow-health-check` firewall rule and use the target tag `allow-health-check` to identify the VMs. This is an ingress rule that allows traffic from the [Google Cloud health checking systems](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges).

###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. Click **Create firewall rule**.

  3. For **Name** , enter `fw-allow-health-check`.

  4. For **Network** , select **default**.

  5. For **Targets** , select **Specified target tags**.

  6. In the **Target tags** field, enter `allow-health-check`.

  7. Set **Source filter** to **IPv4 ranges**.

  8. Set **Source IPv4 ranges** to `35.191.0.0/16`.

  9. In the **Protocols and ports** section, select **Specified protocols and ports**.

  10. Select the **TCP** checkbox, and then type `80` for the port number.

  11. Click **Create**.




###  gcloud 

Run the [`gcloud compute firewall-rules create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create) to create the firewall rule.
    
    
    gcloud compute firewall-rules create fw-allow-health-check \
        --network=default \
        --action=allow \
        --direction=ingress \
        --source-ranges=35.191.0.0/16 \
        --target-tags=allow-health-check \
        --rules=tcp:80
    

### Create a Cloud Storage bucket

In this section, you create a Cloud Storage bucket for the load balancer to access. For production deployments, we recommend that you choose a [multi-region bucket](https://docs.cloud.google.com/storage/docs/locations#location-mr), which automatically replicates objects across multiple Google Cloud regions. This can improve the availability of your content and improve failure tolerance across your application.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Storage Buckets** page.

[Go to Cloud Storage Buckets](https://console.cloud.google.com/storage/browser)

  2. Click **Create**.

  3. In the **Name your bucket** box, enter `storage-backend-bucket` and click **Continue**.

  4. Click **Choose where to store your data**.

  5. Set **Location type** to **Region** , and specify `REGION`.

  6. Click **Create**.

  7. Optional: If you see the Public access will be prevented dialog, clear the **Enforce public access prevention on this bucket** checkbox and click **Confirm**.




###  gcloud 

Run the [`gcloud storage buckets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/create) to create the bucket:
    
    
    gcloud storage buckets create gs://storage-backend-bucket \
        --default-storage-class=standard \
        --location=REGION --uniform-bucket-level-access
    

#### Transfer content to your Cloud Storage buckets

To test the bucket after you create the load balancer, copy the following image file from a public Cloud Storage bucket to your own Cloud Storage bucket.

###  gcloud 

  1. Click terminal **Activate Cloud Shell**.

  2. Run the following commands in Cloud Shell:



    
    
    gcloud storage cp gs://gcp-external-http-lb-with-bucket/three-cats.jpg gs://storage-backend-bucket/never-fetch/
    

In the Google Cloud console, click **Refresh** on the bucket's details page to verify that the file has been copied successfully.

#### Make your Cloud Storage bucket publicly readable

When you make a Cloud Storage bucket publicly readable, anyone on the internet can list and view their objects, and view their metadata (excluding ACLs). _Don't include sensitive information in your public buckets._

To reduce the likelihood of accidental exposure of sensitive information, don't store public objects and sensitive data in the same bucket.

###  Console 

To grant all users access to view objects in your buckets, follow these steps:

  1. In the Google Cloud console, go to the **Cloud Storage Buckets** page.

[Go to Cloud Storage Buckets](https://console.cloud.google.com/storage/browser)

  2. Click the `storage-backend-bucket` name, and then click the **Permissions** tab.

  3. Click **Grant access**.

  4. In the **New principals** box, enter `allUsers`.

  5. In the **Select a role** box, select **Cloud Storage > Storage Object Viewer**.

  6. Click **Save**.

  7. Click **Allow public access**.




###  gcloud 

Run the [`gcloud storage buckets add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/add-iam-policy-binding) to grant all users access to view objects in your buckets:
    
    
    gcloud storage buckets add-iam-policy-binding gs://storage-backend-bucket \
        --member=allUsers \
        --role=roles/storage.objectViewer
    

### Reserve an external IP address

Now that your instances are up and running, set up a [global static external IP address](https://docs.cloud.google.com/compute/docs/ip-addresses#externaladdresses) that your customers use to reach your load balancer.

###  Console 

  1. In the Google Cloud console, go to the **IP addresses** page.

[Go to IP addresses](https://console.cloud.google.com/networking/addresses/list)

  2. To reserve an IPv4 address, click **Reserve external**.

  3. On the **Reserve external static IP address** page, for **Name** , enter `lb-ipv4-1`.

  4. Set **Network Service Tier** to **Premium**.

  5. Set **IP version** to **IPv4**.

  6. Set **Type** to **Global**.

  7. Click **Reserve**.




###  gcloud 

To reserve an external IP address, run the following command:
    
    
    gcloud compute addresses create lb-ipv4-1 \
        --ip-version=IPV4 \
        --network-tier=PREMIUM \
        --global
      

To note the IPv4 address that was reserved, run the following command:
    
    
    gcloud compute addresses describe lb-ipv4-1 \
        --format="get(address)" \
        --global
      

### Set up the classic Application Load Balancer

In this section, you use HTTP (frontend) between the client and the load balancer.

###  Console 

#### Select the load balancer type

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/list)

  2. Click **Create load balancer**.
  3. For **Type of load balancer** , select **Application Load Balancer (HTTP/HTTPS)** and click **Next**.
  4. For **Public facing or internal** , select **Public facing (external)** and click **Next**.
  5. For **Global or single region deployment** , select **Best for global workloads** and click **Next**.
  6. For **Load balancer generation** , select **Classic Application Load Balancer** and click **Next**.
  7. Click **Configure**.



**Basic configuration**

  1. In the **Load balancer name** field, enter `web-map-http`.
  2. Click **Frontend configuration** , configure the following fields, and then click **Done**. 
     * **Protocol** : **HTTP**.
     * **IP version** : **IPv4**
     * **IP address** : **`lb-ipv4-1`**
     * **Port** : `443`
  3. Click **Backend configuration**.
  4. In **Backend services & backend buckets**, click **Create a backend service** , and then do the following: 
     1. Configure the following fields: 
        * **Name** : `web-backend-service`
        * **Protocol** : **HTTP**
        * **Named Port** : **http**
     2. In the **Health check** list, click **Create a health check** , and then enter the following information: 
        * **Name** : `http-basic-check`
        * **Protocol** : **HTTP**
     3. Click **Create**.
     4. In the **Backends > New backend** section, configure the following fields, and then click **Done**. 
        * **Instance group** : **lb-backend-example**
        * **Port numbers** : `80`
     5. In the **Logging** section, select the **Enable logging** checkbox.
     6. Click **Create**.
  5. Click **OK**.
  6. In **Backend services & backend buckets**, click **Create a backend bucket** , configure the following fields, and then click **Create**. 
     * **Backend bucket name** : `cats`
     * **Cloud Storage bucket** : `storage-backend-bucket`
  7. Click **OK**.
  8. Click **Host and path rules**.
  9. For `cats`, enter `*` in the **Host 2** field, and `/never-fetch/*` in the **Path 2** field.
  10. Click **Review and finalize**.
  11. Review your load balancer configuration settings.
  12. Click **Create**.



###  gcloud 

  1. Create a health check.
         
         gcloud compute health-checks create http http-basic-check \
             --port 80
         

  2. Create a backend service.
         
         gcloud compute backend-services create web-backend-service \
             --load-balancing-scheme=EXTERNAL \
             --protocol=HTTP \
             --port-name=http \
             --health-checks=http-basic-check \
             --enable-logging \
             --logging-sample-rate=1.0 \
             --enable-cdn \
             --global
         

  3. Add your instance group as the backend to the backend service.
         
         gcloud compute backend-services add-backend web-backend-service \
             --instance-group=lb-backend-example \
             --instance-group-zone=ZONE \
             --global
         

  4. Add a backend bucket.
         
         gcloud compute backend-buckets create cats \
             --gcs-bucket-name=storage-backend-bucket
         

  5. Create a URL map to route the incoming requests to the backend service and backend bucket.
         
         gcloud compute url-maps create web-map-http \
             --default-service web-backend-service
         
         
         gcloud compute url-maps add-path-matcher web-map-http \
             --path-matcher-name=cats-path-matcher \
             --default-backend-bucket=cats \
             --new-hosts="*" \
             --backend-bucket-path-rules="/never-fetch/*=cats"
         

  6. Create a target HTTP proxy to route requests to URL maps.
         
         gcloud compute target-http-proxies create http-lb-proxy \
             --url-map=web-map-http
         

  7. Create a global forwarding rule to route incoming requests to the proxy.
         
         gcloud compute forwarding-rules create web-map-http-forwarding-rule \
             --load-balancing-scheme=EXTERNAL \
             --address=lb-ipv4-1 \
             --global \
             --target-http-proxy=http-lb-proxy \
             --ports=80
         




### Test traffic sent to your instances

Now that the load balancing service is running, you can send traffic to the forwarding rule and watch the traffic be dispersed to different instances.

###  Console 

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/networking/loadbalancing/)

  2. Click `web-map-http`.

  3. In the **Frontend** section, note the **IP:Port** of the load balancer.

  4. To test the backend instance, enter `http://IP_ADDRESS` in the address bar of the web browser.

Your browser renders a page with content showing the name of the instance that served the page, along with its zone (for example, `Page served from: lb-backend-example-xxxx`).

  5. To test the backend bucket, enter `http://IP_ADDRESS/never-fetch/three-cats.jpg` in the address bar of the web browser.

Your browser renders the image.




## Migrate classic Application Load Balancer resources

In this section, you perform the following steps to migrate the load balancer to the global external Application Load Balancer infrastructure:

  1. Migrate the backend services. You must migrate all backend services associated with a forwarding rule before you can proceed to migrate the forwarding rule.
  2. Migrate the backend buckets. If you're using the Google Cloud console, you'll migrate any backend buckets along with the forwarding rule.
  3. Migrate the forwarding rule.



Due to architectural differences, when migrating to the global external Application Load Balancer, you might see an increase in the number of connections to your backends, especially when using the HTTP/1.1 protocol. This can lead to increased memory consumption on the backend instances. Monitor your backend resource usage during and after migration. 

### Migrate the backend service

###  Console 

**Prepare the backend service for migration**

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/list)

  2. Click **`web-map-http`**.

  3. Click the **Migration** tab.

  4. In the **Backend services** section, for **`web-backend-service`** , verify the following fields and then click **Manage migration**.

     * **Status** : **Not started**
     * **Scheme activity** : **EXTERNAL: 100% EXTERNAL_MANAGED:0%**
  5. In the **Manage migration** pane, for **Status change** , select **Prepare**.

  6. Click **Save**.




Wait for some time, at least six minutes, before you proceed. The **Status** changes to **Prepared for test**.

**Send a percentage of traffic to the global external Application Load Balancer infrastructure**

  1. For **`web-backend-service`** , click **Manage migration**
  2. In the **Manage migration** pane, for **Status change** , select **Test by percentage**.
  3. For **Testing percentage** , enter `10`. This means that 10 percent of requests will be sent to the global external Application Load Balancer infrastructure for testing and the remaining 90 percent of requests continue to go to the classic Application Load Balancer infrastructure.
  4. Click **Save**.

Wait for some time, at least six minutes, until **Status** changes to **Testing by %** and **Migration rate** changes to **10%**.

  5. Test the load balancer to ensure that requests are being served as expected.

Enter `http://IP_ADDRESS` in the address bar of the web browser. You should see the `Page served from: lb-backend-example-xxxx` message.

You can check the [load balancer's metrics](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring#monitoring_metrics) to verify that the overall balance of requests matches your configured migration rate.

  6. You can repeat these steps to progressively increase the percentage of traffic sent to the global external Application Load Balancer infrastructure until you are satisfied that the load balancer works as expected.




**Send all traffic to the global external Application Load Balancer infrastructure**

  1. For **`web-backend-service`** , click **Manage migration**
  2. In the **Manage migration** pane, for **Status change** , select **Test all traffic**. This means that all requests will be sent to the global external Application Load Balancer infrastructure.
  3. Click **Save**.

The **Status** changes to **Testing all traffic** and **Migration rate** changes to **100%**. Wait for some time, at least six minutes, before you proceed to the next step.




**Migrate to the`EXTERNAL_MANAGED` load balancing scheme**

  1. For **`web-backend-service`** , click **Manage migration**.
  2. In the **Manage migration** pane, for **Status change** , select **Migrate**.
  3. Click **Save**.

Wait for some time, at least six minutes, for the resource to be migrated. The **Status** column changes to **Migrated** and **Scheme activity** to **EXTERNAL: 0% EXTERNAL_MANAGED:100%**.




You must migrate every backend service associated with a forwarding rule before you can proceed to migrate the forwarding rule. Repeat these steps as needed.

###  gcloud 

  1. Prepare the backend service for migration.
         
         gcloud compute backend-services update web-backend-service \
           --external-managed-migration-state=PREPARE \
           --global
         

Wait for some time (at least six minutes).

  2. Send some traffic, such as 10%, to the backend service.
         
         gcloud compute backend-services update web-backend-service \
           --external-managed-migration-state=TEST_BY_PERCENTAGE \
           --external-managed-migration-testing-percentage=10 \
           --global
         

Wait for some time (at least six minutes).

After the resource is ready, it sends 10% of requests to the global external Application Load Balancer infrastructure and 90% of requests to the classic Application Load Balancer infrastructure.

  3. Access the load balancer.

Enter `http://IP_ADDRESS` in the address bar of the web browser. If you see the `Page served from: lb-backend-example-xxxx` message, run the following command to increase the percentage.
         
         gcloud compute backend-services update web-backend-service \
           --external-managed-migration-state=TEST_BY_PERCENTAGE \
           --external-managed-migration-testing-percentage=50 \
           --global
         

You can check the [load balancer's metrics](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring#monitoring_metrics) to verify that the overall balance of requests matches your configured migration rate.

Repeat the process until you reach 100%.

  4. Optional: Check the logs of the backend service.

  5. Complete the test and send all traffic to the backend service.
         
         gcloud compute backend-services update web-backend-service \
           --external-managed-migration-state=TEST_ALL_TRAFFIC \
           --global
         

Wait for some time, at least six minutes, before you proceed to the next step.

  6. Optional: Check the logs of the backend service.

  7. Change the scheme of the backend service to `EXTERNAL_MANAGED`.
         
         gcloud compute backend-services update web-backend-service \
           --load-balancing-scheme=EXTERNAL_MANAGED \
           --global
         

Wait for some time (at least six minutes) for the backend service to be fully migrated to the global external Application Load Balancer infrastructure.

  8. Optional: Check the logs of the backend service. You see that the load balancing scheme is `EXTERNAL_MANAGED`.




You must migrate every backend service associated with a forwarding rule before you can proceed to migrate the forwarding rule. Repeat these steps as needed.

### Migrate the backend bucket

###  Console 

You can't use Google Cloud console to migrate backend buckets because they are migrated along with forwarding rules. To migrate backend buckets individually, use the Google Cloud CLI.

###  gcloud 

  1. Prepare the backend bucket for migration.
         
         gcloud compute forwarding-rules update web-map-http-forwarding-rule \
           --external-managed-backend-bucket-migration-state=PREPARE \
           --global
         

Wait for some time (at least six minutes).

  2. Send some traffic, such as 10%, to the backend bucket.
         
         gcloud compute forwarding-rules update web-map-http-forwarding-rule \
           --external-managed-backend-bucket-migration-state=TEST_BY_PERCENTAGE \
           --external-managed-backend-bucket-migration-testing-percentage=10 \
           --global
         

Wait for some time (at least six minutes).

After the resource is ready, it sends 10% of requests to the global external Application Load Balancer infrastructure and 90% of requests to the classic Application Load Balancer infrastructure.

  3. Access the backend bucket.

Enter `http://IP_ADDRESS/never-fetch/three-cats.jpg` in the address bar of the web browser. If you see the image of cats, run the following command to increase the percentage. Repeat the process until you reach 100%.
         
         gcloud compute forwarding-rules update web-map-http-forwarding-rule \
           --external-managed-backend-bucket-migration-state=TEST_BY_PERCENTAGE \
           --external-managed-backend-bucket-migration-testing-percentage=50 \
           --global
         

  4. Optional: Check the logs of the backend bucket.

  5. Complete the test and send all traffic to the backend bucket.
         
         gcloud compute forwarding-rules update web-map-http-forwarding-rule \
           --external-managed-backend-bucket-migration-state=TEST_ALL_TRAFFIC \
           --global
         

  6. Optional: Check the logs of the backend bucket.




### Migrate the forwarding rule

###  Console 

**Prepare the forwarding rule for migration**

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/list)

  2. Click **`web-map-http`**.

  3. Click the **Migration** tab.

  4. In the **Forwarding rules** section, for **`web-map-http-forwarding-rule`** , verify the following fields and then click **Manage migration**.

     * **Status** : **Not started**
     * **Scheme activity** : **EXTERNAL: 100% EXTERNAL_MANAGED:0%**
  5. In the **Manage migration** pane, for **Status change** , select **Prepare**.

  6. Click **Save**.




Wait for some time, at least six minutes, before you proceed. The **Status** changes to **Prepared for test**.

**Send a percentage of traffic to the global external Application Load Balancer infrastructure**

  1. For **`web-map-http-forwarding-rule`** , click **Manage migration**
  2. In the **Manage migration** pane, for **Status change** , select **Test by percentage**.
  3. For **Testing percentage** , enter `10`. This means that 10 percent of requests will be sent to the global external Application Load Balancer infrastructure for testing and the remaining 90 percent of requests continue to go to the classic Application Load Balancer infrastructure.
  4. Click **Save**.

Wait for some time until **Status** changes to **Testing by %** and **Migration rate** changes to **10%**.

  5. Test the load balancer to ensure that requests are being served as expected.

Enter `http://IP_ADDRESS` in the address bar of the web browser. You should see the `Page served from: lb-backend-example-xxxx` message.

You can check the [load balancer's metrics](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring#monitoring_metrics) to verify that the overall balance of requests matches your configured migration rate.

  6. You can repeat these steps to progressively increase the percentage of traffic sent to the global external Application Load Balancer infrastructure until you are satisfied that the load balancer works as expected.




**Send all traffic to the global external Application Load Balancer infrastructure**

  1. For **`web-map-http-forwarding-rule`** , click **Manage migration**
  2. In the **Manage migration** pane, for **Status change** , select **Test all traffic**. This means that all requests will be sent to the global external Application Load Balancer infrastructure.
  3. Click **Save**.

The **Status** changes to **Testing all traffic** and **Migration rate** changes to **100%**. Wait for some time, at least six minutes, before you proceed to the next step.




**Migrate to the`EXTERNAL_MANAGED` load balancing scheme**

  1. For **`web-map-http-forwarding-rule`** , click **Manage migration**.
  2. In the **Manage migration** pane, for **Status change** , select **Migrate**.
  3. Click **Save**.

Wait for some time, at least six minutes, for the resource to be migrated. The **Status** column changes to **Migrated** and **Scheme activity** to **EXTERNAL: 0% EXTERNAL_MANAGED:100%**.




###  gcloud 

  1. Change the scheme of the forwarding rule to `EXTERNAL_MANAGED`.
         
         gcloud compute forwarding-rules update web-map-http-forwarding-rule \
           --load-balancing-scheme=EXTERNAL_MANAGED \
           --global
         

Wait for some time (at least six minutes) for the forwarding rule to be fully migrated to the global external Application Load Balancer infrastructure.

  2. Optional: Check the logs of the forwarding rule. You see that the load balancing scheme is `EXTERNAL_MANAGED`.




## What's next

  * [Roll back migrated resources to classic Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/roll-back-migrated-resources)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
