---
url: https://docs.cloud.google.com/chrome-enterprise-premium/docs/cross-org-authorization/
title: Configure authorization across organizations \u00a0|\u00a0 Chrome Enterprise Premium \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:35:54.676348+00:00
---

# Configure authorization across organizations  |  Chrome Enterprise Premium  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chrome-enterprise-premium/docs/cross-org-authorization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Chrome Enterprise Premium ](https://docs.cloud.google.com/chrome-enterprise-premium/docs)
  * [ Guides ](https://docs.cloud.google.com/chrome-enterprise-premium/docs/overview)



Send feedback 

#  Configure authorization across organizations Stay organized with collections  Save and categorize content based on your preferences. 

This page provides a high-level overview of the cross-org authorization feature and the steps to configure it.

You can use Chrome Enterprise Premium to allow secure data access from devices within an [organization](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-%0Ahierarchy#organizations). This ensures that devices are evaluated against the organization [access policy](https://docs.cloud.google.com/access-context-manager/docs/overview#access-%0Apolicies) at the enforcement points when determining access. For example, whether to allow or deny access from another organization is one piece of information in the access policy that is evaluated. If you need the devices in your organization to access resources in another organization, your organization and the other organization must have cross-org authorization configured.

Cross-org authorization lets you configure an access policy to trust and use data, such as device attributes, owned by other organizations. For example, you can configure the access policy of your organization to allow access to its resources from devices in other organizations.

## Before you begin

To set up and manage cross-org authorization, you need the organization IDs of your organization and the IDs of the organizations that you want to authorize. You also need your organization-level policy number. If you don't have the organization IDs or your organization-level policy number, see the following information:

  * [Getting your organization resource ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id)
  * Get the organization-level access policy number



When setting up and managing cross-org authorization, you work with the `AuthorizedOrgsDesc` resource. The `AuthorizedOrgsDesc` resource contains the list of organizations that you want to authorize and specifies the authorization type, asset type, and authorization direction for the organizations.

You can use the Google Cloud CLI to create an `AuthorizedOrgsDesc` resource and modify its settings. When working with the `AuthorizedOrgsDesc` resource, the following applies:

  * `ASSET_TYPE_DEVICE` is the only option available for asset type.
  * `AUTHORIZATION_TYPE_TRUST` is the only option available for the authorization type.



## Set up cross-org device authorization between two organizations

This section provides the steps for setting up cross-org authorization by using an example throughout the steps.

This example creates a bi-directional authorization relationship between two organizations and allows devices from one organization to access resource in another organization. The resource organization (`organizations/RESOURCE_ORG_ID`) contains resources such as Cloud Storage buckets and VMs. The resource organization has access levels that allow specific devices in the organization to access its resources. The partner organization (`organizations/PARTNER_ORG_ID`) is an organization that needs to access resources in the resource organization.

Following are the policies for the resource and partner organizations before cross-org authorization is configured:

Resource organization (organizations/RESOURCE_ORG_ID):
    
    
    access policy:
    access level: SP1
      --"requireScreenlock": true
    

Partner organization (organizations/PARTNER_ORG_ID):
    
    
    no access policy
    
    

In the following image, the device attributes of the device in the partner organization are not visible to the resource organization because cross-org authorization is not configured.

![Before cross-org is configured, the device attributes of the partner organization device are not visible to the resource organization.](https://docs.cloud.google.com/chrome-enterprise-premium/images/device-org-no-access.png)

The following steps show how to configure both the resource organization and partner organization to enable cross-org authorization by using the Google Cloud CLI.

### Prepare

Complete the steps in this section for both the resource and the partner organizations.

  1. Ensure that both organizations have an organization-level policy. To create an organization-level policy, see [Create an organization-level access policy](https://docs.cloud.google.com/access-context-manager/docs/create-access-policy#organization-access-%0Apolicy).

  2. Run the following command to get the organization-level access policy number:
         
         gcloud access-context-manager policies list --organization=ORG_ID
         

Replace ORG_ID with your organization ID.

You should receive information in the following format:
         
         NAME                    ORGANIZATION SCOPES     TITLE     ETAG
         <ACCESS_POLICY_NUMBER>  <ORGANIZATION_NUMBER>   A title   002cb3fbfde471e7
         




### Configure the resource organization

  1. You must be the resource organization (`organizations/RESOURCE_ORG_ID`) admin to complete this step. Create an `AuthorizedOrgsDesc` resource for the resource organization by running the following command:
         
         gcloud access-context-manager authorized-orgs create AUTHORIZED_ORGS_DESC_NAME \
          --authorization_type=AUTHORIZATION_TYPE_TRUST \
          --asset_type=ASSET_TYPE_DEVICE \
          --authorization_direction=AUTHORIZATION_DIRECTION_FROM \
          --orgs=organizations/PARTNER_ORG_ID \
          --policy=ACCESS_POLICY_NUMBER
         

Replace the following:

     * AUTHORIZED_ORGS_DESC_NAME: A unique name for the `AuthorizedOrgsDesc` resource. The name must begin with a letter and contain only letters, numbers, and underscores. The name can be a maximum of 50 characters.

     * ACCESS_POLICY_NUMBER: Your organization-level access policy number.

     * PARTNER_ORG_ID: The partner organization number.

  2. Display the newly-created `AuthorizedOrgsDesc` resource to verify that it is correct by running the following command:
         
         gcloud access-context-manager authorized-orgs describe AUTHORIZED_ORGS_DESC_NAME \
          --policy=ACCESS_POLICY_NUMBER
         

Replace the following:

     * AUTHORIZED_ORGS_DESC_NAME: A unique name for the `AuthorizedOrgsDesc` resource. The name must begin with a letter and contain only letters, numbers, and underscores. The name can be a maximum of 50 characters.

     * ACCESS_POLICY_NUMBER: Your organization-level access policy number.




### Configure the partner organization

  1. You must be the partner organization (`organizations/PARTNER_ORG_ID`) admin to complete this step. Create an `AuthorizedOrgsDesc` resource for the partner organization by running the following command:
         
         gcloud access-context-manager authorized-orgs create AUTHORIZED_ORGS_DESC_NAME \
           --authorization_type=AUTHORIZATION_TYPE_TRUST \
           --asset_type=ASSET_TYPE_DEVICE \
           --authorization_direction=AUTHORIZATION_DIRECTION_TO \
           --orgs=organizations/RESOURCE_ORG_ID \
           --policy=ACCESS_POLICY_NUMBER
         

Replace the following:

     * AUTHORIZED_ORGS_DESC_NAME: A unique name for the `AuthorizedOrgsDesc` resource. The name must begin with a letter and contain only letters, numbers, and underscores. The name can be a maximum of 50 characters.

     * ACCESS_POLICY_NUMBER: Your organization-level access policy number.

     * RESOURCE_ORG_ID: The resource organization number.

  2. Display the newly-created `AuthorizedOrgsDesc` resource to verify that it is correct by running the following command:
         
         gcloud access-context-manager authorized-orgs describe AUTHORIZED_ORGS_DESC_NAME \
           --policy=ACCESS_POLICY_NUMBER
         

Replace the following:

     * AUTHORIZED_ORGS_DESC_NAME: A unique name for the `AuthorizedOrgsDesc` resource. The name must begin with a letter and contain only letters, numbers, and underscores. The name can be a maximum of 50 characters.

     * ACCESS_POLICY_NUMBER: Your organization-level access policy number.




### Expected post-configuration policies

Following are the policies for the resource and partner organizations after cross-org authorization is configured:

Resource organization (organizations/RESOURCE_ORG_ID):
    
    
    access policy:
    access level: SP1
      --"requireScreenlock": true
    AuthorizedorgsDesc: AOD1
      --authorizationtype: trust
      --asset type: device
      --authorization direction: from
      --orgs: [organizations/PARTNER_ORG_ID]
    

Partner organization (organizations/PARTNER_ORG_ID):
    
    
    access policy:
    AuthorizedOrgsDesc: AOD2
      --authorizationtype: trust
      --asset type: device
      --authorization direction: to
      --orgs: [organizations/RESOURCE_ORG_ID]
    

The following image shows the visibility of the device attributes of the partner organization after cross-org authorization is configured.

![The device attributes of the partner organization device are visible to the resource organization after configuring cross-org authorization](https://docs.cloud.google.com/chrome-enterprise-premium/images/device-org-access.png)

### Test your configuration

After you configure the two organizations, you can have a user in the partner organization attempt to access resources in the resource organization using a compliant device. If access is granted, your cross-org authorization works as expected. Users in the partner organization can now access bucket A in Cloud Storage of the resource organization only if the user's device has a screen lock policy in place.

If the device is not granted access, step through the configuration steps again to fix your configuration.

## Manage a cross-org authorization configuration

After you configure cross-org authorization, you might need to remove access to an organization, add access to another organization, or other tasks. This section contains information about how to complete common tasks when managing cross-org authorization.

### Create an `AuthorizedOrgsDesc` resource and authorize external organizations

To create an `AuthorizedOrgsDesc` resource and include the external organizations to which you want to grant access, run the following command:
    
    
    gcloud access-context-manager authorized-orgs create AUTHORIZED_ORGS_DESC_NAME
     --authorization_type=AUTHORIZATION_TYPE_TRUST
     --asset_type=ASSET_TYPE_DEVICE
     --authorization_direction=AUTHORIZATION_DIRECTION_FROM
     --orgs=ORG_ID --policy=ACCESS_POLICY_NUMBER
    

Replace the following:

  * AUTHORIZED_ORGS_DESC_NAME: A unique name for the `AuthorizedOrgsDesc` resource. The name must begin with a letter and contain only letters, numbers, and underscores. The name can be a maximum of 50 characters.

  * ORG_ID: The organization ID of the organization to which you want to grant access. When specifying more than one organization, use a comma to separate the organization IDs.

  * ACCESS_POLICY_NUMBER: Your organization-level access policy number.




### Add an organization

To add an organization to an existing `AuthorizedOrgsDesc` resource, run the following command:
    
    
    gcloud access-context-manager authorized-orgs update AUTHORIZED_ORGS_DESC_NAME \
      --add-orgs=ORG_ID \
      --policy=ACCESS_POLICY_NUMBER
    

Replace the following:

  * AUTHORIZED_ORGS_DESC_NAME: A unique name for the `AuthorizedOrgsDesc` resource. The name must begin with a letter and contain only letters, numbers, and underscores. The name can be a maximum of 50 characters.

  * ORG_ID: The organization ID of the organization to which you want to grant access. When specifying more than one organization, use a comma to separate the organization IDs.

  * ACCESS_POLICY_NUMBER: Your organization-level access policy number.




### Remove an organization

To remove an organization from an existing `AuthorizedOrgsDesc` resource, run the following command:
    
    
    gcloud access-context-manager authorized-orgs update AUTHORIZED_ORGS_DESC_NAME \
      --remove-orgs=ORG_ID \
      --policy=ACCESS_POLICY_NUMBER
    

Replace the following:

  * AUTHORIZED_ORGS_DESC_NAME: A unique name for the `AuthorizedOrgsDesc` resource. The name must begin with a letter and contain only letters, numbers, and underscores. The name can be a maximum of 50 characters.

  * ORG_ID The organization ID of the organization that you want to remove.

  * ACCESS_POLICY_NUMBER: Your organization-level access policy number.




### Specify a new list of organizations

To specify a new list of organizations in an existing `AuthorizedOrgsDesc` resource, run the following command:
    
    
    gcloud access-context-manager authorized-orgs update AUTHORIZED_ORGS_DESC_NAME \
      --set-orgs=ORG_IDS \
      --policy=ACCESS_POLICY_NUMBER
    

Replace the following:

  * AUTHORIZED_ORGS_DESC_NAME: A unique name for the `AuthorizedOrgsDesc` resource. The name must begin with a letter and contain only letters, numbers, and underscores. The name can be a maximum of 50 characters.

  * ORG_ID: The organization ID of the organization to which you want to grant access. When specifying more than one organization, use a comma to separate the organization IDs.

  * ACCESS_POLICY_NUMBER: Your organization-level access policy number.




### Remove all organizations

To remove all organizations from an existing `AuthorizedOrgsDesc` resource, run the following command:
    
    
    gcloud access-context-manager authorized-orgs update AUTHORIZED_ORGS_DESC_NAME \
      --clear-orgs --policy=ACCESS_POLICY_NUMBER
    

Replace the following:

  * AUTHORIZED_ORGS_DESC_NAME: A unique name for the `AuthorizedOrgsDesc` resource. The name must begin with a letter and contain only letters, numbers, and underscores. The name can be a maximum of 50 characters.

  * ACCESS_POLICY_NUMBER The organization-level access policy number.




### Display an `AuthorizedOrgsDesc` resource

To display an existing `AuthorizedOrgsDesc` resource, run the following command:
    
    
    gcloud access-context-manager authorized-orgs describe AUTHORIZED_ORGS_DESC_NAME \
      --policy=ACCESS_POLICY_NUMBER
    

Replace the following:

  * AUTHORIZED_ORGS_DESC_NAME: A unique name for the `AuthorizedOrgsDesc` resource. The name must begin with a letter and contain only letters, numbers, and underscores. The name can be a maximum of 50 characters.

  * ACCESS_POLICY_NUMBER The organization-level access policy number.




### List the `AuthorizedOrgsDesc` resources

To list the `AuthorizedOrgsDesc` resources in the access policy, run the following command:
    
    
    gcloud access-context-manager authorized-orgs list --policy=ACCESS_POLICY_NUMBER
    

Replace ACCESS_POLICY_NUMBER with organization-level access policy number.

### Remove an `AuthorizedOrgsDesc` resource

To remove an `AuthorizedOrgsDesc` resource, run the following command:
    
    
    gcloud access-context-manager authorized-orgs delete  AUTHORIZED_ORGS_DESC_NAME \
      --policy=ACCESS_POLICY_NUMBER
    

Replace the following:

  * AUTHORIZED_ORGS_DESC_NAME: A unique name for the `AuthorizedOrgsDesc` resource. The name must begin with a letter and contain only letters, numbers, and underscores. The name can be a maximum of 50 characters.

  * ACCESS_POLICY_NUMBER The organization-level access policy number.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
