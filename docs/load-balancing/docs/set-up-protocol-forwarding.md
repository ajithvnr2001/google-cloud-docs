---
url: https://docs.cloud.google.com/load-balancing/docs/set-up-protocol-forwarding/
title: Set up protocol forwarding \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:25:25.871181+00:00
---

# Set up protocol forwarding  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/set-up-protocol-forwarding/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Set up protocol forwarding Stay organized with collections  Save and categorize content based on your preferences. 

This document contains instructions to configure protocol forwarding for both internal and external protocol forwarding. Before you configure protocol forwarding, read [Protocol forwarding overview](https://docs.cloud.google.com/load-balancing/docs/protocol-forwarding).

**Note:** You cannot create target instance resources using the Google Cloud console. You can only use the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-instances) or [API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetInstances) commands.

## Set up external protocol forwarding

This section shows you how to set up external protocol forwarding by using a forwarding rule to forward TCP traffic to a single target instance. There are separate instructions for IPv4-only, dual-stack, and IPv6-only traffic.

To set up external protocol forwarding, you create a target instance that contains a single VM instance. You then create an external regional forwarding rule that forwards traffic to the target instance.

### IPv4 only

For simplicity, this example uses the default network and subnets.

  1. Create a firewall rule that allows external traffic to reach the target instance.
         
         gcloud compute firewall-rules create ALLOW_IPV4_FIREWALL_RULE_NAME \
             --target-tags=allow-ipv4-ext \
             --allow=tcp:80 \
             --source-ranges=0.0.0.0/0
         

  2. Create a VM. For this example, you set up an Apache server on the VM.
         
         gcloud compute instances create VM_INSTANCE_NAME \
             --zone=ZONE \
             --image-family=debian-12 \
             --image-project=debian-cloud \
             --tags=allow-ipv4-ext \
             --metadata=startup-script='#! /bin/bash
             sudo apt-get update
             sudo apt-get install apache2 -y
             sudo a2ensite default-ssl
             sudo a2enmod ssl
             vm_hostname="$(curl -H "Metadata-Flavor:Google" \
             http://169.254.169.254/computeMetadata/v1/instance/name)"
             echo "Page served from: $vm_hostname" | \
             tee /var/www/html/index.html
             sudo systemctl restart apache2'
         

  3. Create a target instance that contains the VM created in the previous step. You must create a target instance before you can create a forwarding rule object because the forwarding rule must reference an existing target resource.
         
         gcloud compute target-instances create TARGET_INSTANCE_NAME \
             --instance=VM_INSTANCE_NAME \
             --zone=ZONE
         

  4. Reserve a [static external IPv4 address](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create).
         
         gcloud compute addresses create IPV4_ADDRESS \
             --region=REGION
         

  5. Create the forwarding rule that forwards TCP traffic to the target instance. The forwarding rule must be created in the same region in which the target instance was created.
         
         gcloud compute forwarding-rules create IPV4_FORWARDING_RULE_NAME \
             --load-balancing-scheme=EXTERNAL \
             --region=REGION \
             --ip-protocol=TCP \
             --address=IPV4_ADDRESS \
             --ports=80 \
             --target-instance=TARGET_INSTANCE_NAME \
             --target-instance-zone=ZONE
         

  6. Test your setup.

     1. Get the IP address of your forwarding rule.
            
            gcloud compute forwarding-rules describe IPV4_FORWARDING_RULE_NAME \
                --region=REGION
            

     2. Make web requests to the load balancer by using curl to contact its IP address. Replace `IP_ADDRESS` with the IP address from the previous step.
            
            while true; do curl -m1 IP_ADDRESS; done
            

The output is similar to the following, where the name of the backend VM generating the response is displayed.
            
            Page served from: VM_INSTANCE_NAME.
            




### Dual-stack

Handling both IPv4 and IPv6 traffic requires a dual-stack subnet with a dual-stack VM instance for the target instance backend.

  1. Create a custom mode VPC network.
         
         gcloud compute networks create VPC_NAME \
             --subnet-mode=custom
         

  2. Within the VPC network, create a dual-stack subnet.
         
         gcloud compute networks subnets create SUBNET_NAME \
             --network=VPC_NAME \
             --range=IPV4_ADDRESS_RANGE \
             --stack-type=IPV4_IPV6 \
             --ipv6-access-type=EXTERNAL \
             --region=REGION
         

For IPV4_ADDRESS_RANGE, you can enter any primary IPv4 range for the new subnet, in CIDR notation. For example, `192.168.11.0/24`. For more information, see [IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/vpc#manually_created_subnet_ip_ranges).

  3. Create a firewall rule that allows external traffic to reach the target instance.
         
         gcloud compute firewall-rules create ALLOW_IPV6_FIREWALL_RULE_NAME \
             --network=VPC_NAME \
             --target-tags=allow-ipv6-ext \
             --allow=tcp:80 \
             --source-ranges=::/0
         

  4. Create a dual-stack VM.
         
         gcloud compute instances create VM_INSTANCE_NAME \
             --subnet=SUBNET_NAME \
             --stack-type=IPV4_IPV6 \
             --zone=ZONE \
             --image-family=debian-12 \
             --image-project=debian-cloud \
             --tags=allow-ipv6-ext \
             --metadata=startup-script='#! /bin/bash
             sudo apt-get update
             sudo apt-get install apache2 -y
             sudo a2ensite default-ssl
             sudo a2enmod ssl
             vm_hostname="$(curl -H "Metadata-Flavor:Google" \
             http://metadata.google.internal/computeMetadata/v1/instance/name)"
             echo "Page served from: $vm_hostname" | \
             tee /var/www/html/index.html
             sudo systemctl restart apache2'
         

  5. Create a target instance that contains the VM created in the previous step.
         
         gcloud compute target-instances create TARGET_INSTANCE_NAME \
             --instance=VM_INSTANCE_NAME \
             --network=VPC_NAME \
             --zone=ZONE
         

  6. Reserve a [static external IPv4 address](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create).
         
         gcloud compute addresses create IPV4_ADDRESS \
            --region=REGION
         

  7. Create an IPv4 forwarding rule that forwards TCP traffic to the target instance. The forwarding rule must be created in the same region in which the target instance was created.
         
         gcloud compute forwarding-rules create IPV4_FORWARDING_RULE_NAME \
             --load-balancing-scheme=EXTERNAL \
             --region=REGION \
             --ip-protocol=TCP \
             --address=IPV4_ADDRESS \
             --ports=80 \
             --target-instance=TARGET_INSTANCE_NAME \
             --target-instance-zone=ZONE
         

  8. Reserve a [static external IPv6 address range](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create).
         
         gcloud compute addresses create IPV6_ADDRESS \
             --region=REGION \
             --subnet=SUBNET_NAME \
             --ip-version=IPV6 \
             --endpoint-type=NETLB
         

  9. Create an IPv6 forwarding rule that forwards TCP traffic to the target instance. The forwarding rule must be created in the same region in which the target instance was created.
         
         gcloud compute forwarding-rules create IPV6_FORWARDING_RULE_NAME \
             --load-balancing-scheme=EXTERNAL \
             --subnet=SUBNET_NAME \
             --ip-version=IPV6 \
             --region=REGION \
             --address=IPV6_ADDRESS \
             --network-tier=PREMIUM \
             --target-instance=TARGET_INSTANCE_NAME \
             --target-instance-zone=ZONE \
             --ip-protocol=TCP \
             --ports=80
         

  10. Test your setup.

     1. Get the IP address of the forwarding rules.
            
            gcloud compute forwarding-rules describe IPV4_FORWARDING_RULE_NAME \
              --region=REGION
            
            
            gcloud compute forwarding-rules describe IPV6_FORWARDING_RULE_NAME \
              --region=REGION
            

     2. Make web requests to the load balancer by using curl to contact its IP address. Replace `IP_ADDRESS` with the IP address from the previous step.

For IPv4 traffic:
            
            while true; do curl -m1 IP_ADDRESS; done
            

For IPv6 traffic:
            
            curl -6 'http://[IP_ADDRESS]:80'
            

The output is similar to the following, where the name of the backend VM generating the response is displayed.
            
            Page served from: VM_INSTANCE_NAME.
            




### IPv6 only

Handling only IPv6 traffic requires an IPv6-only subnet with an IPv6-only VM instance for the target instance backend.

  1. Create a custom mode VPC network.
         
         gcloud beta compute networks create VPC_NAME \
             --subnet-mode=custom
         

  2. Within the VPC network, create an IPv6-only subnet.
         
         gcloud beta compute networks subnets create SUBNET_NAME \
             --network=VPC_NAME \
             --stack-type=IPV6_ONLY \
             --ipv6-access-type=EXTERNAL \
             --region=REGION
          

  3. Create a firewall rule that allows external traffic to reach the target instance.
         
         gcloud beta compute firewall-rules create ALLOW_IPV6_FIREWALL_RULE_NAME \
             --network=VPC_NAME \
             --target-tags=allow-ipv6-ext \
             --allow=tcp:80 \
             --source-ranges=::/0
         

  4. Create an IPv6-only VM.
         
         gcloud beta compute instances create VM_INSTANCE_NAME \
             --subnet=SUBNET_NAME \
             --stack-type=IPV6_ONLY \
             --zone=ZONE \
             --image-family=debian-12 \
             --image-project=debian-cloud \
             --tags=allow-ipv6-ext \
             --metadata=startup-script='#! /bin/bash
             sudo apt-get update
             sudo apt-get install apache2 -y
             sudo a2ensite default-ssl
             sudo a2enmod ssl
             vm_hostname="$(curl -H "Metadata-Flavor:Google" \
             http://metadata.google.internal/computeMetadata/v1/instance/name)"
             echo "Page served from: $vm_hostname" | \
             tee /var/www/html/index.html
             sudo systemctl restart apache2'
         

  5. Create a target instance that contains the VM created in the previous step.
         
         gcloud beta compute target-instances create TARGET_INSTANCE_NAME \
             --instance=VM_INSTANCE_NAME \
             --network=VPC_NAME \
             --zone=ZONE
         

  6. Reserve a [static external IPv6 address range](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create).
         
         gcloud beta compute addresses create IPV6_ADDRESS \
             --region=REGION \
             --subnet=SUBNET_NAME \
             --ip-version=IPV6 \
             --endpoint-type=NETLB
         

  7. Create an IPv6 forwarding rule that forwards TCP traffic to the target instance. The forwarding rule must be created in the same region in which the target instance was created.
         
         gcloud beta compute forwarding-rules create IPV6_FORWARDING_RULE_NAME \
             --load-balancing-scheme=EXTERNAL \
             --subnet=SUBNET_NAME \
             --ip-version=IPV6 \
             --region=REGION \
             --address=IPV6_ADDRESS \
             --network-tier=PREMIUM \
             --target-instance=TARGET_INSTANCE_NAME \
             --target-instance-zone=ZONE \
             --ip-protocol=TCP \
             --ports=80
         

  8. Test your setup.

     1. Get the IP address of the forwarding rule.
            
            gcloud beta compute forwarding-rules describe IPV6_FORWARDING_RULE_NAME \
                --region=REGION
            

     2. Make web requests to the load balancer by using curl to contact its IP address. Replace `IPV6_ADDRESS` with the IP address from the previous step.
            
            curl -6 'http://[IPV6_ADDRESS]:80'
            

The output is similar to the following, where the name of the backend VM generating the response is displayed.
            
            Page served from: VM_INSTANCE_NAME.
            




## Set up internal protocol forwarding

This section shows you how to set up internal protocol forwarding by using a forwarding rule to forward TCP traffic to a single target instance. There are separate instructions for IPv4-only, dual-stack, and IPv6-only traffic.

For this example, you create a target instance that contains a single VM instance with an Apache server installed on it. You then create an internal regional forwarding rule that forwards traffic to the target instance.

### IPv4 only

For simplicity, this example uses the default network and subnets to set up internal protocol forwarding.

  1. Create a firewall rule that allows internal traffic to reach the target instance.
         
         gcloud compute firewall-rules create ALLOW_IPV4_FIREWALL_RULE_NAME \
             --target-tags=allow-ipv4-int \
             --allow=tcp \
             --source-ranges=0.0.0.0/0
         

  2. Create a firewall rule to allow SSH connectivity to VMs with the network tag `allow-ssh`. This is used to establish an SSH connection to the client VM.
         
         gcloud compute firewall-rules create ALLOW_SSH_FIREWALL_RULE_NAME \
             --target-tags=allow-ssh \
             --allow=tcp:22 \
             --source-ranges=0.0.0.0/0
         

  3. Create a VM.
         
         gcloud compute instances create VM_INSTANCE_NAME \
             --zone=ZONE \
             --image-family=debian-12 \
             --image-project=debian-cloud \
             --tags=allow-ipv4-int \
             --metadata=startup-script='#! /bin/bash
             sudo apt-get update
             sudo apt-get install apache2 -y
             sudo a2ensite default-ssl
             sudo a2enmod ssl
             vm_hostname="$(curl -H "Metadata-Flavor:Google" \
             http://169.254.169.254/computeMetadata/v1/instance/name)"
             echo "Page served from: $vm_hostname" | \
             tee /var/www/html/index.html
             sudo systemctl restart apache2'
         

  4. Create a target instance that contains the VM created in the previous step. You must create a target instance before you can create a forwarding rule object because the forwarding rule must reference an existing target resource.
         
         gcloud compute target-instances create TARGET_INSTANCE_NAME \
             --instance=VM_INSTANCE_NAME \
             --zone=ZONE
         

  5. Create the forwarding rule that forwards TCP traffic to the target instance. The forwarding rule must be created in the same region in which the target instance was created.
         
         gcloud compute forwarding-rules create IPV4_FORWARDING_RULE_NAME \
             --load-balancing-scheme=INTERNAL \
             --network-tier=PREMIUM \
             --region=REGION \
             --ip-protocol=TCP \
             --ports=80 \
             --target-instance=TARGET_INSTANCE_NAME \
             --target-instance-zone=ZONE
         

  6. Create a test client VM.
         
         gcloud compute instances create CLIENT_VM_NAME \
             --zone=ZONE \
             --image-family=debian-12 \
             --image-project=debian-cloud \
             --tags=allow-ssh
         

You can now test your protocol forwarding configuration by sending traffic from this client VM to the forwarding rule IP address.

  7. Test your setup.

     1. Get the IP address of your forwarding rule.
            
            gcloud compute forwarding-rules describe IPV4_FORWARDING_RULE_NAME \
                --region=REGION
            

     2. Establish an SSH connection to the client VM.
            
            gcloud compute ssh CLIENT_VM_NAME \
                --zone=ZONE
            

     3. Make requests to the load balancer by using curl to contact its IP address.
            
            while true; do curl -m1 IP_ADDRESS; done
            

The output is similar to the following, where the name of the backend VM generating the response is displayed.
            
            Page served from: VM_INSTANCE_NAME.
            




### Dual-stack

Handling both IPv4 and IPv6 traffic requires a dual-stack subnet with a dual-stack VM instance for the target instance backend.

  1. Create a custom mode VPC network with the `--enable-ula-internal-ipv6` flag to configure internal IPv6 ranges on any subnets in this network.
         
         gcloud compute networks create VPC_NAME \
             --subnet-mode=custom \
             --enable-ula-internal-ipv6
         

  2. Within the VPC network, create a dual-stack subnet.
         
         gcloud compute networks subnets create SUBNET_NAME \
             --network=VPC_NAME \
             --range=IPV4_ADDRESS_RANGE \
             --region=REGION \
             --stack-type=IPV4_IPV6 \
             --ipv6-access-type=INTERNAL
         

For IPV4_ADDRESS_RANGE, you can enter any primary IPv4 range for the new subnet, in CIDR notation. For example, `192.168.11.0/24`. For more information, see [IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/vpc#manually_created_subnet_ip_ranges).

  3. Create a firewall rule that allows internal traffic to reach the target instance.
         
         gcloud compute firewall-rules create ALLOW_IPV6_FIREWALL_RULE_NAME \
             --network=VPC_NAME \
             --target-tags=allow-ipv6-int \
             --allow=tcp \
             --source-ranges=::/0
         

  4. Create a firewall rule to allow SSH connectivity to VMs by using the network tag `allow-ssh`.
         
         gcloud compute firewall-rules create ALLOW_SSH_FIREWALL_RULE_NAME \
             --network=VPC_NAME \
             --target-tags=allow-ssh \
             --allow=tcp:22 \
             --source-ranges=0.0.0.0/0
         

This firewall rule is applied to a client VM (created in one of the following steps) that you connect to by using SSH to send HTTP traffic to the IP address of the forwarding rule.

  5. Create a dual-stack VM.
         
         gcloud compute instances create VM_INSTANCE_NAME \
             --subnet=SUBNET_NAME \
             --stack-type=IPV4_IPV6 \
             --zone=ZONE \
             --image-family=debian-12 \
             --image-project=debian-cloud \
             --tags=allow-ipv6-int \
             --metadata=startup-script='#! /bin/bash
             sudo apt-get update
             sudo apt-get install apache2 -y
             sudo a2ensite default-ssl
             sudo a2enmod ssl
             vm_hostname="$(curl -H "Metadata-Flavor:Google" \
             http://metadata.google.internal/computeMetadata/v1/instance/name)"
             echo "Page served from: $vm_hostname" | \
             tee /var/www/html/index.html
             sudo systemctl restart apache2'
         

  6. Create a target instance that contains the VM created in the previous step.
         
         gcloud compute target-instances create TARGET_INSTANCE_NAME \
             --instance=VM_INSTANCE_NAME \
             --network=VPC_NAME \
             --zone=ZONE
         

  7. Create an IPv4 forwarding rule that forwards TCP traffic to the target instance. The forwarding rule must be created in the same region in which the target instance was created.
         
         gcloud compute forwarding-rules create IPV4_FORWARDING_RULE_NAME \
             --load-balancing-scheme=INTERNAL \
             --network-tier=PREMIUM \
             --region=REGION \
             --ip-protocol=TCP \
             --ports=80 \
             --target-instance=TARGET_INSTANCE_NAME \
             --target-instance-zone=ZONE
         

  8. Create an IPv6 forwarding rule that forwards TCP traffic to the target instance. The forwarding rule must be created in the same region in which the target instance was created.
         
         gcloud compute forwarding-rules create IPV6_FORWARDING_RULE_NAME \
             --load-balancing-scheme=INTERNAL \
             --network-tier=PREMIUM \
             --network=VPC_NAME \
             --subnet=SUBNET_NAME \
             --region=REGION \
             --ip-protocol=TCP \
             --ports=80 \
             --target-instance=TARGET_INSTANCE_NAME \
             --target-instance-zone=ZONE \
             --ip-version=IPV6
         

  9. Create a client VM.
         
         gcloud compute instances create CLIENT_VM_NAME \
             --subnet=SUBNET_NAME \
             --stack-type=IPV4_IPV6 \
             --zone=ZONE \
             --image-family=debian-12 \
             --image-project=debian-cloud \
             --tags=allow-ssh
         

  10. Test your setup.

     1. Get the IP address of the forwarding rule.
            
            gcloud compute forwarding-rules describe IPV4_FORWARDING_RULE_NAME \
                --region=REGION
            
            
            gcloud compute forwarding-rules describe IPV6_FORWARDING_RULE_NAME \
                --region=REGION
            

     2. Establish an SSH connection to the client VM.
            
            gcloud compute ssh CLIENT_VM_NAME \
                --zone=ZONE
            

     3. Make an HTTP request to the IP address of the forwarding rule by using curl.

For IPv4 traffic:
            
            while true; do curl -m1 IP_ADDRESS; done
            

For IPv6 traffic:
            
            curl -6 'http://[FORWARDING_RULE_IP_ADDRESS]:80'
            

The output is similar to the following, where the name of the backend VM generating the response is displayed in the text.
            
            Page served from: VM_INSTANCE_NAME.
            




### IPv6 only

Handling only IPv6 traffic requires an IPv6-only subnet with an IPv6-only VM instance for the target instance backend.

  1. Create a custom mode VPC network with the `--enable-ula-internal-ipv6` flag to configure internal IPv6 ranges on any subnets in this network.
         
         gcloud beta compute networks create VPC_NAME \
             --subnet-mode=custom \
             --enable-ula-internal-ipv6
         

  2. Within the VPC network, create an IPv6-only subnet.
         
         gcloud beta compute networks subnets create SUBNET_NAME \
             --network=VPC_NAME \
             --region=REGION \
             --stack-type=IPV6_ONLY \
             --ipv6-access-type=INTERNAL
         

  3. Create a firewall rule that allows internal traffic to reach the target instance.
         
         gcloud beta compute firewall-rules create ALLOW_IPV6_FIREWALL_RULE_NAME \
             --network=VPC_NAME \
             --target-tags=allow-ipv6-int \
             --allow=tcp \
             --source-ranges=::/0
         

  4. Create a firewall rule to allow SSH connectivity to VMs by using the network tag `allow-ssh`.
         
         gcloud beta compute firewall-rules create ALLOW_SSH_FIREWALL_RULE_NAME \
             --network=VPC_NAME \
             --target-tags=allow-ssh \
             --allow=tcp:22 \
             --source-ranges=0.0.0.0/0
         

This firewall rule is applied to a client VM (created in one of the following steps) that you connect to by using SSH to send HTTP traffic to the IP address of the forwarding rule.

  5. Create an IPv6-only VM.
         
         gcloud beta compute instances create VM_INSTANCE_NAME \
             --subnet=SUBNET_NAME \
             --stack-type=IPV6_ONLY \
             --zone=ZONE \
             --image-family=debian-12 \
             --image-project=debian-cloud \
             --tags=allow-ipv6-int \
             --metadata=startup-script='#! /bin/bash
             sudo apt-get update
             sudo apt-get install apache2 -y
             sudo a2ensite default-ssl
             sudo a2enmod ssl
             vm_hostname="$(curl -H "Metadata-Flavor:Google" \
             http://metadata.google.internal/computeMetadata/v1/instance/name)"
             echo "Page served from: $vm_hostname" | \
             tee /var/www/html/index.html
             sudo systemctl restart apache2'
         

  6. Create a target instance that contains the VM created in the previous step.
         
         gcloud beta compute target-instances create TARGET_INSTANCE_NAME \
             --instance=VM_INSTANCE_NAME \
             --network=VPC_NAME \
             --zone=ZONE
         

  7. Create an IPv6 forwarding rule that forwards TCP traffic to the target instance. The forwarding rule must be created in the same region in which the target instance was created.
         
         gcloud beta compute forwarding-rules create IPV6_FORWARDING_RULE_NAME \
             --load-balancing-scheme=INTERNAL \
             --network-tier=PREMIUM \
             --network=VPC_NAME \
             --subnet=SUBNET_NAME \
             --region=REGION \
             --ip-protocol=TCP \
             --ports=80 \
             --target-instance=TARGET_INSTANCE_NAME \
             --target-instance-zone=ZONE \
             --ip-version=IPV6
         

  8. Create a client VM.
         
         gcloud beta compute instances create CLIENT_VM_NAME \
             --subnet=SUBNET_NAME \
             --stack-type=IPV6_ONLY \
             --zone=ZONE \
             --image-family=debian-12 \
             --image-project=debian-cloud \
             --tags=allow-ssh
         

  9. Test your setup.

     1. Get the IP address of the forwarding rule.
            
            gcloud beta compute forwarding-rules describe IPV6_FORWARDING_RULE_NAME \
                --region=REGION
            

     2. Establish an SSH connection to the client VM.
            
            gcloud beta compute ssh CLIENT_VM_NAME \
                --zone=ZONE
            

     3. Make an HTTP request to the IP address of the forwarding rule by using curl.
            
            curl -6 'http://[FORWARDING_RULE_IP_ADDRESS]:80'
            

The output is similar to the following, where the name of the backend VM generating the response is displayed in the text.
            
            Page served from: VM_INSTANCE_NAME.
            




## What's next

  * [Restrict protocol forwarding types](https://docs.cloud.google.com/load-balancing/docs/org-policy-constraints#restrict_protocol_forwarding_types)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
