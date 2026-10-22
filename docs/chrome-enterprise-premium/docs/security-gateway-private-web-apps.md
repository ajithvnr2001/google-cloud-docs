---
url: https://docs.cloud.google.com/chrome-enterprise-premium/docs/security-gateway-private-web-apps/
title: Secure access to private web applications \u00a0|\u00a0 Chrome Enterprise Premium \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:56:06.462813+00:00
---

# Secure access to private web applications  |  Chrome Enterprise Premium  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chrome-enterprise-premium/docs/security-gateway-private-web-apps/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Chrome Enterprise Premium ](https://docs.cloud.google.com/chrome-enterprise-premium/docs)
  * [ Guides ](https://docs.cloud.google.com/chrome-enterprise-premium/docs/overview)



Send feedback 

#  Secure access to private web applications Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to set up a Chrome Enterprise Premium secure gateway for securing access to your private web applications.

A Chrome Enterprise Premium secure gateway functions as a forward proxy, enforcing a zero trust access framework and delivering granular, context-aware control over who accesses your private web applications.

## How securing access to private web applications works

By establishing a secure tunnel and enforcing context-aware access policies, the secure gateway keeps private applications private and shielded from public internet exposure. A client-side browser configuration directs traffic for these applications through the secure gateway proxy endpoint. The secure gateway then applies the relevant access policy and, if permitted, routes the request to the destination application.

The secure gateway can help protect private web applications hosted in the following environments:

  * Google Cloud project: The secure gateway can direct access to applications that are running in your Google Cloud VPC network.

  * Non-Google Cloud (on-premises data centers or other clouds): You must first establish a connection between your private VPC network on Google Cloud and the non-Google Cloud network. This is commonly done using Cloud VPN or Cloud Interconnect. The secure gateway then uses the connection to send the traffic to your private VPC network, which in turn routes it to the non-Google Cloud environment.




### Required roles

Ask your administrator to grant the following roles:

  * [Cloud BeyondCorp Admin (`roles/beyondcorp.admin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/beyondcorp#beyondcorp.admin) to set up Chrome Enterprise Premium on the project

  * [Access Context Manager Admin (`roles/accesscontextmanager.policyAdmin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyAdmin) to read and add new access levels

  * [Service Usage Viewer (`roles/serviceusage.serviceUsageViewer`)](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageViewer) to use the Google Cloud console




Learn more about [Identity and Access Management (IAM) roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

### Required Chrome Enterprise policies

Secure gateway proxy authentication requires the `Basic` HTTP authentication scheme. If you configure Chrome Enterprise authentication policies for your organization, verify the following policy settings:

  * [`AuthSchemes`](https://chromeenterprise.google/policies/#AuthSchemes) must include `basic` authentication (enabled by default when the policy is unset). Other values in this policy don't affect secure gateway proxy authentication.

  * [`BasicAuthOverHttpEnabled`](https://chromeenterprise.google/policies/#BasicAuthOverHttpEnabled) must be set to `0` (`false`, or disabled) to disallow non-secure HTTP connections from using the `Basic` authentication scheme.




## Before you begin

Before setting up the secure gateway, verify that you have the following:

  * A [Chrome Enterprise Premium](https://console.cloud.google.com/security/caa) license.
  * Access to the [Google Admin console](https://admin.google.com) with an administrator account.
  * [Additional Google services without individual control](https://knowledge.workspace.google.com/admin/users/advanced/manage-access-to-services-that-arent-controlled-individually) are turned on.
  * The [Google Cloud service is turned on](https://knowledge.workspace.google.com/admin/users/access/turn-google-cloud-on-or-off-for-users) for your users.
  * A Google Cloud project with an assigned billing account and the following [API enabled](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api): [BeyondCorp API](https://docs.cloud.google.com/beyondcorp/docs/reference/rest)

  * For private applications in a non-Google Cloud environment, a Cloud VPN or Cloud Interconnect connection between your Google Cloud environment and the non-Google Cloud environment where your application resides. For more information about setting up network connections, see the following resources:

    * [Cloud VPN documentation](https://docs.cloud.google.com/network-connectivity/docs/vpn)

    * [Cloud Interconnect documentation](https://docs.cloud.google.com/network-connectivity/docs/interconnect)




## Set up your shell environment

To streamline the setup process and interact with the secure gateway APIs, define the following environment variables in your working shell.

  * General parameters 
        
        PROJECT_ID=PROJECT_ID
              

Replace the following:

    * `PROJECT_ID`: The ID of the project where the secure gateway is created.
  * Secure gateway parameters 
        
        SECURITY_GATEWAY_ID=SECURITY_GATEWAY_ID
        SECURITY_GATEWAY_DISPLAY_NAME="SECURITY_GATEWAY_DISPLAY_NAME"
              

Replace the following:

    * `SECURITY_GATEWAY_ID`: The ID of the secure gateway that you want to create. The ID can be up to 63 characters and can contain lowercase letters, numbers, and hyphens. The first character must be a letter, and the last character can be a letter or number.
    * `SECURITY_GATEWAY_DISPLAY_NAME`: The human-readable name of the secure gateway. The name can be up to 63 characters long and include printable characters.



## Create a secure gateway

A Chrome Enterprise Premium secure gateway is a fundamental building block for establishing secure connections to your applications.

### console

To create a secure gateway, do the following:

  1. In the Google Cloud console, go to the **secure gateway** page.   
[Go to secure gateway](https://console.cloud.google.com/security/cep/secure-gateway)
  2. Select the project you want to create the secure gateway for.
  3. To create a secure gateway, click **Create new gateway** and wait for the gateway creation process to complete. You can track the progress in the **Notifications** section of the Google Cloud console.



### gcloud

To create a secure gateway using gcloud, run the following command:
    
    
    gcloud beyondcorp security-gateways create SECURITY_GATEWAY_ID \
        --project=PROJECT_ID \
        --location=global \
        --display-name="SECURITY_GATEWAY_DISPLAY_NAME" \
        --service-discovery={}
          

### REST

To create a secure gateway using the REST API, run the following command:
    
    
    curl \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        -X POST \
        -d '{ "display_name": "SECURITY_GATEWAY_DISPLAY_NAME", "service_discovery": {} }' \
        "https://beyondcorp.googleapis.com/v1/projects/PROJECT_ID/locations/global/securityGateways?security_gateway_id=SECURITY_GATEWAY_ID"
          

## Configure a private web application

Before you can define specific application resources in the secure gateway, you must configure the necessary permissions and network settings to enable connectivity and proper routing.

### Grant permissions to the service account

To successfully send traffic to your VPC network, the secure gateway needs certain IAM permissions granted to its delegating service account. Doing this allows the secure gateway to reach your private applications, whether they're hosted within a Google Cloud VPC or in a non-Google Cloud environment connected through Cloud VPN or Cloud Interconnect.

To grant permissions to the service account, do the following:

  1. Get the details of your secure gateway to identify the delegating service account email. The email is in the `delegatingServiceAccount` field of the response. 

### gcloud
         
         gcloud beyondcorp security-gateways describe SECURITY_GATEWAY_ID \
             --project=PROJECT_ID \
             --location=global
                        

### REST
         
         curl \
             -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             -H "Content-Type: application/json" \
             "https://beyondcorp.googleapis.com/v1/projects/PROJECT_ID/locations/global/securityGateways/SECURITY_GATEWAY_ID"
                        

  2. Set environment variables for the service account and your target VPC project. To get the service account email, you can use the following command: 
         
         DELEGATING_SERVICE_ACCOUNT=`gcloud beyondcorp security-gateways describe SECURITY_GATEWAY_ID --project=PROJECT_ID --location=global --format="value(delegatingServiceAccount)"`
               

  3. Grant the `roles/beyondcorp.upstreamAccess` IAM role to the delegating service account on your private VPC project. 
         
         gcloud projects add-iam-policy-binding PRIVATE_VPC_PROJECT_ID \
             --role=roles/beyondcorp.upstreamAccess \
             --member=serviceAccount:DELEGATING_SERVICE_ACCOUNT
             

Replace `PRIVATE_VPC_PROJECT_ID` with the Project ID of the VPC network where the private web app is deployed or where Cloud VPN/Interconnect is configured. 



Allow approximately two minutes for the Identity and Access Management policy to take effect after you grant the role.

### Configure network routing and firewall rules

To allow traffic from the secure gateway to reach your private web applications, configure firewall rules, network routing, and DNS settings.

#### Firewall rules for applications in Google Cloud

If your private web application is hosted within your Google Cloud VPC network, such as on a Compute Engine VM, a Google Kubernetes Engine service with an internal IP, or behind an internal TCP/UDP load balancer, configure Google Cloud VPC firewall rules. This allows ingress TCP traffic from the secure gateway IP range: `136.124.16.0/20`.

### gcloud

To create a firewall rule using gcloud, run the following command:
    
    
    gcloud compute firewall-rules create FIREWALL_RULE_NAME \
       --project=PRIVATE_VPC_PROJECT_ID \
       --network=NETWORK_NAME \
       --allow=tcp \
       --source-ranges=136.124.16.0/20
          

Replace the following:

  * `FIREWALL_RULE_NAME`: A name for your firewall rule.
  * `PRIVATE_VPC_PROJECT_ID`: The ID of the project where your VPC network is hosted.
  * `NETWORK_NAME`: The name of the VPC network where your application is hosted.



#### Firewall rules for applications in non-Google Cloud environments

If your private web application resides on an on-premises data center or on another cloud provider's network, and is connected to your Google Cloud VPC using Cloud VPN or Cloud Interconnect, configure firewall rules on your on-premises firewall or the equivalent network security controls, such as security groups and network ACLs, in the other cloud environment. This allows ingress TCP traffic from the secure gateway IP range: `136.124.16.0/20`.

#### Configure routing from non-Google Cloud environments to a secure gateway

To facilitate two-way communication for private applications that are hosted in non-Google Cloud environments, such as on-premises or other clouds, your external network must create a return path to the following secure gateway IP range: `136.124.16.0/20`.

Verify that your private network can reach the secure gateway IP ranges through your Cloud VPN or Cloud Interconnect:

  * **Dynamic routing** : If you're using dynamic routing, such as Border Gateway Protocol (BGP) with Cloud Router, set your VPC network's [dynamic routing mode](https://docs.cloud.google.com/vpc/docs/vpc#routing_for_hybrid_networks) to **Global** so that routes learned through BGP are advertised to all regions within the VPC network. Because a secure gateway is a global service, global dynamic routing ensures that traffic arriving from any region can reach your private application.

Also verify that your Cloud Router in Google Cloud explicitly advertises secure gateway IP ranges to your on-premises BGP device. Although BGP dynamically exchanges many routes, the secure gateway IP ranges require explicit advertisement.

### gcloud

To check if the source range is advertised, run the following command:
        
        gcloud compute routers list-bgp-routes ROUTER_NAME \
        --peer=PEER_NAME \
        --region=REGION \
        --project=PROJECT_ID \
        --route-direction=OUTBOUND \
        --address-family=IPV4 \
        --destination-range=136.124.16.0/20
              

Replace the following:

    * `ROUTER_NAME`: the name of your Cloud Router
    * `PEER_NAME`: the name of your BGP peer
    * `REGION`: the region where your router is located
    * `PROJECT_ID`: the ID of the project containing the router
  * **Static routing** : If you're using static routes, you must manually add routes for each of the secure gateway IP ranges on your on-premises network equipment, such as your router or firewall. These static routes must specify that traffic destined for the secure gateway IP ranges must be sent over the Cloud VPN or Cloud Interconnect connection.

If you configure Cloud VPN with static routes instead of dynamic routing (BGP), those routes are only available in the specific region where the VPN tunnel is established. Because a secure gateway is a global service, ingress traffic arriving from a different region fails to reach your private application because static routes aren't advertised globally across regions. To avoid cross-region routing failures when using static routes, do one of the following:

    * **Switch to dynamic routing (BGP)** : Set your VPC network's [dynamic routing mode](https://docs.cloud.google.com/vpc/docs/vpc#routing_for_hybrid_networks) to **Global** so that routes learned through BGP are available across all regions in the VPC network.

    * **Configure an egress policy** : When you create the application resource, configure an egress policy on the upstream network to force traffic from the secure gateway to egress in the specific region where your Cloud VPN or Cloud Interconnect connection is established.

When using static routing, Cloud VPN must be in one of the following supported regions:

    * `africa-south1`
    * `asia-east1`
    * `asia-east2`
    * `asia-northeast1`
    * `asia-northeast2`
    * `asia-northeast3`
    * `asia-south1`
    * `asia-south2`
    * `asia-southeast1`
    * `asia-southeast2`
    * `asia-southeast3`
    * `australia-southeast2`
    * `europe-central2`
    * `europe-north1`
    * `europe-north2`
    * `europe-southwest1`
    * `europe-west1`
    * `europe-west10`
    * `europe-west12`
    * `europe-west2`
    * `europe-west3`
    * `europe-west4`
    * `europe-west6`
    * `europe-west8`
    * `europe-west9`
    * `me-central1`
    * `me-central2`
    * `me-west1`
    * `northamerica-northeast1`
    * `northamerica-northeast2`
    * `northamerica-south1`
    * `southamerica-east1`
    * `southamerica-west1`
    * `us-central1`
    * `us-central2`
    * `us-east1`
    * `us-east4`
    * `us-east5`
    * `us-east7`
    * `us-south1`
    * `us-west1`
    * `us-west2`
    * `us-west3`
    * `us-west4`
    * `us-west8`



## DNS configuration for secure gateway private hostname resolution

For the secure gateway to resolve your private application hostnames, your Google Cloud VPC network must be able to resolve the hostnames using Cloud DNS. The specific Cloud DNS configuration depends on where your private DNS records are authoritatively hosted:

  * **Applications within Google Cloud using Cloud DNS private zones** : If your private applications are hosted in Google Cloud and their DNS records are managed within Cloud DNS private zones that are associated with your VPC network, verify that the zones are correctly configured and accessible. The secure gateway uses your VPC's existing Cloud DNS resolution capabilities.

  * **Applications in non-Google Cloud environments or using external DNS servers** : If your private applications are in non-Google Cloud environments (on-premises or other clouds) or if their DNS records are managed by DNS servers external to your VPC's Cloud DNS private zones, you must configure Cloud DNS to forward queries for these private domains. This typically involves creating Cloud DNS forwarding zones within your VPC. These zones will direct DNS queries for your specified private domains to your authoritative private DNS servers, such as on-premises or other clouds.




For detailed instructions on DNS configuration, see [Create a forwarding zone](https://docs.cloud.google.com/dns/docs/zones/forwarding-zones).

## Create an application resource

To provide access to a private web application, you must establish the application within the secure gateway framework by creating an application resource. This resource defines how the secure gateway identifies traffic for your application (based on the hostname) and where to route that traffic.

  1. Set the required environment variables by running the following command: 
         
         APPLICATION_ID=APPLICATION_ID
            APP_DISPLAY_NAME="APP_DISPLAY_NAME"
            HOST_NAME=HOST_NAME
            PRIVATE_NETWORK_RESOURCE_NAME=PRIVATE_NETWORK_RESOURCE_NAME
            

Replace the following: 
     * `APPLICATION_ID`: A unique ID for the application resource.
     * `APP_DISPLAY_NAME`: The human-readable name to display.
     * `HOST_NAME`: The primary hostname that users access (for example, `private.local`).
     * `PRIVATE_NETWORK_RESOURCE_NAME`: The full resource name of the VPC network (for example, `projects/my-project/global/networks/my-network`).
  2. Create the application resource. 

### console

To create the application resource by using the Google Cloud console, do the following:

     1. In the Google Cloud console, go to the **secure gateway** page.   
[Go to secure gateway](https://console.cloud.google.com/security/cep/secure-gateway)
     2. To add an application, click **Add application**.
     3. Select the application type: **Private application**.
     4. Enter the application details: 
        * **Application name** : Enter a name, for example, `GitHub`.
        * **Domain matchers** : Enter a comma-separated list of domain patterns to route through the secure gateway. Include the port in the format `domain:port`. Wildcards (`*`) are allowed. For example: `github.com:443`.
     5. Configure VPC Network: 
        * **In current project** : If your VPC network is in the current project, choose the VPC network from the drop-down.
        * **In another project** : If your VPC network is in a different Google Cloud project, specify the full resource name of the VPC network, for example, `projects/my-project/global/networks/my-network`.
     6. Optional: **Define egress policy** : Select one or more Google Cloud regions from the drop-down menu. If you use regional static routes, select the region where your Cloud VPN or Cloud Interconnect connection is established.
     7. Optional: **Define an access policy** : Select an Access Context Manager access policy. You can skip this step for this guide.
     8. To create the application resource, click **Create**.

### gcloud

To create the application resource using gcloud, run the following command:
    
    gcloud beyondcorp security-gateways applications create APPLICATION_ID \
        --project=PROJECT_ID \
        --security-gateway=SECURITY_GATEWAY_ID \
        --location=global \
        --display-name="APP_DISPLAY_NAME" \
        --endpoint-matchers="hostname=HOST_NAME,ports=[443]" \
        --upstreams=network=name="PRIVATE_NETWORK_RESOURCE_NAME"
            

To specify an egress region (for example, when using static routes), include `egressPolicy` in the `--upstreams` flag:
    
    gcloud beyondcorp security-gateways applications create APPLICATION_ID \
        --project=PROJECT_ID \
        --security-gateway=SECURITY_GATEWAY_ID \
        --location=global \
        --display-name="APP_DISPLAY_NAME" \
        --endpoint-matchers="hostname=HOST_NAME,ports=[443]" \
        --upstreams=network=name="PRIVATE_NETWORK_RESOURCE_NAME",egressPolicy=regions=us-central1
            

Replace `us-central1` with the Google Cloud region (such as `europe-west1` or `asia-northeast1`) that aligns with your regional static routing setup. If you don't have specific regional static routing requirements, you can omit the egress policy from your configuration. 

### REST

To create an application resource with the API, complete the following steps:

     1. Create a file named `application.json`.
            
            {
            "display_name": "APP_DISPLAY_NAME",
            "endpoint_matchers": [
               {"hostname": "HOST_NAME", "ports": [443]}
            ],
            "upstreams": [{
               "network": {
                  "name": "PRIVATE_NETWORK_RESOURCE_NAME"
               }
            }]
            }
                     

To specify an egress region (for example, when using static routes), add an `egress_policy` to the upstream configuration:
            
            {
            "display_name": "APP_DISPLAY_NAME",
            "endpoint_matchers": [
               {"hostname": "HOST_NAME", "ports": [443]}
            ],
            "upstreams": [{
               "network": {
                  "name": "PRIVATE_NETWORK_RESOURCE_NAME"
               },
               "egress_policy": {
                  "regions": [
                  "us-central1"
                  ]
               }
            }]
            }
                      

Replace `us-central1` with the Google Cloud region (such as `europe-west1` or `asia-northeast1`) that aligns with your regional static routing setup. If you don't have specific regional static routing requirements, you can omit the egress policy from your configuration. 

     2. Call the [`Create`](https://docs.cloud.google.com/beyondcorp/docs/reference/rest/v1/projects.locations.securityGateways/create) API method.
            
            curl \
                -H "Authorization: Bearer $(gcloud auth print-access-token)" \
                -H "Content-Type: application/json" \
                -X POST \
                -d @application.json \
                "https://beyondcorp.googleapis.com/v1/projects/PROJECT_ID/locations/global/securityGateways/SECURITY_GATEWAY_ID/applications?application_id=APPLICATION_ID"
                      




## Configure an access policy

You can apply an access policy to control access at the application level. If no access policy is configured, access to the application is denied by default. 

### console

### Create a policy for multiple applications

To configure an access policy, do the following:

  1. To create a policy that applies to multiple applications linked to the secure gateway, go to the **Policies** page.   
[Go to Policies](https://console.cloud.google.com/security/cep/secure-gateway/policies)
  2. To add access policies to applications, click **Create Policy**.
  3. From the drop-down list, select the applications that you'd like the policies to apply to.
  4. Add principals to the policy: 

Principals can be users, groups, domains, or service accounts. These principals are granted or denied access based on the access levels you assign.

     1. To add a principal, click **Add principal**.
     2. In the **Principal** field, enter the email address of the user, group, service account, or the domain name.
     3. In the **Access Levels** drop-down, select one or more predefined [Context-Aware Access](https://docs.cloud.google.com/access-context-manager/docs/create-access-policy) levels. Access is granted only if the principal meets the conditions of the selected access levels.

To add more principals, click **Add principal** again and repeat the substeps.

You can create and manage access levels in [**Access Context Manager**](https://console.cloud.google.com/security/access-level).

  5. To apply the policy to the application, click **Create Policy**.



### Modify an application-level access policy

  1. To modify a policy for a single application, go to the **Applications** page.   
[Go to Applications](https://console.cloud.google.com/security/cep/secure-gateway/applications)
  2. To find the application that you want to edit, do the following: 
     1. In the **Applications** list, search for the application that you want to modify.
     2. To view the application details, click the **More actions** menu (more_vert) and select **View Details**.
  3. To edit the application, click **Edit**.
  4. Add principals to the policy: 

Principals can be users, groups, domains, or service accounts. These principals are granted or denied access based on the access levels you assign.

     1. To add a principal, click **Add principal**.
     2. In the **Principal** field, enter the email address of the user, group, service account, or the domain name.
     3. In the **Access Levels** drop-down list, select one or more predefined Context-Aware Access levels. Access is granted only if the principal meets the conditions of the selected access levels.

To add more principals, click **Add principal** again and repeat the substeps.

You can create and manage access levels in [**Access Context Manager**](https://console.cloud.google.com/security/access-level).

  5. To apply the policy to the application, click **Save**.



### gcloud

### Add a Service Discovery gateway-level binding

Before granting a user access to an application, make sure the user has Service Discovery permissions at the Secure Gateway level.
    
    
    gcloud beyondcorp security-gateways add-iam-policy-binding SECURITY_GATEWAY_ID \
        --project=PROJECT_ID \
        --location=global \
        --role="roles/beyondcorp.serviceDiscoveryUser" \
        --member=MEMBER
      

Replace the following:

  * `SECURITY_GATEWAY_ID`: the ID of the secure gateway
  * `PROJECT_ID`: the ID of the project where the secure gateway is configured
  * `MEMBER`: the user, group, or service account that you want to assign the Service Discovery role to. For more information, see [IAM principals](https://docs.cloud.google.com/iam/docs/principals-overview)



### Add an application-level binding
    
    
    gcloud beyondcorp security-gateways applications add-iam-policy-binding APPLICATION_ID \
        --security-gateway=SECURITY_GATEWAY_ID \
        --project=PROJECT_ID \
        --location=global \
        --role="roles/beyondcorp.sgApplicationUser" \
        --member=MEMBER
      

Replace the following:

  * `APPLICATION_ID`: the ID of the application resource
  * `SECURITY_GATEWAY_ID`: the ID of the secure gateway
  * `PROJECT_ID`: the ID of the project where the secure gateway is configured
  * `MEMBER`: the user, group, or service account that you want to assign the Service Discovery role to. For more information, see [IAM principals](https://docs.cloud.google.com/iam/docs/principals-overview)



#### Add a conditional binding

You can also add a binding with conditions. Conditions specify requirements, such as a user's IP address originating from a specific location. (The access level can be defined in either an organization-level access policy or a scoped access policy.)

The following example command grants access only if the source IP address is within a specified access level:
    
    
    gcloud beyondcorp security-gateways applications add-iam-policy-binding APPLICATION_ID \
        --security-gateway=SECURITY_GATEWAY_ID \
        --project=PROJECT_ID \
        --location=global \
        --role="roles/beyondcorp.sgApplicationUser" \
        --member=MEMBER \
        --condition="expression='accessPolicies/1234567890/accessLevels/in_us' in request.auth.access_levels,title=Source IP must be in US"
      

### Remove a Service Discovery gateway-level binding

Revoke a user's Service Discovery permissions at the Secure Gateway level.
    
    
    gcloud beyondcorp security-gateways remove-iam-policy-binding SECURITY_GATEWAY_ID \
        --project=PROJECT_ID \
        --location=global \
        --role="roles/beyondcorp.serviceDiscoveryUser" \
        --member=MEMBER
      

Replace the following:

  * `SECURITY_GATEWAY_ID`: the ID of the secure gateway
  * `PROJECT_ID`: the ID of the project where the secure gateway is configured
  * `MEMBER`: the user, group, or service account that you want to remove the Service Discovery role from. For more information, see [IAM principals](https://docs.cloud.google.com/iam/docs/principals-overview)



### Remove an application-level binding
    
    
    gcloud beyondcorp security-gateways applications remove-iam-policy-binding APPLICATION_ID \
        --security-gateway=SECURITY_GATEWAY_ID \
        --project=PROJECT_ID \
        --location=global \
        --role="roles/beyondcorp.sgApplicationUser" \
        --member=MEMBER
      

Replace the following:

  * `APPLICATION_ID`: the ID of the application resource
  * `SECURITY_GATEWAY_ID`: the ID of the secure gateway
  * `PROJECT_ID`: the ID of the project where the secure gateway is configured
  * `MEMBER`: the user, group, or service account that you want to remove the Service Discovery role from. For more information, see [IAM principals](https://docs.cloud.google.com/iam/docs/principals-overview)



#### Remove a conditional binding

You can also remove a binding with conditions. Conditions specify requirements, such as a user's IP address originating from a specific location. (The access level can be defined in either an organization-level access policy or a scoped access policy.)

The following example command removes a conditional binding with a specified access level:
    
    
    gcloud beyondcorp security-gateways applications remove-iam-policy-binding APPLICATION_ID \
        --security-gateway=SECURITY_GATEWAY_ID \
        --project=PROJECT_ID \
        --location=global \
        --role="roles/beyondcorp.sgApplicationUser" \
        --member=MEMBER \
        --condition="expression='accessPolicies/1234567890/accessLevels/in_us' in request.auth.access_levels,title=Source IP must be in US"
      

### REST

### Safely update an access policy

The `setIamPolicy` command replaces the entire existing policy with the one that you provide. To avoid accidentally removing existing permissions, we recommend that you use the following "read-modify-write" pattern. This pattern helps prevent accidental removal of existing permissions.

  1. **Read** : Save the current access policy to a file.
  2. **Modify** : Edit the policy file locally to add or change permissions.
  3. **Write** : Apply your updated policy file.



### Set a Service Discovery gateway-level policy

To grant service discovery permissions, you must set an access policy on the security gateway instead of an individual application. This follows the same "read-modify-write" pattern.

Retrieve the current policy and save it to a file named `gateway_policy.json`.
    
    
    curl \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://beyondcorp.googleapis.com/v1/projects/PROJECT_ID/locations/global/securityGateways/SECURITY_GATEWAY_ID:getIamPolicy" > gateway_policy.json
      

Next, open the `gateway_policy.json` file in a text editor and add the required principals to the `members` list for the `roles/beyondcorp.serviceDiscoveryUser` role, similar to the application-level modifications.

The `gateway_policy.json` file is similar to the following example:
    
    
    {
      "version": 3,
      "bindings": [
        {
          "role": "roles/beyondcorp.serviceDiscoveryUser",
          "members": [
            "group:existing-group@example.com"
          ]
        }
      ],
      "etag": "BwXN8_d-bOM="
    }
      

You can also add other types of members, such as `serviceAccount`, `user`, `group`, `principal`, and `principalSet`, in policy bindings. For more information, see [IAM principals](https://docs.cloud.google.com/iam/docs/principals-overview).

Apply the updated policy:
    
    
    jq '{policy: .}' gateway_policy.json | curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        -d @- \
        "https://beyondcorp.googleapis.com/v1/projects/PROJECT_ID/locations/global/securityGateways/SECURITY_GATEWAY_ID:setIamPolicy"
      

### Set an application-level access policy

#### Get the current policy

Retrieve the current policy. The `etag` field prevents conflicting updates if multiple administrators make changes simultaneously.

The following command retrieves the policy and saves it to a file named `policy.json`. 
    
    
    curl \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://beyondcorp.googleapis.com/v1/projects/PROJECT_ID/locations/global/securityGateways/SECURITY_GATEWAY_ID/applications/APPLICATION_ID:getIamPolicy" > policy.json
      

Replace the following:

  * `PROJECT_ID`: the ID of the project where the secure gateway is configured
  * `SECURITY_GATEWAY_ID`: the ID of the secure gateway
  * `APPLICATION_ID`: the ID of the application resource



The command creates a `policy.json` file that contains the current policy.

#### Modify the policy file

To grant a group access to use the secure gateway, do the following:

  1. Open the `policy.json` file in a text editor.
  2. Add the group to the `members` list for the `roles/beyondcorp.securityGatewayUser` role.



The `policy.json` file is similar to the following example:
    
    
    {
      "version": 3,
      "bindings": [
        {
          "role": "roles/beyondcorp.sgApplicationUser",
          "members": [
            "group:existing-group@example.com"
          ]
        }
      ],
      "etag": "BwXN8_d-bOM="
    }
          

To add an additional group, add a new entry to the `members` array. Include a comma after the preceding entry. The following example adds `new-group@example.com`:
    
    
    {
      "version": 3,
      "bindings": [
        {
          "role": "roles/beyondcorp.sgApplicationUser",
          "members": [
            "group:existing-group@example.com",
            "group:new-group@example.com"
          ]
        }
      ],
      "etag": "BwXN8_d-bOM="
    }
        

You can also add other types of members, such as `serviceAccount`, `user`, `group`, `principal`, and `principalSet`, in policy bindings. For more information, see [IAM principals](https://docs.cloud.google.com/iam/docs/principals-overview).

#### Apply the updated policy

After editing and saving your `policy.json` file, apply it to the resource using the `setIamPolicy` command. This command uses the `etag` from your file to ensure that you update the correct version.
    
    
    jq '{policy: .}' policy.json | curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        -d @- \
        "https://beyondcorp.googleapis.com/v1/projects/PROJECT_ID/locations/global/securityGateways/SECURITY_GATEWAY_ID/applications/APPLICATION_ID:setIamPolicy"
      

Replace the following:

  * `PROJECT_ID`: the ID of the project where the secure gateway is configured
  * `SECURITY_GATEWAY_ID`: the ID of the secure gateway
  * `APPLICATION_ID`: the ID of the application resource



#### Add a conditional access policy

You can also set access policies with conditions. Conditions specify requirements, such as a user's IP address originating from a specific location. (The access level can be defined in either an organization-level access policy or a scoped access policy.)

The following example policy grants access only if the source IP address is within a specified access level:
    
    
    {
      "version": 3,
      "bindings": [
        {
          "role": "roles/beyondcorp.sgApplicationUser",
          "members": [
            "group:group@example.com"
          ],
          "condition": {
            "expression": "request.auth.access_levels.contains('accessPolicies/1234567890/accessLevels/in_us')",
            "title": "Source IP must be in US"
          }
        }
      ],
      "etag": "BwXN8_d-bOM="
    }
      

To apply this policy, follow the steps described earlier.

### Enhance Security with Context-Aware Access

To further enhance security and ensure that only managed Google Chrome instances can access your web applications through the Security Gateway, we recommend adding a Context-Aware Access (CAA) rule. This rule verifies that the user's Chrome profile is under management, preventing potential misuse from unmanaged or malicious browsers.

Note: This feature requires the installation and setup of the [Endpoint Verification extension](https://docs.cloud.google.com/endpoint-verification/docs/deploying-with-admin-console). 

You can implement this by adding a condition to your [Access Context Manager custom access levels](https://docs.cloud.google.com/access-context-manager/docs/create-custom-access-level). Here is an example condition you can adapt:
    
    
      device.chrome.management_state == ChromeManagementState.CHROME_MANAGEMENT_STATE_PROFILE_MANAGED
      

For more information about how to configure, check, and manage this state, see [Chrome browser attributes](https://docs.cloud.google.com/access-context-manager/docs/browser-attributes).

## Install the Chrome Enterprise Premium extension

The Chrome Enterprise Premium extension is an integral part of a secure gateway, and it helps with authentication. Install the extension for all of the users of the secure gateway. For information about deploying the extension, see [View and configure apps and extensions](https://support.google.com/chrome/a/answer/6177447). To install the Chrome Enterprise Premium extension, do the following:

  1. Go to the [Google Admin console](https://admin.google.com).
  2. Click **Chrome browser > Apps & Extensions**.
  3. Click the **Users & browsers** tab.
  4. To add the Chrome extension, click the **+** button, and then select **Add Chrome app or extension by ID**.
  5. Search for the **Secure Enterprise Browser** extension using the following ID, and then set its installation policy to **Force install** for all of the users in the organization unit or group:
         
         ekajlcmdfcigmdbphhifahdfjbkciflj

  6. Click the installed extension, and in the **Policy for extensions** field, enter the following JSON value:
         
         {
           "securityGateway": {
             "Value": {
               "authentication": {},
               "context": { "resource": "projects/PROJECT_ID/locations/global/securityGateways/SECURITY_GATEWAY_ID" },
               "serviceDiscovery": { "routes": {} }
             }
           }
         }

Replace the following: 

     * `PROJECT_ID`: the ID of the project where the secure gateway is configured
     * `SECURITY_GATEWAY_ID`: the ID of the secure gateway
  7. To save the configuration, click **Save**.




## Legacy PAC file setup

When enabled, **Service Discovery** allows the Chrome Browser client to automatically detect and route traffic to your configured applications through the secure gateway, eliminating the need for manual routing configurations using a PAC file.

If Service Discovery is not enabled on your secure gateway, you have a **legacy setup**. You will need to configure a PAC file to control routing on the Chrome Browser client.

To check whether you have the legacy setup, use the following commands to see if service discovery is enabled:

### gcloud
    
    
    gcloud beyondcorp security-gateways describe SECURITY_GATEWAY_ID \
        --project=PROJECT_ID \
        --location=global | grep -i "serviceDiscovery"
          

### REST
    
    
    curl --silent \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://beyondcorp.googleapis.com/v1/projects/PROJECT_ID/locations/global/securityGateways/SECURITY_GATEWAY_ID" | grep -i "serviceDiscovery"
          

If the command returns no output, your gateway uses the legacy setup. For gateways that use the legacy setup, routing is handled by using a hosted PAC file.

#### Step 1: Create and host the PAC file

  1. Create a file named `pac_config.js` with the following JavaScript, replacing `HOST_NAME` with your application's domain (for example, `myapp.example.com`):
         
         function FindProxyForURL(url, host) {
           const PROXY = "HTTPS via.prod.securegateway.goog:443";
           const sites = ["HOST_NAME"];
         
           for (const site of sites) {
             if (shExpMatch(url, 'https://' + site + '/*') || shExpMatch(url, '*.' + site + '/*')) {
               return PROXY;
             }
           }
           return 'DIRECT';
         }

  2. Upload the PAC file to a hosting service, such as a Cloud Storage bucket.

     * Ensure the file is publicly downloadable.
     * Set the HTTP header `Cache-Control` to `no-cache` so browsers always fetch the latest routing rules.
  3. Copy the public URL of the uploaded PAC file.




#### Step 2: Apply the PAC file in the Google Admin console

  1. Go to the [Google Admin console](https://admin.google.com).
  2. Navigate to **Devices > Chrome > Settings**.
  3. Select your organizational unit or group, then click **Proxy mode**.
  4. Under **Proxy mode** , select **Always use the proxy auto-config specified below**.
  5. Enter the public URL of your hosted PAC file into the provided field.
  6. Click **Save**.



#### Step 3: Configure the Chrome Enterprise Premium extension

The extension is required to handle authentication. This extension policy differs from the standard configuration because it excludes the `serviceDiscovery` block.

  1. In the [Google Admin console](https://admin.google.com), navigate to **Chrome browser > Apps & Extensions**.
  2. Go to the **Users & browsers** tab and ensure the Secure Enterprise Browser extension (`ekajlcmdfcigmdbphhifahdfjbkciflj`) is added and enforced.
  3. Click the extension, and in the **Policy for extensions** field, enter the following JSON value:
         
         {
           "securityGateway": {
             "Value": {
               "authentication": {},
               "context": {
                 "resource": "projects/PROJECT_ID/locations/global/securityGateways/SECURITY_GATEWAY_ID"
               }
             }
           }
         }

  4. Click **Save**.




#### Transition to the service discovery setup

To transition your legacy secure gateway from a PAC file setup to the newer service discovery setup, you must manually enable the feature and update your configurations.

  1. **Enable service discovery on your secure gateway** : Update your existing gateway to enable service discovery.

### gcloud
         
         gcloud beyondcorp security-gateways update SECURITY_GATEWAY_ID \
         --project=PROJECT_ID \
         --location=global \
         --service-discovery={}
               

### REST
         
         curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -d '{ "service_discovery": {} }' \
         "https://beyondcorp.googleapis.com/v1/projects/PROJECT_ID/locations/global/securityGateways/SECURITY_GATEWAY_ID?updateMask=service_discovery"
               

  2. **Set the gateway-level access policy** : Grant users the `roles/beyondcorp.serviceDiscoveryUser` role at the gateway level so they can use service discovery. Follow the instructions in the Add a Service Discovery gateway-level binding section.

  3. **Update the Chrome Enterprise Premium extension configuration** : Follow the instructions in the Install the Chrome Enterprise Premium extension section to update your extension policy. The new JSON configuration must include the `"serviceDiscovery": { "routes": {} }` block.

  4. **Remove the legacy PAC file** : Once service discovery is active, the legacy PAC file is no longer needed.

     1. In the [Google Admin console](https://admin.google.com), navigate to **Devices > Chrome > Settings > User & browser settings > Network**.
     2. Find the **Proxy mode** setting.
     3. Remove the proxy auto-config (PAC) URL or switch the setting from **Always use the proxy auto-config specified below** to an appropriate mode for your network, such as **Allow user to configure**.
     4. Click **Save**.



## End user experience

When the setup is complete, end users who access the protected SaaS application are granted or denied access based on the access policy applied to the application.

### Accessing the application in Chrome

[The Chrome Enterprise Premium extension](https://chromewebstore.google.com/detail/secure-enterprise-browser/ekajlcmdfcigmdbphhifahdfjbkciflj?pli=1) is required to direct traffic through the secure gateway. The extension handles the authentication between the user and the secure gateway. The extension is automatically installed through the domain policy.

When users access the SaaS application that you configured, their traffic goes through the secure gateway, which checks if they satisfy the access policy. If the users pass the access policy checks, they're granted access to the application.

When browser access to the application is rejected by the authorization policy, users receive an `Access denied` message.

## What's next

  * [Troubleshoot secure gateway issues](https://docs.cloud.google.com/chrome-enterprise-premium/docs/troubleshoot-security-gateway)

  * [Manage a secure gateway](https://docs.cloud.google.com/chrome-enterprise-premium/docs/manage-security-gateway)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
