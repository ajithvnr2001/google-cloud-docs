---
url: https://docs.cloud.google.com/load-balancing/docs/https/setting-up-query-and-header-routing/
title: Set up header and query parameter-based routing for the classic Application Load Balancer \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:36.470793+00:00
---

# Set up header and query parameter-based routing for the classic Application Load Balancer  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/https/setting-up-query-and-header-routing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Set up header and query parameter-based routing for the classic Application Load Balancer Stay organized with collections  Save and categorize content based on your preferences. 

This page includes two examples for classic Application Load Balancer:

  * Set up query parameter-based routing
  * Set up HTTP header-based routing



To configure traffic management for the global external Application Load Balancer and the regional external Application Load Balancer, see the following pages:

  * [Set up traffic management for global external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-global-traffic-mgmt#headers)
  * [Set up traffic management for regional external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-traffic-mgmt#headers)



## Before you begin

  * Read the [Traffic management overview for external Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/https/traffic-management).
  * Be familiar with the [URL map API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/urlMaps/insert).



## Set up query parameter-based routing

This example demonstrates using query parameters to do A/B testing by matching on the query string.

### Add two backend instance groups

For routing to be useful, you must have multiple backends.

To set up two backends, your VMs need to be in two instance groups. This guide describes how to create managed instance groups with Linux VMs that have Apache running and then set up load balancing.

The managed instance groups provide VMs running the backend servers of an external HTTP load balancer. For demonstration purposes, backends serve their own hostnames.

For simplicity, the backends reside in the same region. If you want a multi-region setup, you must have an instance template setup for the second region.

###  Console 

  1. Create an instance template. In the Google Cloud console, go to the **Instance templates** page.

[Go to Instance templates](https://console.cloud.google.com/compute/instanceTemplates/list)

     1. Click **Create instance template**.
     2. For **Name** , enter `lb-backend-template`.
     3. Ensure that the **Boot disk** is set to a Debian image, such as **Debian GNU/Linux 12 (bookworm)**. These instructions use commands that are only available on Debian, such as `apt-get`.
     4. Click **Advanced options**.
     5. Click **Networking** and configure the following field: 
        1. For **Network tags** , enter `allow-health-check`.
     6. Click **Management**. Enter the following script into the **Startup script** field.
            
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
            

     7. Click **Create**.

  2. Create a managed instance group. Go to the **Instance groups** page in the Google Cloud console.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

     1. Click **Create instance group**.
     2. Select **New managed instance group (stateless)**. For more information, see [Stateless or stateful MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#stateless_or_stateful_migs).
     3. For **Name** , enter `first-example-ig`.
     4. Under **Location** , select **Single zone**.
     5. For **Region** , select your preferred region. This example uses `us-east1`.
     6. For **Zone** , select `us-east1-b`.
     7. Under **Instance template** , select the instance template `lb-backend-template`.
     8. Under **Maximum number of instances** , enter `2`.
     9. Under **Autoscaling mode** , select `Off:do not autoscale`.
     10. Click **Create**.



Create another managed instance group like this one. Name the second one `second-example-ig`, and base it on the `lb-backend-template` template.

###  gcloud 

  1. Create an instance template.
         
         gcloud compute instance-templates create lb-backend-template \
            --region=us-east1 \
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
         

  2. Create the first managed instance group based on the template.
         
         gcloud compute instance-groups managed create first-example-ig \
            --template=lb-backend-template --size=2 --zone=us-east1-b
         

  3. Create the second managed instance group based on the template.
         
         gcloud compute instance-groups managed create second-example-ig \
            --template=lb-backend-template --size=2 --zone=us-east1-c
         




### Configuring a firewall rule

In this example, you create the `fw-allow-health-check` firewall rule. This is an ingress rule that allows traffic from the [Google Cloud health checking systems](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges). This example uses the target tag `allow-health-check` to identify the VMs.

###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.   
[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)
  2. Click **Create firewall rule** to create the second firewall rule:
  3. Enter a **Name** of `fw-allow-health-check`.
  4. Under **Network** , select `Default`.
  5. Under **Targets** , select **Specified target tags**.
  6. Populate the **Target tags** field with `allow-health-check`.
  7. Set **Source filter** to **IPv4 ranges**.
  8. Set **Source IPv4 ranges** to `35.191.0.0/16`.
  9. Under **Protocols and ports** , select **Specified protocols and ports**.
  10. Select the **TCP** checkbox and enter `80` for the port numbers.
  11. Click **Create**.



###  gcloud 
    
    
    gcloud compute firewall-rules create fw-allow-health-check \
        --network=default \
        --action=allow \
        --direction=ingress \
        --source-ranges=35.191.0.0/16 \
        --target-tags=allow-health-check \
        --rules=tcp
    

### Reserving an external IP address

Now that your instances are up and running, set up a [global static external IP address](https://docs.cloud.google.com/compute/docs/ip-addresses#externaladdresses) that your customers use to reach your load balancer.

###  Console 

  1. In the Google Cloud console, go to the **IP addresses** page.

[Go to IP addresses](https://console.cloud.google.com/networking/addresses/list)

  2. Click **Reserve external**.

  3. On the **Reserve external static IP address** page, for **Name** , enter `lb-ipv4-1`.

  4. Set **Network Service Tier** to **Premium**.

  5. Set **IP version** to **IPv4**.

  6. Set **Type** to **Global**.

  7. Click **Reserve**.




###  gcloud 
    
    
    gcloud compute addresses create lb-ipv4-1 \
        --ip-version=IPV4 \
        --network-tier=PREMIUM \
        --global
    

Note the IPv4 address that was reserved:
    
    
    gcloud compute addresses describe lb-ipv4-1 \
        --format="get(address)" \
        --global
    

### Setting up the load balancer backends

###  Console 

The Google Cloud console is currently unsupported for setting up header-based and parameter-based routing. Use `gcloud` or the API instead.

###  gcloud 

  1. Create a [health check](https://docs.cloud.google.com/load-balancing/docs/health-checks). 
         
         gcloud compute health-checks create http http-basic-check \
                 --port 80
             

  2. Create the first [backend service](https://docs.cloud.google.com/compute/docs/reference/v1/backendServices). 
     * For a global external Application Load Balancer, use the gcloud CLI command with `load-balancing-scheme=EXTERNAL_MANAGED`. This setting offers [advanced traffic management capability](https://docs.cloud.google.com/load-balancing/docs/https/traffic-management-global).
     * For an classic Application Load Balancer, use `load-balancing-scheme=EXTERNAL`.
    
    gcloud compute backend-services create service-a \
            --load-balancing-scheme=LOAD_BALANCING_SCHEME \
            --global-health-checks \
            --protocol HTTP \
            --health-checks http-basic-check \
            --global
        

  3. Create the second [backend service](https://docs.cloud.google.com/compute/docs/reference/v1/backendServices). 
         
         gcloud compute backend-services create service-b \
                 --load-balancing-scheme=LOAD_BALANCING_SCHEME \
                 --global-health-checks \
                 --protocol HTTP \
                 --health-checks http-basic-check \
                 --global
             

  4. Add your first instance group as the backend to the first backend service. 
         
         gcloud compute backend-services add-backend service-a \
                 --balancing-mode=UTILIZATION \
                 --max-utilization=0.8 \
                 --capacity-scaler=1 \
                 --instance-group=first-example-ig \
                 --instance-group-zone=us-east1-b \
                 --global
             

  5. Add your second instance group as the backend to the second backend service. 
         
         gcloud compute backend-services add-backend service-b \
                 --balancing-mode=UTILIZATION \
                 --max-utilization=0.8 \
                 --capacity-scaler=1 \
                 --instance-group=second-example-ig \
                 --instance-group-zone=us-east1-c \
                 --global
             




### Creating the URL map

###  Console 

The Google Cloud console is currently unsupported for setting up header-based and parameter-based routing. Use `gcloud` or the API instead.

###  gcloud 

  1. Create a YAML file `/tmp/web-map-http.yaml`. Replace `PROJECT_ID` with your project ID.
         
         defaultService: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/service-a
         hostRules:
         - hosts:
           - '*'
           pathMatcher: path-matcher-1
         name: web-map-http
         pathMatchers:
         - defaultService: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/service-a
           name: path-matcher-1
           routeRules:
             - matchRules:
                 - prefixMatch: /
                   queryParameterMatches:
                     - name: ABTest
                       exactMatch: A
               priority: 0
               service: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/service-a
             - matchRules:
                 - prefixMatch: /
                   queryParameterMatches:
                     - name: ABTest
                       exactMatch: B
               priority: 1
               service: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/service-b
         selfLink: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/urlMaps/web-map-http
         tests:
         - description: Test routing for query ABTest with A
           host: example.com
           path: /?ABTest=A
           service: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/service-a
           expectedOutputUrl: http://example.com/?ABTest=A
         - description: Test routing for query ABTest with B
           host: example.com
           path: /?ABTest=B
           service: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/service-b
           expectedOutputUrl: http://example.com/?ABTest=B
         

  2. Validate the URL map.
         
         gcloud compute url-maps validate --source /tmp/web-map-http.yaml
         

If the tests pass and the command outputs a success message, save the changes to the URL map.

  3. Update the URL map.
         
         gcloud compute url-maps import web-map-http \
            --source /tmp/web-map-http.yaml \
            --global
         




### Creating the target proxy and forwarding rule

###  Console 

The Google Cloud console is currently unsupported for setting up header-based and parameter-based routing. Use `gcloud` or the API instead.

###  gcloud 

  1. Create a target HTTP proxy to route requests to your URL map. 
         
         gcloud compute target-http-proxies create http-lb-proxy \
                 --url-map web-map-http
             

  2. Create a global forwarding rule to route incoming requests to the proxy. 
     * For a global external Application Load Balancer, use the gcloud CLI command with `load-balancing-scheme=EXTERNAL_MANAGED`. This setting offers [advanced traffic management capability](https://docs.cloud.google.com/load-balancing/docs/https/traffic-management-global).
     * For an classic Application Load Balancer, use `load-balancing-scheme=EXTERNAL`.
    
    gcloud compute forwarding-rules create http-content-rule \
            --load-balancing-scheme=LOAD_BALANCING_SCHEME \
            --network-tier=PREMIUM \
            --address=lb-ipv4-1 \
            --global \
            --target-http-proxy=http-lb-proxy \
            --ports=80
        




### Testing

Note the IPv4 address that was reserved:
    
    
    gcloud compute addresses describe lb-ipv4-1 \
        --format="get(address)" \
        --global
    

Test this setup by running:
    
    
    curl http://IP_ADDRESS?ABTest=A
    
    
    
    curl http://IP_ADDRESS?ABTest=B
    

In a browser, open `http://IP_ADDRESS?ABTest=A` and `http://IP_ADDRESS?ABTest=B`.

## Set up HTTP header-based routing

This example demonstrates adding and removing HTTP headers to do intelligent routing.

### Before you begin

You can use an existing external Application Load Balancer or create a new one.

You can use this feature with any of the [supported backend types](https://docs.cloud.google.com/load-balancing/docs/features#backends). This example assumes that you're using VMs in an instance group.

To set up a simple load balancer, see the query parameter-based example above.

### Updating the URL map

###  Console 

The Google Cloud console is currently unsupported for setting up header-based and parameter-based routing. Use `gcloud` or the API instead.

###  gcloud 

  1. This example demonstrates using HTTP request headers to do A/B testing by matching on values in the request's HTTP headers.

Create a YAML file `/tmp/web-map-http.yaml`. Replace `PROJECT_ID` with your project ID.
         
         defaultService: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/service-a
         kind: compute#urlMap
         name: web-map-http
         hostRules:
         - hosts:
           - '*'
           pathMatcher: path-matcher-1
         pathMatchers:
         - defaultService: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/service-a
           name: path-matcher-1
           routeRules:
             - matchRules:
                 - prefixMatch: /
                   headerMatches:
                     - headerName: ABTest
                       exactMatch: A
               priority: 0
               service: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/service-a
             - matchRules:
                 - prefixMatch: /
                   headerMatches:
                     - headerName: ABTest
                       exactMatch: B
               priority: 1
               service: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/service-b
         tests:
         - description: Test routing for query ABTest with A
           host: example.com
           path: /
           headers:
           - name: ABTest
             value: A
           service: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/service-a
         - description: Test routing for query ABTest with B
           host: example.com
           path: /
           headers:
           - name: ABTest
             value: B
           service: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/service-b
         

  2. Validate the URL map.
         
         gcloud compute url-maps validate --source /tmp/web-map-http.yaml
         

If the tests pass and the command outputs a success message, save the changes to the URL map.

  3. Update the URL map.
         
         gcloud compute url-maps import web-map-http \
            --source /tmp/web-map-http.yaml \
            --global
         




### Testing

Using the IPv4 address of the associated load balancer, test this setup by running:
    
    
    curl http://IP_ADDRESS -H "ABTest: A"
    
    
    
    curl http://IP_ADDRESS -H "ABTest: B"
    

## What's next

  * [Clean up the load balancer setup](https://docs.cloud.google.com/load-balancing/docs/cleaning-up-lb-setup).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
