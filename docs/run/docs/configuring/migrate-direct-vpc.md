---
url: https://docs.cloud.google.com/run/docs/configuring/migrate-direct-vpc/
title: Migrate standard VPC connector to Direct VPC egress \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:15:48.877380+00:00
---

# Migrate standard VPC connector to Direct VPC egress  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/migrate-direct-vpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Migrate standard VPC connector to Direct VPC egress Stay organized with collections  Save and categorize content based on your preferences. 

This page is for networking specialists who want to migrate standard VPC network traffic from using [Serverless VPC Access connectors](https://docs.cloud.google.com/run/docs/configuring/vpc-connectors) to using [Direct VPC egress](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc) when sending traffic to a VPC network.

Direct VPC egress is faster and can handle more traffic than connectors, delivering lower latency and higher throughput because it uses a new, direct network path rather than connector instances.

Before migration, we recommend that you familiarize yourself with Direct VPC egress [prerequisites](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc#before_you_begin), [limitations](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc#limitations), [IP address allocation](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc#direct-vpc-ip-allocation), [IAM permissions](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc#set_up_iam_permissions), and [firewall rules](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc#restrict-access).

Connectors continue to incur charges even if they have no traffic and are disconnected. For details, see [pricing](https://cloud.google.com/vpc/pricing#serverless-vpc-pricing). If you no longer need your connector, be sure to [delete](https://docs.cloud.google.com/run/docs/configuring/vpc-connectors#delete) it to avoid continued billing.

## Migrate services to Direct VPC egress gradually

When you migrate Cloud Run services from Serverless VPC Access connectors to Direct VPC egress, we recommend that you do so in a gradual transition.

To transition gradually:

  1. Follow the instructions in this section to update your service to use Direct VPC egress.
  2. [Split a small percentage of traffic](https://docs.cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration#split-traffic) to determine whether the traffic works correctly.
  3. Update the traffic split to send all traffic to the new revision using Direct VPC egress.



To migrate traffic with Direct VPC egress for a service, use the Google Cloud console or Google Cloud CLI:

### Console

  1. In the Google Cloud console, go to the Cloud Run **Services** page.

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Click the service that you want to migrate from a connector to Direct VPC egress.

  3. Click the **Networking** tab.

  4. From the **VPC** section, select the checkbox next to **Connect to a VPC for outbound traffic**.

  5. In the **Network** field, select the VPC network that you want to send traffic to.

  6. In the **Subnet** field, select the subnet where your service receives IP addresses from. You can deploy multiple services on the same subnet.

  7. Optional: Enter the names of the [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#restrictions) that you want to associate with your service or services. Network tags are specified at the revision-level. Each service revision can have different network tags, such as `network-tag-2`.

  8. For **Traffic routing** , select one of the following:

     * **Route only requests to private IPs to the VPC** to send only traffic to internal addresses through the VPC network.
     * **Route all traffic to the VPC** to send all outbound traffic through the VPC network.
  9. Click **View diff & redeploy**, then **Deploy changes**.

  10. To verify that your service is on your VPC network, click the service, then click the **Networking** tab. The network and subnet are listed in the **VPC** card.

You can now send requests directly from your Cloud Run service to any resource on the VPC network, as allowed by your firewall rules.




###  gcloud 

To migrate a Cloud Run service from a connector to Direct VPC egress using the Google Cloud CLI:

  1. Update your Cloud Run service to use Direct VPC egress and clear the connector using the following command.

**Note:** Don't specify the `--vpc-egress` flag in this step. Using the `--clear-vpc-connector` flag ignores custom egress settings, such as routing all traffic, and resets the default to `private-ranges-only`. If you need to route all traffic through the VPC network, also follow the next step.
         
         gcloud run services update SERVICE_NAME \
           --clear-vpc-connector \
           --network=NETWORK \
           --subnet=SUBNET \
           --network-tags=NETWORK_TAG_NAMES \
           --region=REGION \
           --no-traffic

Replace:

     * SERVICE_NAME with the name of your service.
     * NETWORK with the name of your VPC network.
     * SUBNET with the name of your subnet. You can deploy or execute multiple services or jobs on the same subnet. 
     * Optional: NETWORK_TAG_NAMES with the comma-separated names of the [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#restrictions) you want to associate with a service. For services, network tags are specified at the revision-level. Each service revision can have different network tags, such as `network-tag-2`.
     * REGION with a region for your service.
  2. Optional: To route all outbound traffic through the VPC network, run the following command to update the egress setting:
         
         gcloud run services update SERVICE_NAME \
           --vpc-egress=all-traffic \
           --region REGION

Replace:

     * SERVICE_NAME with the name of your service.
     * REGION with the region you specified in the previous step.
  3. To verify that your service is on your VPC network, run the following command:
         
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




You can now send requests from your Cloud Run service to any resource on the VPC network, as allowed by your firewall rules.

## Migrate jobs to Direct VPC egress

**Important:** Connectors continue to incur charges even if they have no traffic and are disconnected. For details, see [pricing](https://cloud.google.com/vpc/pricing#serverless-vpc-pricing). If you no longer need your connector, be sure to [delete](https://docs.cloud.google.com/run/docs/configuring/vpc-connectors#delete) it to avoid continued billing.

You can migrate traffic with Direct VPC egress for a job by using the Google Cloud console or Google Cloud CLI.

### Console

  1. In the Google Cloud console, go to the Cloud Run **Jobs** page.

[Go to Cloud Run](https://console.cloud.google.com/run/jobs)

  2. Click the job that you want to migrate from a connector to Direct VPC egress, then click **Edit**.

  3. Click the **Networking** tab.

  4. Click **Container, Variables & Secrets, Connections, Security** to expand the job properties page.

  5. Click the **Connections** tab.

  6. From **Connect to a VPC for outbound traffic** , click **Send traffic directly to a VPC**.

  7. In the **Network** field, select the VPC network that you want to send traffic to.

  8. In the **Subnet** field, select the subnet where your job receives IP addresses from. You can deploy multiple jobs on the same subnet.

  9. Optional: Enter the names of the [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#restrictions) that you want to associate with your service or services. Network tags are specified at the revision-level. Each service revision can have different network tags, such as `network-tag-2`.

  10. For **Traffic routing** , select one of the following:

     * **Route only requests to private IPs to the VPC** to send only traffic to internal addresses through the VPC network.
     * **Route all traffic to the VPC** to send all outbound traffic through the VPC network.
  11. Click **Update**.

  12. To verify that your job is on your VPC network, click the job, then click the **Configuration** tab. The network and subnet are listed in the **VPC** card.




You can now execute your Cloud Run job and send requests from the job to any resource on the VPC network, as allowed by your firewall rules.

###  gcloud 

To migrate a Cloud Run job from a connector to Direct VPC egress using the Google Cloud CLI:

  1. Update your Cloud Run job to use Direct VPC egress and clear the connector by running the following command.

**Note:** Don't specify the `--vpc-egress` flag in this step. Using the `--clear-vpc-connector` flag ignores custom egress settings, such as routing all traffic, and resets the default to `private-ranges-only`. If you need to route all traffic through the VPC network, also follow the next step.
         
         gcloud run jobs update JOB_NAME \
           --clear-vpc-connector \
           --network=NETWORK \
           --subnet=SUBNET \
           --network-tags=NETWORK_TAG_NAMES \
           --region=REGION

Replace:

     * JOB_NAME with the name of your job.
     * NETWORK with the name of your VPC network.
     * SUBNET with the name of your subnet. You can deploy or execute multiple services or jobs on the same subnet. 
     * Optional: NETWORK_TAG_NAMES with the names of the [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#restrictions) you want to associate with a job. For jobs, network tags are specified at the execution-level. Each job execution can have different network tags, such as `network-tag-2`.
     * REGION with a region for your job.
  2. Optional: To route all outbound traffic through the VPC network, run the following command to update the egress setting:
         
         gcloud run jobs update JOB_NAME \
           --vpc-egress=all-traffic \
           --region=REGION

Replace:

     * JOB_NAME with the name of your job.
     * REGION with the region you specified in the previous step.
  3. To verify that your job is on your VPC network, run the following command:
         
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
    




You can now send requests from your Cloud Run job to any resource on the VPC network, as allowed by your firewall rules.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
