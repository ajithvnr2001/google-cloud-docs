---
url: https://docs.cloud.google.com/run/docs/configuring/shared-vpc-direct-vpc/
title: Direct VPC egress with a Shared VPC network \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:18.434353+00:00
---

# Direct VPC egress with a Shared VPC network  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/shared-vpc-direct-vpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Direct VPC egress with a Shared VPC network Stay organized with collections  Save and categorize content based on your preferences. 

You can enable your Cloud Run service or job to send traffic to a [Shared VPC network](https://docs.cloud.google.com/vpc/docs/shared-vpc#shared_vpc_networks) by using Direct VPC egress with no Serverless VPC Access connector required.

This page describes how to configure Cloud Run's IAM permissions to use the subnet of the Shared VPC network, and then place your service or job on the shared subnet.

## Before you begin

  * Review the following IP address configuration sections:

    * IP address allocation for guidance with allocating IP addresses from your subnet.

    * [IP address exhaustion strategies](https://docs.cloud.google.com/run/docs/configuring/networking-best-practices#alt-ip-address) for using alternative IP address ranges.




## Limitations

The following limitations apply to Cloud Run services, functions, jobs, worker pools, and instances: 

  * You might experience connection establishment delays of a minute or more on instance startup when using Direct VPC egress. We recommend configuring a [HTTP startup probe](https://docs.cloud.google.com/run/docs/configuring/healthchecks#healthcheck-endpoint) that tests a connection to an egress destination used by the application before the application accepts requests. This egress connectivity test should either implement retries or the startup probe should be set with appropriate period and threshold configurations to act as a retry.
  * Cloud Run jobs that run for more than 1 hour might experience connection breaks. These can occur during [maintenance events](https://docs.cloud.google.com/run/docs/configuring/task-timeout#observing_and_handling_maintenance_events) that migrate the job from one machine to another. The container receives a `SIGTSTP` signal 10 seconds before the event and a `SIGCONT` signal after the event. After the container receives the `SIGCONT` signal, retry the connection.
  * With Cloud NAT, you might experience cold start delays of 30s or more on instance startup when using Direct VPC egress. For better startup performance, we recommend using [Serverless VPC Access connectors](https://docs.cloud.google.com/run/docs/configuring/vpc-connectors) with Cloud NAT.
  * Cloud Run supports throughput of up to 1 Gbps per individual container instance. Exceeding this amount results in performance throttling.
  * A [Cloud Run usage quota](https://docs.cloud.google.com/run/quotas#cloud_run_limits) limits the maximum number of container instances you can configure to use Direct VPC egress. The maximum number is configured per Cloud Run revision or job execution. To increase the default limits, see [how to increase quotas.](https://docs.cloud.google.com/run/quotas#increase)

  * Cloud Run services, jobs, worker pools, and instances might experience connection breaks during networking infrastructure maintenance events. We recommend that you use client libraries that can handle occasional connection resets.
  * Network Intelligence Center supports only [Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview) and [Flow Analyzer](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/overview) for IPv4 and IPv6 subnet ranges.
  * Even though worker pools and Cloud Run instances support Direct VPC ingress, you can't use network tags to define the target of an ingress firewall rule.
  * Ingress to worker pools and Cloud Run instances are only supported using Direct VPC, not Serverless VPC Access connectors. Connectors don't support ingress.




The following items are not supported by Direct VPC egress:

  * VPC Flow Logs doesn't provide the name of the Cloud Run revision.
  * VPC firewall rules logging
  * Packet Mirroring
  * [Network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags) or [service identity](https://docs.cloud.google.com/run/docs/securing/service-identity) in ingress firewall rules.
  * Firewall rules cannot use Resource Manager tags attached to Cloud Run workloads.
  * Inspecting egress traffic with Cloud Next Generation Firewall Enterprise, such as intrusion detection and prevention service, URL filtering service, and TLS inspection.



## Set up IAM permissions

Before Cloud Run in a Shared VPC service project can access a Shared VPC network, you must first make sure the Cloud Run service agent has sufficient permissions to use the subnet.

  1. To access the Shared VPC network, grant sufficient permissions to the Cloud Run service agent by adding one of the following roles:

     * [Compute Network User (`roles/compute.networkUser`)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkUser) on the Shared VPC host project. Subnets with external IPv6 also require the [Compute Public IP Admin (`roles/compute.publicIpAdmin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.publicIpAdmin) role.

For example, to grant the Compute Network User role, run the following command:
           
           gcloud projects add-iam-policy-binding HOST_PROJECT_ID \
           --member "serviceAccount:service-SERVICE_PROJECT_NUMBER@serverless-robot-prod.iam.gserviceaccount.com" \
           --role "roles/compute.networkUser"

Replace the following:

       * HOST_PROJECT_ID: the ID of your Shared VPC host project.
       * SERVICE_PROJECT_NUMBER: the Shared VPC service project number where you deploy your Cloud Run service or job.
     * [Compute Network Viewer (`compute.networkViewer`)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkViewer) on the Shared VPC host project and the [Compute Network User (`compute.networkUser`)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkUser) role on the Shared VPC subnet. Subnets with external IPv6 also require the [Compute Public IP Admin (`roles/compute.publicIpAdmin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.publicIpAdmin) role.

For example, to grant the Compute Network User role on the subnet, run the following command:
           
           gcloud compute networks subnets add-iam-policy-binding SUBNET_NAME \
             --region REGION \
             --member "serviceAccount:service-SERVICE_PROJECT_NUMBER@serverless-robot-prod.iam.gserviceaccount.com" \
             --role "roles/compute.networkUser" \
             --project HOST_PROJECT_ID

Replace the following:

       * SUBNET_NAME: the fully qualified resource name of the subnet that you want to run your Cloud Run services.
       * REGION: the region for your Cloud Run service, which must match the region of your subnet.
       * SERVICE_PROJECT_NUMBER: the Shared VPC service project number where you deploy your Cloud Run service or job.
       * HOST_PROJECT_ID: the ID of your Shared VPC host project.
  2. The Cloud Run service agent requires the **Cloud Run Service Agent** role on your Cloud Run project. You can verify that the role was not manually removed by running the following command:
         
         gcloud projects get-iam-policy SERVICE_PROJECT_ID \
           --flatten bindings \
           --filter "bindings.role:roles/run.serviceAgent"

Replace SERVICE_PROJECT_ID with the project ID of your Cloud Run service or job.




For more granular control, you can ensure that the Cloud Run service agent has the following permissions:

  * `compute.networks.get` on the Shared VPC host project
  * `compute.subnetworks.get` on the host project or the specific subnet
  * `compute.subnetworks.use` on the host project or the specific subnet
  * `compute.addresses.get` on the Shared VPC service project
  * `compute.addresses.list` on the Shared VPC service project
  * `compute.addresses.create` on the Shared VPC service project (required only for [dual-stack subnets with external IPv6](https://docs.cloud.google.com/run/docs/configuring/vpc-dual-stack-subnet))
  * `compute.addresses.delete` on the Shared VPC service project (required only for dual-stack subnets with external IPv6)
  * `compute.addresses.createInternal` on the Shared VPC service project
  * `compute.addresses.deleteInternal` on the Shared VPC service project
  * `compute.regionOperations.get` on the Shared VPC service project



## IP address allocation

To place your Cloud Run service, job, worker pool, or instance on a VPC network, specify either a VPC network or a subnet, or both. If you specify only a network, the subnet uses the same name as the network. Cloud Run allocates IP addresses from your subnet.

IP addresses are ephemeral, so don't create policies based on individual IPs. If you need to create a policy based on IPs, such as in firewall rules, you must use the IP address range of the entire subnet.

To change the network or subnet that your Cloud Run resource uses, create a new deployment of your revision, job tasks, or instance that uses the new network and subnet values.

### Scale up and scale down

For faster scale up during a traffic surge, Cloud Run reserves IP addresses in blocks of 16 (`28` subnet mask) at a time. [See which IP addresses Cloud Run has allocated](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc#view-allocated). To ensure that you have enough IPv4 addresses available for use across Cloud Run, your subnet's IPv4 address range must be `/26` or larger.

For IP allocation efficiency and ease of management, place multiple resources on the same subnet. If your IPv4 address space is limited, see Supported IPv4 ranges for more options.

To delete the subnet, you must first delete or redeploy your Cloud Run services, jobs, worker pools, or instances to stop using the subnet, and then wait 1-2 hours.

### IP address consumption for services and worker pools

At steady state, Cloud Run uses 2 times (2X) as many IP addresses as the number of container instances. When a revision scales down, Cloud Run retains its IP addresses for up to 20 minutes. In total, reserve at least 2X the number of IP addresses, plus a buffer to account for revision updates.

For example, if you upgrade revisions so that `revision 1` scales from 100 container instances down to zero while `revision 2` scales from zero up to 100, Cloud Run retains the `revision 1` IP addresses for up to 20 minutes after scaling down. During the 20-minute retention window, you must reserve at least 400 IP addresses (`(100 + 100) * 2`).

### IP consumption for jobs

For Cloud Run jobs, each task consumes 1 IP address for the duration of its execution plus 7 minutes after it completes. Ensure that your subnet is large enough to accommodate all concurrent job task executions, with a minimum reservation `/26` subnet required.

For example:

  * A single-task job that runs daily and always completes at least 7 minutes before the next execution consumes a maximum of 1 IP address on the subnet.
  * A 10-task job running every 10 minutes, with each task running for 15 minutes, consumes 1 IP address for 22 minutes per task (3 executions consume IP addresses at the same time), as shown in the following example. The job therefore consumes 30 IP addresses at steady state. [ ![](https://docs.cloud.google.com/static/run/docs/images/ip-consumption.png)](https://docs.cloud.google.com/static/run/docs/images/ip-consumption.png)
  * A single-task job that takes 1 minute to run and executes 100 times per minute requires roughly 800 IP addresses depending on the exact time of execution.



### IP address consumption for Cloud Run instances

Each Cloud Run instance consumes four IP addresses on the subnet for as long as it is connected to the VPC network.

IP addresses are not static for any Cloud Run resource, even though Cloud Run instances are long lived. These IP address bindings don't persist across stops, restarts, or updates. When you stop, restart, or update an instance, a new private IP address is assigned to the instance.

### Supported IPv4 ranges

Cloud Run supports the following IPv4 ranges for your subnet:

  * [RFC 1918](https://tools.ietf.org/html/rfc1918#section-3)
    * `10.0.0.0/8`
    * `172.16.0.0/12`
    * `192.168.0.0/16`
  * [RFC 6598](https://tools.ietf.org/html/rfc6598#section-7)
    * `100.64.0.0/10`
  * Class E 
    * `240.0.0.0/4`

**Note:** Test non-RFC 1918 setups to identify possible compatibility issues with non-Google Cloud resources or hardware. Learn more about [creating subnets with non-RFC 1918 IP ranges](https://docs.cloud.google.com/vpc/docs/subnets#ipv4-ranges).

## Deploy a service

Direct VPC egress allows your Cloud Run service to send traffic to a Shared VPC network without a Serverless VPC Access connector. Network costs scale to zero just like the service itself. You can also [add network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags) directly on Cloud Run service revisions for more granular network security, such as applying [VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls).

You can configure Direct VPC egress with a service by using the Google Cloud console, Google Cloud CLI, or YAML.

### Console

  1. In the Google Cloud console, go to the Cloud Run page:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Select **Services** from the Cloud Run navigation menu, and click **Deploy container** to configure a new service. If you are configuring an existing service, click the service.

  3. If you are configuring a new service, fill out the initial service settings page as needed, then click **Containers, Networking, Security** to expand the service configuration page.

  4. Click the **Networking** tab.

  5. Click **Connect to a VPC for outbound traffic**.

  6. Click **Send traffic directly to a VPC**.

  7. Select **Networks shared with me**.

  8. In the **Network** field, select the Shared VPC network that you want to send traffic to.

  9. In the **Subnet** field, select the subnet where your service receives IP addresses from.

  10. Optional: Enter the names of the [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#restrictions) that you want to associate with your service or services. Network tags are specified at the revision-level. Each service revision can have different network tags, such as `network-tag-2`.

  11. For **Traffic routing** , select one of the following:

     * **Route only requests to private IPs to the VPC** to send only traffic to internal addresses through the Shared VPC network.
     * **Route all traffic to the VPC** to send all outbound traffic through the Shared VPC network.
  12. Click **Create** for a new service. Click **View diff & redeploy**, then **Deploy changes** for an existing service.

  13. To verify that your service is on your Shared VPC network, click the service, then click the **Networking** tab. The network and subnet are listed in the **VPC** card.




You can now send requests from your Cloud Run service to any resource on the Shared VPC network, as allowed by your firewall rules.

###  gcloud 

To place your service on the shared subnet, specify the fully qualified resource names for the Shared VPC network and subnet by running the following command:
    
    
    gcloud run deploy SERVICE_NAME \
      --image IMAGE_URL \
      --network projects/HOST_PROJECT_ID/global/networks/VPC_NETWORK \
      --subnet projects/HOST_PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME \
      --network-tags NETWORK_TAG_NAMES \
      --vpc-egress=EGRESS_SETTING \
      --region REGION \
      --max-instances MAX
      

Replace the following:

  * SERVICE_NAME: the name of your Cloud Run service.
  * IMAGE_URL: the image URL of the service.
  * HOST_PROJECT_ID: the ID of your Shared VPC project.
  * VPC_NETWORK: the fully qualified resource name of your Shared VPC network.
  * REGION: the region for your Cloud Run service, which must match the region of your subnet.
  * SUBNET_NAME: the fully qualified resource name of your subnet.
  * Optional: NETWORK_TAG_NAMES with the comma-separated names of the [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#restrictions) you want to associate with a service. For services, network tags are specified at the revision-level. Each service revision can have different network tags, such as `network-tag-2`.
  * EGRESS_SETTING with an [egress setting value](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--vpc-egress): 
    * `all-traffic`: Sends all outbound traffic through the Shared VPC network.
    * `private-ranges-only`: Sends only traffic to internal addresses through the Shared VPC network.
  * MAX: the maximum number of instances to use for the Shared VPC network. The maximum number of instances allowed for services is 100.



For more details and optional arguments, see the [`gcloud` reference](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy).

### YAML

  1. If you are creating a new service, skip this step. If you are updating an existing service, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run services describe SERVICE --format export > service.yaml

  2. Update the following attributes:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
           name: SERVICE_NAME
           labels:
             cloud.googleapis.com/location: REGION
         spec:
           template:
             metadata:
               annotations:
                 run.googleapis.com/network-interfaces: '[{"network":"NETWORK","subnetwork":"SUBNET","tags":"NETWORK_TAG_NAMES"}]'
                 run.googleapis.com/vpc-access-egress: EGRESS_SETTING
             spec:
               containers:
               - image: IMAGE

Replace:

     * SERVICE_NAME with the name of your Cloud Run service. Service names must be 49 characters or less and must be unique per region and project.
     * REGION with the region for your Cloud Run service, which must match the region of your subnet.
     * NETWORK with the fully qualified resource name of your Shared VPC network.
     * SUBNET_NAME with the fully qualified resource name of your subnet.
     * Optional: NETWORK_TAG_NAMES with the names of the [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#restrictions) you want to associate with a service. For services, network tags are specified at the revision-level. Each service revision can have different network tags, such as `network-tag-2`.
     * EGRESS_SETTING with an [egress setting value](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--vpc-egress): 
       * `all-traffic`: Sends all outbound traffic through the Shared VPC network.
       * `private-ranges-only`: Sends only traffic to internal addresses through the Shared VPC network.
     * IMAGE with the URL of your service container image.
  3. Create or update the service using the following command:
         
         gcloud run services replace service.yaml




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

  1. Add the following to your `main.tf` file:
         
         /**
          * Copyright 2024 Google LLC
          *
          * Licensed under the Apache License, Version 2.0 (the "License");
          * you may not use this file except in compliance with the License.
          * You may obtain a copy of the License at
          *
          *      http://www.apache.org/licenses/LICENSE-2.0
          *
          * Unless required by applicable law or agreed to in writing, software
          * distributed under the License is distributed on an "AS IS" BASIS,
          * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
          * See the License for the specific language governing permissions and
          * limitations under the License.
          */
         
         # Example configuration of a Cloud Run service with direct VPC
         
         resource "google_cloud_run_v2_service" "default" {
           name     = "cloudrun-service"
           location = "us-central1"
         
           deletion_protection = false # set to "true" in production
         
           template {
             containers {
               image = "us-docker.pkg.dev/cloudrun/container/hello"
             }
             vpc_access {
               network_interfaces {
                 network    = "default"
                 subnetwork = "default"
                 tags       = ["tag1", "tag2", "tag3"]
               }
             }
           }
         }
         




**Note:** Administrators can restrict the egress settings that developers can select by setting the [`run.allowedVPCEgress`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints#available_constraints) organization policy.

Optionally, [make your service public](https://docs.cloud.google.com/run/docs/authenticating/public) if you want to allow unauthenticated access to the service.

## Create a job

Direct VPC egress allows your Cloud Run job to send traffic to a Shared VPC network without a Serverless VPC Access connector. You can also [add network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags) directly on Cloud Run jobs for more granular network security, such as applying [VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls).

You can configure Direct VPC egress with a job by using the Google Cloud console, Google Cloud CLI, or YAML.

### Console

  1. In the Google Cloud console, go to the Cloud Run **Jobs** page:

[Go to Cloud Run](https://console.cloud.google.com/run/jobs)

  2. If you are configuring a new job, click **Deploy container** to fill out the initial **Create job** form as needed. If you are configuring an existing job, click the **Jobs** tab, select a job, then click **Edit**.

  3. Click **Container, Variables & Secrets, Connections, Security** to expand the job properties page.

  4. Click the **Connections** tab.

  5. Click **Connect to a VPC for outbound traffic**.

  6. Click **Send traffic directly to a VPC**.

  7. Select **Networks shared with me**.

  8. In the **Network** field, select the Shared VPC network that you want to send traffic to.

  9. In the **Subnet** field, select the subnet where your job receives IP addresses from.

  10. Optional: Enter the names of the [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#restrictions) that you want to associate with a job. For jobs, network tags are specified at the execution-level. Each job execution can have different network tags, such as `network-tag-2`.

  11. For **Traffic routing** , select one of the following:

     * **Route only requests to private IPs to the VPC** to send only traffic to internal addresses through the Shared VPC network.
     * **Route all traffic to the VPC** to send all outbound traffic through the Shared VPC network.
  12. Click **Create** or **Update**.

  13. To verify that your job is on your Shared VPC network, click the job, then click the **Configuration** tab. The network and subnet are listed in the **VPC** card.




You can now execute your Cloud Run job and send requests from the job to any resource on the Shared VPC network, as allowed by your firewall rules.

###  gcloud 

To place your job on the shared subnet, specify the fully qualified resource names for the Shared VPC network and subnet by running the following command:
    
    
    gcloud run jobs create JOB_NAME \
      --image IMAGE_URL \
      --network projects/HOST_PROJECT_ID/global/networks/VPC_NETWORK \
      --subnet projects/HOST_PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME \
      --network-tags NETWORK_TAG_NAMES \
      --vpc-egress=EGRESS_SETTING \
      --region REGION \
      

Replace the following:

  * JOB_NAME: the name of your Cloud Run job.
  * IMAGE_URL: the image URL of the job.
  * HOST_PROJECT_ID: the ID of your Shared VPC host project.
  * VPC_NETWORK: the fully qualified resource name of your Shared VPC network.
  * REGION: the region for your Cloud Run job, which must match the region of the subnet.
  * SUBNET_NAME: the fully qualified resource name of your name of your subnet.
  * Optional: NETWORK_TAG_NAMES with the comma-separated names of the [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#restrictions) you want to associate with a job. Each job execution can have different network tags, such as `network-tag-2`.
  * EGRESS_SETTING with an [egress setting value](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--vpc-egress): 
    * `all-traffic`: Sends all outbound traffic through the Shared VPC network.
    * `private-ranges-only`: Sends only traffic to internal addresses through the Shared VPC network.



For more details and optional arguments, see the [`gcloud` reference](https://docs.cloud.google.com/sdk/gcloud/reference/beta/run/deploy).

### YAML

  1. If you are creating a new job, skip this step. If you are updating an existing job, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1#job):
         
         gcloud run jobs describe JOB --format export > job.yaml

  2. Update the following attributes:
         
         apiVersion: run.googleapis.com/v1
         kind: Job
         metadata:
           name: JOB_NAME
           annotations:
             run.googleapis.com/launch-stage: BETA
           labels:
             cloud.googleapis.com/location: REGION
         spec:
           template:
             metadata:
               annotations:
                 run.googleapis.com/network-interfaces: '[{"network":"NETWORK","subnetwork":"SUBNET","tags":"NETWORK_TAG_NAMES"}]'
                 run.googleapis.com/vpc-access-egress: EGRESS_SETTING
             spec:
               containers:
               - image: IMAGE

Replace:

     * JOB_NAME with the name of your Cloud Run job. Job names must be 49 characters or less and must be unique per region and project.
     * REGION with the region for your Cloud Run job, which must match the region of your subnet.
     * NETWORK with the fully qualified resource name of your Shared VPC network.
     * SUBNET with the fully qualified resource name of your subnet.
     * Optional: NETWORK_TAG_NAMES with the names of the [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#restrictions) you want to associate with a job. For jobs, network tags are specified at the execution-level. Each job execution can have different network tags, such as `network-tag-2`.
     * EGRESS_SETTING with an [egress setting value](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--vpc-egress): 
       * `all-traffic`: Sends all outbound traffic through the Shared VPC network.
       * `private-ranges-only`: Sends only traffic to internal addresses through the Shared VPC network.
     * IMAGE with the URL of your job container image.
  3. Create or update the job using the following command:
         
         gcloud run jobs replace job.yaml




**Note:** Administrators can restrict the egress settings that developers can select by setting the [`run.allowedVPCEgress`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints#available_constraints) organization policy.

## Set up a dual-stack subnet

To add a dual-stack subnet with an IPv6 range on a Cloud Run resource, see [Set up a dual-stack subnet](https://docs.cloud.google.com/run/docs/configuring/vpc-dual-stack-subnet).

## Disconnect a service

### Console

  * To remove your service from the Shared VPC network:

    1. In the Google Cloud console, go to the Cloud Run **Services** page:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

    2. Click the service.

    3. Click the **Networking** tab.

    4. Clear the checkbox next to **Connect to a VPC for outbound traffic**.

    5. Click **View diff & redeploy**, then **Deploy changes**.

    6. To verify that your service is no longer on your Shared VPC network, click the **Networking** tab. The network and subnet are no longer listed in the **VPC** card.

  * To remove only the network tags while keeping the service connected to the Shared VPC network:

    1. Click the service that contains the network tags you want to remove.

    2. Click the **Networking** tab.

    3. Clear the names of the [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#restrictions) that you no longer want to associate with your service.

    4. Click **View diff & redeploy**, then **Deploy changes**.




###  gcloud 

  * To remove your service from the Shared VPC network, run the following command:
        
        gcloud run services update SERVICE_NAME --region=REGION \
        --clear-network

  * To remove only the network tags while keeping the service connected to the Shared VPC network, run the following command:
        
        gcloud run services update SERVICE_NAME --region=REGION \
        --clear-network-tags

Replace the following:

    * SERVICE_NAME: the name of your Cloud Run service.
    * REGION: the region for your Cloud Run service.



### YAML

  * To remove your service from the Shared VPC network:

    1. Download the service's [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
           
           gcloud run services describe SERVICE_NAME --format export > service.yaml

    2. Remove the following content from your `service.yaml` file:
           
           run.googleapis.com/network-interfaces: '[{"network":"NETWORK","subnetwork":"SUBNET","tags":"NETWORK_TAG_NAMES"}]'

Where

       * NETWORK: the fully qualified resource name of your Shared VPC network.
       * SUBNET: the fully qualified resource name of your subnet.
       * Optional: NETWORK_TAG_NAMES: the names of the network tags if you had associated them with a service.
    3. Update the service using the following command:
           
           gcloud run services replace service.yaml

  * To remove only the network tags while keeping the service connected to the Shared VPC network:

    1. Download the service's [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
           
           gcloud run services describe SERVICE_NAME --format export > service.yaml

    2. Remove the `tags` variable from the content in your `service.yaml` file, leaving the `network` and `subnetwork` variables in place, as shown in the following example:
           
           run.googleapis.com/network-interfaces: '[{"network":"NETWORK","subnetwork":"SUBNET"}]'

Replace the following:

       * NETWORK: the fully qualified resource name of your Shared VPC network.
       * SUBNET: the fully qualified resource name of your subnet.
    3. Update the service using the following command:
           
           gcloud run services replace service.yaml




## Disconnect a job

### Console

  * To remove your job from the Shared VPC network:

    1. In the Google Cloud console, go to the Cloud Run **Jobs** page:

[Go to Cloud Run](https://console.cloud.google.com/run/jobs)

    2. Click the job you want to remove, then click **Edit and deploy new revision**.

    3. Click the **Configuration** tab.

    4. Clear **Connect to a VPC for outbound traffic**.

    5. Click **Update**.

    6. To verify that your job is no longer on your Shared VPC network, click the **Configuration** tab. The network and subnet are no longer listed in the **VPC** card.

  * To remove only the network tags while keeping the job connected to the Shared VPC network:

    1. Click the job that contains the network tags you want to remove, then click **Edit and deploy new revision**.

    2. Click the **Connections** tab.

    3. Clear the names of the [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#restrictions) that you no longer want to associate with your job.

    4. Click **Update**.




###  gcloud 

  * To remove your job from the Shared VPC network, run the following command:
        
        gcloud run jobs update JOB_NAME --region=REGION \
          --clear-network
          

  * To remove only the network tags while keeping the job connected to the Shared VPC network, run the following command:
        
        gcloud run jobs update JOB_NAME --region=REGION \
          --clear-network-tags
          

Replace the following:

    * JOB_NAME: the name of your Cloud Run job.
    * REGION: the region for your Cloud Run job.



### YAML

  * To remove your job from the Shared VPC network:

    1. Download the job's [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1#job):
           
           gcloud run jobs describe JOB_NAME --format export > job.yaml

    2. Remove the following content from your `job.yaml` file:
           
           run.googleapis.com/network-interfaces: '[{"network":"NETWORK","subnetwork":"SUBNET","tags":"NETWORK_TAG_NAMES"}]'

Where

       * NETWORK: the fully qualified resource name of your Shared VPC network.
       * SUBNET: the fully qualified resource name of your subnet.
       * Optional: NETWORK_TAG_NAMES: the names of the network tags if you had associated them with a job.
    3. Update the job using the following command:
           
           gcloud run jobs replace job.yaml

  * To remove only the network tags while keeping the job connected to the Shared VPC network:

    1. Download the job's [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1#job):
           
           gcloud run jobs describe JOB_NAME --format export > job.yaml

    2. Remove the following content from your `job.yaml` file:
           
           run.googleapis.com/network-interfaces: '[{"network":"NETWORK","subnetwork":"SUBNET","tags":"NETWORK_TAG_NAMES"}]'

Where

       * NETWORK: the fully qualified resource name of your Shared VPC network.
       * SUBNET: the fully qualified resource name of your subnet.
       * Optional: NETWORK_TAG_NAMES: the names of the network tags if you had associated them with a job.
    3. Update the job using the following command:
           
           gcloud run jobs replace job.yaml




## Troubleshooting

### Cannot delete subnet

To delete a subnet, you must first delete all resources that use it. If Cloud Run is using a subnet, you must [disconnect Cloud Run](https://docs.cloud.google.com/run/docs/configuring/connecting-vpc#disconnect) from the Shared VPC network or move it to a different subnet before deleting the subnet.

**Note:** After you delete or move your Cloud Run resources, wait 1-2 hours for Cloud Run to release the IPs before you delete the subnet.

### Cannot detach Shared VPC network

To detach the Shared VPC network in the host project, follow the steps to [Deprovision Shared VPC](https://docs.cloud.google.com/vpc/docs/deprovisioning-shared-vpc) and be sure to disconnect any Cloud Run [services](https://docs.cloud.google.com/run/docs/configuring/connecting-vpc#disconnect) or [jobs](https://docs.cloud.google.com/run/docs/configuring/connecting-vpc#disconnect) from the Shared VPC network.

To see which Cloud Run resources are using the Shared VPC network, run the following command:
    
    
    gcloud compute shared-vpc list-associated-resources HOST_PROJECT_ID

Replace HOST_PROJECT_ID with the ID of your Shared VPC host project.

### Direct VPC egress subnet runs out of IPv4 addresses

The following error occurs when you try to deploy:
    
    
    Instance failed to start because of insufficient free IP addresses in the
    subnetwork SUBNET_ID when attempting to create an address in the
    subnetwork. Please consider moving to a subnetwork with more available IP
    addresses.

If the subnet of the VPC network runs out of IPv4 addresses, it is logged by Cloud Logging. When this occurs, Cloud Run cannot start any more service instances or job tasks until more IPv4 addresses become available.

To resolve this issue, follow the [IP address exhaustion strategies](https://docs.cloud.google.com/run/docs/configuring/networking-best-practices#alt-ip-address).

### View allocated IP addresses

To see which IP addresses Cloud Run has allocated, go to the [IP addresses page](https://console.cloud.google.com/networking/addresses) in the Google Cloud console or run the following command from the Google Cloud CLI:
    
    
    gcloud compute addresses list

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
