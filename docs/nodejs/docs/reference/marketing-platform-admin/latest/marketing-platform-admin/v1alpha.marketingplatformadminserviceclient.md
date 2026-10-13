---
url: https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/v1alpha.marketingplatformadminserviceclient
title: Class v1alpha.MarketingplatformAdminServiceClient (0.6.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:17.183093+00:00
---

# Class v1alpha.MarketingplatformAdminServiceClient (0.6.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/v1alpha.marketingplatformadminserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1alpha.MarketingplatformAdminServiceClient (0.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.1 (latest)  0.6.0  0.4.0  0.1.0 

Service Interface for the Google Marketing Platform Admin API. v1alpha

## Package

[@google-ads/marketing-platform-admin](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of MarketingplatformAdminServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new MarketingplatformAdminServiceClient({fallback: true}, gax); ```  
  
## Properties 

### apiEndpoint
    
    
    get apiEndpoint(): string;

The DNS address for this API service.

### apiEndpoint
    
    
    static get apiEndpoint(): string;

The DNS address for this API service - same as servicePath.

### auth
    
    
    auth: gax.GoogleAuth;

### descriptors
    
    
    descriptors: Descriptors;

### innerApiCalls
    
    
    innerApiCalls: {
            [name: string]: Function;
        };

### marketingplatformAdminServiceStub
    
    
    marketingplatformAdminServiceStub?: Promise<{
            [name: string]: Function;
        }>;

### pathTemplates
    
    
    pathTemplates: {
            [name: string]: gax.PathTemplate;
        };

### port
    
    
    static get port(): number;

The port for this API service.

### scopes
    
    
    static get scopes(): string[];

The scopes needed to make gRPC calls for every method defined in this service.

### servicePath
    
    
    static get servicePath(): string;

The DNS address for this API service.

### universeDomain
    
    
    get universeDomain(): string;

### warn
    
    
    warn: (code: string, message: string, warnType?: string) => void;

## Methods 

### adminAccessBindingPath(organization, adminAccessBinding)
    
    
    adminAccessBindingPath(organization: string, adminAccessBinding: string): string;

Return a fully-qualified adminAccessBinding resource name string.

**Parameters**  
---  
**Name** | **Description**  
`organization` |  `string`   
  
`adminAccessBinding` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### analyticsAccountLinkPath(organization, analyticsAccountLink)
    
    
    analyticsAccountLinkPath(organization: string, analyticsAccountLink: string): string;

Return a fully-qualified analyticsAccountLink resource name string.

**Parameters**  
---  
**Name** | **Description**  
`organization` |  `string`   
  
`analyticsAccountLink` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### close()
    
    
    close(): Promise<void>;

Terminate the gRPC channel and close the client.

The client will no longer be usable and all future behavior is undefined.

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` | {Promise} A promise that resolves when the client is closed.  
  
### createAdminAccessBinding(request, options)
    
    
    createAdminAccessBinding(request?: protos.google.marketingplatform.admin.v1alpha.ICreateAdminAccessBindingRequest, options?: CallOptions): Promise<[
            protos.google.marketingplatform.admin.v1alpha.IAdminAccessBinding,
            (protos.google.marketingplatform.admin.v1alpha.ICreateAdminAccessBindingRequest | undefined),
            {} | undefined
        ]>;

Creates an admin access binding in the specified GMP organization.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAdminAccessBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.icreateadminaccessbindingrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.marketingplatform.admin.v1alpha.IAdminAccessBinding](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iadminaccessbinding), ([protos.google.marketingplatform.admin.v1alpha.ICreateAdminAccessBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.icreateadminaccessbindingrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [AdminAccessBinding](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.adminaccessbinding). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent organization, which owns this Admin Access Binding.
       *  Format: organizations/{org_id}
       */
      // const parent = 'abc123'
      /**
       *  Required. The Admin Access Binding to create.
       *  Only 'user_email' input is allowed.
       */
      // const adminAccessBinding = {}
    
      // Imports the Admin library
      const {MarketingplatformAdminServiceClient} = require('[@google-ads/marketing-platform-admin](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const adminClient = new [MarketingplatformAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/overview.html)();
    
      async function callCreateAdminAccessBinding() {
        // Construct request
        const request = {
          parent,
          adminAccessBinding,
        };
    
        // Run request
        const response = await adminClient.createAdminAccessBinding(request);
        console.log(response);
      }
    
      callCreateAdminAccessBinding();
    
    

### createAdminAccessBinding(request, options, callback)
    
    
    createAdminAccessBinding(request: protos.google.marketingplatform.admin.v1alpha.ICreateAdminAccessBindingRequest, options: CallOptions, callback: Callback<protos.google.marketingplatform.admin.v1alpha.IAdminAccessBinding, protos.google.marketingplatform.admin.v1alpha.ICreateAdminAccessBindingRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAdminAccessBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.icreateadminaccessbindingrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.marketingplatform.admin.v1alpha.IAdminAccessBinding](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iadminaccessbinding), [protos.google.marketingplatform.admin.v1alpha.ICreateAdminAccessBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.icreateadminaccessbindingrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createAdminAccessBinding(request, callback)
    
    
    createAdminAccessBinding(request: protos.google.marketingplatform.admin.v1alpha.ICreateAdminAccessBindingRequest, callback: Callback<protos.google.marketingplatform.admin.v1alpha.IAdminAccessBinding, protos.google.marketingplatform.admin.v1alpha.ICreateAdminAccessBindingRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAdminAccessBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.icreateadminaccessbindingrequest)`   
  
`callback` |  `Callback<[protos.google.marketingplatform.admin.v1alpha.IAdminAccessBinding](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iadminaccessbinding), [protos.google.marketingplatform.admin.v1alpha.ICreateAdminAccessBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.icreateadminaccessbindingrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createAnalyticsAccountLink(request, options)
    
    
    createAnalyticsAccountLink(request?: protos.google.marketingplatform.admin.v1alpha.ICreateAnalyticsAccountLinkRequest, options?: CallOptions): Promise<[
            protos.google.marketingplatform.admin.v1alpha.IAnalyticsAccountLink,
            (protos.google.marketingplatform.admin.v1alpha.ICreateAnalyticsAccountLinkRequest | undefined),
            {} | undefined
        ]>;

Creates the link between the Analytics account and the Google Marketing Platform organization.

User needs to be an org user, and admin on the Analytics account to create the link. If the account is already linked to an organization, user needs to unlink the account from the current organization, then try link again.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAnalyticsAccountLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.icreateanalyticsaccountlinkrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.marketingplatform.admin.v1alpha.IAnalyticsAccountLink](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ianalyticsaccountlink), ([protos.google.marketingplatform.admin.v1alpha.ICreateAnalyticsAccountLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.icreateanalyticsaccountlinkrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [AnalyticsAccountLink](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.analyticsaccountlink). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource where this Analytics account link will be
       *  created. Format: organizations/{org_id}
       */
      // const parent = 'abc123'
      /**
       *  Required. The Analytics account link to create.
       */
      // const analyticsAccountLink = {}
    
      // Imports the Admin library
      const {MarketingplatformAdminServiceClient} = require('[@google-ads/marketing-platform-admin](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const adminClient = new [MarketingplatformAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/overview.html)();
    
      async function callCreateAnalyticsAccountLink() {
        // Construct request
        const request = {
          parent,
          analyticsAccountLink,
        };
    
        // Run request
        const response = await adminClient.createAnalyticsAccountLink(request);
        console.log(response);
      }
    
      callCreateAnalyticsAccountLink();
    
    

### createAnalyticsAccountLink(request, options, callback)
    
    
    createAnalyticsAccountLink(request: protos.google.marketingplatform.admin.v1alpha.ICreateAnalyticsAccountLinkRequest, options: CallOptions, callback: Callback<protos.google.marketingplatform.admin.v1alpha.IAnalyticsAccountLink, protos.google.marketingplatform.admin.v1alpha.ICreateAnalyticsAccountLinkRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAnalyticsAccountLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.icreateanalyticsaccountlinkrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.marketingplatform.admin.v1alpha.IAnalyticsAccountLink](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ianalyticsaccountlink), [protos.google.marketingplatform.admin.v1alpha.ICreateAnalyticsAccountLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.icreateanalyticsaccountlinkrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createAnalyticsAccountLink(request, callback)
    
    
    createAnalyticsAccountLink(request: protos.google.marketingplatform.admin.v1alpha.ICreateAnalyticsAccountLinkRequest, callback: Callback<protos.google.marketingplatform.admin.v1alpha.IAnalyticsAccountLink, protos.google.marketingplatform.admin.v1alpha.ICreateAnalyticsAccountLinkRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAnalyticsAccountLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.icreateanalyticsaccountlinkrequest)`   
  
`callback` |  `Callback<[protos.google.marketingplatform.admin.v1alpha.IAnalyticsAccountLink](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ianalyticsaccountlink), [protos.google.marketingplatform.admin.v1alpha.ICreateAnalyticsAccountLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.icreateanalyticsaccountlinkrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createUserGroup(request, options)
    
    
    createUserGroup(request?: protos.google.marketingplatform.admin.v1alpha.ICreateUserGroupRequest, options?: CallOptions): Promise<[
            protos.google.marketingplatform.admin.v1alpha.IUserGroup,
            (protos.google.marketingplatform.admin.v1alpha.ICreateUserGroupRequest | undefined),
            {} | undefined
        ]>;

Creates a user group in the specified GMP organization.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateUserGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.icreateusergrouprequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.marketingplatform.admin.v1alpha.IUserGroup](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iusergroup), ([protos.google.marketingplatform.admin.v1alpha.ICreateUserGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.icreateusergrouprequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [UserGroup](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.usergroup). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource where this UserGroup will be created.
       *  Format: organizations/{org_id}
       */
      // const parent = 'abc123'
      /**
       *  Required. The user group to create.
       */
      // const userGroup = {}
    
      // Imports the Admin library
      const {MarketingplatformAdminServiceClient} = require('[@google-ads/marketing-platform-admin](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const adminClient = new [MarketingplatformAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/overview.html)();
    
      async function callCreateUserGroup() {
        // Construct request
        const request = {
          parent,
          userGroup,
        };
    
        // Run request
        const response = await adminClient.createUserGroup(request);
        console.log(response);
      }
    
      callCreateUserGroup();
    
    

### createUserGroup(request, options, callback)
    
    
    createUserGroup(request: protos.google.marketingplatform.admin.v1alpha.ICreateUserGroupRequest, options: CallOptions, callback: Callback<protos.google.marketingplatform.admin.v1alpha.IUserGroup, protos.google.marketingplatform.admin.v1alpha.ICreateUserGroupRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateUserGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.icreateusergrouprequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.marketingplatform.admin.v1alpha.IUserGroup](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iusergroup), [protos.google.marketingplatform.admin.v1alpha.ICreateUserGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.icreateusergrouprequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createUserGroup(request, callback)
    
    
    createUserGroup(request: protos.google.marketingplatform.admin.v1alpha.ICreateUserGroupRequest, callback: Callback<protos.google.marketingplatform.admin.v1alpha.IUserGroup, protos.google.marketingplatform.admin.v1alpha.ICreateUserGroupRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateUserGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.icreateusergrouprequest)`   
  
`callback` |  `Callback<[protos.google.marketingplatform.admin.v1alpha.IUserGroup](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iusergroup), [protos.google.marketingplatform.admin.v1alpha.ICreateUserGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.icreateusergrouprequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createUserGroupMember(request, options)
    
    
    createUserGroupMember(request?: protos.google.marketingplatform.admin.v1alpha.ICreateUserGroupMemberRequest, options?: CallOptions): Promise<[
            protos.google.marketingplatform.admin.v1alpha.IUserGroupMember,
            (protos.google.marketingplatform.admin.v1alpha.ICreateUserGroupMemberRequest | undefined),
            {} | undefined
        ]>;

Adds a member to the specified GMP user group.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateUserGroupMemberRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.icreateusergroupmemberrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.marketingplatform.admin.v1alpha.IUserGroupMember](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iusergroupmember), ([protos.google.marketingplatform.admin.v1alpha.ICreateUserGroupMemberRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.icreateusergroupmemberrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource where this UserGroupMember will be created.
       *  Format: organizations/{org_id}/userGroups/{user_group_id}
       */
      // const parent = 'abc123'
      /**
       *  Required. The user group member to create.
       */
      // const userGroupMember = {}
    
      // Imports the Admin library
      const {MarketingplatformAdminServiceClient} = require('[@google-ads/marketing-platform-admin](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const adminClient = new [MarketingplatformAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/overview.html)();
    
      async function callCreateUserGroupMember() {
        // Construct request
        const request = {
          parent,
          userGroupMember,
        };
    
        // Run request
        const response = await adminClient.createUserGroupMember(request);
        console.log(response);
      }
    
      callCreateUserGroupMember();
    
    

### createUserGroupMember(request, options, callback)
    
    
    createUserGroupMember(request: protos.google.marketingplatform.admin.v1alpha.ICreateUserGroupMemberRequest, options: CallOptions, callback: Callback<protos.google.marketingplatform.admin.v1alpha.IUserGroupMember, protos.google.marketingplatform.admin.v1alpha.ICreateUserGroupMemberRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateUserGroupMemberRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.icreateusergroupmemberrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.marketingplatform.admin.v1alpha.IUserGroupMember](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iusergroupmember), [protos.google.marketingplatform.admin.v1alpha.ICreateUserGroupMemberRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.icreateusergroupmemberrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createUserGroupMember(request, callback)
    
    
    createUserGroupMember(request: protos.google.marketingplatform.admin.v1alpha.ICreateUserGroupMemberRequest, callback: Callback<protos.google.marketingplatform.admin.v1alpha.IUserGroupMember, protos.google.marketingplatform.admin.v1alpha.ICreateUserGroupMemberRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateUserGroupMemberRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.icreateusergroupmemberrequest)`   
  
`callback` |  `Callback<[protos.google.marketingplatform.admin.v1alpha.IUserGroupMember](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iusergroupmember), [protos.google.marketingplatform.admin.v1alpha.ICreateUserGroupMemberRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.icreateusergroupmemberrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAnalyticsAccountLink(request, options)
    
    
    deleteAnalyticsAccountLink(request?: protos.google.marketingplatform.admin.v1alpha.IDeleteAnalyticsAccountLinkRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.marketingplatform.admin.v1alpha.IDeleteAnalyticsAccountLinkRequest | undefined),
            {} | undefined
        ]>;

Deletes the AnalyticsAccountLink, which detaches the Analytics account from the Google Marketing Platform organization.

User needs to be an org user, and admin on the Analytics account in order to delete the link.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAnalyticsAccountLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ideleteanalyticsaccountlinkrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.protobuf.iempty), ([protos.google.marketingplatform.admin.v1alpha.IDeleteAnalyticsAccountLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ideleteanalyticsaccountlinkrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the Analytics account link to delete.
       *  Format:
       *  organizations/{org_id}/analyticsAccountLinks/{analytics_account_link_id}
       */
      // const name = 'abc123'
    
      // Imports the Admin library
      const {MarketingplatformAdminServiceClient} = require('[@google-ads/marketing-platform-admin](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const adminClient = new [MarketingplatformAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/overview.html)();
    
      async function callDeleteAnalyticsAccountLink() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await adminClient.deleteAnalyticsAccountLink(request);
        console.log(response);
      }
    
      callDeleteAnalyticsAccountLink();
    
    

### deleteAnalyticsAccountLink(request, options, callback)
    
    
    deleteAnalyticsAccountLink(request: protos.google.marketingplatform.admin.v1alpha.IDeleteAnalyticsAccountLinkRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.marketingplatform.admin.v1alpha.IDeleteAnalyticsAccountLinkRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAnalyticsAccountLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ideleteanalyticsaccountlinkrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.protobuf.iempty), [protos.google.marketingplatform.admin.v1alpha.IDeleteAnalyticsAccountLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ideleteanalyticsaccountlinkrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAnalyticsAccountLink(request, callback)
    
    
    deleteAnalyticsAccountLink(request: protos.google.marketingplatform.admin.v1alpha.IDeleteAnalyticsAccountLinkRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.marketingplatform.admin.v1alpha.IDeleteAnalyticsAccountLinkRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAnalyticsAccountLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ideleteanalyticsaccountlinkrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.protobuf.iempty), [protos.google.marketingplatform.admin.v1alpha.IDeleteAnalyticsAccountLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ideleteanalyticsaccountlinkrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteUserGroup(request, options)
    
    
    deleteUserGroup(request?: protos.google.marketingplatform.admin.v1alpha.IDeleteUserGroupRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.marketingplatform.admin.v1alpha.IDeleteUserGroupRequest | undefined),
            {} | undefined
        ]>;

Deletes a user group in the specified GMP organization.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteUserGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ideleteusergrouprequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.protobuf.iempty), ([protos.google.marketingplatform.admin.v1alpha.IDeleteUserGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ideleteusergrouprequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the user group to delete.
       *  Format: organizations/{org_id}/userGroups/{user_group_id}
       */
      // const name = 'abc123'
    
      // Imports the Admin library
      const {MarketingplatformAdminServiceClient} = require('[@google-ads/marketing-platform-admin](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const adminClient = new [MarketingplatformAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/overview.html)();
    
      async function callDeleteUserGroup() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await adminClient.deleteUserGroup(request);
        console.log(response);
      }
    
      callDeleteUserGroup();
    
    

### deleteUserGroup(request, options, callback)
    
    
    deleteUserGroup(request: protos.google.marketingplatform.admin.v1alpha.IDeleteUserGroupRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.marketingplatform.admin.v1alpha.IDeleteUserGroupRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteUserGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ideleteusergrouprequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.protobuf.iempty), [protos.google.marketingplatform.admin.v1alpha.IDeleteUserGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ideleteusergrouprequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteUserGroup(request, callback)
    
    
    deleteUserGroup(request: protos.google.marketingplatform.admin.v1alpha.IDeleteUserGroupRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.marketingplatform.admin.v1alpha.IDeleteUserGroupRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteUserGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ideleteusergrouprequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.protobuf.iempty), [protos.google.marketingplatform.admin.v1alpha.IDeleteUserGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ideleteusergrouprequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteUserGroupMember(request, options)
    
    
    deleteUserGroupMember(request?: protos.google.marketingplatform.admin.v1alpha.IDeleteUserGroupMemberRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.marketingplatform.admin.v1alpha.IDeleteUserGroupMemberRequest | undefined),
            {} | undefined
        ]>;

Deletes a member in the specified GMP user group.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteUserGroupMemberRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ideleteusergroupmemberrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.protobuf.iempty), ([protos.google.marketingplatform.admin.v1alpha.IDeleteUserGroupMemberRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ideleteusergroupmemberrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the user group member to delete.
       *  Format:
       *  organizations/{org_id}/userGroups/{user_group_id}/members/{member_id}
       */
      // const name = 'abc123'
    
      // Imports the Admin library
      const {MarketingplatformAdminServiceClient} = require('[@google-ads/marketing-platform-admin](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const adminClient = new [MarketingplatformAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/overview.html)();
    
      async function callDeleteUserGroupMember() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await adminClient.deleteUserGroupMember(request);
        console.log(response);
      }
    
      callDeleteUserGroupMember();
    
    

### deleteUserGroupMember(request, options, callback)
    
    
    deleteUserGroupMember(request: protos.google.marketingplatform.admin.v1alpha.IDeleteUserGroupMemberRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.marketingplatform.admin.v1alpha.IDeleteUserGroupMemberRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteUserGroupMemberRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ideleteusergroupmemberrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.protobuf.iempty), [protos.google.marketingplatform.admin.v1alpha.IDeleteUserGroupMemberRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ideleteusergroupmemberrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteUserGroupMember(request, callback)
    
    
    deleteUserGroupMember(request: protos.google.marketingplatform.admin.v1alpha.IDeleteUserGroupMemberRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.marketingplatform.admin.v1alpha.IDeleteUserGroupMemberRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteUserGroupMemberRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ideleteusergroupmemberrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.protobuf.iempty), [protos.google.marketingplatform.admin.v1alpha.IDeleteUserGroupMemberRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ideleteusergroupmemberrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### findSalesPartnerManagedClients(request, options)
    
    
    findSalesPartnerManagedClients(request?: protos.google.marketingplatform.admin.v1alpha.IFindSalesPartnerManagedClientsRequest, options?: CallOptions): Promise<[
            protos.google.marketingplatform.admin.v1alpha.IFindSalesPartnerManagedClientsResponse,
            (protos.google.marketingplatform.admin.v1alpha.IFindSalesPartnerManagedClientsRequest | undefined),
            {} | undefined
        ]>;

Returns a list of clients managed by the sales partner organization.

User needs to be an OrgAdmin/BillingAdmin on the sales partner organization in order to view the end clients.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFindSalesPartnerManagedClientsRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ifindsalespartnermanagedclientsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.marketingplatform.admin.v1alpha.IFindSalesPartnerManagedClientsResponse](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ifindsalespartnermanagedclientsresponse), ([protos.google.marketingplatform.admin.v1alpha.IFindSalesPartnerManagedClientsRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ifindsalespartnermanagedclientsrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the sales partner organization.
       *  Format: organizations/{org_id}
       */
      // const organization = 'abc123'
      /**
       *  Optional. If set, only active and just ended clients will be returned.
       */
      // const isActive = true
    
      // Imports the Admin library
      const {MarketingplatformAdminServiceClient} = require('[@google-ads/marketing-platform-admin](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const adminClient = new [MarketingplatformAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/overview.html)();
    
      async function callFindSalesPartnerManagedClients() {
        // Construct request
        const request = {
          organization,
        };
    
        // Run request
        const response = await adminClient.findSalesPartnerManagedClients(request);
        console.log(response);
      }
    
      callFindSalesPartnerManagedClients();
    
    

### findSalesPartnerManagedClients(request, options, callback)
    
    
    findSalesPartnerManagedClients(request: protos.google.marketingplatform.admin.v1alpha.IFindSalesPartnerManagedClientsRequest, options: CallOptions, callback: Callback<protos.google.marketingplatform.admin.v1alpha.IFindSalesPartnerManagedClientsResponse, protos.google.marketingplatform.admin.v1alpha.IFindSalesPartnerManagedClientsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFindSalesPartnerManagedClientsRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ifindsalespartnermanagedclientsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.marketingplatform.admin.v1alpha.IFindSalesPartnerManagedClientsResponse](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ifindsalespartnermanagedclientsresponse), [protos.google.marketingplatform.admin.v1alpha.IFindSalesPartnerManagedClientsRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ifindsalespartnermanagedclientsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### findSalesPartnerManagedClients(request, callback)
    
    
    findSalesPartnerManagedClients(request: protos.google.marketingplatform.admin.v1alpha.IFindSalesPartnerManagedClientsRequest, callback: Callback<protos.google.marketingplatform.admin.v1alpha.IFindSalesPartnerManagedClientsResponse, protos.google.marketingplatform.admin.v1alpha.IFindSalesPartnerManagedClientsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFindSalesPartnerManagedClientsRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ifindsalespartnermanagedclientsrequest)`   
  
`callback` |  `Callback<[protos.google.marketingplatform.admin.v1alpha.IFindSalesPartnerManagedClientsResponse](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ifindsalespartnermanagedclientsresponse), [protos.google.marketingplatform.admin.v1alpha.IFindSalesPartnerManagedClientsRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ifindsalespartnermanagedclientsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAdminAccessBinding(request, options)
    
    
    getAdminAccessBinding(request?: protos.google.marketingplatform.admin.v1alpha.IGetAdminAccessBindingRequest, options?: CallOptions): Promise<[
            protos.google.marketingplatform.admin.v1alpha.IAdminAccessBinding,
            (protos.google.marketingplatform.admin.v1alpha.IGetAdminAccessBindingRequest | undefined),
            {} | undefined
        ]>;

Looks up a single admin access binding.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAdminAccessBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.igetadminaccessbindingrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.marketingplatform.admin.v1alpha.IAdminAccessBinding](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iadminaccessbinding), ([protos.google.marketingplatform.admin.v1alpha.IGetAdminAccessBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.igetadminaccessbindingrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [AdminAccessBinding](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.adminaccessbinding). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the AdminAccessBinding to retrieve.
       *  Format:
       *  organizations/{org_id}/adminAccessBindings/{admin_access_binding_id}
       */
      // const name = 'abc123'
    
      // Imports the Admin library
      const {MarketingplatformAdminServiceClient} = require('[@google-ads/marketing-platform-admin](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const adminClient = new [MarketingplatformAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/overview.html)();
    
      async function callGetAdminAccessBinding() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await adminClient.getAdminAccessBinding(request);
        console.log(response);
      }
    
      callGetAdminAccessBinding();
    
    

### getAdminAccessBinding(request, options, callback)
    
    
    getAdminAccessBinding(request: protos.google.marketingplatform.admin.v1alpha.IGetAdminAccessBindingRequest, options: CallOptions, callback: Callback<protos.google.marketingplatform.admin.v1alpha.IAdminAccessBinding, protos.google.marketingplatform.admin.v1alpha.IGetAdminAccessBindingRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAdminAccessBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.igetadminaccessbindingrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.marketingplatform.admin.v1alpha.IAdminAccessBinding](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iadminaccessbinding), [protos.google.marketingplatform.admin.v1alpha.IGetAdminAccessBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.igetadminaccessbindingrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAdminAccessBinding(request, callback)
    
    
    getAdminAccessBinding(request: protos.google.marketingplatform.admin.v1alpha.IGetAdminAccessBindingRequest, callback: Callback<protos.google.marketingplatform.admin.v1alpha.IAdminAccessBinding, protos.google.marketingplatform.admin.v1alpha.IGetAdminAccessBindingRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAdminAccessBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.igetadminaccessbindingrequest)`   
  
`callback` |  `Callback<[protos.google.marketingplatform.admin.v1alpha.IAdminAccessBinding](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iadminaccessbinding), [protos.google.marketingplatform.admin.v1alpha.IGetAdminAccessBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.igetadminaccessbindingrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getOrganization(request, options)
    
    
    getOrganization(request?: protos.google.marketingplatform.admin.v1alpha.IGetOrganizationRequest, options?: CallOptions): Promise<[
            protos.google.marketingplatform.admin.v1alpha.IOrganization,
            (protos.google.marketingplatform.admin.v1alpha.IGetOrganizationRequest | undefined),
            {} | undefined
        ]>;

Looks up a single organization.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetOrganizationRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.igetorganizationrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.marketingplatform.admin.v1alpha.IOrganization](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iorganization), ([protos.google.marketingplatform.admin.v1alpha.IGetOrganizationRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.igetorganizationrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Organization](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.organization). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the Organization to retrieve.
       *  Format: organizations/{org_id}
       */
      // const name = 'abc123'
    
      // Imports the Admin library
      const {MarketingplatformAdminServiceClient} = require('[@google-ads/marketing-platform-admin](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const adminClient = new [MarketingplatformAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/overview.html)();
    
      async function callGetOrganization() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await adminClient.getOrganization(request);
        console.log(response);
      }
    
      callGetOrganization();
    
    

### getOrganization(request, options, callback)
    
    
    getOrganization(request: protos.google.marketingplatform.admin.v1alpha.IGetOrganizationRequest, options: CallOptions, callback: Callback<protos.google.marketingplatform.admin.v1alpha.IOrganization, protos.google.marketingplatform.admin.v1alpha.IGetOrganizationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetOrganizationRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.igetorganizationrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.marketingplatform.admin.v1alpha.IOrganization](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iorganization), [protos.google.marketingplatform.admin.v1alpha.IGetOrganizationRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.igetorganizationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getOrganization(request, callback)
    
    
    getOrganization(request: protos.google.marketingplatform.admin.v1alpha.IGetOrganizationRequest, callback: Callback<protos.google.marketingplatform.admin.v1alpha.IOrganization, protos.google.marketingplatform.admin.v1alpha.IGetOrganizationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetOrganizationRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.igetorganizationrequest)`   
  
`callback` |  `Callback<[protos.google.marketingplatform.admin.v1alpha.IOrganization](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iorganization), [protos.google.marketingplatform.admin.v1alpha.IGetOrganizationRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.igetorganizationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getProjectId()
    
    
    getProjectId(): Promise<string>;

**Returns**  
---  
**Type** | **Description**  
`Promise<string>` |   
  
### getProjectId(callback)
    
    
    getProjectId(callback: Callback<string, undefined, undefined>): void;

**Parameter**  
---  
**Name** | **Description**  
`callback` |  `Callback<string, undefined, undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getUserGroup(request, options)
    
    
    getUserGroup(request?: protos.google.marketingplatform.admin.v1alpha.IGetUserGroupRequest, options?: CallOptions): Promise<[
            protos.google.marketingplatform.admin.v1alpha.IUserGroup,
            (protos.google.marketingplatform.admin.v1alpha.IGetUserGroupRequest | undefined),
            {} | undefined
        ]>;

Looks up a single user group.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetUserGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.igetusergrouprequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.marketingplatform.admin.v1alpha.IUserGroup](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iusergroup), ([protos.google.marketingplatform.admin.v1alpha.IGetUserGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.igetusergrouprequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [UserGroup](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.usergroup). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the UserGroup to retrieve.
       *  Format: organizations/{org_id}/userGroups/{user_group_id}
       */
      // const name = 'abc123'
    
      // Imports the Admin library
      const {MarketingplatformAdminServiceClient} = require('[@google-ads/marketing-platform-admin](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const adminClient = new [MarketingplatformAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/overview.html)();
    
      async function callGetUserGroup() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await adminClient.getUserGroup(request);
        console.log(response);
      }
    
      callGetUserGroup();
    
    

### getUserGroup(request, options, callback)
    
    
    getUserGroup(request: protos.google.marketingplatform.admin.v1alpha.IGetUserGroupRequest, options: CallOptions, callback: Callback<protos.google.marketingplatform.admin.v1alpha.IUserGroup, protos.google.marketingplatform.admin.v1alpha.IGetUserGroupRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetUserGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.igetusergrouprequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.marketingplatform.admin.v1alpha.IUserGroup](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iusergroup), [protos.google.marketingplatform.admin.v1alpha.IGetUserGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.igetusergrouprequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getUserGroup(request, callback)
    
    
    getUserGroup(request: protos.google.marketingplatform.admin.v1alpha.IGetUserGroupRequest, callback: Callback<protos.google.marketingplatform.admin.v1alpha.IUserGroup, protos.google.marketingplatform.admin.v1alpha.IGetUserGroupRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetUserGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.igetusergrouprequest)`   
  
`callback` |  `Callback<[protos.google.marketingplatform.admin.v1alpha.IUserGroup](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iusergroup), [protos.google.marketingplatform.admin.v1alpha.IGetUserGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.igetusergrouprequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getUserGroupMember(request, options)
    
    
    getUserGroupMember(request?: protos.google.marketingplatform.admin.v1alpha.IGetUserGroupMemberRequest, options?: CallOptions): Promise<[
            protos.google.marketingplatform.admin.v1alpha.IUserGroupMember,
            (protos.google.marketingplatform.admin.v1alpha.IGetUserGroupMemberRequest | undefined),
            {} | undefined
        ]>;

Looks up a single user group member.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetUserGroupMemberRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.igetusergroupmemberrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.marketingplatform.admin.v1alpha.IUserGroupMember](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iusergroupmember), ([protos.google.marketingplatform.admin.v1alpha.IGetUserGroupMemberRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.igetusergroupmemberrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the user group member to retrieve.
       *  Format:
       *  organizations/{org_id}/userGroups/{user_group_id}/members/{member_id}
       */
      // const name = 'abc123'
    
      // Imports the Admin library
      const {MarketingplatformAdminServiceClient} = require('[@google-ads/marketing-platform-admin](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const adminClient = new [MarketingplatformAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/overview.html)();
    
      async function callGetUserGroupMember() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await adminClient.getUserGroupMember(request);
        console.log(response);
      }
    
      callGetUserGroupMember();
    
    

### getUserGroupMember(request, options, callback)
    
    
    getUserGroupMember(request: protos.google.marketingplatform.admin.v1alpha.IGetUserGroupMemberRequest, options: CallOptions, callback: Callback<protos.google.marketingplatform.admin.v1alpha.IUserGroupMember, protos.google.marketingplatform.admin.v1alpha.IGetUserGroupMemberRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetUserGroupMemberRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.igetusergroupmemberrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.marketingplatform.admin.v1alpha.IUserGroupMember](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iusergroupmember), [protos.google.marketingplatform.admin.v1alpha.IGetUserGroupMemberRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.igetusergroupmemberrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getUserGroupMember(request, callback)
    
    
    getUserGroupMember(request: protos.google.marketingplatform.admin.v1alpha.IGetUserGroupMemberRequest, callback: Callback<protos.google.marketingplatform.admin.v1alpha.IUserGroupMember, protos.google.marketingplatform.admin.v1alpha.IGetUserGroupMemberRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetUserGroupMemberRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.igetusergroupmemberrequest)`   
  
`callback` |  `Callback<[protos.google.marketingplatform.admin.v1alpha.IUserGroupMember](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iusergroupmember), [protos.google.marketingplatform.admin.v1alpha.IGetUserGroupMemberRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.igetusergroupmemberrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### initialize()
    
    
    initialize(): Promise<{
            [name: string]: Function;
        }>;

Initialize the client. Performs asynchronous operations (such as authentication) and prepares the client. This function will be called automatically when any class method is called for the first time, but if you need to initialize it before calling an actual method, feel free to call initialize() directly.

You can await on this method if you want to make sure the client is initialized.

**Returns**  
---  
**Type** | **Description**  
`Promise<{ [name: string]: Function; }>` | {Promise} A promise that resolves to an authenticated service stub.  
  
### listAdminAccessBindings(request, options)
    
    
    listAdminAccessBindings(request?: protos.google.marketingplatform.admin.v1alpha.IListAdminAccessBindingsRequest, options?: CallOptions): Promise<[
            protos.google.marketingplatform.admin.v1alpha.IAdminAccessBinding[],
            protos.google.marketingplatform.admin.v1alpha.IListAdminAccessBindingsRequest | null,
            protos.google.marketingplatform.admin.v1alpha.IListAdminAccessBindingsResponse
        ]>;

Returns a list of admin access bindings in the specified GMP organization.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAdminAccessBindingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistadminaccessbindingsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.marketingplatform.admin.v1alpha.IAdminAccessBinding](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iadminaccessbinding)[], [protos.google.marketingplatform.admin.v1alpha.IListAdminAccessBindingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistadminaccessbindingsrequest) | null, [protos.google.marketingplatform.admin.v1alpha.IListAdminAccessBindingsResponse](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistadminaccessbindingsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [AdminAccessBinding](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.adminaccessbinding). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listAdminAccessBindingsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listAdminAccessBindings(request, options, callback)
    
    
    listAdminAccessBindings(request: protos.google.marketingplatform.admin.v1alpha.IListAdminAccessBindingsRequest, options: CallOptions, callback: PaginationCallback<protos.google.marketingplatform.admin.v1alpha.IListAdminAccessBindingsRequest, protos.google.marketingplatform.admin.v1alpha.IListAdminAccessBindingsResponse | null | undefined, protos.google.marketingplatform.admin.v1alpha.IAdminAccessBinding>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAdminAccessBindingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistadminaccessbindingsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.marketingplatform.admin.v1alpha.IListAdminAccessBindingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistadminaccessbindingsrequest), [protos.google.marketingplatform.admin.v1alpha.IListAdminAccessBindingsResponse](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistadminaccessbindingsresponse) | null | undefined, [protos.google.marketingplatform.admin.v1alpha.IAdminAccessBinding](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iadminaccessbinding)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAdminAccessBindings(request, callback)
    
    
    listAdminAccessBindings(request: protos.google.marketingplatform.admin.v1alpha.IListAdminAccessBindingsRequest, callback: PaginationCallback<protos.google.marketingplatform.admin.v1alpha.IListAdminAccessBindingsRequest, protos.google.marketingplatform.admin.v1alpha.IListAdminAccessBindingsResponse | null | undefined, protos.google.marketingplatform.admin.v1alpha.IAdminAccessBinding>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAdminAccessBindingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistadminaccessbindingsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.marketingplatform.admin.v1alpha.IListAdminAccessBindingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistadminaccessbindingsrequest), [protos.google.marketingplatform.admin.v1alpha.IListAdminAccessBindingsResponse](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistadminaccessbindingsresponse) | null | undefined, [protos.google.marketingplatform.admin.v1alpha.IAdminAccessBinding](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iadminaccessbinding)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAdminAccessBindingsAsync(request, options)
    
    
    listAdminAccessBindingsAsync(request?: protos.google.marketingplatform.admin.v1alpha.IListAdminAccessBindingsRequest, options?: CallOptions): AsyncIterable<protos.google.marketingplatform.admin.v1alpha.IAdminAccessBinding>;

Equivalent to `listAdminAccessBindings`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAdminAccessBindingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistadminaccessbindingsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.marketingplatform.admin.v1alpha.IAdminAccessBinding](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iadminaccessbinding)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [AdminAccessBinding](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.adminaccessbinding). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent organization, which owns this collection of Admin
       *  Access Bindings. Format: organizations/{org_id}
       */
      // const parent = 'abc123'
      /**
       *  Optional. The maximum number of Admin Access Bindings to return in one
       *  call. The service may return fewer than this value.
       *  If unspecified, at most 50 Admin Access Bindings will be returned. The
       *  maximum value is 1000; values above 1000 will be coerced to 1000.
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous ListAdminAccessBindings
       *  call. Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to
       *  `ListAdminAccessBindings` must match the call that provided the page
       *  token.
       */
      // const pageToken = 'abc123'
    
      // Imports the Admin library
      const {MarketingplatformAdminServiceClient} = require('[@google-ads/marketing-platform-admin](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const adminClient = new [MarketingplatformAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/overview.html)();
    
      async function callListAdminAccessBindings() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = adminClient.[listAdminAccessBindingsAsync](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/v1alpha.marketingplatformadminserviceclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListAdminAccessBindings();
    
    

### listAdminAccessBindingsStream(request, options)
    
    
    listAdminAccessBindingsStream(request?: protos.google.marketingplatform.admin.v1alpha.IListAdminAccessBindingsRequest, options?: CallOptions): Transform;

Equivalent to `listAdminAccessBindings`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAdminAccessBindingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistadminaccessbindingsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [AdminAccessBinding](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.adminaccessbinding) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listAdminAccessBindingsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listAnalyticsAccountLinks(request, options)
    
    
    listAnalyticsAccountLinks(request?: protos.google.marketingplatform.admin.v1alpha.IListAnalyticsAccountLinksRequest, options?: CallOptions): Promise<[
            protos.google.marketingplatform.admin.v1alpha.IAnalyticsAccountLink[],
            protos.google.marketingplatform.admin.v1alpha.IListAnalyticsAccountLinksRequest | null,
            protos.google.marketingplatform.admin.v1alpha.IListAnalyticsAccountLinksResponse
        ]>;

Lists the Google Analytics accounts link to the specified Google Marketing Platform organization.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAnalyticsAccountLinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistanalyticsaccountlinksrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.marketingplatform.admin.v1alpha.IAnalyticsAccountLink](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ianalyticsaccountlink)[], [protos.google.marketingplatform.admin.v1alpha.IListAnalyticsAccountLinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistanalyticsaccountlinksrequest) | null, [protos.google.marketingplatform.admin.v1alpha.IListAnalyticsAccountLinksResponse](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistanalyticsaccountlinksresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [AnalyticsAccountLink](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.analyticsaccountlink). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listAnalyticsAccountLinksAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listAnalyticsAccountLinks(request, options, callback)
    
    
    listAnalyticsAccountLinks(request: protos.google.marketingplatform.admin.v1alpha.IListAnalyticsAccountLinksRequest, options: CallOptions, callback: PaginationCallback<protos.google.marketingplatform.admin.v1alpha.IListAnalyticsAccountLinksRequest, protos.google.marketingplatform.admin.v1alpha.IListAnalyticsAccountLinksResponse | null | undefined, protos.google.marketingplatform.admin.v1alpha.IAnalyticsAccountLink>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAnalyticsAccountLinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistanalyticsaccountlinksrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.marketingplatform.admin.v1alpha.IListAnalyticsAccountLinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistanalyticsaccountlinksrequest), [protos.google.marketingplatform.admin.v1alpha.IListAnalyticsAccountLinksResponse](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistanalyticsaccountlinksresponse) | null | undefined, [protos.google.marketingplatform.admin.v1alpha.IAnalyticsAccountLink](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ianalyticsaccountlink)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAnalyticsAccountLinks(request, callback)
    
    
    listAnalyticsAccountLinks(request: protos.google.marketingplatform.admin.v1alpha.IListAnalyticsAccountLinksRequest, callback: PaginationCallback<protos.google.marketingplatform.admin.v1alpha.IListAnalyticsAccountLinksRequest, protos.google.marketingplatform.admin.v1alpha.IListAnalyticsAccountLinksResponse | null | undefined, protos.google.marketingplatform.admin.v1alpha.IAnalyticsAccountLink>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAnalyticsAccountLinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistanalyticsaccountlinksrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.marketingplatform.admin.v1alpha.IListAnalyticsAccountLinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistanalyticsaccountlinksrequest), [protos.google.marketingplatform.admin.v1alpha.IListAnalyticsAccountLinksResponse](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistanalyticsaccountlinksresponse) | null | undefined, [protos.google.marketingplatform.admin.v1alpha.IAnalyticsAccountLink](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ianalyticsaccountlink)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAnalyticsAccountLinksAsync(request, options)
    
    
    listAnalyticsAccountLinksAsync(request?: protos.google.marketingplatform.admin.v1alpha.IListAnalyticsAccountLinksRequest, options?: CallOptions): AsyncIterable<protos.google.marketingplatform.admin.v1alpha.IAnalyticsAccountLink>;

Equivalent to `listAnalyticsAccountLinks`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAnalyticsAccountLinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistanalyticsaccountlinksrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.marketingplatform.admin.v1alpha.IAnalyticsAccountLink](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ianalyticsaccountlink)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [AnalyticsAccountLink](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.analyticsaccountlink). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent organization, which owns this collection of Analytics
       *  account links. Format: organizations/{org_id}
       */
      // const parent = 'abc123'
      /**
       *  Optional. The maximum number of Analytics account links to return in one
       *  call. The service may return fewer than this value.
       *  If unspecified, at most 50 Analytics account links will be returned. The
       *  maximum value is 1000; values above 1000 will be coerced to 1000.
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous ListAnalyticsAccountLinks
       *  call. Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to
       *  `ListAnalyticsAccountLinks` must match the call that provided the page
       *  token.
       */
      // const pageToken = 'abc123'
    
      // Imports the Admin library
      const {MarketingplatformAdminServiceClient} = require('[@google-ads/marketing-platform-admin](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const adminClient = new [MarketingplatformAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/overview.html)();
    
      async function callListAnalyticsAccountLinks() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = adminClient.[listAnalyticsAccountLinksAsync](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/v1alpha.marketingplatformadminserviceclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListAnalyticsAccountLinks();
    
    

### listAnalyticsAccountLinksStream(request, options)
    
    
    listAnalyticsAccountLinksStream(request?: protos.google.marketingplatform.admin.v1alpha.IListAnalyticsAccountLinksRequest, options?: CallOptions): Transform;

Equivalent to `listAnalyticsAccountLinks`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAnalyticsAccountLinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistanalyticsaccountlinksrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [AnalyticsAccountLink](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.analyticsaccountlink) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listAnalyticsAccountLinksAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listOrganizations(request, options)
    
    
    listOrganizations(request?: protos.google.marketingplatform.admin.v1alpha.IListOrganizationsRequest, options?: CallOptions): Promise<[
            protos.google.marketingplatform.admin.v1alpha.IOrganization[],
            protos.google.marketingplatform.admin.v1alpha.IListOrganizationsRequest | null,
            protos.google.marketingplatform.admin.v1alpha.IListOrganizationsResponse
        ]>;

Returns a list of organizations that the user has access to.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListOrganizationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistorganizationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.marketingplatform.admin.v1alpha.IOrganization](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iorganization)[], [protos.google.marketingplatform.admin.v1alpha.IListOrganizationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistorganizationsrequest) | null, [protos.google.marketingplatform.admin.v1alpha.IListOrganizationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistorganizationsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [Organization](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.organization). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listOrganizationsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listOrganizations(request, options, callback)
    
    
    listOrganizations(request: protos.google.marketingplatform.admin.v1alpha.IListOrganizationsRequest, options: CallOptions, callback: PaginationCallback<protos.google.marketingplatform.admin.v1alpha.IListOrganizationsRequest, protos.google.marketingplatform.admin.v1alpha.IListOrganizationsResponse | null | undefined, protos.google.marketingplatform.admin.v1alpha.IOrganization>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListOrganizationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistorganizationsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.marketingplatform.admin.v1alpha.IListOrganizationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistorganizationsrequest), [protos.google.marketingplatform.admin.v1alpha.IListOrganizationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistorganizationsresponse) | null | undefined, [protos.google.marketingplatform.admin.v1alpha.IOrganization](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iorganization)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listOrganizations(request, callback)
    
    
    listOrganizations(request: protos.google.marketingplatform.admin.v1alpha.IListOrganizationsRequest, callback: PaginationCallback<protos.google.marketingplatform.admin.v1alpha.IListOrganizationsRequest, protos.google.marketingplatform.admin.v1alpha.IListOrganizationsResponse | null | undefined, protos.google.marketingplatform.admin.v1alpha.IOrganization>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListOrganizationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistorganizationsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.marketingplatform.admin.v1alpha.IListOrganizationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistorganizationsrequest), [protos.google.marketingplatform.admin.v1alpha.IListOrganizationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistorganizationsresponse) | null | undefined, [protos.google.marketingplatform.admin.v1alpha.IOrganization](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iorganization)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listOrganizationsAsync(request, options)
    
    
    listOrganizationsAsync(request?: protos.google.marketingplatform.admin.v1alpha.IListOrganizationsRequest, options?: CallOptions): AsyncIterable<protos.google.marketingplatform.admin.v1alpha.IOrganization>;

Equivalent to `listOrganizations`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListOrganizationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistorganizationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.marketingplatform.admin.v1alpha.IOrganization](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iorganization)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [Organization](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.organization). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. The maximum number of organizations to return in one call. The
       *  service may return fewer than this value.
       *  If unspecified, at most 50 organizations will be returned. The
       *  maximum value is 1000; values above 1000 will be coerced to 1000.
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous ListOrganizations call.
       *  Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to
       *  `ListOrganizations` must match the call that provided the page
       *  token.
       */
      // const pageToken = 'abc123'
    
      // Imports the Admin library
      const {MarketingplatformAdminServiceClient} = require('[@google-ads/marketing-platform-admin](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const adminClient = new [MarketingplatformAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/overview.html)();
    
      async function callListOrganizations() {
        // Construct request
        const request = {
        };
    
        // Run request
        const iterable = adminClient.[listOrganizationsAsync](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/v1alpha.marketingplatformadminserviceclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListOrganizations();
    
    

### listOrganizationsStream(request, options)
    
    
    listOrganizationsStream(request?: protos.google.marketingplatform.admin.v1alpha.IListOrganizationsRequest, options?: CallOptions): Transform;

Equivalent to `listOrganizations`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListOrganizationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistorganizationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [Organization](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.organization) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listOrganizationsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listUserGroupMembers(request, options)
    
    
    listUserGroupMembers(request?: protos.google.marketingplatform.admin.v1alpha.IListUserGroupMembersRequest, options?: CallOptions): Promise<[
            protos.google.marketingplatform.admin.v1alpha.IUserGroupMember[],
            protos.google.marketingplatform.admin.v1alpha.IListUserGroupMembersRequest | null,
            protos.google.marketingplatform.admin.v1alpha.IListUserGroupMembersResponse
        ]>;

Returns a list of members in the specified user group.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListUserGroupMembersRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistusergroupmembersrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.marketingplatform.admin.v1alpha.IUserGroupMember](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iusergroupmember)[], [protos.google.marketingplatform.admin.v1alpha.IListUserGroupMembersRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistusergroupmembersrequest) | null, [protos.google.marketingplatform.admin.v1alpha.IListUserGroupMembersResponse](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistusergroupmembersresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listUserGroupMembersAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listUserGroupMembers(request, options, callback)
    
    
    listUserGroupMembers(request: protos.google.marketingplatform.admin.v1alpha.IListUserGroupMembersRequest, options: CallOptions, callback: PaginationCallback<protos.google.marketingplatform.admin.v1alpha.IListUserGroupMembersRequest, protos.google.marketingplatform.admin.v1alpha.IListUserGroupMembersResponse | null | undefined, protos.google.marketingplatform.admin.v1alpha.IUserGroupMember>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListUserGroupMembersRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistusergroupmembersrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.marketingplatform.admin.v1alpha.IListUserGroupMembersRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistusergroupmembersrequest), [protos.google.marketingplatform.admin.v1alpha.IListUserGroupMembersResponse](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistusergroupmembersresponse) | null | undefined, [protos.google.marketingplatform.admin.v1alpha.IUserGroupMember](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iusergroupmember)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listUserGroupMembers(request, callback)
    
    
    listUserGroupMembers(request: protos.google.marketingplatform.admin.v1alpha.IListUserGroupMembersRequest, callback: PaginationCallback<protos.google.marketingplatform.admin.v1alpha.IListUserGroupMembersRequest, protos.google.marketingplatform.admin.v1alpha.IListUserGroupMembersResponse | null | undefined, protos.google.marketingplatform.admin.v1alpha.IUserGroupMember>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListUserGroupMembersRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistusergroupmembersrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.marketingplatform.admin.v1alpha.IListUserGroupMembersRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistusergroupmembersrequest), [protos.google.marketingplatform.admin.v1alpha.IListUserGroupMembersResponse](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistusergroupmembersresponse) | null | undefined, [protos.google.marketingplatform.admin.v1alpha.IUserGroupMember](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iusergroupmember)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listUserGroupMembersAsync(request, options)
    
    
    listUserGroupMembersAsync(request?: protos.google.marketingplatform.admin.v1alpha.IListUserGroupMembersRequest, options?: CallOptions): AsyncIterable<protos.google.marketingplatform.admin.v1alpha.IUserGroupMember>;

Equivalent to `listUserGroupMembers`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListUserGroupMembersRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistusergroupmembersrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.marketingplatform.admin.v1alpha.IUserGroupMember](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iusergroupmember)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent user group where this UserGroupMember will be listed.
       *  Format: organizations/{org_id}/userGroups/{user_group_id}
       */
      // const parent = 'abc123'
      /**
       *  Optional. The maximum number of user group members to return in one call.
       *  The service may return fewer than this value.
       *  If unspecified, at most 50 user group members will be returned. The
       *  maximum value is 1000; values above 1000 will be coerced to 1000.
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous ListUserGroupMembers call.
       *  Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to
       *  `ListUserGroupMembers` must match the call that provided the page token.
       */
      // const pageToken = 'abc123'
    
      // Imports the Admin library
      const {MarketingplatformAdminServiceClient} = require('[@google-ads/marketing-platform-admin](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const adminClient = new [MarketingplatformAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/overview.html)();
    
      async function callListUserGroupMembers() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = adminClient.[listUserGroupMembersAsync](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/v1alpha.marketingplatformadminserviceclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListUserGroupMembers();
    
    

### listUserGroupMembersStream(request, options)
    
    
    listUserGroupMembersStream(request?: protos.google.marketingplatform.admin.v1alpha.IListUserGroupMembersRequest, options?: CallOptions): Transform;

Equivalent to `listUserGroupMembers`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListUserGroupMembersRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistusergroupmembersrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listUserGroupMembersAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listUserGroups(request, options)
    
    
    listUserGroups(request?: protos.google.marketingplatform.admin.v1alpha.IListUserGroupsRequest, options?: CallOptions): Promise<[
            protos.google.marketingplatform.admin.v1alpha.IUserGroup[],
            protos.google.marketingplatform.admin.v1alpha.IListUserGroupsRequest | null,
            protos.google.marketingplatform.admin.v1alpha.IListUserGroupsResponse
        ]>;

Returns a list of user groups in the specified GMP organization.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListUserGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistusergroupsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.marketingplatform.admin.v1alpha.IUserGroup](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iusergroup)[], [protos.google.marketingplatform.admin.v1alpha.IListUserGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistusergroupsrequest) | null, [protos.google.marketingplatform.admin.v1alpha.IListUserGroupsResponse](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistusergroupsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [UserGroup](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.usergroup). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listUserGroupsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listUserGroups(request, options, callback)
    
    
    listUserGroups(request: protos.google.marketingplatform.admin.v1alpha.IListUserGroupsRequest, options: CallOptions, callback: PaginationCallback<protos.google.marketingplatform.admin.v1alpha.IListUserGroupsRequest, protos.google.marketingplatform.admin.v1alpha.IListUserGroupsResponse | null | undefined, protos.google.marketingplatform.admin.v1alpha.IUserGroup>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListUserGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistusergroupsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.marketingplatform.admin.v1alpha.IListUserGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistusergroupsrequest), [protos.google.marketingplatform.admin.v1alpha.IListUserGroupsResponse](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistusergroupsresponse) | null | undefined, [protos.google.marketingplatform.admin.v1alpha.IUserGroup](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iusergroup)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listUserGroups(request, callback)
    
    
    listUserGroups(request: protos.google.marketingplatform.admin.v1alpha.IListUserGroupsRequest, callback: PaginationCallback<protos.google.marketingplatform.admin.v1alpha.IListUserGroupsRequest, protos.google.marketingplatform.admin.v1alpha.IListUserGroupsResponse | null | undefined, protos.google.marketingplatform.admin.v1alpha.IUserGroup>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListUserGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistusergroupsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.marketingplatform.admin.v1alpha.IListUserGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistusergroupsrequest), [protos.google.marketingplatform.admin.v1alpha.IListUserGroupsResponse](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistusergroupsresponse) | null | undefined, [protos.google.marketingplatform.admin.v1alpha.IUserGroup](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iusergroup)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listUserGroupsAsync(request, options)
    
    
    listUserGroupsAsync(request?: protos.google.marketingplatform.admin.v1alpha.IListUserGroupsRequest, options?: CallOptions): AsyncIterable<protos.google.marketingplatform.admin.v1alpha.IUserGroup>;

Equivalent to `listUserGroups`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListUserGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistusergroupsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.marketingplatform.admin.v1alpha.IUserGroup](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iusergroup)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [UserGroup](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.usergroup). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent org where this UserGroup will be listed.
       *  Format: organizations/{org_id}
       */
      // const parent = 'abc123'
      /**
       *  Optional. The maximum number of user groups to return in one call. The
       *  service may return fewer than this value.
       *  If unspecified, at most 50 user groups will be returned. The maximum value
       *  is 1000; values above 1000 will be coerced to 1000.
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous ListUserGroups call.
       *  Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to `ListUserGroups` must
       *  match the call that provided the page token.
       */
      // const pageToken = 'abc123'
    
      // Imports the Admin library
      const {MarketingplatformAdminServiceClient} = require('[@google-ads/marketing-platform-admin](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const adminClient = new [MarketingplatformAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/overview.html)();
    
      async function callListUserGroups() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = adminClient.[listUserGroupsAsync](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/v1alpha.marketingplatformadminserviceclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListUserGroups();
    
    

### listUserGroupsStream(request, options)
    
    
    listUserGroupsStream(request?: protos.google.marketingplatform.admin.v1alpha.IListUserGroupsRequest, options?: CallOptions): Transform;

Equivalent to `listUserGroups`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListUserGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ilistusergroupsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [UserGroup](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.usergroup) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listUserGroupsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### matchAdminAccessBindingFromAdminAccessBindingName(adminAccessBindingName)
    
    
    matchAdminAccessBindingFromAdminAccessBindingName(adminAccessBindingName: string): string | number;

Parse the admin_access_binding from AdminAccessBinding resource.

**Parameter**  
---  
**Name** | **Description**  
`adminAccessBindingName` |  `string`   
A fully-qualified path representing AdminAccessBinding resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the admin_access_binding.  
  
### matchAnalyticsAccountLinkFromAnalyticsAccountLinkName(analyticsAccountLinkName)
    
    
    matchAnalyticsAccountLinkFromAnalyticsAccountLinkName(analyticsAccountLinkName: string): string | number;

Parse the analytics_account_link from AnalyticsAccountLink resource.

**Parameter**  
---  
**Name** | **Description**  
`analyticsAccountLinkName` |  `string`   
A fully-qualified path representing AnalyticsAccountLink resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the analytics_account_link.  
  
### matchMemberFromUserGroupMemberName(userGroupMemberName)
    
    
    matchMemberFromUserGroupMemberName(userGroupMemberName: string): string | number;

Parse the member from UserGroupMember resource.

**Parameter**  
---  
**Name** | **Description**  
`userGroupMemberName` |  `string`   
A fully-qualified path representing UserGroupMember resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the member.  
  
### matchOrganizationFromAdminAccessBindingName(adminAccessBindingName)
    
    
    matchOrganizationFromAdminAccessBindingName(adminAccessBindingName: string): string | number;

Parse the organization from AdminAccessBinding resource.

**Parameter**  
---  
**Name** | **Description**  
`adminAccessBindingName` |  `string`   
A fully-qualified path representing AdminAccessBinding resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the organization.  
  
### matchOrganizationFromAnalyticsAccountLinkName(analyticsAccountLinkName)
    
    
    matchOrganizationFromAnalyticsAccountLinkName(analyticsAccountLinkName: string): string | number;

Parse the organization from AnalyticsAccountLink resource.

**Parameter**  
---  
**Name** | **Description**  
`analyticsAccountLinkName` |  `string`   
A fully-qualified path representing AnalyticsAccountLink resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the organization.  
  
### matchOrganizationFromOrganizationName(organizationName)
    
    
    matchOrganizationFromOrganizationName(organizationName: string): string | number;

Parse the organization from Organization resource.

**Parameter**  
---  
**Name** | **Description**  
`organizationName` |  `string`   
A fully-qualified path representing Organization resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the organization.  
  
### matchOrganizationFromUserGroupMemberName(userGroupMemberName)
    
    
    matchOrganizationFromUserGroupMemberName(userGroupMemberName: string): string | number;

Parse the organization from UserGroupMember resource.

**Parameter**  
---  
**Name** | **Description**  
`userGroupMemberName` |  `string`   
A fully-qualified path representing UserGroupMember resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the organization.  
  
### matchOrganizationFromUserGroupName(userGroupName)
    
    
    matchOrganizationFromUserGroupName(userGroupName: string): string | number;

Parse the organization from UserGroup resource.

**Parameter**  
---  
**Name** | **Description**  
`userGroupName` |  `string`   
A fully-qualified path representing UserGroup resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the organization.  
  
### matchPropertyFromPropertyName(propertyName)
    
    
    matchPropertyFromPropertyName(propertyName: string): string | number;

Parse the property from Property resource.

**Parameter**  
---  
**Name** | **Description**  
`propertyName` |  `string`   
A fully-qualified path representing Property resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the property.  
  
### matchUserGroupFromUserGroupMemberName(userGroupMemberName)
    
    
    matchUserGroupFromUserGroupMemberName(userGroupMemberName: string): string | number;

Parse the user_group from UserGroupMember resource.

**Parameter**  
---  
**Name** | **Description**  
`userGroupMemberName` |  `string`   
A fully-qualified path representing UserGroupMember resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the user_group.  
  
### matchUserGroupFromUserGroupName(userGroupName)
    
    
    matchUserGroupFromUserGroupName(userGroupName: string): string | number;

Parse the user_group from UserGroup resource.

**Parameter**  
---  
**Name** | **Description**  
`userGroupName` |  `string`   
A fully-qualified path representing UserGroup resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the user_group.  
  
### organizationPath(organization)
    
    
    organizationPath(organization: string): string;

Return a fully-qualified organization resource name string.

**Parameter**  
---  
**Name** | **Description**  
`organization` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### propertyPath(property)
    
    
    propertyPath(property: string): string;

Return a fully-qualified property resource name string.

**Parameter**  
---  
**Name** | **Description**  
`property` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### reportPropertyUsage(request, options)
    
    
    reportPropertyUsage(request?: protos.google.marketingplatform.admin.v1alpha.IReportPropertyUsageRequest, options?: CallOptions): Promise<[
            protos.google.marketingplatform.admin.v1alpha.IReportPropertyUsageResponse,
            (protos.google.marketingplatform.admin.v1alpha.IReportPropertyUsageRequest | undefined),
            {} | undefined
        ]>;

Gets the usage and billing data for properties within the organization for the specified month.

Per direct client org, user needs to be OrgAdmin/BillingAdmin on the organization in order to view the billing and usage data.

Per sales partner client org, user needs to be OrgAdmin/BillingAdmin on the sales partner org in order to view the billing and usage data, or OrgAdmin/BillingAdmin on the sales partner client org in order to view the usage data only.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IReportPropertyUsageRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ireportpropertyusagerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.marketingplatform.admin.v1alpha.IReportPropertyUsageResponse](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ireportpropertyusageresponse), ([protos.google.marketingplatform.admin.v1alpha.IReportPropertyUsageRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ireportpropertyusagerequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Specifies the organization whose property usage will be listed.
       *  Format: organizations/{org_id}
       */
      // const organization = 'abc123'
      /**
       *  Required. The target month to list property usages.
       *  Format: YYYY-MM. For example, "2025-05"
       */
      // const month = 'abc123'
    
      // Imports the Admin library
      const {MarketingplatformAdminServiceClient} = require('[@google-ads/marketing-platform-admin](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const adminClient = new [MarketingplatformAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/overview.html)();
    
      async function callReportPropertyUsage() {
        // Construct request
        const request = {
          organization,
          month,
        };
    
        // Run request
        const response = await adminClient.reportPropertyUsage(request);
        console.log(response);
      }
    
      callReportPropertyUsage();
    
    

### reportPropertyUsage(request, options, callback)
    
    
    reportPropertyUsage(request: protos.google.marketingplatform.admin.v1alpha.IReportPropertyUsageRequest, options: CallOptions, callback: Callback<protos.google.marketingplatform.admin.v1alpha.IReportPropertyUsageResponse, protos.google.marketingplatform.admin.v1alpha.IReportPropertyUsageRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IReportPropertyUsageRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ireportpropertyusagerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.marketingplatform.admin.v1alpha.IReportPropertyUsageResponse](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ireportpropertyusageresponse), [protos.google.marketingplatform.admin.v1alpha.IReportPropertyUsageRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ireportpropertyusagerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### reportPropertyUsage(request, callback)
    
    
    reportPropertyUsage(request: protos.google.marketingplatform.admin.v1alpha.IReportPropertyUsageRequest, callback: Callback<protos.google.marketingplatform.admin.v1alpha.IReportPropertyUsageResponse, protos.google.marketingplatform.admin.v1alpha.IReportPropertyUsageRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IReportPropertyUsageRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ireportpropertyusagerequest)`   
  
`callback` |  `Callback<[protos.google.marketingplatform.admin.v1alpha.IReportPropertyUsageResponse](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ireportpropertyusageresponse), [protos.google.marketingplatform.admin.v1alpha.IReportPropertyUsageRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.ireportpropertyusagerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setPropertyServiceLevel(request, options)
    
    
    setPropertyServiceLevel(request?: protos.google.marketingplatform.admin.v1alpha.ISetPropertyServiceLevelRequest, options?: CallOptions): Promise<[
            protos.google.marketingplatform.admin.v1alpha.ISetPropertyServiceLevelResponse,
            (protos.google.marketingplatform.admin.v1alpha.ISetPropertyServiceLevelRequest | undefined),
            {} | undefined
        ]>;

Updates the service level for an Analytics property.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetPropertyServiceLevelRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.isetpropertyservicelevelrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.marketingplatform.admin.v1alpha.ISetPropertyServiceLevelResponse](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.isetpropertyservicelevelresponse), ([protos.google.marketingplatform.admin.v1alpha.ISetPropertyServiceLevelRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.isetpropertyservicelevelrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [SetPropertyServiceLevelResponse](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.setpropertyservicelevelresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent AnalyticsAccountLink scope where this property is in.
       *  Format:
       *  organizations/{org_id}/analyticsAccountLinks/{analytics_account_link_id}
       */
      // const analyticsAccountLink = 'abc123'
      /**
       *  Required. The Analytics property to change the ServiceLevel setting. This
       *  field is the name of the Google Analytics Admin API property resource.
       *  Format: analyticsadmin.googleapis.com/properties/{property_id}
       */
      // const analyticsProperty = 'abc123'
      /**
       *  Required. The service level to set for this property.
       */
      // const serviceLevel = {}
    
      // Imports the Admin library
      const {MarketingplatformAdminServiceClient} = require('[@google-ads/marketing-platform-admin](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const adminClient = new [MarketingplatformAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/overview.html)();
    
      async function callSetPropertyServiceLevel() {
        // Construct request
        const request = {
          analyticsAccountLink,
          analyticsProperty,
          serviceLevel,
        };
    
        // Run request
        const response = await adminClient.setPropertyServiceLevel(request);
        console.log(response);
      }
    
      callSetPropertyServiceLevel();
    
    

### setPropertyServiceLevel(request, options, callback)
    
    
    setPropertyServiceLevel(request: protos.google.marketingplatform.admin.v1alpha.ISetPropertyServiceLevelRequest, options: CallOptions, callback: Callback<protos.google.marketingplatform.admin.v1alpha.ISetPropertyServiceLevelResponse, protos.google.marketingplatform.admin.v1alpha.ISetPropertyServiceLevelRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetPropertyServiceLevelRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.isetpropertyservicelevelrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.marketingplatform.admin.v1alpha.ISetPropertyServiceLevelResponse](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.isetpropertyservicelevelresponse), [protos.google.marketingplatform.admin.v1alpha.ISetPropertyServiceLevelRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.isetpropertyservicelevelrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setPropertyServiceLevel(request, callback)
    
    
    setPropertyServiceLevel(request: protos.google.marketingplatform.admin.v1alpha.ISetPropertyServiceLevelRequest, callback: Callback<protos.google.marketingplatform.admin.v1alpha.ISetPropertyServiceLevelResponse, protos.google.marketingplatform.admin.v1alpha.ISetPropertyServiceLevelRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetPropertyServiceLevelRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.isetpropertyservicelevelrequest)`   
  
`callback` |  `Callback<[protos.google.marketingplatform.admin.v1alpha.ISetPropertyServiceLevelResponse](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.isetpropertyservicelevelresponse), [protos.google.marketingplatform.admin.v1alpha.ISetPropertyServiceLevelRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.isetpropertyservicelevelrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateAdminAccessBinding(request, options)
    
    
    updateAdminAccessBinding(request?: protos.google.marketingplatform.admin.v1alpha.IUpdateAdminAccessBindingRequest, options?: CallOptions): Promise<[
            protos.google.marketingplatform.admin.v1alpha.IAdminAccessBinding,
            (protos.google.marketingplatform.admin.v1alpha.IUpdateAdminAccessBindingRequest | undefined),
            {} | undefined
        ]>;

Updates an admin access binding in the specified GMP organization.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAdminAccessBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iupdateadminaccessbindingrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.marketingplatform.admin.v1alpha.IAdminAccessBinding](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iadminaccessbinding), ([protos.google.marketingplatform.admin.v1alpha.IUpdateAdminAccessBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iupdateadminaccessbindingrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [AdminAccessBinding](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.adminaccessbinding). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The AdminAccessBinding to update.
       */
      // const adminAccessBinding = {}
      /**
       *  Required. The list of fields to update. Field names must be in snake case
       *  (for example, "field_to_update"). Omitted fields will not be updated. To
       *  replace the entire entity, use one path with the string "*" to match all
       *  fields.
       */
      // const updateMask = {}
    
      // Imports the Admin library
      const {MarketingplatformAdminServiceClient} = require('[@google-ads/marketing-platform-admin](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const adminClient = new [MarketingplatformAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/overview.html)();
    
      async function callUpdateAdminAccessBinding() {
        // Construct request
        const request = {
          adminAccessBinding,
          updateMask,
        };
    
        // Run request
        const response = await adminClient.updateAdminAccessBinding(request);
        console.log(response);
      }
    
      callUpdateAdminAccessBinding();
    
    

### updateAdminAccessBinding(request, options, callback)
    
    
    updateAdminAccessBinding(request: protos.google.marketingplatform.admin.v1alpha.IUpdateAdminAccessBindingRequest, options: CallOptions, callback: Callback<protos.google.marketingplatform.admin.v1alpha.IAdminAccessBinding, protos.google.marketingplatform.admin.v1alpha.IUpdateAdminAccessBindingRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAdminAccessBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iupdateadminaccessbindingrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.marketingplatform.admin.v1alpha.IAdminAccessBinding](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iadminaccessbinding), [protos.google.marketingplatform.admin.v1alpha.IUpdateAdminAccessBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iupdateadminaccessbindingrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateAdminAccessBinding(request, callback)
    
    
    updateAdminAccessBinding(request: protos.google.marketingplatform.admin.v1alpha.IUpdateAdminAccessBindingRequest, callback: Callback<protos.google.marketingplatform.admin.v1alpha.IAdminAccessBinding, protos.google.marketingplatform.admin.v1alpha.IUpdateAdminAccessBindingRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAdminAccessBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iupdateadminaccessbindingrequest)`   
  
`callback` |  `Callback<[protos.google.marketingplatform.admin.v1alpha.IAdminAccessBinding](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iadminaccessbinding), [protos.google.marketingplatform.admin.v1alpha.IUpdateAdminAccessBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iupdateadminaccessbindingrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateUserGroup(request, options)
    
    
    updateUserGroup(request?: protos.google.marketingplatform.admin.v1alpha.IUpdateUserGroupRequest, options?: CallOptions): Promise<[
            protos.google.marketingplatform.admin.v1alpha.IUserGroup,
            (protos.google.marketingplatform.admin.v1alpha.IUpdateUserGroupRequest | undefined),
            {} | undefined
        ]>;

Updates a user group in the specified GMP organization.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateUserGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iupdateusergrouprequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.marketingplatform.admin.v1alpha.IUserGroup](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iusergroup), ([protos.google.marketingplatform.admin.v1alpha.IUpdateUserGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iupdateusergrouprequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [UserGroup](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.usergroup). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The user group to update.
       */
      // const userGroup = {}
      /**
       *  Required. The list of fields to update. Field names must be in snake case
       *  (for example, "field_to_update"). Omitted fields will not be updated. To
       *  replace the entire entity, use one path with the string "*" to match all
       *  fields.
       */
      // const updateMask = {}
    
      // Imports the Admin library
      const {MarketingplatformAdminServiceClient} = require('[@google-ads/marketing-platform-admin](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const adminClient = new [MarketingplatformAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/overview.html)();
    
      async function callUpdateUserGroup() {
        // Construct request
        const request = {
          userGroup,
          updateMask,
        };
    
        // Run request
        const response = await adminClient.updateUserGroup(request);
        console.log(response);
      }
    
      callUpdateUserGroup();
    
    

### updateUserGroup(request, options, callback)
    
    
    updateUserGroup(request: protos.google.marketingplatform.admin.v1alpha.IUpdateUserGroupRequest, options: CallOptions, callback: Callback<protos.google.marketingplatform.admin.v1alpha.IUserGroup, protos.google.marketingplatform.admin.v1alpha.IUpdateUserGroupRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateUserGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iupdateusergrouprequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.marketingplatform.admin.v1alpha.IUserGroup](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iusergroup), [protos.google.marketingplatform.admin.v1alpha.IUpdateUserGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iupdateusergrouprequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateUserGroup(request, callback)
    
    
    updateUserGroup(request: protos.google.marketingplatform.admin.v1alpha.IUpdateUserGroupRequest, callback: Callback<protos.google.marketingplatform.admin.v1alpha.IUserGroup, protos.google.marketingplatform.admin.v1alpha.IUpdateUserGroupRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateUserGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iupdateusergrouprequest)`   
  
`callback` |  `Callback<[protos.google.marketingplatform.admin.v1alpha.IUserGroup](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iusergroup), [protos.google.marketingplatform.admin.v1alpha.IUpdateUserGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iupdateusergrouprequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateUserGroupMember(request, options)
    
    
    updateUserGroupMember(request?: protos.google.marketingplatform.admin.v1alpha.IUpdateUserGroupMemberRequest, options?: CallOptions): Promise<[
            protos.google.marketingplatform.admin.v1alpha.IUserGroupMember,
            (protos.google.marketingplatform.admin.v1alpha.IUpdateUserGroupMemberRequest | undefined),
            {} | undefined
        ]>;

Updates a member in the specified GMP user group.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateUserGroupMemberRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iupdateusergroupmemberrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.marketingplatform.admin.v1alpha.IUserGroupMember](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iusergroupmember), ([protos.google.marketingplatform.admin.v1alpha.IUpdateUserGroupMemberRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iupdateusergroupmemberrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The user group member to update.
       */
      // const userGroupMember = {}
      /**
       *  Required. The list of fields to update. Field names must be in snake case
       *  (for example, "field_to_update"). Omitted fields will not be updated. To
       *  replace the entire entity, use one path with the string "*" to match all
       *  fields.
       */
      // const updateMask = {}
    
      // Imports the Admin library
      const {MarketingplatformAdminServiceClient} = require('[@google-ads/marketing-platform-admin](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const adminClient = new [MarketingplatformAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/overview.html)();
    
      async function callUpdateUserGroupMember() {
        // Construct request
        const request = {
          userGroupMember,
          updateMask,
        };
    
        // Run request
        const response = await adminClient.updateUserGroupMember(request);
        console.log(response);
      }
    
      callUpdateUserGroupMember();
    
    

### updateUserGroupMember(request, options, callback)
    
    
    updateUserGroupMember(request: protos.google.marketingplatform.admin.v1alpha.IUpdateUserGroupMemberRequest, options: CallOptions, callback: Callback<protos.google.marketingplatform.admin.v1alpha.IUserGroupMember, protos.google.marketingplatform.admin.v1alpha.IUpdateUserGroupMemberRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateUserGroupMemberRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iupdateusergroupmemberrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.marketingplatform.admin.v1alpha.IUserGroupMember](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iusergroupmember), [protos.google.marketingplatform.admin.v1alpha.IUpdateUserGroupMemberRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iupdateusergroupmemberrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateUserGroupMember(request, callback)
    
    
    updateUserGroupMember(request: protos.google.marketingplatform.admin.v1alpha.IUpdateUserGroupMemberRequest, callback: Callback<protos.google.marketingplatform.admin.v1alpha.IUserGroupMember, protos.google.marketingplatform.admin.v1alpha.IUpdateUserGroupMemberRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateUserGroupMemberRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iupdateusergroupmemberrequest)`   
  
`callback` |  `Callback<[protos.google.marketingplatform.admin.v1alpha.IUserGroupMember](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iusergroupmember), [protos.google.marketingplatform.admin.v1alpha.IUpdateUserGroupMemberRequest](https://docs.cloud.google.com/nodejs/docs/reference/marketing-platform-admin/latest/marketing-platform-admin/protos.google.marketingplatform.admin.v1alpha.iupdateusergroupmemberrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### userGroupMemberPath(organization, userGroup, member)
    
    
    userGroupMemberPath(organization: string, userGroup: string, member: string): string;

Return a fully-qualified userGroupMember resource name string.

**Parameters**  
---  
**Name** | **Description**  
`organization` |  `string`   
  
`userGroup` |  `string`   
  
`member` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### userGroupPath(organization, userGroup)
    
    
    userGroupPath(organization: string, userGroup: string): string;

Return a fully-qualified userGroup resource name string.

**Parameters**  
---  
**Name** | **Description**  
`organization` |  `string`   
  
`userGroup` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
