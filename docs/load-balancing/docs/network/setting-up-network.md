---
url: https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network/
title: Set up a regional external passthrough Network Load Balancer with a target pool \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:31.817420+00:00
---

# Set up a regional external passthrough Network Load Balancer with a target pool  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Set up a regional external passthrough Network Load Balancer with a target pool Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This guide provides instructions for creating a target pool-based regional external passthrough Network Load Balancer. We recommend using a backend service-based regional external passthrough Network Load Balancer instead. For more information, see [Backend service-based regional external passthrough Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service).

The example assumes that you have multiple web servers running on Compute Engine instances, and balances new TCP connections among them. This example uses a legacy HTTP health check so that new connections are only sent to healthy backend VMs.

Before you start, read [Regional external passthrough Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/network) for conceptual information about regional external passthrough Network Load Balancers.

## Before you begin

Install the Google Cloud CLI. For a complete overview of the tool, see the [gcloud Tool Guide](https://docs.cloud.google.com/sdk/gcloud). You can find commands related to load balancing in the [`gcloud compute`](https://docs.cloud.google.com/sdk/gcloud/reference/compute) command group.

You can also get detailed help for any `gcloud` command by using the `--help` flag:
    
    
    gcloud compute http-health-checks create --help
    

If you haven't run the Google Cloud CLI previously, first run [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) to authenticate. 

In addition, you must create a static external IP address for the load balancer. If you are using an image provided by Compute Engine, your virtual machine (VM) instances are automatically configured to handle this IP address. If you are using any other image, you will have to configure this address as an alias on eth0 or as a loopback on each instance.

This guide assumes that you are familiar with [bash](https://en.wikipedia.org/wiki/Bash_\(Unix_shell\)).

## Configuring Compute Engine VM instances

For this load balancing scenario, you will create three Compute Engine VM instances and install Apache on them. You will add a firewall rule that allows HTTP traffic to reach the instances.

Instances that participate as backend VMs for regional external passthrough Network Load Balancers must be running the appropriate [Linux Guest Environment](https://docs.cloud.google.com/compute/docs/instances/linux-guest-environment), [Windows Guest Environment](https://github.com/GoogleCloudPlatform/compute-image-windows), or other processes that provide equivalent functionality.

### Setting up the backend instances

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click **Create instance**.

  3. Set **Name** to `www1`.

  4. Set the **Region** to **us-central1**.

  5. Set the **Zone** to **us-central1-b**.

  6. Under **Boot disk** , the default OS image of **Debian GNU/Linux 12 (bookworm)** is already selected.

  7. Click **Advanced options**.

  8. Click **Networking** and configure the following field:

     1. For **Network tags** , enter `network-lb-tag`.
  9. Click **Management**. Enter the following script into the **Startup script** field.
         
         #! /bin/bash
          sudo apt-get update
          sudo apt-get install apache2 -y
          sudo service apache2 restart
          echo '<!doctype html><html><body><h1>www1</h1></body></html>' | tee /var/www/html/index.html
          

     1. Click **Create**.
  10. Create an instance named `www2` with the same settings, except with the following script inserted into the **Automation** , **Startup script** field. 
         
         #! /bin/bash
           sudo apt-get update
           sudo apt-get install apache2 -y
           sudo service apache2 restart
           echo '<!doctype html><html><body><h1>www2</h1></body></html>' | tee /var/www/html/index.html
          

  11. Create an instance named `www3` with the same settings, except with the following script inserted into the **Automation** , **Startup script** field. 
         
         #! /bin/bash
             sudo apt-get update
             sudo apt-get install apache2 -y
             sudo service apache2 restart
             echo '<!doctype html><html><body><h1>www3</h1></body></html>' | tee /var/www/html/index.html
           




###  gcloud 

The commands below are all run on your local system and assume a `bash` command prompt.

To see OS image names, attributes, and status use the `gcloud compute images list` command.

  1. Create three new virtual machines in a given zone and give them all the same tag. This example sets the zone to us-central1-b. Setting the `tags` field lets you reference these instances all at once, such as with a firewall rule. These commands also install Apache on each instance and give each instance a unique home page. 
         
         gcloud compute instances create www1 \
           --image-family debian-12 \
           --image-project debian-cloud \
           --zone us-central1-b \
           --tags network-lb-tag \
           --metadata startup-script="#! /bin/bash
             sudo apt-get update
             sudo apt-get install apache2 -y
             sudo service apache2 restart
             echo '<!doctype html><html><body><h1>www1</h1></body></html>' | tee /var/www/html/index.html"
         
         gcloud compute instances create www2 \
           --image-family debian-12 \
           --image-project debian-cloud \
           --zone us-central1-b \
           --tags network-lb-tag \
           --metadata startup-script="#! /bin/bash
             sudo apt-get update
             sudo apt-get install apache2 -y
             sudo service apache2 restart
             echo '<!doctype html><html><body><h1>www2</h1></body></html>' | tee /var/www/html/index.html"
         
         gcloud compute instances create www3 \
           --image-family debian-12 \
           --image-project debian-cloud \
           --zone us-central1-b \
           --tags network-lb-tag \
           --metadata startup-script="#! /bin/bash
             sudo apt-get update
             sudo apt-get install apache2 -y
             sudo service apache2 restart
             echo '<!doctype html><html><body><h1>www3</h1></body></html>' | tee /var/www/html/index.html"




###  api 

**Create instance`www1` in zone `us-central1-b` with the** **[`instances.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert)** **method**
    
    
    POST https://compute.googleapis.com/compute/v1/projects/[PROJECT_ID]/zones/us-central1-b/instances
    
    {
      "canIpForward": false,
      "deletionProtection": false,
      "disks": [
        {
          "type": "PERSISTENT",
          "boot": true,
          "mode": "READ_WRITE",
          "autoDelete": true,
          "deviceName": "www1",
          "initializeParams": {
            "sourceImage": "projects/debian-cloud/global/images/debian-12-buster-v20220719",
            "diskType": "projects/[PROJECT_ID]/zones/us-central1-b/diskTypes/pd-standard",
            "diskSizeGb": "10"
          }
        }
      ],
      "machineType": "projects/[PROJECT_ID]/zones/us-central1-b/machineTypes/e2-standard-2",
      "metadata": {
        "items": [
          {
            "key": "startup-script",
            "value": "sudo apt-get update\nsudo apt-get install apache2 -y\nsudo a2ensite default-ssl\nsudo a2enmod ssl\nsudo service apache2 restart\necho '<!doctype html><html><body><h1>www1</h1></body></html>' | tee /var/www/html/index.html"
          }
        ]
      },
      "name": "www1",
      "networkInterfaces": [
        {
          "network": "projects/[PROJECT_ID]/global/networks/default",
          "subnetwork": "projects/[PROJECT_ID]/regions/us-central1/subnetworks/default"
        }
      ],
      "tags": {
        "items": [
          "network-lb-tag"
        ]
      }
    }
    

Create instances named `www2` and `www3` with the same settings, except replace `www1` in the `deviceName`, `value`, and `name` fields.

### Creating a firewall rule to allow external traffic to these VM instances

###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. Click **Create firewall rule**.

  3. Enter a **Name** of `www-firewall-network-lb`.

  4. Select the **Network** that the firewall rule applies to (**Default**).

  5. Under **Targets** , select **Specified target tags**.

  6. In the **Target tags** field, enter `network-lb-tag`.

  7. Set **Source filter** to **IPv4 ranges**.

  8. Set the **Source IPv4 ranges** to `0.0.0.0/0`, which allows traffic from any source.

  9. Under **Specified protocols and ports** , select the **TCP** checkbox and enter `80`.

  10. Click **Create**. It might take a moment for the Console to display the new firewall rule, or you might have to click **Refresh** to see the rule.




###  gcloud 
    
    
    gcloud compute firewall-rules create www-firewall-network-lb \
        --target-tags network-lb-tag --allow tcp:80
    

###  api 

**Create a firewall rule that allows all traffic within the subnet with the** **[`firewalls.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls/insert)** ** method**
    
    
    POST https://compute.googleapis.com/compute/projects/[PROJECT_ID]/global/firewalls
    
    {
      "name": "www-firewall-network-lb",
      "direction": "INGRESS",
      "priority": 1000,
      "targetTags": [
        "network-lb-tag"
      ],
      "allowed": [
        {
          "IPProtocol": "tcp",
          "ports": [
            "80"
          ]
        }
      ],
      "sourceRanges": [
        "0.0.0.0/0"
      ]
    }
    

### Getting the external IP addresses of your instances and verifying that they are running

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. View the addresses for your instances in the **External IP** column.

  3. Verify that your instances are running by looking for a green checkmark to the left of the instance name. If you don't see a green checkmark, refer to the [General Troubleshooting page for instances](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-instances).




###  gcloud 

  1. List your instances to get their IP addresses from the `EXTERNAL_IP` column.
         
         gcloud compute instances list
         

  2. Verify that each instance is running.

At the command line, run `curl` using the external IP address of each instance to confirm that all of the instances respond.
         
         curl http://[IP_ADDRESS]
         




###  api 

**Get information about instance`www1` with the** **[`instances.get`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/get)** **method**

Make sure the `status` field says `RUNNING`, and look for the external IP address in the `natIP` field.
    
    
    GET https://compute.googleapis.com/compute/v1/projects/[PROJECT_ID]/zones/us-central1-b/instances/www1
    
    {
     "kind": "compute#instance",
     "id": "6734015273571474749",
     "creationTimestamp": "2018-11-09T11:45:23.487-08:00",
     "name": "www1",
     "description": "",
     "tags": {
      "items": [
       "network-lb-tag"
      ],
      "fingerprint": "9GVlO4gPawg="
     },
     "machineType": "https://www.googleapis.com/compute/v1/projects/[PROJECT_ID]/zones/us-central1-b/machineTypes/e2-standard-2",
     "status": "RUNNING",
     "zone": "https://www.googleapis.com/compute/v1/projects/[PROJECT_ID]/zones/us-central1-b",
     "canIpForward": false,
     "networkInterfaces": [
      {
       "kind": "compute#networkInterface",
       "network": "https://www.googleapis.com/compute/v1/projects/[PROJECT_ID]/global/networks/default",
       "subnetwork": "https://www.googleapis.com/compute/v1/projects/[PROJECT_ID]/regions/us-central1/subnetworks/default",
       "networkIP": "10.128.0.2",
       "name": "nic0",
       "accessConfigs": [
        {
         "kind": "compute#accessConfig",
         "type": "ONE_TO_ONE_NAT",
         "name": "External NAT",
         "natIP": "35.192.37.233",
         "networkTier": "PREMIUM"
        }
       ],
       "fingerprint": "lxD5f5ua_sw="
      }
     ],
     "disks": [
      {
       "kind": "compute#attachedDisk",
       "type": "PERSISTENT",
       "mode": "READ_WRITE",
       "source": "https://www.googleapis.com/compute/v1/projects/[PROJECT_ID]/zones/us-central1-b/disks/www1",
       "deviceName": "www1",
       "index": 0,
       "boot": true,
       "autoDelete": true,
       "licenses": [
        "https://www.googleapis.com/compute/v1/projects/debian-cloud/global/licenses/debian-12-buster"
       ],
       "interface": "SCSI",
       "guestOsFeatures": [
        {
         "type": "VIRTIO_SCSI_MULTIQUEUE"
        }
       ]
      }
     ],
     "metadata": {
      "kind": "compute#metadata",
      "fingerprint": "IyHRmHoJx6E=",
      "items": [
       {
        "key": "startup-script",
        "value": "#! /bin/bash\n sudo apt-get update\n sudo apt-get install apache2 -y\n sudo service apache2 restart\n echo '\u003c!doctype html\u003e\u003chtml\u003e\u003cbody\u003e\u003ch1\u003ewww1\u003c/h1\u003e\u003c/body\u003e\u003c/html\u003e' | tee /var/www/html/index.html"
       }
      ]
     },
     "serviceAccounts": [
      {
       "email": "674259759219-compute@developer.gserviceaccount.com",
       "scopes": [
        "https://www.googleapis.com/auth/devstorage.read_only",
        "https://www.googleapis.com/auth/logging.write",
        "https://www.googleapis.com/auth/monitoring.write",
        "https://www.googleapis.com/auth/servicecontrol",
        "https://www.googleapis.com/auth/service.management.readonly",
        "https://www.googleapis.com/auth/trace.append"
       ]
      }
     ],
     "selfLink": "https://www.googleapis.com/compute/v1/projects/[PROJECT_ID]/zones/us-central1-b/instances/www1",
     "scheduling": {
      "onHostMaintenance": "MIGRATE",
      "automaticRestart": true,
      "preemptible": false
     },
     "cpuPlatform": "Intel Haswell",
     "labelFingerprint": "42WmSpB8rSM=",
     "startRestricted": false,
     "deletionProtection": false
    }
    

Repeat this API call for `www2` and `www3`.

## Configuring the load balancing service

Next, set up the load balancing service.

When you configure the load balancing service, your virtual machine instances will receive packets that are destined for the static external IP address you configure. If you are using an [image provided by Compute Engine](https://docs.cloud.google.com/compute/docs/images#os-compute-support), your instances are automatically configured to handle this IP address. If you are using any other image, you will have to configure this address as an alias on eth0 or as a loopback on each instance.

###  Console 

You can't use the Google Cloud console to create target pool-based regional external passthrough Network Load Balancers. Instead, use either gcloud or the REST API.

###  gcloud 

  1. Create a [static external IP address](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create) for your load balancer
         
         gcloud compute addresses create network-lb-ip-1 \
             --region us-central1
         

  2. Add a legacy HTTP health check resource Target pool-based regional external passthrough Network Load Balancers can only use [legacy health checks](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts).

This example uses the default settings for the health check mechanism, but you can also customize the health check on your own.
         
         gcloud compute http-health-checks create basic-check
         

  3. Add a target pool

Add a target pool in the same region as your virtual machine instances. Use the health check created in the prior step for this target pool.
         
         gcloud compute target-pools create www-pool \
             --region us-central1 --http-health-check basic-check
         

  4. Add your instances to the target pool
         
         gcloud compute target-pools add-instances www-pool \
             --instances www1,www2,www3 \
             --instances-zone us-central1-b
         

Instances within a target pool must belong to the same region but can be spread out across different zones in the same region. For example, you can have instances in zone `us-central1-f` and instances in zone `us-central1-b` in one target pool because they are in the same region, `us-central1`.

  5. Add a forwarding rule

Add a forwarding rule serving on behalf of an external IP address and port range that points to your target pool. For the `--address` field, use either the numeric IP address or its fully qualified name.
         
         gcloud compute forwarding-rules create www-rule \
             --region us-central1 \
             --ports 80 \
             --address network-lb-ip-1 \
             --target-pool www-pool
         




###  api 

  1. Create a [static external IP address](https://docs.cloud.google.com/compute/docs/reference/rest/v1/addresses/insert) for your load balancer
         
         POST https://compute.googleapis.com/compute/v1/projects/[PROJECT_ID/regions/us-central1/addresses
         {
           "name": "network-lb-ip-1"
         }
         

  2. Add a [legacy HTTP health check](https://docs.cloud.google.com/compute/docs/reference/rest/v1/httpHealthChecks/insert) Target pool-based regional external passthrough Network Load Balancers can only use [legacy health checks](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts).

This example uses the default settings for the health check mechanism, but you can also customize this on your own.
         
         POST https://compute.googleapis.com/compute/v1/projects/[PROJECT_ID]/global/httpHealthChecks
         {
           "name": "basic-check"
         }
         

  3. Add a [target pool](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetPools/insert)

Add a target pool in the same region as your virtual machine instances. Use the health check created in the prior step for this target pool.
         
         POST https://compute.googleapis.com/compute/v1/projects/[PROJECT_ID]/regions/us-central1/targetPools
         {
           "name": "www-pool",
           "healthChecks": [
             "https://www.googleapis.com/compute/v1/projects/[PROJECT_ID]/global/httpHealthChecks/basic-check"
           ]
         }
         

  4. Add your [instances to the target pool](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetPools/addInstance)
         
         POST https://compute.googleapis.com/compute/v1/projects/[PROJECT_ID]/regions/us-central1/targetPools/www-pool/addInstance
         {
           "instances": [
             {
               "instance": "projects/[PROJECT_ID]/zones/us-central1-b/instances/www1"
             }
           ]
         }
         

Repeat this API call for instances `www2` and `www3`.

Instances within a target pool must belong to the same region but can be spread out across different zones in the same region. For example, you can have instances in zone `us-central1-f` and instances in zone `us-central1-b` in one target pool because they are in the same region, `us-central1`.

  5. Add a [forwarding rule](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules/insert)
         
         POST https://compute.googleapis.com/compute/v1/projects/[PROJECT_ID]/regions/us-central1/forwardingRules
         {
           "name": "www-rule",
           "portRange": "80",
           "loadBalancingScheme": "EXTERNAL",
           "target": "https://www.googleapis.com/compute/v1/projects/[PROJECT_ID]/regions/us-central1/targetPools/www-network-lb"
         }
         




## Sending traffic to your instances

Now that the load balancing service is configured, you can start sending traffic to the forwarding rule and watch the traffic be dispersed to different instances.

### Looking up the forwarding rule's external IP address

###  Console 

  1. Go to the **Forwarding Rules** tab on the **Advanced** load balancing page in the Google Cloud console.   
[Go to the Forwarding Rules tab](https://console.cloud.google.com/loadbalancing/advanced/forwardingRules/list)
  2. Locate `www-rule`, the forwarding rule used by the load balancer.
  3. In the **IP Address** column for `www-rule`, note the external IP address listed.



###  gcloud 

Enter the following command to view the external IP address of the `www-rule` forwarding rule used by the load balancer.
    
    
    gcloud compute forwarding-rules describe www-rule --region us-central1
    

###  api 

**View the external IP address of the`www-rule` forwarding rule with the** **[`forwardingRules.get`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules/get)** **method**

In the output, look for the `IPAddress` field.
    
    
    GET https://compute.googleapis.com/compute/v1/projects/[PROJECT_ID]/regions/us-central1/forwardingRules/www-rule
    {
      "kind": "compute#forwardingRule",
      "id": "5133886346582800002",
      "creationTimestamp": "2018-11-09T14:21:33.574-08:00",
      "name": "www-rule",
      "description": "",
      "region": "https://www.googleapis.com/compute/v1/projects/[PROJECT_ID]/regions/us-central1",
      "IPAddress": "35.232.228.9",
      "IPProtocol": "TCP",
      "portRange": "80-80",
      "target": "https://www.googleapis.com/compute/v1/projects/[PROJECT_ID]/regions/us-central1/targetPools/www-network-lb",
      "selfLink": "https://www.googleapis.com/compute/v1/projects/[PROJECT_ID]/regions/us-central1/forwardingRules/www-rule",
      "loadBalancingScheme": "EXTERNAL",
      "networkTier": "PREMIUM"
    }

### ICMP not supported for backend instances

Regional external passthrough Network Load Balancers don't deliver ICMP packets to backend instances. If you send an ICMP packet, for example with `ping` or `traceroute`, the reply doesn't come from the load balancer's backend instances.

Google Cloud infrastructure might send an ICMP reply, even if you have firewall rules that prohibit ICMP traffic on the load balancer's backend instances. This behavior can't be changed.

### Using the `curl` command to access the external IP address

The response from the `curl` command alternates randomly among the three instances. If your response is initially unsuccessful, you might need to wait approximately 30 seconds for the configuration to be fully loaded and for your instances to be marked healthy before trying again:
    
    
    $ while true; do curl -m1 IP_ADDRESS; done
    

## What's next

  * To learn how regional external passthrough Network Load Balancers work with target pools, see the [Target pool-based regional external passthrough Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/network/networklb-target-pools).
  * To learn how regional external passthrough Network Load Balancers work with regional backend services instead of target pools, see the following: 
    * [Regional external passthrough Network Load Balancer with backend services overview](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service)
    * [Set up a regional external passthrough Network Load Balancer with a backend service](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network-backend-service)
    * [Migrate a regional external passthrough Network Load Balancer from target pool to backend service](https://docs.cloud.google.com/load-balancing/docs/network/transition-to-backend-services)
  * To configure advanced network DDoS protection for a regional external passthrough Network Load Balancer by using Cloud Armor, see [Configure advanced network DDoS protection](https://docs.cloud.google.com/armor/docs/advanced-network-ddos).
  * To learn about issues and workarounds when using a regional external passthrough Network Load Balancer for UDP traffic, see [Use UDP with regional external passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/network/udp-with-network-load-balancing).
  * To delete resources so you aren't billed for them, see [Clean up a load balancing setup](https://docs.cloud.google.com/load-balancing/docs/cleaning-up-lb-setup).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
