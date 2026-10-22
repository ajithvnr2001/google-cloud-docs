---
url: https://docs.cloud.google.com/compute/docs/tutorials/globally-autoscaling-a-web-service-on-compute-engine/
title: Globally autoscaling a web service on Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:16.857720+00:00
---

# Globally autoscaling a web service on Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/tutorials/globally-autoscaling-a-web-service-on-compute-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Globally autoscaling a web service on Compute Engine Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows how to set up a globally available web service with regional Compute Engine [managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) that automatically scale to meet capacity needs. You can use the techniques shown in this tutorial for implementing your own globally distributed and scalable project on Compute Engine. 

## Objectives

  * Deploy multiple regional Compute Engine managed instance groups with autoscaling enabled.
  * Create a cross-region load balancer.
  * Generate test traffic from different regions across the globe.
  * Use the [Google Cloud console](https://docs.cloud.google.com/storage/docs/cloud-console) to visualize how the load balancer routes requests and how the instance groups autoscale to meet demand.



## Costs

This tutorial uses billable components of Google Cloud including: 

  * Compute Engine



## Before you begin

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  3. Enable the Compute Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=compute_engine)




## Application architecture

The application includes the following Compute Engine components:

  1. [Instance template](https://docs.cloud.google.com/compute/docs/instance-templates): A template used to create each instance in the instance groups.
  2. [Instance groups](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups): Multiple instance groups that autoscale based on incoming traffic.
  3. [Load balancer](https://docs.cloud.google.com/load-balancing/docs/https): An HTTP load balancer that distributes traffic among the instance groups.
  4. [Instances](https://docs.cloud.google.com/compute/docs/instances): Multiple testing instances to generate test traffic from different parts of the globe.



![System architecture diagram showing a load balancer with multiple regional instance groups](https://docs.cloud.google.com/static/compute/docs/tutorials/images/globally-autoscaling-compute-engine-architecture.png)

**Note:** For more information about geographical regions and zones, see the documentation for [Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones).

## Set up the web service

### Create the instance groups

### Console

  1. Create a network for the instance groups.

     1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks)

     2. Click **Create VPC Network**.

     3. Set the **Name** to `fortressnet`.

     4. Set **Subnet creation mode** to **Automatic**.

     5. Click **Create** at the bottom of the page.

  2. Create a firewall rule for the network. This rule will allow all HTTP requests sent to your instances.

     1. In the Google Cloud console, go to the **Firewall rules** page.

[Go to Firewall rules](https://console.cloud.google.com/networking/firewalls)

     2. Click **Create Firewall Rule**.

     3. Set the **Name** to `fortressnet-allow-http`.

     4. For **Network** select `fortressnet`.

     5. For **Targets** select `All instances in the network`.

     6. Set **Source IPv4 ranges** to `0.0.0.0/0`.

     7. For **Protocols and ports** , choose **Specified protocols and ports** and then select the **tcp** checkbox and enter `80`.

     8. Click **Create**.

  3. Create an instance template. Include a startup script that starts up a simple Apache web server on each instance.

     1. In the Google Cloud console, go to the **Instance templates** page.

[Go to Instance templates](https://console.cloud.google.com/compute/instanceTemplates)

     2. Click **Create instance template**.

     3. Set the **Name** to `fort-template`.

     4. For **Machine configuration** , select `e2-micro` (2 vCPU, 1 GB memory).

     5. In the **Advanced options** section, expand **Networking** , and then do the following:

        1. In the **Network interfaces** section, expand the network interface to edit it.
        2. For **Network** , select `fortressnet`.
     6. In the **Management** section, for **Automation** enter the following **Startup script** : 
            
            apt update && apt -y install apache2
            

     7. Click **Create**.

  4. Create multiple regional managed instance groups using the instance template. Configure autoscaling for each instance group.

     1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

     2. Click **Create instance group** to create a new managed instance group.

     3. Select **New managed instance group (stateless)**.

     4. Set the **Name** to `us-central1-pool`.

     5. For **Instance template** , select `fort-template`.

     6. For **Location** , select **Multiple zones**.

     7. For **Region** , select `us-central1`. For **Zones** , leave the predefined values selected.

     8. For **Autoscaling mode** , select **On: add and remove instances to the group**.

     9. Set **Minimum number of instances** to `1`.

     10. Set **Maximum number of instances** to `5`.

     11. For **Autoscaling signals** , edit the default selection (CPU utilization) and set the **Signal type** to **HTTP load balancing utilization**.

     12. Set **Target HTTP load balancing utilization** to `80`.

     13. Click **Done**.

     14. Click **Create**. A dialog displays the message that you must also assign the instance group to a backend service of an HTTP load balancer.

     15. In the confirmation dialog, click **Confirm**. You can configure the load balancer after you create all the instance groups.

     16. Repeat these steps to create two more instance groups with the following changes:

        * Create a group with **Name** as `europe-west1-pool` and **Region** as `europe-west1`.
        * Create a group with **Name** as `asia-east1-pool` and **Region** as `asia-east1`.
**Note:** **Autoscaling** of instance groups can be based on different criteria. Because your web service employs a **Load Balancer** , your autoscalers should be configured to scale based on **load balancing usage**. For more information, see [Scaling based on load balancing serving capacity](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-load-balancing).
  5. (Optional) Verify the instances are healthy and serving HTTP traffic. Test the external IP address of one or more instances. You might need to wait a minute for the instances to finish the startup process.

     1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

     2. Verify that each running instance has a green checkmark in the **Status** column next to the name of your instance group.

     3. Copy an instance's **External IP** and paste it into a web browser.

You should see the 'Apache2 Debian Default Page' web page.

If it doesn't seem to work, try waiting a few moments.




### gcloud

  1. Create a network for the instance groups.
         
         gcloud compute networks create fortressnet --subnet-mode auto
         

  2. Create a firewall rule for the network. This rule will allow all HTTP requests sent to your instances.
         
         gcloud compute firewall-rules create fortressnet-allow-http \
             --network fortressnet \
             --allow tcp:80
         

  3. Create an instance template. Include a startup script that starts up a simple Apache web server on each instance.
         
         gcloud compute instance-templates create fort-template \
             --machine-type e2-micro \
             --network fortressnet \
             --metadata startup-script='apt update && apt -y install apache2'
         

  4. Create multiple regional managed instance groups using the instance template. Configure autoscaling for each instance group.
         
         gcloud compute instance-groups managed create us-central1-pool \
             --region us-central1 \
             --template fort-template \
             --size 1
         gcloud compute instance-groups managed set-autoscaling us-central1-pool \
             --region us-central1 \
             --min-num-replicas 1 \
             --max-num-replicas 5 \
             --scale-based-on-load-balancing \
             --target-load-balancing-utilization .8
         
         
         gcloud compute instance-groups managed create europe-west1-pool \
             --region europe-west1 \
             --template fort-template \
             --size 1
         gcloud compute instance-groups managed set-autoscaling europe-west1-pool \
             --region europe-west1 \
             --min-num-replicas 1 \
             --max-num-replicas 5 \
             --scale-based-on-load-balancing \
             --target-load-balancing-utilization .8
         
         
         gcloud compute instance-groups managed create asia-east1-pool \
             --region asia-east1 \
             --template fort-template \
             --size 1
         gcloud compute instance-groups managed set-autoscaling asia-east1-pool \
             --region asia-east1 \
             --min-num-replicas 1 \
             --max-num-replicas 5 \
             --scale-based-on-load-balancing \
             --target-load-balancing-utilization .8
         

**Note:** **Autoscaling** of instance groups can be based on different criteria. Because your web service employs a **Load Balancer** , your autoscalers should be configured to scale based on **load balancing usage**. For more information, see [Scaling based on load balancing serving capacity](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-load-balancing).
  5. (Optional) Verify the instances are healthy and serving HTTP traffic. Test the external IP address of one or more instances. You might need to wait a minute for the instances to finish the startup process.

     1. List your instances. 
            
            gcloud compute instances list
            

     2. Verify under the `STATUS` column that the instances are `RUNNING`.

     3. Check an instance by querying it's IP address under the `EXTERNAL_IP` column. 
            
            curl http://EXTERNAL_IP | head
            

You should see some HTML text, including the line `<title>Apache2 Debian Default Page: It works</title>`.

If it doesn't seem to work, try waiting a few moments.




**Note:** You can create an autoscaler with multiple signals. So even though you need to scale based on **load balancing usage** to work with your **Load Balancer** , at the same time you can also autoscale based on CPU utilization, Cloud Monitoring metrics, or schedules. For more information, see [Using an autoscaling policy with multiple signals](https://docs.cloud.google.com/compute/docs/autoscaler/multiple-policies).

### Configure the load balancer

The load balancer will distribute client requests among your multiple backends.

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

  1. Set the **Load balancer name** as `fortressnet-balancer`.



#### Backend configuration

  1. On the **Create global external Application Load Balancer** page, click **Backend configuration**.
  2. In the **Create or select backend services & backend buckets** pull-down menu, select **Backend services** , then **Create a backend service**. You should see the **Create Backend Service** dialog box.
  3. Set the **Name** of the backend service to `fortressnet-backend-service`.
  4. Under the **New backend** dialog box, set **Instance group** to `asia-east1-pool`.
  5. For **Balancing mode** select **Rate**.
  6. Set **Maximum RPS** to `100` RPS per instance.
  7. Click **Done**.
  8. Click **Add backend**.
  9. Under the **New backend** dialog box, set **Instance group** to `europe-west1-pool`.
  10. For **Balancing mode** select **Rate**.
  11. Set **Maximum RPS** to `100` RPS per instance.
  12. Click **Done**.
  13. Click **Add backend**.
  14. Under the **New backend** dialog box, set **Instance group** to `us-central1-pool`.
  15. For **Balancing mode** select **Rate**.
  16. Set **Maximum RPS** to `100` RPS per instance.
  17. Click **Done**.
  18. Under **Health check** , select **Create a health check**.
  19. Set the **Name** to `http-basic-check`.
  20. For **Protocol** select `HTTP`.
  21. Set **Port** to `80`.
  22. Click **Save and continue**.
  23. Click **Create**.

**Note:** **Load balancing** of requests between backends can be based on different criteria. For more information see the documentation for the [Load distribution algorithm](https://docs.cloud.google.com/load-balancing/docs/https#load_distribution_algorithm).

#### Host and path rules

  1. On the left panel of the **Create global external Application Load Balancer** page, click **Host and path rules**.   
For this example, we don't need to configure any host or path rules since all traffic will go to the default rule. So, we can accept [the pre-populated default values](https://docs.cloud.google.com/load-balancing/docs/url-map#path-matchers).



#### Frontend configuration

  1. On the left panel of the **Create global external Application Load Balancer** page, click **Frontend configuration**.
  2. Set **Name** to `fortressnet-http-rule`.
  3. For **IP version** select **IPv4**.
  4. For **IP address** select **Create IP address**.
  5. In the **Reserve a new static IP** dialog box, set **Name** to `fortressnet-ip`.
  6. Click **Reserve** and wait a few moments.
  7. Click **Done** at the bottom of the **New Frontend IP and port** dialog box.
  8. Click **Add frontend IP and port**.
  9. Set **Name** to `fortressnet-http-ipv6-rule`.
  10. For **IP version** select **IPv6**.
  11. For **IP address** select **Create IP address**.
  12. In the dialog box, set **Name** to `fortressnet-ipv6`.
  13. Click **Reserve** and wait a few moments.
  14. Click **Done** at the bottom of the **New Frontend IP and port** dialog box.



#### Review and finalize

  1. On the left panel of the **Create global external Application Load Balancer** page, click **Review and finalize**.
  2. Compare your settings to what you intended to create.
  3. If the settings are correct, click **Create** at the bottom of the left panel. You are returned to the Load balancing screen. After the load balancer is created, a green check mark next to it indicates that it is running.



### gcloud

### Backend configuration

  1. Create a basic health check. This will check whether a load balancer backend is responding to HTTP requests.
         
         gcloud compute health-checks create http http-basic-check
         

  2. Create a global backend service. This backend service will receive HTTP traffic from the load balancer.
         
         gcloud compute backend-services create fortressnet-backend-service \
             --protocol HTTP \
             --health-checks http-basic-check \
             --global
         

  3. Add the instance groups as regional backends of the backend service. This configuration will distribute traffic among the backends based on a maximum number of requests per second (RPS) per instance.
         
         gcloud compute backend-services add-backend fortressnet-backend-service \
             --balancing-mode RATE \
             --max-rate-per-instance 100 \
             --instance-group us-central1-pool \
             --instance-group-region us-central1 \
             --global
         gcloud compute backend-services add-backend fortressnet-backend-service \
             --balancing-mode RATE \
             --max-rate-per-instance 100 \
             --instance-group europe-west1-pool \
             --instance-group-region europe-west1 \
             --global
         gcloud compute backend-services add-backend fortressnet-backend-service \
             --balancing-mode RATE \
             --max-rate-per-instance 100 \
             --instance-group asia-east1-pool \
             --instance-group-region asia-east1 \
             --global
         


**Note:** **Load balancing** of requests between backends can be based on different criteria. For more information see the documentation for the [Load distribution algorithm](https://docs.cloud.google.com/load-balancing/docs/https#load_distribution_algorithm).

### Host and path rules

  1. Define a URL map. URL maps route different URLs to different backend services. Since we only have one backend service, we'll simply set that backend service as the default service for all URLs.
         
         gcloud compute url-maps create fortressnet-balancer \
             --default-service fortressnet-backend-service
         

  2. Create an HTTP proxy route. HTTP proxy routes accept HTTP requests and route them according to your URL map. In this case, it will send all requests to your single backend service.
         
         gcloud compute target-http-proxies create fortressnet-http-proxy \
             --url-map fortressnet-balancer
         




### Frontend configuration

  1. Create two global static external IP addresses: one for IPv4 and one for IPv6. These will be the global external IP addresses of the load balancer.
         
         gcloud compute addresses create fortressnet-ip \
             --ip-version IPV4 \
             --network-tier=PREMIUM \
             --global
         gcloud compute addresses create fortressnet-ipv6 \
             --ip-version IPV6 \
             --network-tier=PREMIUM \
             --global
         

  2. Lookup the external IP addresses of the load balancer.
         
         gcloud compute addresses list
         

  3. Create global forwarding rules for the external IP addresses. This will forward both IPv4 and IPv6 HTTP requests to your HTTP proxy.
         
         gcloud compute forwarding-rules create fortressnet-http-rule \
             --load-balancing-scheme=EXTERNAL \
             --network-tier=PREMIUM \
             --global \
             --target-http-proxy fortressnet-http-proxy \
             --ports 80 \
             --address LOAD_BALANCER_IP_ADDRESS
         
         
         gcloud compute forwarding-rules create fortressnet-http-ipv6-rule \
             --load-balancing-scheme=EXTERNAL \
             --network-tier=PREMIUM \
             --global \
             --target-http-proxy fortressnet-http-proxy \
             --ports 80 \
             --address LOAD_BALANCER_IPV6_ADDRESS
         




**Note:** Notice that each backend now has a load balancer **balancing mode** and an instance group **autoscaler policy**. These two mechanisms work together to properly distribute load among the backends. For more information read the documentation for [Backend services and autoscaled managed instance groups](https://docs.cloud.google.com/load-balancing/docs/backend-service#backend_services_and_autoscaled_managed_instance_groups).

(Optional) Verify the load balancer is working. You may need to wait a minute or three.

### Console

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing)

  2. Wait for `fortressnet-balancer` to have a green check mark under the **Backends** column.

  3. Click on `fortressnet-balancer`.

  4. Under **Frontend** copy the IPv4 address under the **IP:Port** column. (IPv4 addresses are of the form `www.xxx.yyy.zzz`. You don't need the trailing port number `:nn`.) If the **Frontend** section is missing, try waiting a few moments and then reloading the web page.

  5. Enter the IP address in a web browser.




You should see the 'Apache2 Debian Default Page' web page.

If you get an 'Error 404 (Not Found)' web page instead, try waiting a few more minutes.

### gcloud

  1. Lookup the external IP addresses of the load balancer.
         
         gcloud compute addresses list
         

  2. Query the IPv4 address. (IPv4 addresses are of the form `www.xxx.yyy.zzz`.)
         
         curl http://LOAD_BALANCER_IP_ADDRESS | head
         




You should see some HTML text, including the line `<title>Apache2 Debian Default Page: It works</title>`.

If you see `<title>Error 404 (Not Found)!!1</title>` instead, try waiting a few more minutes.

Best Practice: Create a secure firewall to allow only internal traffic from the load balancer and the health check. Then delete the original firewall that allowed any HTTP request. This prevents individual instances from being accessible by outside clients.

### Console

  1. Create a new firewall only allowing traffic from the load balancer and the health check.

     1. In the Google Cloud console, go to the **Firewall rules** page.

[Go to Firewall rules](https://console.cloud.google.com/networking/firewalls)

     2. Click **Create Firewall Rule**.

     3. Set the **Name** to `fortressnet-allow-load-balancer`.

     4. For **Network** select `fortressnet`.

     5. For **Targets** select `All instances in the network`.

     6. For **Source IP ranges** type `130.211.0.0/22` and press the **Enter** key, then type `35.191.0.0/16` and press **Enter** again.

     7. Under **Protocols and ports** select **tcp** and enter `80`.

     8. Click **Create**.

  2. Delete the old allow-everything firewall.

     1. Select the checkmark next to `fortressnet-allow-http`.
     2. Click **Delete** at the top of the page.
     3. In the dialog box, click **Delete**.



### gcloud

  1. Create a new firewall only allowing traffic from the load balancer and the health check.
         
         gcloud compute firewall-rules create fortressnet-allow-load-balancer \
             --network fortressnet \
             --source-ranges 130.211.0.0/22,35.191.0.0/16 \
             --allow tcp:80
         

  2. Delete the old allow-everything firewall.
         
         gcloud compute firewall-rules delete fortressnet-allow-http -q
         




**Note:** `130.211.0.0/22` and `35.191.0.0/16` are noteworthy source IPs. `130.211.0.0/22` is the source IP for any request redirected by a Compute Engine **Load Balancer**. `35.191.0.0/16` is the source IP for any request sent by a Compute Engine **Health Check**. For more information, see the documentation for [Load balancing firewall rules](https://docs.cloud.google.com/load-balancing/docs/https#firewall_rules).

## (Optional) Verify that autoscaling and load balancing works

### Generate some test traffic

Suppose it is morning in Europe and your web service suddenly goes viral on the internet. Generate a high number of client requests all at once from Europe.

### Console

  1. Create an instance installed with the Siege load testing tool.

     1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

     2. Set the **Name** to `europe-loadtest`.

     3. For **Region** select `europe-west1`.

     4. For advanced settings, expand the **Advanced options** section, and do the following:

        1. Expand the **Management** section.
        2. In the **Automation** field, enter the following startup script: 
               
               apt -y install siege
               

     5. To create the VM, click **Create**.

  2. Get the IPv4 address of the load balancer.

     1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing)

     2. Click `fortressnet-balancer`.

     3. Under **Frontend** copy the IPv4 address under the **IP:Port** column. (IPv4 addresses are of the form `www.xxx.yyy.zzz`.)

  3. SSH into the load testing instance.

     1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

     2. Wait for the `europe-loadtest` instance to have a green checkmark under the **Name** column.

     3. Click **SSH** on `europe-loadtest` under the **Connect** column.

  4. Start siege. Target the IPv4 address of the load balancer.
         
         siege -c150 http://LOAD_BALANCER_IP_ADDRESS
         




### gcloud

  1. Create an instance installed with the Siege load testing tool.
         
         gcloud compute instances create europe-loadtest \
             --network default \
             --zone europe-west1-c \
             --metadata startup-script='apt -y install siege'
         

  2. Get the IPv4 address of the load balancer.
         
         gcloud compute addresses list
         

  3. Open a new shell session where the `gcloud` command is available.

**Note:** If you are using Cloud Shell, you can open multiple shell sessions in the same browser window. See the Cloud Shell documentation on [Opening Multiple Sessions](https://docs.cloud.google.com/shell/docs/starting-cloud-shell#opening_multiple_sessions).
     1. In your new shell session, SSH into the load testing instance.
            
            gcloud compute ssh --zone europe-west1-c europe-loadtest
            

     2. Start siege. Target the IPv4 address of the load balancer.
            
            siege -c150 http://LOAD_BALANCER_IP_ADDRESS
            




After running the `siege` command you should see output declaring `The server is now under siege...`
    
    
    [alert] Zip encoding disabled; siege requires zlib support to enable it
    ** SIEGE 4.0.2
    ** Preparing 150 concurrent users for battle.
    The server is now under siege...
    

### Monitor load balancing and autoscaling

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing)

  2. Click the load balancer named `fortressnet-balancer`.

  3. Click the **Monitoring** tab.

  4. In the **Backend** drop-down, select `fortressnet-backend-service`.




It may take up to ten minutes to display enough data. Soon you should see a display similar to the following:

![Google Cloud console monitoring display showing requests from Europe distributed equally among all three backends.](https://docs.cloud.google.com/static/compute/docs/tutorials/images/globally-autoscaling-compute-engine-loadtest-monitoring.png)

What's happening here:

  1. The load test starts sending a large amount of traffic all at once. At first, the load balancer distributes requests equally among the three backends. The number of requests quickly exceeds your autoscaling limits, and may even cause your servers to return `Backend 5xx errors` which will show up on the monitoring display. The autoscaler starts to spin up additional instances as needed.

  2. Autoscaling catches up with capacity needs. To minimize request latency, Compute Engine load balancers try to route requests to the backend that is closest to the client. In this case, since the load test traffic originates from Europe, the load balancer prefers to route more requests to the Europe backend. As a result, autoscaling may spin up more instances in the Europe backend to handle a higher fraction of requests.




### Generate test traffic somewhere else

Suppose your web service also catches on in Asia with the afternoon internet crowd. Generate a high number of requests from Asia.

### Console

  1. To create another instance installed with the Siege load testing tool, do the following:

     1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

     2. Click **Create instance**.

     3. Set the **Name** to `asia-loadtest`.

     4. For **Region** select `asia-east1`.

     5. Expand the **Advanced options** section.

     6. Expand the **Management** section.

     7. In the **Automation** section, enter the following startup script: 
            
            apt -y install siege
            

     8. Click **Create**.

  2. To get the IP address of the load balancer, do the following:

     1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing)

     2. Click `fortressnet-balancer`.

     3. Under **Frontend** copy the IPv4 address under the **IP:Port** column. (IPv4 addresses are of the form `www.xxx.yyy.zzz`.)

  3. SSH into the load testing instance.

     1. Wait for the `asia-loadtest` instance to have a green checkmark under the **Name** column.
     2. Click **SSH** on `asia-loadtest` under the **Connect** column.
  4. Start siege. Target the IPv4 address of the load balancer.
         
         siege -c150 http://LOAD_BALANCER_IP_ADDRESS
         




### gcloud

  1. In your original shell session, create another instance installed with the Siege load testing tool.
         
         gcloud compute instances create asia-loadtest \
             --network default \
             --zone asia-east1-c \
             --metadata startup-script='apt -y install siege'
         

  2. Get the IPv4 address of the load balancer.
         
         gcloud compute addresses list
         

  3. Open a new shell session where the `gcloud` command is available.

     1. In your new shell session, SSH into the load testing instance.
            
            gcloud compute ssh --zone asia-east1-c asia-loadtest
            

     2. Start siege. Target the IPv4 address of the load balancer.
            
            siege -c150 http://LOAD_BALANCER_IP_ADDRESS
            




Again, you should see output declaring `The server is now under siege...`
    
    
    [alert] Zip encoding disabled; siege requires zlib support to enable it
    ** SIEGE 4.0.2
    ** Preparing 150 concurrent users for battle.
    The server is now under siege...
    

### Monitor load balancing and autoscaling

Go back to the load balancing monitoring display from last time. It may take up to ten minutes to display enough new data. Soon you should see a display similar to the following:

![Google Cloud console monitoring display showing requests from Europe and Asia distributed among all three backends](https://docs.cloud.google.com/static/compute/docs/tutorials/images/globally-autoscaling-compute-engine-loadtest-monitoring2.png)

What's happening here:

  1. Again, the load test sends another large number of requests all at once. At first the load balancer distributes requests equally among the existing three backends. As the number of requests exceeds your autoscaling limits, the autoscaler starts to spin up additional instances as needed.

  2. Autoscaling catches up with the new capacity needs. The load balancer still prefers to route requests to the nearest available backends. As a result, eventually the Asia backend receives requests mostly from Asia, the Europe backend receives requests mostly from Europe, and the US backend receives everything else.




## Clean up

After you finish the tutorial, you can clean up the resources that you created so that they stop using quota and incurring charges. The following sections describe how to delete or turn off these resources. 

### Deleting the project

The easiest way to eliminate billing is to delete the project that you created for the tutorial. 

To delete the project: 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Deleting instances

To delete a Compute Engine instance: 

  1. In the Google Cloud console, go to the **VM instances** page. 

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select the checkbox for the instance that you want to delete. 
  3. To delete the instance, click more_vert **More actions** , click **Delete** , and then follow the instructions. 



## What's next

  * [Scaling based on load balancing serving capacity](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-load-balancing#scaling-based-on-https-load-balancing-serving-capacity).
  * [Global load balancing on Google Cloud](https://docs.cloud.google.com/load-balancing/docs/tutorials/about-capacity-optimization-with-global-lb).
  * [Building scalable and resilient web applications on Google Cloud](https://docs.cloud.google.com/solutions/scalable-and-resilient-apps).
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
