---
url: https://docs.cloud.google.com/chrome-enterprise-premium/docs/security-gateway-saas-apps/
title: Secure access to SaaS applications \u00a0|\u00a0 Chrome Enterprise Premium \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:44:55.649854+00:00
---

# Secure access to SaaS applications  |  Chrome Enterprise Premium  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chrome-enterprise-premium/docs/security-gateway-saas-apps/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Chrome Enterprise Premium ](https://docs.cloud.google.com/chrome-enterprise-premium/docs)
  * [ Guides ](https://docs.cloud.google.com/chrome-enterprise-premium/docs/overview)



Send feedback 

#  Secure access to SaaS applications Stay organized with collections  Save and categorize content based on your preferences. 

This page guides you through the process of securing your SaaS applications through the Chrome Enterprise Premium secure gateway.

A Chrome Enterprise Premium secure gateway functions as a forward proxy, enforcing a zero trust access framework and delivering granular, context-aware control over who accesses your SaaS applications.

## How securing access to SaaS applications works

The following is a high level overview of how a secure gateway protects your SaaS applications:

  1. The client-side browser settings route application traffic through a secure gateway proxy.
  2. The secure gateway checks Context-Aware Access policies to authorize client (user and device) access.
  3. If client access is allowed, the gateway forwards traffic to the application using unique source IP addresses assigned to that gateway and Google Cloud region. These assigned IP addresses are reserved exclusively for the gateway that you create and cannot be used by other users or gateways. To control access, you can add these dedicated source IP addresses to an allowlist in your SaaS application.



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

  * A SaaS application that you want to protect. The application must support `IP allowlisting` to enforce security checks by the secure gateway.




### Limitations

A Chrome Enterprise Premium secure gateway has the following limitations:

  * IPv6 connectivity: Chrome Enterprise Premium secure gateway doesn't support SaaS applications that use IPv6 connectivity.
  * Identity provider as a SaaS application: An Identity provider must not be configured as a SaaS application to be protected by the secure gateway, if the end-user's authentication with secure gateway is dependent on the same IdP.



## Set up your shell environment

To streamline the setup process and interact with the secure gateway APIs, define the following environment variables in your working shell.

  * General parameters
        
        PROJECT_ID=PROJECT_ID
        APPLICATION_ID=APPLICATION_ID
        APPLICATION_DISPLAY_NAME="APPLICATION_DISPLAY_NAME"
        HOST_NAME=HOST_NAME

Replace the following:

    * `PROJECT_ID`: The ID of the project where the secure gateway is created.
    * `APPLICATION_ID`: The ID of your application, such as `github`. The name can be up to 63 characters, and can contain lowercase letters, numbers, and hyphens. The first character must be a letter, and the last character can be a letter or number.
    * `APPLICATION_DISPLAY_NAME`: The human-readable name to display.
    * `HOST_NAME`: The hostname of your application. For example, `github.com`. The hostname can be up to 253 characters long, and must adhere to one of the following formats:

      * A valid IPv4 address
      * A valid IPv6 address
      * A [valid DNS](https://datatracker.ietf.org/doc/html/rfc1034) name
      * An asterisk (*)
      * An asterisk (*) followed by a valid DNS name
  * Secure gateway parameters
        
        SECURITY_GATEWAY_ID=SECURITY_GATEWAY_ID
        SECURITY_GATEWAY_DISPLAY_NAME="SECURITY_GATEWAY_DISPLAY_NAME"

Replace the following:

    * `SECURITY_GATEWAY_ID`: The ID of the secure gateway. The ID can be up to 63 characters, and can contain lowercase letters, numbers, and hyphens. The first character should be a letter, and the last character can be a letter or number.
    * `SECURITY_GATEWAY_DISPLAY_NAME`: The human-readable name of the secure gateway. The name can be up to 63 characters long and can only contain printable characters.



## Create a secure gateway

A Chrome Enterprise Premium secure gateway is a fundamental building block for establishing secure connections to your applications. It allocates a dedicated project and network, providing isolation and security.

### console

To create a secure gateway resource, do the following:

  1. In the Google Cloud console, go to the **secure gateway** page.   
[Go to secure gateway](https://console.cloud.google.com/security/cep/secure-gateway)
  2. Select the project you want to create the secure gateway for.
  3. To create a secure gateway, click **Create new gateway** and wait for the gateway creation process to complete.
  4. You can track the progress in the Notifications section of the Google Cloud console.
  5. Before you create a SaaS application resource, we recommend that you create **SaaS egress hubs**. The `hubs` flag represents the regional resources required for enabling egress connectivity to the target application. You can configure one hub for each region, and each hub provides two IP addresses. A Secure Gateway can have at most 20 hubs. You can specify the following regions: 
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
  6. In the Google Cloud console, go to the **SaaS Egress Hubs** page.   
[Go to SaaS Egress Hubs](https://console.cloud.google.com/security/cep/secure-gateway/egress-hubs)
  7. Select the project you want to create the SaaS Egress Hubs for.
  8. To add a SaaS egress hub, click **Add SaaS egress hub**.
  9. From the drop-down list, select the regions where you'd like to add the egress hubs. To add the egress hubs, click **Add SaaS egress hub** to add more than one hub. After you're done, click Save to create the egress hubs.



### gcloud

To create a secure gateway resource, run the following command. For the `--hubs` flag, specify one or more regions from the following list.
    
    
    gcloud beyondcorp security-gateways create SECURITY_GATEWAY_ID \
        --project=PROJECT_ID \
        --location=global \
        --display-name="SECURITY_GATEWAY_DISPLAY_NAME" \
        --hubs=us-central1 \
        --service-discovery={}
          

The `hubs` flag sets the regional resources required for enabling egress connectivity to the target application. You can have one hub for each region, and each hub provides two IP addresses. A Secure Gateway can have at most 20 hubs. You can specify the following regions:

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



### REST

To create a secure gateway resource, call the Create API method with the gateway details in the request body. For the `hubs` flag, specify one or more regions from the following list.
    
    
    curl \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        -X POST \
        -d '{ "display_name": "SECURITY_GATEWAY_DISPLAY_NAME", "hubs": { "us-central1": {} }, "service_discovery": {} }' \
        "https://beyondcorp.googleapis.com/v1/projects/PROJECT_ID/locations/global/securityGateways?security_gateway_id=SECURITY_GATEWAY_ID"
          

The `hubs` flag represents the regional resources required for enabling egress connectivity to the target application. You can have one hub for each region, and each hub provides two IP addresses. A Secure Gateway can have at most 20 hubs. You can specify the following regions:

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



## Configure a SaaS application

After you create a secure gateway, you can configure your SaaS applications to use the secure gateway for secure access.

### console

To configure SaaS egress hubs, do the following:

  1. In the Google Cloud console, go to the **SaaS Egress Hubs** page.   
[Go to SaaS Egress Hubs](https://console.cloud.google.com/security/cep/secure-gateway/egress-hubs)
  2. On the **SaaS Egress Hubs** page, find the table listing the hubs. For each region you intend to use, copy all the IP addresses listed in the **Static dedicated egress IPs** column. Each region provides two IP addresses.
  3. Add the IP addresses to the IP allowlist of your SaaS application. For example, for a GitHub application, you can follow this guide: [Managing allowed IP addresses for your organization](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization).



### gcloud

To configure SaaS egress hubs, do the following:

  1. Get the IP addresses allocated by the secure gateway for each hub. Two IP addresses are allocated for a region.
    
    gcloud beyondcorp security-gateways describe SECURITY_GATEWAY_ID \
        --project=PROJECT_ID \
        --location=global
            

The following is a sample `GET` response of a secure gateway with `hubs`. In the example, `hubs` are created in the `us-central1` and `us-east1` regions, and all of the IP addresses returned in the response must be allowed in the SaaS application.
    
    createTime: 'CREATE_TIME'
    displayName: My secure gateway
    hubs:
      us-central1:
        internetGateway:
          assignedIps:
          -   IP_ADDRESS_1
          -   IP_ADDRESS_2
      us-east1:
        internetGateway:
          assignedIps:
          -   IP_ADDRESS_1
          -   IP_ADDRESS_2
    name: projects/PROJECT_ID/locations/global/securityGateways/SECURITY_GATEWAY_ID
    state: RUNNING
    updateTime: 'UPDATE_TIME'
        

  2. Add the IP addresses to the IP allowlist of your SaaS application. For example, for a GitHub application, you can follow this guide: [Managing allowed IP addresses for your organization](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization).



### REST

To configure SaaS egress hubs, do the following:

  1. Get the IP addresses allocated by the secure gateway for each hub. Two IP addresses are allocated for a region.
    
    curl \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://beyondcorp.googleapis.com/v1/projects/PROJECT_ID/locations/global/securityGateways/SECURITY_GATEWAY_ID"
            

The following is a sample `GET` response of a secure gateway with `hubs`. In the example, `hubs` are created in the `us-central1` and `us-east1` regions, and all of the IP addresses returned in the response must be allowed in the SaaS application.
    
    {
      "securityGateways": [
        {
          "name": "projects/PROJECT_ID/locations/global/securityGateways/SECURITY_GATEWAY_ID",
          "createTime": "CREATE_TIME",
          "updateTime": "UPDATE_TIME",
          "displayName": "My secure gateway",
          "state": "RUNNING",
          "hubs": {
            "us-central1": {
              "internetGateway": {
                "assignedIps": [
                  "IP_ADDRESS_1",
                  "IP_ADDRESS_2",
                ]
              }
            },
            "us-east1": {
              "internetGateway": {
                "assignedIps": [
                  "IP_ADDRESS_1",
                  "IP_ADDRESS_2",
                ]
              }
            }
          }
        }
      ]
    }
        

  2. Add the IP addresses to the IP allowlist of your SaaS application. For example, for a GitHub application, you can follow this guide: [Managing allowed IP addresses for your organization](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization).



## Create an application resource

The following information guides you through the process of setting up and configuring a secure gateway application resource.

### Create a secure gateway application resource in Google Cloud

The Google Cloud application resource is a sub-resource of the secure gateway resource. Create an application resource by using the Google Cloud console or calling the [`Create`](https://docs.cloud.google.com/beyondcorp/docs/reference/rest/v1/projects.locations.securityGateways/create) API.

### console

To create a SaaS application, do the following:

  1. In the Google Cloud console, go to the **secure gateway** page.   
[Go to secure gateway](https://console.cloud.google.com/security/cep/secure-gateway)
  2. To create an application, click **Add application**.
  3. Select the application type: **Public application**.
  4. If SaaS egress hubs aren't yet configured for this secure gateway, you will be prompted to create them. Public applications require at least one SaaS egress hub. To configure SaaS egress hubs, click **Go to SaaS egress hubs** and add one or more regions.
  5. After you have one or more egress hubs, click **Next**.
  6. Enter the application details: 
     * **Application name** : Enter a name, for example, `GitHub`.
     * **Domain matchers** : Enter a comma-separated list of domain patterns to route through the secure gateway. Include the port in the format `domain:port`. Wildcards (`*`) are allowed. For example: `github.com:443`.
  7. To configure your SaaS application, click **Continue**.
  8. Configure your SaaS application to allow traffic from the secure gateway:
     1. Carefully note or copy all the IP addresses listed for the regions you are using. These IP addresses are unique to your secure gateway.
     2. Sign in to your SaaS application's administration console.
     3. Navigate to the network settings or security settings where IP allowlists are managed.
     4. Add all the IP addresses obtained to the application's IP allowlist.
  9. To add the application, click **Continue**.
  10. Optional: **Define an access policy** : Select an Access Context Manager access policy. You can skip this step for this guide.
  11. To create, save your settings and create the application, click **Create**.



### gcloud

To create a SaaS application using gcloud, run the following command:
    
    
    gcloud beyondcorp security-gateways applications create APPLICATION_ID \
        --project=PROJECT_ID \
        --security-gateway=SECURITY_GATEWAY_ID \
        --location=global \
        --display-name="APPLICATION_DISPLAY_NAME" \
        --endpoint-matchers="hostname=HOST_NAME,ports=443"
          

### REST

To create a SaaS application using the REST API, run the following command:
    
    
    curl \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        -X POST \
        -d "{ \"display_name\": \"APPLICATION_DISPLAY_NAME\", \"endpoint_matchers\": [{hostname: \"HOST_NAME\", ports: 443}] }" \
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

  * [Manage a secure gateway](https://docs.cloud.google.com/chrome-enterprise-premium/docs/manage-security-gateway)

  * [Troubleshoot secure gateway issues](https://docs.cloud.google.com/chrome-enterprise-premium/docs/troubleshoot-security-gateway)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
