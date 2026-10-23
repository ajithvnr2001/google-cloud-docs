---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/load-balancer-subnets/
title: Load balancer subnets \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:25:45.347278+00:00
---

# Load balancer subnets  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/load-balancer-subnets/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  Load balancer subnets Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how GKE on AWS works with AWS to choose subnets for Service load balancers, and how to tag subnets to be auto-discovered during Service load balancer creation.

## Why you need to specify subnets

When creating load balancers, AWS needs to know which subnets to place them in. The subnet determines load balancer availability zones, IP addresses, and endpoints.

Normally, load balancers are allocated to one subnet for each availability zone containing a node pool. AWS needs a minimum of one available subnet to create a Network Load Balancer (NLB), and a minimum of two subnets for an Application Load Balancer (ALB).

All AWS subnets are either public (with public IPs and a route to the VPC's internet gateway) or private (lacking these features). Internet-facing load balancers must be located in public subnets. Internal load balancers can reside in either public or private subnets.

### If there are no tagged subnets available

If GKE on AWS needs to create a load balancer and no tagged subnets are available or have capacity, it might create the load balancer in another subnet. To avoid this and control which subnets your load balancers are placed in, you should tag all your subnets.

## Subnet auto-discovery

GKE on AWS will auto-discover subnets to use for a load balancer by listing all the subnets in the VPC, and selecting up to one subnet from each availability zone.

For GKE on AWS to auto-discover a subnet, the subnet must:

  * Be tagged with `kubernetes.io/role/elb` (for an internet-facing load balancer)
  * Be tagged with `kubernetes.io/role/internal-elb` (for an internal load balancer)
  * Either contain no tags with prefix `kubernetes.io/cluster/`, or contain the tag `kubernetes.io/cluster/CLUSTER_UID`, where `CLUSTER_UID` is the current cluster's UID.



In addition, a subnet intended for use with an internet-facing load balancer must have a route to the VPC's internet gateway.

If there are several subnets in an availability zone that satisfy the load balancer's requirements, GKE on AWS ranks subnets in order by their subnet ID.

## Tag your subnets for their intended use

For GKE on AWS to auto-discover a subnet for a load balancer, you must apply one of two tags to the subnet to signal its availability. They are:

  * `kubernetes.io/role/elb`: apply this tag to your subnet to mark it as available for an internet-facing load balancer. This must be a public subnet with a route to your VPC's internet Gateway. Set the tag to `1`. To apply this tag, run the following command:
        
        aws ec2 create-tags \
          --resources SUBNET_ID \
          --tags "Key=kubernetes.io/role/elb,Value=1"
        

  * `kubernetes.io/role/internal-elb`: apply this tag to your subnet to mark it as available for an internal load balancer. Set the tag's value to `1`. To apply this tag, run the following command:
        
        aws ec2 create-tags \
          --resources SUBNET_ID \
          --tags Key=kubernetes.io/role/internal-elb,Value=1
        




Replace the following:

  * `SUBNET_ID`: the ID of the subnet you're tagging



After giving your subnet a `kubernetes.io/role` tag, you can also tag it with one or more `kubernetes.io/cluster/CLUSTER_UID` tags, where CLUSTER_UID is the UID of a GKE on AWS cluster. This prevents any cluster not listed in one of these tags from auto-discovering the subnet for use by its load balancers.

See the Amazon [aws ec2 create-tags](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-tags.html#create-tags) documentation for more information about the `aws ec2 create-tags` command.

## Troubleshooting

The most common problem with load balancer configuration is incorrectly tagged subnets. This can cause the auto-discovery algorithm to select the wrong subnets. To diagnose and resolve this problem:

  * If you're creating an internet-facing load balancer, make sure there is at least one public subnet in each of the availability zones that contain a node pool, and that the subnets are tagged with `kubernetes.io/role/elb`.

  * If you're creating an internal load balancer, make sure there is at least one subnet in each of the availability zones that contain a node pool, and that the subnets are tagged with `kubernetes.io/role/internal-elb`.

  * Check whether the subnets you want auto-discovered have any tags of the form `kubernetes.io/cluster/CLUSTER_UID`. If a subnet has any such tags naming a cluster, the subnet can only be auto-discovered by the named clusters. To resolve this, either delete all cluster name tags (to let the subnet be auto-discovered from any cluster) or add a cluster name tag with your GKE on AWS cluster UID and a value of `shared`.

  * Check the Kubernetes event history with the following command:
        
        kubectl get events -A | grep LoadBalancer
        

For example, the event message `could not find any suitable subnets for creating the ELB` indicates that no subnets could be auto-discovered. If you get this warning, ensure that your subnets and their tags are correct and complete.

  * To list the subnets that can be auto-discovered for internet-facing load balancers, run the following command:
        
        aws ec2 describe-subnets \
          --filters "Name=vpc-id,Values=VPC_ID" "Name=tag:kubernetes.io/role/elb,Values=*"
        

Replace `VPC_ID` with the ID of your VPC.

  * To list the subnets that can be auto-discovered for internal load balancers, run:
        
        aws ec2 describe-subnets \
          --filters "Name=vpc-id,Values=VPC_ID" "Name=tag:kubernetes.io/role/internal-elb,Values=*"
        




## Next steps

  * Learn more about [network load balancing](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/network-load-balancing)

  * [Set up an HTTP Load Balancer](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/http-load-balancing).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
