---
url: https://docs.cloud.google.com/cpp/docs/reference/channel/latest/classgoogle_1_1cloud_1_1channel__v1_1_1CloudChannelServiceConnectionIdempotencyPolicy/
title: Class CloudChannelServiceConnectionIdempotencyPolicy (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:22:02.343209+00:00
---

# Class CloudChannelServiceConnectionIdempotencyPolicy (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/channel/latest/classgoogle_1_1cloud_1_1channel__v1_1_1CloudChannelServiceConnectionIdempotencyPolicy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class CloudChannelServiceConnectionIdempotencyPolicy (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

## Functions 

### virtual clone() const

Create a new copy of this object. 

**Returns**  
---  
**Type** | **Description**  
`std::unique_ptr< CloudChannelServiceConnectionIdempotencyPolicy >` |   
  
### virtual ListCustomers(google::cloud::channel::v1::ListCustomersRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::ListCustomersRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual GetCustomer(google::cloud::channel::v1::GetCustomerRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::GetCustomerRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual CheckCloudIdentityAccountsExist(google::cloud::channel::v1::CheckCloudIdentityAccountsExistRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::CheckCloudIdentityAccountsExistRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual CreateCustomer(google::cloud::channel::v1::CreateCustomerRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::CreateCustomerRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual UpdateCustomer(google::cloud::channel::v1::UpdateCustomerRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::UpdateCustomerRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual DeleteCustomer(google::cloud::channel::v1::DeleteCustomerRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::DeleteCustomerRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ImportCustomer(google::cloud::channel::v1::ImportCustomerRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::ImportCustomerRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ProvisionCloudIdentity(google::cloud::channel::v1::ProvisionCloudIdentityRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::ProvisionCloudIdentityRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListEntitlements(google::cloud::channel::v1::ListEntitlementsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::ListEntitlementsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListTransferableSkus(google::cloud::channel::v1::ListTransferableSkusRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::ListTransferableSkusRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListTransferableOffers(google::cloud::channel::v1::ListTransferableOffersRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::ListTransferableOffersRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual GetEntitlement(google::cloud::channel::v1::GetEntitlementRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::GetEntitlementRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual CreateEntitlement(google::cloud::channel::v1::CreateEntitlementRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::CreateEntitlementRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ChangeParameters(google::cloud::channel::v1::ChangeParametersRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::ChangeParametersRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ChangeRenewalSettings(google::cloud::channel::v1::ChangeRenewalSettingsRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::ChangeRenewalSettingsRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ChangeOffer(google::cloud::channel::v1::ChangeOfferRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::ChangeOfferRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual StartPaidService(google::cloud::channel::v1::StartPaidServiceRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::StartPaidServiceRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual SuspendEntitlement(google::cloud::channel::v1::SuspendEntitlementRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::SuspendEntitlementRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual CancelEntitlement(google::cloud::channel::v1::CancelEntitlementRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::CancelEntitlementRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ActivateEntitlement(google::cloud::channel::v1::ActivateEntitlementRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::ActivateEntitlementRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual TransferEntitlements(google::cloud::channel::v1::TransferEntitlementsRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::TransferEntitlementsRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual TransferEntitlementsToGoogle(google::cloud::channel::v1::TransferEntitlementsToGoogleRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::TransferEntitlementsToGoogleRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListChannelPartnerLinks(google::cloud::channel::v1::ListChannelPartnerLinksRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::ListChannelPartnerLinksRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual GetChannelPartnerLink(google::cloud::channel::v1::GetChannelPartnerLinkRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::GetChannelPartnerLinkRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual CreateChannelPartnerLink(google::cloud::channel::v1::CreateChannelPartnerLinkRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::CreateChannelPartnerLinkRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual UpdateChannelPartnerLink(google::cloud::channel::v1::UpdateChannelPartnerLinkRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::UpdateChannelPartnerLinkRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual GetCustomerRepricingConfig(google::cloud::channel::v1::GetCustomerRepricingConfigRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::GetCustomerRepricingConfigRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListCustomerRepricingConfigs(google::cloud::channel::v1::ListCustomerRepricingConfigsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::ListCustomerRepricingConfigsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual CreateCustomerRepricingConfig(google::cloud::channel::v1::CreateCustomerRepricingConfigRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::CreateCustomerRepricingConfigRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual UpdateCustomerRepricingConfig(google::cloud::channel::v1::UpdateCustomerRepricingConfigRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::UpdateCustomerRepricingConfigRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual DeleteCustomerRepricingConfig(google::cloud::channel::v1::DeleteCustomerRepricingConfigRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::DeleteCustomerRepricingConfigRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual GetChannelPartnerRepricingConfig(google::cloud::channel::v1::GetChannelPartnerRepricingConfigRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::GetChannelPartnerRepricingConfigRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListChannelPartnerRepricingConfigs(google::cloud::channel::v1::ListChannelPartnerRepricingConfigsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::ListChannelPartnerRepricingConfigsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual CreateChannelPartnerRepricingConfig(google::cloud::channel::v1::CreateChannelPartnerRepricingConfigRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::CreateChannelPartnerRepricingConfigRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual UpdateChannelPartnerRepricingConfig(google::cloud::channel::v1::UpdateChannelPartnerRepricingConfigRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::UpdateChannelPartnerRepricingConfigRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual DeleteChannelPartnerRepricingConfig(google::cloud::channel::v1::DeleteChannelPartnerRepricingConfigRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::DeleteChannelPartnerRepricingConfigRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListSkuGroups(google::cloud::channel::v1::ListSkuGroupsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::ListSkuGroupsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListSkuGroupBillableSkus(google::cloud::channel::v1::ListSkuGroupBillableSkusRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::ListSkuGroupBillableSkusRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual LookupOffer(google::cloud::channel::v1::LookupOfferRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::LookupOfferRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListProducts(google::cloud::channel::v1::ListProductsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::ListProductsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListSkus(google::cloud::channel::v1::ListSkusRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::ListSkusRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListOffers(google::cloud::channel::v1::ListOffersRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::ListOffersRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListPurchasableSkus(google::cloud::channel::v1::ListPurchasableSkusRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::ListPurchasableSkusRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListPurchasableOffers(google::cloud::channel::v1::ListPurchasableOffersRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::ListPurchasableOffersRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual QueryEligibleBillingAccounts(google::cloud::channel::v1::QueryEligibleBillingAccountsRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::QueryEligibleBillingAccountsRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual RegisterSubscriber(google::cloud::channel::v1::RegisterSubscriberRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::RegisterSubscriberRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual UnregisterSubscriber(google::cloud::channel::v1::UnregisterSubscriberRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::UnregisterSubscriberRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListSubscribers(google::cloud::channel::v1::ListSubscribersRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::ListSubscribersRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListEntitlementChanges(google::cloud::channel::v1::ListEntitlementChangesRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::channel::v1::ListEntitlementChangesRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListOperations(google::longrunning::ListOperationsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::ListOperationsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual GetOperation(google::longrunning::GetOperationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::GetOperationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual DeleteOperation(google::longrunning::DeleteOperationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::DeleteOperationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual CancelOperation(google::longrunning::CancelOperationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::CancelOperationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
