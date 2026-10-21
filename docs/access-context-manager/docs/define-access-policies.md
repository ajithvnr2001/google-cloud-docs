---
url: https://docs.cloud.google.com/access-context-manager/docs/define-access-policies/
title: Define access policies using access levels \u00a0|\u00a0 Access Context Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T21:27:14.289874+00:00
---

# Define access policies using access levels  |  Access Context Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/access-context-manager/docs/define-access-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Access Context Manager ](https://docs.cloud.google.com/access-context-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/access-context-manager/docs/create-access-level)



Send feedback 

#  Define access policies using access levels Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to define Context-Aware Access policies using access levels.

An [access level](https://docs.cloud.google.com/access-context-manager/docs/overview#access-levels) is a set of attributes assigned to requests based on their origin. Using information such as device type, IP address, and user identity, you can designate what level of access to grant. For example, you might assign a `High_Trust` level to connections from within your corporate network and a `Medium_Trust` level to external devices running approved operating systems.

An access policy is a container for all of your Access Context Manager resources, such as access levels and service perimeters.

For more information about access levels and access policies, see the [Access Context Manager overview](https://docs.cloud.google.com/access-context-manager/docs/overview).

## Limitations

When defining an access level, the following limitations apply:

  * You can't use an IP address as an attribute for Docker connections, nor can you use private IP addresses when connecting to private clusters using `kubectl` or a managed Looker instance.
  * Data Studio is always allowed unrestricted access to the Google Cloud APIs, regardless of Access Context Manager policies.
  * Device attributes aren't available for non-Google OAuth client applications.
  * You can't use a [scoped access level](https://docs.cloud.google.com/vpc-service-controls/docs/manage-policies).



## Define your policy using access levels

###  Console 

Create a basic access level:

  1. In the Google Cloud console, open the **Access Context Manager** page.

[Go to the Access Context Manager page](https://console.cloud.google.com/security/access-level)

  2. If you are prompted, select a project.

  3. On the **Access Context Manager** page, click **New**.

  4. In the **New Access Level** pane, do the following:

     1. In the **Access level title** field, enter a title for the access level. The title must be at most 50 characters, start with a letter, and can contain only numbers, letters, underscores, and spaces.

     2. In the **Conditions** section, click the add button for the type of attribute you want to add, and then provide the values you want applied to that attribute.

For a complete list of the attributes that you can add, see [access level attributes](https://docs.cloud.google.com/access-context-manager/docs/access-level-attributes).

For example, if you want the access level to consider where a request is coming from within your network, you would select the **IP Subnetworks** attribute.

Repeat this step to add multiple attributes to the same condition. When a condition has multiple attributes, all of the attributes must be met by the access request.

An access level condition can include one of each type of attribute. Some attributes include additional options, such as the **Device Policy** attribute.

Access levels support conditions based on user identity. However, to add identities to a condition, you must create or update the access level using the gcloud CLI or the API.

     3. Use the **When condition is met, return** option to specify whether the condition is evaluated as an **AND** operation that requires a request to meet all specified attributes (**TRUE**), or as a negated (**NAND**) operation that is met when a request doesn't meet at least one specified attribute (**FALSE**).

For example, if you want to deny requests from a certain IP address range of your network, specify the IP address range using the **IP Subnetworks** attribute and then set the condition to **FALSE**.

     4. Optionally, click **Add another condition** to add an additional condition to your access level and then repeat the previous two steps.

For example, if you want to deny access to a subset of IP addresses within a broader IP address range, create a new condition, specify the subset IP address range for the **IP Subnetworks** attribute, and set the condition to return **FALSE**.

Repeat this step to add multiple conditions to the same access level.

     5. If you created more than one condition, use **Combine condition with** to specify whether you want the access level to require a request to meet at least one of the conditions (**OR**), or all of the conditions (**AND**).

     6. Click **Save**.




###  gcloud 

If you don't have an access policy for your organization, [create one](https://docs.cloud.google.com/access-context-manager/docs/create-access-policy) before continuing.

Use the [`gcloud access-context-manager levels create`](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/levels/create) command to create an access level:
    
    
    gcloud access-context-manager levels create LEVEL_NAME OPTIONS \
        --policy=POLICY

Replace the following:

  * LEVEL_NAME: The unique name for the access level. It must begin with a letter and include only letters, numbers, and underscores. The name can be a maximum of 50 characters.

  * OPTIONS: The required options from the following table.

Options  
---  
`basic-level-spec` |  A YAML file that specifies one or more conditions for the access level.   
`title` |  A short title for the access level. The access level's title is displayed in the Google Cloud console.   
`combine-function` |  (Optional) Determines how conditions are combined.  Valid values: `AND`, `OR`  
`description` |  (Optional) A long-form description of the access level.  
  * POLICY: The ID of your organization's access policy. If you have a default policy set, this parameter is optional.




Optionally, you can include any of the [gcloud flags](https://docs.cloud.google.com/sdk/gcloud/reference).

### basic-level-spec YAML file

When you use the gcloud CLI to create an access level, you must provide a YAML file for the `basic-level-spec` option. The YAML file defines one or more conditions for the access level. Conditions must contain at least one attribute. When a condition contains more than one attribute, they are combined as either an **AND** operation (all must be true) or as a **NAND** operation (at least one must be false), depending on whether the `negate` attribute is set to true in the condition.

For a complete list of the attributes that you can include in your YAML file, see [access level attributes](https://docs.cloud.google.com/access-context-manager/docs/access-level-attributes).

For more information about access levels and YAML, refer to the example YAML for an access level.

### Example command
    
    
    gcloud access-context-manager levels create Device_Trust \
        --basic-level-spec=corpdevspec.yaml \
        --combine-function=AND \
        --description='Access level that conforms to corporate spec.' \
        --title='Device_Trust Extended' \
        --policy=1521580097614100
    

###  API 

If you don't have an access policy for your organization, [create one](https://docs.cloud.google.com/access-context-manager/docs/create-access-policy) before continuing.

To create an access level, call [`accessLevels.create`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels/create).
    
    
    POST https://accesscontextmanager.googleapis.com/v1/accessPolicies/POLICY/accessLevels
    

POLICY is the ID of your organization's access policy.

### Request body

The request body must include an [`AccessLevel`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels#AccessLevel) resource that specifies the conditions you want for the new access level. Each [`Condition`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels#condition) has one or more attributes that are evaluated as an **AND** operation (all must be true) or as a **NAND** operation (at least one must be false) depending on whether the `negate` field is set to true. The resulting evaluation determines whether the condition is met or not.

### Response body

If successful, the response body for the call contains an [`Operation`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/Shared.Types/Operation) resource that provides details about the `POST` operation.

## Common policy configurations

The following examples cover a few of the practical ways your organization might want to implement access levels. The examples assume your organization already has an [access policy](https://docs.cloud.google.com/access-context-manager/docs/create-access-policy).

### Limit access on a corporate network

This example describes how to create an access level condition that allows access only from a specified range of IP addresses (for example, those within a corporate network).

By restricting the range of IP addresses that are granted access, you can make exfiltrating data more difficult for an attacker that is inside or outside your organization.

For this example, assume you want to create an access level that will allow a group of internal auditors to access the Cloud Logging service for a project named _sensitive-data_. All of the devices for the auditors are assigned IPs on a subnet ranging between 203.0.113.0 and 203.0.113.127. You know there won't be any devices assigned to that subnet other than those used by the auditors.

If you want to use a private IP address range (for example, `192.168.0.0/16` or `172.16.0.0/12`), see [Allow access to protected resources from an internal IP address](https://docs.cloud.google.com/vpc-service-controls/docs/enable-internal-ip-access) for additional information and an example implementation using VPC Service Controls.

###  Console 

  1. In the Google Cloud console, open the Access Context Manager.

[Go to the Access Context Manager page](https://console.cloud.google.com/security/access-level)

  2. If you are prompted, select project.

  3. At the top of the **Access Context Manager** page, click **New**.

  4. In the **New Access Level** pane, in the **Conditions** section, click **Add attribute** and then click **IP Subnetworks**.

  5. In the **IP Subnetworks** box, select either **Public IP** or **Private IP**.

     * If you select **Public IP** , enter one or more IPv4 or IPv6 ranges formatted as [CIDR](https://wikipedia.org/wiki/Classless_Inter-Domain_Routing) blocks.

In this example, to limit access to only the auditors, enter `203.0.113.0/25` in the **IP Subnetworks** box.

     * If you select **Private IP** , click **Select VPC networks**. You can specify VPC networks using one of the three options available in the **Import options** list.

       * _Option 1:_

         1. Select **Browse for VPC networks in your organization** and select the VPC networks.

         2. Click **Add selected VPC networks**.

         3. Click **Select IP subnets** and select the subnets.

         4. Click **Add IP subnets**.

       * _Option 2:_

         1. Select **Manually enter VPC network address** and enter one or more VPC networks.

         2. Click **Add VPC network**.

         3. Click **Select IP subnets** and select the subnets.

         4. Click **Add IP subnets**.

       * _Option 3:_

         1. Select **Upload CSV file (overwrites existing networks)**.

If you use a CSV file to add VPC networks and subnets to an access level, Access Context Manager overwrites the previously selected VPC networks and subnets.

         2. Click **Browse** and upload the CSV file. In the CSV file, you must specify the VPC networks and subnets in the following format:
                
                VPC_NETWORK_NAME_1       | IP_RANGE_1       | IP_RANGE_2       | ...
                VPC_NETWORK_NAME_2       | .                | .                | ...
                .                        | .                | .                | ...
                .                        | .                | .                | ...
                

         3. Click **Import networks**.

Using the CSV file, Access Context Manager populates the VPC network names and subnet information in the **VPC network address** and **IP subnetworks** boxes respectively.

For information about the VPC network name and private IP address format, see [Use internal IP address in access levels](https://docs.cloud.google.com/vpc-service-controls/docs/enable-internal-ip-access#enable).

  6. Click **Save**.




###  gcloud 

  1. Create a YAML file for an access level that includes one or more IPv4 or IPv6 ranges formatted as [CIDR](https://wikipedia.org/wiki/Classless_Inter-Domain_Routing) blocks.

In this example, to limit access to only the auditors, you would enter the following into the YAML file:
         
         - ipSubnetworks:
           - 203.0.113.0/25
         

If you want to use a private IP address, you need to enter the following information in the YAML file:
         
         - vpcNetworkSources:
           - vpcSubnetwork:
               network: VPC_NETWORK_NAME
               vpcIpSubnetworks:
               - IP_RANGE
         

Replace VPC_NETWORK_NAME and IP_RANGE with the values described in the [Use internal IP address in access levels](https://docs.cloud.google.com/vpc-service-controls/docs/enable-internal-ip-access#enable) section.

  2. Save the file. In this example, the file is named `CONDITIONS.yaml`.

  3. Create the access level.
         
         gcloud access-context-manager levels create NAME \
            --title TITLE \
            --basic-level-spec CONDITIONS.yaml \
            --policy=POLICY

Replace the following:

     * NAME: The unique name for the access level. It must begin with a letter and include only letters, numbers, and underscores.

     * TITLE: A human-readable title. It must be unique to the policy.

     * POLICY: The ID of your organization's access policy. If you have a default policy set, this parameter is optional.

You should see output similar to the following:
    
    Create request issued for: NAME
    Waiting for operation [accessPolicies/POLICY/accessLevels/NAME/create/1521594488380943] to complete...done.
    Created level NAME.
    




###  API 

  1. Craft a request body to create an [`AccessLevel`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels#AccessLevel) resource that includes one or more IPv4 or IPv6 ranges formatted as [CIDR](https://wikipedia.org/wiki/Classless_Inter-Domain_Routing) blocks.

In this example, to limit access to only the auditors, you would enter the following into the request body:
         
         {
          "name": "NAME",
          "title": "TITLE",
          "basic": {
            "conditions": [
              {
                "ipSubnetworks": [
                  "203.0.113.0/25"
                ]
              }
            ]
          }
         }

Replace the following:

     * NAME: The unique name for the access level. It must begin with a letter and include only letters, numbers, and underscores.

     * TITLE: A human-readable title. It must be unique to the policy.

If you want to use a private IP address, you need to enter the following information in the request body:
    
    {
     "name": "NAME",
     "title": "TITLE",
     "basic": {
       "conditions": [
         {
           "vpcNetworkSources": [
            {
              "vpcSubnetwork": {
                "network": VPC_NETWORK_NAME,
                "vpcIpSubnetworks": [
                  IP_RANGE
                ]
              }
            }
           ]
         }
       ]
     }
    }

Replace VPC_NETWORK_NAME and IP_RANGE with the values described in the [Use internal IP address in access levels](https://docs.cloud.google.com/vpc-service-controls/docs/enable-internal-ip-access#enable) section.

  2. Create the access level by calling [`accessLevels.create`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels/create).
         
         POST https://accesscontextmanager.googleapis.com/v1/accessPolicies/POLICY/accessLevels
         

POLICY is the ID of your organization's access policy.




After you create the access level, you must apply it using an [access binding](https://docs.cloud.google.com/access-context-manager/docs/apply-policies-to-user-groups) for it to be enforced.

### Limit access by device attributes

**Note:** This feature is available only with [Chrome Enterprise Premium](https://chromeenterprise.google/products/chrome-enterprise-premium/). To purchase a Chrome Enterprise Premium subscription, contact sales.

This example describes how to create an access level that grants access only to devices which meet a specified set of requirements, like a certain operating system (OS) version.

Information about devices is provided to Access Context Manager using [Endpoint Verification](https://docs.cloud.google.com/endpoint-verification/docs/overview). The following criteria can be checked when determining whether to grant access:

  * Screen lock is enabled
  * Storage encryption is enabled
  * Device is running a specified operating system kind and version



For this example, assume your organization uses only machines that have either ChromeOS or Windows installed. To add a layer of security, you want to create an access level that will prevent access by anyone using other operating systems. Additionally, to manage risk, you want to make sure that only certain versions of the OSes can gain access.

###  Console 

  1. In the Google Cloud console, open the Access Context Manager page.

[Go to the Access Context Manager page](https://console.cloud.google.com/security/access-level)

  2. If you are prompted, select a project.

  3. At the top of the **Access Context Manager** page, click **New**.

  4. In the **New Access Level** pane, in the **Conditions** section, click **Add attribute** and then click **Device Policy**.

  5. Add the device policy attributes:

     1. Click **Add OS Policy** and then click **Chrome OS Policy**.

     2. In the **Minimum version** box, enter the minimum version of ChromeOS you want to allow.

     3. Repeat steps 1 and 2 for **Windows OS Policy**.

  6. Click **Save**.




###  gcloud 

  1. Create a YAML file for an access level that includes a device policy with OS constraints.

In this example, to allow only devices with a minimum acceptable version of ChromeOS and Windows, you would enter the following into the YAML file:
         
         - devicePolicy:
             osConstraints:
               - osType: DESKTOP_CHROME_OS
                 minimumVersion: 11316.165.0
               - osType: DESKTOP_WINDOWS
                 minimumVersion: 10.0.1809
         

  2. Save the file. In this example, the file is named `CONDITIONS.yaml`.

  3. Create the access level.
         
         gcloud access-context-manager levels create NAME \
            --title TITLE \
            --basic-level-spec CONDITIONS.yaml \
            --policy=POLICY

Replace the following:

     * NAME: The unique name for the access level. It must begin with a letter and include only letters, numbers, and underscores.

     * TITLE: A human-readable title. It must be unique to the policy.

     * POLICY: The ID of your organization's access policy. If you have a default policy set, this parameter is optional.

You should see output similar to the following:
    
    Create request issued for: NAME
    Waiting for operation [accessPolicies/POLICY/accessLevels/NAME/create/1521594488380943] to complete...done.
    Created level NAME.
    




###  API 

  1. Craft a request body to create an [`AccessLevel`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels#AccessLevel) resource that includes a device policy with OS constraints.

In this example, to allow only devices with a minimum acceptable version of ChromeOS and Windows, you would enter the following into the request body:
         
         {
          "name": "NAME",
          "title": "TITLE",
          "basic": {
            "conditions": [
              {
                "devicePolicy": {
                  "osConstraints": [
                    {
                      "osType": "DESKTOP_CHROME_OS",
                      "minimumVersion": "11316.165.0"
                    },
                    {
                      "osType": "DESKTOP_WINDOWS",
                      "minimumVersion": "10.0.1809"
                    }
                  ]
                {
              }
            ]
          }
         }

Replace the following:

     * NAME: The unique name for the access level. It must begin with a letter and include only letters, numbers, and underscores.

     * TITLE: A human-readable title. It must be unique to the policy.

  2. Create the access level by calling [`accessLevels.create`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels/create).
         
         POST https://accesscontextmanager.googleapis.com/v1/accessPolicies/POLICY/accessLevels
         

POLICY is the ID of your organization's access policy.




After you create the access level, you must apply it using an [access binding](https://docs.cloud.google.com/access-context-manager/docs/apply-policies-to-user-groups) for it to be enforced.

### Limit access to trusted corporate devices with valid certificates

You can use [certificate-based access (CBA)](https://docs.cloud.google.com/access-context-manager/docs/securing-resources-with-certificate-based-access) to require verified X.509 certificates for access to Google Cloud resources. The additional credential provides a stronger signal of device identity and helps protect your organization from credential theft or accidental loss by requiring that both the user credentials and the original device certificate are present before granting access.

Before continuing, ensure that the Endpoint Verification Chrome extension and the Endpoint Verification helper app are deployed on all of the devices that require access to Google Cloud resources. These become trusted devices to which you can grant access. See [Deploy Endpoint Verification to use with certificate-based access](https://docs.cloud.google.com/chrome-enterprise-premium/docs/deploy-cba-endpoint-verification) for details.

To create a policy that requires certificate-based access, you must have an [access level](https://docs.cloud.google.com/access-context-manager/docs/create-custom-access-level) with a custom [access level specification](https://docs.cloud.google.com/access-context-manager/docs/custom-access-level-spec).

###  Console 

  1. In the Google Cloud console, open the **Access Context Manager** page.

[Go to the Access Context Manager page](https://console.cloud.google.com/security/access-level)

  2. If you are prompted, select a project.

  3. Click **Create access level**.

  4. In the **New access level** pane, select **Advanced mode**. You must have a Chrome Enterprise Premium license to use this mode.

  5. In the **Conditions** section, enter the following expression in the **CEL expression** box.
         
         certificateBindingState(origin, device) == CertificateBindingState.CERT_MATCHES_EXISTING_DEVICE
         

  6. Click **Save**.




###  gcloud 

  1. Create a YAML file for an access level that includes certificate enforcement.
         
         expression: "certificateBindingState(origin, device) == CertificateBindingState.CERT_MATCHES_EXISTING_DEVICE"
         

  2. Save the file. In this example, the file is named `CONDITIONS.yaml`.

  3. Create the access level.
         
         gcloud access-context-manager levels create NAME \
            --title TITLE \
            --basic-level-spec CONDITIONS.yaml \
            --policy=POLICY




Replace the following:

  * NAME: The unique name for the access level. The name must begin with a letter and include only letters, numbers, and underscores.

  * TITLE: A human-readable title. It must be unique to the policy.

  * POLICY: The ID of your organization's access policy. If you have a default policy set, this parameter is optional.




You should see output similar to the following:
    
    
    Create request issued for: NAME
    Waiting for operation [accessPolicies/POLICY/accessLevels/NAME/create/1234] to complete...done.
    Created level NAME.

###  API 

  1. Create a request body file for an access level that includes a device policy with OS constraints.
         
         {
          "name": "require_certificate",
          "title": "Certificate-Based Access",
          "description": "An example certificate-based access level.",
          "custom": {
            "expr": {
              "expression": "certificateBindingState(origin, device) == CertificateBindingState.CERT_MATCHES_EXISTING_DEVICE",
              "title": "Require a valid certificate",
              "description": "Permits requests from a device with a valid mTLS certificate."
             }
           }
         }

  2. Create the access level by calling [`accessLevels.create`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels/create).
         
         POST https://accesscontextmanager.googleapis.com/v1/accessPolicies/POLICY/accessLevels
         

POLICY is the ID of your organization's access policy.




After you create the access level, you must apply it using an [access binding](https://docs.cloud.google.com/access-context-manager/docs/apply-policies-to-user-groups) for it to be enforced.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
