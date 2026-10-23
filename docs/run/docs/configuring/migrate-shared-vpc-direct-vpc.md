---
url: https://docs.cloud.google.com/run/docs/configuring/migrate-shared-vpc-direct-vpc/
title: Migrate Shared VPC connector to Direct VPC egress \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:44:27.522656+00:00
---

# Migrate Shared VPC connector to Direct VPC egress  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/migrate-shared-vpc-direct-vpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Migrate Shared VPC connector to Direct VPC egress Stay organized with collections  Save and categorize content based on your preferences. 

This page is for networking specialists who want to migrate Shared VPC network traffic from using [Serverless VPC Access connectors](https://docs.cloud.google.com/run/docs/configuring/shared-vpc-service-projects) to using [Direct VPC egress](https://docs.cloud.google.com/run/docs/configuring/shared-vpc-direct-vpc) when sending traffic to a Shared VPC network.

Direct VPC egress is faster and can handle more traffic than connectors, delivering lower latency and higher throughput because it uses a new, direct network path instead of connector instances.

Before migration, we recommend that you familiarize yourself with Direct VPC egress [prerequisites](https://docs.cloud.google.com/run/docs/configuring/shared-vpc-direct-vpc#before_you_begin), [limitations](https://docs.cloud.google.com/run/docs/configuring/shared-vpc-direct-vpc#limitations), [IP address allocation](https://docs.cloud.google.com/run/docs/configuring/shared-vpc-direct-vpc#direct-vpc-ip-allocation), and [IAM permissions](https://docs.cloud.google.com/run/docs/configuring/shared-vpc-direct-vpc#set_up_iam_permissions).

Connectors continue to incur charges even if they have no traffic and are disconnected. For details, see [pricing](https://cloud.google.com/vpc/pricing#serverless-vpc-pricing). If you no longer need your connector, be sure to [delete](https://docs.cloud.google.com/run/docs/configuring/vpc-connectors#delete) it to avoid continued billing.

## Migrate services to Direct VPC egress gradually

When you migrate Cloud Run services from Serverless VPC Access connectors to Direct VPC egress, we recommend that you do so in a gradual transition.

To transition gradually:

  1. Follow the instructions in this guide to update your service or job to use Direct VPC egress.
  2. [Split a small percentage of traffic](https://docs.cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration#split-traffic) to test that the traffic works correctly.
  3. Update the traffic split to send all traffic to the new revision using Direct VPC egress.



To migrate traffic with Direct VPC egress for a service, use the Google Cloud console or Google Cloud CLI:

### Console

  1. In the Google Cloud console, go to the Cloud Run **Services** page:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Click the service that you want to migrate from a connector to Direct VPC egress.

  3. Click the **Networking** tab.

  4. From **Connect to a VPC for outbound traffic** , click **Send traffic directly to a VPC**.

  5. Select **Networks shared with me**.

  6. In the **Network** field, select the Shared VPC network that you want to send traffic to.

  7. In the **Subnet** field, select the subnet where your service receives IP addresses from. You can deploy multiple services on the same subnet.

  8. Optional: Enter the names of the [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#restrictions) that you want to associate with your service or services. Network tags are specified at the revision-level. Each service revision can have different network tags, such as `network-tag-2`.

  9. For **Traffic routing** , select one of the following:

     * **Route only requests to private IPs to the VPC** to send only traffic to internal addresses through the Shared VPC network.
     * **Route all traffic to the VPC** to send all outbound traffic through the Shared VPC network.
  10. Click **View diff & redeploy**, then **Deploy changes**.

  11. To verify that your service is on your Shared VPC network, click the service, then click the **Networking** tab. The network and subnet are listed in the **VPC** card.

You can now send requests directly from your Cloud Run service to any resource on the Shared VPC network, as allowed by your firewall rules.




###  gcloud 

To migrate a Cloud Run service from a connector to Direct VPC egress using the Google Cloud CLI:

  1. Update your service on the shared subnet by specifying the fully qualified resource names for the Shared VPC network and subnet using the following command.

**Note:** Don't specify the `--vpc-egress` flag in this step. Using the `--clear-vpc-connector` flag ignores custom egress settings, such as routing all traffic, and resets the default to `private-ranges-only`. If you need to route all traffic through the Shared VPC network, also follow the next step.
         
         gcloud run services update SERVICE_NAME \
           --clear-vpc-connector \
           --network projects/HOST_PROJECT_ID/global/networks/VPC_NETWORK \
           --subnet projects/HOST_PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME \
           --network-tags NETWORK_TAG_NAMES \
           --region REGION \
           --max-instances MAX \
           --no-traffic

Replace the following:

     * SERVICE_NAME: the name of your Cloud Run service.
     * HOST_PROJECT_ID: the ID of your Shared VPC project.
     * VPC_NETWORK: the name of your Shared VPC network.
     * REGION: the region for your Cloud Run service, which must match the region of your subnet.
     * SUBNET_NAME: the name of your subnet.
     * Optional: NETWORK_TAG_NAMES with the comma-separated names of the [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#restrictions) you want to associate with a service. For services, network tags are specified at the revision-level. Each service revision can have different network tags, such as `network-tag-2`.
     * MAX: the maximum number of instances to use for the Shared VPC network. The maximum number of instances allowed for services is 100.
  2. Optional: To route all outbound traffic through the Shared VPC network, run the following command to update the egress setting:
         
         gcloud run services update SERVICE_NAME \
           --vpc-egress=all-traffic \
           --region REGION

Replace the following:

     * SERVICE_NAME: the name of your Cloud Run service.
     * REGION: the region for your Cloud Run service.

For more details and optional arguments, see the [`gcloud` reference](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy).

  3. To verify that your service is on your Shared VPC network, run the following command:
         
         gcloud run services describe SERVICE_NAME \
           --region=REGION

Replace:

     * SERVICE_NAME with the name of your service.
     * REGION with the region for your service that you specified in the previous step.

The output should contain the name of your network, subnet, and egress setting, for example:
    
    VPC access:
      Network:       default
      Subnet:        subnet
      Egress:        private-ranges-only
    

  4. Divert a fraction of traffic to the new Direct VPC egress path. For example, to divert 10% of traffic to the latest revision created in the previous step, run the following command:
         
         gcloud run services update-traffic SERVICE_NAME --to-revisions=LATEST=10

Replace SERVICE_NAME with the name of your service.

After you are confident that there are no regressions, gradually migrate traffic to the latest revision.




You can now send requests from your Cloud Run service to any resource on the Shared VPC network, as allowed by your firewall rules.

## Migrate jobs to Direct VPC egress

**Important:** Connectors continue to incur charges even if they have no traffic and are disconnected. For details, see [pricing](https://cloud.google.com/vpc/pricing#serverless-vpc-pricing). If you no longer need your connector, be sure to [delete](https://docs.cloud.google.com/run/docs/configuring/vpc-connectors#delete) it to avoid continued billing.

You can migrate traffic with Direct VPC egress for a job by using the Google Cloud console or Google Cloud CLI.

### Console

  1. In the Google Cloud console, go to the Cloud Run **Jobs** page:

[Go to Cloud Run](https://console.cloud.google.com/run/jobs)

  2. Click the job that you want to migrate from a connector to Direct VPC egress, then click **Edit**.

  3. Click the **Networking** tab.

  4. Click **Container, Variables & Secrets, Connections, Security** to expand the job properties page.

  5. Click the **Connections** tab.

  6. From **Connect to a VPC for outbound traffic** , click **Send traffic directly to a VPC**.

  7. Select **Networks shared with me**.

  8. In the **Network** field, select the Shared VPC network that you want to send traffic to.

  9. In the **Subnet** field, select the subnet where your job receives IP addresses from. You can deploy multiple jobs on the same subnet.

  10. Optional: Enter the names of the [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#restrictions) that you want to associate with a job. For jobs, network tags are specified at the execution-level. Each job execution can have different network tags, such as `network-tag-2`.

  11. For **Traffic routing** , select one of the following:

     * **Route only requests to private IPs to the VPC** to send only traffic to internal addresses through the Shared VPC network.
     * **Route all traffic to the VPC** to send all outbound traffic through the Shared VPC network.
  12. Click **Update**.

  13. To verify that your job is on your Shared VPC network, click the job, then click the **Configuration** tab. The network and subnet are listed in the **VPC** card.




You can now execute your Cloud Run job and send requests from the job to any resource on the Shared VPC network, as allowed by your firewall rules.

###  gcloud 

To migrate a Cloud Run job from a connector to Direct VPC egress using the Google Cloud CLI:

  1. Update your job on the shared subnet by specifying the fully qualified resource names for the Shared VPC network and subnet using the following command.

**Note:** Don't specify the `--vpc-egress` flag in this step. Using the `--clear-vpc-connector` flag ignores custom egress settings, such as routing all traffic, and resets the default to `private-ranges-only`. If you need to route all traffic through the Shared VPC network, also follow the next step.
         
         gcloud run jobs update JOB_NAME \
           --clear-vpc-connector \
           --network projects/HOST_PROJECT_ID/global/networks/VPC_NETWORK \
           --subnet projects/HOST_PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME \
           --network-tags NETWORK_TAG_NAMES \
           --region REGION

Replace the following:

     * JOB_NAME: the name of your Cloud Run job.
     * HOST_PROJECT_ID: the ID of your Shared VPC project.
     * VPC_NETWORK: the name of your Shared VPC network.
     * REGION: the region for your Cloud Run job, which must match the region of your subnet.
     * SUBNET_NAME: the name of your subnet.
     * Optional: NETWORK_TAG_NAMES with the comma-separated names of the [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#restrictions) you want to associate with a job. Each job execution can have different network tags, such as `network-tag-2`.
  2. Optional: To route all outbound traffic through the Shared VPC network, run the following command to update the egress setting:
         
         gcloud run jobs update JOB_NAME \
           --vpc-egress=all-traffic \
           --region REGION

Replace the following:

     * JOB_NAME: the name of your Cloud Run job.
     * REGION: the region for your Cloud Run job.

For more details and optional arguments, see the [`gcloud` reference](https://docs.cloud.google.com/sdk/gcloud/reference/run/jobs/update).

  3. To verify that your job is on your Shared VPC network, run the following command:
         
         gcloud run jobs describe JOB_NAME \
           --region=REGION

Replace:

     * JOB_NAME with the name of your job.
     * REGION with the region for your job that you specified in the previous step.

The output should contain the name of your network, subnet, and egress setting, for example:
    
    VPC access:
      Network:       default
      Subnet:        subnet
      Egress:        private-ranges-only
    




You can now send requests from your Cloud Run job to any resource on the Shared VPC network, as allowed by your firewall rules.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
