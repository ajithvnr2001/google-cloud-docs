---
url: https://docs.cloud.google.com/iap/docs/tcp-by-host/
title: Set up IAP TCP forwarding \u00a0|\u00a0 Identity-Aware Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:27:20.732514+00:00
---

# Set up IAP TCP forwarding  |  Identity-Aware Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iap/docs/tcp-by-host/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Identity-Aware Proxy ](https://docs.cloud.google.com/iap/docs)
  * [ Guides ](https://docs.cloud.google.com/iap/docs/quickstarts)



Send feedback 

#  Set up IAP TCP forwarding Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to set up and use Identity-Aware Proxy (IAP) TCP forwarding with an IP address or hostname in a Google Cloud or non-Google Cloud environment.

## Overview

You can use the Google Cloud CLI to create tunnels to resources by using a resource private IP address or hostname. If you have external resources in non-Google Cloud environments connected to Google Cloud through Cloud Interconnect or a VPN, you can use IAP TCP forwarding with those resources.

## Before you begin

If you need to tunnel to resources outside Google Cloud, you must have hybrid connectivity configured. Hybrid connectivity is required for connecting your external non-Google Cloud resources to Google Cloud. For more information, see the [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview) or [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn) documentation.

Your cloud router must advertise the IAP-TCP IP range `35.235.240.0/20`, so that the destinations send response traffic back through Cloud VPN or Cloud Interconnect and not through the internet. If you do not have this configuration, you cannot create tunnels to resources external to your Google Cloud project.

To configure your cloud router to advertise the IAP-TCP IP range `35.235.240.0/20`, follow the instructions in [Advertising custom IP ranges](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/advertising-custom-ip).

The following procedures provide Google Cloud CLI examples for completing the tasks. For information about how to interact with destination groups by using the APIs, see [REST Resource: projects.iap_tunnel.locations.destGroups](https://docs.cloud.google.com/iap/docs/reference/rest/v1/projects.iap_tunnel.locations.destGroups).

## Create a tunnel destination group

When you configure a tunnel, you specify a tunnel destination group to use for permission checks. Tunnel destination groups represent resources that have the same tunnel access restrictions. You can create any number of destination groups, each with any number of matching IP ranges or fully qualified domain names (FQDNs). Destination groups can overlap for more flexibility.

When you create a destination group, you must specify a region. For the best results, the region that you specify must match the location of the destination resources. For example, if the resources are connected by a VPN, you must use the region of the VPN gateway.

To create a destination group, you must have the `iap.tunnelDestGroups.create` permission, which you can grant through the `iap.tunnelDestGroupEditor` role. To grant a single role, see [Grant a single role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role) in the IAM documentation.

### Console

  1. Go to the [IAP page](https://console.cloud.google.com/iam-admin/iap) and select a project if one isn't already selected.

  2. On the **SSH and TCP resources** tab, click **Create destination group**.

  3. Enter a name for your group name. The group name can contain only lowercase letters (a-z) and dashes (-).

  4. From the dropdown list, select the region in which to create the destination group.

  5. In the **IP address** section, click **Add row** , and then enter the IP addresses or FQDNs of resources.

An IP range consists of comma-separated ranges using CIDR notation, such as `10.1.2.0/24,172.0.0.0/8`.

An FQDN list is a comma-separated list of hostnames, such as `*.internal.company.com`. You can use wildcards with your FQDN entry.

  6. Click **Create destination group**.




### gcloud
    
    
    gcloud iap tcp dest-groups create YOUR_GROUP_NAME \
      --region=REGION \
      --ip-range-list=IP_RANGE_LIST \
      --fqdn-list=FQDN_LIST
    

Replace the following:

  * `YOUR_GROUP_NAME`: your group name. A group name can contain only lowercase letters (a-z) and dashes (-).
  * `REGION`: the region in which to create the destination group, such as `us-central1`.
  * `IP_RANGE_LIST`: optional. The IP range list, which consists of comma-separated ranges using CIDR notation, such as `10.1.2.0/24,172.0.0.0/8`.
  * `FQDN_LIST`: optional. The FQDN list is a comma-separated list of hostnames, such as `*.internal.company.com`. If an FQDN entry has a wildcard prefix, it will match any hostname with the specified ending. Otherwise, it requires an exact match. If a request matches any IP range or FQDN, it is considered a match.



If you're unsure of what groups already exist, run the following command to list the groups:
    
    
    gcloud iap tcp dest-groups list \
      --region=REGION
    

## Managing tunnel destination groups

You can view the details of a destination group, modify the destination group, and remove it.

### Console

  1. Go to the [IAP page](https://console.cloud.google.com/iam-admin/iap) and click the **SSH and TCP resources** tab.

     * To view the details of a destination group, click the name of the destination group.

     * To modify a destination group, select the destination group, and then click the pencil icon to open the **Edit destination group** panel. You can also delete the destination group from this panel.

     * To remove a destination group, select the destination group, and then click the garbage can icon.




### gcloud

For details about how to manage destination groups using the gcloud CLI, see [destination group gcloud commands](https://docs.cloud.google.com/sdk/gcloud/reference/iap/tcp/dest-groups).

## Configuring tunnel permissions

To create a tunnel, you must have the `iap.tunnelDestGroups.accessViaIAP` permission on the relevant destination group. You can grant the permission through the `iap.tunnelResourceAccessor` role.

To configure permissions on destination groups, you must have the `iap.tunnelDestGroups.setIamPolicy` permission, which you can grant through the `iap.admin` role.

### Console

  1. Go to the [IAP page](https://console.cloud.google.com/iam-admin/iap).

  2. On the **SSH and TCP resources** tab, select the destination group for which you want to configure permissions.

  3. In the panel that opens, click **Add principal** and enter an email address for the user.

  4. In the **Assign roles** section, select a role to assign to the principal.

  5. Click **Save**.




### gcloud
    
    
    gcloud iap tcp dest-groups add-iam-policy-binding \
      --member=MEMBER \
      --role=ROLE \
      --dest-group=GROUP_NAME \
      --region=REGION
    

Replace the following:

  * MEMBER: the email address for the user, such as `user:exampleuser@company.com`.

  * ROLE: the required IAP role, `roles/iap.tunnelResourceAccessor`.

  * GROUP_NAME: the destination group name.

  * REGION: the name of the region, such as `us-central1`.




## Understanding tunnel usage

There are three gcloud CLI commands that you can use when working with IAP-TCP: [start-iap-tunnel](https://docs.cloud.google.com/sdk/gcloud/reference/compute/start-iap-tunnel), [ssh](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssh), and [scp](https://docs.cloud.google.com/sdk/gcloud/reference/compute/scp).

The IAP-TCP commands have been updated to support IP- and FQDN-based tunneling. To switch to IP address or FQDN, do the following when using the commands:

  * Specify an IP address or FQDN instead of the instance name.
  * Use `--region` instead of `--zone`.
  * Use `--dest-group` to specify the destination group to use.
  * Use `--network` to specify the name of the VPC network to use.



The IP address you specify must be the private IP address of the destination. You cannot use IAP-TCP with public IP addresses. If you use FQDN, it must resolve to the private IP address of the destination. Note that the name resolution is done from within the VPC network you specify, not from the client's network. For example, if you're attempting to create a tunnel to `vm.corp.company.com`, the step that converts `vm.corp.company.com` to an IP address happens within the context of the VPC network.

The region you specify must match the region of the destination group.

The network you specify must match the name of the VPC network that has access to the destination. A typical network name is `default`. You can view the list of network names on the VPC networks page in the Google Cloud console, or you can retrieve the list of network names by running the following command:
    
    
    gcloud compute networks list --format='value(name)'
    

## Examples

The following examples use an example IP address of `172.16.1.2`. Each command can also take an FQDN (for example, `example.internal.company.com`) in place of the IP address.

### SSH example

To start an SSH session to `172.16.1.2`, run the following command:
    
    
    gcloud compute ssh 172.16.1.2 \
        --region=us-central1 \
        --dest-group=DESTINATION_GROUP_NAME \
        --network=default \
        --tunnel-through-iap
    

Replace `DESTINATION_GROUP_NAME` with the destination group name.

Note that `--plain` is implied, so there is no attempt to automatically manage and push SSH keys when using an IP address.

If you receive the error `Permission denied (publickey)`, the command did not find the file that contains the SSH keys. To resolve this issue, add the path to the file containing the SSH private keys as a parameter for the SSH command, as shown in the following example:
    
    
    gcloud compute ssh 172.16.1.2 \
        --region=us-central1 \
        --dest-group=DESTINATION_GROUP_NAME \
        --network=default \
        --tunnel-through-iap \
        -- -i ~/.ssh/google_compute_engine
    

Replace DESTINATION_GROUP_NAME with the destination group name.

If you want to sign in as a specific user, use the format `USER`@`IP` instead of specifying the IP only:
    
    
    gcloud compute ssh user@172.16.1.2 \
        --region=us-central1 \
        --dest-group=DESTINATION_GROUP_NAME \
        --network=default \
        --tunnel-through-iap
    

If the account is password protected, you must enter a password. If the account is protected by a private or public SSH key pair, you must specify it using the `-- -i` flag as specified above.

### Tunnel example

To establish a tunnel to a different TCP port, use the `start-iap-tunnel` command. To create a tunnel from `localhost:8022` to port `172.16.1.2:8085`, run the following command:
    
    
    gcloud compute start-iap-tunnel 172.16.1.2 8085 \
        --local-host-port=localhost:8022 \
        --region=us-central1 \
        --dest-group=DESTINATION_GROUP_NAME \
        --network=default
    

Note that the destination machine must be listening to port `8085` in this example.

After you establish a tunnel, you can use any tool, such as PuTTY, to establish a connection.

### SCP example

To copy a file to `172.16.1.2` using SCP, run the following command:
    
    
    gcloud compute scp file.txt 172.16.1.2:~/ \
        --region=us-central1 \
        --dest-group=DESTINATION_GROUP_NAME \
        --network=default \
        --tunnel-through-iap
    

Note that `--plain` is implied, so there is no attempt to automatically manage and push SSH keys when using an IP address.

### SSH ProxyCommand example

To use the command as a ProxyCommand that always tunnels to `172.16.1.2`, add an entry to your `~/.ssh/config` configuration or equivalent, as shown in the following example:
    
    
    Host example
    ProxyCommand gcloud compute start-iap-tunnel 172.16.1.2 '%p' --region=us-central1 --dest-group=DESTINATION_GROUP_NAME --network=default --verbosity=warning
      

The ProxyCommand takes effect when you run the following command: `ssh example`

You can also set up the ProxyCommand to handle many hostnames, as shown in the following example: 
    
    
    Host *.internal.company.com
    ProxyCommand gcloud compute start-iap-tunnel '%h' '%p' --region=us-central1 --dest-group=DESTINATION_GROUP_NAME --network=default --verbosity=warning
    

The ProxyCommand takes effect when you run the following command: `ssh example.internal.company.com`

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
