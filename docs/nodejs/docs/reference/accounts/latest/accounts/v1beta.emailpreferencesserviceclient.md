---
url: https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/v1beta.emailpreferencesserviceclient
title: Class v1beta.EmailPreferencesServiceClient (4.0.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:24:57.135473+00:00
---

# Class v1beta.EmailPreferencesServiceClient (4.0.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/v1beta.emailpreferencesserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta.EmailPreferencesServiceClient (4.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.1 (latest)  3.2.0  2.2.0  1.0.0 

Service to support the `EmailPreferences` API.

This service only permits retrieving and updating email preferences for the authenticated user. v1beta

## Package

[@google-shopping/accounts](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of EmailPreferencesServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new EmailPreferencesServiceClient({fallback: true}, gax); ```  
  
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

### emailPreferencesServiceStub
    
    
    emailPreferencesServiceStub?: Promise<{
            [name: string]: Function;
        }>;

### innerApiCalls
    
    
    innerApiCalls: {
            [name: string]: Function;
        };

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

### accountIssuePath(account, issue)
    
    
    accountIssuePath(account: string, issue: string): string;

Return a fully-qualified accountIssue resource name string.

**Parameters**  
---  
**Name** | **Description**  
`account` |  `string`   
  
`issue` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### accountPath(account)
    
    
    accountPath(account: string): string;

Return a fully-qualified account resource name string.

**Parameter**  
---  
**Name** | **Description**  
`account` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### accountTaxPath(account, tax)
    
    
    accountTaxPath(account: string, tax: string): string;

Return a fully-qualified accountTax resource name string.

**Parameters**  
---  
**Name** | **Description**  
`account` |  `string`   
  
`tax` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### autofeedSettingsPath(account)
    
    
    autofeedSettingsPath(account: string): string;

Return a fully-qualified autofeedSettings resource name string.

**Parameter**  
---  
**Name** | **Description**  
`account` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### automaticImprovementsPath(account)
    
    
    automaticImprovementsPath(account: string): string;

Return a fully-qualified automaticImprovements resource name string.

**Parameter**  
---  
**Name** | **Description**  
`account` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### businessIdentityPath(account)
    
    
    businessIdentityPath(account: string): string;

Return a fully-qualified businessIdentity resource name string.

**Parameter**  
---  
**Name** | **Description**  
`account` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### businessInfoPath(account)
    
    
    businessInfoPath(account: string): string;

Return a fully-qualified businessInfo resource name string.

**Parameter**  
---  
**Name** | **Description**  
`account` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### checkoutSettingsPath(account, program)
    
    
    checkoutSettingsPath(account: string, program: string): string;

Return a fully-qualified checkoutSettings resource name string.

**Parameters**  
---  
**Name** | **Description**  
`account` |  `string`   
  
`program` |  `string`   
  
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
  
### emailPreferencesPath(account, email)
    
    
    emailPreferencesPath(account: string, email: string): string;

Return a fully-qualified emailPreferences resource name string.

**Parameters**  
---  
**Name** | **Description**  
`account` |  `string`   
  
`email` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### gbpAccountPath(account, gbpAccount)
    
    
    gbpAccountPath(account: string, gbpAccount: string): string;

Return a fully-qualified gbpAccount resource name string.

**Parameters**  
---  
**Name** | **Description**  
`account` |  `string`   
  
`gbpAccount` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### getEmailPreferences(request, options)
    
    
    getEmailPreferences(request?: protos.google.shopping.merchant.accounts.v1beta.IGetEmailPreferencesRequest, options?: CallOptions): Promise<[
            protos.google.shopping.merchant.accounts.v1beta.IEmailPreferences,
            (protos.google.shopping.merchant.accounts.v1beta.IGetEmailPreferencesRequest | undefined),
            {} | undefined
        ]>;

Returns the email preferences for a Merchant Center account user.

Use the name=accounts/* /users/me/emailPreferences alias to get preferences for the authenticated user.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEmailPreferencesRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.igetemailpreferencesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.shopping.merchant.accounts.v1beta.IEmailPreferences](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.iemailpreferences), ([protos.google.shopping.merchant.accounts.v1beta.IGetEmailPreferencesRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.igetemailpreferencesrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the `EmailPreferences` resource.
       *  Format: `accounts/{account}/users/{email}/emailPreferences`
       */
      // const name = 'abc123'
    
      // Imports the Accounts library
      const {EmailPreferencesServiceClient} = require('[@google-shopping/accounts](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const accountsClient = new [EmailPreferencesServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/overview.html)();
    
      async function callGetEmailPreferences() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await accountsClient.getEmailPreferences(request);
        console.log(response);
      }
    
      callGetEmailPreferences();
    
    

### getEmailPreferences(request, options, callback)
    
    
    getEmailPreferences(request: protos.google.shopping.merchant.accounts.v1beta.IGetEmailPreferencesRequest, options: CallOptions, callback: Callback<protos.google.shopping.merchant.accounts.v1beta.IEmailPreferences, protos.google.shopping.merchant.accounts.v1beta.IGetEmailPreferencesRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEmailPreferencesRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.igetemailpreferencesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.shopping.merchant.accounts.v1beta.IEmailPreferences](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.iemailpreferences), [protos.google.shopping.merchant.accounts.v1beta.IGetEmailPreferencesRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.igetemailpreferencesrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getEmailPreferences(request, callback)
    
    
    getEmailPreferences(request: protos.google.shopping.merchant.accounts.v1beta.IGetEmailPreferencesRequest, callback: Callback<protos.google.shopping.merchant.accounts.v1beta.IEmailPreferences, protos.google.shopping.merchant.accounts.v1beta.IGetEmailPreferencesRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEmailPreferencesRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.igetemailpreferencesrequest)`   
  
`callback` |  `Callback<[protos.google.shopping.merchant.accounts.v1beta.IEmailPreferences](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.iemailpreferences), [protos.google.shopping.merchant.accounts.v1beta.IGetEmailPreferencesRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.igetemailpreferencesrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### homepagePath(account)
    
    
    homepagePath(account: string): string;

Return a fully-qualified homepage resource name string.

**Parameter**  
---  
**Name** | **Description**  
`account` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
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
  
### lfpProviderPath(account, omnichannelSetting, lfpProvider)
    
    
    lfpProviderPath(account: string, omnichannelSetting: string, lfpProvider: string): string;

Return a fully-qualified lfpProvider resource name string.

**Parameters**  
---  
**Name** | **Description**  
`account` |  `string`   
  
`omnichannelSetting` |  `string`   
  
`lfpProvider` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### matchAccountFromAccountIssueName(accountIssueName)
    
    
    matchAccountFromAccountIssueName(accountIssueName: string): string | number;

Parse the account from AccountIssue resource.

**Parameter**  
---  
**Name** | **Description**  
`accountIssueName` |  `string`   
A fully-qualified path representing AccountIssue resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the account.  
  
### matchAccountFromAccountName(accountName)
    
    
    matchAccountFromAccountName(accountName: string): string | number;

Parse the account from Account resource.

**Parameter**  
---  
**Name** | **Description**  
`accountName` |  `string`   
A fully-qualified path representing Account resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the account.  
  
### matchAccountFromAccountTaxName(accountTaxName)
    
    
    matchAccountFromAccountTaxName(accountTaxName: string): string | number;

Parse the account from AccountTax resource.

**Parameter**  
---  
**Name** | **Description**  
`accountTaxName` |  `string`   
A fully-qualified path representing AccountTax resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the account.  
  
### matchAccountFromAutofeedSettingsName(autofeedSettingsName)
    
    
    matchAccountFromAutofeedSettingsName(autofeedSettingsName: string): string | number;

Parse the account from AutofeedSettings resource.

**Parameter**  
---  
**Name** | **Description**  
`autofeedSettingsName` |  `string`   
A fully-qualified path representing AutofeedSettings resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the account.  
  
### matchAccountFromAutomaticImprovementsName(automaticImprovementsName)
    
    
    matchAccountFromAutomaticImprovementsName(automaticImprovementsName: string): string | number;

Parse the account from AutomaticImprovements resource.

**Parameter**  
---  
**Name** | **Description**  
`automaticImprovementsName` |  `string`   
A fully-qualified path representing AutomaticImprovements resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the account.  
  
### matchAccountFromBusinessIdentityName(businessIdentityName)
    
    
    matchAccountFromBusinessIdentityName(businessIdentityName: string): string | number;

Parse the account from BusinessIdentity resource.

**Parameter**  
---  
**Name** | **Description**  
`businessIdentityName` |  `string`   
A fully-qualified path representing BusinessIdentity resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the account.  
  
### matchAccountFromBusinessInfoName(businessInfoName)
    
    
    matchAccountFromBusinessInfoName(businessInfoName: string): string | number;

Parse the account from BusinessInfo resource.

**Parameter**  
---  
**Name** | **Description**  
`businessInfoName` |  `string`   
A fully-qualified path representing BusinessInfo resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the account.  
  
### matchAccountFromCheckoutSettingsName(checkoutSettingsName)
    
    
    matchAccountFromCheckoutSettingsName(checkoutSettingsName: string): string | number;

Parse the account from CheckoutSettings resource.

**Parameter**  
---  
**Name** | **Description**  
`checkoutSettingsName` |  `string`   
A fully-qualified path representing CheckoutSettings resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the account.  
  
### matchAccountFromEmailPreferencesName(emailPreferencesName)
    
    
    matchAccountFromEmailPreferencesName(emailPreferencesName: string): string | number;

Parse the account from EmailPreferences resource.

**Parameter**  
---  
**Name** | **Description**  
`emailPreferencesName` |  `string`   
A fully-qualified path representing EmailPreferences resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the account.  
  
### matchAccountFromGbpAccountName(gbpAccountName)
    
    
    matchAccountFromGbpAccountName(gbpAccountName: string): string | number;

Parse the account from GbpAccount resource.

**Parameter**  
---  
**Name** | **Description**  
`gbpAccountName` |  `string`   
A fully-qualified path representing GbpAccount resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the account.  
  
### matchAccountFromHomepageName(homepageName)
    
    
    matchAccountFromHomepageName(homepageName: string): string | number;

Parse the account from Homepage resource.

**Parameter**  
---  
**Name** | **Description**  
`homepageName` |  `string`   
A fully-qualified path representing Homepage resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the account.  
  
### matchAccountFromLfpProviderName(lfpProviderName)
    
    
    matchAccountFromLfpProviderName(lfpProviderName: string): string | number;

Parse the account from LfpProvider resource.

**Parameter**  
---  
**Name** | **Description**  
`lfpProviderName` |  `string`   
A fully-qualified path representing LfpProvider resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the account.  
  
### matchAccountFromOmnichannelSettingName(omnichannelSettingName)
    
    
    matchAccountFromOmnichannelSettingName(omnichannelSettingName: string): string | number;

Parse the account from OmnichannelSetting resource.

**Parameter**  
---  
**Name** | **Description**  
`omnichannelSettingName` |  `string`   
A fully-qualified path representing OmnichannelSetting resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the account.  
  
### matchAccountFromOnlineReturnPolicyName(onlineReturnPolicyName)
    
    
    matchAccountFromOnlineReturnPolicyName(onlineReturnPolicyName: string): string | number;

Parse the account from OnlineReturnPolicy resource.

**Parameter**  
---  
**Name** | **Description**  
`onlineReturnPolicyName` |  `string`   
A fully-qualified path representing OnlineReturnPolicy resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the account.  
  
### matchAccountFromProgramName(programName)
    
    
    matchAccountFromProgramName(programName: string): string | number;

Parse the account from Program resource.

**Parameter**  
---  
**Name** | **Description**  
`programName` |  `string`   
A fully-qualified path representing Program resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the account.  
  
### matchAccountFromRegionName(regionName)
    
    
    matchAccountFromRegionName(regionName: string): string | number;

Parse the account from Region resource.

**Parameter**  
---  
**Name** | **Description**  
`regionName` |  `string`   
A fully-qualified path representing Region resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the account.  
  
### matchAccountFromShippingSettingsName(shippingSettingsName)
    
    
    matchAccountFromShippingSettingsName(shippingSettingsName: string): string | number;

Parse the account from ShippingSettings resource.

**Parameter**  
---  
**Name** | **Description**  
`shippingSettingsName` |  `string`   
A fully-qualified path representing ShippingSettings resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the account.  
  
### matchAccountFromTermsOfServiceAgreementStateName(termsOfServiceAgreementStateName)
    
    
    matchAccountFromTermsOfServiceAgreementStateName(termsOfServiceAgreementStateName: string): string | number;

Parse the account from TermsOfServiceAgreementState resource.

**Parameter**  
---  
**Name** | **Description**  
`termsOfServiceAgreementStateName` |  `string`   
A fully-qualified path representing TermsOfServiceAgreementState resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the account.  
  
### matchAccountFromUserName(userName)
    
    
    matchAccountFromUserName(userName: string): string | number;

Parse the account from User resource.

**Parameter**  
---  
**Name** | **Description**  
`userName` |  `string`   
A fully-qualified path representing User resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the account.  
  
### matchEmailFromEmailPreferencesName(emailPreferencesName)
    
    
    matchEmailFromEmailPreferencesName(emailPreferencesName: string): string | number;

Parse the email from EmailPreferences resource.

**Parameter**  
---  
**Name** | **Description**  
`emailPreferencesName` |  `string`   
A fully-qualified path representing EmailPreferences resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the email.  
  
### matchEmailFromUserName(userName)
    
    
    matchEmailFromUserName(userName: string): string | number;

Parse the email from User resource.

**Parameter**  
---  
**Name** | **Description**  
`userName` |  `string`   
A fully-qualified path representing User resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the email.  
  
### matchGbpAccountFromGbpAccountName(gbpAccountName)
    
    
    matchGbpAccountFromGbpAccountName(gbpAccountName: string): string | number;

Parse the gbp_account from GbpAccount resource.

**Parameter**  
---  
**Name** | **Description**  
`gbpAccountName` |  `string`   
A fully-qualified path representing GbpAccount resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the gbp_account.  
  
### matchIdentifierFromTermsOfServiceAgreementStateName(termsOfServiceAgreementStateName)
    
    
    matchIdentifierFromTermsOfServiceAgreementStateName(termsOfServiceAgreementStateName: string): string | number;

Parse the identifier from TermsOfServiceAgreementState resource.

**Parameter**  
---  
**Name** | **Description**  
`termsOfServiceAgreementStateName` |  `string`   
A fully-qualified path representing TermsOfServiceAgreementState resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the identifier.  
  
### matchIssueFromAccountIssueName(accountIssueName)
    
    
    matchIssueFromAccountIssueName(accountIssueName: string): string | number;

Parse the issue from AccountIssue resource.

**Parameter**  
---  
**Name** | **Description**  
`accountIssueName` |  `string`   
A fully-qualified path representing AccountIssue resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the issue.  
  
### matchLfpProviderFromLfpProviderName(lfpProviderName)
    
    
    matchLfpProviderFromLfpProviderName(lfpProviderName: string): string | number;

Parse the lfp_provider from LfpProvider resource.

**Parameter**  
---  
**Name** | **Description**  
`lfpProviderName` |  `string`   
A fully-qualified path representing LfpProvider resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the lfp_provider.  
  
### matchOmnichannelSettingFromLfpProviderName(lfpProviderName)
    
    
    matchOmnichannelSettingFromLfpProviderName(lfpProviderName: string): string | number;

Parse the omnichannel_setting from LfpProvider resource.

**Parameter**  
---  
**Name** | **Description**  
`lfpProviderName` |  `string`   
A fully-qualified path representing LfpProvider resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the omnichannel_setting.  
  
### matchOmnichannelSettingFromOmnichannelSettingName(omnichannelSettingName)
    
    
    matchOmnichannelSettingFromOmnichannelSettingName(omnichannelSettingName: string): string | number;

Parse the omnichannel_setting from OmnichannelSetting resource.

**Parameter**  
---  
**Name** | **Description**  
`omnichannelSettingName` |  `string`   
A fully-qualified path representing OmnichannelSetting resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the omnichannel_setting.  
  
### matchProgramFromCheckoutSettingsName(checkoutSettingsName)
    
    
    matchProgramFromCheckoutSettingsName(checkoutSettingsName: string): string | number;

Parse the program from CheckoutSettings resource.

**Parameter**  
---  
**Name** | **Description**  
`checkoutSettingsName` |  `string`   
A fully-qualified path representing CheckoutSettings resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the program.  
  
### matchProgramFromProgramName(programName)
    
    
    matchProgramFromProgramName(programName: string): string | number;

Parse the program from Program resource.

**Parameter**  
---  
**Name** | **Description**  
`programName` |  `string`   
A fully-qualified path representing Program resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the program.  
  
### matchRegionFromRegionName(regionName)
    
    
    matchRegionFromRegionName(regionName: string): string | number;

Parse the region from Region resource.

**Parameter**  
---  
**Name** | **Description**  
`regionName` |  `string`   
A fully-qualified path representing Region resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the region.  
  
### matchReturnPolicyFromOnlineReturnPolicyName(onlineReturnPolicyName)
    
    
    matchReturnPolicyFromOnlineReturnPolicyName(onlineReturnPolicyName: string): string | number;

Parse the return_policy from OnlineReturnPolicy resource.

**Parameter**  
---  
**Name** | **Description**  
`onlineReturnPolicyName` |  `string`   
A fully-qualified path representing OnlineReturnPolicy resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the return_policy.  
  
### matchTaxFromAccountTaxName(accountTaxName)
    
    
    matchTaxFromAccountTaxName(accountTaxName: string): string | number;

Parse the tax from AccountTax resource.

**Parameter**  
---  
**Name** | **Description**  
`accountTaxName` |  `string`   
A fully-qualified path representing AccountTax resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the tax.  
  
### matchVersionFromTermsOfServiceName(termsOfServiceName)
    
    
    matchVersionFromTermsOfServiceName(termsOfServiceName: string): string | number;

Parse the version from TermsOfService resource.

**Parameter**  
---  
**Name** | **Description**  
`termsOfServiceName` |  `string`   
A fully-qualified path representing TermsOfService resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the version.  
  
### omnichannelSettingPath(account, omnichannelSetting)
    
    
    omnichannelSettingPath(account: string, omnichannelSetting: string): string;

Return a fully-qualified omnichannelSetting resource name string.

**Parameters**  
---  
**Name** | **Description**  
`account` |  `string`   
  
`omnichannelSetting` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### onlineReturnPolicyPath(account, returnPolicy)
    
    
    onlineReturnPolicyPath(account: string, returnPolicy: string): string;

Return a fully-qualified onlineReturnPolicy resource name string.

**Parameters**  
---  
**Name** | **Description**  
`account` |  `string`   
  
`returnPolicy` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### programPath(account, program)
    
    
    programPath(account: string, program: string): string;

Return a fully-qualified program resource name string.

**Parameters**  
---  
**Name** | **Description**  
`account` |  `string`   
  
`program` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### regionPath(account, region)
    
    
    regionPath(account: string, region: string): string;

Return a fully-qualified region resource name string.

**Parameters**  
---  
**Name** | **Description**  
`account` |  `string`   
  
`region` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### shippingSettingsPath(account)
    
    
    shippingSettingsPath(account: string): string;

Return a fully-qualified shippingSettings resource name string.

**Parameter**  
---  
**Name** | **Description**  
`account` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### termsOfServiceAgreementStatePath(account, identifier)
    
    
    termsOfServiceAgreementStatePath(account: string, identifier: string): string;

Return a fully-qualified termsOfServiceAgreementState resource name string.

**Parameters**  
---  
**Name** | **Description**  
`account` |  `string`   
  
`identifier` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### termsOfServicePath(version)
    
    
    termsOfServicePath(version: string): string;

Return a fully-qualified termsOfService resource name string.

**Parameter**  
---  
**Name** | **Description**  
`version` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### updateEmailPreferences(request, options)
    
    
    updateEmailPreferences(request?: protos.google.shopping.merchant.accounts.v1beta.IUpdateEmailPreferencesRequest, options?: CallOptions): Promise<[
            protos.google.shopping.merchant.accounts.v1beta.IEmailPreferences,
            (protos.google.shopping.merchant.accounts.v1beta.IUpdateEmailPreferencesRequest | undefined),
            {} | undefined
        ]>;

Updates the email preferences for a Merchant Center account user. MCA users should specify the MCA account rather than a sub-account of the MCA.

Preferences which are not explicitly selected in the update mask will not be updated.

It is invalid for updates to specify an UNCONFIRMED opt-in status value.

Use the name=accounts/* /users/me/emailPreferences alias to update preferences for the authenticated user.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEmailPreferencesRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.iupdateemailpreferencesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.shopping.merchant.accounts.v1beta.IEmailPreferences](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.iemailpreferences), ([protos.google.shopping.merchant.accounts.v1beta.IUpdateEmailPreferencesRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.iupdateemailpreferencesrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Email Preferences to be updated.
       */
      // const emailPreferences = {}
      /**
       *  Required. List of fields being updated.
       */
      // const updateMask = {}
    
      // Imports the Accounts library
      const {EmailPreferencesServiceClient} = require('[@google-shopping/accounts](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const accountsClient = new [EmailPreferencesServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/overview.html)();
    
      async function callUpdateEmailPreferences() {
        // Construct request
        const request = {
          emailPreferences,
          updateMask,
        };
    
        // Run request
        const response = await accountsClient.updateEmailPreferences(request);
        console.log(response);
      }
    
      callUpdateEmailPreferences();
    
    

### updateEmailPreferences(request, options, callback)
    
    
    updateEmailPreferences(request: protos.google.shopping.merchant.accounts.v1beta.IUpdateEmailPreferencesRequest, options: CallOptions, callback: Callback<protos.google.shopping.merchant.accounts.v1beta.IEmailPreferences, protos.google.shopping.merchant.accounts.v1beta.IUpdateEmailPreferencesRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEmailPreferencesRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.iupdateemailpreferencesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.shopping.merchant.accounts.v1beta.IEmailPreferences](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.iemailpreferences), [protos.google.shopping.merchant.accounts.v1beta.IUpdateEmailPreferencesRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.iupdateemailpreferencesrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateEmailPreferences(request, callback)
    
    
    updateEmailPreferences(request: protos.google.shopping.merchant.accounts.v1beta.IUpdateEmailPreferencesRequest, callback: Callback<protos.google.shopping.merchant.accounts.v1beta.IEmailPreferences, protos.google.shopping.merchant.accounts.v1beta.IUpdateEmailPreferencesRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEmailPreferencesRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.iupdateemailpreferencesrequest)`   
  
`callback` |  `Callback<[protos.google.shopping.merchant.accounts.v1beta.IEmailPreferences](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.iemailpreferences), [protos.google.shopping.merchant.accounts.v1beta.IUpdateEmailPreferencesRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.iupdateemailpreferencesrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### userPath(account, email)
    
    
    userPath(account: string, email: string): string;

Return a fully-qualified user resource name string.

**Parameters**  
---  
**Name** | **Description**  
`account` |  `string`   
  
`email` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
