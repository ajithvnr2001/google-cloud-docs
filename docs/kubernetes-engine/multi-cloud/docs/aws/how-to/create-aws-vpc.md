---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-aws-vpc/
title: Create an AWS VPC \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:34.650516+00:00
---

# Create an AWS VPC  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-aws-vpc/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  Create an AWS VPC Stay organized with collections  Save and categorize content based on your preferences. 

GKE on AWS runs in an AWS Virtual Private Cloud (VPC). This page explains how to set up a new VPC for your cluster.

GKE on AWS creates and manages resources within the VPC that you specify. You must also create several subnets inside the VPC:

  * Up to three subnets for the control plane nodes
  * A subnet for the node pool
  * Subnets for Kubernetes Service load balancers



This page is for Networking specialists who want to install, configure, and support network equipment. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Sample VPC

Follow these steps to set up the VPC illustrated below. For your own production use cases, you can choose different IP ranges, availability zones, subnets, and network access control lists suited to your workloads.

The following diagram shows the sample VPC you create when following these steps:

![Sample VPC](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/images/vpc-with-nat-and-load-balancer.svg)

  * This example uses three availability zones— _Availability Zone 1_ , _Availability Zone 2_ , _Availability Zone 3_. For example, to create a VPC in the `us-east-1` region, these could be set to `us-east-1a`, `us-east-1b`, `us-east-1c`.

  * Within each of the three availability zones there is one public subnet and one private subnet.

  * Control plane replicas and load balancer endpoints, as well as node pools are created in the private subnets.

  * Public subnets provide outbound internet access for the private subnets and public load balancer endpoints.

  * All of these subnets are [tagged for subnet auto-discovery](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/load-balancer-subnets). Internal load balancers will be provisioned in the private subnets, and internet-facing load balancers in the public subnets.




### Create your VPC

  1. Choose a prefix and edit the page variable AMC_PREFIX in the command below to set it to the prefix you've chosen. The sample commands below will then automatically attach this prefix to all references to your VPC and its resources.

  2. Create an AWS Virtual Private Cloud (VPC):
         
         aws --region AWS_REGION ec2 create-vpc \
             --cidr-block 10.0.0.0/16 \
             --tag-specifications 'ResourceType=vpc, Tags=[{Key=Name,Value=AMC_PREFIXVPC}]'
         

Replace the following:

     * `AWS_REGION`: the name of the [Supported AWS region](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/supported-regions) to create the VPC in
     * `AMC_PREFIX`: the VPC name prefix you've chosen for your VPC and its resources
  3. Save your VPC ID to an environment variable and enable AWS-provided DNS support for the VPC:
         
         VPC_ID=$(aws ec2 describe-vpcs \
           --filters 'Name=tag:Name,Values=AMC_PREFIXVPC' \
           --query "Vpcs[].VpcId" --output text)
         aws ec2 modify-vpc-attribute --enable-dns-hostnames --vpc-id $VPC_ID
         aws ec2 modify-vpc-attribute --enable-dns-support --vpc-id $VPC_ID
         

You can also use different DNS settings for your VPC. For more information, see [AWS VPC DNS](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/service-discovery-dns#aws_vpc_dns).




### Control plane subnets

You can configure up to three subnets for control plane replicas. If you specify fewer than three subnets, GKE on AWS creates three control plane replicas and distributes them across the specified subnets.

Clusters are private to your VPC. Direct inbound access to clusters from the internet is not permitted. GKE on AWS requires limited outbound internet access to create and manage clusters. This example uses an internet Gateway for outbound access.

#### Subnet requirements

Subnets must

  * Be able to resolve DNS addresses
  * Be able to establish outbound TCP connections on port 443 to routable IP addresses
  * Be able to connect to the following endpoints:

Endpoint | Purpose  
---|---  
storage.googleapis.com | To download from Cloud Storage during installation  
*.gcr.io | To download from Container Registry during installation  
gkeconnect.googleapis.com | To connect to the management service  
oauth2.googleapis.com | For cluster authentication  
sts.googleapis.com | For cluster authentication  
logging.googleapis.com | For sending logs to Cloud Logging  
monitoring.googleapis.com | For sending metrics to Cloud Monitoring  
opsconfigmonitoring.googleapis.com` | For sending resource metadata to Cloud Monitoring  
servicecontrol.googleapis.com | For Cloud Audit Logging  
  
If you don't have subnets for your control plane instances, use the following commands to create them.

### Create private subnets

Create three private subnets in their corresponding availability zones:
    
    
       aws ec2 create-subnet \
         --availability-zone AWS_ZONE_1 \
         --vpc-id $VPC_ID \
         --cidr-block 10.0.1.0/24 \
         --tag-specifications 'ResourceType=subnet, Tags=[{Key=Name,Value=AMC_PREFIXPrivateSubnet1}]'
       aws ec2 create-subnet \
         --availability-zone AWS_ZONE_2 \
         --vpc-id $VPC_ID \
         --cidr-block 10.0.2.0/24 \
         --tag-specifications 'ResourceType=subnet, Tags=[{Key=Name,Value=AMC_PREFIXPrivateSubnet2}]'
       aws ec2 create-subnet \
         --availability-zone AWS_ZONE_3 \
         --vpc-id $VPC_ID \
         --cidr-block 10.0.3.0/24 \
         --tag-specifications 'ResourceType=subnet, Tags=[{Key=Name,Value=AMC_PREFIXPrivateSubnet3}]'
    

Replace the following:

  * `AWS_ZONE_1`: _Availability Zone 1_
  * `AWS_ZONE_2`: _Availability Zone 2_
  * `AWS_ZONE_3`: _Availability Zone 3_



### Create public subnets

  1. Create three public subnets. These will be used to provide outbound internet access for the private subnets.
         
         aws ec2 create-subnet \
           --availability-zone AWS_ZONE_1 \
           --vpc-id $VPC_ID \
           --cidr-block 10.0.101.0/24 \
           --tag-specifications 'ResourceType=subnet, Tags=[{Key=Name,Value=AMC_PREFIXPublicSubnet1}]'
         aws ec2 create-subnet \
           --availability-zone AWS_ZONE_2 \
           --vpc-id $VPC_ID \
           --cidr-block 10.0.102.0/24 \
           --tag-specifications 'ResourceType=subnet, Tags=[{Key=Name,Value=AMC_PREFIXPublicSubnet2}]'
         aws ec2 create-subnet \
           --availability-zone AWS_ZONE_3 \
           --vpc-id $VPC_ID \
           --cidr-block 10.0.103.0/24 \
           --tag-specifications 'ResourceType=subnet, Tags=[{Key=Name,Value=AMC_PREFIXPublicSubnet3}]'
         

Replace the following:

     * `AWS_ZONE_1`
     * `AWS_ZONE_2`
     * `AWS_ZONE_3`
  2. Mark the subnets as public:
         
         PUBLIC_SUBNET_ID_1=$(aws ec2 describe-subnets \
           --filters 'Name=tag:Name,Values=AMC_PREFIXPublicSubnet1' \
           --query "Subnets[].SubnetId" --output text)
         PUBLIC_SUBNET_ID_2=$(aws ec2 describe-subnets \
           --filters 'Name=tag:Name,Values=AMC_PREFIXPublicSubnet2' \
           --query "Subnets[].SubnetId" --output text)
         PUBLIC_SUBNET_ID_3=$(aws ec2 describe-subnets \
           --filters 'Name=tag:Name,Values=AMC_PREFIXPublicSubnet3' \
           --query "Subnets[].SubnetId" --output text)
         aws ec2 modify-subnet-attribute \
           --map-public-ip-on-launch \
           --subnet-id $PUBLIC_SUBNET_ID_1
         aws ec2 modify-subnet-attribute \
           --map-public-ip-on-launch \
           --subnet-id $PUBLIC_SUBNET_ID_2
         aws ec2 modify-subnet-attribute \
           --map-public-ip-on-launch \
           --subnet-id $PUBLIC_SUBNET_ID_3
         




### Create an internet gateway

  1. Create an internet gateway so the public subnets have access to the internet:
         
         aws --region AWS_REGION  ec2 create-internet-gateway \
           --tag-specifications 'ResourceType=internet-gateway, Tags=[{Key=Name,Value=AMC_PREFIXInternetGateway}]'
         

Replace `AWS_REGION`: the name of the AWS region where your VPC was created.

  2. Attach the internet gateway to your VPC:
         
         INTERNET_GW_ID=$(aws ec2 describe-internet-gateways \
           --filters 'Name=tag:Name,Values=AMC_PREFIXInternetGateway' \
           --query "InternetGateways[].InternetGatewayId" --output text)
         aws ec2 attach-internet-gateway \
           --internet-gateway-id $INTERNET_GW_ID \
           --vpc-id $VPC_ID
         




### Configure the routing tables for public subnets

  1. Create a route table for each of the public subnets.
         
         aws ec2 create-route-table --vpc-id $VPC_ID \
           --tag-specifications 'ResourceType=route-table, Tags=[{Key=Name,Value=AMC_PREFIXPublicRouteTbl1}]'
         aws ec2 create-route-table --vpc-id $VPC_ID \
           --tag-specifications 'ResourceType=route-table, Tags=[{Key=Name,Value=AMC_PREFIXPublicRouteTbl2}]'
         aws ec2 create-route-table --vpc-id $VPC_ID \
           --tag-specifications 'ResourceType=route-table, Tags=[{Key=Name,Value=AMC_PREFIXPublicRouteTbl3}]'
         

  2. Associate the public route tables with the public subnets:
         
         PUBLIC_ROUTE_TABLE_ID_1=$(aws ec2 describe-route-tables \
             --filters 'Name=tag:Name,Values=AMC_PREFIXPublicRouteTbl1' \
             --query "RouteTables[].RouteTableId" --output text)
         PUBLIC_ROUTE_TABLE_ID_2=$(aws ec2 describe-route-tables \
             --filters 'Name=tag:Name,Values=AMC_PREFIXPublicRouteTbl2' \
             --query "RouteTables[].RouteTableId" --output text)
         PUBLIC_ROUTE_TABLE_ID_3=$(aws ec2 describe-route-tables \
             --filters 'Name=tag:Name,Values=AMC_PREFIXPublicRouteTbl3' \
             --query "RouteTables[].RouteTableId" --output text)
         aws ec2 associate-route-table \
           --route-table-id $PUBLIC_ROUTE_TABLE_ID_1 \
           --subnet-id $PUBLIC_SUBNET_ID_1
         aws ec2 associate-route-table \
           --route-table-id $PUBLIC_ROUTE_TABLE_ID_2 \
           --subnet-id $PUBLIC_SUBNET_ID_2
         aws ec2 associate-route-table \
           --route-table-id $PUBLIC_ROUTE_TABLE_ID_3 \
           --subnet-id $PUBLIC_SUBNET_ID_3
         

  3. Create default routes to the internet gateway:
         
         aws ec2 create-route --route-table-id $PUBLIC_ROUTE_TABLE_ID_1 \
           --destination-cidr-block 0.0.0.0/0 --gateway-id $INTERNET_GW_ID
         aws ec2 create-route --route-table-id $PUBLIC_ROUTE_TABLE_ID_2 \
           --destination-cidr-block 0.0.0.0/0 --gateway-id $INTERNET_GW_ID
         aws ec2 create-route --route-table-id $PUBLIC_ROUTE_TABLE_ID_3 \
           --destination-cidr-block 0.0.0.0/0 --gateway-id $INTERNET_GW_ID
         

  4. Allocate an Elastic IP (EIP) address for each NAT gateway:
         
         aws ec2 allocate-address \
           --tag-specifications 'ResourceType=elastic-ip, Tags=[{Key=Name,Value=AMC_PREFIXNatEip1}]'
         aws ec2 allocate-address \
           --tag-specifications 'ResourceType=elastic-ip, Tags=[{Key=Name,Value=AMC_PREFIXNatEip2}]'
         aws ec2 allocate-address \
           --tag-specifications 'ResourceType=elastic-ip, Tags=[{Key=Name,Value=AMC_PREFIXNatEip3}]'
         




### Create NAT gateways

Create a NAT gateway in each of the three public subnets:
    
    
       NAT_EIP_ALLOCATION_ID_1=$(aws ec2 describe-addresses \
         --filters 'Name=tag:Name,Values=AMC_PREFIXNatEip1' \
         --query "Addresses[].AllocationId" --output text)
       NAT_EIP_ALLOCATION_ID_2=$(aws ec2 describe-addresses \
         --filters 'Name=tag:Name,Values=AMC_PREFIXNatEip2' \
         --query "Addresses[].AllocationId" --output text)
       NAT_EIP_ALLOCATION_ID_3=$(aws ec2 describe-addresses \
         --filters 'Name=tag:Name,Values=AMC_PREFIXNatEip3' \
         --query "Addresses[].AllocationId" --output text)
       aws ec2 create-nat-gateway \
         --allocation-id $NAT_EIP_ALLOCATION_ID_1 \
         --subnet-id $PUBLIC_SUBNET_ID_1 \
         --tag-specifications 'ResourceType=natgateway, Tags=[{Key=Name,Value=AMC_PREFIXNatGateway1}]'
       aws ec2 create-nat-gateway \
         --allocation-id $NAT_EIP_ALLOCATION_ID_2 \
         --subnet-id $PUBLIC_SUBNET_ID_2 \
         --tag-specifications 'ResourceType=natgateway, Tags=[{Key=Name,Value=AMC_PREFIXNatGateway2}]'
       aws ec2 create-nat-gateway \
         --allocation-id $NAT_EIP_ALLOCATION_ID_3 \
         --subnet-id $PUBLIC_SUBNET_ID_3 \
         --tag-specifications 'ResourceType=natgateway, Tags=[{Key=Name,Value=AMC_PREFIXNatGateway3}]'
    

### Configure the routing tables for private subnets

  1. Create a route table for each private subnet:
         
         aws ec2 create-route-table --vpc-id $VPC_ID \
           --tag-specifications 'ResourceType=route-table, Tags=[{Key=Name,Value=AMC_PREFIXPrivateRouteTbl1}]'
         aws ec2 create-route-table --vpc-id $VPC_ID \
           --tag-specifications 'ResourceType=route-table, Tags=[{Key=Name,Value=AMC_PREFIXPrivateRouteTbl2}]'
         aws ec2 create-route-table --vpc-id $VPC_ID \
           --tag-specifications 'ResourceType=route-table, Tags=[{Key=Name,Value=AMC_PREFIXPrivateRouteTbl3}]'
         

  2. Associate the private route tables with the private subnets:
         
         PRIVATE_SUBNET_ID_1=$(aws ec2 describe-subnets \
           --filters 'Name=tag:Name,Values=AMC_PREFIXPrivateSubnet1' \
           --query "Subnets[].SubnetId" --output text)
         PRIVATE_SUBNET_ID_2=$(aws ec2 describe-subnets \
           --filters 'Name=tag:Name,Values=AMC_PREFIXPrivateSubnet2' \
           --query "Subnets[].SubnetId" --output text)
         PRIVATE_SUBNET_ID_3=$(aws ec2 describe-subnets \
           --filters 'Name=tag:Name,Values=AMC_PREFIXPrivateSubnet3' \
           --query "Subnets[].SubnetId" --output text)
         PRIVATE_ROUTE_TABLE_ID_1=$(aws ec2 describe-route-tables \
           --filters 'Name=tag:Name,Values=AMC_PREFIXPrivateRouteTbl1' \
           --query "RouteTables[].RouteTableId" --output text)
         PRIVATE_ROUTE_TABLE_ID_2=$(aws ec2 describe-route-tables \
           --filters 'Name=tag:Name,Values=AMC_PREFIXPrivateRouteTbl2' \
           --query "RouteTables[].RouteTableId" --output text)
         PRIVATE_ROUTE_TABLE_ID_3=$(aws ec2 describe-route-tables \
           --filters 'Name=tag:Name,Values=AMC_PREFIXPrivateRouteTbl3' \
           --query "RouteTables[].RouteTableId" --output text)
         aws ec2 associate-route-table --route-table-id $PRIVATE_ROUTE_TABLE_ID_1 \
           --subnet-id $PRIVATE_SUBNET_ID_1
         aws ec2 associate-route-table --route-table-id $PRIVATE_ROUTE_TABLE_ID_2 \
           --subnet-id $PRIVATE_SUBNET_ID_2
         aws ec2 associate-route-table --route-table-id $PRIVATE_ROUTE_TABLE_ID_3 \
           --subnet-id $PRIVATE_SUBNET_ID_3
         

  3. Create the default routes to NAT gateways:
         
         NAT_GW_ID_1=$(aws ec2 describe-nat-gateways \
          --filter 'Name=tag:Name,Values=AMC_PREFIXNatGateway1' \
          --query "NatGateways[].NatGatewayId" --output text)
         NAT_GW_ID_2=$(aws ec2 describe-nat-gateways \
          --filter 'Name=tag:Name,Values=AMC_PREFIXNatGateway2' \
          --query "NatGateways[].NatGatewayId" --output text)
         NAT_GW_ID_3=$(aws ec2 describe-nat-gateways \
          --filter 'Name=tag:Name,Values=AMC_PREFIXNatGateway3' \
          --query "NatGateways[].NatGatewayId" --output text)
         aws ec2 create-route --route-table-id $PRIVATE_ROUTE_TABLE_ID_1  \
           --destination-cidr-block 0.0.0.0/0 --gateway-id $NAT_GW_ID_1
         aws ec2 create-route --route-table-id $PRIVATE_ROUTE_TABLE_ID_2  \
           --destination-cidr-block 0.0.0.0/0 --gateway-id $NAT_GW_ID_2
         aws ec2 create-route --route-table-id $PRIVATE_ROUTE_TABLE_ID_3 \
           --destination-cidr-block 0.0.0.0/0 --gateway-id $NAT_GW_ID_3
         




### Node pool subnets

Each node pool is placed in a single subnet. You can place multiple node pools in a subnet. The number of nodes and node pools you can create is limited by the IP address range available in the subnet.

Each node pool subnet must:

  * Satisfy the same outbound internet access requirements as your control plane subnets
  * Have enough IP address space to cover the size of the node pool
  * Not have "Auto-assign public IPs" enabled



The private subnets created earlier satisfy the requirements for both control plane subnets, and node pool subnets.

### Service load balancer subnets

If you are creating [network load balancers](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/network-load-balancing) or [HTTP load balancers](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/http-load-balancing), [tag load balancer subnets](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/load-balancer-subnets) for auto-discovery.

Tag the public subnets with `kubernetes.io/role/elb`:
    
    
    aws ec2 create-tags \
      --resources $PUBLIC_SUBNET_ID_1 \
      --tags Key=kubernetes.io/role/elb,Value=1
    aws ec2 create-tags \
      --resources $PUBLIC_SUBNET_ID_2 \
      --tags Key=kubernetes.io/role/elb,Value=1
    aws ec2 create-tags \
      --resources $PUBLIC_SUBNET_ID_3 \
      --tags Key=kubernetes.io/role/elb,Value=1
    

Tag the private subnets with `kubernetes.io/role/internal-elb`:
    
    
    aws ec2 create-tags \
      --resources $PRIVATE_SUBNET_ID_1 \
      --tags Key=kubernetes.io/role/internal-elb,Value=1
    aws ec2 create-tags \
      --resources $PRIVATE_SUBNET_ID_2 \
      --tags Key=kubernetes.io/role/internal-elb,Value=1
    aws ec2 create-tags \
      --resources $PRIVATE_SUBNET_ID_3 \
      --tags Key=kubernetes.io/role/internal-elb,Value=1
    

## What's next

[Create AWS KMS keys](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-aws-kms-key).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
