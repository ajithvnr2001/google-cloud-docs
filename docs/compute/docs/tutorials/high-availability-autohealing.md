---
url: https://docs.cloud.google.com/compute/docs/tutorials/high-availability-autohealing/
title: Using autohealing for highly available apps \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:17.083359+00:00
---

# Using autohealing for highly available apps  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/tutorials/high-availability-autohealing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Using autohealing for highly available apps Stay organized with collections  Save and categorize content based on your preferences. 

This interactive tutorial shows how to use [autohealing](https://docs.cloud.google.com/compute/docs/instance-groups#autohealing) to build highly available apps on Compute Engine.

Highly available apps are designed to serve clients with minimal latency and downtime. Availability is compromised when an app crashes or freezes. Clients of a compromised app can experience high latency or downtime.

Autohealing lets you automatically restart apps that are compromised. It promptly detects failed virtual machine (VM) instances and recreates them automatically, so clients can be served again. With autohealing, you no longer need to manually bring an app back to service after a failure.

## Objectives

  * Configure a health check and an autohealing policy.
  * Set up a demo web service on a managed instance group (MIG).
  * Simulate health check failures and witness the autohealing recovery process.



## Costs

This tutorial uses billable components of Google Cloud including: 

  * Compute Engine



## Before you begin

Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

[Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

Enable the Compute Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com)

In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

[Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

Enable the Compute Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com)




If you prefer to work from the command line, install the Google Cloud CLI.

  * [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  * If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  * To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
        
        gcloud init

**Note:** You can run the gcloud CLI in the Google Cloud console without installing the Google Cloud CLI. To run the gcloud CLI in the Google Cloud console, [use Cloud Shell](https://console.cloud.google.com/?cloudshell=true). 



## App architecture

The app includes the following Compute Engine components:

  * [Health check](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts): An HTTP health check policy used by the autohealer to detect failed VM.
  * [Firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls): Google Cloud firewall rules let you allow or deny traffic to your VMs.
  * [Managed instance group](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups): A group of VMs running the same demo web service.
  * [Instance template](https://docs.cloud.google.com/compute/docs/instance-templates): A template used to create each VM in the instance group.



![System architecture for a health check and an instance group.](https://docs.cloud.google.com/static/compute/docs/tutorials/images/high-availability-autohealing-architecture.png)

### How the health check probes the demo webservice

A health check sends probe requests to a VM using a specified protocol, such as HTTP(S), SSL, or TCP. For more information, see [how health checks work](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#method) and [health check categories, protocols, and ports](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#categories_protocols_ports).

The health check in this tutorial is an HTTP health check that probes the HTTP path `/health` on port 80. For an HTTP health check, the probe request passes only if the path returns an `HTTP 200 (OK)` response. For this tutorial, the demo web server defines the path `/health` to return an `HTTP 200 (OK)` response when healthy or an `HTTP 500 (Internal Server Error)` response when unhealthy. For more information, see [success criteria for HTTP, HTTPS, and HTTP/2](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#criteria-protocol-http).

## Create the health check

To set up autohealing, create a custom health check and configure the network firewall to allow health check probes.

In this tutorial, you create a regional health check. For autohealing, you can use either a [regional](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks) or a [global](https://docs.cloud.google.com/compute/docs/reference/rest/v1/healthChecks) health check. Regional health checks reduce cross-region dependencies and help to achieve data residency. Global health checks are convenient if you want to use the same health check for MIGs in multiple regions.

**Pro Tip:** Use separate health checks for load balancing and for [autohealing](https://docs.cloud.google.com/compute/docs/instance-groups#autohealing). Health checks for load balancing detect unresponsive VMs and direct traffic away from them. Health checks for autohealing detect and recreate failed VMs, so they should be less aggressive than load balancing health checks. Using the same health check for these services would remove the distinction between unresponsive VMs and failed VMs, causing unnecessary latency and unavailability for your users.   
For more information, see What makes a good autohealing health check. 

### Console

  1. Create a health check.

     1. In the Google Cloud console, go to the **Create health check** page.

[Go to Create health check](https://console.cloud.google.com/compute/healthChecksAdd)

     2. In the **Name** field, enter `autohealer-check`.

     3. Set the **Scope** to `Regional`.

     4. In the **Region** drop-down, select `europe-west1`.

     5. For **Protocol** select `HTTP`.

     6. Set **Request path** to `/health`. This indicates what HTTP path the health check uses. For this tutorial, the demo web server defines the path `/health` to return either an `HTTP 200 (OK)` response when healthy or an `HTTP 500 (Internal Server Error)` response when unhealthy.

     7. Set the **Health criteria** :

        1. Set **Check interval** to `10`. This defines the amount of time from the start of one probe to the start of the next one.
        2. Set **Timeout** to `5`. This defines the amount of time that Google Cloud waits for a response to a probe. This value must be less than or equal to the check interval.
        3. Set **Healthy threshold** to `2`. This defines the number of sequential probes that must succeed for the VM to be considered healthy.
        4. Set **Unhealthy threshold** to `3`. This defines the number of sequential probes that must fail for the VM to be considered unhealthy.
     8. Leave default values for the other options.

     9. Click **Create** at the bottom.

  2. Create a firewall rule to allow health check probes to make HTTP requests.

     1. In the Google Cloud console, go to the **Create firewall rule** page.

[Go to Create firewall rule](https://console.cloud.google.com/networking/firewalls/add)

     2. For **Name** , enter `default-allow-http-health-check`.

     3. For **Network** , select `default`.

     4. For **Targets** , select `All instances in the network`.

     5. For **Source filter** , select `IPv4 ranges`.

     6. For **Source IPv4 ranges** , enter `130.211.0.0/22, 35.191.0.0/16`.

**Note:** Health check probes come from addresses in the ranges `130.211.0.0/22` and `35.191.0.0/16`. For this tutorial, your health check uses the `HTTP` protocol, so make sure the firewall rule allows connections to port 80. For more information, see [setting up health checking and autohealing for managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs).
     7. In **Protocols and ports** , select **TCP** and enter `80`.

     8. Leave default values for the other options.

     9. Click **Create**.




### gcloud

  1. Create a health check using the [`health-checks create http` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/http).
         
         gcloud compute health-checks create http autohealer-check \
             --region europe-west1 \
             --check-interval 10 \
             --timeout 5 \
             --healthy-threshold 2 \
             --unhealthy-threshold 3 \
             --request-path "/health"
         

     * `check-interval` defines the amount of time from the start of one probe to the start of the next one.
     * `timeout` defines the amount of time that Google Cloud waits for a response to a probe. This value must be less than or equal to the check interval.
     * `healthy-threshold` defines the number of sequential probes that must succeed for the VM to be considered healthy.
     * `unhealthy-threshold` defines the number of sequential probes that must fail for the VM to be considered unhealthy.
     * `request-path` indicates what HTTP path the health check uses. For this tutorial, the demo web server defines the path `/health` to return either an `HTTP 200 (OK)` response when healthy or an `HTTP 500 (Internal Server Error)` response when unhealthy.
  2. Create a firewall rule to allow health check probes to make HTTP requests.
         
         gcloud compute firewall-rules create default-allow-http-health-check \
             --network default \
             --allow tcp:80 \
             --source-ranges 130.211.0.0/22,35.191.0.0/16
         

**Note:** Health check probes come from addresses in the ranges `130.211.0.0/22` and `35.191.0.0/16`. For this tutorial, your health check uses the `HTTP` protocol, so make sure the firewall rule allows connections to port 80. For more information, see [setting up health checking and autohealing for managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs).



### What makes a good autohealing health check

Health checks used for autohealing should be conservative so they don't preemptively delete and recreate your instances. When an autohealer health check is too aggressive, the autohealer might mistake busy instances for failed instances and unnecessarily restart them, reducing availability.

  * `unhealthy-threshold`. Should be more than `1`. Ideally, set this value to `3` or more. This protects against rare failures like a network packet loss.
  * `healthy-threshold`. A value of `2` is sufficient for most apps.
  * `timeout`. Set this time value to a generous amount (five times or more than the expected response time). The timeout must be less than or equal to the `check-interval`. This protects against unexpected delays like busy instances or a slow network connection.
  * `check-interval`. This value should be between 1 second and two times the timeout (not too long nor too short). When a value is too long, a failed instance is not caught soon enough. When a value is too short, the instances and the network can become measurably busy, given the high number of health check probes being sent every second.



## Set up the web service

This tutorial uses a web app that is stored on GitHub. If you would like learn more about how the app was implemented, see the [GoogleCloudPlatform/python-docs-samples](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/compute/managed-instances/demo) GitHub repository.

To set up the demo web service, create an instance template that launches the demo web server on startup. Then, use this instance template to deploy a managed instance group and enable autohealing.

### Console

  1. Create an instance template. Include a startup script that starts up the demo web server.

     1. In the Google Cloud console, go to the **Create instance template** page.

[Go to Create instance template](https://console.cloud.google.com/compute/instanceTemplates/add)

     2. Set the **Name** to `webserver-template`.

     3. In the **Location** section, from the **Region** drop-down, select **europe-west1**.

     4. In the **Machine configuration** section, for the **Machine type** drop-down, select **e2-medium**.

     5. In the **Firewall** section, select the **Allow HTTP traffic** checkbox.

     6. Expand the **Advanced options** section to reveal advanced settings. Several sub-sections appear.

     7. In the **Management** section, find **Automation** and enter the following **Startup script** : 
            
            apt-get update
            apt-get -y install git python3-pip python3-venv
            git clone https://github.com/GoogleCloudPlatform/python-docs-samples.git
            python3 -m venv venv
            ./venv/bin/pip3 install -Ur ./python-docs-samples/compute/managed-instances/demo/requirements.txt
            ./venv/bin/pip3 install gunicorn
            ./venv/bin/gunicorn --bind 0.0.0.0:80 app:app --daemon --chdir ./python-docs-samples/compute/managed-instances/demo
            

     8. Leave default values for the other options.

     9. Click **Create**.

  2. Deploy the web server as a managed instance group.

     1. In the Google Cloud console, go to the **Create instance group** page.

[Go to Create instance group](https://console.cloud.google.com/compute/instanceGroups/add)

     2. Set the **Name** to `webserver-group`.

     3. For **Instance template** , select `webserver-template`.

     4. For **Region** , select `europe-west1`.

     5. For **Zone** , select `europe-west1-b`.

     6. In the **Autoscaling** section, for **Autoscaling mode** , select **Off: do not autoscale**.

     7. Scroll back to the **Number of instances** field and set it to `3`.

     8. In the **Autohealing** section, do the following:

        1. In the **Health check** drop-down, select `autohealer-check`.
        2. Set **Initial delay** to `300`.

**Note:** The _initial delay_ is the number of seconds that a new VM takes to initialize and run its startup script. During a VM's initial delay period, the MIG ignores unsuccessful health checks because the VM might be in the startup process. This prevents the MIG from prematurely recreating a VM. If the health check receives a healthy response during the initial delay, it indicates that the startup process is complete and the VM is ready. The initial delay timer starts when the VM's `currentAction` field changes to `VERIFYING`. The timer stops when the set time completes or when a health check succeeds. The value of initial delay must be between `0` and `3600` seconds. In the console, the default value is `300` seconds. 
     9. Leave default values for the other options.

     10. Click **Create**.

  3. Create a firewall rule that allows HTTP requests to the web servers.

     1. In the Google Cloud console, go to the **Create firewall rule** page.

[Go to Create firewall rule](https://console.cloud.google.com/networking/firewalls/add)

     2. For **Name** , enter `default-allow-http`.

     3. For **Network** , select `default`.

     4. For **Targets** , select `Specified target tags`.

     5. For **Target Tags** , enter `http-server`.

     6. For **Source filter** , select `IPv4 ranges`.

     7. For **Source IPv4 ranges** , enter `0.0.0.0/0` to allow access for all IP addresses.

     8. In **Protocols and ports** , select **TCP** and enter `80`.

     9. Leave default values for the other options.

     10. Click **Create**.




### gcloud

  1. Create an instance template. Include a startup script that starts the demo web server.
         
         gcloud compute instance-templates create webserver-template \
             --instance-template-region europe-west1 \
             --machine-type e2-medium \
             --tags http-server \
             --metadata startup-script='
           apt-get update
           apt-get -y install git python3-pip python3-venv
           git clone https://github.com/GoogleCloudPlatform/python-docs-samples.git
           python3 -m venv venv
           ./venv/bin/pip3 install -Ur ./python-docs-samples/compute/managed-instances/demo/requirements.txt
           ./venv/bin/pip3 install gunicorn
           ./venv/bin/gunicorn --bind 0.0.0.0:80 app:app --daemon --chdir ./python-docs-samples/compute/managed-instances/demo'
         

  2. Create a managed instance group.
         
         gcloud compute instance-groups managed create webserver-group \
             --zone europe-west1-b \
             --template projects/PROJECT_ID/regions/europe-west1/instanceTemplates/webserver-template \
             --size 3 \
             --health-check projects/PROJECT_ID/regions/europe-west1/healthChecks/autohealer-check \
             --initial-delay 300
         

**Note:** The _initial delay_ is the number of seconds that a new VM takes to initialize and run its startup script. During a VM's initial delay period, the MIG ignores unsuccessful health checks because the VM might be in the startup process. This prevents the MIG from prematurely recreating a VM. If the health check receives a healthy response during the initial delay, it indicates that the startup process is complete and the VM is ready. The initial delay timer starts when the VM's `currentAction` field changes to `VERIFYING`. The timer stops when the set time completes or when a health check succeeds. The value of initial delay must be between `0` and `3600` seconds. The default value is `0`. 
  3. Create a firewall rule that allows HTTP requests to the web servers.
         
         gcloud compute firewall-rules create default-allow-http \
             --network default \
             --allow tcp:80 \
             --target-tags http-server
         




Wait a few minutes for the managed instance group to create and verify its VMs.

**Note:** If your health checks fail, your VMs may be taking longer to initialize than expected. Consider adjusting your initial delay: 

  1. In the Google Cloud console, go to the **Instance groups** page.
  2. Click `webserver-group`.
  3. Click **Edit**.
  4. Under **Initialization period** , increase the number of seconds. You may input a number from 0 to 3600.
  5. Click **Save** and wait for the managed instance group to update.



## Simulate health check failures

To simulate health check failures, the demo web server provides ways for you to force a health check failure.

### Console

  1. Navigate to a web server VM.

     1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

     2. For any `webserver-group` VM, under the **External IP** column, click the IP address. A new tab opens in your web browser. If the request times out or the web page is not available, wait a minute to let the server finish setting up and try again.

The demo web server displays a page similar to the following:

![Demo web page showing green status buttons and blue action buttons.](https://docs.cloud.google.com/static/compute/docs/tutorials/images/high-availability-webserver-demo.png)

  2. On the demo web page, click **Make unhealthy**.

This causes the web server to fail the health check. Specifically, the web server makes the `/health` path return an `HTTP 500 (Internal Server Error)`. You can verify this yourself by quickly clicking the **Check health** button (this stops working after the autohealer has started rebooting the VM).

  3. Wait for the autohealer to take action.

     1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

     2. Wait for the status of the web server VM to change. The green checkmark next to the VM name should change to a grey square, indicating that the autohealer has started rebooting the unhealthy VM.

     3. Click **Refresh** at the top of the page periodically to get the most recent status.

     4. The autohealing process is finished when the grey square changes back to a green checkmark, indicating the VM is healthy again.




### gcloud

  1. Monitor the status of the managed instance group. (When you have finished, stop by pressing `Ctrl+C`.)
         
         while : ; do
           gcloud compute instance-groups managed list-instances webserver-group \
           --zone europe-west1-b
           sleep 5  # Wait for 5 seconds
         done
         
         
         NAME: webserver-group-0zx6
           ZONE: europe-west1-b
           STATUS: RUNNING
           HEALTH_STATE: HEALTHY
           ACTION: NONE
           INSTANCE_TEMPLATE: webserver-template
           VERSION_NAME:
           LAST_ERROR:
         
           NAME: webserver-group-4qbx
           ZONE: europe-west1-b
           STATUS: RUNNING
           HEALTH_STATE: HEALTHY
           ACTION: NONE
           INSTANCE_TEMPLATE: webserver-template
           VERSION_NAME:
           LAST_ERROR:
         
           NAME: webserver-group-m5v5
           ZONE: europe-west1-b
           STATUS: RUNNING
           HEALTH_STATE: HEALTHY
           ACTION: NONE
           INSTANCE_TEMPLATE: webserver-template
           VERSION_NAME:
           LAST_ERROR:
         

All VMs in the group must show `STATUS: RUNNING` and `ACTION: NONE`. If not, wait a few minutes to let the VMs finish setting up and try again.

  2. Open a new Cloud Shell session with the Google Cloud CLI installed.

**Note:** If you're using Cloud Shell, you can [open multiple sessions](https://docs.cloud.google.com/shell/docs/starting-cloud-shell#opening_multiple_sessions).
  3. Get the address of a web server VM.
         
         gcloud compute instances list --filter webserver-group
         

Under the `EXTERNAL_IP` column, copy the IP address of any web server VM and save it as a local bash variable.
         
         export IP_ADDRESS=EXTERNAL_IP_ADDRESS
         

  4. Verify the web server has finished setting up. The server returns an `HTTP 200 OK` response.
         
         curl --head $IP_ADDRESS/health
         
         
         HTTP/1.1 200 OK
         Server: gunicorn
         ...
         

If you get a `Connection refused` error, wait a minute to let the server finish setting up and try again.

  5. Make the web server unhealthy.
         
         curl $IP_ADDRESS/makeUnhealthy > /dev/null
         

This causes the web server to fail the health check. Specifically, the web server makes the `/health` path return an `HTTP 500 INTERNAL SERVER ERROR`. You can verify this yourself by quickly making a request to `/health` (this stops working after the autohealer has started rebooting the VM).
         
         curl --head $IP_ADDRESS/health
         
         
         HTTP/1.1 500 INTERNAL SERVER ERROR
         Server: gunicorn
         ...
         

  6. Return to your first shell session to monitor the managed instance group and wait for the autohealer to take action.

     1. When the autohealing process has started, the `STATUS` and `ACTION` columns update, indicating that the autohealer has started rebooting the unhealthy VM.
            
            NAME: webserver-group-0zx6
              ZONE: europe-west1-b
              STATUS: STOPPING
              HEALTH_STATE: UNHEALTHY
              ACTION: RECREATING
              INSTANCE_TEMPLATE: webserver-template
              VERSION_NAME:
              LAST_ERROR:
            
              ...
            

     2. The autohealing process has finished when the VM again reports a `STATUS` of `RUNNING` and an `ACTION` of `NONE`, indicating the VM is successfully restarted.
            
            NAME: webserver-group-0zx6
              ZONE: europe-west1-b
              STATUS: RUNNING
              HEALTH_STATE: HEALTHY
              ACTION: NONE
              INSTANCE_TEMPLATE: webserver-template
              VERSION_NAME:
              LAST_ERROR:
            
              ...
            

     3. When you have finished monitoring the managed instance group, stop by pressing `Ctrl+C`.

**Note:** For more information about possible VM statuses and actions, see [Instance life cycle](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle) and [Current actions on instances](https://docs.cloud.google.com/compute/docs/instance-groups/updating-managed-instance-groups#current_actions_on_instances).



Feel free to repeat this exercise. Here are some ideas:

  * What happens if you make all VMs unhealthy at one time? For more information about autohealing behavior during concurrent failures, see [autohealing behavior](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs#autohealing_behavior).

  * Can you update the health check configuration to heal VMs as fast as possible? (In practice, you should set the health check parameters to use conservative values as explained in this tutorial. Otherwise, you may risk VMs being mistakenly deleted and restarted when there is no real problem.)

  * The managed instance group has an `initial delay` configuration setting. Can you determine the minimum delay needed for this demo web server? (In practice, you should set the delay to somewhat longer (10%–20%) than it takes for a VM to boot and start serving app requests. Otherwise, you risk the VM getting stuck in an autohealing boot loop.)




## View autohealer history (optional)

To view a history of autohealer operations use the following `gcloud` command:
    
    
    gcloud compute operations list --filter='operationType~compute.instances.repair.*'
    

For more information, see [viewing historical autohealing operations](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs#viewing_historical_autohealing_operations)

## Clean up

After you finish the tutorial, you can clean up the resources that you created so that they stop using quota and incurring charges. The following sections describe how to delete or turn off these resources. 

If you created a separate project for this tutorial, delete the entire project. Otherwise, if the project has resources that you want to keep, only delete the specific resources created in this tutorial.

### Deleting the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Deleting specific resources

If you can't delete the project used for this tutorial, delete the tutorial resources individually.

#### Deleting the instance group

### console

  1. In the Google Cloud console, go to the **Instance groups** page. 

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups/list)

  2. Select the checkbox for your `webserver-group` instance group. 
  3. To delete the instance group, click delete **Delete**. 



### gcloud
    
    
    gcloud compute instance-groups managed delete webserver-group --zone europe-west1-b -q
    

#### Deleting the instance template

**Note:** You must delete the managed instance group before deleting the instance template. You can't delete an instance template if a managed instance group uses it.

### console

  1. In the Google Cloud console, go to the **Instance templates** page.

[Go to Instance templates](https://console.cloud.google.com/compute/instanceTemplates)

  2. Click the checkbox next to the instance template.

  3. Click delete **Delete** at the top of the page. In the new window, click **Delete** to confirm the deletion.




### gcloud
    
    
    gcloud compute instance-templates delete webserver-template -q \
        --region=europe-west1
    

#### Deleting the health check

**Note:** You must delete the managed instance group before deleting the health check. You can't delete a health check if other resources use it.

### console

  1. In the Google Cloud console, go to the **Health checks** page.

[Go to Health checks](https://console.cloud.google.com/compute/healthChecks)

  2. Click the checkbox next to the health check.

  3. Click delete **Delete** at the top of the page. In the new window, click **Delete** to confirm the deletion.




### gcloud
    
    
    gcloud compute health-checks delete autohealer-check -q \
        --region=europe-west1
    

#### Deleting the firewall rules

### console

  1. In the Google Cloud console, go to the **Firewall rules** page.

[Go to Firewall rules](https://console.cloud.google.com/networking/firewalls)

  2. Click the checkboxes next to the firewall rules named `default-allow-http` and `default-allow-http-health-check`.

  3. Click delete **Delete** at the top of the page. In the new window, click **Delete** to confirm the deletion.




### gcloud
    
    
    gcloud compute firewall-rules delete default-allow-http default-allow-http-health-check -q
    

## What's next

  * Try another tutorial: 
    * [Using load balancing for highly available applications](https://docs.cloud.google.com/compute/docs/tutorials/high-availability-load-balancing).
    * [Using autoscaling for highly scalable applications](https://docs.cloud.google.com/compute/docs/tutorials/high-scalability-autoscaling).
  * Learn more about [managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups).
  * Learn more about [designing robust systems](https://docs.cloud.google.com/compute/docs/tutorials/robustsystems).
  * Learn more about [building scalable and resilient web apps on Google Cloud](https://docs.cloud.google.com/solutions/scalable-and-resilient-apps).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
