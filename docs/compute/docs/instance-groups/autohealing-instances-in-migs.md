---
url: https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs/
title: Set up an application-based health check and autohealing \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:25:18.295577+00:00
---

# Set up an application-based health check and autohealing  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Set up an application-based health check and autohealing Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to set up an application-based health check to autoheal VMs in a managed instance group (MIG). It also describes how to do the following: use a health check without autohealing, remove a health check, view autohealing policy, and check the health state of each VM.

You can configure an application-based health check to verify that your application on a VM is responding as expected. If the health check that you configure detects that your application on a VM isn't responding, then the MIG marks that VM as _unhealthy_ and repairs it by default. Repairing a VM based on an application-based health check is called _autohealing_.

You can also turn off autohealing in a MIG so that you can use a health check without triggering the repairs for unhealthy VMs.

To know more about repairs in a MIG, see [About repairing VMs for high availability](https://docs.cloud.google.com/compute/docs/instance-groups/about-repair).

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### Terraform

To use the Terraform samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development). 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Pricing

When you set up an application-based health check, whenever a VM's health state changes, by default Compute Engine writes a log entry in [Cloud Logging](https://docs.cloud.google.com/logging). Cloud Logging provides a [free allotment per month](https://cloud.google.com/stackdriver/pricing) after which logging is priced by data volume. To avoid costs, you can [disable](https://docs.cloud.google.com/compute/docs/instance-groups/disabling-and-enabling-health-state-change-logs#disabling_health_state_change_logs) the health state change logs. 

## Set up an application-based health check and autohealing

To set up an application-based health check and autohealing in a MIG, you must do the following:

  1. Create a health check, if you haven't already.
  2. Configure an autohealing policy in the MIG to apply the health check.

**Tip:** Use separate health checks for load balancing and for autohealing. [Health checks for load balancing](https://docs.cloud.google.com/compute/docs/load-balancing/health-checks#create_a_health_check) detect unresponsive VMs and direct traffic away from them. Health checks for autohealing detect unhealthy VMs and proactively recreate those VMs, so this health check should be more conservative than a load balancing health check. For more information, see What makes a good autohealing health check.

### Create a health check

You can apply a single health check to a maximum of 50 MIGs. If you have more than 50 groups, create multiple health checks.

The following example shows how to create a health check for autohealing. You can create either a [regional](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks) or a [global](https://docs.cloud.google.com/compute/docs/reference/rest/v1/healthChecks) health check for autohealing in MIGs. In this example, you create a global health check that looks for a web server response on port `80`. To enable the health check probes to reach the web server, configure a firewall rule.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.healthChecks.create` on the project if creating a health check.
  * `compute.healthChecks.use` on the health check to use.
  * `compute.firewalls.create` on the project if creating a firewall.
  * `compute.networks.updatePolicy` on the network if creating a firewall.



The permissions are available in the following preconfigured [roles](https://docs.cloud.google.com/compute/docs/access/iam).

  * `compute.networkAdmin` for creating health checks.
  * `compute.securityAdmin` for configuring firewall rules to let health checking connect.



###  Console 

  1. Create a health check for autohealing that is more conservative than a [load balancing health check](https://docs.cloud.google.com/compute/docs/load-balancing/health-checks#create_a_health_check).

For example, create a health check that looks for a response on port `80` and that can tolerate some failure before it marks VMs as `UNHEALTHY` and causes them to be recreated. In this example, a VM is marked as healthy if the health check returns successfully once. The VM is marked as unhealthy if the health check returns unsuccessfully `3` consecutive times.

     1. In the Google Cloud console, go to the **Create a health check** page.

[Go to Create a health check](https://console.cloud.google.com/compute/healthChecksAdd)

     2. Give the health check a name, such as `example-check`.

     3. Select a **Scope**. You can select either **Regional** or **Global**. For this example, select **Global**.

     4. For **Protocol** , make sure that **HTTP** is selected.

     5. For **Port** , enter `80`.

     6. In the **Health criteria** section, provide the following values:

        1. For **Check interval** , enter `5`.
        2. For **Timeout** , enter `5`.
        3. Set a **Healthy threshold** to determine how many consecutive successful health checks must be returned before an unhealthy VM is marked as healthy. Enter `1` for this example.
        4. Set an **Unhealthy threshold** to determine how many consecutive unsuccessful health checks must be returned before a healthy VM is marked as unhealthy. Enter `3` for this example.
     7. Click **Create** to create the health check.

  2. Create a firewall rule to allow health check probes to connect to your app.

**Caution:** If health check probes are blocked by firewall rules, they mark your VMs as `UNHEALTHY` because they cannot connect to the app. This can prompt automatic recreation of VMs that may be healthy.

Health check [probes](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#method) come from addresses in the ranges `130.211.0.0/22` and `35.191.0.0/16`, so make sure your network firewall rules allow the health check to connect. For this example, the MIG uses the [`default`](https://docs.cloud.google.com/vpc/docs/vpc#default-network) network and its VMs are listening on port `80`. If port `80` is not already open on the default network, create a firewall rule.

     1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/networking/firewalls/add)

     2. Click **Create firewall rule**.

     3. Enter a **Name** for the firewall rule. For example, `allow-health-check`.

     4. For **Network** , select the `default` network.

     5. For **Targets** , select `All instances in the network`.

     6. For **Source filter** , select `IPv4 ranges`.

     7. For **Source IPv4 ranges** , enter `130.211.0.0/22` and `35.191.0.0/16`.

     8. In **Protocols and ports** , select **Specified protocols and ports** and do the following:

        1. Select **TCP**.
        2. In the **Ports** field, enter `80`.
     9. Click **Create**.




###  gcloud 

  1. Create a health check for autohealing that is more conservative than a [load balancing health check](https://docs.cloud.google.com/compute/docs/load-balancing/health-checks#create_a_health_check).

For example, create a health check that looks for a response on port `80` and that can tolerate some failure before it marks VMs as `UNHEALTHY` and causes them to be recreated. In this example, VM is marked as healthy if it returns successfully once. The VM is marked as unhealthy if it returns unsuccessfully `3` consecutive times. The following command creates a global health check.
         
         gcloud compute health-checks create http example-check --port 80 \
            --check-interval 30s \
            --healthy-threshold 1 \
            --timeout 10s \
            --unhealthy-threshold 3 \
            --global
         

**Note:** Use newer [health checks](https://docs.cloud.google.com/compute/docs/reference/latest/healthChecks), which support HTTP, HTTPS, TCP, and SSL (TLS) protocols. Legacy Compute Engine [HTTP](https://docs.cloud.google.com/compute/docs/reference/latest/httpHealthChecks) /[HTTPS](https://docs.cloud.google.com/compute/docs/reference/latest/httpsHealthChecks) health checks continue to work.
  2. Create a firewall rule to allow health check probes to connect to your app.

**Caution:** If health check probes are blocked by firewall rules, they mark your VMs as `UNHEALTHY` because they cannot connect to the app. This can prompt automatic recreation of VMs that might be healthy.

Health check [probes](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#method) come from addresses in the ranges `130.211.0.0/22` and `35.191.0.0/16`, so make sure your firewall rules allow the health check to connect. For this example, the MIG uses the [`default`](https://docs.cloud.google.com/vpc/docs/vpc#default-network) network, and its VMs listen on port `80`. If port `80` isn't already open on the default network, create a firewall rule.
         
         gcloud compute firewall-rules create allow-health-check \
             --allow tcp:80 \
             --source-ranges 130.211.0.0/22,35.191.0.0/16 \
             --network default
         




###  Terraform 

  1. Create a health check using the [`google_compute_http_health_check` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_http_health_check).

For example, create a health check that looks for a response on port `80` and that can tolerate some failure before it marks VMs as `UNHEALTHY` and causes them to be recreated. In this example, a VM is marked as healthy if it returns successfully once. The VM is marked as unhealthy if it returns unsuccessfully `3` consecutive times. The following request creates a global health check.
         
         resource "google_compute_http_health_check" "default" {
           name                = "example-check"
           timeout_sec         = 10
           check_interval_sec  = 30
           healthy_threshold   = 1
           unhealthy_threshold = 3
           port                = 80
         }

  2. Create a firewall using the [`google_compute_firewall` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_firewall).

**Caution:** If health check probes are blocked by firewall rules, they mark your VMs as `UNHEALTHY` because they cannot connect to the app. This can prompt automatic recreation of VMs that might be healthy.

Health check [probes](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#method) come from addresses in the ranges `130.211.0.0/22` and `35.191.0.0/16`, so make sure your firewall rules allow the health check to connect. For this example, the MIG uses the [`default`](https://docs.cloud.google.com/vpc/docs/vpc#default-network) network and its VMs are listening on port `80`. If port `80` is not already open on the default network, create a firewall rule.
         
         resource "google_compute_firewall" "default" {
           name          = "allow-health-check"
           network       = "default"
           source_ranges = ["130.211.0.0/22", "35.191.0.0/16"]
           allow {
             protocol = "tcp"
             ports    = [80]
           }
         }




To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  REST 

  1. Create a [health check](https://docs.cloud.google.com/compute/docs/load-balancing/health-checks#create_a_health_check) for autohealing that is more conservative than a load balancing health check.

For example, create a health check that looks for a response on port `80` and that can tolerate some failure before it marks VMs as `UNHEALTHY` and causes them to be recreated. In this example, a VM is marked as healthy if it returns successfully once. The VM is marked as unhealthy if it returns unsuccessfully `3` consecutive times. The following request creates a global health check.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/healthChecks
         
         {
          "name": "example-check",
          "type": "http",
          "port": 80,
          "checkIntervalSec": 30,
          "healthyThreshold": 1,
          "timeoutSec": 10,
          "unhealthyThreshold": 3
         }
         

**Note:** Use newer [health checks](https://docs.cloud.google.com/compute/docs/reference/latest/healthChecks), which support HTTP, HTTPS, TCP, and SSL (TLS) protocols. Legacy Compute Engine [HTTP](https://docs.cloud.google.com/compute/docs/reference/latest/httpHealthChecks) /[HTTPS](https://docs.cloud.google.com/compute/docs/reference/latest/httpsHealthChecks) health checks continue to work.
  2. Create a firewall rule to allow health check probes to connect to your app.

**Caution:** If health check probes are blocked by firewall rules, they mark your VMs as `UNHEALTHY` because they cannot connect to the app. This can prompt automatic recreation of VMs that might be healthy.

Health check [probes](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#method) come from addresses in the ranges `130.211.0.0/22` and `35.191.0.0/16`, so make sure your firewall rules allow the health check to connect. For this example, the MIG uses the [`default`](https://docs.cloud.google.com/vpc/docs/vpc#default-network) network and its VMs are listening on port `80`. If port `80` is not already open on the default network, create a firewall rule.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/firewalls
         
         {
          "name": "allow-health-check",
          "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/default",
          "sourceRanges": [
           "130.211.0.0/22",
           "35.191.0.0/16"
          ],
          "allowed": [
           {
            "ports": [
             "80"
            ],
            "IPProtocol": "tcp"
           }
          ]
         }
         

Replace `PROJECT_ID` with your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).




### Configure an autohealing policy in a MIG

In a MIG, you can set up only one autohealing policy to apply a health check.

Before configuring an autohealing policy, if you don't have a health check already, then create one. You can use either a [regional](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks) or a [global](https://docs.cloud.google.com/compute/docs/reference/rest/v1/healthChecks) health check for autohealing in MIGs. A regional health check reduce cross-region dependencies and help to achieve data residency whereas a global health check is convenient if you want to use the same health check for MIGs in multiple regions.

If you want to prevent inadvertently triggering autohealing while setting up a new health check or want to use a health check without autohealing, then see Configure health check without autohealing. You can also [turn off autohealing](https://docs.cloud.google.com/compute/docs/instance-groups/turn-off-vm-repairs-in-mig#turn_off_autohealing) after you configure a health check in the MIG.

To configure an autohealing policy, select one of the following options:

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.instanceGroupManagers.update` on the MIG.



The permissions are available in the following preconfigured [roles](https://docs.cloud.google.com/compute/docs/access/iam).

  * `compute.instanceAdmin.v1` for creating and updating autohealing policies in MIGs.



###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Under the **Name** column of the list, click the name of the MIG in which you want to apply the health check.

  3. Click **Edit** to modify this MIG. 

  4. Click **Instance lifecycle and autohealing** to expand the section. 
     1. In the **Autohealing** section, for the **Health check** , select a global or a regional health check.
     2. For the **Initial delay** , use the default value or modify as needed. 

The _initial delay_ is the number of seconds that a new VM takes to initialize and run its startup script. During a VM's initial delay period, the MIG ignores unsuccessful health checks because the VM might be in the startup process. This prevents the MIG from prematurely recreating a VM. If the health check receives a healthy response during the initial delay, it indicates that the startup process is complete and the VM is ready. The initial delay timer starts when the VM's `currentAction` field changes to `VERIFYING`. The timer stops when the set time completes or when a health check succeeds. The value of initial delay must be between `0` and `3600` seconds. In the console, the default value is `300` seconds. 

  5. Click **Save** to apply your changes.




###  gcloud 

To configure autohealing policy in an existing MIG, use the [`update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update). For example, use the following command to configure autohealing policy in an existing zonal MIG:
    
    
    gcloud compute instance-groups managed update MIG_NAME \
        --health-check HEALTH_CHECK_URL \
        --initial-delay INITIAL_DELAY \
        --zone ZONE
    

To configure autohealing policy when creating a MIG, use the [`create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create). For example, use the following command to configure autohealing policy when creating a zonal MIG:
    
    
    gcloud compute instance-groups managed create MIG_NAME \
        --size SIZE \
        --template INSTANCE_TEMPLATE_URL \
        --health-check HEALTH_CHECK_URL \
        --initial-delay INITIAL_DELAY \
        --zone ZONE
    

Replace the following:

  * `MIG_NAME`: the name of the MIG in which you want to set up autohealing.
  * `SIZE`: the number of VMs in the group.
  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you want to use to create instances in the MIG. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or name of the instance template. Specify one of the following values: 
    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`
    * For a global instance template: `INSTANCE_TEMPLATE_ID`
  * `HEALTH_CHECK_URL`: the partial URL of the health check that you want to set up for autohealing. For example: 
    * Regional health check: `projects/example-project/regions/us-central1/healthChecks/example-health-check`.
    * Global health check: `projects/example-project/global/healthChecks/example-health-check`.
  * `INITIAL_DELAY`: the number of seconds that a new VM takes to initialize and run its startup script. During a VM's initial delay period, the MIG ignores unsuccessful health checks because the VM might be in the startup process. This prevents the MIG from prematurely recreating a VM. If the health check receives a healthy response during the initial delay, it indicates that the startup process is complete and the VM is ready. The initial delay timer starts when the VM's `currentAction` field changes to `VERIFYING`. The timer stops when the set time completes or when a health check succeeds. The value of initial delay must be between `0` and `3600` seconds. The default value is `0`. 
  * `ZONE`: the zone where the MIG is located. For a regional MIG, use the `--region` flag.



###  Terraform 

To configure an autohealing policy in a MIG, use the `auto_healing_policies` block.

The following sample configures autohealing policy in a zonal MIG. For more information about the resource used in the sample, see [`google_compute_instance_group_manager`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance_group_manager). For a regional MIG, use the [`google_compute_region_instance_group_manager` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_instance_group_manager).
    
    
    resource "google_compute_instance_group_manager" "default" {
      name               = "igm-with-hc"
      base_instance_name = "test"
      target_size        = 3
      zone               = "us-central1-f"
      version {
        instance_template = google_compute_instance_template.default.id
        name              = "primary"
      }
      auto_healing_policies {
        health_check      = google_compute_http_health_check.default.id
        initial_delay_sec = 30
      }
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  REST 

To configure autohealing policy in an existing MIG, use the `patch` method as follows:

  * For a zonal MIG, use the [`instanceGroupManager.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patch).
  * For a regional MIG, use the [`regionInstanceGroupManager.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch).



For example, make the following call to set up autohealing in an existing zonal MIG:
    
    
      PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/MIG_NAME
      {
        "autoHealingPolicies": [
          {
            "healthCheck": "HEALTH_CHECK_URL",
            "initialDelaySec": INITIAL_DELAY
          }
        ]
      }
    

To configure autohealing policy when creating a MIG, use the `insert` method as follows:

  * For a zonal MIG, use the [`instanceGroupManager.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/insert).
  * For a regional MIG, use the [`regionInstanceGroupManager.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/insert).



For example, make the following call to configure autohealing policy when creating a zonal MIG:
    
    
      POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers
      {
        "name": "MIG_NAME",
        "targetSize": SIZE,
        "instanceTemplate": "INSTANCE_TEMPLATE_URL",
        "autoHealingPolicies": [
          {
            "healthCheck": "HEALTH_CHECK_URL",
            "initialDelaySec": INITIAL_DELAY
          }
        ]
      }
    

Replace the following:

  * `PROJECT_ID`: your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * `MIG_NAME`: the name of the MIG in which you want to set up autohealing.
  * `SIZE`: the number of VMs in the group.
  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you want to use to create instances in the MIG. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or name of the instance template. Specify one of the following values: 
    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`
    * For a global instance template: `INSTANCE_TEMPLATE_ID`
  * `HEALTH_CHECK_URL`: the partial URL of the health check that you want to set up for autohealing. For example: 
    * Regional health check: `projects/example-project/regions/us-central1/healthChecks/example-health-check`.
    * Global health check: `projects/example-project/global/healthChecks/example-health-check`.
  * `INITIAL_DELAY`: the number of seconds that a new VM takes to initialize and run its startup script. During a VM's initial delay period, the MIG ignores unsuccessful health checks because the VM might be in the startup process. This prevents the MIG from prematurely recreating a VM. If the health check receives a healthy response during the initial delay, it indicates that the startup process is complete and the VM is ready. The initial delay timer starts when the VM's `currentAction` field changes to `VERIFYING`. The timer stops when the set time completes or when a health check succeeds. The value of initial delay must be between `0` and `3600` seconds. The default value is `0`. 
  * `ZONE`: the zone where the MIG is located. For a regional MIG, use `regions/REGION` in the URL.



After the autohealing setup is complete, it can take 10 minutes before autohealing begins monitoring VMs in the group. After the monitoring begins, Compute Engine begins to mark VMs as healthy (or else recreates them) based on your autohealing configuration. For example, if you configure an initial delay of 5 minutes, a health check interval of 1 minute, and a healthy threshold of 1 check, the timeline looks like the following:

  * 10 minute delay before autohealing begins monitoring VMs in the group
  * \+ 5 minutes for the configured initial delay
  * \+ 1 minute for the check interval * healthy threshold (60s * 1)
  * = 16 minutes before the VM is either marked as healthy or is recreated



## Configure a health check without autohealing

You can turn off autohealing in a MIG and use the configured health check for monitoring your application health or you can implement your own repair logic. Turning off autohealing in a MIG doesn't affect the functioning of the health check. The health check continues to probe the application and provides the VM health states. However, the MIG will no longer repair unhealthy VMs.

To configure a health check without autohealing, select one of the following options.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.instanceGroupManagers.update` on the MIG.



The permissions are available in the following preconfigured [roles](https://docs.cloud.google.com/compute/docs/access/iam).

  * `compute.instanceAdmin.v1` for creating and updating autohealing policies in MIGs.



###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Under the **Name** column of the list, click the name of the MIG in which you want to apply the health check.

  3. Click **Edit** to modify this MIG. 

  4. Click **Instance lifecycle and autohealing** to expand the section. 
     1. In the **Autohealing** section, for the **Health check** , select a global or a regional health check.
     2. For the **Initial delay** , use the default value or modify as needed. 

The _initial delay_ is the number of seconds that a new VM takes to initialize and run its startup script. During a VM's initial delay period, the MIG ignores unsuccessful health checks because the VM might be in the startup process. This prevents the MIG from prematurely recreating a VM. If the health check receives a healthy response during the initial delay, it indicates that the startup process is complete and the VM is ready. The initial delay timer starts when the VM's `currentAction` field changes to `VERIFYING`. The timer stops when the set time completes or when a health check succeeds. The value of initial delay must be between `0` and `3600` seconds. In the console, the default value is `300` seconds. 

     1. In the **On failed health check** list, select **No action**.
  5. Click **Save** to apply your changes.




###  gcloud 

To configure a health check without autohealing, when you specify the health check configuration you must also set the `--action-on-vm-failed-health-check` flag to `do-nothing` as follows:

  * In an existing MIG, use the [`update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update).

For example, use the following command in an existing zonal MIG:
        
        gcloud compute instance-groups managed update MIG_NAME \
            --health-check HEALTH_CHECK_URL \
            --initial-delay INITIAL_DELAY \
            --action-on-vm-failed-health-check do-nothing \
            --zone ZONE
        

  * When creating a MIG, use the [`create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create).

For example, use the following command when creating a zonal MIG:
        
        gcloud compute instance-groups managed create MIG_NAME \
            --size SIZE \
            --template INSTANCE_TEMPLATE_URL \
            --health-check HEALTH_CHECK_URL \
            --initial-delay INITIAL_DELAY \
            --action-on-vm-failed-health-check do-nothing \
            --zone ZONE
        




Replace the following:

  * `MIG_NAME`: the name of the MIG in which you want to set up autohealing.
  * `SIZE`: the number of VMs in the group.
  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you want to use to create instances in the MIG. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or name of the instance template. Specify one of the following values: 
    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`
    * For a global instance template: `INSTANCE_TEMPLATE_ID`
  * `HEALTH_CHECK_URL`: the partial URL of the health check that you want to set up for autohealing. For example: 
    * Regional health check: `projects/example-project/regions/us-central1/healthChecks/example-health-check`.
    * Global health check: `projects/example-project/global/healthChecks/example-health-check`.
  * `INITIAL_DELAY`: the number of seconds that a new VM takes to initialize and run its startup script. During a VM's initial delay period, the MIG ignores unsuccessful health checks because the VM might be in the startup process. This prevents the MIG from prematurely recreating a VM. If the health check receives a healthy response during the initial delay, it indicates that the startup process is complete and the VM is ready. The initial delay timer starts when the VM's `currentAction` field changes to `VERIFYING`. The timer stops when the set time completes or when a health check succeeds. The value of initial delay must be between `0` and `3600` seconds. The default value is `0`. 
  * `ZONE`: the zone where the MIG is located. For a regional MIG, use the `--region` flag.



###  REST 

To configure a health check without autohealing, when you specify the health check configuration you must also set the `onFailedHealthCheck` field to `DO_NOTHING` as follows:

  * In an existing MIG, use the `patch` method as follows:

    * For a zonal MIG, use the [`instanceGroupManager.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patch).
    * For a regional MIG, use the [`regionInstanceGroupManager.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch).

For example, make the following call in an existing zonal MIG:
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/MIG_NAME
    {
      "autoHealingPolicies": [
        {
          "healthCheck": "HEALTH_CHECK_URL",
          "initialDelaySec": INITIAL_DELAY
        }
      ],
      "instanceLifecyclePolicy": {
        "onFailedHealthCheck": "DO_NOTHING"
      }
    }
    

  * When creating a MIG, use the `insert` method as follows:

    * For a zonal MIG, use the [`instanceGroupManager.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/insert).
    * For a regional MIG, use the [`regionInstanceGroupManager.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/insert).

For example, make the following call when creating a zonal MIG:
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers
    {
      "name": "MIG_NAME",
      "targetSize": SIZE,
      "instanceTemplate": "INSTANCE_TEMPLATE_URL",
      "autoHealingPolicies": [
        {
          "healthCheck": "HEALTH_CHECK_URL",
          "initialDelaySec": INITIAL_DELAY
        }
      ],
      "instanceLifecyclePolicy": {
        "onFailedHealthCheck": "DO_NOTHING"
      }
    }
    




Replace the following:

  * `PROJECT_ID`: your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * `MIG_NAME`: the name of the MIG in which you want to set up autohealing.
  * `SIZE`: the number of VMs in the group.
  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you want to use to create instances in the MIG. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or name of the instance template. Specify one of the following values: 
    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`
    * For a global instance template: `INSTANCE_TEMPLATE_ID`
  * `HEALTH_CHECK_URL`: the partial URL of the health check that you want to set up for autohealing. For example: 
    * Regional health check: `projects/example-project/regions/us-central1/healthChecks/example-health-check`.
    * Global health check: `projects/example-project/global/healthChecks/example-health-check`.
  * `INITIAL_DELAY`: the number of seconds that a new VM takes to initialize and run its startup script. During a VM's initial delay period, the MIG ignores unsuccessful health checks because the VM might be in the startup process. This prevents the MIG from prematurely recreating a VM. If the health check receives a healthy response during the initial delay, it indicates that the startup process is complete and the VM is ready. The initial delay timer starts when the VM's `currentAction` field changes to `VERIFYING`. The timer stops when the set time completes or when a health check succeeds. The value of initial delay must be between `0` and `3600` seconds. The default value is `0`. 
  * `ZONE`: the zone where the MIG is located. For a regional MIG, use `regions/REGION` in the URL.



After configuring the health check, you can monitor the VM health states to confirm that the health check is working as expected. If you want the MIG to repair unhealthy VMs, you can [turn on autohealing](https://docs.cloud.google.com/compute/docs/instance-groups/turn-off-vm-repairs-in-mig#set_a_mig_to_repair_failed_and_unhealthy_vms).

## Remove a health check

You can remove a health check configured in an autohealing policy as follows:

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click the name of the MIG from which you want to remove the health check.

  3. Click **Edit** to modify this MIG.

  4. Click **Instance lifecycle and autohealing** to expand the section.

  5. In **Autohealing** section, for **Health check** , select **No health check**.

  6. Click **Save** to apply the changes.




###  gcloud 

To remove the health check configuration in an autohealing policy, in the [`update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update) use the `--clear-autohealing` flag as follows:
    
    
    gcloud compute instance-groups managed update MIG_NAME \
        --clear-autohealing
    

Replace `MIG_NAME` with the name of a MIG.

###  REST 

To remove the health check configuration in an autohealing policy, set the autohealing policy to an empty value.

  * For a zonal MIG, use the [`instanceGroupManagers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patch)
  * For a regional MIG, use the [`regionInstanceGroupManagers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch)



For example, to remove health check in a zonal MIG, make the following request:
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/MIG_NAME
    
    {
      "autoHealingPolicies": [
        {}
      ]
    }
    

Replace the following:

  * `PROJECT_ID`: your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * `MIG_NAME`: the name of the MIG in which you want to set up autohealing.
  * `ZONE`: the zone where the MIG is located. For a regional MIG, use `regions/REGION`.



## View autohealing policy in a MIG

You can view the autohealing policy of a MIG as follows:

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click the name of the MIG of which you want to view the autohealing policy.

  3. Go to the **Details** tab.

The **VM instance lifecycle** section displays the health check and the initial delay configured in the autohealing policy.




###  gcloud 

To view the autohealing policy in a MIG, use the following command:
    
    
    gcloud compute instance-groups managed describe MIG_NAME \
        --format="(autoHealingPolicies)"
    

Replace `MIG_NAME` with the name of a MIG.

The following is a sample output: 
    
    
    autoHealingPolicies:
      healthCheck: https://www.googleapis.com/compute/v1/projects/example-project/global/healthChecks/example-health-check
      initialDelaySec: 300
    

###  REST 

To view the autohealing policy in a MIG, use the REST methods as follows:

  * For a zonal MIG, use the [`instanceGroupManagers.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/get)
  * For a regional MIG, use the [`regionInstanceGroupManagers.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/get)



For example, make the following request to view the autohealing policy in a zonal MIG:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/MIG_NAME
    

In the response body, check for the `autoHealingPolicies[]` object.

The following is a sample response:
    
    
    {
      ...
      "autoHealingPolicies": [
        {
          "healthCheck": "https://www.googleapis.com/compute/v1/projects/example-project/global/healthChecks/example-health-check",
          "initialDelaySec": 300
        }
      ],
      ...
    }
    

Replace the following:

  * `PROJECT_ID`: your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * `MIG_NAME`: the name of the MIG in which you want to set up autohealing.
  * `ZONE`: the zone where the MIG is located. For a regional MIG, use `regions/REGION`.



## Check the status

After you set up an application-based health check in a MIG, you can verify that a VM is running and its application is responding using the following ways:

  * Check whether VMs are healthy
  * Check the current actions on VMs
  * Check whether the MIG is stable



### Check whether VMs are healthy

If you have configured an application-based health check in your MIG, you can review the health state of each [managed instance](https://docs.cloud.google.com/compute/docs/instance-groups/working-with-managed-instances#what_is_a_managed_instance).

Inspect your managed instance health states to:

  * Identify unhealthy VMs that are not being repaired. A VM might not be repaired immediately even if it has been diagnosed as unhealthy in the following situations: 
    * The VM is still booting, and its initial delay has not passed.
    * A significant share of unhealthy instances is being repaired. The MIG delays further autohealing to ensure that the group keeps running a subset of instances.
  * Detect health check configuration errors. For example, you can detect misconfigured firewall rules or an invalid application health checking endpoint if the instance reports a health state of `TIMEOUT`.
  * Determine the initial delay value to configure by measuring the amount of time between when the VM transitions to a `RUNNING` [status](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle) and when the VM transitions to a `HEALTHY` health state. You can measure this gap by polling the [`list-instances`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/list-instances) method or by [observing the time](https://docs.cloud.google.com/compute/docs/instance-groups/monitoring-managed-instance-health-state-changes#determining_initial_delay_value_of_a_mig) between `instances.insert` operation and the first healthy signal received.



Use the [console](https://console.cloud.google.com/compute/instanceGroups), the [`gcloud`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/list-instances) command-line tool, or [REST](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/listManagedInstances) to view health states.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.instanceGroupManagers.get` on the MIG



###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups).

  2. Under the **Name** column of the list, click the name of the MIG that you want to examine. A page opens with the instance group properties and a list of VMs that are included in the group.

  3. If a VM is unhealthy, you can see its health state in the **Health check status** column.




###  gcloud 

Use the [`list-instances`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/list-instances) sub-command.
    
    
    gcloud compute instance-groups managed list-instances MIG_NAME
        --zone ZONE
    

The command gives an output similar to the following. The `HEALTH_STATE` field shows each VM's health state.
    
    
    NAME: igm-with-hc-fvz6
    ZONE: europe-west1-b
    STATUS: RUNNING
    HEALTH_STATE: HEALTHY
    ACTION: NONE
    INSTANCE_TEMPLATE: my-template
    VERSION_NAME:
    LAST_ERROR:
    
    NAME: igm-with-hc-gtz3
    ZONE: europe-west1-b
    STATUS: RUNNING
    HEALTH_STATE: HEALTHY
    ACTION: NONE
    INSTANCE_TEMPLATE: my-template
    VERSION_NAME:
    LAST_ERROR:
    

Replace the following:

  * `MIG_NAME`: the name of the MIG.
  * `ZONE`: the zone where the MIG is located. For a regional MIG, use `--region REGION`.



###  REST 

For a regional MIG, construct a `POST` request to the [`listManagedInstances`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/listManagedInstances) method:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/project-id/regions/region/instanceGroupManagers/MIG_NAME/listManagedInstances
    

For a zonal MIG, use the zonal MIG [`listManagedInstances`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/listManagedInstances) method:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/project-id/zones/zone/instanceGroupManagers/MIG_NAME/listManagedInstances
    

The request returns a response similar to the following, which includes an `instanceHealth` field for each managed instance.
    
    
    {
      "managedInstances": [
        {
          "instance": "https://www.googleapis.com/compute/v1/projects/sproject-id/zones/zone/instances/igm-with-hc-fvz6",
          "instanceStatus": "RUNNING",
          "currentAction": "NONE",
          "id": "6159431761228150698",
          "version": {
            "instanceTemplate": "https://www.googleapis.com/compute/v1/projects/project-id/global/instanceTemplates/my-template"
          },
          "instanceHealth": [
            {
              "healthCheck": "https://www.googleapis.com/compute/v1/projects/project-id/global/healthChecks/example-check-01",
              "detailedHealthState": "HEALTHY"
            }
          ],
          "name": "igm-with-hc-fvz6"
        },
        {
          "instance": "https://www.googleapis.com/compute/v1/projects/project-id/zones/zone/instances/igm-with-hc-gtz3",
          "instanceStatus": "RUNNING",
          "currentAction": "NONE",
          "id": "6622324799312181783",
          "version": {
            "instanceTemplate": "https://www.googleapis.com/compute/v1/projects/project-id/global/instanceTemplates/my-template"
          },
          "instanceHealth": [
            {
              "healthCheck": "https://www.googleapis.com/compute/v1/projects/project-id/global/healthChecks/example-check-01",
              "detailedHealthState": "HEALTHY"
            }
          ],
          "name": "igm-with-hc-gtz3"
        }
      ]
    }

#### Health states

The following VM health states are available:

  * `HEALTHY`: The VM is reachable, a connection to the application health checking endpoint can be established, and the response conforms to the requirements defined by the health check.
  * `DRAINING`: The VM is being drained. Existing connections to the VM have time to complete, but new connections are being refused.
  * `UNHEALTHY`: The VM is reachable, but does not conform to the requirements defined by the health check.
  * `TIMEOUT`: The VM is unreachable, a connection to the application health checking endpoint cannot be established, or the server on a VM does not respond within the specified timeout. For example, this may be caused by misconfigured [firewall rules](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges) or an overloaded server application on a VM.
  * `UNKNOWN`: The health checking system is not aware of the VM or its health is not known at the moment. It can take 10 minutes for monitoring to begin on new VMs in a MIG.



New VMs return an `UNHEALTHY` state until they are verified by the health checking system.

Whether a VM is repaired depends on its health state:

  * If a VM has a health state of `UNHEALTHY` or `TIMEOUT`, and it has passed its initialization period, then the MIG immediately attempts to repair it.
  * If a VM has a health state of `UNKNOWN`, then the MIG doesn't repair it immediately. This is to prevent an unnecessary repair of a VM for which the health checking signal is temporarily unavailable.



Autohealing attempts can be delayed if:

  * A VM remains unhealthy after multiple consecutive repairs.
  * A significant overall share of unhealthy VMs exists in the group.



We want to learn about your use cases, challenges, or feedback about VM health state values. You can share your feedback with our team at [mig-discuss@google.com](mailto:mig-discuss@google.com).

### Check current actions on VMs

When a MIG is in the process of creating a VM instance, the MIG sets that instance's read-only `currentAction` field to `CREATING`. If an autohealing policy is attached to the group, after the VM is created and running, the MIG sets the instance's current action to `VERIFYING` and the health checker begins to probe the VM's application. If the application passes this initial health check within the time that it takes for the application to start, then the VM is verified and the MIG changes the VM's `currentAction` field to `NONE`.

To check the current actions on VMs, see [View current actions on VMs](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#verify_instances).

### Check whether the MIG is stable

At the group level, Compute Engine populates a read-only field called [`status`](https://docs.cloud.google.com/compute/docs/reference/v1/regionInstanceGroupManagers#InstanceGroupManager.FIELDS.status) that contains an `isStable` flag.

If all VMs in the group are running and healthy (that is, the [`currentAction`](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#current_actions_on_instances) field for each managed instance is set to `NONE`), then the MIG sets the `status.isStable` field to `true`. Remember that the stability of a MIG depends on group configurations beyond the autohealing policy; for example, if your group is autoscaled, and if it is being scaled in or out, then the MIG sets the `status.isStable` field to `false` due to the autoscaler operation.

To check the values of your MIG's `status.isStable` field, see [Check whether a MIG is stable](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#verify_group).

## View historical autohealing operations

You can use the gcloud CLI or the REST to view past autohealing events.

###  gcloud 

Use the [`gcloud compute operations list`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/operations/list) command with a [filter](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters) to see only the autohealing repair events in your project.
    
    
    gcloud compute operations list --filter='operationType~compute.instances.repair.*'

For more information about a specific repair operation, use the [`describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/operations/describe) command. For example:
    
    
    gcloud compute operations describe repair-1539070348818-577c6bd6cf650-9752b3f3-1d6945e5 --zone us-east1-b

###  REST 

For regional MIGs, submit a `GET` request to the [`regionOperations`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionOperations/get) resource and include a filter to scope the output list to `compute.instances.repair.*` events.
    
    
    GET https://compute.googleapis.com/compute/v1/projects/project-id/region/region/operations?filter=operationType+%3D+%22compute.instances.repair.*%22
    

For zonal MIGs, use the [`zoneOperations`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/zoneOperations/get) resource.
    
    
    GET https://compute.googleapis.com/compute/v1/projects/project-id/zones/zone/operations?filter=operationType+%3D+%22compute.instances.repair.*%22
    

For more information about a specific repair operation, submit a `GET` request for that specific operation. For example:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/project-id/zones/zone/operations/repair-1539070348818-577c6bd6cf650-9752b3f3-1d6945e5
    

## What makes a good autohealing health check

Health checks used for autohealing should be conservative so they don't preemptively delete and recreate your instances. When an autohealer health check is too aggressive, the autohealer might mistake busy instances for failed instances and unnecessarily restart them, reducing availability.

  * `unhealthy-threshold`. Should be more than `1`. Ideally, set this value to `3` or more. This protects against rare failures like a network packet loss.
  * `healthy-threshold`. A value of `2` is sufficient for most apps.
  * `timeout`. Set this time value to a generous amount (five times or more than the expected response time). The timeout must be less than or equal to the `check-interval`. This protects against unexpected delays like busy instances or a slow network connection.
  * `check-interval`. This value should be between 1 second and two times the timeout (not too long nor too short). When a value is too long, a failed instance is not caught soon enough. When a value is too short, the instances and the network can become measurably busy, given the high number of health check probes being sent every second.



## Potential causes for delays in autohealing

To maintain the stability of your MIG during autohealing, Compute Engine applies the following limits. Due to these limits, you might see delays in autohealing.

  * **Maximum concurrent repairs:** When instances in a MIG fail health checks, the MIG attempts to autoheal a maximum of 30% of the instances in each zone (rounded up) at any given time. For example, if a zonal MIG has 10 VMs and 4 of them fail health checks, then the MIG attempts to repair at most 3 VMs (30% of 10 VMs). If it is a regional MIG, then the MIG attempts to repair at most 30% of the instances in each zone where VMs have failed—for example, if you have 3 instances in a zone, then the MIG can repair at most 1 instance in that zone.

  * **Delay between subsequent repair attempts:** If an instance repeatedly fails the health check after being autohealed, then the MIG gradually increases the time between subsequent repair attempts. This delay can extend to a maximum of about 60 minutes between retries.




## What's next

  * Try the tutorial, [Using autohealing for highly available apps](https://docs.cloud.google.com/compute/docs/tutorials/high-availability-autohealing).
  * [Monitor VM health state changes](https://docs.cloud.google.com/compute/docs/instance-groups/monitoring-managed-instance-health-state-changes).
  * [Apply configuration updates during repairs](https://docs.cloud.google.com/compute/docs/instance-groups/update-on-repair).
  * [Turn on repairs or autohealing](https://docs.cloud.google.com/compute/docs/instance-groups/turn-off-vm-repairs-in-mig#set_a_mig_to_repair_failed_and_unhealthy_vms), if you've turned off autohealing.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
