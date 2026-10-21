---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/egress-control/
title: Control egress in a private instance \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:25.008233+00:00
---

# Control egress in a private instance  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/egress-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Control egress in a private instance Stay organized with collections  Save and categorize content based on your preferences. 

This section describes the high level architecture for establishing egress control from private Cloud Data Fusion instances during the development phase and the pipeline execution phase.

The following system architecture diagram shows how a private Cloud Data Fusion instance connects with the public internet when you develop a pipeline:

![Private instance architecture diagram](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/egress-control/egress-control-diagram.png)

You can control connections to SaaS applications and third-party public cloud services during pipeline development or execution, by routing all egress traffic through customer projects. This process uses the following resources:

  * **Custom VPC network route** : A custom VPC network routes traffic through an imported custom route to gateway VMs, which export to a tenant project VPC using [VPC peering](https://cloud.google.com/vpc/docs/vpc-peering#importing-exporting-routes).

  * **Proxy VM** : A Proxy VM routes egress traffic out of Google Cloud from the Cloud Data Fusion tenant project to the specified destination through the public internet. You create and manage a gateway VM in your customer projects. It's recommended you configure them in a High-Availability (HA) setup using an Internal Load Balancer (ILB). If you have multiple private Cloud Data Fusion instances that use the same VPC network, you can reuse the same VM within the VPC.


**Note:** When you set up egress controls, only the public internet traffic is routed through the proxy VM. All other traffic, such as accessing Google Cloud services or on-premises data centers, does not get routed through the proxy VM.

## Before you begin

  * You can connect to a public source from a private instance in Cloud Data Fusion versions 6.4 or later. To use one of those versions, you can create a new [private Cloud Data Fusion instance](https://docs.cloud.google.com/data-fusion/docs/how-to/create-private-ip) or [upgrade an existing instance](https://docs.cloud.google.com/data-fusion/docs/how-to/upgrading).

  * When you [create a VPC network peering connection](https://docs.cloud.google.com/data-fusion/docs/how-to/create-private-ip?hl=en#create_a_peering_connection) for your instance, select **Export routes**.




## Set up egress control during pipeline development

Egress control lets you control or filter what can go out of your network, which is useful in VPC Service Controls environments. There is no preferred network proxy for performing this task. Examples of proxies include [Squid proxy](http://www.squid-cache.org/), [HAProxy](https://www.haproxy.com/), and [Envoy](https://www.envoyproxy.io/).

The examples in this guide describe how to setup HTTP proxy for HTTP filtering on VM instances that use a Debian image. The examples use a [Squid proxy server](http://www.squid-cache.org/), which is one of the ways of setting up a proxy server.

### Create a proxy VM

Create a VM in the same VPC as your private Cloud Data Fusion instance with the following startup script and IP forwarding.

This script installs Squid proxy, and configures it to intercept HTTP traffic and allow `.squid-cache.org` and `.google.com` domains. You can replace these domains with the domains that you want to connect with your Cloud Data Fusion instance.

**Note:** The examples in this guide describe how to set up a network proxy on VM instances that use a Debian image (`debian-10-buster-v20210316`). They use a gateway instance as a [Squid proxy server](http://www.squid-cache.org/) but this is only one way of setting up a proxy server.

### Console

  1. Go to the **VM instances** page.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  2. Click **Create instance**.

  3. Use the same VPC that has network peering set up with the private Cloud Data Fusion instance. For more information about VPC network peering in this scenario, see Before you begin.

  4. [Enable IP forwarding](https://docs.cloud.google.com/vpc/docs/using-routes#canipforward) for the instance **in the same network** as the Cloud Data Fusion instance.

  5. In the **Startup script** field, enter the following script:
         
         #! /bin/bash
         apt-get -y install squid3
         cat <<EOF > /etc/squid/conf.d/debian.conf
         #
         # Squid configuration settings for Debian
         #
         logformat squid %ts.%03tu %6tr %>a %Ss/%03>Hs %<st %rm %ru %ssl::>sni %Sh/%<a %mt
         logfile_rotate 10
         debug_options rotate=10
         
         # configure intercept port
         http_port 3129 intercept
         
         # allow only certain sites
         acl allowed_domains dstdomain "/etc/squid/allowed_domains.txt"
         http_access allow allowed_domains
         
         # deny all other http requests
         http_access deny all
         EOF
         
         # Create a file with allowed egress domains
         # Replace these example domains with the domains that you want to allow
         # egress from in Data Fusion pipelines
         cat <<EOF > /etc/squid/allowed_domains.txt
         .squid-cache.org
         .google.com
         EOF
         
         /etc/init.d/squid restart
         
         iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 3129
         
         echo 1 > /proc/sys/net/ipv4/ip_forward
         echo net.ipv4.ip_forward=1 > /etc/sysctl.d/11-gce-network-security.conf
         iptables -t nat -A POSTROUTING -s 0.0.0.0/0 -p tcp --dport 443 -j MASQUERADE
         




### gcloud
    
    
    export CDF_PROJECT=<cdf-project>
    export PROXY_VM=<proxy-vm>
    export ZONE=<vm-zone>
    export SUBNET=<subnet>
    export VPC_NETWORK=<vpc-network>
    export COMPUTE_ENGINE_SA=<compute-engine-sa>
    
    gcloud beta compute --project=$CDF_PROJECT instances create $PROXY_VM --zone=$ZONE --machine-type=e2-medium --subnet=$SUBNET --no-address --metadata=startup-script=\#\!\ /bin/bash$'\n'apt-get\ -y\ install\ squid3$'\n'cat\ \<\<EOF\ \>\ /etc/squid/conf.d/debian.conf$'\n'\#$'\n'\#\ Squid\ configuration\ settings\ for\ Debian$'\n'\#$'\n'logformat\ squid\ \%ts.\%03tu\ \%6tr\ \%\>a\ \%Ss/\%03\>Hs\ \%\<st\ \%rm\ \%ru\ \%ssl::\>sni\ \%Sh/\%\<a\ \%mt$'\n'logfile_rotate\ 10$'\n'debug_options\ rotate=10$'\n'$'\n'\#\ configure\ intercept\ port$'\n'http_port\ 3129\ intercept$'\n'$'\n'\#\ allow\ only\ certain\ sites$'\n'acl\ allowed_domains\ dstdomain\ \"/etc/squid/allowed_domains.txt\"$'\n'http_access\ allow\ allowed_domains$'\n'$'\n'\#\ deny\ all\ other\ http\ requests$'\n'http_access\ deny\ all$'\n'EOF$'\n'$'\n'$'\n'\#\ Create\ a\ file\ with\ allowed\ egress\ domains$'\n'\#\ Replace\ these\ example\ domains\ with\ the\ domains\ that\ you\ want\ to\ allow\ $'\n'\#\ egress\ from\ in\ Data\ Fusion\ pipelines$'\n'cat\ \<\<EOF\ \>\ /etc/squid/allowed_domains.txt$'\n'.squid-cache.org$'\n'.google.com$'\n'EOF$'\n'$'\n'/etc/init.d/squid\ restart$'\n'$'\n'iptables\ -t\ nat\ -A\ PREROUTING\ -p\ tcp\ --dport\ 80\ -j\ REDIRECT\ --to-port\ 3129$'\n'echo\ 1\ \>\ /proc/sys/net/ipv4/ip_forward$'\n'echo\ net.ipv4.ip_forward=1\ \>\ /etc/sysctl.d/11-gce-network-security.conf$'\n'iptables\ -t\ nat\ -A\ POSTROUTING\ -s\ 0.0.0.0/0\ -p\ tcp\ --dport\ 443\ -j\ MASQUERADE --can-ip-forward --maintenance-policy=MIGRATE --service-account=$COMPUTE_ENGINE_SA --scopes=https://www.googleapis.com/auth/devstorage.read_only,https://www.googleapis.com/auth/logging.write,https://www.googleapis.com/auth/monitoring.write,https://www.googleapis.com/auth/servicecontrol,https://www.googleapis.com/auth/service.management.readonly,https://www.googleapis.com/auth/trace.append --tags=http-server,https-server --image=debian-10-buster-v20210420 --image-project=debian-cloud --boot-disk-size=10GB --boot-disk-type=pd-balanced --boot-disk-device-name=instance-1 --no-shielded-secure-boot --shielded-vtpm --shielded-integrity-monitoring --reservation-affinity=any
    
    gcloud compute --project=$CDF_PROJECT firewall-rules create egress-allow-http --direction=INGRESS --priority=1000 --network=$VPC_NETWORK --action=ALLOW --rules=tcp:80 --source-ranges=0.0.0.0/0 --target-tags=https-server
    
    gcloud compute --project=$CDF_PROJECT firewall-rules create egress-allow-https --direction=INGRESS --priority=1000 --network=$VPC_NETWORK --action=ALLOW --rules=tcp:443 --source-ranges=0.0.0.0/0 --target-tags=https-server
    

### Create a custom route

Create a custom [route](https://docs.cloud.google.com/vpc/docs/routes) to connect to the [gateway VM instance that you created](https://docs.cloud.google.com/data-fusion/docs/how-to/connect-to-public-source#create-vm).

### Console

To create your route in the Google Cloud console, see [Adding a static route](https://docs.cloud.google.com/vpc/docs/using-routes#addingroute).

When you configure the route, do the following:

  * Set the **Priority** to greater than or equal to `1001`.
  * Use the same project and VPC as the private Cloud Data Fusion instance.
  * Be sure that your VPC network peering configuration allows exporting routes, so that the Cloud Data Fusion tenant project VPC imports this custom route through VPC network peering.



### gcloud

To create your route in gcloud CLI: 
    
    
    gcloud beta compute routes create $ROUTE --project=$CDF_PROJECT \
        --network=$VPC_NETWORK --priority=1001 \
        --destination-range=0.0.0.0/0 \
        --next-hop-instance=$PROXY_VM \
        --next-hop-instance-zone=$ZONE
    

## Set up egress control for pipeline execution

After you're able to access the public internet with allowed hostnames in Preview and Wrangler in your design environment, deploy your pipeline. Deployed Cloud Data Fusion pipelines run on Managed Service for Apache Spark clusters by default.

To ensure that all public internet traffic from the Managed Service for Apache Spark cluster goes through one or more Proxy VMs, add the private DNS zone and records. This step is required because Cloud NAT doesn't support filtering.

In the DNS records, include the IP address of the proxy VM or ILB.

### Deploy your pipeline

After you've verified the pipeline in the design phase, deploy your pipeline. Deployed pipelines run on Managed Service for Apache Spark clusters by default.

To ensure that all public internet traffic from the Managed Service for Apache Spark cluster goes through one or more Proxy VMs, add a custom route with instance tags `proxy` and priority `1000` to the same VPC as the Managed Service for Apache Spark VMs:

![Create custom route](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/egress-control/create-custom-route.png)

Modify your pipeline to use Managed Service for Apache Spark tags because Cloud NAT currently doesn't support any egress filtering.

## What's next

  * Learn more about [Networking in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/networking).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
