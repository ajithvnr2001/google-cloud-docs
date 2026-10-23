---
url: https://docs.cloud.google.com/sap/docs/sap-netweaver-ha-vip-migration-for-rhel/
title: Migrate a VIP in an SAP NetWeaver HA cluster on RHEL to an internal passthrough Network Load Balancer \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:01:48.131867+00:00
---

# Migrate a VIP in an SAP NetWeaver HA cluster on RHEL to an internal passthrough Network Load Balancer  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/sap-netweaver-ha-vip-migration-for-rhel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Migrate a VIP in an SAP NetWeaver HA cluster on RHEL to an internal passthrough Network Load Balancer Stay organized with collections  Save and categorize content based on your preferences. 

On Google Cloud, the recommended way to implement a virtual IP address (VIP) for an OS-based high-availability (HA) cluster for SAP NetWeaver is to use the failover support of an internal passthrough Network Load Balancer. 

This guide describes how to migrate a virtual IP (VIP) implementation in a Red Hat Enterprise Linux (RHEL) HA cluster for SAP NetWeaver from alias IPs to an internal passthrough Network Load Balancer.

## Before you begin

  * These instructions assume that you already have a properly configured SAP NetWeaver (ASCS/ERS) HA cluster on Google Cloud that uses an alias IP for the virtual IP (VIP) implementation.
  * This migration requires a scheduled downtime for your SAP system.

All steps from the beginning of this guide up to and including "Test the load balancer configuration" can be performed while your SAP system is fully operational. These preparatory steps configure the load balancer components and test health checks using a temporary IP without impacting your live SAP system.

Stop your SAP application server instances before you proceed to the section "Migrate the VIP implementation to use the load balancer". The actions within that section and all subsequent steps cause your SAP NetWeaver system to become unavailable. This is because the initial step in the migration process involves deallocating the existing alias IPs from your Compute Engine instances, which make the SAP VIPs unreachable on the network.




## Migration overview

Migrating a VIP implementation from alias IP to internal passthrough Network Load Balancer in an SAP NetWeaver HA cluster on RHEL includes the following high-level steps:

  1. Configure and test a load balancer by using a temporary forwarding rule and a temporary IP address in place of the VIP.
  2. Set your cluster to maintenance mode and stop your SAP application server instances.
  3. Deallocate the alias IP addresses from the primary and secondary hosts. These addresses become the VIPs with the load balancer.
  4. In the Pacemaker cluster configuration: 
     1. Delete the existing VIP resources from the ASCS and ERS resource groups.
     2. Add new health check resources to respond to the load balancer's TCP health checks.
     3. Reassemble the resource groups to ensure the health check service starts before the SAP instance.



## Verify the existing VIP addresses

Identify the alias IP addresses that are managed by the cluster. In an SAP NetWeaver system, you must identify the VIPs for both the ASCS and the ERS instances. These addresses are used as the frontend IPs for the internal passthrough Network Load Balancer.

  * To check the existing cluster primitives for the ASCS and ERS alias configurations:
        
        pcs config
        

In the resource definition, the VIP address appears on the `alias` and `IPaddr2` resources for both instances. The output is similar to the following example:
        
        Resource: rsc_vip_rmk_ascs01_alias (class=ocf provider=heartbeat type=gcp-vpc-move-vip)
          Attributes: rsc_vip_rmk_ascs01_alias-instance_attributes
            alias_ip=10.10.0.50/32
            project=project-1998-467706
          Operations:
            monitor: rsc_vip_rmk_ascs01_alias-monitor-interval-30s
              interval=30s
              timeout=60s
            start: rsc_vip_rmk_ascs01_alias-start-interval-0s
              interval=0s
              timeout=120s
            stop: rsc_vip_rmk_ascs01_alias-stop-interval-0s
              interval=0s
              timeout=120s
        Resource: ascs_vip_rmk (class=ocf provider=heartbeat type=IPaddr2)
          Attributes: ascs_vip_rmk-instance_attributes
            cidr_netmask=32
            ip=10.10.0.50
            nic=lo
          Operations:
            monitor: ascs_vip_rmk-monitor-interval-3600
              interval=3600
              timeout=60
            start: ascs_vip_rmk-start-interval-0s
              interval=0s
              timeout=20s
            stop: ascs_vip_rmk-stop-interval-0s
              interval=0s
              timeout=20s
        Resource: rsc_vip_rmk_ers03_alias (class=ocf provider=heartbeat type=gcp-vpc-move-vip)
          Attributes: rsc_vip_rmk_ers03_alias-instance_attributes
            alias_ip=10.10.0.60/32
            project=project-1998-467706
          Operations:
            monitor: rsc_vip_rmk_ers03_alias-monitor-interval-30s
              interval=30s
              timeout=60s
            start: rsc_vip_rmk_ers03_alias-start-interval-0s
              interval=0s
              timeout=120s
            stop: rsc_vip_rmk_ers03_alias-stop-interval-0s
              interval=0s
              timeout=120s
        Resource: ers_vip_rmk (class=ocf provider=heartbeat type=IPaddr2)
          Attributes: ers_vip_rmk-instance_attributes
            cidr_netmask=32
            ip=10.10.0.60
            nic=lo
          Operations:
            monitor: ers_vip_rmk-monitor-interval-3600
              interval=3600
              timeout=60
            start: ers_vip_rmk-start-interval-0s
              interval=0s
              timeout=20s
            stop: ers_vip_rmk-stop-interval-0s
              interval=0s
              timeout=20s




### Verify that VIP addresses are reserved

In the Google Cloud console, verify that the IP addresses used for both the ASCS and ERS alias IPs are reserved. You can reuse the existing alias IP addresses or reserve new ones.

  1. List the reserved addresses in your region:
         
         gcloud compute addresses list \
            --filter="region:( CLUSTER_REGION )"

Replace `CLUSTER_REGION` with the [region](https://docs.cloud.google.com/compute/docs/regions-zones) where you've deployed your HA cluster.

If the IP addresses are reserved and allocated as alias IPs, then their status shows as `IN_USE`. When you later deallocate these from the compute instances to move them to the load balancer, their status changes to `RESERVED`.

If the addresses are not included in the IP addresses that are returned by the preceding command, then reserve them to prevent IP address conflicts:
         
         gcloud compute addresses create VIP_NAME \
            --region CLUSTER_REGION --subnet CLUSTER_SUBNET --addresses IP_ADDRESS

Replace the following:

     * `VIP_NAME`: the name you want to set for the static internal IP address resource
     * `CLUSTER_SUBNET`: the name of the subnetwork where you've allocated the IP address
     * `IP_ADDRESS`: the static internal IP address that you want to reserve
  2. List your addresses again to verify that the IP addresses show up as `RESERVED`.




## Enable load balancer backend communication between the compute instances

You enable backend communication between the compute instances by modifying the configuration of the `google-guest-agent`, which is included in the [Linux guest environment](https://docs.cloud.google.com/compute/docs/images/guest-environment#linux) for all Linux public images that are provided by Google Cloud.

To enable load balancer backend communications, complete the following steps on each compute instance that is part of your cluster:

  1. Open or create the file `/etc/default/instance_configs.cfg` for editing. For example:
         
         sudo vi /etc/default/instance_configs.cfg

  2. In the `/etc/default/instance_configs.cfg` file, specify the following configuration properties.

If the `IpForwarding` and `NetworkInterfaces` sections don't exist, then create them. Verify that both the `target_instance_ips` and `ip_forwarding` properties are set to `false`.
         
         [IpForwarding]
         ethernet_proto_id = 66
         ip_aliases = true
         target_instance_ips = false
         [NetworkInterfaces]
         dhclient_script = /sbin/google-dhclient-script
         dhcp_command =
         ip_forwarding = false
         setup = true
         

  3. [Restart the guest agent](https://docs.cloud.google.com/compute/docs/images/manage-guest-agent#restart-guest-agent).




## Configure failover support for the load balancer

To support high-availability failover of SAP NetWeaver, you must configure an internal passthrough Network Load Balancer with two separate backend services and health checks: one for the ASCS and one for the ERS.

### Reserve a temporary IP address for testing

Before moving the production VIPs, reserve a temporary IP address from the same subnet. You use this temporary IP address to verify that the load balancer can successfully see the SAP services through the health check ports. VIP follows the active ASCS instance.

  1. Reserve a temporary IP address in the same subnet as the alias IP for testing purposes. If you omit the `--addresses` flag, then an IP address in the specified subnet is chosen for you:
         
         gcloud compute addresses create TEST_VIP_NAME \
            --region CLUSTER_REGION --subnet CLUSTER_SUBNET --addresses TEST_VIP_ADDRESS

Replace the following:

     * `TEST_VIP_NAME`: the name you want to set for the temporary VIP
     * `CLUSTER_REGION`: the region where your HA cluster and load balancer are deployed
     * `CLUSTER_SUBNET`: the name of the subnetwork where the IP address is allocated
     * `TEST_VIP_ADDRESS`: the static internal IP address that you want to set for the temporary VIP

For more information about reserving a static IP, see [Reserving a static internal IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address).

  2. Verify IP address reservation:
         
         gcloud compute addresses describe TEST_VIP_NAME --region CLUSTER_REGION

The output is similar to the following example:
         
         address: 10.10.0.4
         addressType: INTERNAL
         creationTimestamp: '2026-04-21T21:01:38.630-07:00'
         description: ''
         id: '1549225759355565773'
         kind: compute#address
         labelFingerprint: 42WmSpB8rSM=
         Name:nw-test-vip
         networkTier: PREMIUM
         purpose: GCE_ENDPOINT
         region: https://www.googleapis.com/compute/v1/projects/example-project-123456/regions/us-central1
         selfLink: https://www.googleapis.com/compute/v1/projects/example-project-123456/regions/us-central1/addresses/nw-test-vip
         status: RESERVED
         subnetwork: https://www.googleapis.com/compute/v1/projects/example-project-123456/regions/us-central1/subnetworks/example-subnet-us-central1




### Create instance groups for your host compute instances

The internal passthrough Network Load Balancer uses instance groups to identify the compute instances that can host the SAP NetWeaver services.

  1. Create one unmanaged instance group for each compute instance in your HA cluster:
         
         gcloud compute instance-groups unmanaged create ASCS_IG_NAME \
            --zone=ASCS_ZONE
         gcloud compute instance-groups unmanaged add-instances ASCS_IG_NAME \
            --zone=ASCS_ZONE --instances=ASCS_HOST_NAME
         gcloud compute instance-groups unmanaged create ERS_IG_NAME \
            --zone=ERS_ZONE
         gcloud compute instance-groups unmanaged add-instances ERS_IG_NAME \
            --zone=ERS_ZONE --instances=ERS_HOST_NAME

Replace the following:

     * `ASCS_IG_NAME`: the name you want to set for the unmanaged instance group that contains the ASCS host compute instance
     * `ASCS_ZONE`: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones) where the ASCS host compute instance is deployed
     * `ASCS_HOST_NAME`: the name of the ASCS host compute instance
     * `ERS_IG_NAME`: the name you want to set for the unmanaged instance group that contains the ERS host compute instance
     * `ERS_ZONE`: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones) where the ERS host compute instance is deployed
     * `ERS_HOST_NAME`: the name of the ERS host compute instance
  2. Confirm the creation of the instance groups:
         
         gcloud compute instance-groups unmanaged list

The output is similar to the following example:
         
         NAME       ZONE            NETWORK           NETWORK_PROJECT   MANAGED  INSTANCES
         ig-vm1     us-central1-a   example-network   example-project   No       1
         ig-vm2     us-central1-b   example-network   example-project   No       1




### Create Compute Engine health checks

For an SAP NetWeaver HA setup, you must create two separate health checks to independently monitor the ASCS and ERS instances.

To avoid clashing with other services, create the Compute Engine health checks with ports that are in the private range `49152-65535`. The check-interval and timeout values are set slightly higher than the default values so as to increase failover tolerance during Compute Engine live migration events. You can adjust the values if needed.

To create the Compute Engine health checks, complete the following steps:

  1. Create the health check for the ASCS instance:
         
         gcloud compute health-checks create tcp HEALTH_CHECK_NAME_ASCS \
            --port=HEALTHCHECK_PORT_NUM_ASCS \
            --proxy-header=NONE --check-interval=10 --timeout=10 --unhealthy-threshold=2 \
            --healthy-threshold=2

Replace the following:

     * `HEALTH_CHECK_NAME_ASCS`: the name that you want to set for the ASCS instance health check resource
     * `HEALTHCHECK_PORT_NUM_ASCS`: the port number that the ASCS health check resource must use to monitor the ASCS instance
  2. Create the health check for the ERS instance:
         
         gcloud compute health-checks create tcp HEALTH_CHECK_NAME_ERS \
            --port=HEALTHCHECK_PORT_NUM_ERS \
            --proxy-header=NONE --check-interval=10 --timeout=10 --unhealthy-threshold=2 \
            --healthy-threshold=2

Replace the following:

     * `HEALTH_CHECK_NAME_ERS`: the name that you want to set for the ERS instance health check resource
     * `HEALTHCHECK_PORT_NUM_ERS`: the port number that the ERS health check resource must use to monitor the ERS instance
  3. Confirm the creation of the health check resources:
         
         gcloud compute health-checks describe HEALTH_CHECK_NAME

The output is similar to the following example:
         
         $ gcloud compute health-checks describe **hc-ascs-r**
         checkIntervalSec: 10
         creationTimestamp: '2026-04-21T21:56:09.599-07:00'
         healthyThreshold: 2
         id: '8622301245279169030'
         kind: compute#healthCheck
         name: hc-ascs-r
         selfLink: https://www.googleapis.com/compute/v1/projects/example-project-123456/global/healthChecks/hc-ascs-r
         tcpHealthCheck:
          port: 62001
          portSpecification: USE_FIXED_PORT
          proxyHeader: NONE
         timeoutSec: 10
         type: TCP
         unhealthyThreshold: 2
         
         $ gcloud compute health-checks describe **hc-ers-r**
         checkIntervalSec: 10
         creationTimestamp: '2026-04-21T21:56:51.615-07:00'
         healthyThreshold: 2
         id: '6550997522402634748'
         kind: compute#healthCheck
         name: hc-ers-r
         selfLink: https://www.googleapis.com/compute/v1/projects/example-project-123456/global/healthChecks/hc-ers-r
         tcpHealthCheck:
          port: 62003
          portSpecification: USE_FIXED_PORT
          proxyHeader: NONE
         timeoutSec: 10
         type: TCP
         unhealthyThreshold: 2




### Create a firewall rule for the health checks

Define a firewall rule that allows access to your host compute instances from the following Google Cloud health check IP ranges: `35.191.0.0/16` and `130.211.0.0/22`. This rule must include the ports that you defined for both the ASCS and ERS health checks.

To create this firewall rule, complete the following steps:

  1. Add a network tag to your compute instances if they don't already have one. This tag is used to target the firewall rule:
         
         gcloud compute instances add-tags ASCS_HOST_NAME \
            --tags NETWORK_TAGS --zone PRIMARY_ZONE
         gcloud compute instances add-tags ERS_HOST_NAME \
            --tags NETWORK_TAGS --zone SECONDARY_ZONE

Replace the following:

     * `NETWORK_TAGS`: one or more network tags that are assigned to the compute instances and targeted by the firewall rule
     * `PRIMARY_ZONE`: the zone where the primary ASCS host instance runs
     * `SECONDARY_ZONE`: the zone where the secondary ERS host instance runs
  2. Create a firewall rule that lets the health checks access your host compute instances:
         
         gcloud compute firewall-rules create RULE_NAME \
            --network NETWORK_NAME --action ALLOW --direction INGRESS \
            --source-ranges 35.191.0.0/16,130.211.0.0/22 --target-tags NETWORK_TAGS \
            --rules tcp:HLTH_CHK_PORT_NUM_ASCS,tcp:HLTH_CHK_PORT_NUM_ERS

Replace the following:

     * `RULE_NAME`: the name that you want to set for the firewall rule
     * `NETWORK_NAME`: the name of the VPC network to which you want to attach this firewall rule
     * `NETWORK_TAGS`: the network tags that you assigned to the compute instances
     * `HLTH_CHK_PORT_NUM_ASCS`: the port number that you've allocated to monitor the ASCS instance
     * `HLTH_CHK_PORT_NUM_ERS`: the port number that you've allocated to monitor the ERS instance

For example:
    
    gcloud compute firewall-rules create fw-allow-health-checks \
       --network example-network \
       --action ALLOW \
       --direction INGRESS \
       --source-ranges 35.191.0.0/16,130.211.0.0/22 \
       --target-tags sap-nw-ha \
       --rules tcp:60000,tcp:60001




## Configure the load balancer and failover group

  1. Create the load balancer backend service for ASCS:
         
         gcloud compute backend-services create BACKEND_SERVICE_NAME_ASCS \
            --load-balancing-scheme internal \
            --health-checks HEALTH_CHECK_NAME_ASCS \
            --no-connection-drain-on-failover \
            --drop-traffic-if-unhealthy \
            --failover-ratio 1.0 \
            --region CLUSTER_REGION

Replace the following:

     * `BACKEND_SERVICE_NAME_ASCS`: the name that you want to set for the load balancer backend service for the ASCS instance
     * `HEALTH_CHECK_NAME_ASCS`: the name of the Compute Engine health check resource that you created for the ASCS instance
  2. Create the load balancer backend service for ERS:
         
         gcloud compute backend-services create BACKEND_SERVICE_NAME_ERS \
            --load-balancing-scheme internal \
            --health-checks HEALTH_CHECK_NAME_ERS \
            --no-connection-drain-on-failover \
            --drop-traffic-if-unhealthy \
            --failover-ratio 1.0 \
            --region CLUSTER_REGION

Replace the following:

     * `BACKEND_SERVICE_NAME_ERS`: the name that you want to set for the load balancer backend service for the ERS instance
     * `HEALTH_CHECK_NAME_ERS`: the name of the Compute Engine health check resource that you created for the ERS instance
  3. Add your instance groups to the ASCS backend service:

     * Add ASCS instance group as the `PRIMARY` backend for ASCS:
           
           gcloud compute backend-services add-backend BACKEND_SERVICE_NAME_ASCS \
           --instance-group ASCS_IG_NAME \
           --instance-group-zone ASCS_ZONE \
           --region CLUSTER_REGION

Replace the following:

       * `BACKEND_SERVICE_NAME_ASCS`: the name that you set for load balancer backend service for the ASCS instance
       * `ASCS_IG_NAME`: the name you set for the unmanaged instance group that contains the ASCS host compute instance
       * `ASCS_ZONE`: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones) where ASCS compute instance is deployed
       * `CLUSTER_REGION`: the [region](https://docs.cloud.google.com/compute/docs/regions-zones) where you've deployed your HA cluster
     * Add ERS instance group as the `FAILOVER` backend for ASCS
           
           gcloud compute backend-services add-backend BACKEND_SERVICE_NAME_ASCS \
            --instance-group ERS_IG_NAME \
            --instance-group-zone ERS_ZONE \
            --region CLUSTER_REGION \
            --failover

Replace the following:

       * `ERS_IG_NAME`: the name you set for the unmanaged instance group that contains the ERS host compute instance
       * `ERS_ZONE`: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones) where ERS compute instance is deployed
  4. Add your instance groups to the ERS backend service:

     * Add ASCS instance group as the `FAILOVER` backend for ERS
           
           gcloud compute backend-services add-backend BACKEND_SERVICE_NAME_ERS \
            --instance-group ASCS_IG_NAME \
            --instance-group-zone ASCS_ZONE \
            --region CLUSTER_REGION \
            --failover

Replace `BACKEND_SERVICE_NAME_ERS` with the name that you set for load balancer backend service for the ERS instance.

     * Add ERS instance group as the PRIMARY backend for ERS
           
           gcloud compute backend-services add-backend BACKEND_SERVICE_NAME_ERS \
            --instance-group ERS_IG_NAME \
            --instance-group-zone ERS_ZONE \
            --region CLUSTER_REGION

  5. Create a temporary forwarding rule to test the load balancer configuration.

Use the temporary IP address that you reserved earlier. This rule maps the test IP address to your ASCS backend service.

If you need to access the SAP NetWeaver system from outside of the specified region, then include the flag `--allow-global-access` in the definition as follows:
         
         gcloud compute forwarding-rules create TEMPORARY_RULE_NAME \
            --load-balancing-scheme internal \
            --address TEST_VIP_NAME \
            --subnet CLUSTER_SUBNET \
            --region CLUSTER_REGION \
            --backend-service BACKEND_SERVICE_NAME_ASCS \
            --ports ALL

Replace the following:

     * `TEMPORARY_RULE_NAME`: the name you want to set for the temporary forwarding rule
     * `TEST_VIP_NAME`: the name that you set for the temporary VIP

For more information about cross-region access to your SAP NetWeaver high-availability system, see [Internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal#client-access).




Your backend instance groups won't register as healthy until you have completed the Pacemaker cluster configuration.

## Test the load balancer configuration

Although your backend instance groups won't register as healthy until later, you can test the load balancer configuration by setting up a listener to respond to the health checks. After setting up a listener, if the load balancer is configured correctly, then the status of the backend instance groups changes to healthy.

Choose **one** of the following methods to test connectivity:

  * Test the load balancer with the `socat` utility
  * Test the load balancer by using port `22`



### Test the load balancer with the `socat` utility

You can use the `socat` utility to temporarily listen on the health check port. You need to install the `socat` utility anyway, because you use it later when you configure cluster resources.

To test the load balancer by using the `socat` utility, complete the following steps:

  1. On both compute instances, as the root user, install the `socat` utility:
         
         yum install -y socat

  2. Start a `socat` process to listen for 60 seconds on the ASCS health check port:
         
         sudo timeout 60s socat - TCP-LISTEN:HLTH_CHK_PORT_NUM_ASCS,fork

  3. In Cloud Shell, after waiting a few seconds for the health check to detect the listener, check the health of your backend instance groups:
         
         gcloud compute backend-services get-health BACKEND_SERVICE_NAME_ASCS \
            --region CLUSTER_REGION

The output is similar to the following example:
         
         backend: https://www.googleapis.com/compute/v1/projects/project-1998-467706/zones/us-central1-a/instanceGroups/ig-ascs-r
         status:
          healthStatus:
         
         

     * forwardingRule: https://www.googleapis.com/compute/v1/projects/example-project-123456/regions/us-central1/forwardingRules/fr-test-lb-r forwardingRuleIp: 10.10.0.4 healthState: HEALTHY instance: https://www.googleapis.com/compute/v1/projects/example-project-123456/zones/us-central1-a/instances/ascs-r ipAddress: 10.10.0.3 port: 80 kind: compute#backendServiceGroupHealth \--- backend: https://www.googleapis.com/compute/v1/projects/example-project-123456/zones/us-central1-b/instanceGroups/ig-ers-r status: healthStatus:
     * forwardingRule: https://www.googleapis.com/compute/v1/projects/example-project-123456/regions/us-central1/forwardingRules/fr-test-lb-r forwardingRuleIp: 10.10.0.4 healthState: HEALTHY instance: https://www.googleapis.com/compute/v1/projects/example-project-123456/zones/us-central1-b/instances/ers-r ipAddress: 10.10.0.2 port: 80 kind: compute#backendServiceGroupHealth



### Test the load balancer by using port `22`

If port `22` is open for SSH connections on your host compute instances, then you can temporarily edit the health checker to use port `22`, which has a listener that can respond to the health checker.

To temporarily use port `22`, complete the following steps:

  1. Click your health check in the Google Cloud console.
  2. Click **Edit**.
  3. In the **Port** field, change the port number to `22`.
  4. Click **Save** and wait a minute or two.
  5. In Cloud Shell, check the health of your backend instance groups:
         
         gcloud compute backend-services get-health BACKEND_SERVICE_NAME_ASCS \
            --region CLUSTER_REGION

The output is similar to the following example:
         
         backend: https://www.googleapis.com/compute/v1/projects/project-1998-467706/zones/us-central1-a/instanceGroups/ig-ascs-vm1
         status:
          healthStatus:
         
         

     * forwardingRule: https://www.googleapis.com/compute/v1/projects/project-1998-467706/regions/us-central1/forwardingRules/fr-nw-test-ascs forwardingRuleIp: 10.1.0.5 healthState: HEALTHY instance: https://www.googleapis.com/compute/v1/projects/project-1998-467706/zones/us-central1-a/instances/ascs-vm1 ipAddress: 10.1.0.2 port: 80 kind: compute#backendServiceGroupHealth \--- backend: https://www.googleapis.com/compute/v1/projects/project-1998-467706/zones/us-central1-b/instanceGroups/ig-ers-vm2 status: healthStatus:
     * forwardingRule: https://www.googleapis.com/compute/v1/projects/project-1998-467706/regions/us-central1/forwardingRules/fr-nw-test-ascs forwardingRuleIp: 10.1.0.5 healthState: HEALTHY instance: https://www.googleapis.com/compute/v1/projects/project-1998-467706/zones/us-central1-b/instances/ers-vm2 ipAddress: 10.1.0.3 port: 80 kind: compute#backendServiceGroupHealth
  6. When you are done, revert the health check port number back to the original port number.




## Migrate the VIP implementation to use the load balancer

**Important:** Before proceeding with any steps in this section, a scheduled downtime is required for your SAP NetWeaver system. To avoid unexpected behavior, first stop all SAP application server instances.

The following steps guide you through editing the Pacemaker cluster configuration and the load balancer forwarding rules:

  1. As the root user, on the active primary instance, put the cluster into maintenance mode:
         
         pcs property set maintenance-mode="true"

  2. Back up the cluster configuration:
         
         pcs config show > clusterconfig.backup




### Deallocate the alias IP

To deallocate the alias IPs, you need to update the network interface of the primary instance to remove the alias IP. If there are multiple alias IPs and you need to keep any of them, then you need to specify the alias IPs that you need to keep in the command. Any alias IPs that are not specified in the update command are deallocated.

To deallocate the alias IPs, complete the following steps:

  1. In Cloud Shell, confirm the alias IP ranges that are assigned to ASCS and ERS instances:
         
         gcloud compute instances describe ASCS_HOST_NAME \
            --zone ASCS_ZONE_NAME --format="flattened(name,networkInterfaces[].aliasIpRanges)"
         gcloud compute instances describe ERS_HOST_NAME \
            --zone ERS_ZONE_NAME --format="flattened(name,networkInterfaces[].aliasIpRanges)"

  2. In the Google Cloud console, update the network interface. If you don't need to retain any alias IPs, then specify `--aliases ""`:

     * Deallocate alias IPs for ASCS:
           
           gcloud compute instances network-interfaces update ASCS_HOST_NAME \
            --zone ASCS_ZONE_NAME --aliases "IP_RANGES_TO_RETAIN"

Replace `IP_RANGES_TO_RETAIN` with the IP addresses that you want to retain.

     * Deallocate alias IPs for ERS:
           
           gcloud compute instances network-interfaces update ERS_HOST_NAME \
            --zone ERS_ZONE_NAME --aliases "IP_RANGES_TO_RETAIN"




### Create the VIP forwarding rule and clean up

In the Google Cloud console, create a new frontend forwarding rule for the load balancer, specifying the IP address that was previously used for the alias-IP's as the IP address. These are the VIPs.

To create the VIP forwarding rule, complete the following steps:

  1. Create the ASCS forwarding rule:
         
         gcloud compute forwarding-rules create ASCS_RULE_NAME \
            --load-balancing-scheme internal \
            --address VIP_ADDRESS \
            --subnet CLUSTER_SUBNET \
            --region CLUSTER_REGION \
            --backend-service BACKEND_SERVICE_NAME_ASCS \
            --ports ALL

  2. Create the ERS forwarding rule:
         
         gcloud compute forwarding-rules create ERS_RULE_NAME \
            --load-balancing-scheme internal \
            --address VIP_ADDRESS \
            --subnet CLUSTER_SUBNET \
            --region CLUSTER_REGION \
            --backend-service BACKEND_SERVICE_NAME_ERS \
            --ports ALL

  3. Confirm that the forwarding rules have been created. Note the name of the temporary forwarding rule for deletion:
         
         gcloud compute forwarding-rules list

  4. Delete the temporary forwarding rule:
         
         gcloud compute forwarding-rules delete TEMPORARY_RULE_NAME \
            --region CLUSTER_REGION

  5. Release the temporary IP address that you had reserved:
         
         gcloud compute addresses delete TEMPORARY_VIP \
            --region CLUSTER_REGION




## Install listeners and create a health check resource

Before you configure a health check resource, you need to install the listeners.

### Install a listener

The load balancer uses a listener on the health-check port of each host to determine where the primary instance of the SAP NetWeaver HA cluster is running. The following instructions install and use `HAProxy` as the listener.

  1. As the root user, on the master instance on the primary and secondary systems, install a TCP listener:
         
         yum install haproxy
         

  2. Open the configuration file `haproxy.cfg` for editing:
         
         vi /etc/haproxy/haproxy.cfg
         

  3. Edit the `haproxy.cfg` file as follows:

     * In the `defaults` section, change the value of the parameter `mode` to `tcp`.
     * Create a new section and place it after the `defaults` section:
           
           #---------------------------------------------------------------------
           # Health check listener port for SAP NetWeaver HA cluster
           #---------------------------------------------------------------------
           listen ascs_healthcheck
             bind *:ASCS_HEALTHCHECK_PORT_NUM
           listen ers_healthcheck
             bind *:ERS_HEALTHCHECK_PORT_NUM
           

  4. After you save the changes, your `haproxy.cfg` file is similar to the following example:
         
         #---------------------------------------------------------------------
         defaults
            mode                    tcp
            log                     global
            option                  httplog
            option                  dontlognull
            option http-server-close
            option forwardfor       except 127.0.0.0/8
            option                  redispatch
            retries                 3
            timeout http-request    10s
            timeout queue           1m
            timeout connect         10s
            timeout client          1m
            timeout server          1m
            timeout http-keep-alive 10s
            timeout check           10s
            maxconn                 3000
         #---------------------------------------------------------------------
         # Health check listener port for SAP NW HA cluster
         #---------------------------------------------------------------------
         listen ascs_healthcheck
            bind *:62001
         listen ers_healthcheck
            bind *:62003

  5. On each host, as the root user, start the service to verify that it is correctly configured:
         
         systemctl start haproxy.service
         

  6. In the Google Cloud console, go to the **Load balancing** page:

[Go to load balancing](https://console.cloud.google.com/net-services/loadbalancing/list/loadBalancers)

  7. Click the load balancer that you created. You see the **Load balancer details** page.

If the `HAProxy` service is active on both hosts, then in the **Backend** section, the **Healthy** column of each instance group entry shows **1/1**.

  8. On each host, stop the `HAProxy` service:
         
         systemctl stop haproxy.service
         

After you stop the `HAProxy` service on each host, the **Healthy** column of each instance group shows **0/1**. Later, when you've configured the health check, the cluster restarts the listener on the master node.




### Create a health check resource

  1. On either host, as the root user, create and add ASCS health check resource to the ASCS group :
         
         pcs resource create rsc_haproxy_ascs service:haproxy op monitor interval=10s timeout=20s
         pcs resource group add <ASCS-GROUP-NAME> rsc_haproxy_ascs
         

  2. Create and add ERS health check resource to the ERS group:
         
         pcs resource create rsc_haproxy_ers service:haproxy op monitor interval=10s timeout=20s
         pcs resource group add <ERS-GROUP-NAME> rsc_haproxy_ers
         

  3. Delete the alias resource:
         
         pcs resource delete rsc_vip_rmk_ascs01_alias
         pcs resource delete rsc_vip_rmk_ers03_alias
         

  4. Take the cluster out of maintenance mode:
         
         pcs property set maintenance-mode=false
         




## Test the updated HA cluster

After completing the migration, verify that the internal passthrough Network Load Balancer is correctly steering traffic to the active node. You can perform this verification by using the following:

  * Check infrastructure health
  * Test network connectivity
  * Simulate a failover
  * Confirm lock entries are retained



### Check infrastructure health

  1. Identify the nodes that run the ASCS resource group and the standby node:
         
         pcs status

  2. Verify that Google Cloud correctly identifies the active and standby nodes:
         
         gcloud compute backend-services get-health BACKEND_SERVICE_NAME_ASCS \
            --region CLUSTER_REGION

The node that runs the ASCS resource group must show `healthState: HEALTHY`. The standby node must show `healthState: UNHEALTHY`.




### Test network connectivity

Confirm that the VIP is reachable through the load balancer from a remote node or the partner node, by completing the following steps:

  1. Test the ASCS health check port:
         
         nc -zv ASCS_VIP HEALTHCHECK_PORT_NUM_ASCS

The output must include `Connection succeeded`.

  2. Test the SAP Message Server Port (if SAP is started):
         
         nc -zv ASCS_VIP 36ASCS_INSTANCE_NO

The output must include `Connection succeeded`.




### Simulate a failover

To make sure that the load balancer automatically redirects traffic to the new primary node, simulate a failover event in your cluster by completing the following steps:

  1. Trigger failover by identifying the active ASCS node and bringing down the network interface on this node:
         
         sudo ip link set eth0 down

  2. Observe failover by monitoring `psc status`. The cluster detects the node failure, triggers fencing, and relocates the ASCS resource group to the partner node.

  3. Monitor the backend service health status:
         
         watch -d gcloud compute backend-services get-health BACKEND_SERVICE_NAME_ASCS \
            --region CLUSTER_REGION

Within 15–30 seconds, the previously `HEALTHY` node becomes `UNHEALTHY`, and the new active node becomes `HEALTHY`.




### Confirm lock entries are retained

To confirm lock entries are preserved across a failover, first select the tab for your version of the Enqueue Server and the follow the procedure to generate lock entries, simulate a failover, and confirm that the lock entries are retained after ASCS is activated again.

###  ENSA1 

  1. As `SID_LCadm`, on the server where ERS is active, generate lock entries by using the `enqt` program:
         
         > enqt pf=/PATH_TO_PROFILE/SID_ERSERS_INSTANCE_NUMBER_ERS_VIRTUAL_HOST_NAME 11 NUMBER_OF_LOCKS

  2. As `SID_LCadm`, on the server where ASCS is active, verify that the lock entries are registered:
         
         > sapcontrol -nr ASCS_INSTANCE_NUMBER -function EnqGetStatistic | grep locks_now

If you created 10 locks, your output is similar to the following example:
         
         locks_now: 10

  3. As `SID_LCadm`, on the server where ERS is active, start the monitoring function, `OpCode=20`, of the `enqt` program:
         
         > enqt pf=/PATH_TO_PROFILE/SID_ERSERS_INSTANCE_NUMBER_ERS_VIRTUAL_HOST_NAME 20 1 1 9999

For example:
         
         > enqt pf=/sapmnt/AHA/profile/AHA_ERS10_ers-aha-vip 20 1 1 9999

  4. Where ASCS is active, reboot the server.

On the monitoring server, by the time Pacemaker stops ERS to move it to the other server, your output is similar to the following:
         
         Number of selected entries: 10
         Number of selected entries: 10
         Number of selected entries: 10
         Number of selected entries: 10
         Number of selected entries: 10

  5. When the `enqt` monitor stops, exit the monitor by entering `Ctrl + c`.

  6. Optionally, as root on either server, monitor the cluster failover:
         
         # crm_mon

  7. As `SID_LCadm`, after you confirm the locks were retained, release the locks:
         
         > enqt pf=/PATH_TO_PROFILE/SID_ERSERS_INSTANCE_NUMBER_ERS_VIRTUAL_HOST_NAME 12 NUMBER_OF_LOCKS

  8. As `SID_LCadm`, on the server where ASCS is active, verify that the lock entries are removed:
         
         > sapcontrol -nr ASCS_INSTANCE_NUMBER -function EnqGetStatistic | grep locks_now




###  ENSA2 

  1. As `SID_LCadm`, on the server where ASCS is active, generate lock entries by using the `enq_adm` program:
         
         > enq_admin --set_locks=NUMBER_OF_LOCKS:X:DIAG::TAB:%u pf=/PATH_TO_PROFILE/SID_ASCSASCS_INSTANCE_NUMBER_ASCS_VIRTUAL_HOST_NAME

  2. As `SID_LCadm`, on the server where ASCS is active, verify that the lock entries are registered:
         
         > sapcontrol -nr ASCS_INSTANCE_NUMBER -function EnqGetStatistic | grep locks_now

If you created 10 locks, your output is similar to the following example:
         
         locks_now: 10

  3. Where ERS is active, confirm that the lock entries were replicated:
         
         > sapcontrol -nr ERS_INSTANCE_NUMBER -function EnqGetStatistic | grep locks_now

The number of returned locks must be the same as on the ASCS instance.

  4. Where ASCS is active, reboot the server.

  5. Optionally, as the root user, on either server, monitor the cluster failover:
         
         # crm_mon

  6. As `SID_LCadm`, on the server where ASCS was restarted, verify that the lock entries were retained:
         
         > sapcontrol -nr ASCS_INSTANCE_NUMBER -function EnqGetStatistic | grep locks_now

  7. As `SID_LCadm`, on the server where ERS is active, after you confirm the locks were retained, release the locks:
         
         > enq_admin --release_locks=NUMBER_OF_LOCKS:X:DIAG::TAB:%u pf=/PATH_TO_PROFILE/SID_ERSERS_INSTANCE_NUMBER_ERS_VIRTUAL_HOST_NAME

  8. As `SID_LCadm`, on the server where ASCS is active, verify that the lock entries are removed:
         
         > sapcontrol -nr ASCS_INSTANCE_NUMBER -function EnqGetStatistic | grep locks_now

Your output is similar to the following example:
         
         locks_now: 0




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
