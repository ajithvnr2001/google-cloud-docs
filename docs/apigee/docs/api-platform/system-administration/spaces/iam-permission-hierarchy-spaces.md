---
url: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/spaces/iam-permission-hierarchy-spaces/
title: IAM permission hierarchy in Apigee Spaces \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:55:16.864657+00:00
---

# IAM permission hierarchy in Apigee Spaces  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/spaces/iam-permission-hierarchy-spaces/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  IAM permission hierarchy in Apigee Spaces Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This page describes how [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs) permission hierarchies are applied to Apigee API resources (API proxies, shared flows, and API products) and their children when using Apigee Spaces.

## IAM interaction with Apigee Spaces

In general, IAM policies governing access to resources are inherited through the [ Google Cloud resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#resource-hierarchy-detail). The specific IAM policies that apply to a given resource include both of the following: 

  * Any policies directly applied to the resource
  * Any policies the resource [inherits](https://docs.cloud.google.com/iam/docs/overview#policy-inheritance) from its ancestors



### Resource and permission hierarchy in Apigee

In Apigee, the top of the resource hierarchy is the [organization](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations) resource. Child resources of an organization include [API proxies](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis#ApiProxy), [shared flows](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.sharedflows#resource:-sharedflow), and [API products](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts#resource:-apiproduct). When you use Apigee without Spaces, permissions are applied to the Google Cloud project, which correlates directly with the Apigee organization resource. As a result, the IAM policies governing access to a given API proxy, shared flow, or API product include any policies inherited from the organization, in addition to any policies directly applied to the specific resource. 

### Resource and permission hierarchy with Spaces

When you use Apigee with Spaces, the Space resource is added to the hierarchy. Consider a scenario where an Apigee organization has three API proxies, `proxy-a`, `proxy-b`, and `proxy-c`. In this example, `proxy-b` and `proxy-c` are associated with `space-red` and `space-blue`, respectively. When you associate an API resource with a Space, the `space` attribute is set on the resource. 

When you make an API call to get the details of `proxy-c`, your API endpoint reflects the actual resource hierarchy, where the API proxy is a child of the organization _with a Space attribute_ , as shown in the following example: 
    
    
    curl -X GET -H "Authorization: Bearer $TOKEN" "https://apigee.googleapis.com/v1/**organizations/org1/apis/proxy-c** "
    {
      "metaData": {
        "createdAt": "1725665197737",
        "lastModifiedAt": "1725665462105",
        "subType": "Proxy"
      },
      **"name": "proxy-c"** ,
      "revision": [
        "1"
      ],
      "apiProxyType": "PROGRAMMABLE",
      **"space": "space-blue"**
    }

Although the path to an API resource associated with a Space remains the same, the effective _IAM permission hierarchy_ changes. In our example scenario, the IAM permission checks will behave as though the API resource is a child of the Space. As a result, the IAM policies that apply to the API resource include those policies inherited from the Space, in addition to any policies directly applied to the Space, as shown in the following figure: ![IAM hierarchy for Spaces](https://docs.cloud.google.com/static/apigee/docs/api-platform/system-administration/spaces/images/spaces-effective.png)**Figure 1** : The effective IAM permission hierarchy for API resources when using Spaces

## IAM policy checks for Space resources 

As noted in a previous section, when API proxies, shared flows, and API products are associated with a Space, they are treated as child resources of the Space during IAM policy checks. This effective resource hierarchy applies to all sub-children of API proxies, shared flows, and API products.

For example, [API Product attributes](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.attributes#Attribute) are child resources of an API product. To list all attributes of the API product `product-a` in the Apigee organization `org1`, which is associated with the Apigee space `space-blue`, the actual resource path is `GET organizations/org1/apiproduct/product-a/attributes`. However, the path that is checked for IAM permissions is `organizations/org1/**spaces/space-blue** /apiproduct/product-a/attributes`.

### IAM policy checks for deployments

The [Environment](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments) resource is not associated with Spaces. However, some existing APIs have been updated to enable fine-grained access to deployments and debug sessions for API proxies and shared flows.

Changes to IAM permission checks for the following deployment operations on resources in a Space are described below: 

**Method** | **Space IAM Permission Check**  
---|---  
[organizations.deployments.list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.deployments/list) | No changes   
[organizations.apis.deployments.list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.deployments/list) | **apigee.deployments.list** on**** `organizations/$ORG/spaces/$SPACE/apis/$API`  
[organizations.apis.revisions.deployments.list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.revisions.deployments/list) | **apigee.deployments.list** on `organizations/$ORG/spaces/$SPACE/apis/$API/revisions/$REV`  
[organizations.environments.deployments.list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.deployments/list) | No changes   
[organizations.environments.deployments.get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.deployments/get) | No changes   
[organizations.environments.apis.deployments.list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.deployments/list) | **apigee.deployments.list** on `organizations/$ORG/environments/$ENV`  
**OR** `organizations/$ORG/spaces/$SPACE/apis/$API`  
[organizations.environments.apis.revisions.deployments.get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.deployments.get) | **apigee.deployments.get** on `organizations/$ORG/environments/$ENV` **OR** **apigee.deployments.get** on `organizations/$ORG/spaces/$SPACE/apis/$API/revisions/$REV`  
[organizations.environments.apis.revisions.deployments.deploy](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.deployments/deploy) | **apigee.deployments.create** on `organizations/$ORG/environments/$ENV` **AND** **apigee.proxyrevisions.deploy** on `organizations/$ORG/spaces/$SPACE/apis/$API/revisions/$REV`  
[organizations.environments.apis.revisions.deployments.generateDeployChangeReport](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.deployments/generateDeployChangeReport) | **apigee.deployments.create** on `organizations/$ORG/environments/$ENV` **AND** **apigee.proxyrevisions.deploy** on `organizations/$ORG/spaces/$SPACE/apis/$API/revisions/$REV`  
[organizations.environments.apis.revisions.deployments.generateUndeployChangeReport](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.deployments/generateUndeployChangeReport) | **apigee.deployments.delete** on `organizations/$ORG/environments/$ENV` **AND** **apigee.proxyrevisions.undeploy** on `organizations/$ORG/spaces/$SPACE/apis/$API/revisions/$REV`  
[organizations.environments.apis.revisions.deployments.undeploy](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.deployments/undeploy) | **apigee.deployments.delete** on `organizations/$ORG/environments/$ENV` **AND** **apigee.proxyrevisions.undeploy** on `organizations/$ORG/spaces/$SPACE/apis/$API/revisions/$REV`  
[organizations.environments.sharedflows.deployments.list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.sharedflows.deployments/list) | **apigee.deployments.list** on `organizations/$ORG/environments/$ENV`   
OR  
**apigee.deployments.list** on  
`organizations/$ORG/spaces/$SPACE/sharedflows/$SF`  
[organizations.environments.sharedflows.revisions.deployments.deploy](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.sharedflows.revisions.deployments/deploy) | **apigee.deployments.create** on `organizations/$ORG/environments/$ENV` **AND** **apigee.sharedflowrevisions.deploy** on `organizations/$ORG/spaces/$SPACE/sharedflow/$SF/revisions/$REV`  
[organizations.environments.sharedflows.revisions.deployments.get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.sharedflows.revisions.deployments/get) | **apigee.deployments.get** on `organizations/$ORG/environments/$ENV` OR  **apigee.deployments.get** on  `organizations/$ORG/spaces/$SPACE/sharedflows/$SF/revisions/$REV`  
[organizations.environments.sharedflows.revisions.deployments.undeploy](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.sharedflows.revisions.deployments/undeploy) | **apigee.deployments.delete** on `organizations/$ORG/environments/$ENV` **AND** **apigee.sharedflowrevisions.undeploy** on `organizations/$ORG/spaces/$SPACE/sharedflow/$SF/revisions/$REV`  
[organizations.sharedflows.deployments.list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.sharedflows.deployments/list) | **apigee.deployments.list** on  
`organizations/$ORG/spaces/$SPACE/sharedflows/$SF`  
[organizations.sharedflows.revisions.deployments.list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.sharedflows.revisions.deployments/list) | **apigee.deployments.list** on  
`organizations/$ORG/spaces/$SPACE/sharedflows/$SF/revisions/$REV`  
  
## Permission checks for debug sessions

If an API proxy is associated with a Space, the IAM permission checks for the proxy's debug sessions have changed, as described in the following table: 

**Method** | **Space IAM Permission Check**  
---|---  
[organizations.environments.apis.revisions.debugsessions.create](https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions/create) | **apigee.tracesessions.create** on `organizations/$ORG/spaces/$SPACE/apis/$API/revisions/$REV` **AND** `organizations/$ORG/environments/$ENV`  
[organizations.environments.apis.revisions.debugsessions.get](https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions/get) | **apigee.tracesessions.get** on `organizations/$ORG/environments/$ENV`   
**AND** `organizations/$ORG/spaces/$SPACE/apis/$API`  
[organizations.environments.apis.revisions.debugsessions.deleteData](https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions/deleteData) | **apigee.tracesessions.delete** on `organizations/$ORG/environments/$ENV`  
**AND** **apigee.tracesessions.delete** on  `organizations/$ORG/spaces/$SPACE/apis/$API`  
[organizations.environments.apis.revisions.debugsessions.list](https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions/list) | **apigee.tracesessions.list** on `organizations/$ORG/environments/$ENV` **OR** **apigee.tracesessions.list** on `organizations/$ORG/spaces/$SPACE/apis/$API/revisions/$REV`  
[organizations.environments.apis.revisions.debugsessions.data.get](https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions.data/get) | **apigee.tracesessions.get** on `organizations/$ORG/environments/$ENV` **AND** **apigee.tracesessions.get** on `organizations/$ORG/spaces/$SPACE/apis/$API/revisions/$REV`  
[organizations.environments.apis.revisions.debugsessions.data.list](https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions.data/list) | **apigee.tracesessions.get** on `organizations/$ORG/environments/$ENV` AND  **apigee.tracesessions.get** on `organizations/$ORG/spaces/$SPACE/apis/$API`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
