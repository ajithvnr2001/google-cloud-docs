---
url: https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc/
title: Direct VPC with a VPC network \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:15:47.590310+00:00
---

# Direct VPC with a VPC network  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Direct VPC with a VPC network Stay organized with collections  Save and categorize content based on your preferences. 

You can enable your Cloud Run service, function, job, worker pool, or instance to send traffic to a VPC network by using Direct VPC _egress_ with no Serverless VPC Access connector required.

Some resources, such as worker pools and instances, can also receive traffic from a VPC network by using Direct VPC _ingress_. 

Cloud Run supports the following Direct VPC configurations:

  * Services: Egress only
  * Jobs: Egress only
  * Worker pools: Egress and ingress
  * Instances: Egress and ingress



## Before you begin

  * If you don't already have a VPC network in your project, [create one](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks).

  * If you use Shared VPC with Cloud Run services or jobs, see [Connecting to a Shared VPC network](https://docs.cloud.google.com/run/docs/configuring/connecting-shared-vpc).

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

## Set up IAM permissions

Ensure that Cloud Run has access to the VPC network by using one of the following methods:

  * **Cloud Run Service Agent role** : By default, the Cloud Run service agent has the [Cloud Run Service Agent role (`roles/run.serviceAgent`)](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.serviceAgent) that contains the necessary permissions.

  * **Custom permissions** : For more granular control, grant the Cloud Run service agent with the following additional permissions on the project:

    * `compute.networks.get`
    * `compute.subnetworks.get`
    * `compute.subnetworks.use` on the project or the specific subnet
    * `compute.addresses.get`
    * `compute.addresses.list`
    * `compute.addresses.create` (required only for [dual-stack subnets with external IPv6](https://docs.cloud.google.com/run/docs/configuring/vpc-dual-stack-subnet))
    * `compute.addresses.delete` (required only for dual-stack subnets with external IPv6)
    * `compute.addresses.createInternal`
    * `compute.addresses.deleteInternal`
    * `compute.regionOperations.get`
  * **Compute Network User role** : If you don't use the default Cloud Run Service Agent role or the custom permissions, grant the [Compute Network User role (`roles/compute.networkUser`)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkUser) on the Cloud Run Service Agent service account. Subnets with external IPv6 also require the [Compute Public IP Admin role (`roles/compute.publicIpAdmin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.publicIpAdmin).

For example, to grant the Compute Network User role, run the following command:
        
        gcloud projects add-iam-policy-binding PROJECT_ID \
        --member "serviceAccount:service-PROJECT_NUMBER@serverless-robot-prod.iam.gserviceaccount.com" \
        --role "roles/compute.networkUser"

Replace the following:

    * PROJECT_ID: the ID of your project.
    * PROJECT_NUMBER: the project number where you deploy your Cloud Run resource.



## Connect Cloud Run resources to a VPC network

Depending on the Cloud Run resource that you have, see the instructions in one of the following sections:

  * Deploy a service
  * Create a job
  * Deploy a worker pool
  * Deploy an instance



### Connect a service to a VPC network

Direct VPC egress allows your Cloud Run service to send traffic to a VPC network without a Serverless VPC Access connector. Network costs scale to zero just like the service itself. You can also [add network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags) directly on Cloud Run service revisions for more granular network security, such as applying [VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls).

You can configure Direct VPC egress with a service by using the Google Cloud console, Google Cloud CLI, YAML, or Terraform.

### Console

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Click **Create Service** if you are configuring a new service you are deploying to. If you are configuring and deploying an existing service, click the service.

  3. If you are configuring a new service, fill out the initial service settings page as needed, then click **Containers, Networking, Security** to expand the service configuration page.

  4. Click the **Networking** tab.

  5. Click **Connect to a VPC for outbound traffic**.

  6. Click **Send traffic directly to a VPC**.

  7. In the **Network** field, select the VPC network that you want to send traffic to.

  8. In the **Subnet** field, select the subnet where your service receives IP addresses from. You can deploy multiple services on the same subnet.

  9. Optional: Enter the names of the [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#restrictions) that you want to associate with your service or services. Network tags are specified at the revision-level. Each service revision can have different network tags, such as `network-tag-2`.

  10. For **Traffic routing** , select one of the following:

     * **Route only requests to private IPs to the VPC** to send only traffic to internal addresses through the VPC network.
     * **Route all traffic to the VPC** to send all outbound traffic through the VPC network.
  11. Click **Create** for a new service. Click **View diff & redeploy**, then **Deploy changes** for an existing service.

  12. To verify that your service is on your VPC network, click the service, then click the **Networking** tab. The network and subnet are listed in the **VPC** card.

You can now send requests from your Cloud Run service to any resource on the VPC network, as allowed by your firewall rules.




### gcloud

### Service

To deploy a Cloud Run service without a connector from the Google Cloud CLI:

  1. Update `gcloud` components to the latest version:
         
         gcloud components update

  2. Ensure that the Compute Engine API is enabled for your project:
         
         gcloud services enable compute.googleapis.com
         

  3. Deploy your Cloud Run service with the following command:
         
         gcloud run deploy SERVICE_NAME \
             --image=IMAGE_URL \
             --network=NETWORK \
             --subnet=SUBNET \
             --network-tags=NETWORK_TAG_NAMES \
             --vpc-egress=EGRESS_SETTING \
             --region=REGION

Replace:

     * SERVICE_NAME with the name of your Cloud Run service.
     * `IMAGE_URLus-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG`
     * NETWORK with the name of your VPC network. Specify either a VPC network or a subnet, or both. If you specify only a network, the subnet uses the same name as the network.
     * SUBNET with the name of your subnet. Specify either a VPC network or a subnet, or both. If you specify only a network, the subnet uses the same name as the network. You can deploy or execute multiple services, jobs, worker pools, or instances on the same subnet. 
     * Optional: NETWORK_TAG_NAMES with the comma-separated names of the [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#restrictions) you want to associate with a service. For services, network tags are specified at the revision-level. Each service revision can have different network tags, such as `network-tag-2`.
     * EGRESS_SETTING with an [egress setting value](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--vpc-egress): 
       * `all-traffic`: Sends all outbound traffic through the VPC network.
       * `private-ranges-only`: Sends only traffic to internal addresses through the VPC network.
     * REGION with a region for your service.
  4. To verify that your service is on your VPC network, run the following command:
         
         gcloud run services describe SERVICE_NAME \
             --region=REGION

Replace:

     * `SERVICE_NAME` with the name of your service.
     * `REGION` with the region for your service that you specified in the previous step.

The output should contain the name of your network, subnet, and egress setting, for example:
    
    VPC access:
      Network:       default
      Subnet:        subnet
      Egress:        private-ranges-only
    




You can now send requests from your Cloud Run service to any resource on the VPC network, as allowed by your firewall rules.

### Function

To deploy a Cloud Run function without a connector from the Google Cloud CLI:

  1. Update `gcloud` components to the latest version:
         
         gcloud components update

  2. Ensure that the Compute Engine API is enabled for your project:
         
         gcloud services enable compute.googleapis.com
         

  3. Deploy your Cloud Run function with the following command:
         
         gcloud run deploy FUNCTION_NAME \
             --image=IMAGE_URL \
             --network=NETWORK \
             --subnet=SUBNET \
             --network-tags=NETWORK_TAG_NAMES \
             --vpc-egress=EGRESS_SETTING \
             --region=REGION \
             --function=FUNCTION_ENTRYPOINT

Replace:

     * FUNCTION_NAME with the name of your Cloud Run function.
     * `IMAGE_URLus-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG`
     * NETWORK with the name of your VPC network. Specify either a VPC network or a subnet, or both. If you specify only a network, the subnet uses the same name as the network.
     * SUBNET with the name of your subnet. Specify either a VPC network or a subnet, or both. If you specify only a network, the subnet uses the same name as the network. You can deploy or execute multiple services, jobs, worker pools, or instances on the same subnet. 
     * Optional: NETWORK_TAG_NAMES with the comma-separated names of the [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#restrictions) you want to associate with a function. For functions, network tags are specified at the revision-level. Each revision can have different network tags, such as `network-tag-2`.
     * EGRESS_SETTING with an [egress setting value](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--vpc-egress): 
       * `all-traffic`: Sends all outbound traffic through the VPC network.
       * `private-ranges-only`: Sends only traffic to internal addresses through the VPC network.
     * REGION with a region for your function.
     * Optional: FUNCTION_ENTRYPOINT with the entry point to your function in your source code. This is the code Cloud Run executes when your function runs. The value of this flag must be a function name or fully qualified class name that exists in your source code.
  4. To verify that your function is on your VPC network, run the following command:
         
         gcloud run services describe FUNCTION_NAME \
             --region=REGION

Replace:

     * `FUNCTION_NAME` with the name of your function.
     * `REGION` with the region for your function that you specified in the previous step.

The output should contain the name of your network, subnet, and egress setting, for example:
    
    VPC access:
      Network:       default
      Subnet:        subnet
      Egress:        private-ranges-only
    




You can now send requests from your Cloud Run function to any resource on the VPC network, as allowed by your firewall rules.

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
     * NETWORK with the name of your VPC network. Specify either a VPC network or a subnet, or both. If you specify only a network, the subnet uses the same name as the network.
     * SUBNET with the name of your subnet. Specify either a VPC network or a subnet, or both. If you specify only a network, the subnet uses the same name as the network. You can deploy or execute multiple services, jobs, worker pools, or instances on the same subnet. 
     * Optional: NETWORK_TAG_NAMES with the names of the [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#restrictions) you want to associate with a service. For services, network tags are specified at the revision-level. Each service revision can have different network tags, such as `network-tag-2`.
     * EGRESS_SETTING with an [egress setting value](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--vpc-egress): 
       * `all-traffic`: Sends all outbound traffic through the VPC network.
       * `private-ranges-only`: Sends only traffic to internal addresses through the VPC network.
     * IMAGE with the URL of your service container image.

You can also [specify more configuration](https://docs.cloud.google.com/run/docs/how-to#configure), such as environment variables or memory limits.

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

### Connect a job to a VPC network

Direct VPC egress allows your Cloud Run job to send traffic to a VPC network without a Serverless VPC Access connector. You can also [add network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags) directly on Cloud Run jobs for more granular network security, such as applying [VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls).

You can configure Direct VPC egress with a job by using the Google Cloud console, Google Cloud CLI, or YAML.

### Console

  1. [Go to Cloud Run](https://console.cloud.google.com/run)

  2. If you are configuring a new job, click the **Jobs** tab and fill out the initial job settings page as needed. If you are configuring an existing job, click the job, then click **Edit**.

  3. Click **Container, Variables & Secrets, Connections, Security** to expand the job properties page.

  4. Click the **Connections** tab.

  5. Click **Connect to a VPC for outbound traffic**.

  6. Click **Send traffic directly to a VPC**.

  7. In the **Network** field, select the VPC network that you want to send traffic to.

  8. In the **Subnet** field, select the subnet where your job receives IP addresses from. You can execute multiple jobs on the same subnet.

  9. For **Traffic routing** , select one of the following:

     * **Route only requests to private IPs to the VPC** to send only traffic to internal addresses through the VPC network.
     * **Route all traffic to the VPC** to send all outbound traffic through the VPC network.
  10. Optional: Enter the names of the [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#restrictions) that you want to associate with your service or services. Network tags are specified at the revision-level. Each service revision can have different network tags, such as `network-tag-2`.

  11. Optional: Enter the names of the [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#restrictions) that you want to associate with your job or jobs. For jobs, network tags are specified at the execution level. Each job execution can have different network tags, such as `network-tag-2`.

  12. Click **Create** or **Update**.

  13. To verify that your job is on your VPC network, click the job, then click the **Configuration** tab. The network and subnet are listed in the **VPC** card.

You can now execute your Cloud Run job and send requests from the job to any resource on the VPC network, as allowed by your firewall rules.




### gcloud

To create a Cloud Run job without a connector from the Google Cloud CLI:

  1. Update `gcloud` components to the latest version:
         
         gcloud components update

  2. Ensure that the Compute Engine API is enabled for your project:
         
         gcloud services enable compute.googleapis.com
         

  3. Create a Cloud Run job with the following command:
         
         gcloud run jobs create JOB_NAME \
         --image=IMAGE_URL \
         --network=NETWORK \
         --subnet=SUBNET \
         --network-tags=NETWORK_TAG_NAMES \
         --vpc-egress=EGRESS_SETTING \
         --region=REGION

Replace:

     * JOB_NAME with the name of your Cloud Run job.
     * `IMAGE_URL`: a reference to the [container image](https://docs.cloud.google.com/run/docs/building/containers)—for example, `us-docker.pkg.dev/cloudrun/container/job:latest`
     * NETWORK with the name of your VPC network. Specify either a VPC network or a subnet, or both. If you specify only a network, the subnet uses the same name as the network.
     * SUBNET with the name of your subnet. Specify either a VPC network or a subnet, or both. If you specify only a network, the subnet uses the same name as the network. You can deploy or execute multiple services, jobs, worker pools, or instances on the same subnet. 
     * Optional: NETWORK_TAG_NAMES with the names of the [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#restrictions) you want to associate with a job. For jobs, network tags are specified at the execution-level. Each job execution can have different network tags, such as `network-tag-2`.
     * EGRESS_SETTING with an [egress setting value](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--vpc-egress): 
       * `all-traffic`: Sends all outbound traffic through the VPC network.
       * `private-ranges-only`: Sends only traffic to internal addresses through the VPC network.
     * REGION with a region for your job.
  4. To verify that the job is on your VPC network, run the following command:
         
         gcloud run jobs describe JOB_NAME \
           --region=REGION
           

Replace:

     * `JOB_NAME` with the name of your job.
     * `REGION` with the region for your job that you specified in the previous step.

The output should contain the name of your network and subnet, for example:
    
    VPC network:
      Network:       default
      Subnet:        default
    




You can now execute your Cloud Run job and send requests from the job to any resource on the VPC network, as allowed by your firewall rules.

### YAML

  1. If you are creating a new job, skip this step. If you are updating an existing job, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1#job):
         
         gcloud run jobs describe JOB --format export > job.yaml

  2. Update the following attributes:
         
         apiVersion: run.googleapis.com/v1
           kind: Job
           metadata:
             name: JOB_NAME
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
     * NETWORK with the name of your VPC network. Specify either a VPC network or a subnet, or both. If you specify only a network, the subnet uses the same name as the network.
     * SUBNET with the name of your subnet. Specify either a VPC network or a subnet, or both. If you specify only a network, the subnet uses the same name as the network. You can deploy or execute multiple services, jobs, worker pools, or instances on the same subnet. 
     * Optional: NETWORK_TAG_NAMES with the names of the [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#restrictions) you want to associate with a job. For jobs, network tags are specified at the execution-level. Each job execution can have different network tags, such as `network-tag-2`.
     * EGRESS_SETTING with an [egress setting value](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--vpc-egress): 
       * `all-traffic`: Sends all outbound traffic through the VPC network.
       * `private-ranges-only`: Sends only traffic to internal addresses through the VPC network.
     * IMAGE with the URL of your job container image.
  3. Create or update the job using the following command:
         
         gcloud run jobs replace job.yaml




**Note:** Administrators can restrict the egress settings that developers can select by setting the [`run.allowedVPCEgress`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints#available_constraints) organization policy.

### Connect a worker pool to a VPC network

Direct VPC allows your Cloud Run worker pool to send or receive traffic to or from a VPC. Each worker pool instance receives a private IP address on the configured network and subnet.

Contrary to services or jobs, Direct VPC connectivity for worker pools allows egress and ingress. This means that worker pool instances can reach resources on the VPC network, and resources on the VPC network can also reach a worker pool instance using its IP address. See how an instance can [retrieve its private IP addresses using the metadata server](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc#mds-support).

You can also [add network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags) directly on Cloud Run worker pool revisions with Direct VPC egress for more granular network security, such as applying [VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls).

You can configure Direct VPC egress by using the Google Cloud console, the Google Cloud CLI, or YAML.

### Console

  1. [Go to Cloud Run](https://console.cloud.google.com/run)

  2. Select **Worker pools** from the menu, and click **Deploy container** to configure a new worker pool. If you are configuring an existing worker pool, click the worker pool, then click **Edit and deploy new revision**.

  3. If you are configuring a new worker pool, fill out the initial worker pool page, then click **Container(s), Volumes, Networking, Security** to expand the worker pools configuration page.

  4. Click the **Networking** tab.

  5. Select **Connect to a VPC**.

  6. Click **Create** or **Deploy**.

You can now send requests from your Cloud Run worker pool to any resource on the VPC network, as allowed by your firewall rules.




### gcloud

To deploy a Cloud Run worker pool without a connector from the Google Cloud CLI:

  1. Update `gcloud` components to the latest version:
         
         gcloud components update

  2. Ensure that the Compute Engine API is enabled for your project:
         
         gcloud services enable compute.googleapis.com
         

  3. Deploy your Cloud Run worker pool with the following command:

     * For Direct VPC egress:
    
    gcloud run worker-pools deploy WORKER_POOL \
        --image=IMAGE_URL \
        --network=NETWORK \
        --subnet=SUBNET \
        --network-tags=NETWORK_TAG_NAMES \
        --region=REGION

     * For Direct VPC ingress:
    
    gcloud run worker-pools deploy WORKER_POOL \
        --image=IMAGE_URL \
        --network=NETWORK \
        --subnet=SUBNET \
        --region=REGION

Replace:

     * `WORKER_POOL` with the name of your Cloud Run worker pool. Worker pool names must be 49 characters or less, use a unique name per region and project, and must not share the same name as an existing service name from your project. If the worker pool does not exist yet, this command creates the worker pool during the deployment. You can omit this parameter entirely, but you will be prompted for the worker pool name if you omit it.
     * `IMAGE_URL`: a reference to the container image that contains the worker pool, such as `us-docker.pkg.dev/cloudrun/container/worker-pool:latest`
     * `NETWORK` with the name of your VPC network. Specify either a VPC network or a subnet, or both. If you specify only a network, the subnet uses the same name as the network.
     * SUBNET with the name of your subnet. Specify either a VPC network or a subnet, or both. If you specify only a network, the subnet uses the same name as the network. You can deploy or execute multiple services, jobs, worker pools, or instances on the same subnet. 
     * Optional (Direct VPC egress only): `NETWORK_TAG_NAMES` with the comma-separated names of the [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#restrictions) you want to associate with a worker pool. For services, network tags are specified at the revision-level. Each worker pool revision can have different network tags, such as `network-tag-2`.
     * `REGION` with a region for your worker pool.
  4. To verify that your worker pool is on your VPC network, run the following command:
         
         gcloud run worker-pools describe WORKER_POOL \
             --region=REGION

Replace:

     * `WORKER_POOL` with the name of your worker pool.
     * `REGION` with the region for your worker pool that you specified in the previous step.

The output should contain the name of your network, subnet, and egress setting, for example:
    
    VPC access:
      Network:       default
      Subnet:        subnet
      Egress:        private-ranges-only
    




You can now send requests from your Cloud Run worker pool to any resource on the VPC network, as allowed by your firewall rules.

### YAML

  1. If you are creating a new worker pool, skip this step. If you are updating an existing worker pool, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run worker-pools describe WORKER_POOL --format export > worker-pool.yaml

  2. Update the following attributes:
         
         apiVersion: run.googleapis.com/v1
           kind: WorkerPool
           metadata:
             name: WORKER_POOL
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
                 - image: IMAGE_URL

**Note:** For Direct VPC ingress, remove the `run.googleapis.com/vpc-access-egress` and the `tags` attributes.

Replace the following:

     * WORKER_POOL: the name of your Cloud Run worker pool.
     * REGION: the region for your Cloud Run worker pool, which must match the region of your subnet.
     * NETWORK: the name of your VPC network. Specify either a VPC network or a subnet, or both. If you specify only a network, the subnet uses the same name as the network.
     * SUBNET with the name of your subnet. Specify either a VPC network or a subnet, or both. If you specify only a network, the subnet uses the same name as the network. You can deploy or execute multiple services, jobs, worker pools, or instances on the same subnet. 
     * Optional (Direct VPC egress only): NETWORK_TAG_NAMES: the names of the [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#restrictions) you want to associate with the worker pool. For worker pools, network tags are specified at the revision-level. Each worker pool revision can have different network tags, such as `network-tag-2`.
     * EGRESS_SETTING: an [egress setting value](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--vpc-egress). 
       * `all-traffic`: Sends all outbound traffic through the VPC network.
       * `private-ranges-only`: Sends only traffic to internal addresses through the VPC network.
     * `IMAGE_URL`: a reference to the container image that contains the worker pool, such as `us-docker.pkg.dev/cloudrun/container/worker-pool:latest`.

You can also [specify more configuration](https://docs.cloud.google.com/run/docs/how-to#configure), such as environment variables or memory limits.

  3. Create or update the worker pool using the following command:
         
         gcloud run worker-pools replace worker-pool.yaml

The `gcloud run worker-pools replace` command defaults to using `worker-pool.yaml` file if present.




**Note:** Administrators can restrict the egress settings that developers can select by setting the [`run.allowedVPCEgress`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints#available_constraints) organization policy.

### Connect an instance to a VPC network

Direct VPC allows your Cloud Run instance to send or receive traffic to or from a VPC network. Each instance receives a private IP address on the configured network and subnet.

Unlike to services or jobs, Direct VPC connectivity for instances allows both egress and ingress. This means that instances can reach resources on the VPC network, and resources on the VPC network can also reach an instance using its private IP address. See how an instance can retrieve its private IP addresses using the metadata server.

You can also [add network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags) directly on Cloud Run instances with Direct VPC egress for more granular network security, such as applying [VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls).

You can configure Direct VPC for an instance by using the Google Cloud CLI or YAML:

###  gcloud 

To deploy a Cloud Run instance with Direct VPC from the Google Cloud CLI:

  1. Update `gcloud` components to the latest version:
         
         gcloud components update

  2. Ensure that the Compute Engine API is enabled for your project:
         
         gcloud services enable compute.googleapis.com
         

  3. Deploy your Cloud Run instance with the following command:

     * For Direct VPC egress:
    
    gcloud beta run instances deploy INSTANCE_NAME \
        --image=IMAGE_URL \
        --network=NETWORK \
        --subnet=SUBNET \
        --network-tags=NETWORK_TAG_NAMES \
        --region=REGION

     * For Direct VPC ingress:
    
    gcloud beta run instances deploy INSTANCE_NAME \
        --image=IMAGE_URL \
        --network=NETWORK \
        --subnet=SUBNET \
        --region=REGION

Replace the following:

     * `INSTANCE_NAME`: the name of your Cloud Run instance.
     * `IMAGE_URL`: a reference to the container image, such as `us-docker.pkg.dev/cloudrun/container/hello:latest`.
     * `NETWORK`: the name of your VPC network. Specify either a VPC network or a subnet, or both. If you specify only a network, the subnet uses the same name as the network.
     * SUBNET with the name of your subnet. Specify either a VPC network or a subnet, or both. If you specify only a network, the subnet uses the same name as the network. You can deploy or execute multiple services, jobs, worker pools, or instances on the same subnet. 
     * Optional (Direct VPC egress only): `NETWORK_TAG_NAMES`: the comma-separated names of the [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#restrictions) you want to associate with the instance.
     * `REGION`: the region for your instance.
  4. To verify that your instance is on your VPC network, run the following command:
         
         gcloud beta run instances describe INSTANCE_NAME \
             --region=REGION




### YAML

  1. If you are creating a new instance, skip this step. If you are updating an existing instance, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud beta run instances describe INSTANCE --format export > instance.yaml

  2. Update the `run.googleapis.com/network-interfaces` and `run.googleapis.com/vpc-access-egress` annotations under `metadata.annotations`:
         
         apiVersion: run.googleapis.com/v1
         kind: Instance
         metadata:
           name: INSTANCE_NAME
           labels:
             cloud.googleapis.com/location: REGION
           annotations:
             run.googleapis.com/launch-stage: BETA
             run.googleapis.com/network-interfaces: '[{"network":"NETWORK","subnetwork":"SUBNET","tags":["NETWORK_TAG_NAMES"]}]'
             run.googleapis.com/vpc-access-egress: 'EGRESS_SETTING'
         spec:
           containers:
           - image: IMAGE_URL

**Note:** For Direct VPC ingress only, remove the `run.googleapis.com/vpc-access-egress` annotation and the `tags` attribute.
  3. Create or update the instance using the following command:
         
         gcloud beta run instances replace instance.yaml




**Note:** Administrators can restrict the egress settings that developers can select by setting the [`run.allowedVPCEgress`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints#available_constraints) organization policy.

### Retrieve private IP addresses using the metadata server

**Note:** Direct VPC IP addresses (both ingress and egress) are **ephemeral** and are not static for any Cloud Run resource.

You can access private IP addresses between instances in your VPC network for secure internal communication. To retrieve a worker pool instance's or Cloud Run instance's private IP address from the [metadata server](https://docs.cloud.google.com/run/docs/container-contract#metadata-server), run the following commands inside your container:

  * To get the IPv4 address, send a request to the metadata server at the `/computeMetadata/v1/instance/network-interfaces/0/ip` endpoint:
        
        curl "http://metadata.google.internal/computeMetadata/v1/instance/network-interfaces/0/ip" -H "Metadata-Flavor: Google"
        

  * To get the IPv6 address, create your instance with a [dual-stack subnet](https://docs.cloud.google.com/run/docs/configuring/vpc-dual-stack-subnet), and send a request to the metadata server at the `/computeMetadata/v1/instance/network-interfaces/0/ipv6` endpoint:
        
        curl "http://metadata.google.internal/computeMetadata/v1/instance/network-interfaces/0/ipv6" -H "Metadata-Flavor: Google"
        

  * To verify that your worker pool instance or Cloud Run instance is attached to a VPC network, query the following network interface metadata paths:
        
        # Verify the existence of the network interface directory
        
        curl "http://metadata.google.internal/computeMetadata/v1/instance/network-interfaces/" -H "Metadata-Flavor: Google"
        
        # Verify the existence of the first network interface
        
        curl "http://metadata.google.internal/computeMetadata/v1/instance/network-interfaces/0/" -H "Metadata-Flavor: Google"
        




### Handle metadata server errors

The metadata server returns a `404: Not Found` error in the following scenarios:

  * If you query for an IPv6 address on an IPv4-only subnet.
  * If you don't connect your worker pool instance or Cloud Run instance to a VPC network. In this case, the metadata server returns an error for the following paths:

    * `/computeMetadata/v1/instance/network-interfaces`
    * `/computeMetadata/v1/instance/network-interfaces/0`
    * `/computeMetadata/v1/instance/network-interfaces/0/ip`
    * `/computeMetadata/v1/instance/network-interfaces/0/ipv6`



## Set up dual-stack (IPv4 and IPv6)

To add a dual-stack subnet with an IPv6 range on a Cloud Run resource, see [Set up dual-stack](https://docs.cloud.google.com/run/docs/configuring/vpc-dual-stack-subnet).

## Restrict access with firewall rules

Restrict access to resources in a VPC network by using [VPC firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls). Add these restrictions by using one of the following strategies:

  * Create an ingress firewall rule that refers to your [service](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc#direct-vpc-service) or [job](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc#direct-vpc-job) by using the subnet's IP range.
  * Create an egress firewall rule that refers to your [service](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc#direct-vpc-service) or [job](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc#direct-vpc-job).

In the egress firewall rule, refer to your service or job by using the linked service account [service identity](https://docs.cloud.google.com/run/docs/securing/service-identity), the subnet's IP range, or the associated network tags.




### Network tags for egress

Add an additional layer of network security by using network tags in egress firewall rules.

### Console

To associate [network tags](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access#network-tags) with a service or job:

  1. In the Google Cloud console, go to the **Cloud Run** page.

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Click the service or job you want to associate network tags with, then click **Edit** for jobs.

  3. Click the **Networking** tab for services, or the **Connections** tab for jobs.

  4. Ensure that you have selected **Connect to a VPC for outbound traffic** and **Send traffic directly to a VPC**.

  5. In the **Subnet** field, select the subnet where your service receives IP addresses from. You can deploy or execute multiple services or jobs on the same subnet.

  6. In the **Network tags** field, enter the names of the [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#restrictions) that you want to associate with your service or job.

  7. For jobs, click **Update**. For services, click **View diff & redeploy**, then **Deploy changes**.




For services, every service revision can have a different set of network tags because network tags are specified at the revision level. For jobs, a job execution has the same network tags that the job had when the execution of the job was created. 

### gcloud

To associate [network tags](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access#network-tags) with a service or job, use the `gcloud run deploy` command:
    
    
    gcloud run deploy SERVICE_JOB_NAME \
        --image=IMAGE_URL \
        --network=NETWORK \
        --subnet=SUBNET \
        --network-tags=NETWORK_TAG_NAMES \
        --region=REGION

Replace the following:

  * SERVICE_JOB_NAME with the name of your service or job.
  * IMAGE_URL with the image URL of the service or job.
  * NETWORK with the name of your VPC network.
  * SUBNET with the name of your subnet. Specify either a VPC network or a subnet, or both. If you specify only a network, the subnet uses the same name as the network. You can deploy or execute multiple services, jobs, worker pools, or instances on the same subnet. 
  * NETWORK_TAG_NAMES with the name of your network tag or a comma-separated list of network tags.
  * REGION with the name of your region.



For services, every service revision can have a different set of network tags because network tags are specified at the revision level. For jobs, a job execution has the same network tags that the job had when the execution of the job was created. 

## Disconnect a Cloud Run resource

Depending on the Cloud Run resource that you have, see the instructions in one of the following sections:

  * Disconnect a service
  * Disconnect a job
  * Disconnect a worker pool
  * Disconnect an instance



### Disconnect a service

### Console

  * To remove your service from the VPC network:

    1. [Go to Cloud Run](https://console.cloud.google.com/run/services)

    2. Click the service.

    3. Click the **Networking** tab.

    4. Clear **Connect to a VPC for outbound traffic**.

    5. Click **View diff & redeploy**, then **Deploy changes**.

    6. To verify that your service is no longer on your VPC network, click the **Networking** tab. The network and subnet are no longer listed in the **VPC** card.

  * To remove only the network tags while keeping the service connected to the VPC network:

    1. Click the service that contains the network tags you want to remove.

    2. Click the **Networking** tab.

    3. Clear the names of the [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#restrictions) that you no longer want to associate with your service.

    4. Click **View diff & redeploy**, then **Deploy changes**.




###  gcloud 

  * To remove your service from the VPC network, run the following command:
        
        gcloud run services update SERVICE_NAME --region=REGION \
        --clear-network

  * To remove only the network tags while keeping the service connected to the VPC network, run the following command:
        
        gcloud run services update SERVICE_NAME --region=REGION \
        --clear-network-tags

Replace the following:

    * SERVICE_NAME: the name of your Cloud Run service.
    * REGION: the region for your Cloud Run service.



### YAML

  * To remove your service from the VPC network:

    1. Download the service's [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
           
           gcloud run services describe SERVICE_NAME --format export > service.yaml

    2. Remove the following content from your `service.yaml` file:
           
           run.googleapis.com/network-interfaces: '[{"network":"NETWORK","subnetwork":"SUBNET","tags":"NETWORK_TAG_NAMES"}]'

Where

       * NETWORK: the name of your VPC network.
       * SUBNET: the name of your subnet.
       * Optional: NETWORK_TAG_NAMES: the names of the network tags if you had associated them with a service.
    3. Deploy the service revision by running the following command:
           
           gcloud run services replace service.yaml

  * To remove only the network tags while keeping the service connected to the VPC network:

    1. Download the service's [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
           
           gcloud run services describe SERVICE_NAME --format export > service.yaml

    2. Remove the `tags` variable from the content in your `service.yaml` file, leaving the `network` and `subnetwork` variables in place, as shown in the following example:
           
           run.googleapis.com/network-interfaces: '[{"network":"NETWORK","subnetwork":"SUBNET"}]'

Where

       * NETWORK: the name of your VPC network.
       * SUBNET: the name of your subnet.
    3. Deploy the service revision by running the following command:
           
           gcloud run services replace service.yaml




### Disconnect a job

### Console

  * To remove your job from the VPC network:

    1. [Go to Cloud Run](https://console.cloud.google.com/run/jobs)

    2. Click the job you want to remove, then click **Edit and deploy new revision**.

    3. Click the **Connections** tab.

    4. Clear **Connect to a VPC for outbound traffic**.

    5. Click **Update**.

    6. To verify that your job is no longer on your VPC network, click the **Configuration** tab. The network and subnet are no longer listed in the **VPC** card.

  * To remove only the network tags while keeping the job connected to the VPC network:

    1. Click the job that contains the network tags you want to remove, then click **Edit and deploy new revision**.

    2. Click the **Connections** tab.

    3. Clear the names of the [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#restrictions) that you no longer want to associate with your job.

    4. Click **Update**.




###  gcloud 

  * To remove your job from the VPC network, run the following command:
        
        gcloud run jobs update JOB_NAME --region=REGION \
          --clear-network
          

  * To remove only the network tags while keeping the job connected to the VPC network, run the following command:
        
        gcloud run jobs update JOB_NAME --region=REGION \
          --clear-network-tags
          

Replace the following:

    * JOB_NAME: the name of your Cloud Run job.
    * REGION: the region for your Cloud Run job.



### YAML

  * To remove your job from the VPC network:

    1. Download the job's [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1#job):
           
           gcloud run jobs describe JOB_NAME --format export > job.yaml

    2. Remove the following content from your `job.yaml` file:
           
           run.googleapis.com/network-interfaces: '[{"network":"NETWORK","subnetwork":"SUBNET","tags":"NETWORK_TAG_NAMES"}]'

Replace the following:

       * NETWORK: the name of your VPC network.
       * SUBNET: the name of your subnet.
       * Optional: NETWORK_TAG_NAMES with the names of the network tags if you had associated them with a job.
    3. Update the job by running the following command:
           
           gcloud run jobs replace job.yaml

  * To remove only the network tags while keeping the job connected to the VPC network:

    1. Download the job's [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1#job):
           
           gcloud run jobs describe JOB_NAME --format export > job.yaml

    2. Remove the `tags` variable from the content in your `job.yaml` file, leaving the `network` and `subnetwork` variables in place, as shown in the following example:
           
           run.googleapis.com/network-interfaces: '[{"network":"NETWORK","subnetwork":"SUBNET"}]'

Replace the following:

       * NETWORK: the name of your VPC network.
       * SUBNET: the name of your subnet.
    3. Update the job by running the following command:
           
           gcloud run jobs replace job.yaml




### Disconnect a worker pool

###  gcloud 

  * To remove your worker pool from the VPC network, run the following command:
        
        gcloud run worker-pools update WORKER_POOL --region=REGION \
        --clear-network

  * To remove only the network tags while keeping the worker pool connected to the VPC network, run the following command:
        
        gcloud run worker-pools update WORKER_POOL --region=REGION \
        --clear-network-tags

Replace the following:

    * WORKER_POOL: the name of your Cloud Run worker pool.
    * REGION: the region for your Cloud Run worker pool.



### Disconnect an instance

###  gcloud 

  * To remove your instance from the VPC network, run the following command:
        
        gcloud beta run instances update INSTANCE_NAME \
          --region=REGION \
          --clear-network

  * To remove only the network tags while keeping the instance connected to the VPC network, run the following command:
        
        gcloud beta run instances update INSTANCE_NAME \
            --region=REGION \
            --clear-network-tags

Replace the following:

    * `INSTANCE_NAME`: the name of your Cloud Run instance.
    * `REGION`: the region for your Cloud Run instance.



### YAML

  * To remove your instance from the VPC network:

    1. Download the instance's [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
           
           gcloud beta run instances describe INSTANCE_NAME --format export > instance.yaml

    2. Remove the `run.googleapis.com/network-interfaces` annotation from `metadata.annotations` in your `instance.yaml` file.

    3. Update the instance by running the following command:
           
           gcloud beta run instances replace instance.yaml




## Troubleshooting

### Cannot delete subnet

To delete a subnet, you must first delete or redeploy all resources that use it. If Cloud Run is using a subnet, disconnect the Cloud Run service, job, worker pool, or instance from the VPC network or move it to a different subnet before deleting the subnet.

**Note:** After you delete or move your Cloud Run resources, wait 1-2 hours for Cloud Run to release the IP addresses before you delete the subnet.

### Direct VPC egress subnet runs out of IPv4 addresses

The following error occurs when you try to deploy:
    
    
    Instance failed to start because of insufficient free IP addresses in the
    subnetwork SUBNET_ID when attempting to create an address in the
    subnetwork. Please consider moving to a subnetwork with more available IP
    addresses.

If the subnet of the VPC network runs out of IPv4 addresses, it is logged by Cloud Logging. When this occurs, Cloud Run cannot start any more service instances or job tasks until more IPv4 addresses become available.

To resolve this issue, follow the [IP address exhaustion strategies](https://docs.cloud.google.com/run/docs/configuring/networking-best-practices#alt-ip-address).

### View allocated IP addresses

You cannot manually delete a reserved address. The following error occurs when you try to delete an IP address allocated for Cloud Run:
    
    
    The address resource 'ADDRESS_NAME' is already being used by
    '//serverless.googleapis.com/projects/PROJECT_ID/locations/REGION/addressReservations/ADDRESS_NAME'

To see which IP addresses Cloud Run has allocated, go to the [IP addresses page](https://console.cloud.google.com/networking/addresses) in the Google Cloud console and look for addresses where the **In use by** column is set to **Serverless**.

Alternatively, you can run the following command from the Google Cloud CLI:
    
    
    gcloud compute addresses list --filter="purpose=SERVERLESS"

### Issues with custom MTU

If you experience issues with a custom MTU, ensure that you [use the default MTU setting for Cloud Run](https://docs.cloud.google.com/run/docs/configuring/networking-best-practices#mtu).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
