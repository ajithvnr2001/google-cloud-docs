---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/merchant/accounts/apiv1beta/accountspb/
title: Shopping Merchant Accounts API v1beta - Package cloud.google.com/go/shopping/merchant/accounts/apiv1beta/accountspb (v1.17.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:57:14.795113+00:00
---

# Shopping Merchant Accounts API v1beta - Package cloud.google.com/go/shopping/merchant/accounts/apiv1beta/accountspb (v1.17.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/merchant/accounts/apiv1beta/accountspb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Shopping Merchant Accounts API v1beta - Package cloud.google.com/go/shopping/merchant/accounts/apiv1beta/accountspb (v1.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.17.0 (latest)  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.1  1.1.1  1.0.0  0.25.0  0.24.1  0.23.0  0.22.0  0.21.0  0.20.0  0.19.1  0.18.1  0.17.1  0.16.0  0.15.0  0.14.0  0.13.0  0.12.1  0.11.1  0.10.0  0.9.2  0.8.7  0.7.0  0.6.0  0.5.0  0.4.0  0.3.2  0.2.2 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/shopping/merchant/accounts/apiv1beta/accountspb). 

##  Constants 

### AccountTaxService_GetAccountTax_FullMethodName, AccountTaxService_ListAccountTax_FullMethodName, AccountTaxService_UpdateAccountTax_FullMethodName
    
    
    const (
    	AccountTaxService_GetAccountTax_FullMethodName    = "/google.shopping.merchant.accounts.v1beta.AccountTaxService/GetAccountTax"
    	AccountTaxService_ListAccountTax_FullMethodName   = "/google.shopping.merchant.accounts.v1beta.AccountTaxService/ListAccountTax"
    	AccountTaxService_UpdateAccountTax_FullMethodName = "/google.shopping.merchant.accounts.v1beta.AccountTaxService/UpdateAccountTax"
    )

### AccountsService_GetAccount_FullMethodName, AccountsService_CreateAndConfigureAccount_FullMethodName, AccountsService_DeleteAccount_FullMethodName, AccountsService_UpdateAccount_FullMethodName, AccountsService_ListAccounts_FullMethodName, AccountsService_ListSubAccounts_FullMethodName
    
    
    const (
    	AccountsService_GetAccount_FullMethodName                = "/google.shopping.merchant.accounts.v1beta.AccountsService/GetAccount"
    	AccountsService_CreateAndConfigureAccount_FullMethodName = "/google.shopping.merchant.accounts.v1beta.AccountsService/CreateAndConfigureAccount"
    	AccountsService_DeleteAccount_FullMethodName             = "/google.shopping.merchant.accounts.v1beta.AccountsService/DeleteAccount"
    	AccountsService_UpdateAccount_FullMethodName             = "/google.shopping.merchant.accounts.v1beta.AccountsService/UpdateAccount"
    	AccountsService_ListAccounts_FullMethodName              = "/google.shopping.merchant.accounts.v1beta.AccountsService/ListAccounts"
    	AccountsService_ListSubAccounts_FullMethodName           = "/google.shopping.merchant.accounts.v1beta.AccountsService/ListSubAccounts"
    )

### AutofeedSettingsService_GetAutofeedSettings_FullMethodName, AutofeedSettingsService_UpdateAutofeedSettings_FullMethodName
    
    
    const (
    	AutofeedSettingsService_GetAutofeedSettings_FullMethodName    = "/google.shopping.merchant.accounts.v1beta.AutofeedSettingsService/GetAutofeedSettings"
    	AutofeedSettingsService_UpdateAutofeedSettings_FullMethodName = "/google.shopping.merchant.accounts.v1beta.AutofeedSettingsService/UpdateAutofeedSettings"
    )

### AutomaticImprovementsService_GetAutomaticImprovements_FullMethodName, AutomaticImprovementsService_UpdateAutomaticImprovements_FullMethodName
    
    
    const (
    	AutomaticImprovementsService_GetAutomaticImprovements_FullMethodName    = "/google.shopping.merchant.accounts.v1beta.AutomaticImprovementsService/GetAutomaticImprovements"
    	AutomaticImprovementsService_UpdateAutomaticImprovements_FullMethodName = "/google.shopping.merchant.accounts.v1beta.AutomaticImprovementsService/UpdateAutomaticImprovements"
    )

### BusinessIdentityService_GetBusinessIdentity_FullMethodName, BusinessIdentityService_UpdateBusinessIdentity_FullMethodName
    
    
    const (
    	BusinessIdentityService_GetBusinessIdentity_FullMethodName    = "/google.shopping.merchant.accounts.v1beta.BusinessIdentityService/GetBusinessIdentity"
    	BusinessIdentityService_UpdateBusinessIdentity_FullMethodName = "/google.shopping.merchant.accounts.v1beta.BusinessIdentityService/UpdateBusinessIdentity"
    )

### BusinessInfoService_GetBusinessInfo_FullMethodName, BusinessInfoService_UpdateBusinessInfo_FullMethodName
    
    
    const (
    	BusinessInfoService_GetBusinessInfo_FullMethodName    = "/google.shopping.merchant.accounts.v1beta.BusinessInfoService/GetBusinessInfo"
    	BusinessInfoService_UpdateBusinessInfo_FullMethodName = "/google.shopping.merchant.accounts.v1beta.BusinessInfoService/UpdateBusinessInfo"
    )

### CheckoutSettingsService_GetCheckoutSettings_FullMethodName, CheckoutSettingsService_CreateCheckoutSettings_FullMethodName, CheckoutSettingsService_UpdateCheckoutSettings_FullMethodName, CheckoutSettingsService_DeleteCheckoutSettings_FullMethodName
    
    
    const (
    	CheckoutSettingsService_GetCheckoutSettings_FullMethodName    = "/google.shopping.merchant.accounts.v1beta.CheckoutSettingsService/GetCheckoutSettings"
    	CheckoutSettingsService_CreateCheckoutSettings_FullMethodName = "/google.shopping.merchant.accounts.v1beta.CheckoutSettingsService/CreateCheckoutSettings"
    	CheckoutSettingsService_UpdateCheckoutSettings_FullMethodName = "/google.shopping.merchant.accounts.v1beta.CheckoutSettingsService/UpdateCheckoutSettings"
    	CheckoutSettingsService_DeleteCheckoutSettings_FullMethodName = "/google.shopping.merchant.accounts.v1beta.CheckoutSettingsService/DeleteCheckoutSettings"
    )

### EmailPreferencesService_GetEmailPreferences_FullMethodName, EmailPreferencesService_UpdateEmailPreferences_FullMethodName
    
    
    const (
    	EmailPreferencesService_GetEmailPreferences_FullMethodName    = "/google.shopping.merchant.accounts.v1beta.EmailPreferencesService/GetEmailPreferences"
    	EmailPreferencesService_UpdateEmailPreferences_FullMethodName = "/google.shopping.merchant.accounts.v1beta.EmailPreferencesService/UpdateEmailPreferences"
    )

### GbpAccountsService_ListGbpAccounts_FullMethodName, GbpAccountsService_LinkGbpAccount_FullMethodName
    
    
    const (
    	GbpAccountsService_ListGbpAccounts_FullMethodName = "/google.shopping.merchant.accounts.v1beta.GbpAccountsService/ListGbpAccounts"
    	GbpAccountsService_LinkGbpAccount_FullMethodName  = "/google.shopping.merchant.accounts.v1beta.GbpAccountsService/LinkGbpAccount"
    )

### HomepageService_GetHomepage_FullMethodName, HomepageService_UpdateHomepage_FullMethodName, HomepageService_ClaimHomepage_FullMethodName, HomepageService_UnclaimHomepage_FullMethodName
    
    
    const (
    	HomepageService_GetHomepage_FullMethodName     = "/google.shopping.merchant.accounts.v1beta.HomepageService/GetHomepage"
    	HomepageService_UpdateHomepage_FullMethodName  = "/google.shopping.merchant.accounts.v1beta.HomepageService/UpdateHomepage"
    	HomepageService_ClaimHomepage_FullMethodName   = "/google.shopping.merchant.accounts.v1beta.HomepageService/ClaimHomepage"
    	HomepageService_UnclaimHomepage_FullMethodName = "/google.shopping.merchant.accounts.v1beta.HomepageService/UnclaimHomepage"
    )

### LfpProvidersService_FindLfpProviders_FullMethodName, LfpProvidersService_LinkLfpProvider_FullMethodName
    
    
    const (
    	LfpProvidersService_FindLfpProviders_FullMethodName = "/google.shopping.merchant.accounts.v1beta.LfpProvidersService/FindLfpProviders"
    	LfpProvidersService_LinkLfpProvider_FullMethodName  = "/google.shopping.merchant.accounts.v1beta.LfpProvidersService/LinkLfpProvider"
    )

### OmnichannelSettingsService_GetOmnichannelSetting_FullMethodName, OmnichannelSettingsService_ListOmnichannelSettings_FullMethodName, OmnichannelSettingsService_CreateOmnichannelSetting_FullMethodName, OmnichannelSettingsService_UpdateOmnichannelSetting_FullMethodName, OmnichannelSettingsService_RequestInventoryVerification_FullMethodName
    
    
    const (
    	OmnichannelSettingsService_GetOmnichannelSetting_FullMethodName        = "/google.shopping.merchant.accounts.v1beta.OmnichannelSettingsService/GetOmnichannelSetting"
    	OmnichannelSettingsService_ListOmnichannelSettings_FullMethodName      = "/google.shopping.merchant.accounts.v1beta.OmnichannelSettingsService/ListOmnichannelSettings"
    	OmnichannelSettingsService_CreateOmnichannelSetting_FullMethodName     = "/google.shopping.merchant.accounts.v1beta.OmnichannelSettingsService/CreateOmnichannelSetting"
    	OmnichannelSettingsService_UpdateOmnichannelSetting_FullMethodName     = "/google.shopping.merchant.accounts.v1beta.OmnichannelSettingsService/UpdateOmnichannelSetting"
    	OmnichannelSettingsService_RequestInventoryVerification_FullMethodName = "/google.shopping.merchant.accounts.v1beta.OmnichannelSettingsService/RequestInventoryVerification"
    )

### OnlineReturnPolicyService_GetOnlineReturnPolicy_FullMethodName, OnlineReturnPolicyService_ListOnlineReturnPolicies_FullMethodName, OnlineReturnPolicyService_CreateOnlineReturnPolicy_FullMethodName, OnlineReturnPolicyService_UpdateOnlineReturnPolicy_FullMethodName, OnlineReturnPolicyService_DeleteOnlineReturnPolicy_FullMethodName
    
    
    const (
    	OnlineReturnPolicyService_GetOnlineReturnPolicy_FullMethodName    = "/google.shopping.merchant.accounts.v1beta.OnlineReturnPolicyService/GetOnlineReturnPolicy"
    	OnlineReturnPolicyService_ListOnlineReturnPolicies_FullMethodName = "/google.shopping.merchant.accounts.v1beta.OnlineReturnPolicyService/ListOnlineReturnPolicies"
    	OnlineReturnPolicyService_CreateOnlineReturnPolicy_FullMethodName = "/google.shopping.merchant.accounts.v1beta.OnlineReturnPolicyService/CreateOnlineReturnPolicy"
    	OnlineReturnPolicyService_UpdateOnlineReturnPolicy_FullMethodName = "/google.shopping.merchant.accounts.v1beta.OnlineReturnPolicyService/UpdateOnlineReturnPolicy"
    	OnlineReturnPolicyService_DeleteOnlineReturnPolicy_FullMethodName = "/google.shopping.merchant.accounts.v1beta.OnlineReturnPolicyService/DeleteOnlineReturnPolicy"
    )

### ProgramsService_GetProgram_FullMethodName, ProgramsService_ListPrograms_FullMethodName, ProgramsService_EnableProgram_FullMethodName, ProgramsService_DisableProgram_FullMethodName
    
    
    const (
    	ProgramsService_GetProgram_FullMethodName     = "/google.shopping.merchant.accounts.v1beta.ProgramsService/GetProgram"
    	ProgramsService_ListPrograms_FullMethodName   = "/google.shopping.merchant.accounts.v1beta.ProgramsService/ListPrograms"
    	ProgramsService_EnableProgram_FullMethodName  = "/google.shopping.merchant.accounts.v1beta.ProgramsService/EnableProgram"
    	ProgramsService_DisableProgram_FullMethodName = "/google.shopping.merchant.accounts.v1beta.ProgramsService/DisableProgram"
    )

### RegionsService_GetRegion_FullMethodName, RegionsService_CreateRegion_FullMethodName, RegionsService_UpdateRegion_FullMethodName, RegionsService_DeleteRegion_FullMethodName, RegionsService_ListRegions_FullMethodName
    
    
    const (
    	RegionsService_GetRegion_FullMethodName    = "/google.shopping.merchant.accounts.v1beta.RegionsService/GetRegion"
    	RegionsService_CreateRegion_FullMethodName = "/google.shopping.merchant.accounts.v1beta.RegionsService/CreateRegion"
    	RegionsService_UpdateRegion_FullMethodName = "/google.shopping.merchant.accounts.v1beta.RegionsService/UpdateRegion"
    	RegionsService_DeleteRegion_FullMethodName = "/google.shopping.merchant.accounts.v1beta.RegionsService/DeleteRegion"
    	RegionsService_ListRegions_FullMethodName  = "/google.shopping.merchant.accounts.v1beta.RegionsService/ListRegions"
    )

### ShippingSettingsService_GetShippingSettings_FullMethodName, ShippingSettingsService_InsertShippingSettings_FullMethodName
    
    
    const (
    	ShippingSettingsService_GetShippingSettings_FullMethodName    = "/google.shopping.merchant.accounts.v1beta.ShippingSettingsService/GetShippingSettings"
    	ShippingSettingsService_InsertShippingSettings_FullMethodName = "/google.shopping.merchant.accounts.v1beta.ShippingSettingsService/InsertShippingSettings"
    )

### TermsOfServiceService_GetTermsOfService_FullMethodName, TermsOfServiceService_RetrieveLatestTermsOfService_FullMethodName, TermsOfServiceService_AcceptTermsOfService_FullMethodName
    
    
    const (
    	TermsOfServiceService_GetTermsOfService_FullMethodName            = "/google.shopping.merchant.accounts.v1beta.TermsOfServiceService/GetTermsOfService"
    	TermsOfServiceService_RetrieveLatestTermsOfService_FullMethodName = "/google.shopping.merchant.accounts.v1beta.TermsOfServiceService/RetrieveLatestTermsOfService"
    	TermsOfServiceService_AcceptTermsOfService_FullMethodName         = "/google.shopping.merchant.accounts.v1beta.TermsOfServiceService/AcceptTermsOfService"
    )

### TermsOfServiceAgreementStateService_GetTermsOfServiceAgreementState_FullMethodName, TermsOfServiceAgreementStateService_RetrieveForApplicationTermsOfServiceAgreementState_FullMethodName
    
    
    const (
    	TermsOfServiceAgreementStateService_GetTermsOfServiceAgreementState_FullMethodName                    = "/google.shopping.merchant.accounts.v1beta.TermsOfServiceAgreementStateService/GetTermsOfServiceAgreementState"
    	TermsOfServiceAgreementStateService_RetrieveForApplicationTermsOfServiceAgreementState_FullMethodName = "/google.shopping.merchant.accounts.v1beta.TermsOfServiceAgreementStateService/RetrieveForApplicationTermsOfServiceAgreementState"
    )

### UserService_GetUser_FullMethodName, UserService_CreateUser_FullMethodName, UserService_DeleteUser_FullMethodName, UserService_UpdateUser_FullMethodName, UserService_ListUsers_FullMethodName
    
    
    const (
    	UserService_GetUser_FullMethodName    = "/google.shopping.merchant.accounts.v1beta.UserService/GetUser"
    	UserService_CreateUser_FullMethodName = "/google.shopping.merchant.accounts.v1beta.UserService/CreateUser"
    	UserService_DeleteUser_FullMethodName = "/google.shopping.merchant.accounts.v1beta.UserService/DeleteUser"
    	UserService_UpdateUser_FullMethodName = "/google.shopping.merchant.accounts.v1beta.UserService/UpdateUser"
    	UserService_ListUsers_FullMethodName  = "/google.shopping.merchant.accounts.v1beta.UserService/ListUsers"
    )

### AccountIssueService_ListAccountIssues_FullMethodName
    
    
    const (
    	AccountIssueService_ListAccountIssues_FullMethodName = "/google.shopping.merchant.accounts.v1beta.AccountIssueService/ListAccountIssues"
    )

## Variables 

### AccessRight_name, AccessRight_value
    
    
    var (
    	AccessRight_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "ACCESS_RIGHT_UNSPECIFIED",
    		1: "STANDARD",
    		2: "ADMIN",
    		3: "PERFORMANCE_REPORTING",
    	}
    	AccessRight_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"ACCESS_RIGHT_UNSPECIFIED": 0,
    		"STANDARD":                 1,
    		"ADMIN":                    2,
    		"PERFORMANCE_REPORTING":    3,
    	}
    )

Enum value maps for AccessRight.

### AccountIssue_Severity_name, AccountIssue_Severity_value
    
    
    var (
    	AccountIssue_Severity_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "SEVERITY_UNSPECIFIED",
    		1: "CRITICAL",
    		2: "ERROR",
    		3: "SUGGESTION",
    	}
    	AccountIssue_Severity_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"SEVERITY_UNSPECIFIED": 0,
    		"CRITICAL":             1,
    		"ERROR":                2,
    		"SUGGESTION":           3,
    	}
    )

Enum value maps for AccountIssue_Severity.

### BusinessIdentity_PromotionsConsent_name, BusinessIdentity_PromotionsConsent_value
    
    
    var (
    	BusinessIdentity_PromotionsConsent_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "PROMOTIONS_CONSENT_UNSPECIFIED",
    		1: "PROMOTIONS_CONSENT_GIVEN",
    		2: "PROMOTIONS_CONSENT_DENIED",
    	}
    	BusinessIdentity_PromotionsConsent_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"PROMOTIONS_CONSENT_UNSPECIFIED": 0,
    		"PROMOTIONS_CONSENT_GIVEN":       1,
    		"PROMOTIONS_CONSENT_DENIED":      2,
    	}
    )

Enum value maps for BusinessIdentity_PromotionsConsent.

### BusinessIdentity_IdentityAttribute_IdentityDeclaration_name, BusinessIdentity_IdentityAttribute_IdentityDeclaration_value
    
    
    var (
    	BusinessIdentity_IdentityAttribute_IdentityDeclaration_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "IDENTITY_DECLARATION_UNSPECIFIED",
    		1: "SELF_IDENTIFIES_AS",
    		2: "DOES_NOT_SELF_IDENTIFY_AS",
    	}
    	BusinessIdentity_IdentityAttribute_IdentityDeclaration_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"IDENTITY_DECLARATION_UNSPECIFIED": 0,
    		"SELF_IDENTIFIES_AS":               1,
    		"DOES_NOT_SELF_IDENTIFY_AS":        2,
    	}
    )

Enum value maps for BusinessIdentity_IdentityAttribute_IdentityDeclaration.

### CheckoutSettings_CheckoutEnrollmentState_name, CheckoutSettings_CheckoutEnrollmentState_value
    
    
    var (
    	CheckoutSettings_CheckoutEnrollmentState_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "CHECKOUT_ENROLLMENT_STATE_UNSPECIFIED",
    		1: "INACTIVE",
    		2: "ENROLLED",
    		3: "OPTED_OUT",
    	}
    	CheckoutSettings_CheckoutEnrollmentState_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"CHECKOUT_ENROLLMENT_STATE_UNSPECIFIED": 0,
    		"INACTIVE":                              1,
    		"ENROLLED":                              2,
    		"OPTED_OUT":                             3,
    	}
    )

Enum value maps for CheckoutSettings_CheckoutEnrollmentState.

### CheckoutSettings_CheckoutReviewState_name, CheckoutSettings_CheckoutReviewState_value
    
    
    var (
    	CheckoutSettings_CheckoutReviewState_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "CHECKOUT_REVIEW_STATE_UNSPECIFIED",
    		1: "IN_REVIEW",
    		2: "APPROVED",
    		3: "DISAPPROVED",
    	}
    	CheckoutSettings_CheckoutReviewState_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"CHECKOUT_REVIEW_STATE_UNSPECIFIED": 0,
    		"IN_REVIEW":                         1,
    		"APPROVED":                          2,
    		"DISAPPROVED":                       3,
    	}
    )

Enum value maps for CheckoutSettings_CheckoutReviewState.

### EmailPreferences_OptInState_name, EmailPreferences_OptInState_value
    
    
    var (
    	EmailPreferences_OptInState_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "OPT_IN_STATE_UNSPECIFIED",
    		1: "OPTED_OUT",
    		2: "OPTED_IN",
    		3: "UNCONFIRMED",
    	}
    	EmailPreferences_OptInState_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"OPT_IN_STATE_UNSPECIFIED": 0,
    		"OPTED_OUT":                1,
    		"OPTED_IN":                 2,
    		"UNCONFIRMED":              3,
    	}
    )

Enum value maps for EmailPreferences_OptInState.

### GbpAccount_Type_name, GbpAccount_Type_value
    
    
    var (
    	GbpAccount_Type_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "TYPE_UNSPECIFIED",
    		1: "USER",
    		2: "BUSINESS_ACCOUNT",
    	}
    	GbpAccount_Type_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"TYPE_UNSPECIFIED": 0,
    		"USER":             1,
    		"BUSINESS_ACCOUNT": 2,
    	}
    )

Enum value maps for GbpAccount_Type.

### OmnichannelSetting_LsfType_name, OmnichannelSetting_LsfType_value
    
    
    var (
    	OmnichannelSetting_LsfType_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "LSF_TYPE_UNSPECIFIED",
    		1: "GHLSF",
    		2: "MHLSF_BASIC",
    		3: "MHLSF_FULL",
    	}
    	OmnichannelSetting_LsfType_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"LSF_TYPE_UNSPECIFIED": 0,
    		"GHLSF":                1,
    		"MHLSF_BASIC":          2,
    		"MHLSF_FULL":           3,
    	}
    )

Enum value maps for OmnichannelSetting_LsfType.

### ReviewState_State_name, ReviewState_State_value
    
    
    var (
    	ReviewState_State_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "STATE_UNSPECIFIED",
    		1: "ACTIVE",
    		2: "FAILED",
    		3: "RUNNING",
    		4: "ACTION_REQUIRED",
    	}
    	ReviewState_State_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"STATE_UNSPECIFIED": 0,
    		"ACTIVE":            1,
    		"FAILED":            2,
    		"RUNNING":           3,
    		"ACTION_REQUIRED":   4,
    	}
    )

Enum value maps for ReviewState_State.

### InventoryVerification_State_name, InventoryVerification_State_value
    
    
    var (
    	InventoryVerification_State_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "STATE_UNSPECIFIED",
    		1: "ACTION_REQUIRED",
    		5: "INACTIVE",
    		2: "RUNNING",
    		3: "SUCCEEDED",
    		4: "SUSPENDED",
    	}
    	InventoryVerification_State_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"STATE_UNSPECIFIED": 0,
    		"ACTION_REQUIRED":   1,
    		"INACTIVE":          5,
    		"RUNNING":           2,
    		"SUCCEEDED":         3,
    		"SUSPENDED":         4,
    	}
    )

Enum value maps for InventoryVerification_State.

### OnlineReturnPolicy_ReturnMethod_name, OnlineReturnPolicy_ReturnMethod_value
    
    
    var (
    	OnlineReturnPolicy_ReturnMethod_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "RETURN_METHOD_UNSPECIFIED",
    		1: "BY_MAIL",
    		2: "IN_STORE",
    		3: "AT_A_KIOSK",
    	}
    	OnlineReturnPolicy_ReturnMethod_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"RETURN_METHOD_UNSPECIFIED": 0,
    		"BY_MAIL":                   1,
    		"IN_STORE":                  2,
    		"AT_A_KIOSK":                3,
    	}
    )

Enum value maps for OnlineReturnPolicy_ReturnMethod.

### OnlineReturnPolicy_ItemCondition_name, OnlineReturnPolicy_ItemCondition_value
    
    
    var (
    	OnlineReturnPolicy_ItemCondition_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "ITEM_CONDITION_UNSPECIFIED",
    		1: "NEW",
    		2: "USED",
    	}
    	OnlineReturnPolicy_ItemCondition_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"ITEM_CONDITION_UNSPECIFIED": 0,
    		"NEW":                        1,
    		"USED":                       2,
    	}
    )

Enum value maps for OnlineReturnPolicy_ItemCondition.

### OnlineReturnPolicy_ReturnLabelSource_name, OnlineReturnPolicy_ReturnLabelSource_value
    
    
    var (
    	OnlineReturnPolicy_ReturnLabelSource_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "RETURN_LABEL_SOURCE_UNSPECIFIED",
    		1: "DOWNLOAD_AND_PRINT",
    		2: "IN_THE_PACKAGE",
    		3: "CUSTOMER_RESPONSIBILITY",
    	}
    	OnlineReturnPolicy_ReturnLabelSource_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"RETURN_LABEL_SOURCE_UNSPECIFIED": 0,
    		"DOWNLOAD_AND_PRINT":              1,
    		"IN_THE_PACKAGE":                  2,
    		"CUSTOMER_RESPONSIBILITY":         3,
    	}
    )

Enum value maps for OnlineReturnPolicy_ReturnLabelSource.

### OnlineReturnPolicy_ReturnShippingFee_Type_name, OnlineReturnPolicy_ReturnShippingFee_Type_value
    
    
    var (
    	OnlineReturnPolicy_ReturnShippingFee_Type_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "TYPE_UNSPECIFIED",
    		1: "FIXED",
    		2: "CUSTOMER_PAYING_ACTUAL_FEE",
    	}
    	OnlineReturnPolicy_ReturnShippingFee_Type_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"TYPE_UNSPECIFIED":           0,
    		"FIXED":                      1,
    		"CUSTOMER_PAYING_ACTUAL_FEE": 2,
    	}
    )

Enum value maps for OnlineReturnPolicy_ReturnShippingFee_Type.

### OnlineReturnPolicy_Policy_Type_name, OnlineReturnPolicy_Policy_Type_value
    
    
    var (
    	OnlineReturnPolicy_Policy_Type_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "TYPE_UNSPECIFIED",
    		1: "NUMBER_OF_DAYS_AFTER_DELIVERY",
    		2: "NO_RETURNS",
    		3: "LIFETIME_RETURNS",
    	}
    	OnlineReturnPolicy_Policy_Type_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"TYPE_UNSPECIFIED":              0,
    		"NUMBER_OF_DAYS_AFTER_DELIVERY": 1,
    		"NO_RETURNS":                    2,
    		"LIFETIME_RETURNS":              3,
    	}
    )

Enum value maps for OnlineReturnPolicy_Policy_Type.

### PhoneVerificationState_name, PhoneVerificationState_value
    
    
    var (
    	PhoneVerificationState_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "PHONE_VERIFICATION_STATE_UNSPECIFIED",
    		1: "PHONE_VERIFICATION_STATE_VERIFIED",
    		2: "PHONE_VERIFICATION_STATE_UNVERIFIED",
    	}
    	PhoneVerificationState_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"PHONE_VERIFICATION_STATE_UNSPECIFIED": 0,
    		"PHONE_VERIFICATION_STATE_VERIFIED":    1,
    		"PHONE_VERIFICATION_STATE_UNVERIFIED":  2,
    	}
    )

Enum value maps for PhoneVerificationState.

### Program_State_name, Program_State_value
    
    
    var (
    	Program_State_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "STATE_UNSPECIFIED",
    		1: "NOT_ELIGIBLE",
    		2: "ELIGIBLE",
    		3: "ENABLED",
    	}
    	Program_State_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"STATE_UNSPECIFIED": 0,
    		"NOT_ELIGIBLE":      1,
    		"ELIGIBLE":          2,
    		"ENABLED":           3,
    	}
    )

Enum value maps for Program_State.

### Service_ShipmentType_name, Service_ShipmentType_value
    
    
    var (
    	Service_ShipmentType_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "SHIPMENT_TYPE_UNSPECIFIED",
    		1: "DELIVERY",
    		2: "LOCAL_DELIVERY",
    		3: "COLLECTION_POINT",
    	}
    	Service_ShipmentType_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"SHIPMENT_TYPE_UNSPECIFIED": 0,
    		"DELIVERY":                  1,
    		"LOCAL_DELIVERY":            2,
    		"COLLECTION_POINT":          3,
    	}
    )

Enum value maps for Service_ShipmentType.

### Service_StoreConfig_StoreServiceType_name, Service_StoreConfig_StoreServiceType_value
    
    
    var (
    	Service_StoreConfig_StoreServiceType_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "STORE_SERVICE_TYPE_UNSPECIFIED",
    		1: "ALL_STORES",
    		2: "SELECTED_STORES",
    	}
    	Service_StoreConfig_StoreServiceType_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"STORE_SERVICE_TYPE_UNSPECIFIED": 0,
    		"ALL_STORES":                     1,
    		"SELECTED_STORES":                2,
    	}
    )

Enum value maps for Service_StoreConfig_StoreServiceType.

### Distance_Unit_name, Distance_Unit_value
    
    
    var (
    	Distance_Unit_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "UNIT_UNSPECIFIED",
    		1: "MILES",
    		2: "KILOMETERS",
    	}
    	Distance_Unit_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"UNIT_UNSPECIFIED": 0,
    		"MILES":            1,
    		"KILOMETERS":       2,
    	}
    )

Enum value maps for Distance_Unit.

### BusinessDayConfig_Weekday_name, BusinessDayConfig_Weekday_value
    
    
    var (
    	BusinessDayConfig_Weekday_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "WEEKDAY_UNSPECIFIED",
    		1: "MONDAY",
    		2: "TUESDAY",
    		3: "WEDNESDAY",
    		4: "THURSDAY",
    		5: "FRIDAY",
    		6: "SATURDAY",
    		7: "SUNDAY",
    	}
    	BusinessDayConfig_Weekday_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"WEEKDAY_UNSPECIFIED": 0,
    		"MONDAY":              1,
    		"TUESDAY":             2,
    		"WEDNESDAY":           3,
    		"THURSDAY":            4,
    		"FRIDAY":              5,
    		"SATURDAY":            6,
    		"SUNDAY":              7,
    	}
    )

Enum value maps for BusinessDayConfig_Weekday.

### TermsOfServiceKind_name, TermsOfServiceKind_value
    
    
    var (
    	TermsOfServiceKind_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "TERMS_OF_SERVICE_KIND_UNSPECIFIED",
    		1: "MERCHANT_CENTER",
    	}
    	TermsOfServiceKind_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"TERMS_OF_SERVICE_KIND_UNSPECIFIED": 0,
    		"MERCHANT_CENTER":                   1,
    	}
    )

Enum value maps for TermsOfServiceKind.

### User_State_name, User_State_value
    
    
    var (
    	User_State_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "STATE_UNSPECIFIED",
    		1: "PENDING",
    		2: "VERIFIED",
    	}
    	User_State_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"STATE_UNSPECIFIED": 0,
    		"PENDING":           1,
    		"VERIFIED":          2,
    	}
    )

Enum value maps for User_State.

### VerificationMailSettings_VerificationMailMode_name, VerificationMailSettings_VerificationMailMode_value
    
    
    var (
    	VerificationMailSettings_VerificationMailMode_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "VERIFICATION_MAIL_MODE_UNSPECIFIED",
    		1: "SEND_VERIFICATION_MAIL",
    		2: "SUPPRESS_VERIFICATION_MAIL",
    	}
    	VerificationMailSettings_VerificationMailMode_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"VERIFICATION_MAIL_MODE_UNSPECIFIED": 0,
    		"SEND_VERIFICATION_MAIL":             1,
    		"SUPPRESS_VERIFICATION_MAIL":         2,
    	}
    )

Enum value maps for VerificationMailSettings_VerificationMailMode.

### AccountIssueService_ServiceDesc
    
    
    var AccountIssueService_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.shopping.merchant.accounts.v1beta.AccountIssueService",
    	HandlerType: (*AccountIssueServiceServer)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "ListAccountIssues",
    			Handler:    _AccountIssueService_ListAccountIssues_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/shopping/merchant/accounts/v1beta/accountissue.proto",
    }

AccountIssueService_ServiceDesc is the grpc.ServiceDesc for AccountIssueService service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

### AccountTaxService_ServiceDesc
    
    
    var AccountTaxService_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.shopping.merchant.accounts.v1beta.AccountTaxService",
    	HandlerType: (*AccountTaxServiceServer)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "GetAccountTax",
    			Handler:    _AccountTaxService_GetAccountTax_Handler,
    		},
    		{
    			MethodName: "ListAccountTax",
    			Handler:    _AccountTaxService_ListAccountTax_Handler,
    		},
    		{
    			MethodName: "UpdateAccountTax",
    			Handler:    _AccountTaxService_UpdateAccountTax_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/shopping/merchant/accounts/v1beta/account_tax.proto",
    }

AccountTaxService_ServiceDesc is the grpc.ServiceDesc for AccountTaxService service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

### AccountsService_ServiceDesc
    
    
    var AccountsService_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.shopping.merchant.accounts.v1beta.AccountsService",
    	HandlerType: (*AccountsServiceServer)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "GetAccount",
    			Handler:    _AccountsService_GetAccount_Handler,
    		},
    		{
    			MethodName: "CreateAndConfigureAccount",
    			Handler:    _AccountsService_CreateAndConfigureAccount_Handler,
    		},
    		{
    			MethodName: "DeleteAccount",
    			Handler:    _AccountsService_DeleteAccount_Handler,
    		},
    		{
    			MethodName: "UpdateAccount",
    			Handler:    _AccountsService_UpdateAccount_Handler,
    		},
    		{
    			MethodName: "ListAccounts",
    			Handler:    _AccountsService_ListAccounts_Handler,
    		},
    		{
    			MethodName: "ListSubAccounts",
    			Handler:    _AccountsService_ListSubAccounts_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/shopping/merchant/accounts/v1beta/accounts.proto",
    }

AccountsService_ServiceDesc is the grpc.ServiceDesc for AccountsService service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

### AutofeedSettingsService_ServiceDesc
    
    
    var AutofeedSettingsService_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.shopping.merchant.accounts.v1beta.AutofeedSettingsService",
    	HandlerType: (*AutofeedSettingsServiceServer)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "GetAutofeedSettings",
    			Handler:    _AutofeedSettingsService_GetAutofeedSettings_Handler,
    		},
    		{
    			MethodName: "UpdateAutofeedSettings",
    			Handler:    _AutofeedSettingsService_UpdateAutofeedSettings_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/shopping/merchant/accounts/v1beta/autofeedsettings.proto",
    }

AutofeedSettingsService_ServiceDesc is the grpc.ServiceDesc for AutofeedSettingsService service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

### AutomaticImprovementsService_ServiceDesc
    
    
    var AutomaticImprovementsService_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.shopping.merchant.accounts.v1beta.AutomaticImprovementsService",
    	HandlerType: (*AutomaticImprovementsServiceServer)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "GetAutomaticImprovements",
    			Handler:    _AutomaticImprovementsService_GetAutomaticImprovements_Handler,
    		},
    		{
    			MethodName: "UpdateAutomaticImprovements",
    			Handler:    _AutomaticImprovementsService_UpdateAutomaticImprovements_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/shopping/merchant/accounts/v1beta/automaticimprovements.proto",
    }

AutomaticImprovementsService_ServiceDesc is the grpc.ServiceDesc for AutomaticImprovementsService service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

### BusinessIdentityService_ServiceDesc
    
    
    var BusinessIdentityService_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.shopping.merchant.accounts.v1beta.BusinessIdentityService",
    	HandlerType: (*BusinessIdentityServiceServer)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "GetBusinessIdentity",
    			Handler:    _BusinessIdentityService_GetBusinessIdentity_Handler,
    		},
    		{
    			MethodName: "UpdateBusinessIdentity",
    			Handler:    _BusinessIdentityService_UpdateBusinessIdentity_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/shopping/merchant/accounts/v1beta/businessidentity.proto",
    }

BusinessIdentityService_ServiceDesc is the grpc.ServiceDesc for BusinessIdentityService service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

### BusinessInfoService_ServiceDesc
    
    
    var BusinessInfoService_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.shopping.merchant.accounts.v1beta.BusinessInfoService",
    	HandlerType: (*BusinessInfoServiceServer)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "GetBusinessInfo",
    			Handler:    _BusinessInfoService_GetBusinessInfo_Handler,
    		},
    		{
    			MethodName: "UpdateBusinessInfo",
    			Handler:    _BusinessInfoService_UpdateBusinessInfo_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/shopping/merchant/accounts/v1beta/businessinfo.proto",
    }

BusinessInfoService_ServiceDesc is the grpc.ServiceDesc for BusinessInfoService service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

### CheckoutSettingsService_ServiceDesc
    
    
    var CheckoutSettingsService_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.shopping.merchant.accounts.v1beta.CheckoutSettingsService",
    	HandlerType: (*CheckoutSettingsServiceServer)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "GetCheckoutSettings",
    			Handler:    _CheckoutSettingsService_GetCheckoutSettings_Handler,
    		},
    		{
    			MethodName: "CreateCheckoutSettings",
    			Handler:    _CheckoutSettingsService_CreateCheckoutSettings_Handler,
    		},
    		{
    			MethodName: "UpdateCheckoutSettings",
    			Handler:    _CheckoutSettingsService_UpdateCheckoutSettings_Handler,
    		},
    		{
    			MethodName: "DeleteCheckoutSettings",
    			Handler:    _CheckoutSettingsService_DeleteCheckoutSettings_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/shopping/merchant/accounts/v1beta/checkoutsettings.proto",
    }

CheckoutSettingsService_ServiceDesc is the grpc.ServiceDesc for CheckoutSettingsService service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

### EmailPreferencesService_ServiceDesc
    
    
    var EmailPreferencesService_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.shopping.merchant.accounts.v1beta.EmailPreferencesService",
    	HandlerType: (*EmailPreferencesServiceServer)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "GetEmailPreferences",
    			Handler:    _EmailPreferencesService_GetEmailPreferences_Handler,
    		},
    		{
    			MethodName: "UpdateEmailPreferences",
    			Handler:    _EmailPreferencesService_UpdateEmailPreferences_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/shopping/merchant/accounts/v1beta/emailpreferences.proto",
    }

EmailPreferencesService_ServiceDesc is the grpc.ServiceDesc for EmailPreferencesService service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

### File_google_shopping_merchant_accounts_v1beta_accessright_proto
    
    
    var File_google_shopping_merchant_accounts_v1beta_accessright_proto protoreflect.FileDescriptor

### File_google_shopping_merchant_accounts_v1beta_account_tax_proto
    
    
    var File_google_shopping_merchant_accounts_v1beta_account_tax_proto protoreflect.FileDescriptor

### File_google_shopping_merchant_accounts_v1beta_accountissue_proto
    
    
    var File_google_shopping_merchant_accounts_v1beta_accountissue_proto protoreflect.FileDescriptor

### File_google_shopping_merchant_accounts_v1beta_accounts_proto
    
    
    var File_google_shopping_merchant_accounts_v1beta_accounts_proto protoreflect.FileDescriptor

### File_google_shopping_merchant_accounts_v1beta_accountservices_proto
    
    
    var File_google_shopping_merchant_accounts_v1beta_accountservices_proto protoreflect.FileDescriptor

### File_google_shopping_merchant_accounts_v1beta_autofeedsettings_proto
    
    
    var File_google_shopping_merchant_accounts_v1beta_autofeedsettings_proto protoreflect.FileDescriptor

### File_google_shopping_merchant_accounts_v1beta_automaticimprovements_proto
    
    
    var File_google_shopping_merchant_accounts_v1beta_automaticimprovements_proto protoreflect.FileDescriptor

### File_google_shopping_merchant_accounts_v1beta_businessidentity_proto
    
    
    var File_google_shopping_merchant_accounts_v1beta_businessidentity_proto protoreflect.FileDescriptor

### File_google_shopping_merchant_accounts_v1beta_businessinfo_proto
    
    
    var File_google_shopping_merchant_accounts_v1beta_businessinfo_proto protoreflect.FileDescriptor

### File_google_shopping_merchant_accounts_v1beta_checkoutsettings_proto
    
    
    var File_google_shopping_merchant_accounts_v1beta_checkoutsettings_proto protoreflect.FileDescriptor

### File_google_shopping_merchant_accounts_v1beta_customerservice_proto
    
    
    var File_google_shopping_merchant_accounts_v1beta_customerservice_proto protoreflect.FileDescriptor

### File_google_shopping_merchant_accounts_v1beta_emailpreferences_proto
    
    
    var File_google_shopping_merchant_accounts_v1beta_emailpreferences_proto protoreflect.FileDescriptor

### File_google_shopping_merchant_accounts_v1beta_gbpaccounts_proto
    
    
    var File_google_shopping_merchant_accounts_v1beta_gbpaccounts_proto protoreflect.FileDescriptor

### File_google_shopping_merchant_accounts_v1beta_homepage_proto
    
    
    var File_google_shopping_merchant_accounts_v1beta_homepage_proto protoreflect.FileDescriptor

### File_google_shopping_merchant_accounts_v1beta_lfpproviders_proto
    
    
    var File_google_shopping_merchant_accounts_v1beta_lfpproviders_proto protoreflect.FileDescriptor

### File_google_shopping_merchant_accounts_v1beta_omnichannelsettings_proto
    
    
    var File_google_shopping_merchant_accounts_v1beta_omnichannelsettings_proto protoreflect.FileDescriptor

### File_google_shopping_merchant_accounts_v1beta_online_return_policy_proto
    
    
    var File_google_shopping_merchant_accounts_v1beta_online_return_policy_proto protoreflect.FileDescriptor

### File_google_shopping_merchant_accounts_v1beta_phoneverificationstate_proto
    
    
    var File_google_shopping_merchant_accounts_v1beta_phoneverificationstate_proto protoreflect.FileDescriptor

### File_google_shopping_merchant_accounts_v1beta_programs_proto
    
    
    var File_google_shopping_merchant_accounts_v1beta_programs_proto protoreflect.FileDescriptor

### File_google_shopping_merchant_accounts_v1beta_regions_proto
    
    
    var File_google_shopping_merchant_accounts_v1beta_regions_proto protoreflect.FileDescriptor

### File_google_shopping_merchant_accounts_v1beta_shippingsettings_proto
    
    
    var File_google_shopping_merchant_accounts_v1beta_shippingsettings_proto protoreflect.FileDescriptor

### File_google_shopping_merchant_accounts_v1beta_tax_rule_proto
    
    
    var File_google_shopping_merchant_accounts_v1beta_tax_rule_proto protoreflect.FileDescriptor

### File_google_shopping_merchant_accounts_v1beta_termsofservice_proto
    
    
    var File_google_shopping_merchant_accounts_v1beta_termsofservice_proto protoreflect.FileDescriptor

### File_google_shopping_merchant_accounts_v1beta_termsofserviceagreementstate_proto
    
    
    var File_google_shopping_merchant_accounts_v1beta_termsofserviceagreementstate_proto protoreflect.FileDescriptor

### File_google_shopping_merchant_accounts_v1beta_termsofservicekind_proto
    
    
    var File_google_shopping_merchant_accounts_v1beta_termsofservicekind_proto protoreflect.FileDescriptor

### File_google_shopping_merchant_accounts_v1beta_user_proto
    
    
    var File_google_shopping_merchant_accounts_v1beta_user_proto protoreflect.FileDescriptor

### File_google_shopping_merchant_accounts_v1beta_verificationmailsettings_proto
    
    
    var File_google_shopping_merchant_accounts_v1beta_verificationmailsettings_proto protoreflect.FileDescriptor

### GbpAccountsService_ServiceDesc
    
    
    var GbpAccountsService_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.shopping.merchant.accounts.v1beta.GbpAccountsService",
    	HandlerType: (*GbpAccountsServiceServer)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "ListGbpAccounts",
    			Handler:    _GbpAccountsService_ListGbpAccounts_Handler,
    		},
    		{
    			MethodName: "LinkGbpAccount",
    			Handler:    _GbpAccountsService_LinkGbpAccount_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/shopping/merchant/accounts/v1beta/gbpaccounts.proto",
    }

GbpAccountsService_ServiceDesc is the grpc.ServiceDesc for GbpAccountsService service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

### HomepageService_ServiceDesc
    
    
    var HomepageService_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.shopping.merchant.accounts.v1beta.HomepageService",
    	HandlerType: (*HomepageServiceServer)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "GetHomepage",
    			Handler:    _HomepageService_GetHomepage_Handler,
    		},
    		{
    			MethodName: "UpdateHomepage",
    			Handler:    _HomepageService_UpdateHomepage_Handler,
    		},
    		{
    			MethodName: "ClaimHomepage",
    			Handler:    _HomepageService_ClaimHomepage_Handler,
    		},
    		{
    			MethodName: "UnclaimHomepage",
    			Handler:    _HomepageService_UnclaimHomepage_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/shopping/merchant/accounts/v1beta/homepage.proto",
    }

HomepageService_ServiceDesc is the grpc.ServiceDesc for HomepageService service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

### LfpProvidersService_ServiceDesc
    
    
    var LfpProvidersService_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.shopping.merchant.accounts.v1beta.LfpProvidersService",
    	HandlerType: (*LfpProvidersServiceServer)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "FindLfpProviders",
    			Handler:    _LfpProvidersService_FindLfpProviders_Handler,
    		},
    		{
    			MethodName: "LinkLfpProvider",
    			Handler:    _LfpProvidersService_LinkLfpProvider_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/shopping/merchant/accounts/v1beta/lfpproviders.proto",
    }

LfpProvidersService_ServiceDesc is the grpc.ServiceDesc for LfpProvidersService service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

### OmnichannelSettingsService_ServiceDesc
    
    
    var OmnichannelSettingsService_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.shopping.merchant.accounts.v1beta.OmnichannelSettingsService",
    	HandlerType: (*OmnichannelSettingsServiceServer)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "GetOmnichannelSetting",
    			Handler:    _OmnichannelSettingsService_GetOmnichannelSetting_Handler,
    		},
    		{
    			MethodName: "ListOmnichannelSettings",
    			Handler:    _OmnichannelSettingsService_ListOmnichannelSettings_Handler,
    		},
    		{
    			MethodName: "CreateOmnichannelSetting",
    			Handler:    _OmnichannelSettingsService_CreateOmnichannelSetting_Handler,
    		},
    		{
    			MethodName: "UpdateOmnichannelSetting",
    			Handler:    _OmnichannelSettingsService_UpdateOmnichannelSetting_Handler,
    		},
    		{
    			MethodName: "RequestInventoryVerification",
    			Handler:    _OmnichannelSettingsService_RequestInventoryVerification_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/shopping/merchant/accounts/v1beta/omnichannelsettings.proto",
    }

OmnichannelSettingsService_ServiceDesc is the grpc.ServiceDesc for OmnichannelSettingsService service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

### OnlineReturnPolicyService_ServiceDesc
    
    
    var OnlineReturnPolicyService_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.shopping.merchant.accounts.v1beta.OnlineReturnPolicyService",
    	HandlerType: (*OnlineReturnPolicyServiceServer)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "GetOnlineReturnPolicy",
    			Handler:    _OnlineReturnPolicyService_GetOnlineReturnPolicy_Handler,
    		},
    		{
    			MethodName: "ListOnlineReturnPolicies",
    			Handler:    _OnlineReturnPolicyService_ListOnlineReturnPolicies_Handler,
    		},
    		{
    			MethodName: "CreateOnlineReturnPolicy",
    			Handler:    _OnlineReturnPolicyService_CreateOnlineReturnPolicy_Handler,
    		},
    		{
    			MethodName: "UpdateOnlineReturnPolicy",
    			Handler:    _OnlineReturnPolicyService_UpdateOnlineReturnPolicy_Handler,
    		},
    		{
    			MethodName: "DeleteOnlineReturnPolicy",
    			Handler:    _OnlineReturnPolicyService_DeleteOnlineReturnPolicy_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/shopping/merchant/accounts/v1beta/online_return_policy.proto",
    }

OnlineReturnPolicyService_ServiceDesc is the grpc.ServiceDesc for OnlineReturnPolicyService service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

### ProgramsService_ServiceDesc
    
    
    var ProgramsService_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.shopping.merchant.accounts.v1beta.ProgramsService",
    	HandlerType: (*ProgramsServiceServer)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "GetProgram",
    			Handler:    _ProgramsService_GetProgram_Handler,
    		},
    		{
    			MethodName: "ListPrograms",
    			Handler:    _ProgramsService_ListPrograms_Handler,
    		},
    		{
    			MethodName: "EnableProgram",
    			Handler:    _ProgramsService_EnableProgram_Handler,
    		},
    		{
    			MethodName: "DisableProgram",
    			Handler:    _ProgramsService_DisableProgram_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/shopping/merchant/accounts/v1beta/programs.proto",
    }

ProgramsService_ServiceDesc is the grpc.ServiceDesc for ProgramsService service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

### RegionsService_ServiceDesc
    
    
    var RegionsService_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.shopping.merchant.accounts.v1beta.RegionsService",
    	HandlerType: (*RegionsServiceServer)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "GetRegion",
    			Handler:    _RegionsService_GetRegion_Handler,
    		},
    		{
    			MethodName: "CreateRegion",
    			Handler:    _RegionsService_CreateRegion_Handler,
    		},
    		{
    			MethodName: "UpdateRegion",
    			Handler:    _RegionsService_UpdateRegion_Handler,
    		},
    		{
    			MethodName: "DeleteRegion",
    			Handler:    _RegionsService_DeleteRegion_Handler,
    		},
    		{
    			MethodName: "ListRegions",
    			Handler:    _RegionsService_ListRegions_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/shopping/merchant/accounts/v1beta/regions.proto",
    }

RegionsService_ServiceDesc is the grpc.ServiceDesc for RegionsService service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

### ShippingSettingsService_ServiceDesc
    
    
    var ShippingSettingsService_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.shopping.merchant.accounts.v1beta.ShippingSettingsService",
    	HandlerType: (*ShippingSettingsServiceServer)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "GetShippingSettings",
    			Handler:    _ShippingSettingsService_GetShippingSettings_Handler,
    		},
    		{
    			MethodName: "InsertShippingSettings",
    			Handler:    _ShippingSettingsService_InsertShippingSettings_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/shopping/merchant/accounts/v1beta/shippingsettings.proto",
    }

ShippingSettingsService_ServiceDesc is the grpc.ServiceDesc for ShippingSettingsService service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

### TermsOfServiceAgreementStateService_ServiceDesc
    
    
    var TermsOfServiceAgreementStateService_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.shopping.merchant.accounts.v1beta.TermsOfServiceAgreementStateService",
    	HandlerType: (*TermsOfServiceAgreementStateServiceServer)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "GetTermsOfServiceAgreementState",
    			Handler:    _TermsOfServiceAgreementStateService_GetTermsOfServiceAgreementState_Handler,
    		},
    		{
    			MethodName: "RetrieveForApplicationTermsOfServiceAgreementState",
    			Handler:    _TermsOfServiceAgreementStateService_RetrieveForApplicationTermsOfServiceAgreementState_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/shopping/merchant/accounts/v1beta/termsofserviceagreementstate.proto",
    }

TermsOfServiceAgreementStateService_ServiceDesc is the grpc.ServiceDesc for TermsOfServiceAgreementStateService service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

### TermsOfServiceService_ServiceDesc
    
    
    var TermsOfServiceService_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.shopping.merchant.accounts.v1beta.TermsOfServiceService",
    	HandlerType: (*TermsOfServiceServiceServer)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "GetTermsOfService",
    			Handler:    _TermsOfServiceService_GetTermsOfService_Handler,
    		},
    		{
    			MethodName: "RetrieveLatestTermsOfService",
    			Handler:    _TermsOfServiceService_RetrieveLatestTermsOfService_Handler,
    		},
    		{
    			MethodName: "AcceptTermsOfService",
    			Handler:    _TermsOfServiceService_AcceptTermsOfService_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/shopping/merchant/accounts/v1beta/termsofservice.proto",
    }

TermsOfServiceService_ServiceDesc is the grpc.ServiceDesc for TermsOfServiceService service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

### UserService_ServiceDesc
    
    
    var UserService_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.shopping.merchant.accounts.v1beta.UserService",
    	HandlerType: (*UserServiceServer)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "GetUser",
    			Handler:    _UserService_GetUser_Handler,
    		},
    		{
    			MethodName: "CreateUser",
    			Handler:    _UserService_CreateUser_Handler,
    		},
    		{
    			MethodName: "DeleteUser",
    			Handler:    _UserService_DeleteUser_Handler,
    		},
    		{
    			MethodName: "UpdateUser",
    			Handler:    _UserService_UpdateUser_Handler,
    		},
    		{
    			MethodName: "ListUsers",
    			Handler:    _UserService_ListUsers_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/shopping/merchant/accounts/v1beta/user.proto",
    }

UserService_ServiceDesc is the grpc.ServiceDesc for UserService service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

## Functions 

### func RegisterAccountIssueServiceServer 
    
    
    func RegisterAccountIssueServiceServer(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv AccountIssueServiceServer)

### func RegisterAccountTaxServiceServer 
    
    
    func RegisterAccountTaxServiceServer(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv AccountTaxServiceServer)

### func RegisterAccountsServiceServer 
    
    
    func RegisterAccountsServiceServer(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv AccountsServiceServer)

### func RegisterAutofeedSettingsServiceServer 
    
    
    func RegisterAutofeedSettingsServiceServer(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv AutofeedSettingsServiceServer)

### func RegisterAutomaticImprovementsServiceServer 
    
    
    func RegisterAutomaticImprovementsServiceServer(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv AutomaticImprovementsServiceServer)

### func RegisterBusinessIdentityServiceServer 
    
    
    func RegisterBusinessIdentityServiceServer(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv BusinessIdentityServiceServer)

### func RegisterBusinessInfoServiceServer 
    
    
    func RegisterBusinessInfoServiceServer(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv BusinessInfoServiceServer)

### func RegisterCheckoutSettingsServiceServer 
    
    
    func RegisterCheckoutSettingsServiceServer(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv CheckoutSettingsServiceServer)

### func RegisterEmailPreferencesServiceServer 
    
    
    func RegisterEmailPreferencesServiceServer(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv EmailPreferencesServiceServer)

### func RegisterGbpAccountsServiceServer 
    
    
    func RegisterGbpAccountsServiceServer(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv GbpAccountsServiceServer)

### func RegisterHomepageServiceServer 
    
    
    func RegisterHomepageServiceServer(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv HomepageServiceServer)

### func RegisterLfpProvidersServiceServer 
    
    
    func RegisterLfpProvidersServiceServer(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv LfpProvidersServiceServer)

### func RegisterOmnichannelSettingsServiceServer 
    
    
    func RegisterOmnichannelSettingsServiceServer(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv OmnichannelSettingsServiceServer)

### func RegisterOnlineReturnPolicyServiceServer 
    
    
    func RegisterOnlineReturnPolicyServiceServer(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv OnlineReturnPolicyServiceServer)

### func RegisterProgramsServiceServer 
    
    
    func RegisterProgramsServiceServer(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv ProgramsServiceServer)

### func RegisterRegionsServiceServer 
    
    
    func RegisterRegionsServiceServer(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv RegionsServiceServer)

### func RegisterShippingSettingsServiceServer 
    
    
    func RegisterShippingSettingsServiceServer(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv ShippingSettingsServiceServer)

### func RegisterTermsOfServiceAgreementStateServiceServer 
    
    
    func RegisterTermsOfServiceAgreementStateServiceServer(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv TermsOfServiceAgreementStateServiceServer)

### func RegisterTermsOfServiceServiceServer 
    
    
    func RegisterTermsOfServiceServiceServer(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv TermsOfServiceServiceServer)

### func RegisterUserServiceServer 
    
    
    func RegisterUserServiceServer(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv UserServiceServer)

## About
    
    
    type About struct {
    
    	// Required. The about page URI.
    	Uri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=uri,proto3" json:"uri,omitempty"`
    	// Output only. The state of the URI.
    	State ReviewState_State `protobuf:"varint,2,opt,name=state,proto3,enum=google.shopping.merchant.accounts.v1beta.ReviewState_State" json:"state,omitempty"`
    	// contains filtered or unexported fields
    }

Collection of information related to the about page ([impressum](https://support.google.com/merchants/answer/14675634?hl=en&ref_topic=15145634&sjid=6892280366904591178-NC)).

### func (*About) Descriptor 
    
    
    func (*About) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use About.ProtoReflect.Descriptor instead.

### func (*About) GetState 
    
    
    func (x *About) GetState() ReviewState_State

### func (*About) GetUri 
    
    
    func (x *About) GetUri() [string](https://pkg.go.dev/builtin#string)

### func (*About) ProtoMessage 
    
    
    func (*About) ProtoMessage()

### func (*About) ProtoReflect 
    
    
    func (x *About) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*About) Reset 
    
    
    func (x *About) Reset()

### func (*About) String 
    
    
    func (x *About) String() [string](https://pkg.go.dev/builtin#string)

## AcceptTermsOfServiceRequest
    
    
    type AcceptTermsOfServiceRequest struct {
    
    	// Required. The resource name of the terms of service version.
    	// Format: `termsOfService/{version}`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Required. The account for which to accept the ToS.
    	Account [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=account,proto3" json:"account,omitempty"`
    	// Required. Region code as defined by [CLDR](https://cldr.unicode.org/). This
    	// is either a country when the ToS applies specifically to that country or
    	// 001 when it applies globally.
    	RegionCode [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=region_code,json=regionCode,proto3" json:"region_code,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the `AcceptTermsOfService` method.

### func (*AcceptTermsOfServiceRequest) Descriptor 
    
    
    func (*AcceptTermsOfServiceRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AcceptTermsOfServiceRequest.ProtoReflect.Descriptor instead.

### func (*AcceptTermsOfServiceRequest) GetAccount 
    
    
    func (x *AcceptTermsOfServiceRequest) GetAccount() [string](https://pkg.go.dev/builtin#string)

### func (*AcceptTermsOfServiceRequest) GetName 
    
    
    func (x *AcceptTermsOfServiceRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*AcceptTermsOfServiceRequest) GetRegionCode 
    
    
    func (x *AcceptTermsOfServiceRequest) GetRegionCode() [string](https://pkg.go.dev/builtin#string)

### func (*AcceptTermsOfServiceRequest) ProtoMessage 
    
    
    func (*AcceptTermsOfServiceRequest) ProtoMessage()

### func (*AcceptTermsOfServiceRequest) ProtoReflect 
    
    
    func (x *AcceptTermsOfServiceRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AcceptTermsOfServiceRequest) Reset 
    
    
    func (x *AcceptTermsOfServiceRequest) Reset()

### func (*AcceptTermsOfServiceRequest) String 
    
    
    func (x *AcceptTermsOfServiceRequest) String() [string](https://pkg.go.dev/builtin#string)

## Accepted
    
    
    type Accepted struct {
    
    	// The accepted
    	// [termsOfService](google.shopping.merchant.accounts.v1main.TermsOfService).
    	TermsOfService [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=terms_of_service,json=termsOfService,proto3" json:"terms_of_service,omitempty"`
    	// The account where the acceptance was recorded. This can be the account
    	// itself or, in the case of subaccounts, the MCA account.
    	AcceptedBy [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=accepted_by,json=acceptedBy,proto3" json:"accepted_by,omitempty"`
    	// When set, it states that the accepted
    	// [TermsOfService](google.shopping.merchant.accounts.v1main.TermsOfService)
    	// is only valid until the end of this date (in UTC). A new one must be
    	// accepted before then. The information of the required
    	// [TermsOfService](google.shopping.merchant.accounts.v1main.TermsOfService)
    	// is found in the [Required](Required) message.
    	ValidUntil *date.Date `protobuf:"bytes,3,opt,name=valid_until,json=validUntil,proto3,oneof" json:"valid_until,omitempty"`
    	// contains filtered or unexported fields
    }

Describes the accepted terms of service.

### func (*Accepted) Descriptor 
    
    
    func (*Accepted) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Accepted.ProtoReflect.Descriptor instead.

### func (*Accepted) GetAcceptedBy 
    
    
    func (x *Accepted) GetAcceptedBy() [string](https://pkg.go.dev/builtin#string)

### func (*Accepted) GetTermsOfService 
    
    
    func (x *Accepted) GetTermsOfService() [string](https://pkg.go.dev/builtin#string)

### func (*Accepted) GetValidUntil 
    
    
    func (x *Accepted) GetValidUntil() *[date](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/date).[Date](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/date#Date)

### func (*Accepted) ProtoMessage 
    
    
    func (*Accepted) ProtoMessage()

### func (*Accepted) ProtoReflect 
    
    
    func (x *Accepted) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Accepted) Reset 
    
    
    func (x *Accepted) Reset()

### func (*Accepted) String 
    
    
    func (x *Accepted) String() [string](https://pkg.go.dev/builtin#string)

## AccessRight
    
    
    type AccessRight [int32](https://pkg.go.dev/builtin#int32)

The access right.

### AccessRight_ACCESS_RIGHT_UNSPECIFIED, AccessRight_STANDARD, AccessRight_ADMIN, AccessRight_PERFORMANCE_REPORTING
    
    
    const (
    	// Default value. This value is unused.
    	AccessRight_ACCESS_RIGHT_UNSPECIFIED AccessRight = 0
    	// Standard access rights.
    	AccessRight_STANDARD AccessRight = 1
    	// Admin access rights.
    	AccessRight_ADMIN AccessRight = 2
    	// Users with this right have access to performance and insights.
    	AccessRight_PERFORMANCE_REPORTING AccessRight = 3
    )

### func (AccessRight) Descriptor 
    
    
    func (AccessRight) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (AccessRight) Enum 
    
    
    func (x AccessRight) Enum() *AccessRight

### func (AccessRight) EnumDescriptor 
    
    
    func (AccessRight) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AccessRight.Descriptor instead.

### func (AccessRight) Number 
    
    
    func (x AccessRight) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (AccessRight) String 
    
    
    func (x AccessRight) String() [string](https://pkg.go.dev/builtin#string)

### func (AccessRight) Type 
    
    
    func (AccessRight) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Account
    
    
    type Account struct {
    
    	// Identifier. The resource name of the account.
    	// Format: `accounts/{account}`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Output only. The ID of the account.
    	AccountId [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,2,opt,name=account_id,json=accountId,proto3" json:"account_id,omitempty"`
    	// Required. A human-readable name of the account. See
    	// [store name](https://support.google.com/merchants/answer/160556) and
    	// [business name](https://support.google.com/merchants/answer/12159159) for
    	// more information.
    	AccountName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=account_name,json=accountName,proto3" json:"account_name,omitempty"`
    	// Whether this account contains adult content.
    	AdultContent [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,4,opt,name=adult_content,json=adultContent,proto3" json:"adult_content,omitempty"`
    	// Output only. Whether this is a test account.
    	TestAccount [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,5,opt,name=test_account,json=testAccount,proto3" json:"test_account,omitempty"`
    	// Required. The time zone of the account.
    	//
    	// On writes, `time_zone` sets both the `reporting_time_zone` and the
    	// `display_time_zone`.
    	//
    	// For reads, `time_zone` always returns the `display_time_zone`. If
    	// `display_time_zone` doesn't exist for your account, `time_zone` is empty.
    	TimeZone *datetime.TimeZone `protobuf:"bytes,6,opt,name=time_zone,json=timeZone,proto3" json:"time_zone,omitempty"`
    	// Required. The account's [BCP-47 language
    	// code](https://tools.ietf.org/html/bcp47), such as `en-US` or `sr-Latn`.
    	LanguageCode [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,7,opt,name=language_code,json=languageCode,proto3" json:"language_code,omitempty"`
    	// contains filtered or unexported fields
    }

An account.

### func (*Account) Descriptor 
    
    
    func (*Account) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Account.ProtoReflect.Descriptor instead.

### func (*Account) GetAccountId 
    
    
    func (x *Account) GetAccountId() [int64](https://pkg.go.dev/builtin#int64)

### func (*Account) GetAccountName 
    
    
    func (x *Account) GetAccountName() [string](https://pkg.go.dev/builtin#string)

### func (*Account) GetAdultContent 
    
    
    func (x *Account) GetAdultContent() [bool](https://pkg.go.dev/builtin#bool)

### func (*Account) GetLanguageCode 
    
    
    func (x *Account) GetLanguageCode() [string](https://pkg.go.dev/builtin#string)

### func (*Account) GetName 
    
    
    func (x *Account) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Account) GetTestAccount 
    
    
    func (x *Account) GetTestAccount() [bool](https://pkg.go.dev/builtin#bool)

### func (*Account) GetTimeZone 
    
    
    func (x *Account) GetTimeZone() *[datetime](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/datetime).[TimeZone](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/datetime#TimeZone)

### func (*Account) ProtoMessage 
    
    
    func (*Account) ProtoMessage()

### func (*Account) ProtoReflect 
    
    
    func (x *Account) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Account) Reset 
    
    
    func (x *Account) Reset()

### func (*Account) String 
    
    
    func (x *Account) String() [string](https://pkg.go.dev/builtin#string)

## AccountAggregation
    
    
    type AccountAggregation struct {
    	// contains filtered or unexported fields
    }

`AccountAggregation` payload.

### func (*AccountAggregation) Descriptor 
    
    
    func (*AccountAggregation) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AccountAggregation.ProtoReflect.Descriptor instead.

### func (*AccountAggregation) ProtoMessage 
    
    
    func (*AccountAggregation) ProtoMessage()

### func (*AccountAggregation) ProtoReflect 
    
    
    func (x *AccountAggregation) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AccountAggregation) Reset 
    
    
    func (x *AccountAggregation) Reset()

### func (*AccountAggregation) String 
    
    
    func (x *AccountAggregation) String() [string](https://pkg.go.dev/builtin#string)

## AccountIssue
    
    
    type AccountIssue struct {
    
    	// Identifier. The resource name of the account issue.
    	// Format: `accounts/{account}/issues/{id}`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// The localized title of the issue.
    	Title [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=title,proto3" json:"title,omitempty"`
    	// The overall severity of the issue.
    	Severity AccountIssue_Severity `protobuf:"varint,3,opt,name=severity,proto3,enum=google.shopping.merchant.accounts.v1beta.AccountIssue_Severity" json:"severity,omitempty"`
    	// The impact this issue has on various destinations.
    	ImpactedDestinations []*AccountIssue_ImpactedDestination `protobuf:"bytes,4,rep,name=impacted_destinations,json=impactedDestinations,proto3" json:"impacted_destinations,omitempty"`
    	// Further localized details about the issue.
    	Detail [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=detail,proto3" json:"detail,omitempty"`
    	// Link to Merchant Center Help Center providing further information about the
    	// issue and how to fix it.
    	DocumentationUri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,6,opt,name=documentation_uri,json=documentationUri,proto3" json:"documentation_uri,omitempty"`
    	// contains filtered or unexported fields
    }

An [`AccountIssue`](https://support.google.com/merchants/answer/12153802?sjid=17798438912526418908-EU#account).

### func (*AccountIssue) Descriptor 
    
    
    func (*AccountIssue) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AccountIssue.ProtoReflect.Descriptor instead.

### func (*AccountIssue) GetDetail 
    
    
    func (x *AccountIssue) GetDetail() [string](https://pkg.go.dev/builtin#string)

### func (*AccountIssue) GetDocumentationUri 
    
    
    func (x *AccountIssue) GetDocumentationUri() [string](https://pkg.go.dev/builtin#string)

### func (*AccountIssue) GetImpactedDestinations 
    
    
    func (x *AccountIssue) GetImpactedDestinations() []*AccountIssue_ImpactedDestination

### func (*AccountIssue) GetName 
    
    
    func (x *AccountIssue) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*AccountIssue) GetSeverity 
    
    
    func (x *AccountIssue) GetSeverity() AccountIssue_Severity

### func (*AccountIssue) GetTitle 
    
    
    func (x *AccountIssue) GetTitle() [string](https://pkg.go.dev/builtin#string)

### func (*AccountIssue) ProtoMessage 
    
    
    func (*AccountIssue) ProtoMessage()

### func (*AccountIssue) ProtoReflect 
    
    
    func (x *AccountIssue) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AccountIssue) Reset 
    
    
    func (x *AccountIssue) Reset()

### func (*AccountIssue) String 
    
    
    func (x *AccountIssue) String() [string](https://pkg.go.dev/builtin#string)

## AccountIssueServiceClient
    
    
    type AccountIssueServiceClient interface {
    	// Lists all account issues of a Merchant Center account.
    	ListAccountIssues(ctx context.Context, in *ListAccountIssuesRequest, opts ...grpc.CallOption) (*ListAccountIssuesResponse, [error](https://pkg.go.dev/builtin#error))
    }

AccountIssueServiceClient is the client API for AccountIssueService service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

### func NewAccountIssueServiceClient 
    
    
    func NewAccountIssueServiceClient(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) AccountIssueServiceClient

## AccountIssueServiceServer
    
    
    type AccountIssueServiceServer interface {
    	// Lists all account issues of a Merchant Center account.
    	ListAccountIssues(context.Context, *ListAccountIssuesRequest) (*ListAccountIssuesResponse, [error](https://pkg.go.dev/builtin#error))
    }

AccountIssueServiceServer is the server API for AccountIssueService service. All implementations should embed UnimplementedAccountIssueServiceServer for forward compatibility

## AccountIssue_ImpactedDestination
    
    
    type AccountIssue_ImpactedDestination struct {
    
    	// The impacted reporting context.
    	ReportingContext *typepb.ReportingContext_ReportingContextEnum `protobuf:"varint,1,opt,name=reporting_context,json=reportingContext,proto3,enum=google.shopping.type.ReportingContext_ReportingContextEnum,oneof" json:"reporting_context,omitempty"`
    	// The (negative) impact for various regions on the given destination.
    	Impacts []*AccountIssue_ImpactedDestination_Impact `protobuf:"bytes,2,rep,name=impacts,proto3" json:"impacts,omitempty"`
    	// contains filtered or unexported fields
    }

The impact of the issue on a destination.

### func (*AccountIssue_ImpactedDestination) Descriptor 
    
    
    func (*AccountIssue_ImpactedDestination) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AccountIssue_ImpactedDestination.ProtoReflect.Descriptor instead.

### func (*AccountIssue_ImpactedDestination) GetImpacts 
    
    
    func (x *AccountIssue_ImpactedDestination) GetImpacts() []*AccountIssue_ImpactedDestination_Impact

### func (*AccountIssue_ImpactedDestination) GetReportingContext 
    
    
    func (x *AccountIssue_ImpactedDestination) GetReportingContext() [typepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/type/typepb).[ReportingContext_ReportingContextEnum](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/type/typepb#cloud_google_com_go_shopping_type_typepb_ReportingContext_ReportingContextEnum)

### func (*AccountIssue_ImpactedDestination) ProtoMessage 
    
    
    func (*AccountIssue_ImpactedDestination) ProtoMessage()

### func (*AccountIssue_ImpactedDestination) ProtoReflect 
    
    
    func (x *AccountIssue_ImpactedDestination) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AccountIssue_ImpactedDestination) Reset 
    
    
    func (x *AccountIssue_ImpactedDestination) Reset()

### func (*AccountIssue_ImpactedDestination) String 
    
    
    func (x *AccountIssue_ImpactedDestination) String() [string](https://pkg.go.dev/builtin#string)

## AccountIssue_ImpactedDestination_Impact
    
    
    type AccountIssue_ImpactedDestination_Impact struct {
    
    	// The [CLDR region code](https://cldr.unicode.org/) where this issue
    	// applies.
    	RegionCode [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=region_code,json=regionCode,proto3" json:"region_code,omitempty"`
    	// The severity of the issue on the destination and region.
    	Severity AccountIssue_Severity `protobuf:"varint,2,opt,name=severity,proto3,enum=google.shopping.merchant.accounts.v1beta.AccountIssue_Severity" json:"severity,omitempty"`
    	// contains filtered or unexported fields
    }

The impact of the issue on a region.

### func (*AccountIssue_ImpactedDestination_Impact) Descriptor 
    
    
    func (*AccountIssue_ImpactedDestination_Impact) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AccountIssue_ImpactedDestination_Impact.ProtoReflect.Descriptor instead.

### func (*AccountIssue_ImpactedDestination_Impact) GetRegionCode 
    
    
    func (x *AccountIssue_ImpactedDestination_Impact) GetRegionCode() [string](https://pkg.go.dev/builtin#string)

### func (*AccountIssue_ImpactedDestination_Impact) GetSeverity 
    
    
    func (x *AccountIssue_ImpactedDestination_Impact) GetSeverity() AccountIssue_Severity

### func (*AccountIssue_ImpactedDestination_Impact) ProtoMessage 
    
    
    func (*AccountIssue_ImpactedDestination_Impact) ProtoMessage()

### func (*AccountIssue_ImpactedDestination_Impact) ProtoReflect 
    
    
    func (x *AccountIssue_ImpactedDestination_Impact) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AccountIssue_ImpactedDestination_Impact) Reset 
    
    
    func (x *AccountIssue_ImpactedDestination_Impact) Reset()

### func (*AccountIssue_ImpactedDestination_Impact) String 
    
    
    func (x *AccountIssue_ImpactedDestination_Impact) String() [string](https://pkg.go.dev/builtin#string)

## AccountIssue_Severity
    
    
    type AccountIssue_Severity [int32](https://pkg.go.dev/builtin#int32)

All possible issue severities.

### AccountIssue_SEVERITY_UNSPECIFIED, AccountIssue_CRITICAL, AccountIssue_ERROR, AccountIssue_SUGGESTION
    
    
    const (
    	// The severity is unknown.
    	AccountIssue_SEVERITY_UNSPECIFIED AccountIssue_Severity = 0
    	// The issue causes offers to not serve.
    	AccountIssue_CRITICAL AccountIssue_Severity = 1
    	// The issue might affect offers (in the future) or might be an
    	// indicator of issues with offers.
    	AccountIssue_ERROR AccountIssue_Severity = 2
    	// The issue is a suggestion for improvement.
    	AccountIssue_SUGGESTION AccountIssue_Severity = 3
    )

### func (AccountIssue_Severity) Descriptor 
    
    
    func (AccountIssue_Severity) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (AccountIssue_Severity) Enum 
    
    
    func (x AccountIssue_Severity) Enum() *AccountIssue_Severity

### func (AccountIssue_Severity) EnumDescriptor 
    
    
    func (AccountIssue_Severity) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AccountIssue_Severity.Descriptor instead.

### func (AccountIssue_Severity) Number 
    
    
    func (x AccountIssue_Severity) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (AccountIssue_Severity) String 
    
    
    func (x AccountIssue_Severity) String() [string](https://pkg.go.dev/builtin#string)

### func (AccountIssue_Severity) Type 
    
    
    func (AccountIssue_Severity) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## AccountTax
    
    
    type AccountTax struct {
    
    	// Identifier. The name of the tax setting.
    	// Format:
    	// "{account_tax.name=accounts/{account}}"
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Output only. The ID of the account to which these account tax settings
    	// belong.
    	Account [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,2,opt,name=account,proto3" json:"account,omitempty"`
    	// Tax rules. "Define the tax rules in each region.
    	// No tax will be presented if a region has no rule."
    	TaxRules []*TaxRule `protobuf:"bytes,3,rep,name=tax_rules,json=taxRules,proto3" json:"tax_rules,omitempty"`
    	// contains filtered or unexported fields
    }

The tax settings of a merchant account. All methods require the admin role.

### func (*AccountTax) Descriptor 
    
    
    func (*AccountTax) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AccountTax.ProtoReflect.Descriptor instead.

### func (*AccountTax) GetAccount 
    
    
    func (x *AccountTax) GetAccount() [int64](https://pkg.go.dev/builtin#int64)

### func (*AccountTax) GetName 
    
    
    func (x *AccountTax) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*AccountTax) GetTaxRules 
    
    
    func (x *AccountTax) GetTaxRules() []*TaxRule

### func (*AccountTax) ProtoMessage 
    
    
    func (*AccountTax) ProtoMessage()

### func (*AccountTax) ProtoReflect 
    
    
    func (x *AccountTax) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AccountTax) Reset 
    
    
    func (x *AccountTax) Reset()

### func (*AccountTax) String 
    
    
    func (x *AccountTax) String() [string](https://pkg.go.dev/builtin#string)

## AccountTaxServiceClient
    
    
    type AccountTaxServiceClient interface {
    	// Returns the tax rules that match the conditions of GetAccountTaxRequest
    	GetAccountTax(ctx context.Context, in *GetAccountTaxRequest, opts ...grpc.CallOption) (*AccountTax, [error](https://pkg.go.dev/builtin#error))
    	// Lists the tax settings of the sub-accounts only in your
    	// Merchant Center account.
    	// This method can only be called on a multi-client account, otherwise it'll
    	// return an error.
    	ListAccountTax(ctx context.Context, in *ListAccountTaxRequest, opts ...grpc.CallOption) (*ListAccountTaxResponse, [error](https://pkg.go.dev/builtin#error))
    	// Updates the tax settings of the account.
    	UpdateAccountTax(ctx context.Context, in *UpdateAccountTaxRequest, opts ...grpc.CallOption) (*AccountTax, [error](https://pkg.go.dev/builtin#error))
    }

AccountTaxServiceClient is the client API for AccountTaxService service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

### func NewAccountTaxServiceClient 
    
    
    func NewAccountTaxServiceClient(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) AccountTaxServiceClient

## AccountTaxServiceServer
    
    
    type AccountTaxServiceServer interface {
    	// Returns the tax rules that match the conditions of GetAccountTaxRequest
    	GetAccountTax(context.Context, *GetAccountTaxRequest) (*AccountTax, [error](https://pkg.go.dev/builtin#error))
    	// Lists the tax settings of the sub-accounts only in your
    	// Merchant Center account.
    	// This method can only be called on a multi-client account, otherwise it'll
    	// return an error.
    	ListAccountTax(context.Context, *ListAccountTaxRequest) (*ListAccountTaxResponse, [error](https://pkg.go.dev/builtin#error))
    	// Updates the tax settings of the account.
    	UpdateAccountTax(context.Context, *UpdateAccountTaxRequest) (*AccountTax, [error](https://pkg.go.dev/builtin#error))
    }

AccountTaxServiceServer is the server API for AccountTaxService service. All implementations should embed UnimplementedAccountTaxServiceServer for forward compatibility

## AccountsServiceClient
    
    
    type AccountsServiceClient interface {
    	// Retrieves an account from your Merchant Center account.
    	// After inserting, updating, or deleting an account, it may take several
    	// minutes before changes take effect.
    	GetAccount(ctx context.Context, in *GetAccountRequest, opts ...grpc.CallOption) (*Account, [error](https://pkg.go.dev/builtin#error))
    	// Creates a standalone Merchant Center account with additional configuration.
    	// Adds the user that makes the request as an admin for the new account.
    	CreateAndConfigureAccount(ctx context.Context, in *CreateAndConfigureAccountRequest, opts ...grpc.CallOption) (*Account, [error](https://pkg.go.dev/builtin#error))
    	// Deletes the specified account regardless of its type: standalone, MCA or
    	// sub-account. Deleting an MCA leads to the deletion of all of its
    	// sub-accounts. Executing this method requires admin access.
    	// The deletion succeeds only if the account does not provide services
    	// to any other account and has no processed offers. You can use the `force`
    	// parameter to override this.
    	DeleteAccount(ctx context.Context, in *DeleteAccountRequest, opts ...grpc.CallOption) (*emptypb.Empty, [error](https://pkg.go.dev/builtin#error))
    	// Updates an account regardless of its type: standalone, MCA or sub-account.
    	// Executing this method requires admin access.
    	UpdateAccount(ctx context.Context, in *UpdateAccountRequest, opts ...grpc.CallOption) (*Account, [error](https://pkg.go.dev/builtin#error))
    	// Lists accounts accessible to the calling user and matching the
    	// constraints of the request such as page size or filters.
    	// This is not just listing the sub-accounts of an MCA, but all accounts the
    	// calling user has access to including other MCAs, linked accounts,
    	// standalone accounts and so on. If no filter is provided, then it returns
    	// accounts the user is directly added to.
    	ListAccounts(ctx context.Context, in *ListAccountsRequest, opts ...grpc.CallOption) (*ListAccountsResponse, [error](https://pkg.go.dev/builtin#error))
    	// List all sub-accounts for a given multi client account. This is a
    	// convenience wrapper for the more powerful `ListAccounts` method. This
    	// method will produce the same results as calling `ListsAccounts` with the
    	// following filter:
    	// `relationship(providerId={parent} AND service(type="ACCOUNT_AGGREGATION"))`
    	ListSubAccounts(ctx context.Context, in *ListSubAccountsRequest, opts ...grpc.CallOption) (*ListSubAccountsResponse, [error](https://pkg.go.dev/builtin#error))
    }

AccountsServiceClient is the client API for AccountsService service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

### func NewAccountsServiceClient 
    
    
    func NewAccountsServiceClient(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) AccountsServiceClient

## AccountsServiceServer
    
    
    type AccountsServiceServer interface {
    	// Retrieves an account from your Merchant Center account.
    	// After inserting, updating, or deleting an account, it may take several
    	// minutes before changes take effect.
    	GetAccount(context.Context, *GetAccountRequest) (*Account, [error](https://pkg.go.dev/builtin#error))
    	// Creates a standalone Merchant Center account with additional configuration.
    	// Adds the user that makes the request as an admin for the new account.
    	CreateAndConfigureAccount(context.Context, *CreateAndConfigureAccountRequest) (*Account, [error](https://pkg.go.dev/builtin#error))
    	// Deletes the specified account regardless of its type: standalone, MCA or
    	// sub-account. Deleting an MCA leads to the deletion of all of its
    	// sub-accounts. Executing this method requires admin access.
    	// The deletion succeeds only if the account does not provide services
    	// to any other account and has no processed offers. You can use the `force`
    	// parameter to override this.
    	DeleteAccount(context.Context, *DeleteAccountRequest) (*emptypb.Empty, [error](https://pkg.go.dev/builtin#error))
    	// Updates an account regardless of its type: standalone, MCA or sub-account.
    	// Executing this method requires admin access.
    	UpdateAccount(context.Context, *UpdateAccountRequest) (*Account, [error](https://pkg.go.dev/builtin#error))
    	// Lists accounts accessible to the calling user and matching the
    	// constraints of the request such as page size or filters.
    	// This is not just listing the sub-accounts of an MCA, but all accounts the
    	// calling user has access to including other MCAs, linked accounts,
    	// standalone accounts and so on. If no filter is provided, then it returns
    	// accounts the user is directly added to.
    	ListAccounts(context.Context, *ListAccountsRequest) (*ListAccountsResponse, [error](https://pkg.go.dev/builtin#error))
    	// List all sub-accounts for a given multi client account. This is a
    	// convenience wrapper for the more powerful `ListAccounts` method. This
    	// method will produce the same results as calling `ListsAccounts` with the
    	// following filter:
    	// `relationship(providerId={parent} AND service(type="ACCOUNT_AGGREGATION"))`
    	ListSubAccounts(context.Context, *ListSubAccountsRequest) (*ListSubAccountsResponse, [error](https://pkg.go.dev/builtin#error))
    }

AccountsServiceServer is the server API for AccountsService service. All implementations should embed UnimplementedAccountsServiceServer for forward compatibility

## Address
    
    
    type Address struct {
    
    	// Street-level part of the address. For example: `111w 31st Street`.
    	StreetAddress *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=street_address,json=streetAddress,proto3,oneof" json:"street_address,omitempty"`
    	// Required. City, town or commune. May also include dependent localities or
    	// sublocalities (For example neighborhoods or suburbs).
    	City *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=city,proto3,oneof" json:"city,omitempty"`
    	// Required. Top-level administrative subdivision of the country. For example,
    	// a state like California ("CA") or a province like Quebec ("QC").
    	AdministrativeArea *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=administrative_area,json=administrativeArea,proto3,oneof" json:"administrative_area,omitempty"`
    	// Required. Postal code or ZIP (For example "94043").
    	PostalCode *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=postal_code,json=postalCode,proto3,oneof" json:"postal_code,omitempty"`
    	// Required. [CLDR country
    	// code](http://www.unicode.org/repos/cldr/tags/latest/common/main/en.xml)
    	// (For example "US").
    	RegionCode *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=region_code,json=regionCode,proto3,oneof" json:"region_code,omitempty"`
    	// contains filtered or unexported fields
    }

Shipping address of the warehouse.

### func (*Address) Descriptor 
    
    
    func (*Address) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Address.ProtoReflect.Descriptor instead.

### func (*Address) GetAdministrativeArea 
    
    
    func (x *Address) GetAdministrativeArea() [string](https://pkg.go.dev/builtin#string)

### func (*Address) GetCity 
    
    
    func (x *Address) GetCity() [string](https://pkg.go.dev/builtin#string)

### func (*Address) GetPostalCode 
    
    
    func (x *Address) GetPostalCode() [string](https://pkg.go.dev/builtin#string)

### func (*Address) GetRegionCode 
    
    
    func (x *Address) GetRegionCode() [string](https://pkg.go.dev/builtin#string)

### func (*Address) GetStreetAddress 
    
    
    func (x *Address) GetStreetAddress() [string](https://pkg.go.dev/builtin#string)

### func (*Address) ProtoMessage 
    
    
    func (*Address) ProtoMessage()

### func (*Address) ProtoReflect 
    
    
    func (x *Address) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Address) Reset 
    
    
    func (x *Address) Reset()

### func (*Address) String 
    
    
    func (x *Address) String() [string](https://pkg.go.dev/builtin#string)

## AutofeedSettings
    
    
    type AutofeedSettings struct {
    
    	// Identifier. The resource name of the autofeed settings.
    	// Format: `accounts/{account}/autofeedSettings`.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Required. Enables or disables product crawling through the autofeed for the
    	// given account. Autofeed accounts must meet [certain
    	// conditions](https://support.google.com/merchants/answer/7538732#Configure_automated_feeds_Standard_Experience),
    	// which can be checked through the `eligible` field.
    	// The account must **not** be a marketplace.
    	// When the autofeed is enabled for the first time, the products usually
    	// appear instantly. When re-enabling, it might take up to 24 hours for
    	// products to appear.
    	EnableProducts [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,2,opt,name=enable_products,json=enableProducts,proto3" json:"enable_products,omitempty"`
    	// Output only. Determines whether merchant is eligible for being enrolled
    	// into an autofeed.
    	Eligible [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,3,opt,name=eligible,proto3" json:"eligible,omitempty"`
    	// contains filtered or unexported fields
    }

Collection of information related to the [autofeed](https://support.google.com/merchants/answer/7538732) settings.

### func (*AutofeedSettings) Descriptor 
    
    
    func (*AutofeedSettings) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AutofeedSettings.ProtoReflect.Descriptor instead.

### func (*AutofeedSettings) GetEligible 
    
    
    func (x *AutofeedSettings) GetEligible() [bool](https://pkg.go.dev/builtin#bool)

### func (*AutofeedSettings) GetEnableProducts 
    
    
    func (x *AutofeedSettings) GetEnableProducts() [bool](https://pkg.go.dev/builtin#bool)

### func (*AutofeedSettings) GetName 
    
    
    func (x *AutofeedSettings) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*AutofeedSettings) ProtoMessage 
    
    
    func (*AutofeedSettings) ProtoMessage()

### func (*AutofeedSettings) ProtoReflect 
    
    
    func (x *AutofeedSettings) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AutofeedSettings) Reset 
    
    
    func (x *AutofeedSettings) Reset()

### func (*AutofeedSettings) String 
    
    
    func (x *AutofeedSettings) String() [string](https://pkg.go.dev/builtin#string)

## AutofeedSettingsServiceClient
    
    
    type AutofeedSettingsServiceClient interface {
    	// Retrieves the autofeed settings of an account.
    	GetAutofeedSettings(ctx context.Context, in *GetAutofeedSettingsRequest, opts ...grpc.CallOption) (*AutofeedSettings, [error](https://pkg.go.dev/builtin#error))
    	// Updates the autofeed settings of an account.
    	UpdateAutofeedSettings(ctx context.Context, in *UpdateAutofeedSettingsRequest, opts ...grpc.CallOption) (*AutofeedSettings, [error](https://pkg.go.dev/builtin#error))
    }

AutofeedSettingsServiceClient is the client API for AutofeedSettingsService service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

### func NewAutofeedSettingsServiceClient 
    
    
    func NewAutofeedSettingsServiceClient(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) AutofeedSettingsServiceClient

## AutofeedSettingsServiceServer
    
    
    type AutofeedSettingsServiceServer interface {
    	// Retrieves the autofeed settings of an account.
    	GetAutofeedSettings(context.Context, *GetAutofeedSettingsRequest) (*AutofeedSettings, [error](https://pkg.go.dev/builtin#error))
    	// Updates the autofeed settings of an account.
    	UpdateAutofeedSettings(context.Context, *UpdateAutofeedSettingsRequest) (*AutofeedSettings, [error](https://pkg.go.dev/builtin#error))
    }

AutofeedSettingsServiceServer is the server API for AutofeedSettingsService service. All implementations should embed UnimplementedAutofeedSettingsServiceServer for forward compatibility

## AutomaticImageImprovements
    
    
    type AutomaticImageImprovements struct {
    
    	// Optional. Determines how the images should be automatically updated.
    	// If this field is not present and provided in the update mask, then the
    	// settings will be deleted. If there are no settings for subaccount, they are
    	// inherited from aggregator.
    	AccountImageImprovementsSettings *AutomaticImageImprovements_ImageImprovementsAccountLevelSettings `protobuf:"bytes,1,opt,name=account_image_improvements_settings,json=accountImageImprovementsSettings,proto3,oneof" json:"account_image_improvements_settings,omitempty"`
    	// Output only. The effective value of allow_automatic_image_improvements.
    	// If account_image_improvements_settings is present, then this value is the
    	// same. Otherwise, it represents the inherited value of the parent account.
    	// Read-only.
    	EffectiveAllowAutomaticImageImprovements [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,2,opt,name=effective_allow_automatic_image_improvements,json=effectiveAllowAutomaticImageImprovements,proto3" json:"effective_allow_automatic_image_improvements,omitempty"`
    	// contains filtered or unexported fields
    }

This improvement will attempt to automatically correct submitted images if they don't meet the [image requirements](https://support.google.com/merchants/answer/6324350), for example, removing overlays. If successful, the image will be replaced and approved. This improvement is only applied to images of disapproved offers. For more information see: [Automatic image improvements](https://support.google.com/merchants/answer/9242973)

### func (*AutomaticImageImprovements) Descriptor 
    
    
    func (*AutomaticImageImprovements) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AutomaticImageImprovements.ProtoReflect.Descriptor instead.

### func (*AutomaticImageImprovements) GetAccountImageImprovementsSettings 
    
    
    func (x *AutomaticImageImprovements) GetAccountImageImprovementsSettings() *AutomaticImageImprovements_ImageImprovementsAccountLevelSettings

### func (*AutomaticImageImprovements) GetEffectiveAllowAutomaticImageImprovements 
    
    
    func (x *AutomaticImageImprovements) GetEffectiveAllowAutomaticImageImprovements() [bool](https://pkg.go.dev/builtin#bool)

### func (*AutomaticImageImprovements) ProtoMessage 
    
    
    func (*AutomaticImageImprovements) ProtoMessage()

### func (*AutomaticImageImprovements) ProtoReflect 
    
    
    func (x *AutomaticImageImprovements) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AutomaticImageImprovements) Reset 
    
    
    func (x *AutomaticImageImprovements) Reset()

### func (*AutomaticImageImprovements) String 
    
    
    func (x *AutomaticImageImprovements) String() [string](https://pkg.go.dev/builtin#string)

## AutomaticImageImprovements_ImageImprovementsAccountLevelSettings
    
    
    type AutomaticImageImprovements_ImageImprovementsAccountLevelSettings struct {
    
    	// Enables automatic image improvements.
    	AllowAutomaticImageImprovements *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,1,opt,name=allow_automatic_image_improvements,json=allowAutomaticImageImprovements,proto3,oneof" json:"allow_automatic_image_improvements,omitempty"`
    	// contains filtered or unexported fields
    }

Settings for the Automatic Image Improvements.

### func (*AutomaticImageImprovements_ImageImprovementsAccountLevelSettings) Descriptor 
    
    
    func (*AutomaticImageImprovements_ImageImprovementsAccountLevelSettings) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AutomaticImageImprovements_ImageImprovementsAccountLevelSettings.ProtoReflect.Descriptor instead.

### func (*AutomaticImageImprovements_ImageImprovementsAccountLevelSettings) GetAllowAutomaticImageImprovements 
    
    
    func (x *AutomaticImageImprovements_ImageImprovementsAccountLevelSettings) GetAllowAutomaticImageImprovements() [bool](https://pkg.go.dev/builtin#bool)

### func (*AutomaticImageImprovements_ImageImprovementsAccountLevelSettings) ProtoMessage 
    
    
    func (*AutomaticImageImprovements_ImageImprovementsAccountLevelSettings) ProtoMessage()

### func (*AutomaticImageImprovements_ImageImprovementsAccountLevelSettings) ProtoReflect 
    
    
    func (x *AutomaticImageImprovements_ImageImprovementsAccountLevelSettings) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AutomaticImageImprovements_ImageImprovementsAccountLevelSettings) Reset 
    
    
    func (x *AutomaticImageImprovements_ImageImprovementsAccountLevelSettings) Reset()

### func (*AutomaticImageImprovements_ImageImprovementsAccountLevelSettings) String 
    
    
    func (x *AutomaticImageImprovements_ImageImprovementsAccountLevelSettings) String() [string](https://pkg.go.dev/builtin#string)

## AutomaticImprovements
    
    
    type AutomaticImprovements struct {
    
    	// Identifier. The resource name of the automatic improvements.
    	// Format: `accounts/{account}/automaticImprovements`.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Turning on [item
    	// updates](https://support.google.com/merchants/answer/3246284) allows
    	// Google to automatically update items for you. When item updates are on,
    	// Google uses the structured data markup on the website and advanced data
    	// extractors to update the price and availability of the items. When the item
    	// updates are off, items with mismatched data aren't shown.
    	// This field is only updated (cleared) if provided in the update mask.
    	ItemUpdates *AutomaticItemUpdates `protobuf:"bytes,2,opt,name=item_updates,json=itemUpdates,proto3,oneof" json:"item_updates,omitempty"`
    	// This improvement will attempt to automatically correct submitted images if
    	// they don't meet the [image
    	// requirements](https://support.google.com/merchants/answer/6324350), for
    	// example, removing overlays. If successful, the image will be replaced and
    	// approved. This improvement is only applied to images of disapproved offers.
    	// For more information see: [Automatic image
    	// improvements](https://support.google.com/merchants/answer/9242973)
    	// This field is only updated (cleared) if provided in the update mask.
    	ImageImprovements *AutomaticImageImprovements `protobuf:"bytes,3,opt,name=image_improvements,json=imageImprovements,proto3,oneof" json:"image_improvements,omitempty"`
    	// Not available for MCAs
    	// [accounts](https://support.google.com/merchants/answer/188487). By turning
    	// on [automatic shipping
    	// improvements](https://support.google.com/merchants/answer/10027038),
    	// you are allowing Google to improve the accuracy of your delivery times
    	// shown to shoppers using Google. More accurate delivery times, especially
    	// when faster, typically lead to better conversion rates. Google will improve
    	// your estimated delivery times based on various factors:
    	// * Delivery address of an order
    	// * Current handling time and shipping time settings
    	// * Estimated weekdays or business days
    	// * Parcel tracking data
    	// This field is only updated (cleared) if provided in the update mask.
    	ShippingImprovements *AutomaticShippingImprovements `protobuf:"bytes,4,opt,name=shipping_improvements,json=shippingImprovements,proto3,oneof" json:"shipping_improvements,omitempty"`
    	// contains filtered or unexported fields
    }

Collection of information related to the [automatic improvements](https://developers.google.com/shopping-content/guides/automatic-improvements) of an account.

### func (*AutomaticImprovements) Descriptor 
    
    
    func (*AutomaticImprovements) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AutomaticImprovements.ProtoReflect.Descriptor instead.

### func (*AutomaticImprovements) GetImageImprovements 
    
    
    func (x *AutomaticImprovements) GetImageImprovements() *AutomaticImageImprovements

### func (*AutomaticImprovements) GetItemUpdates 
    
    
    func (x *AutomaticImprovements) GetItemUpdates() *AutomaticItemUpdates

### func (*AutomaticImprovements) GetName 
    
    
    func (x *AutomaticImprovements) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*AutomaticImprovements) GetShippingImprovements 
    
    
    func (x *AutomaticImprovements) GetShippingImprovements() *AutomaticShippingImprovements

### func (*AutomaticImprovements) ProtoMessage 
    
    
    func (*AutomaticImprovements) ProtoMessage()

### func (*AutomaticImprovements) ProtoReflect 
    
    
    func (x *AutomaticImprovements) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AutomaticImprovements) Reset 
    
    
    func (x *AutomaticImprovements) Reset()

### func (*AutomaticImprovements) String 
    
    
    func (x *AutomaticImprovements) String() [string](https://pkg.go.dev/builtin#string)

## AutomaticImprovementsServiceClient
    
    
    type AutomaticImprovementsServiceClient interface {
    	// Retrieves the automatic improvements of an account.
    	GetAutomaticImprovements(ctx context.Context, in *GetAutomaticImprovementsRequest, opts ...grpc.CallOption) (*AutomaticImprovements, [error](https://pkg.go.dev/builtin#error))
    	// Updates the automatic improvements of an account.
    	UpdateAutomaticImprovements(ctx context.Context, in *UpdateAutomaticImprovementsRequest, opts ...grpc.CallOption) (*AutomaticImprovements, [error](https://pkg.go.dev/builtin#error))
    }

AutomaticImprovementsServiceClient is the client API for AutomaticImprovementsService service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

### func NewAutomaticImprovementsServiceClient 
    
    
    func NewAutomaticImprovementsServiceClient(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) AutomaticImprovementsServiceClient

## AutomaticImprovementsServiceServer
    
    
    type AutomaticImprovementsServiceServer interface {
    	// Retrieves the automatic improvements of an account.
    	GetAutomaticImprovements(context.Context, *GetAutomaticImprovementsRequest) (*AutomaticImprovements, [error](https://pkg.go.dev/builtin#error))
    	// Updates the automatic improvements of an account.
    	UpdateAutomaticImprovements(context.Context, *UpdateAutomaticImprovementsRequest) (*AutomaticImprovements, [error](https://pkg.go.dev/builtin#error))
    }

AutomaticImprovementsServiceServer is the server API for AutomaticImprovementsService service. All implementations should embed UnimplementedAutomaticImprovementsServiceServer for forward compatibility

## AutomaticItemUpdates
    
    
    type AutomaticItemUpdates struct {
    
    	// Optional. Determines which attributes of the items should be automatically
    	// updated. If this field is not present and provided in the update mask, then
    	// the settings will be deleted. If there are no settings for subaccount, they
    	// are inherited from aggregator.
    	AccountItemUpdatesSettings *AutomaticItemUpdates_ItemUpdatesAccountLevelSettings `protobuf:"bytes,1,opt,name=account_item_updates_settings,json=accountItemUpdatesSettings,proto3" json:"account_item_updates_settings,omitempty"`
    	// Output only. The effective value of allow_price_updates.
    	// If account_item_updates_settings is present, then this value is the same.
    	// Otherwise, it represents the inherited value of the parent account.
    	// The default value is true if no settings are present.
    	// Read-only.
    	EffectiveAllowPriceUpdates [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,2,opt,name=effective_allow_price_updates,json=effectiveAllowPriceUpdates,proto3" json:"effective_allow_price_updates,omitempty"`
    	// Output only. The effective value of allow_availability_updates.
    	// If account_item_updates_settings is present, then this value is the same.
    	// Otherwise, it represents the inherited value of the parent account.
    	// The default value is true if no settings are present.
    	// Read-only.
    	EffectiveAllowAvailabilityUpdates [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,3,opt,name=effective_allow_availability_updates,json=effectiveAllowAvailabilityUpdates,proto3" json:"effective_allow_availability_updates,omitempty"`
    	// Output only. The effective value of
    	// allow_strict_availability_updates.
    	// If account_item_updates_settings is present, then this value is the same.
    	// Otherwise, it represents the inherited value of the parent account.
    	// The default value is true if no settings are present.
    	// Read-only.
    	EffectiveAllowStrictAvailabilityUpdates [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,4,opt,name=effective_allow_strict_availability_updates,json=effectiveAllowStrictAvailabilityUpdates,proto3" json:"effective_allow_strict_availability_updates,omitempty"`
    	// Output only. The effective value of allow_condition_updates.
    	// If account_item_updates_settings is present, then this value is the same.
    	// Otherwise, it represents the inherited value of the parent account.
    	// The default value is true if no settings are present.
    	// Read-only.
    	EffectiveAllowConditionUpdates [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,5,opt,name=effective_allow_condition_updates,json=effectiveAllowConditionUpdates,proto3" json:"effective_allow_condition_updates,omitempty"`
    	// contains filtered or unexported fields
    }

Turning on [item updates](https://support.google.com/merchants/answer/3246284) allows Google to automatically update items for you. When item updates are on, Google uses the structured data markup on the website and advanced data extractors to update the price and availability of the items. When the item updates are off, items with mismatched data aren't shown.

### func (*AutomaticItemUpdates) Descriptor 
    
    
    func (*AutomaticItemUpdates) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AutomaticItemUpdates.ProtoReflect.Descriptor instead.

### func (*AutomaticItemUpdates) GetAccountItemUpdatesSettings 
    
    
    func (x *AutomaticItemUpdates) GetAccountItemUpdatesSettings() *AutomaticItemUpdates_ItemUpdatesAccountLevelSettings

### func (*AutomaticItemUpdates) GetEffectiveAllowAvailabilityUpdates 
    
    
    func (x *AutomaticItemUpdates) GetEffectiveAllowAvailabilityUpdates() [bool](https://pkg.go.dev/builtin#bool)

### func (*AutomaticItemUpdates) GetEffectiveAllowConditionUpdates 
    
    
    func (x *AutomaticItemUpdates) GetEffectiveAllowConditionUpdates() [bool](https://pkg.go.dev/builtin#bool)

### func (*AutomaticItemUpdates) GetEffectiveAllowPriceUpdates 
    
    
    func (x *AutomaticItemUpdates) GetEffectiveAllowPriceUpdates() [bool](https://pkg.go.dev/builtin#bool)

### func (*AutomaticItemUpdates) GetEffectiveAllowStrictAvailabilityUpdates 
    
    
    func (x *AutomaticItemUpdates) GetEffectiveAllowStrictAvailabilityUpdates() [bool](https://pkg.go.dev/builtin#bool)

### func (*AutomaticItemUpdates) ProtoMessage 
    
    
    func (*AutomaticItemUpdates) ProtoMessage()

### func (*AutomaticItemUpdates) ProtoReflect 
    
    
    func (x *AutomaticItemUpdates) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AutomaticItemUpdates) Reset 
    
    
    func (x *AutomaticItemUpdates) Reset()

### func (*AutomaticItemUpdates) String 
    
    
    func (x *AutomaticItemUpdates) String() [string](https://pkg.go.dev/builtin#string)

## AutomaticItemUpdates_ItemUpdatesAccountLevelSettings
    
    
    type AutomaticItemUpdates_ItemUpdatesAccountLevelSettings struct {
    
    	// If price updates are enabled, Google always updates the active price with
    	// the crawled information.
    	AllowPriceUpdates *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,1,opt,name=allow_price_updates,json=allowPriceUpdates,proto3,oneof" json:"allow_price_updates,omitempty"`
    	// If availability updates are enabled, any previous availability values
    	// get overwritten if Google finds an out-of-stock annotation on the offer's
    	// page.
    	// If additionally `allow_strict_availability_updates` field is set to
    	// true, values get overwritten if Google finds an in-stock annotation on
    	// the offer’s page.
    	AllowAvailabilityUpdates *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,2,opt,name=allow_availability_updates,json=allowAvailabilityUpdates,proto3,oneof" json:"allow_availability_updates,omitempty"`
    	// If `allow_availability_updates` is enabled, items are automatically
    	// updated in all your Shopping target countries. By default, availability
    	// updates will only be applied to items that are 'out of stock' on your
    	// website but 'in stock' on Shopping. Set this to true to also update items
    	// that are 'in stock' on your website, but 'out of stock' on Google
    	// Shopping. In order for this field to have an effect, you must also set
    	// `allow_availability_updates`.
    	AllowStrictAvailabilityUpdates *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,3,opt,name=allow_strict_availability_updates,json=allowStrictAvailabilityUpdates,proto3,oneof" json:"allow_strict_availability_updates,omitempty"`
    	// If condition updates are enabled, Google always updates item condition
    	// with the condition detected from the details of your product.
    	AllowConditionUpdates *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,4,opt,name=allow_condition_updates,json=allowConditionUpdates,proto3,oneof" json:"allow_condition_updates,omitempty"`
    	// contains filtered or unexported fields
    }

Settings for the Automatic Item Updates.

### func (*AutomaticItemUpdates_ItemUpdatesAccountLevelSettings) Descriptor 
    
    
    func (*AutomaticItemUpdates_ItemUpdatesAccountLevelSettings) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AutomaticItemUpdates_ItemUpdatesAccountLevelSettings.ProtoReflect.Descriptor instead.

### func (*AutomaticItemUpdates_ItemUpdatesAccountLevelSettings) GetAllowAvailabilityUpdates 
    
    
    func (x *AutomaticItemUpdates_ItemUpdatesAccountLevelSettings) GetAllowAvailabilityUpdates() [bool](https://pkg.go.dev/builtin#bool)

### func (*AutomaticItemUpdates_ItemUpdatesAccountLevelSettings) GetAllowConditionUpdates 
    
    
    func (x *AutomaticItemUpdates_ItemUpdatesAccountLevelSettings) GetAllowConditionUpdates() [bool](https://pkg.go.dev/builtin#bool)

### func (*AutomaticItemUpdates_ItemUpdatesAccountLevelSettings) GetAllowPriceUpdates 
    
    
    func (x *AutomaticItemUpdates_ItemUpdatesAccountLevelSettings) GetAllowPriceUpdates() [bool](https://pkg.go.dev/builtin#bool)

### func (*AutomaticItemUpdates_ItemUpdatesAccountLevelSettings) GetAllowStrictAvailabilityUpdates 
    
    
    func (x *AutomaticItemUpdates_ItemUpdatesAccountLevelSettings) GetAllowStrictAvailabilityUpdates() [bool](https://pkg.go.dev/builtin#bool)

### func (*AutomaticItemUpdates_ItemUpdatesAccountLevelSettings) ProtoMessage 
    
    
    func (*AutomaticItemUpdates_ItemUpdatesAccountLevelSettings) ProtoMessage()

### func (*AutomaticItemUpdates_ItemUpdatesAccountLevelSettings) ProtoReflect 
    
    
    func (x *AutomaticItemUpdates_ItemUpdatesAccountLevelSettings) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AutomaticItemUpdates_ItemUpdatesAccountLevelSettings) Reset 
    
    
    func (x *AutomaticItemUpdates_ItemUpdatesAccountLevelSettings) Reset()

### func (*AutomaticItemUpdates_ItemUpdatesAccountLevelSettings) String 
    
    
    func (x *AutomaticItemUpdates_ItemUpdatesAccountLevelSettings) String() [string](https://pkg.go.dev/builtin#string)

## AutomaticShippingImprovements
    
    
    type AutomaticShippingImprovements struct {
    
    	// Enables automatic shipping improvements.
    	AllowShippingImprovements *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,1,opt,name=allow_shipping_improvements,json=allowShippingImprovements,proto3,oneof" json:"allow_shipping_improvements,omitempty"`
    	// contains filtered or unexported fields
    }

Not available for MCAs [accounts](https://support.google.com/merchants/answer/188487). By turning on [automatic shipping improvements](https://support.google.com/merchants/answer/10027038), you are allowing Google to improve the accuracy of your delivery times shown to shoppers using Google. More accurate delivery times, especially when faster, typically lead to better conversion rates. Google will improve your estimated delivery times based on various factors:

  * Delivery address of an order
  * Current handling time and shipping time settings
  * Estimated weekdays or business days
  * Parcel tracking data



### func (*AutomaticShippingImprovements) Descriptor 
    
    
    func (*AutomaticShippingImprovements) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AutomaticShippingImprovements.ProtoReflect.Descriptor instead.

### func (*AutomaticShippingImprovements) GetAllowShippingImprovements 
    
    
    func (x *AutomaticShippingImprovements) GetAllowShippingImprovements() [bool](https://pkg.go.dev/builtin#bool)

### func (*AutomaticShippingImprovements) ProtoMessage 
    
    
    func (*AutomaticShippingImprovements) ProtoMessage()

### func (*AutomaticShippingImprovements) ProtoReflect 
    
    
    func (x *AutomaticShippingImprovements) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AutomaticShippingImprovements) Reset 
    
    
    func (x *AutomaticShippingImprovements) Reset()

### func (*AutomaticShippingImprovements) String 
    
    
    func (x *AutomaticShippingImprovements) String() [string](https://pkg.go.dev/builtin#string)

## BusinessDayConfig
    
    
    type BusinessDayConfig struct {
    
    	// Required. Regular business days.
    	// May not be empty.
    	BusinessDays []BusinessDayConfig_Weekday `protobuf:"varint,1,rep,packed,name=business_days,json=businessDays,proto3,enum=google.shopping.merchant.accounts.v1beta.BusinessDayConfig_Weekday" json:"business_days,omitempty"`
    	// contains filtered or unexported fields
    }

Business days of the warehouse.

### func (*BusinessDayConfig) Descriptor 
    
    
    func (*BusinessDayConfig) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use BusinessDayConfig.ProtoReflect.Descriptor instead.

### func (*BusinessDayConfig) GetBusinessDays 
    
    
    func (x *BusinessDayConfig) GetBusinessDays() []BusinessDayConfig_Weekday

### func (*BusinessDayConfig) ProtoMessage 
    
    
    func (*BusinessDayConfig) ProtoMessage()

### func (*BusinessDayConfig) ProtoReflect 
    
    
    func (x *BusinessDayConfig) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*BusinessDayConfig) Reset 
    
    
    func (x *BusinessDayConfig) Reset()

### func (*BusinessDayConfig) String 
    
    
    func (x *BusinessDayConfig) String() [string](https://pkg.go.dev/builtin#string)

## BusinessDayConfig_Weekday
    
    
    type BusinessDayConfig_Weekday [int32](https://pkg.go.dev/builtin#int32)

### BusinessDayConfig_WEEKDAY_UNSPECIFIED, BusinessDayConfig_MONDAY, BusinessDayConfig_TUESDAY, BusinessDayConfig_WEDNESDAY, BusinessDayConfig_THURSDAY, BusinessDayConfig_FRIDAY, BusinessDayConfig_SATURDAY, BusinessDayConfig_SUNDAY
    
    
    const (
    	BusinessDayConfig_WEEKDAY_UNSPECIFIED BusinessDayConfig_Weekday = 0
    	BusinessDayConfig_MONDAY              BusinessDayConfig_Weekday = 1
    	BusinessDayConfig_TUESDAY             BusinessDayConfig_Weekday = 2
    	BusinessDayConfig_WEDNESDAY           BusinessDayConfig_Weekday = 3
    	BusinessDayConfig_THURSDAY            BusinessDayConfig_Weekday = 4
    	BusinessDayConfig_FRIDAY              BusinessDayConfig_Weekday = 5
    	BusinessDayConfig_SATURDAY            BusinessDayConfig_Weekday = 6
    	BusinessDayConfig_SUNDAY              BusinessDayConfig_Weekday = 7
    )

### func (BusinessDayConfig_Weekday) Descriptor 
    
    
    func (BusinessDayConfig_Weekday) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (BusinessDayConfig_Weekday) Enum 
    
    
    func (x BusinessDayConfig_Weekday) Enum() *BusinessDayConfig_Weekday

### func (BusinessDayConfig_Weekday) EnumDescriptor 
    
    
    func (BusinessDayConfig_Weekday) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use BusinessDayConfig_Weekday.Descriptor instead.

### func (BusinessDayConfig_Weekday) Number 
    
    
    func (x BusinessDayConfig_Weekday) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (BusinessDayConfig_Weekday) String 
    
    
    func (x BusinessDayConfig_Weekday) String() [string](https://pkg.go.dev/builtin#string)

### func (BusinessDayConfig_Weekday) Type 
    
    
    func (BusinessDayConfig_Weekday) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## BusinessIdentity
    
    
    type BusinessIdentity struct {
    
    	// Identifier. The resource name of the business identity.
    	// Format: `accounts/{account}/businessIdentity`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. Whether the identity attributes may be used for promotions.
    	PromotionsConsent BusinessIdentity_PromotionsConsent `protobuf:"varint,2,opt,name=promotions_consent,json=promotionsConsent,proto3,enum=google.shopping.merchant.accounts.v1beta.BusinessIdentity_PromotionsConsent" json:"promotions_consent,omitempty"`
    	// Optional. Specifies whether the business identifies itself as being
    	// black-owned. This optional field will only be available for merchants with
    	// a business country set to `US`. It is also not applicable for marketplaces
    	// or marketplace sellers.
    	BlackOwned *BusinessIdentity_IdentityAttribute `protobuf:"bytes,3,opt,name=black_owned,json=blackOwned,proto3" json:"black_owned,omitempty"`
    	// Optional. Specifies whether the business identifies itself as being
    	// women-owned. This optional field will only be available for merchants with
    	// a business country set to `US`. It is also not applicable for marketplaces
    	// or marketplace sellers.
    	WomenOwned *BusinessIdentity_IdentityAttribute `protobuf:"bytes,4,opt,name=women_owned,json=womenOwned,proto3" json:"women_owned,omitempty"`
    	// Optional. Specifies whether the business identifies itself as being
    	// veteran-owned. This optional field will only be available for merchants
    	// with a business country set to `US`. It is also not applicable for
    	// marketplaces or marketplace sellers.
    	VeteranOwned *BusinessIdentity_IdentityAttribute `protobuf:"bytes,5,opt,name=veteran_owned,json=veteranOwned,proto3" json:"veteran_owned,omitempty"`
    	// Optional. Specifies whether the business identifies itself as being
    	// latino-owned. This optional field will only be available for merchants with
    	// a business country set to `US`. It is also not applicable for marketplaces
    	// or marketplace sellers.
    	LatinoOwned *BusinessIdentity_IdentityAttribute `protobuf:"bytes,6,opt,name=latino_owned,json=latinoOwned,proto3" json:"latino_owned,omitempty"`
    	// Optional. Specifies whether the business identifies itself as a small
    	// business. This optional field will only be available for merchants with a
    	// business country set to `US`. It is also not applicable for marketplaces.
    	SmallBusiness *BusinessIdentity_IdentityAttribute `protobuf:"bytes,7,opt,name=small_business,json=smallBusiness,proto3" json:"small_business,omitempty"`
    	// contains filtered or unexported fields
    }

Collection of information related to the [identity of a business](https://support.google.com/merchants/answer/12564247).

### func (*BusinessIdentity) Descriptor 
    
    
    func (*BusinessIdentity) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use BusinessIdentity.ProtoReflect.Descriptor instead.

### func (*BusinessIdentity) GetBlackOwned 
    
    
    func (x *BusinessIdentity) GetBlackOwned() *BusinessIdentity_IdentityAttribute

### func (*BusinessIdentity) GetLatinoOwned 
    
    
    func (x *BusinessIdentity) GetLatinoOwned() *BusinessIdentity_IdentityAttribute

### func (*BusinessIdentity) GetName 
    
    
    func (x *BusinessIdentity) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*BusinessIdentity) GetPromotionsConsent 
    
    
    func (x *BusinessIdentity) GetPromotionsConsent() BusinessIdentity_PromotionsConsent

### func (*BusinessIdentity) GetSmallBusiness 
    
    
    func (x *BusinessIdentity) GetSmallBusiness() *BusinessIdentity_IdentityAttribute

### func (*BusinessIdentity) GetVeteranOwned 
    
    
    func (x *BusinessIdentity) GetVeteranOwned() *BusinessIdentity_IdentityAttribute

### func (*BusinessIdentity) GetWomenOwned 
    
    
    func (x *BusinessIdentity) GetWomenOwned() *BusinessIdentity_IdentityAttribute

### func (*BusinessIdentity) ProtoMessage 
    
    
    func (*BusinessIdentity) ProtoMessage()

### func (*BusinessIdentity) ProtoReflect 
    
    
    func (x *BusinessIdentity) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*BusinessIdentity) Reset 
    
    
    func (x *BusinessIdentity) Reset()

### func (*BusinessIdentity) String 
    
    
    func (x *BusinessIdentity) String() [string](https://pkg.go.dev/builtin#string)

## BusinessIdentityServiceClient
    
    
    type BusinessIdentityServiceClient interface {
    	// Retrieves the business identity of an account.
    	GetBusinessIdentity(ctx context.Context, in *GetBusinessIdentityRequest, opts ...grpc.CallOption) (*BusinessIdentity, [error](https://pkg.go.dev/builtin#error))
    	// Updates the business identity of an account. Executing this method requires
    	// admin access.
    	UpdateBusinessIdentity(ctx context.Context, in *UpdateBusinessIdentityRequest, opts ...grpc.CallOption) (*BusinessIdentity, [error](https://pkg.go.dev/builtin#error))
    }

BusinessIdentityServiceClient is the client API for BusinessIdentityService service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

### func NewBusinessIdentityServiceClient 
    
    
    func NewBusinessIdentityServiceClient(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) BusinessIdentityServiceClient

## BusinessIdentityServiceServer
    
    
    type BusinessIdentityServiceServer interface {
    	// Retrieves the business identity of an account.
    	GetBusinessIdentity(context.Context, *GetBusinessIdentityRequest) (*BusinessIdentity, [error](https://pkg.go.dev/builtin#error))
    	// Updates the business identity of an account. Executing this method requires
    	// admin access.
    	UpdateBusinessIdentity(context.Context, *UpdateBusinessIdentityRequest) (*BusinessIdentity, [error](https://pkg.go.dev/builtin#error))
    }

BusinessIdentityServiceServer is the server API for BusinessIdentityService service. All implementations should embed UnimplementedBusinessIdentityServiceServer for forward compatibility

## BusinessIdentity_IdentityAttribute
    
    
    type BusinessIdentity_IdentityAttribute struct {
    
    	// Required. The declaration of identity for this attribute.
    	IdentityDeclaration BusinessIdentity_IdentityAttribute_IdentityDeclaration `protobuf:"varint,1,opt,name=identity_declaration,json=identityDeclaration,proto3,enum=google.shopping.merchant.accounts.v1beta.BusinessIdentity_IdentityAttribute_IdentityDeclaration" json:"identity_declaration,omitempty"`
    	// contains filtered or unexported fields
    }

All information related to an identity attribute.

### func (*BusinessIdentity_IdentityAttribute) Descriptor 
    
    
    func (*BusinessIdentity_IdentityAttribute) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use BusinessIdentity_IdentityAttribute.ProtoReflect.Descriptor instead.

### func (*BusinessIdentity_IdentityAttribute) GetIdentityDeclaration 
    
    
    func (x *BusinessIdentity_IdentityAttribute) GetIdentityDeclaration() BusinessIdentity_IdentityAttribute_IdentityDeclaration

### func (*BusinessIdentity_IdentityAttribute) ProtoMessage 
    
    
    func (*BusinessIdentity_IdentityAttribute) ProtoMessage()

### func (*BusinessIdentity_IdentityAttribute) ProtoReflect 
    
    
    func (x *BusinessIdentity_IdentityAttribute) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*BusinessIdentity_IdentityAttribute) Reset 
    
    
    func (x *BusinessIdentity_IdentityAttribute) Reset()

### func (*BusinessIdentity_IdentityAttribute) String 
    
    
    func (x *BusinessIdentity_IdentityAttribute) String() [string](https://pkg.go.dev/builtin#string)

## BusinessIdentity_IdentityAttribute_IdentityDeclaration
    
    
    type BusinessIdentity_IdentityAttribute_IdentityDeclaration [int32](https://pkg.go.dev/builtin#int32)

All possible settings regarding the declaration of an identity.

### BusinessIdentity_IdentityAttribute_IDENTITY_DECLARATION_UNSPECIFIED, BusinessIdentity_IdentityAttribute_SELF_IDENTIFIES_AS, BusinessIdentity_IdentityAttribute_DOES_NOT_SELF_IDENTIFY_AS
    
    
    const (
    	// Default value indicating that no selection was made.
    	BusinessIdentity_IdentityAttribute_IDENTITY_DECLARATION_UNSPECIFIED BusinessIdentity_IdentityAttribute_IdentityDeclaration = 0
    	// Indicates that the account identifies with the attribute.
    	BusinessIdentity_IdentityAttribute_SELF_IDENTIFIES_AS BusinessIdentity_IdentityAttribute_IdentityDeclaration = 1
    	// Indicates that the account does not identify with the attribute.
    	BusinessIdentity_IdentityAttribute_DOES_NOT_SELF_IDENTIFY_AS BusinessIdentity_IdentityAttribute_IdentityDeclaration = 2
    )

### func (BusinessIdentity_IdentityAttribute_IdentityDeclaration) Descriptor 
    
    
    func (BusinessIdentity_IdentityAttribute_IdentityDeclaration) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (BusinessIdentity_IdentityAttribute_IdentityDeclaration) Enum 
    
    
    func (x BusinessIdentity_IdentityAttribute_IdentityDeclaration) Enum() *BusinessIdentity_IdentityAttribute_IdentityDeclaration

### func (BusinessIdentity_IdentityAttribute_IdentityDeclaration) EnumDescriptor 
    
    
    func (BusinessIdentity_IdentityAttribute_IdentityDeclaration) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use BusinessIdentity_IdentityAttribute_IdentityDeclaration.Descriptor instead.

### func (BusinessIdentity_IdentityAttribute_IdentityDeclaration) Number 
    
    
    func (x BusinessIdentity_IdentityAttribute_IdentityDeclaration) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (BusinessIdentity_IdentityAttribute_IdentityDeclaration) String 
    
    
    func (x BusinessIdentity_IdentityAttribute_IdentityDeclaration) String() [string](https://pkg.go.dev/builtin#string)

### func (BusinessIdentity_IdentityAttribute_IdentityDeclaration) Type 
    
    
    func (BusinessIdentity_IdentityAttribute_IdentityDeclaration) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## BusinessIdentity_PromotionsConsent
    
    
    type BusinessIdentity_PromotionsConsent [int32](https://pkg.go.dev/builtin#int32)

All possible settings regarding promotions related to the business identity.

### BusinessIdentity_PROMOTIONS_CONSENT_UNSPECIFIED, BusinessIdentity_PROMOTIONS_CONSENT_GIVEN, BusinessIdentity_PROMOTIONS_CONSENT_DENIED
    
    
    const (
    	// Default value indicating that no selection was made.
    	BusinessIdentity_PROMOTIONS_CONSENT_UNSPECIFIED BusinessIdentity_PromotionsConsent = 0
    	// Indicates that the account consented to having their business identity
    	// used for promotions.
    	BusinessIdentity_PROMOTIONS_CONSENT_GIVEN BusinessIdentity_PromotionsConsent = 1
    	// Indicates that the account did not consent to having their business
    	// identity used for promotions.
    	BusinessIdentity_PROMOTIONS_CONSENT_DENIED BusinessIdentity_PromotionsConsent = 2
    )

### func (BusinessIdentity_PromotionsConsent) Descriptor 
    
    
    func (BusinessIdentity_PromotionsConsent) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (BusinessIdentity_PromotionsConsent) Enum 
    
    
    func (x BusinessIdentity_PromotionsConsent) Enum() *BusinessIdentity_PromotionsConsent

### func (BusinessIdentity_PromotionsConsent) EnumDescriptor 
    
    
    func (BusinessIdentity_PromotionsConsent) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use BusinessIdentity_PromotionsConsent.Descriptor instead.

### func (BusinessIdentity_PromotionsConsent) Number 
    
    
    func (x BusinessIdentity_PromotionsConsent) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (BusinessIdentity_PromotionsConsent) String 
    
    
    func (x BusinessIdentity_PromotionsConsent) String() [string](https://pkg.go.dev/builtin#string)

### func (BusinessIdentity_PromotionsConsent) Type 
    
    
    func (BusinessIdentity_PromotionsConsent) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## BusinessInfo
    
    
    type BusinessInfo struct {
    
    	// Identifier. The resource name of the business info.
    	// Format: `accounts/{account}/businessInfo`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. The address of the business.
    	Address *postaladdress.PostalAddress `protobuf:"bytes,2,opt,name=address,proto3,oneof" json:"address,omitempty"`
    	// Output only. The phone number of the business.
    	Phone *phone_number.PhoneNumber `protobuf:"bytes,3,opt,name=phone,proto3,oneof" json:"phone,omitempty"`
    	// Output only. The phone verification state of the business.
    	PhoneVerificationState *PhoneVerificationState `protobuf:"varint,4,opt,name=phone_verification_state,json=phoneVerificationState,proto3,enum=google.shopping.merchant.accounts.v1beta.PhoneVerificationState,oneof" json:"phone_verification_state,omitempty"`
    	// Optional. The customer service of the business.
    	CustomerService *CustomerService `protobuf:"bytes,5,opt,name=customer_service,json=customerService,proto3,oneof" json:"customer_service,omitempty"`
    	// Optional. The 10-digit [Korean business registration
    	// number](https://support.google.com/merchants/answer/9037766) separated with
    	// dashes in the format: XXX-XX-XXXXX.
    	KoreanBusinessRegistrationNumber *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,6,opt,name=korean_business_registration_number,json=koreanBusinessRegistrationNumber,proto3,oneof" json:"korean_business_registration_number,omitempty"`
    	// contains filtered or unexported fields
    }

Collection of information related to a business.

### func (*BusinessInfo) Descriptor 
    
    
    func (*BusinessInfo) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use BusinessInfo.ProtoReflect.Descriptor instead.

### func (*BusinessInfo) GetAddress 
    
    
    func (x *BusinessInfo) GetAddress() *[postaladdress](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/postaladdress).[PostalAddress](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/postaladdress#PostalAddress)

### func (*BusinessInfo) GetCustomerService 
    
    
    func (x *BusinessInfo) GetCustomerService() *CustomerService

### func (*BusinessInfo) GetKoreanBusinessRegistrationNumber 
    
    
    func (x *BusinessInfo) GetKoreanBusinessRegistrationNumber() [string](https://pkg.go.dev/builtin#string)

### func (*BusinessInfo) GetName 
    
    
    func (x *BusinessInfo) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*BusinessInfo) GetPhone 
    
    
    func (x *BusinessInfo) GetPhone() *[phone_number](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/phone_number).[PhoneNumber](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/phone_number#PhoneNumber)

### func (*BusinessInfo) GetPhoneVerificationState 
    
    
    func (x *BusinessInfo) GetPhoneVerificationState() PhoneVerificationState

### func (*BusinessInfo) ProtoMessage 
    
    
    func (*BusinessInfo) ProtoMessage()

### func (*BusinessInfo) ProtoReflect 
    
    
    func (x *BusinessInfo) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*BusinessInfo) Reset 
    
    
    func (x *BusinessInfo) Reset()

### func (*BusinessInfo) String 
    
    
    func (x *BusinessInfo) String() [string](https://pkg.go.dev/builtin#string)

## BusinessInfoServiceClient
    
    
    type BusinessInfoServiceClient interface {
    	// Retrieves the business info of an account.
    	GetBusinessInfo(ctx context.Context, in *GetBusinessInfoRequest, opts ...grpc.CallOption) (*BusinessInfo, [error](https://pkg.go.dev/builtin#error))
    	// Updates the business info of an account. Executing this method requires
    	// admin access.
    	UpdateBusinessInfo(ctx context.Context, in *UpdateBusinessInfoRequest, opts ...grpc.CallOption) (*BusinessInfo, [error](https://pkg.go.dev/builtin#error))
    }

BusinessInfoServiceClient is the client API for BusinessInfoService service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

### func NewBusinessInfoServiceClient 
    
    
    func NewBusinessInfoServiceClient(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) BusinessInfoServiceClient

## BusinessInfoServiceServer
    
    
    type BusinessInfoServiceServer interface {
    	// Retrieves the business info of an account.
    	GetBusinessInfo(context.Context, *GetBusinessInfoRequest) (*BusinessInfo, [error](https://pkg.go.dev/builtin#error))
    	// Updates the business info of an account. Executing this method requires
    	// admin access.
    	UpdateBusinessInfo(context.Context, *UpdateBusinessInfoRequest) (*BusinessInfo, [error](https://pkg.go.dev/builtin#error))
    }

BusinessInfoServiceServer is the server API for BusinessInfoService service. All implementations should embed UnimplementedBusinessInfoServiceServer for forward compatibility

## CarrierRate
    
    
    type CarrierRate struct {
    
    	// Required. Name of the carrier rate. Must be unique per rate group.
    	Name *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3,oneof" json:"name,omitempty"`
    	// Required. Carrier service, such as `"UPS"` or `"Fedex"`.
    	Carrier *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=carrier,proto3,oneof" json:"carrier,omitempty"`
    	// Required. Carrier service, such as `"ground"` or `"2 days"`.
    	CarrierService *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=carrier_service,json=carrierService,proto3,oneof" json:"carrier_service,omitempty"`
    	// Required. Shipping origin for this carrier rate.
    	OriginPostalCode *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=origin_postal_code,json=originPostalCode,proto3,oneof" json:"origin_postal_code,omitempty"`
    	// Optional. Multiplicative shipping rate modifier as a number in decimal
    	// notation. Can be negative. For example `"5.4"` increases the rate by 5.4%,
    	// `"-3"` decreases the rate by 3%.
    	PercentageAdjustment *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=percentage_adjustment,json=percentageAdjustment,proto3,oneof" json:"percentage_adjustment,omitempty"`
    	// Optional. Additive shipping rate modifier. Can be negative. For example
    	// `{ "amount_micros": 1, "currency_code" : "USD" }` adds $1 to the rate,
    	// `{ "amount_micros": -3, "currency_code" : "USD" }` removes $3 from the
    	// rate.
    	FlatAdjustment *typepb.Price `protobuf:"bytes,6,opt,name=flat_adjustment,json=flatAdjustment,proto3,oneof" json:"flat_adjustment,omitempty"`
    	// contains filtered or unexported fields
    }

A list of carrier rates that can be referred to by `main_table` or `single_value`.

### func (*CarrierRate) Descriptor 
    
    
    func (*CarrierRate) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CarrierRate.ProtoReflect.Descriptor instead.

### func (*CarrierRate) GetCarrier 
    
    
    func (x *CarrierRate) GetCarrier() [string](https://pkg.go.dev/builtin#string)

### func (*CarrierRate) GetCarrierService 
    
    
    func (x *CarrierRate) GetCarrierService() [string](https://pkg.go.dev/builtin#string)

### func (*CarrierRate) GetFlatAdjustment 
    
    
    func (x *CarrierRate) GetFlatAdjustment() *[typepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/type/typepb).[Price](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/type/typepb#cloud_google_com_go_shopping_type_typepb_Price)

### func (*CarrierRate) GetName 
    
    
    func (x *CarrierRate) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*CarrierRate) GetOriginPostalCode 
    
    
    func (x *CarrierRate) GetOriginPostalCode() [string](https://pkg.go.dev/builtin#string)

### func (*CarrierRate) GetPercentageAdjustment 
    
    
    func (x *CarrierRate) GetPercentageAdjustment() [string](https://pkg.go.dev/builtin#string)

### func (*CarrierRate) ProtoMessage 
    
    
    func (*CarrierRate) ProtoMessage()

### func (*CarrierRate) ProtoReflect 
    
    
    func (x *CarrierRate) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CarrierRate) Reset 
    
    
    func (x *CarrierRate) Reset()

### func (*CarrierRate) String 
    
    
    func (x *CarrierRate) String() [string](https://pkg.go.dev/builtin#string)

## CheckoutSettings
    
    
    type CheckoutSettings struct {
    
    	// Identifier. The resource name of the program configuration settings.
    	// Format: `accounts/{account}/programs/{program}/checkoutSettings`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// URI settings for cart or checkout URL.
    	UriSettings *UriSettings `protobuf:"bytes,2,opt,name=uri_settings,json=uriSettings,proto3,oneof" json:"uri_settings,omitempty"`
    	// Optional. The destinations to which the checkout program applies, valid
    	// destination values are `SHOPPING_ADS`, `FREE_LISTINGS`
    	EligibleDestinations []typepb.Destination_DestinationEnum `protobuf:"varint,8,rep,packed,name=eligible_destinations,json=eligibleDestinations,proto3,enum=google.shopping.type.Destination_DestinationEnum" json:"eligible_destinations,omitempty"`
    	// Output only. Reflects the merchant enrollment state in `Checkout` program.
    	EnrollmentState *CheckoutSettings_CheckoutEnrollmentState `protobuf:"varint,3,opt,name=enrollment_state,json=enrollmentState,proto3,enum=google.shopping.merchant.accounts.v1beta.CheckoutSettings_CheckoutEnrollmentState,oneof" json:"enrollment_state,omitempty"`
    	// Output only. Reflects the merchant review state in `Checkout` program.
    	// This is set based on the data quality reviews of the URL provided by
    	// the merchant.
    	// A merchant with enrollment state
    	// as `ENROLLED` can be in the following review states: `IN_REVIEW`,
    	// `APPROVED` or `DISAPPROVED`. A merchant must be in an `enrollment_state` of
    	// `ENROLLED` before a review can begin for the merchant.For more details,
    	// check the help center doc.
    	ReviewState *CheckoutSettings_CheckoutReviewState `protobuf:"varint,4,opt,name=review_state,json=reviewState,proto3,enum=google.shopping.merchant.accounts.v1beta.CheckoutSettings_CheckoutReviewState,oneof" json:"review_state,omitempty"`
    	// Output only. The effective value of `uri_settings` for a given merchant. If
    	// account level settings are present then this value will be a copy of url
    	// settings. Otherwise, it will have the value of the parent account (for only
    	// marketplace sellers).
    	EffectiveUriSettings *UriSettings `protobuf:"bytes,5,opt,name=effective_uri_settings,json=effectiveUriSettings,proto3" json:"effective_uri_settings,omitempty"`
    	// Output only. The effective value of enrollment_state for a given merchant
    	// ID. If account level settings are present then this value will be a copy of
    	// the account level settings. Otherwise, it will have the value of the parent
    	// account (for only marketplace sellers).
    	EffectiveEnrollmentState *CheckoutSettings_CheckoutEnrollmentState `protobuf:"varint,6,opt,name=effective_enrollment_state,json=effectiveEnrollmentState,proto3,enum=google.shopping.merchant.accounts.v1beta.CheckoutSettings_CheckoutEnrollmentState,oneof" json:"effective_enrollment_state,omitempty"`
    	// Output only. The effective value of `review_state` for a given merchant ID.
    	// If account level settings are present then this value will be a copy of the
    	// account level settings. Otherwise, it will have the value of the parent
    	// account (for only marketplace sellers).
    	EffectiveReviewState *CheckoutSettings_CheckoutReviewState `protobuf:"varint,7,opt,name=effective_review_state,json=effectiveReviewState,proto3,enum=google.shopping.merchant.accounts.v1beta.CheckoutSettings_CheckoutReviewState,oneof" json:"effective_review_state,omitempty"`
    	// contains filtered or unexported fields
    }

[CheckoutSettings](https://support.google.com/merchants/answer/13945960) for a specific merchant.

### func (*CheckoutSettings) Descriptor 
    
    
    func (*CheckoutSettings) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CheckoutSettings.ProtoReflect.Descriptor instead.

### func (*CheckoutSettings) GetEffectiveEnrollmentState 
    
    
    func (x *CheckoutSettings) GetEffectiveEnrollmentState() CheckoutSettings_CheckoutEnrollmentState

### func (*CheckoutSettings) GetEffectiveReviewState 
    
    
    func (x *CheckoutSettings) GetEffectiveReviewState() CheckoutSettings_CheckoutReviewState

### func (*CheckoutSettings) GetEffectiveUriSettings 
    
    
    func (x *CheckoutSettings) GetEffectiveUriSettings() *UriSettings

### func (*CheckoutSettings) GetEligibleDestinations 
    
    
    func (x *CheckoutSettings) GetEligibleDestinations() [][typepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/type/typepb).[Destination_DestinationEnum](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/type/typepb#cloud_google_com_go_shopping_type_typepb_Destination_DestinationEnum)

### func (*CheckoutSettings) GetEnrollmentState 
    
    
    func (x *CheckoutSettings) GetEnrollmentState() CheckoutSettings_CheckoutEnrollmentState

### func (*CheckoutSettings) GetName 
    
    
    func (x *CheckoutSettings) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*CheckoutSettings) GetReviewState 
    
    
    func (x *CheckoutSettings) GetReviewState() CheckoutSettings_CheckoutReviewState

### func (*CheckoutSettings) GetUriSettings 
    
    
    func (x *CheckoutSettings) GetUriSettings() *UriSettings

### func (*CheckoutSettings) ProtoMessage 
    
    
    func (*CheckoutSettings) ProtoMessage()

### func (*CheckoutSettings) ProtoReflect 
    
    
    func (x *CheckoutSettings) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CheckoutSettings) Reset 
    
    
    func (x *CheckoutSettings) Reset()

### func (*CheckoutSettings) String 
    
    
    func (x *CheckoutSettings) String() [string](https://pkg.go.dev/builtin#string)

## CheckoutSettingsServiceClient
    
    
    type CheckoutSettingsServiceClient interface {
    	// Gets `CheckoutSettings` for the given merchant. This includes
    	// information about review state, enrollment state and URL settings.
    	GetCheckoutSettings(ctx context.Context, in *GetCheckoutSettingsRequest, opts ...grpc.CallOption) (*CheckoutSettings, [error](https://pkg.go.dev/builtin#error))
    	// Creates `CheckoutSettings` for the given merchant.
    	CreateCheckoutSettings(ctx context.Context, in *CreateCheckoutSettingsRequest, opts ...grpc.CallOption) (*CheckoutSettings, [error](https://pkg.go.dev/builtin#error))
    	// Updates `CheckoutSettings` for the given merchant.
    	UpdateCheckoutSettings(ctx context.Context, in *UpdateCheckoutSettingsRequest, opts ...grpc.CallOption) (*CheckoutSettings, [error](https://pkg.go.dev/builtin#error))
    	// Deletes `CheckoutSettings` and unenrolls merchant from
    	// `Checkout` program.
    	DeleteCheckoutSettings(ctx context.Context, in *DeleteCheckoutSettingsRequest, opts ...grpc.CallOption) (*emptypb.Empty, [error](https://pkg.go.dev/builtin#error))
    }

CheckoutSettingsServiceClient is the client API for CheckoutSettingsService service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

### func NewCheckoutSettingsServiceClient 
    
    
    func NewCheckoutSettingsServiceClient(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) CheckoutSettingsServiceClient

## CheckoutSettingsServiceServer
    
    
    type CheckoutSettingsServiceServer interface {
    	// Gets `CheckoutSettings` for the given merchant. This includes
    	// information about review state, enrollment state and URL settings.
    	GetCheckoutSettings(context.Context, *GetCheckoutSettingsRequest) (*CheckoutSettings, [error](https://pkg.go.dev/builtin#error))
    	// Creates `CheckoutSettings` for the given merchant.
    	CreateCheckoutSettings(context.Context, *CreateCheckoutSettingsRequest) (*CheckoutSettings, [error](https://pkg.go.dev/builtin#error))
    	// Updates `CheckoutSettings` for the given merchant.
    	UpdateCheckoutSettings(context.Context, *UpdateCheckoutSettingsRequest) (*CheckoutSettings, [error](https://pkg.go.dev/builtin#error))
    	// Deletes `CheckoutSettings` and unenrolls merchant from
    	// `Checkout` program.
    	DeleteCheckoutSettings(context.Context, *DeleteCheckoutSettingsRequest) (*emptypb.Empty, [error](https://pkg.go.dev/builtin#error))
    }

CheckoutSettingsServiceServer is the server API for CheckoutSettingsService service. All implementations should embed UnimplementedCheckoutSettingsServiceServer for forward compatibility

## CheckoutSettings_CheckoutEnrollmentState
    
    
    type CheckoutSettings_CheckoutEnrollmentState [int32](https://pkg.go.dev/builtin#int32)

Enum indicating the enrollment state of merchant in `Checkout` program.

### CheckoutSettings_CHECKOUT_ENROLLMENT_STATE_UNSPECIFIED, CheckoutSettings_INACTIVE, CheckoutSettings_ENROLLED, CheckoutSettings_OPTED_OUT
    
    
    const (
    	// Default enrollment state when enrollment state is not specified.
    	CheckoutSettings_CHECKOUT_ENROLLMENT_STATE_UNSPECIFIED CheckoutSettings_CheckoutEnrollmentState = 0
    	// Merchant has not enrolled into the program.
    	CheckoutSettings_INACTIVE CheckoutSettings_CheckoutEnrollmentState = 1
    	// Merchant has enrolled into the program by providing either an
    	// account level URL or checkout URLs as part of their feed.
    	CheckoutSettings_ENROLLED CheckoutSettings_CheckoutEnrollmentState = 2
    	// Merchant has previously enrolled but opted out of the program.
    	CheckoutSettings_OPTED_OUT CheckoutSettings_CheckoutEnrollmentState = 3
    )

### func (CheckoutSettings_CheckoutEnrollmentState) Descriptor 
    
    
    func (CheckoutSettings_CheckoutEnrollmentState) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (CheckoutSettings_CheckoutEnrollmentState) Enum 
    
    
    func (x CheckoutSettings_CheckoutEnrollmentState) Enum() *CheckoutSettings_CheckoutEnrollmentState

### func (CheckoutSettings_CheckoutEnrollmentState) EnumDescriptor 
    
    
    func (CheckoutSettings_CheckoutEnrollmentState) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CheckoutSettings_CheckoutEnrollmentState.Descriptor instead.

### func (CheckoutSettings_CheckoutEnrollmentState) Number 
    
    
    func (x CheckoutSettings_CheckoutEnrollmentState) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (CheckoutSettings_CheckoutEnrollmentState) String 
    
    
    func (x CheckoutSettings_CheckoutEnrollmentState) String() [string](https://pkg.go.dev/builtin#string)

### func (CheckoutSettings_CheckoutEnrollmentState) Type 
    
    
    func (CheckoutSettings_CheckoutEnrollmentState) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## CheckoutSettings_CheckoutReviewState
    
    
    type CheckoutSettings_CheckoutReviewState [int32](https://pkg.go.dev/builtin#int32)

Enum indicating the review state of merchant in `Checkout` program.

### CheckoutSettings_CHECKOUT_REVIEW_STATE_UNSPECIFIED, CheckoutSettings_IN_REVIEW, CheckoutSettings_APPROVED, CheckoutSettings_DISAPPROVED
    
    
    const (
    	// Default review state when review state is not specified.
    	CheckoutSettings_CHECKOUT_REVIEW_STATE_UNSPECIFIED CheckoutSettings_CheckoutReviewState = 0
    	// Merchant provided URLs are being reviewed for data quality issues.
    	CheckoutSettings_IN_REVIEW CheckoutSettings_CheckoutReviewState = 1
    	// Merchant account has been approved. Indicates the data quality checks
    	// have passed.
    	CheckoutSettings_APPROVED CheckoutSettings_CheckoutReviewState = 2
    	// Merchant account has been disapproved due to data quality issues.
    	CheckoutSettings_DISAPPROVED CheckoutSettings_CheckoutReviewState = 3
    )

### func (CheckoutSettings_CheckoutReviewState) Descriptor 
    
    
    func (CheckoutSettings_CheckoutReviewState) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (CheckoutSettings_CheckoutReviewState) Enum 
    
    
    func (x CheckoutSettings_CheckoutReviewState) Enum() *CheckoutSettings_CheckoutReviewState

### func (CheckoutSettings_CheckoutReviewState) EnumDescriptor 
    
    
    func (CheckoutSettings_CheckoutReviewState) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CheckoutSettings_CheckoutReviewState.Descriptor instead.

### func (CheckoutSettings_CheckoutReviewState) Number 
    
    
    func (x CheckoutSettings_CheckoutReviewState) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (CheckoutSettings_CheckoutReviewState) String 
    
    
    func (x CheckoutSettings_CheckoutReviewState) String() [string](https://pkg.go.dev/builtin#string)

### func (CheckoutSettings_CheckoutReviewState) Type 
    
    
    func (CheckoutSettings_CheckoutReviewState) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## ClaimHomepageRequest
    
    
    type ClaimHomepageRequest struct {
    
    	// Required. The name of the homepage to claim.
    	// Format: `accounts/{account}/homepage`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the `ClaimHomepage` method.

### func (*ClaimHomepageRequest) Descriptor 
    
    
    func (*ClaimHomepageRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ClaimHomepageRequest.ProtoReflect.Descriptor instead.

### func (*ClaimHomepageRequest) GetName 
    
    
    func (x *ClaimHomepageRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*ClaimHomepageRequest) ProtoMessage 
    
    
    func (*ClaimHomepageRequest) ProtoMessage()

### func (*ClaimHomepageRequest) ProtoReflect 
    
    
    func (x *ClaimHomepageRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ClaimHomepageRequest) Reset 
    
    
    func (x *ClaimHomepageRequest) Reset()

### func (*ClaimHomepageRequest) String 
    
    
    func (x *ClaimHomepageRequest) String() [string](https://pkg.go.dev/builtin#string)

## CreateAndConfigureAccountRequest
    
    
    type CreateAndConfigureAccountRequest struct {
    
    	// Required. The account to be created.
    	Account *Account `protobuf:"bytes,1,opt,name=account,proto3" json:"account,omitempty"`
    	// Optional. Users to be added to the account.
    	Users []*CreateUserRequest `protobuf:"bytes,2,rep,name=users,proto3" json:"users,omitempty"`
    	// Optional. The Terms of Service (ToS) to be accepted immediately upon
    	// account creation.
    	AcceptTermsOfService *CreateAndConfigureAccountRequest_AcceptTermsOfService `protobuf:"bytes,3,opt,name=accept_terms_of_service,json=acceptTermsOfService,proto3,oneof" json:"accept_terms_of_service,omitempty"`
    	// Required. An account service between the account to be created and the
    	// provider account is initialized as part of the creation. At least one such
    	// service needs to be provided. Currently exactly one of these needs to be
    	// `account_aggregation`, which means you can only create sub accounts, not
    	// standalone account through this method. Additional `account_management` or
    	// `product_management` services may be provided.
    	Service []*CreateAndConfigureAccountRequest_AddAccountService `protobuf:"bytes,4,rep,name=service,proto3" json:"service,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the `CreateAndConfigureAccount` method.

### func (*CreateAndConfigureAccountRequest) Descriptor 
    
    
    func (*CreateAndConfigureAccountRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateAndConfigureAccountRequest.ProtoReflect.Descriptor instead.

### func (*CreateAndConfigureAccountRequest) GetAcceptTermsOfService 
    
    
    func (x *CreateAndConfigureAccountRequest) GetAcceptTermsOfService() *CreateAndConfigureAccountRequest_AcceptTermsOfService

### func (*CreateAndConfigureAccountRequest) GetAccount 
    
    
    func (x *CreateAndConfigureAccountRequest) GetAccount() *Account

### func (*CreateAndConfigureAccountRequest) GetService 
    
    
    func (x *CreateAndConfigureAccountRequest) GetService() []*CreateAndConfigureAccountRequest_AddAccountService

### func (*CreateAndConfigureAccountRequest) GetUsers 
    
    
    func (x *CreateAndConfigureAccountRequest) GetUsers() []*CreateUserRequest

### func (*CreateAndConfigureAccountRequest) ProtoMessage 
    
    
    func (*CreateAndConfigureAccountRequest) ProtoMessage()

### func (*CreateAndConfigureAccountRequest) ProtoReflect 
    
    
    func (x *CreateAndConfigureAccountRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreateAndConfigureAccountRequest) Reset 
    
    
    func (x *CreateAndConfigureAccountRequest) Reset()

### func (*CreateAndConfigureAccountRequest) String 
    
    
    func (x *CreateAndConfigureAccountRequest) String() [string](https://pkg.go.dev/builtin#string)

## CreateAndConfigureAccountRequest_AcceptTermsOfService
    
    
    type CreateAndConfigureAccountRequest_AcceptTermsOfService struct {
    
    	// Required. The resource name of the terms of service version in the format
    	// `termsOfService/{version}`. To retrieve the latest version, use the
    	// [termsOfService.retrieveLatest](/merchant/api/reference/rest/accounts_v1beta/termsOfService/retrieveLatest)
    	// method.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Required. Region code as defined by [CLDR](https://cldr.unicode.org/).
    	// This is either a country when the ToS applies specifically to that
    	// country or `001` when it applies globally.
    	RegionCode [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=region_code,json=regionCode,proto3" json:"region_code,omitempty"`
    	// contains filtered or unexported fields
    }

Reference to a Terms of Service resource.

### func (*CreateAndConfigureAccountRequest_AcceptTermsOfService) Descriptor 
    
    
    func (*CreateAndConfigureAccountRequest_AcceptTermsOfService) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateAndConfigureAccountRequest_AcceptTermsOfService.ProtoReflect.Descriptor instead.

### func (*CreateAndConfigureAccountRequest_AcceptTermsOfService) GetName 
    
    
    func (x *CreateAndConfigureAccountRequest_AcceptTermsOfService) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*CreateAndConfigureAccountRequest_AcceptTermsOfService) GetRegionCode 
    
    
    func (x *CreateAndConfigureAccountRequest_AcceptTermsOfService) GetRegionCode() [string](https://pkg.go.dev/builtin#string)

### func (*CreateAndConfigureAccountRequest_AcceptTermsOfService) ProtoMessage 
    
    
    func (*CreateAndConfigureAccountRequest_AcceptTermsOfService) ProtoMessage()

### func (*CreateAndConfigureAccountRequest_AcceptTermsOfService) ProtoReflect 
    
    
    func (x *CreateAndConfigureAccountRequest_AcceptTermsOfService) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreateAndConfigureAccountRequest_AcceptTermsOfService) Reset 
    
    
    func (x *CreateAndConfigureAccountRequest_AcceptTermsOfService) Reset()

### func (*CreateAndConfigureAccountRequest_AcceptTermsOfService) String 
    
    
    func (x *CreateAndConfigureAccountRequest_AcceptTermsOfService) String() [string](https://pkg.go.dev/builtin#string)

## CreateAndConfigureAccountRequest_AddAccountService
    
    
    type CreateAndConfigureAccountRequest_AddAccountService struct {
    
    	// The service type to be added.
    	//
    	// Types that are valid to be assigned to ServiceType:
    	//
    	//	*CreateAndConfigureAccountRequest_AddAccountService_AccountAggregation
    	ServiceType isCreateAndConfigureAccountRequest_AddAccountService_ServiceType `protobuf_oneof:"service_type"`
    	// Optional. The provider of the service.
    	// Format: `accounts/{account}`
    	Provider *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=provider,proto3,oneof" json:"provider,omitempty"`
    	// contains filtered or unexported fields
    }

Additional instructions to add account services during creation of the account.

### func (*CreateAndConfigureAccountRequest_AddAccountService) Descriptor 
    
    
    func (*CreateAndConfigureAccountRequest_AddAccountService) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateAndConfigureAccountRequest_AddAccountService.ProtoReflect.Descriptor instead.

### func (*CreateAndConfigureAccountRequest_AddAccountService) GetAccountAggregation 
    
    
    func (x *CreateAndConfigureAccountRequest_AddAccountService) GetAccountAggregation() *AccountAggregation

### func (*CreateAndConfigureAccountRequest_AddAccountService) GetProvider 
    
    
    func (x *CreateAndConfigureAccountRequest_AddAccountService) GetProvider() [string](https://pkg.go.dev/builtin#string)

### func (*CreateAndConfigureAccountRequest_AddAccountService) GetServiceType 
    
    
    func (x *CreateAndConfigureAccountRequest_AddAccountService) GetServiceType() isCreateAndConfigureAccountRequest_AddAccountService_ServiceType

### func (*CreateAndConfigureAccountRequest_AddAccountService) ProtoMessage 
    
    
    func (*CreateAndConfigureAccountRequest_AddAccountService) ProtoMessage()

### func (*CreateAndConfigureAccountRequest_AddAccountService) ProtoReflect 
    
    
    func (x *CreateAndConfigureAccountRequest_AddAccountService) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreateAndConfigureAccountRequest_AddAccountService) Reset 
    
    
    func (x *CreateAndConfigureAccountRequest_AddAccountService) Reset()

### func (*CreateAndConfigureAccountRequest_AddAccountService) String 
    
    
    func (x *CreateAndConfigureAccountRequest_AddAccountService) String() [string](https://pkg.go.dev/builtin#string)

## CreateAndConfigureAccountRequest_AddAccountService_AccountAggregation
    
    
    type CreateAndConfigureAccountRequest_AddAccountService_AccountAggregation struct {
    	// The provider is an
    	// [aggregator](https://support.google.com/merchants/answer/188487) for
    	// the account. Payload for service type Account Aggregation.
    	AccountAggregation *AccountAggregation `protobuf:"bytes,103,opt,name=account_aggregation,json=accountAggregation,proto3,oneof"`
    }

## CreateCheckoutSettingsRequest
    
    
    type CreateCheckoutSettingsRequest struct {
    
    	// Required. The merchant account for which the `CheckoutSettings` will be
    	// created.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Required. The `CheckoutSettings` object to create.
    	CheckoutSettings *CheckoutSettings `protobuf:"bytes,2,opt,name=checkout_settings,json=checkoutSettings,proto3" json:"checkout_settings,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the `CreateCheckoutSettings` method.

### func (*CreateCheckoutSettingsRequest) Descriptor 
    
    
    func (*CreateCheckoutSettingsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateCheckoutSettingsRequest.ProtoReflect.Descriptor instead.

### func (*CreateCheckoutSettingsRequest) GetCheckoutSettings 
    
    
    func (x *CreateCheckoutSettingsRequest) GetCheckoutSettings() *CheckoutSettings

### func (*CreateCheckoutSettingsRequest) GetParent 
    
    
    func (x *CreateCheckoutSettingsRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*CreateCheckoutSettingsRequest) ProtoMessage 
    
    
    func (*CreateCheckoutSettingsRequest) ProtoMessage()

### func (*CreateCheckoutSettingsRequest) ProtoReflect 
    
    
    func (x *CreateCheckoutSettingsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreateCheckoutSettingsRequest) Reset 
    
    
    func (x *CreateCheckoutSettingsRequest) Reset()

### func (*CreateCheckoutSettingsRequest) String 
    
    
    func (x *CreateCheckoutSettingsRequest) String() [string](https://pkg.go.dev/builtin#string)

## CreateOmnichannelSettingRequest
    
    
    type CreateOmnichannelSettingRequest struct {
    
    	// Required. The parent resource where this omnichannel setting will be
    	// created. Format: `accounts/{account}`
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Required. The omnichannel setting to create.
    	OmnichannelSetting *OmnichannelSetting `protobuf:"bytes,2,opt,name=omnichannel_setting,json=omnichannelSetting,proto3" json:"omnichannel_setting,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the CreateOmnichannelSetting method.

### func (*CreateOmnichannelSettingRequest) Descriptor 
    
    
    func (*CreateOmnichannelSettingRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateOmnichannelSettingRequest.ProtoReflect.Descriptor instead.

### func (*CreateOmnichannelSettingRequest) GetOmnichannelSetting 
    
    
    func (x *CreateOmnichannelSettingRequest) GetOmnichannelSetting() *OmnichannelSetting

### func (*CreateOmnichannelSettingRequest) GetParent 
    
    
    func (x *CreateOmnichannelSettingRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*CreateOmnichannelSettingRequest) ProtoMessage 
    
    
    func (*CreateOmnichannelSettingRequest) ProtoMessage()

### func (*CreateOmnichannelSettingRequest) ProtoReflect 
    
    
    func (x *CreateOmnichannelSettingRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreateOmnichannelSettingRequest) Reset 
    
    
    func (x *CreateOmnichannelSettingRequest) Reset()

### func (*CreateOmnichannelSettingRequest) String 
    
    
    func (x *CreateOmnichannelSettingRequest) String() [string](https://pkg.go.dev/builtin#string)

## CreateOnlineReturnPolicyRequest
    
    
    type CreateOnlineReturnPolicyRequest struct {
    
    	// Required. The merchant account for which the return policy will be created.
    	// Format: `accounts/{account}`
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Required. The return policy object to create.
    	OnlineReturnPolicy *OnlineReturnPolicy `protobuf:"bytes,2,opt,name=online_return_policy,json=onlineReturnPolicy,proto3" json:"online_return_policy,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the `CreateOnlineReturnPolicy` method.

### func (*CreateOnlineReturnPolicyRequest) Descriptor 
    
    
    func (*CreateOnlineReturnPolicyRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateOnlineReturnPolicyRequest.ProtoReflect.Descriptor instead.

### func (*CreateOnlineReturnPolicyRequest) GetOnlineReturnPolicy 
    
    
    func (x *CreateOnlineReturnPolicyRequest) GetOnlineReturnPolicy() *OnlineReturnPolicy

### func (*CreateOnlineReturnPolicyRequest) GetParent 
    
    
    func (x *CreateOnlineReturnPolicyRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*CreateOnlineReturnPolicyRequest) ProtoMessage 
    
    
    func (*CreateOnlineReturnPolicyRequest) ProtoMessage()

### func (*CreateOnlineReturnPolicyRequest) ProtoReflect 
    
    
    func (x *CreateOnlineReturnPolicyRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreateOnlineReturnPolicyRequest) Reset 
    
    
    func (x *CreateOnlineReturnPolicyRequest) Reset()

### func (*CreateOnlineReturnPolicyRequest) String 
    
    
    func (x *CreateOnlineReturnPolicyRequest) String() [string](https://pkg.go.dev/builtin#string)

## CreateRegionRequest
    
    
    type CreateRegionRequest struct {
    
    	// Required. The account to create a region for.
    	// Format: `accounts/{account}`
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Required. The identifier for the region, unique over all regions of the
    	// same account.
    	RegionId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=region_id,json=regionId,proto3" json:"region_id,omitempty"`
    	// Required. The region to create.
    	Region *Region `protobuf:"bytes,3,opt,name=region,proto3" json:"region,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the `CreateRegion` method.

### func (*CreateRegionRequest) Descriptor 
    
    
    func (*CreateRegionRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateRegionRequest.ProtoReflect.Descriptor instead.

### func (*CreateRegionRequest) GetParent 
    
    
    func (x *CreateRegionRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*CreateRegionRequest) GetRegion 
    
    
    func (x *CreateRegionRequest) GetRegion() *Region

### func (*CreateRegionRequest) GetRegionId 
    
    
    func (x *CreateRegionRequest) GetRegionId() [string](https://pkg.go.dev/builtin#string)

### func (*CreateRegionRequest) ProtoMessage 
    
    
    func (*CreateRegionRequest) ProtoMessage()

### func (*CreateRegionRequest) ProtoReflect 
    
    
    func (x *CreateRegionRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreateRegionRequest) Reset 
    
    
    func (x *CreateRegionRequest) Reset()

### func (*CreateRegionRequest) String 
    
    
    func (x *CreateRegionRequest) String() [string](https://pkg.go.dev/builtin#string)

## CreateUserRequest
    
    
    type CreateUserRequest struct {
    
    	// Required. The resource name of the account for which a user will be
    	// created. Format: `accounts/{account}`
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Required. The email address of the user (for example,
    	// `john.doe@gmail.com`).
    	UserId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=user_id,json=userId,proto3" json:"user_id,omitempty"`
    	// Required. The user to create.
    	User *User `protobuf:"bytes,3,opt,name=user,proto3" json:"user,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the `CreateUser` method.

### func (*CreateUserRequest) Descriptor 
    
    
    func (*CreateUserRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateUserRequest.ProtoReflect.Descriptor instead.

### func (*CreateUserRequest) GetParent 
    
    
    func (x *CreateUserRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*CreateUserRequest) GetUser 
    
    
    func (x *CreateUserRequest) GetUser() *User

### func (*CreateUserRequest) GetUserId 
    
    
    func (x *CreateUserRequest) GetUserId() [string](https://pkg.go.dev/builtin#string)

### func (*CreateUserRequest) ProtoMessage 
    
    
    func (*CreateUserRequest) ProtoMessage()

### func (*CreateUserRequest) ProtoReflect 
    
    
    func (x *CreateUserRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreateUserRequest) Reset 
    
    
    func (x *CreateUserRequest) Reset()

### func (*CreateUserRequest) String 
    
    
    func (x *CreateUserRequest) String() [string](https://pkg.go.dev/builtin#string)

## CustomerService
    
    
    type CustomerService struct {
    
    	// Optional. The URI where customer service may be found.
    	Uri *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=uri,proto3,oneof" json:"uri,omitempty"`
    	// Optional. The email address where customer service may be reached.
    	Email *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=email,proto3,oneof" json:"email,omitempty"`
    	// Optional. The phone number where customer service may be called.
    	Phone *phone_number.PhoneNumber `protobuf:"bytes,3,opt,name=phone,proto3,oneof" json:"phone,omitempty"`
    	// contains filtered or unexported fields
    }

Customer service information.

### func (*CustomerService) Descriptor 
    
    
    func (*CustomerService) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CustomerService.ProtoReflect.Descriptor instead.

### func (*CustomerService) GetEmail 
    
    
    func (x *CustomerService) GetEmail() [string](https://pkg.go.dev/builtin#string)

### func (*CustomerService) GetPhone 
    
    
    func (x *CustomerService) GetPhone() *[phone_number](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/phone_number).[PhoneNumber](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/phone_number#PhoneNumber)

### func (*CustomerService) GetUri 
    
    
    func (x *CustomerService) GetUri() [string](https://pkg.go.dev/builtin#string)

### func (*CustomerService) ProtoMessage 
    
    
    func (*CustomerService) ProtoMessage()

### func (*CustomerService) ProtoReflect 
    
    
    func (x *CustomerService) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CustomerService) Reset 
    
    
    func (x *CustomerService) Reset()

### func (*CustomerService) String 
    
    
    func (x *CustomerService) String() [string](https://pkg.go.dev/builtin#string)

## CutoffTime
    
    
    type CutoffTime struct {
    
    	// Required. Hour of the cutoff time until which an order has to be placed to
    	// be processed in the same day.
    	Hour *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,1,opt,name=hour,proto3,oneof" json:"hour,omitempty"`
    	// Required. Minute of the cutoff time until which an order has to be placed
    	// to be processed in the same day.
    	Minute *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=minute,proto3,oneof" json:"minute,omitempty"`
    	// Required. [Timezone
    	// identifier](https://developers.google.com/adwords/api/docs/appendix/codes-formats#timezone-ids)
    	// For example "Europe/Zurich".
    	TimeZone *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=time_zone,json=timeZone,proto3,oneof" json:"time_zone,omitempty"`
    	// contains filtered or unexported fields
    }

Business days cutoff time definition.

### func (*CutoffTime) Descriptor 
    
    
    func (*CutoffTime) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CutoffTime.ProtoReflect.Descriptor instead.

### func (*CutoffTime) GetHour 
    
    
    func (x *CutoffTime) GetHour() [int32](https://pkg.go.dev/builtin#int32)

### func (*CutoffTime) GetMinute 
    
    
    func (x *CutoffTime) GetMinute() [int32](https://pkg.go.dev/builtin#int32)

### func (*CutoffTime) GetTimeZone 
    
    
    func (x *CutoffTime) GetTimeZone() [string](https://pkg.go.dev/builtin#string)

### func (*CutoffTime) ProtoMessage 
    
    
    func (*CutoffTime) ProtoMessage()

### func (*CutoffTime) ProtoReflect 
    
    
    func (x *CutoffTime) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CutoffTime) Reset 
    
    
    func (x *CutoffTime) Reset()

### func (*CutoffTime) String 
    
    
    func (x *CutoffTime) String() [string](https://pkg.go.dev/builtin#string)

## DeleteAccountRequest
    
    
    type DeleteAccountRequest struct {
    
    	// Required. The name of the account to delete.
    	// Format: `accounts/{account}`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. If set to `true`, the account is deleted even if it provides
    	// services to other accounts or has processed offers.
    	Force [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,2,opt,name=force,proto3" json:"force,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the `DeleteAccount` method.

### func (*DeleteAccountRequest) Descriptor 
    
    
    func (*DeleteAccountRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DeleteAccountRequest.ProtoReflect.Descriptor instead.

### func (*DeleteAccountRequest) GetForce 
    
    
    func (x *DeleteAccountRequest) GetForce() [bool](https://pkg.go.dev/builtin#bool)

### func (*DeleteAccountRequest) GetName 
    
    
    func (x *DeleteAccountRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteAccountRequest) ProtoMessage 
    
    
    func (*DeleteAccountRequest) ProtoMessage()

### func (*DeleteAccountRequest) ProtoReflect 
    
    
    func (x *DeleteAccountRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DeleteAccountRequest) Reset 
    
    
    func (x *DeleteAccountRequest) Reset()

### func (*DeleteAccountRequest) String 
    
    
    func (x *DeleteAccountRequest) String() [string](https://pkg.go.dev/builtin#string)

## DeleteCheckoutSettingsRequest
    
    
    type DeleteCheckoutSettingsRequest struct {
    
    	// Required. The name/identifier of the merchant account.
    	// Format: `accounts/{account}/programs/{program}/checkoutSettings`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the `DeleteCheckoutSettings` method.

### func (*DeleteCheckoutSettingsRequest) Descriptor 
    
    
    func (*DeleteCheckoutSettingsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DeleteCheckoutSettingsRequest.ProtoReflect.Descriptor instead.

### func (*DeleteCheckoutSettingsRequest) GetName 
    
    
    func (x *DeleteCheckoutSettingsRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteCheckoutSettingsRequest) ProtoMessage 
    
    
    func (*DeleteCheckoutSettingsRequest) ProtoMessage()

### func (*DeleteCheckoutSettingsRequest) ProtoReflect 
    
    
    func (x *DeleteCheckoutSettingsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DeleteCheckoutSettingsRequest) Reset 
    
    
    func (x *DeleteCheckoutSettingsRequest) Reset()

### func (*DeleteCheckoutSettingsRequest) String 
    
    
    func (x *DeleteCheckoutSettingsRequest) String() [string](https://pkg.go.dev/builtin#string)

## DeleteOnlineReturnPolicyRequest
    
    
    type DeleteOnlineReturnPolicyRequest struct {
    
    	// Required. The name of the return policy to delete.
    	// Format: `accounts/{account}/onlineReturnPolicies/{return_policy}`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the `DeleteOnlineReturnPolicy` method.

### func (*DeleteOnlineReturnPolicyRequest) Descriptor 
    
    
    func (*DeleteOnlineReturnPolicyRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DeleteOnlineReturnPolicyRequest.ProtoReflect.Descriptor instead.

### func (*DeleteOnlineReturnPolicyRequest) GetName 
    
    
    func (x *DeleteOnlineReturnPolicyRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteOnlineReturnPolicyRequest) ProtoMessage 
    
    
    func (*DeleteOnlineReturnPolicyRequest) ProtoMessage()

### func (*DeleteOnlineReturnPolicyRequest) ProtoReflect 
    
    
    func (x *DeleteOnlineReturnPolicyRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DeleteOnlineReturnPolicyRequest) Reset 
    
    
    func (x *DeleteOnlineReturnPolicyRequest) Reset()

### func (*DeleteOnlineReturnPolicyRequest) String 
    
    
    func (x *DeleteOnlineReturnPolicyRequest) String() [string](https://pkg.go.dev/builtin#string)

## DeleteRegionRequest
    
    
    type DeleteRegionRequest struct {
    
    	// Required. The name of the region to delete.
    	// Format: `accounts/{account}/regions/{region}`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the `DeleteRegion` method.

### func (*DeleteRegionRequest) Descriptor 
    
    
    func (*DeleteRegionRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DeleteRegionRequest.ProtoReflect.Descriptor instead.

### func (*DeleteRegionRequest) GetName 
    
    
    func (x *DeleteRegionRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteRegionRequest) ProtoMessage 
    
    
    func (*DeleteRegionRequest) ProtoMessage()

### func (*DeleteRegionRequest) ProtoReflect 
    
    
    func (x *DeleteRegionRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DeleteRegionRequest) Reset 
    
    
    func (x *DeleteRegionRequest) Reset()

### func (*DeleteRegionRequest) String 
    
    
    func (x *DeleteRegionRequest) String() [string](https://pkg.go.dev/builtin#string)

## DeleteUserRequest
    
    
    type DeleteUserRequest struct {
    
    	// Required. The name of the user to delete.
    	// Format: `accounts/{account}/users/{email}`
    	//
    	// It is also possible to delete the user corresponding to the caller by using
    	// `me` rather than an email address as in `accounts/{account}/users/me`.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the `DeleteUser` method.

### func (*DeleteUserRequest) Descriptor 
    
    
    func (*DeleteUserRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DeleteUserRequest.ProtoReflect.Descriptor instead.

### func (*DeleteUserRequest) GetName 
    
    
    func (x *DeleteUserRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteUserRequest) ProtoMessage 
    
    
    func (*DeleteUserRequest) ProtoMessage()

### func (*DeleteUserRequest) ProtoReflect 
    
    
    func (x *DeleteUserRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DeleteUserRequest) Reset 
    
    
    func (x *DeleteUserRequest) Reset()

### func (*DeleteUserRequest) String 
    
    
    func (x *DeleteUserRequest) String() [string](https://pkg.go.dev/builtin#string)

## DeliveryTime
    
    
    type DeliveryTime struct {
    
    	// Minimum number of business days that is spent in transit. 0 means same
    	// day delivery, 1 means next day delivery.
    	// Either `min_transit_days`, `max_transit_days` or
    	// `transit_time_table` must be set, but not both.
    	MinTransitDays *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,1,opt,name=min_transit_days,json=minTransitDays,proto3,oneof" json:"min_transit_days,omitempty"`
    	// Maximum number of business days that is spent in transit. 0 means same
    	// day delivery, 1 means next day delivery. Must be greater than or equal
    	// to `min_transit_days`.
    	MaxTransitDays *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=max_transit_days,json=maxTransitDays,proto3,oneof" json:"max_transit_days,omitempty"`
    	// Business days cutoff time definition.
    	// If not configured the cutoff time will be defaulted to 8AM PST.
    	CutoffTime *CutoffTime `protobuf:"bytes,3,opt,name=cutoff_time,json=cutoffTime,proto3,oneof" json:"cutoff_time,omitempty"`
    	// Minimum number of business days spent before an order is shipped.
    	// 0 means same day shipped, 1 means next day shipped.
    	// 'min_handling_days' and 'max_handling_days' should be either set or not set
    	// at the same time.
    	MinHandlingDays *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,4,opt,name=min_handling_days,json=minHandlingDays,proto3,oneof" json:"min_handling_days,omitempty"`
    	// Maximum number of business days spent before an order is shipped.
    	// 0 means same day shipped, 1 means next day shipped.
    	// Must be greater than or equal to `min_handling_days`.
    	// 'min_handling_days' and 'max_handling_days' should be either set or not set
    	// at the same time.
    	MaxHandlingDays *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,5,opt,name=max_handling_days,json=maxHandlingDays,proto3,oneof" json:"max_handling_days,omitempty"`
    	// Transit time table, number of business days spent in transit based on row
    	// and column dimensions. Either `min_transit_days`, `max_transit_days` or
    	// `transit_time_table` can be set, but not both.
    	TransitTimeTable *TransitTable `protobuf:"bytes,6,opt,name=transit_time_table,json=transitTimeTable,proto3,oneof" json:"transit_time_table,omitempty"`
    	// The business days during which orders can be handled.
    	// If not provided, Monday to Friday business days will be assumed.
    	HandlingBusinessDayConfig *BusinessDayConfig `protobuf:"bytes,7,opt,name=handling_business_day_config,json=handlingBusinessDayConfig,proto3,oneof" json:"handling_business_day_config,omitempty"`
    	// The business days during which orders can be in-transit.
    	// If not provided, Monday to Friday business days will be assumed.
    	TransitBusinessDayConfig *BusinessDayConfig `protobuf:"bytes,8,opt,name=transit_business_day_config,json=transitBusinessDayConfig,proto3,oneof" json:"transit_business_day_config,omitempty"`
    	// Optional. Indicates that the delivery time should be calculated per
    	// warehouse (shipping origin location) based on the settings of the selected
    	// carrier. When set, no other transit time related field in [delivery
    	// time][[google.shopping.content.bundles.ShippingSetting.DeliveryTime] should
    	// be set.
    	WarehouseBasedDeliveryTimes []*WarehouseBasedDeliveryTime `protobuf:"bytes,9,rep,name=warehouse_based_delivery_times,json=warehouseBasedDeliveryTimes,proto3" json:"warehouse_based_delivery_times,omitempty"`
    	// contains filtered or unexported fields
    }

Time spent in various aspects from order to the delivery of the product.

### func (*DeliveryTime) Descriptor 
    
    
    func (*DeliveryTime) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DeliveryTime.ProtoReflect.Descriptor instead.

### func (*DeliveryTime) GetCutoffTime 
    
    
    func (x *DeliveryTime) GetCutoffTime() *CutoffTime

### func (*DeliveryTime) GetHandlingBusinessDayConfig 
    
    
    func (x *DeliveryTime) GetHandlingBusinessDayConfig() *BusinessDayConfig

### func (*DeliveryTime) GetMaxHandlingDays 
    
    
    func (x *DeliveryTime) GetMaxHandlingDays() [int32](https://pkg.go.dev/builtin#int32)

### func (*DeliveryTime) GetMaxTransitDays 
    
    
    func (x *DeliveryTime) GetMaxTransitDays() [int32](https://pkg.go.dev/builtin#int32)

### func (*DeliveryTime) GetMinHandlingDays 
    
    
    func (x *DeliveryTime) GetMinHandlingDays() [int32](https://pkg.go.dev/builtin#int32)

### func (*DeliveryTime) GetMinTransitDays 
    
    
    func (x *DeliveryTime) GetMinTransitDays() [int32](https://pkg.go.dev/builtin#int32)

### func (*DeliveryTime) GetTransitBusinessDayConfig 
    
    
    func (x *DeliveryTime) GetTransitBusinessDayConfig() *BusinessDayConfig

### func (*DeliveryTime) GetTransitTimeTable 
    
    
    func (x *DeliveryTime) GetTransitTimeTable() *TransitTable

### func (*DeliveryTime) GetWarehouseBasedDeliveryTimes 
    
    
    func (x *DeliveryTime) GetWarehouseBasedDeliveryTimes() []*WarehouseBasedDeliveryTime

### func (*DeliveryTime) ProtoMessage 
    
    
    func (*DeliveryTime) ProtoMessage()

### func (*DeliveryTime) ProtoReflect 
    
    
    func (x *DeliveryTime) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DeliveryTime) Reset 
    
    
    func (x *DeliveryTime) Reset()

### func (*DeliveryTime) String 
    
    
    func (x *DeliveryTime) String() [string](https://pkg.go.dev/builtin#string)

## DisableProgramRequest
    
    
    type DisableProgramRequest struct {
    
    	// Required. The name of the program for which to disable participation for
    	// the given account. Format: `accounts/{account}/programs/{program}`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the DisableProgram method.

### func (*DisableProgramRequest) Descriptor 
    
    
    func (*DisableProgramRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DisableProgramRequest.ProtoReflect.Descriptor instead.

### func (*DisableProgramRequest) GetName 
    
    
    func (x *DisableProgramRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*DisableProgramRequest) ProtoMessage 
    
    
    func (*DisableProgramRequest) ProtoMessage()

### func (*DisableProgramRequest) ProtoReflect 
    
    
    func (x *DisableProgramRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DisableProgramRequest) Reset 
    
    
    func (x *DisableProgramRequest) Reset()

### func (*DisableProgramRequest) String 
    
    
    func (x *DisableProgramRequest) String() [string](https://pkg.go.dev/builtin#string)

## Distance
    
    
    type Distance struct {
    
    	// Integer value of distance.
    	Value *[int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,1,opt,name=value,proto3,oneof" json:"value,omitempty"`
    	// Unit can differ based on country, it is parameterized to include miles
    	// and kilometers.
    	Unit *Distance_Unit `protobuf:"varint,2,opt,name=unit,proto3,enum=google.shopping.merchant.accounts.v1beta.Distance_Unit,oneof" json:"unit,omitempty"`
    	// contains filtered or unexported fields
    }

Maximum delivery radius. This is only required for the local delivery shipment type.

### func (*Distance) Descriptor 
    
    
    func (*Distance) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Distance.ProtoReflect.Descriptor instead.

### func (*Distance) GetUnit 
    
    
    func (x *Distance) GetUnit() Distance_Unit

### func (*Distance) GetValue 
    
    
    func (x *Distance) GetValue() [int64](https://pkg.go.dev/builtin#int64)

### func (*Distance) ProtoMessage 
    
    
    func (*Distance) ProtoMessage()

### func (*Distance) ProtoReflect 
    
    
    func (x *Distance) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Distance) Reset 
    
    
    func (x *Distance) Reset()

### func (*Distance) String 
    
    
    func (x *Distance) String() [string](https://pkg.go.dev/builtin#string)

## Distance_Unit
    
    
    type Distance_Unit [int32](https://pkg.go.dev/builtin#int32)

Unit can differ based on country, it is parameterized to include miles and kilometers.

### Distance_UNIT_UNSPECIFIED, Distance_MILES, Distance_KILOMETERS
    
    
    const (
    	// Unit unspecified
    	Distance_UNIT_UNSPECIFIED Distance_Unit = 0
    	// Unit in miles
    	Distance_MILES Distance_Unit = 1
    	// Unit in kilometers
    	Distance_KILOMETERS Distance_Unit = 2
    )

### func (Distance_Unit) Descriptor 
    
    
    func (Distance_Unit) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Distance_Unit) Enum 
    
    
    func (x Distance_Unit) Enum() *Distance_Unit

### func (Distance_Unit) EnumDescriptor 
    
    
    func (Distance_Unit) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Distance_Unit.Descriptor instead.

### func (Distance_Unit) Number 
    
    
    func (x Distance_Unit) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Distance_Unit) String 
    
    
    func (x Distance_Unit) String() [string](https://pkg.go.dev/builtin#string)

### func (Distance_Unit) Type 
    
    
    func (Distance_Unit) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## EmailPreferences
    
    
    type EmailPreferences struct {
    
    	// Identifier. The name of the EmailPreferences. The endpoint is only
    	// supported for the authenticated user.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. Updates on new features, tips and best practices.
    	NewsAndTips EmailPreferences_OptInState `protobuf:"varint,2,opt,name=news_and_tips,json=newsAndTips,proto3,enum=google.shopping.merchant.accounts.v1beta.EmailPreferences_OptInState" json:"news_and_tips,omitempty"`
    	// contains filtered or unexported fields
    }

The categories of notifications the user opted into / opted out of. The email preferences do not include mandatory announcements as users can't opt out of them.

### func (*EmailPreferences) Descriptor 
    
    
    func (*EmailPreferences) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use EmailPreferences.ProtoReflect.Descriptor instead.

### func (*EmailPreferences) GetName 
    
    
    func (x *EmailPreferences) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*EmailPreferences) GetNewsAndTips 
    
    
    func (x *EmailPreferences) GetNewsAndTips() EmailPreferences_OptInState

### func (*EmailPreferences) ProtoMessage 
    
    
    func (*EmailPreferences) ProtoMessage()

### func (*EmailPreferences) ProtoReflect 
    
    
    func (x *EmailPreferences) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*EmailPreferences) Reset 
    
    
    func (x *EmailPreferences) Reset()

### func (*EmailPreferences) String 
    
    
    func (x *EmailPreferences) String() [string](https://pkg.go.dev/builtin#string)

## EmailPreferencesServiceClient
    
    
    type EmailPreferencesServiceClient interface {
    	// Returns the email preferences for a Merchant Center account user.
    	//
    	// Use the name=accounts/*/users/me/emailPreferences alias to get preferences
    	// for the authenticated user.
    	GetEmailPreferences(ctx context.Context, in *GetEmailPreferencesRequest, opts ...grpc.CallOption) (*EmailPreferences, [error](https://pkg.go.dev/builtin#error))
    	// Updates the email preferences for a Merchant Center account user. MCA users
    	// should specify the MCA account rather than a sub-account of the MCA.
    	//
    	// Preferences which are not explicitly selected in the update mask will not
    	// be updated.
    	//
    	// It is invalid for updates to specify an UNCONFIRMED opt-in status value.
    	//
    	// Use the name=accounts/*/users/me/emailPreferences alias to update
    	// preferences
    	// for the authenticated user.
    	UpdateEmailPreferences(ctx context.Context, in *UpdateEmailPreferencesRequest, opts ...grpc.CallOption) (*EmailPreferences, [error](https://pkg.go.dev/builtin#error))
    }

EmailPreferencesServiceClient is the client API for EmailPreferencesService service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

### func NewEmailPreferencesServiceClient 
    
    
    func NewEmailPreferencesServiceClient(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) EmailPreferencesServiceClient

## EmailPreferencesServiceServer
    
    
    type EmailPreferencesServiceServer interface {
    	// Returns the email preferences for a Merchant Center account user.
    	//
    	// Use the name=accounts/*/users/me/emailPreferences alias to get preferences
    	// for the authenticated user.
    	GetEmailPreferences(context.Context, *GetEmailPreferencesRequest) (*EmailPreferences, [error](https://pkg.go.dev/builtin#error))
    	// Updates the email preferences for a Merchant Center account user. MCA users
    	// should specify the MCA account rather than a sub-account of the MCA.
    	//
    	// Preferences which are not explicitly selected in the update mask will not
    	// be updated.
    	//
    	// It is invalid for updates to specify an UNCONFIRMED opt-in status value.
    	//
    	// Use the name=accounts/*/users/me/emailPreferences alias to update
    	// preferences
    	// for the authenticated user.
    	UpdateEmailPreferences(context.Context, *UpdateEmailPreferencesRequest) (*EmailPreferences, [error](https://pkg.go.dev/builtin#error))
    }

EmailPreferencesServiceServer is the server API for EmailPreferencesService service. All implementations should embed UnimplementedEmailPreferencesServiceServer for forward compatibility

## EmailPreferences_OptInState
    
    
    type EmailPreferences_OptInState [int32](https://pkg.go.dev/builtin#int32)

Opt in state of the email preference.

### EmailPreferences_OPT_IN_STATE_UNSPECIFIED, EmailPreferences_OPTED_OUT, EmailPreferences_OPTED_IN, EmailPreferences_UNCONFIRMED
    
    
    const (
    	// Opt-in status is not specified.
    	EmailPreferences_OPT_IN_STATE_UNSPECIFIED EmailPreferences_OptInState = 0
    	// User has opted out of receiving this type of email.
    	EmailPreferences_OPTED_OUT EmailPreferences_OptInState = 1
    	// User has opted in to receiving this type of email.
    	EmailPreferences_OPTED_IN EmailPreferences_OptInState = 2
    	// User has opted in to receiving this type of email and the confirmation
    	// email has been sent, but user has not yet confirmed the opt in (applies
    	// only to certain countries).
    	EmailPreferences_UNCONFIRMED EmailPreferences_OptInState = 3
    )

### func (EmailPreferences_OptInState) Descriptor 
    
    
    func (EmailPreferences_OptInState) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (EmailPreferences_OptInState) Enum 
    
    
    func (x EmailPreferences_OptInState) Enum() *EmailPreferences_OptInState

### func (EmailPreferences_OptInState) EnumDescriptor 
    
    
    func (EmailPreferences_OptInState) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use EmailPreferences_OptInState.Descriptor instead.

### func (EmailPreferences_OptInState) Number 
    
    
    func (x EmailPreferences_OptInState) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (EmailPreferences_OptInState) String 
    
    
    func (x EmailPreferences_OptInState) String() [string](https://pkg.go.dev/builtin#string)

### func (EmailPreferences_OptInState) Type 
    
    
    func (EmailPreferences_OptInState) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## EnableProgramRequest
    
    
    type EnableProgramRequest struct {
    
    	// Required. The name of the program for which to enable participation for the
    	// given account. Format: `accounts/{account}/programs/{program}`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the EnableProgram method.

### func (*EnableProgramRequest) Descriptor 
    
    
    func (*EnableProgramRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use EnableProgramRequest.ProtoReflect.Descriptor instead.

### func (*EnableProgramRequest) GetName 
    
    
    func (x *EnableProgramRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*EnableProgramRequest) ProtoMessage 
    
    
    func (*EnableProgramRequest) ProtoMessage()

### func (*EnableProgramRequest) ProtoReflect 
    
    
    func (x *EnableProgramRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*EnableProgramRequest) Reset 
    
    
    func (x *EnableProgramRequest) Reset()

### func (*EnableProgramRequest) String 
    
    
    func (x *EnableProgramRequest) String() [string](https://pkg.go.dev/builtin#string)

## FindLfpProvidersRequest
    
    
    type FindLfpProvidersRequest struct {
    
    	// Required. The name of the parent resource under which the LFP providers are
    	// found. Format:
    	// `accounts/{account}/omnichannelSettings/{omnichannel_setting}`.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Optional. The maximum number of `LfpProvider` resources to return. The
    	// service returns fewer than this value if the number of lfp providers is
    	// less that than the `pageSize`. The default value is 50. The maximum value
    	// is 1000; If a value higher than the maximum is specified, then the
    	// `pageSize` will default to the maximum.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// Optional. A page token, received from a previous `FindLfpProviders` call.
    	// Provide the page token to retrieve the subsequent page.
    	//
    	// When paginating, all other parameters provided to `FindLfpProviders` must
    	// match the call that provided the page token.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the FindLfpProviders method.

### func (*FindLfpProvidersRequest) Descriptor 
    
    
    func (*FindLfpProvidersRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use FindLfpProvidersRequest.ProtoReflect.Descriptor instead.

### func (*FindLfpProvidersRequest) GetPageSize 
    
    
    func (x *FindLfpProvidersRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*FindLfpProvidersRequest) GetPageToken 
    
    
    func (x *FindLfpProvidersRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*FindLfpProvidersRequest) GetParent 
    
    
    func (x *FindLfpProvidersRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*FindLfpProvidersRequest) ProtoMessage 
    
    
    func (*FindLfpProvidersRequest) ProtoMessage()

### func (*FindLfpProvidersRequest) ProtoReflect 
    
    
    func (x *FindLfpProvidersRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*FindLfpProvidersRequest) Reset 
    
    
    func (x *FindLfpProvidersRequest) Reset()

### func (*FindLfpProvidersRequest) String 
    
    
    func (x *FindLfpProvidersRequest) String() [string](https://pkg.go.dev/builtin#string)

## FindLfpProvidersResponse
    
    
    type FindLfpProvidersResponse struct {
    
    	// The LFP providers from the specified merchant in the specified country.
    	LfpProviders []*LfpProvider `protobuf:"bytes,1,rep,name=lfp_providers,json=lfpProviders,proto3" json:"lfp_providers,omitempty"`
    	// A token, which can be sent as `page_token` to retrieve the next page.
    	// If this field is omitted, there are no subsequent pages.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Response message for the FindLfpProviders method.

### func (*FindLfpProvidersResponse) Descriptor 
    
    
    func (*FindLfpProvidersResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use FindLfpProvidersResponse.ProtoReflect.Descriptor instead.

### func (*FindLfpProvidersResponse) GetLfpProviders 
    
    
    func (x *FindLfpProvidersResponse) GetLfpProviders() []*LfpProvider

### func (*FindLfpProvidersResponse) GetNextPageToken 
    
    
    func (x *FindLfpProvidersResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*FindLfpProvidersResponse) ProtoMessage 
    
    
    func (*FindLfpProvidersResponse) ProtoMessage()

### func (*FindLfpProvidersResponse) ProtoReflect 
    
    
    func (x *FindLfpProvidersResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*FindLfpProvidersResponse) Reset 
    
    
    func (x *FindLfpProvidersResponse) Reset()

### func (*FindLfpProvidersResponse) String 
    
    
    func (x *FindLfpProvidersResponse) String() [string](https://pkg.go.dev/builtin#string)

## GbpAccount
    
    
    type GbpAccount struct {
    
    	// Identifier. The resource name of the GBP account. Format:
    	// `accounts/{account}/gbpAccount/{gbp_account}`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// The id of the GBP account.
    	GbpAccountId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=gbp_account_id,json=gbpAccountId,proto3" json:"gbp_account_id,omitempty"`
    	// The type of the Business Profile.
    	Type GbpAccount_Type `protobuf:"varint,3,opt,name=type,proto3,enum=google.shopping.merchant.accounts.v1beta.GbpAccount_Type" json:"type,omitempty"`
    	// The name of the Business Profile.
    	// For personal accounts: Email id of the owner.
    	// For Business accounts: Name of the Business Account.
    	GbpAccountName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=gbp_account_name,json=gbpAccountName,proto3" json:"gbp_account_name,omitempty"`
    	// Number of listings under this account.
    	ListingCount [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,6,opt,name=listing_count,json=listingCount,proto3" json:"listing_count,omitempty"`
    	// contains filtered or unexported fields
    }

Collection of information related to a Google Business Profile (GBP) account.

### func (*GbpAccount) Descriptor 
    
    
    func (*GbpAccount) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GbpAccount.ProtoReflect.Descriptor instead.

### func (*GbpAccount) GetGbpAccountId 
    
    
    func (x *GbpAccount) GetGbpAccountId() [string](https://pkg.go.dev/builtin#string)

### func (*GbpAccount) GetGbpAccountName 
    
    
    func (x *GbpAccount) GetGbpAccountName() [string](https://pkg.go.dev/builtin#string)

### func (*GbpAccount) GetListingCount 
    
    
    func (x *GbpAccount) GetListingCount() [int64](https://pkg.go.dev/builtin#int64)

### func (*GbpAccount) GetName 
    
    
    func (x *GbpAccount) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GbpAccount) GetType 
    
    
    func (x *GbpAccount) GetType() GbpAccount_Type

### func (*GbpAccount) ProtoMessage 
    
    
    func (*GbpAccount) ProtoMessage()

### func (*GbpAccount) ProtoReflect 
    
    
    func (x *GbpAccount) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GbpAccount) Reset 
    
    
    func (x *GbpAccount) Reset()

### func (*GbpAccount) String 
    
    
    func (x *GbpAccount) String() [string](https://pkg.go.dev/builtin#string)

## GbpAccount_Type
    
    
    type GbpAccount_Type [int32](https://pkg.go.dev/builtin#int32)

The type of the GBP account.

### GbpAccount_TYPE_UNSPECIFIED, GbpAccount_USER, GbpAccount_BUSINESS_ACCOUNT
    
    
    const (
    	// Default value. This value is unused.
    	GbpAccount_TYPE_UNSPECIFIED GbpAccount_Type = 0
    	// The GBP account is a user account.
    	GbpAccount_USER GbpAccount_Type = 1
    	// The GBP account is a business account.
    	GbpAccount_BUSINESS_ACCOUNT GbpAccount_Type = 2
    )

### func (GbpAccount_Type) Descriptor 
    
    
    func (GbpAccount_Type) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (GbpAccount_Type) Enum 
    
    
    func (x GbpAccount_Type) Enum() *GbpAccount_Type

### func (GbpAccount_Type) EnumDescriptor 
    
    
    func (GbpAccount_Type) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GbpAccount_Type.Descriptor instead.

### func (GbpAccount_Type) Number 
    
    
    func (x GbpAccount_Type) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (GbpAccount_Type) String 
    
    
    func (x GbpAccount_Type) String() [string](https://pkg.go.dev/builtin#string)

### func (GbpAccount_Type) Type 
    
    
    func (GbpAccount_Type) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## GbpAccountsServiceClient
    
    
    type GbpAccountsServiceClient interface {
    	// List the GBP accounts for a given merchant.
    	ListGbpAccounts(ctx context.Context, in *ListGbpAccountsRequest, opts ...grpc.CallOption) (*ListGbpAccountsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Link the specified merchant to a GBP account for all countries.
    	LinkGbpAccount(ctx context.Context, in *LinkGbpAccountRequest, opts ...grpc.CallOption) (*LinkGbpAccountResponse, [error](https://pkg.go.dev/builtin#error))
    }

GbpAccountsServiceClient is the client API for GbpAccountsService service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

### func NewGbpAccountsServiceClient 
    
    
    func NewGbpAccountsServiceClient(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) GbpAccountsServiceClient

## GbpAccountsServiceServer
    
    
    type GbpAccountsServiceServer interface {
    	// List the GBP accounts for a given merchant.
    	ListGbpAccounts(context.Context, *ListGbpAccountsRequest) (*ListGbpAccountsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Link the specified merchant to a GBP account for all countries.
    	LinkGbpAccount(context.Context, *LinkGbpAccountRequest) (*LinkGbpAccountResponse, [error](https://pkg.go.dev/builtin#error))
    }

GbpAccountsServiceServer is the server API for GbpAccountsService service. All implementations should embed UnimplementedGbpAccountsServiceServer for forward compatibility

## GetAccountRequest
    
    
    type GetAccountRequest struct {
    
    	// Required. The name of the account to retrieve.
    	// Format: `accounts/{account}`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the `GetAccount` method.

### func (*GetAccountRequest) Descriptor 
    
    
    func (*GetAccountRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetAccountRequest.ProtoReflect.Descriptor instead.

### func (*GetAccountRequest) GetName 
    
    
    func (x *GetAccountRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetAccountRequest) ProtoMessage 
    
    
    func (*GetAccountRequest) ProtoMessage()

### func (*GetAccountRequest) ProtoReflect 
    
    
    func (x *GetAccountRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetAccountRequest) Reset 
    
    
    func (x *GetAccountRequest) Reset()

### func (*GetAccountRequest) String 
    
    
    func (x *GetAccountRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetAccountTaxRequest
    
    
    type GetAccountTaxRequest struct {
    
    	// Required. The name from which tax settings will be retrieved
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request to get tax settings

### func (*GetAccountTaxRequest) Descriptor 
    
    
    func (*GetAccountTaxRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetAccountTaxRequest.ProtoReflect.Descriptor instead.

### func (*GetAccountTaxRequest) GetName 
    
    
    func (x *GetAccountTaxRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetAccountTaxRequest) ProtoMessage 
    
    
    func (*GetAccountTaxRequest) ProtoMessage()

### func (*GetAccountTaxRequest) ProtoReflect 
    
    
    func (x *GetAccountTaxRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetAccountTaxRequest) Reset 
    
    
    func (x *GetAccountTaxRequest) Reset()

### func (*GetAccountTaxRequest) String 
    
    
    func (x *GetAccountTaxRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetAutofeedSettingsRequest
    
    
    type GetAutofeedSettingsRequest struct {
    
    	// Required. The resource name of the autofeed settings.
    	// Format: `accounts/{account}/autofeedSettings`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the `GetAutofeedSettings` method.

### func (*GetAutofeedSettingsRequest) Descriptor 
    
    
    func (*GetAutofeedSettingsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetAutofeedSettingsRequest.ProtoReflect.Descriptor instead.

### func (*GetAutofeedSettingsRequest) GetName 
    
    
    func (x *GetAutofeedSettingsRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetAutofeedSettingsRequest) ProtoMessage 
    
    
    func (*GetAutofeedSettingsRequest) ProtoMessage()

### func (*GetAutofeedSettingsRequest) ProtoReflect 
    
    
    func (x *GetAutofeedSettingsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetAutofeedSettingsRequest) Reset 
    
    
    func (x *GetAutofeedSettingsRequest) Reset()

### func (*GetAutofeedSettingsRequest) String 
    
    
    func (x *GetAutofeedSettingsRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetAutomaticImprovementsRequest
    
    
    type GetAutomaticImprovementsRequest struct {
    
    	// Required. The resource name of the automatic improvements.
    	// Format: `accounts/{account}/automaticImprovements`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the `GetAutomaticImprovements` method.

### func (*GetAutomaticImprovementsRequest) Descriptor 
    
    
    func (*GetAutomaticImprovementsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetAutomaticImprovementsRequest.ProtoReflect.Descriptor instead.

### func (*GetAutomaticImprovementsRequest) GetName 
    
    
    func (x *GetAutomaticImprovementsRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetAutomaticImprovementsRequest) ProtoMessage 
    
    
    func (*GetAutomaticImprovementsRequest) ProtoMessage()

### func (*GetAutomaticImprovementsRequest) ProtoReflect 
    
    
    func (x *GetAutomaticImprovementsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetAutomaticImprovementsRequest) Reset 
    
    
    func (x *GetAutomaticImprovementsRequest) Reset()

### func (*GetAutomaticImprovementsRequest) String 
    
    
    func (x *GetAutomaticImprovementsRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetBusinessIdentityRequest
    
    
    type GetBusinessIdentityRequest struct {
    
    	// Required. The resource name of the business identity.
    	// Format: `accounts/{account}/businessIdentity`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the `GetBusinessIdentity` method.

### func (*GetBusinessIdentityRequest) Descriptor 
    
    
    func (*GetBusinessIdentityRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetBusinessIdentityRequest.ProtoReflect.Descriptor instead.

### func (*GetBusinessIdentityRequest) GetName 
    
    
    func (x *GetBusinessIdentityRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetBusinessIdentityRequest) ProtoMessage 
    
    
    func (*GetBusinessIdentityRequest) ProtoMessage()

### func (*GetBusinessIdentityRequest) ProtoReflect 
    
    
    func (x *GetBusinessIdentityRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetBusinessIdentityRequest) Reset 
    
    
    func (x *GetBusinessIdentityRequest) Reset()

### func (*GetBusinessIdentityRequest) String 
    
    
    func (x *GetBusinessIdentityRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetBusinessInfoRequest
    
    
    type GetBusinessInfoRequest struct {
    
    	// Required. The resource name of the business info.
    	// Format: `accounts/{account}/businessInfo`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the `GetBusinessInfo` method.

### func (*GetBusinessInfoRequest) Descriptor 
    
    
    func (*GetBusinessInfoRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetBusinessInfoRequest.ProtoReflect.Descriptor instead.

### func (*GetBusinessInfoRequest) GetName 
    
    
    func (x *GetBusinessInfoRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetBusinessInfoRequest) ProtoMessage 
    
    
    func (*GetBusinessInfoRequest) ProtoMessage()

### func (*GetBusinessInfoRequest) ProtoReflect 
    
    
    func (x *GetBusinessInfoRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetBusinessInfoRequest) Reset 
    
    
    func (x *GetBusinessInfoRequest) Reset()

### func (*GetBusinessInfoRequest) String 
    
    
    func (x *GetBusinessInfoRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetCheckoutSettingsRequest
    
    
    type GetCheckoutSettingsRequest struct {
    
    	// Required. The name/identifier of the merchant account.
    	// Format: `accounts/{account}/programs/{program}/checkoutSettings`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for `GetCheckoutSettings` method.

### func (*GetCheckoutSettingsRequest) Descriptor 
    
    
    func (*GetCheckoutSettingsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetCheckoutSettingsRequest.ProtoReflect.Descriptor instead.

### func (*GetCheckoutSettingsRequest) GetName 
    
    
    func (x *GetCheckoutSettingsRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetCheckoutSettingsRequest) ProtoMessage 
    
    
    func (*GetCheckoutSettingsRequest) ProtoMessage()

### func (*GetCheckoutSettingsRequest) ProtoReflect 
    
    
    func (x *GetCheckoutSettingsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetCheckoutSettingsRequest) Reset 
    
    
    func (x *GetCheckoutSettingsRequest) Reset()

### func (*GetCheckoutSettingsRequest) String 
    
    
    func (x *GetCheckoutSettingsRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetEmailPreferencesRequest
    
    
    type GetEmailPreferencesRequest struct {
    
    	// Required. The name of the `EmailPreferences` resource.
    	// Format: `accounts/{account}/users/{email}/emailPreferences`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for GetEmailPreferences method.

### func (*GetEmailPreferencesRequest) Descriptor 
    
    
    func (*GetEmailPreferencesRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetEmailPreferencesRequest.ProtoReflect.Descriptor instead.

### func (*GetEmailPreferencesRequest) GetName 
    
    
    func (x *GetEmailPreferencesRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetEmailPreferencesRequest) ProtoMessage 
    
    
    func (*GetEmailPreferencesRequest) ProtoMessage()

### func (*GetEmailPreferencesRequest) ProtoReflect 
    
    
    func (x *GetEmailPreferencesRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetEmailPreferencesRequest) Reset 
    
    
    func (x *GetEmailPreferencesRequest) Reset()

### func (*GetEmailPreferencesRequest) String 
    
    
    func (x *GetEmailPreferencesRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetHomepageRequest
    
    
    type GetHomepageRequest struct {
    
    	// Required. The name of the homepage to retrieve.
    	// Format: `accounts/{account}/homepage`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the `GetHomepage` method.

### func (*GetHomepageRequest) Descriptor 
    
    
    func (*GetHomepageRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetHomepageRequest.ProtoReflect.Descriptor instead.

### func (*GetHomepageRequest) GetName 
    
    
    func (x *GetHomepageRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetHomepageRequest) ProtoMessage 
    
    
    func (*GetHomepageRequest) ProtoMessage()

### func (*GetHomepageRequest) ProtoReflect 
    
    
    func (x *GetHomepageRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetHomepageRequest) Reset 
    
    
    func (x *GetHomepageRequest) Reset()

### func (*GetHomepageRequest) String 
    
    
    func (x *GetHomepageRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetOmnichannelSettingRequest
    
    
    type GetOmnichannelSettingRequest struct {
    
    	// Required. The name of the omnichannel setting to retrieve.
    	// Format: `accounts/{account}/omnichannelSettings/{omnichannel_setting}`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the GetOmnichannelSettings method.

### func (*GetOmnichannelSettingRequest) Descriptor 
    
    
    func (*GetOmnichannelSettingRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetOmnichannelSettingRequest.ProtoReflect.Descriptor instead.

### func (*GetOmnichannelSettingRequest) GetName 
    
    
    func (x *GetOmnichannelSettingRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetOmnichannelSettingRequest) ProtoMessage 
    
    
    func (*GetOmnichannelSettingRequest) ProtoMessage()

### func (*GetOmnichannelSettingRequest) ProtoReflect 
    
    
    func (x *GetOmnichannelSettingRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetOmnichannelSettingRequest) Reset 
    
    
    func (x *GetOmnichannelSettingRequest) Reset()

### func (*GetOmnichannelSettingRequest) String 
    
    
    func (x *GetOmnichannelSettingRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetOnlineReturnPolicyRequest
    
    
    type GetOnlineReturnPolicyRequest struct {
    
    	// Required. The name of the return policy to retrieve.
    	// Format: `accounts/{account}/onlineReturnPolicies/{return_policy}`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the `GetOnlineReturnPolicy` method.

### func (*GetOnlineReturnPolicyRequest) Descriptor 
    
    
    func (*GetOnlineReturnPolicyRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetOnlineReturnPolicyRequest.ProtoReflect.Descriptor instead.

### func (*GetOnlineReturnPolicyRequest) GetName 
    
    
    func (x *GetOnlineReturnPolicyRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetOnlineReturnPolicyRequest) ProtoMessage 
    
    
    func (*GetOnlineReturnPolicyRequest) ProtoMessage()

### func (*GetOnlineReturnPolicyRequest) ProtoReflect 
    
    
    func (x *GetOnlineReturnPolicyRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetOnlineReturnPolicyRequest) Reset 
    
    
    func (x *GetOnlineReturnPolicyRequest) Reset()

### func (*GetOnlineReturnPolicyRequest) String 
    
    
    func (x *GetOnlineReturnPolicyRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetProgramRequest
    
    
    type GetProgramRequest struct {
    
    	// Required. The name of the program to retrieve.
    	// Format: `accounts/{account}/programs/{program}`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the GetProgram method.

### func (*GetProgramRequest) Descriptor 
    
    
    func (*GetProgramRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetProgramRequest.ProtoReflect.Descriptor instead.

### func (*GetProgramRequest) GetName 
    
    
    func (x *GetProgramRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetProgramRequest) ProtoMessage 
    
    
    func (*GetProgramRequest) ProtoMessage()

### func (*GetProgramRequest) ProtoReflect 
    
    
    func (x *GetProgramRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetProgramRequest) Reset 
    
    
    func (x *GetProgramRequest) Reset()

### func (*GetProgramRequest) String 
    
    
    func (x *GetProgramRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetRegionRequest
    
    
    type GetRegionRequest struct {
    
    	// Required. The name of the region to retrieve.
    	// Format: `accounts/{account}/regions/{region}`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the `GetRegion` method.

### func (*GetRegionRequest) Descriptor 
    
    
    func (*GetRegionRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetRegionRequest.ProtoReflect.Descriptor instead.

### func (*GetRegionRequest) GetName 
    
    
    func (x *GetRegionRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetRegionRequest) ProtoMessage 
    
    
    func (*GetRegionRequest) ProtoMessage()

### func (*GetRegionRequest) ProtoReflect 
    
    
    func (x *GetRegionRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetRegionRequest) Reset 
    
    
    func (x *GetRegionRequest) Reset()

### func (*GetRegionRequest) String 
    
    
    func (x *GetRegionRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetShippingSettingsRequest
    
    
    type GetShippingSettingsRequest struct {
    
    	// Required. The name of the shipping setting to retrieve.
    	// Format: `accounts/{account}/shippingsetting`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the `GetShippingSetting` method.

### func (*GetShippingSettingsRequest) Descriptor 
    
    
    func (*GetShippingSettingsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetShippingSettingsRequest.ProtoReflect.Descriptor instead.

### func (*GetShippingSettingsRequest) GetName 
    
    
    func (x *GetShippingSettingsRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetShippingSettingsRequest) ProtoMessage 
    
    
    func (*GetShippingSettingsRequest) ProtoMessage()

### func (*GetShippingSettingsRequest) ProtoReflect 
    
    
    func (x *GetShippingSettingsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetShippingSettingsRequest) Reset 
    
    
    func (x *GetShippingSettingsRequest) Reset()

### func (*GetShippingSettingsRequest) String 
    
    
    func (x *GetShippingSettingsRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetTermsOfServiceAgreementStateRequest
    
    
    type GetTermsOfServiceAgreementStateRequest struct {
    
    	// Required. The resource name of the terms of service version.
    	// Format: `accounts/{account}/termsOfServiceAgreementState/{identifier}`
    	// The identifier format is: `{TermsOfServiceKind}-{country}`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the `GetTermsOfServiceAgreementState` method.

### func (*GetTermsOfServiceAgreementStateRequest) Descriptor 
    
    
    func (*GetTermsOfServiceAgreementStateRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetTermsOfServiceAgreementStateRequest.ProtoReflect.Descriptor instead.

### func (*GetTermsOfServiceAgreementStateRequest) GetName 
    
    
    func (x *GetTermsOfServiceAgreementStateRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetTermsOfServiceAgreementStateRequest) ProtoMessage 
    
    
    func (*GetTermsOfServiceAgreementStateRequest) ProtoMessage()

### func (*GetTermsOfServiceAgreementStateRequest) ProtoReflect 
    
    
    func (x *GetTermsOfServiceAgreementStateRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetTermsOfServiceAgreementStateRequest) Reset 
    
    
    func (x *GetTermsOfServiceAgreementStateRequest) Reset()

### func (*GetTermsOfServiceAgreementStateRequest) String 
    
    
    func (x *GetTermsOfServiceAgreementStateRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetTermsOfServiceRequest
    
    
    type GetTermsOfServiceRequest struct {
    
    	// Required. The resource name of the terms of service version.
    	// Format: `termsOfService/{version}`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the `GetTermsOfService` method.

### func (*GetTermsOfServiceRequest) Descriptor 
    
    
    func (*GetTermsOfServiceRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetTermsOfServiceRequest.ProtoReflect.Descriptor instead.

### func (*GetTermsOfServiceRequest) GetName 
    
    
    func (x *GetTermsOfServiceRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetTermsOfServiceRequest) ProtoMessage 
    
    
    func (*GetTermsOfServiceRequest) ProtoMessage()

### func (*GetTermsOfServiceRequest) ProtoReflect 
    
    
    func (x *GetTermsOfServiceRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetTermsOfServiceRequest) Reset 
    
    
    func (x *GetTermsOfServiceRequest) Reset()

### func (*GetTermsOfServiceRequest) String 
    
    
    func (x *GetTermsOfServiceRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetUserRequest
    
    
    type GetUserRequest struct {
    
    	// Required. The name of the user to retrieve.
    	// Format: `accounts/{account}/users/{email}`
    	//
    	// It is also possible to retrieve the user corresponding to the caller by
    	// using `me` rather than an email address as in
    	// `accounts/{account}/users/me`.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the `GetUser` method.

### func (*GetUserRequest) Descriptor 
    
    
    func (*GetUserRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetUserRequest.ProtoReflect.Descriptor instead.

### func (*GetUserRequest) GetName 
    
    
    func (x *GetUserRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetUserRequest) ProtoMessage 
    
    
    func (*GetUserRequest) ProtoMessage()

### func (*GetUserRequest) ProtoReflect 
    
    
    func (x *GetUserRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetUserRequest) Reset 
    
    
    func (x *GetUserRequest) Reset()

### func (*GetUserRequest) String 
    
    
    func (x *GetUserRequest) String() [string](https://pkg.go.dev/builtin#string)

## Headers
    
    
    type Headers struct {
    
    	// Required. A list of inclusive order price upper bounds. The last price's
    	// value can be infinity by setting price amount_micros = -1. For example
    	// `[{"amount_micros": 10000000, "currency_code": "USD"},
    	// {"amount_micros": 500000000, "currency_code": "USD"},
    	// {"amount_micros": -1, "currency_code": "USD"}]` represents the headers
    	// "<= $10",=""><= $500",="" and="" "=""> $500". All prices within a service must have
    	// the same currency. Must be non-empty. Must be positive except -1. Can only
    	// be set if all other fields are not set.
    	Prices []*typepb.Price `protobuf:"bytes,1,rep,name=prices,proto3" json:"prices,omitempty"`
    	// Required. A list of inclusive order weight upper bounds. The last weight's
    	// value can be infinity by setting price amount_micros = -1. For example
    	// `[{"amount_micros": 10000000, "unit": "kg"}, {"amount_micros": 50000000,
    	// "unit": "kg"},
    	// {"amount_micros": -1, "unit": "kg"}]` represents the headers
    	// "<= 10kg",=""><= 50kg",="" and="" "=""> 50kg". All weights within a service must have
    	// the same unit. Must be non-empty. Must be positive except -1. Can only be
    	// set if all other fields are not set.
    	Weights []*typepb.Weight `protobuf:"bytes,2,rep,name=weights,proto3" json:"weights,omitempty"`
    	// Required. A list of inclusive number of items upper bounds. The last value
    	// can be
    	// `"infinity"`. For example
    	// `["10", "50", "infinity"]` represents the headers
    	// "<= 10="" items",=""><= 50="" items",="" and="" "=""> 50 items". Must be non-empty. Can
    	// only be set if all other fields are not set.
    	NumberOfItems [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,rep,name=number_of_items,json=numberOfItems,proto3" json:"number_of_items,omitempty"`
    	// Required. A list of postal group names. The last value can be
    	// `"all other locations"`. Example:
    	// `["zone 1", "zone 2", "all other locations"]`. The referred
    	// postal code groups must match the delivery country of the service. Must
    	// be non-empty. Can only be set if all other fields are not set.
    	PostalCodeGroupNames [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,rep,name=postal_code_group_names,json=postalCodeGroupNames,proto3" json:"postal_code_group_names,omitempty"`
    	// Required. A list of location ID sets. Must be non-empty. Can only be set if
    	// all other fields are not set.
    	Locations []*LocationIdSet `protobuf:"bytes,5,rep,name=locations,proto3" json:"locations,omitempty"`
    	// contains filtered or unexported fields
    }

A non-empty list of row or column headers for a table. Exactly one of `prices`, `weights`, `num_items`, `postal_code_group_names`, or `location` must be set.

### func (*Headers) Descriptor 
    
    
    func (*Headers) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Headers.ProtoReflect.Descriptor instead.

### func (*Headers) GetLocations 
    
    
    func (x *Headers) GetLocations() []*LocationIdSet

### func (*Headers) GetNumberOfItems 
    
    
    func (x *Headers) GetNumberOfItems() [][string](https://pkg.go.dev/builtin#string)

### func (*Headers) GetPostalCodeGroupNames 
    
    
    func (x *Headers) GetPostalCodeGroupNames() [][string](https://pkg.go.dev/builtin#string)

### func (*Headers) GetPrices 
    
    
    func (x *Headers) GetPrices() []*[typepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/type/typepb).[Price](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/type/typepb#cloud_google_com_go_shopping_type_typepb_Price)

### func (*Headers) GetWeights 
    
    
    func (x *Headers) GetWeights() []*[typepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/type/typepb).[Weight](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/type/typepb#cloud_google_com_go_shopping_type_typepb_Weight)

### func (*Headers) ProtoMessage 
    
    
    func (*Headers) ProtoMessage()

### func (*Headers) ProtoReflect 
    
    
    func (x *Headers) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Headers) Reset 
    
    
    func (x *Headers) Reset()

### func (*Headers) String 
    
    
    func (x *Headers) String() [string](https://pkg.go.dev/builtin#string)

## Homepage
    
    
    type Homepage struct {
    
    	// Identifier. The resource name of the store's homepage.
    	// Format: `accounts/{account}/homepage`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Required. The URI (typically a URL) of the store's homepage.
    	Uri *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=uri,proto3,oneof" json:"uri,omitempty"`
    	// Output only. Whether the homepage is claimed. See
    	// https://support.google.com/merchants/answer/176793.
    	Claimed [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,3,opt,name=claimed,proto3" json:"claimed,omitempty"`
    	// contains filtered or unexported fields
    }

A store's homepage.

### func (*Homepage) Descriptor 
    
    
    func (*Homepage) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Homepage.ProtoReflect.Descriptor instead.

### func (*Homepage) GetClaimed 
    
    
    func (x *Homepage) GetClaimed() [bool](https://pkg.go.dev/builtin#bool)

### func (*Homepage) GetName 
    
    
    func (x *Homepage) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Homepage) GetUri 
    
    
    func (x *Homepage) GetUri() [string](https://pkg.go.dev/builtin#string)

### func (*Homepage) ProtoMessage 
    
    
    func (*Homepage) ProtoMessage()

### func (*Homepage) ProtoReflect 
    
    
    func (x *Homepage) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Homepage) Reset 
    
    
    func (x *Homepage) Reset()

### func (*Homepage) String 
    
    
    func (x *Homepage) String() [string](https://pkg.go.dev/builtin#string)

## HomepageServiceClient
    
    
    type HomepageServiceClient interface {
    	// Retrieves a store's homepage.
    	GetHomepage(ctx context.Context, in *GetHomepageRequest, opts ...grpc.CallOption) (*Homepage, [error](https://pkg.go.dev/builtin#error))
    	// Updates a store's homepage. Executing this method requires admin access.
    	UpdateHomepage(ctx context.Context, in *UpdateHomepageRequest, opts ...grpc.CallOption) (*Homepage, [error](https://pkg.go.dev/builtin#error))
    	// Claims a store's homepage. Executing this method requires admin access.
    	//
    	// If the homepage is already claimed, this will recheck the
    	// verification (unless the merchant is exempted from claiming, which also
    	// exempts from verification) and return a successful response. If ownership
    	// can no longer be verified, it will return an error, but it won't clear the
    	// claim. In case of failure, a canonical error message will be returned:
    	//   - PERMISSION_DENIED: user doesn't have the necessary permissions on this
    	//     MC account;
    	//   - FAILED_PRECONDITION:
    	//   - The account is not a Merchant Center account;
    	//   - MC account doesn't have a homepage;
    	//   - claiming failed (in this case the error message will contain more
    	//     details).
    	ClaimHomepage(ctx context.Context, in *ClaimHomepageRequest, opts ...grpc.CallOption) (*Homepage, [error](https://pkg.go.dev/builtin#error))
    	// Unclaims a store's homepage. Executing this method requires admin access.
    	UnclaimHomepage(ctx context.Context, in *UnclaimHomepageRequest, opts ...grpc.CallOption) (*Homepage, [error](https://pkg.go.dev/builtin#error))
    }

HomepageServiceClient is the client API for HomepageService service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

### func NewHomepageServiceClient 
    
    
    func NewHomepageServiceClient(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) HomepageServiceClient

## HomepageServiceServer
    
    
    type HomepageServiceServer interface {
    	// Retrieves a store's homepage.
    	GetHomepage(context.Context, *GetHomepageRequest) (*Homepage, [error](https://pkg.go.dev/builtin#error))
    	// Updates a store's homepage. Executing this method requires admin access.
    	UpdateHomepage(context.Context, *UpdateHomepageRequest) (*Homepage, [error](https://pkg.go.dev/builtin#error))
    	// Claims a store's homepage. Executing this method requires admin access.
    	//
    	// If the homepage is already claimed, this will recheck the
    	// verification (unless the merchant is exempted from claiming, which also
    	// exempts from verification) and return a successful response. If ownership
    	// can no longer be verified, it will return an error, but it won't clear the
    	// claim. In case of failure, a canonical error message will be returned:
    	//   - PERMISSION_DENIED: user doesn't have the necessary permissions on this
    	//     MC account;
    	//   - FAILED_PRECONDITION:
    	//   - The account is not a Merchant Center account;
    	//   - MC account doesn't have a homepage;
    	//   - claiming failed (in this case the error message will contain more
    	//     details).
    	ClaimHomepage(context.Context, *ClaimHomepageRequest) (*Homepage, [error](https://pkg.go.dev/builtin#error))
    	// Unclaims a store's homepage. Executing this method requires admin access.
    	UnclaimHomepage(context.Context, *UnclaimHomepageRequest) (*Homepage, [error](https://pkg.go.dev/builtin#error))
    }

HomepageServiceServer is the server API for HomepageService service. All implementations should embed UnimplementedHomepageServiceServer for forward compatibility

## InStock
    
    
    type InStock struct {
    
    	// Optional. Product landing page URI. It is only used for the review of MHLSF
    	// in-stock serving. This URI domain should match with the business's
    	// homepage. Required to be empty if the lsf_type is GHLSF, and required when
    	// the lsf_type is MHLSF_FULL or MHLSF_BASIC.
    	Uri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=uri,proto3" json:"uri,omitempty"`
    	// Output only. The state of the in-stock serving.
    	State ReviewState_State `protobuf:"varint,2,opt,name=state,proto3,enum=google.shopping.merchant.accounts.v1beta.ReviewState_State" json:"state,omitempty"`
    	// contains filtered or unexported fields
    }

Collection of information related to InStock.

### func (*InStock) Descriptor 
    
    
    func (*InStock) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use InStock.ProtoReflect.Descriptor instead.

### func (*InStock) GetState 
    
    
    func (x *InStock) GetState() ReviewState_State

### func (*InStock) GetUri 
    
    
    func (x *InStock) GetUri() [string](https://pkg.go.dev/builtin#string)

### func (*InStock) ProtoMessage 
    
    
    func (*InStock) ProtoMessage()

### func (*InStock) ProtoReflect 
    
    
    func (x *InStock) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*InStock) Reset 
    
    
    func (x *InStock) Reset()

### func (*InStock) String 
    
    
    func (x *InStock) String() [string](https://pkg.go.dev/builtin#string)

## InsertShippingSettingsRequest
    
    
    type InsertShippingSettingsRequest struct {
    
    	// Required. The account where this product will be inserted.
    	// Format: accounts/{account}
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Required. The new version of the account.
    	ShippingSetting *ShippingSettings `protobuf:"bytes,2,opt,name=shipping_setting,json=shippingSetting,proto3" json:"shipping_setting,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the `InsertShippingSetting` method.

### func (*InsertShippingSettingsRequest) Descriptor 
    
    
    func (*InsertShippingSettingsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use InsertShippingSettingsRequest.ProtoReflect.Descriptor instead.

### func (*InsertShippingSettingsRequest) GetParent 
    
    
    func (x *InsertShippingSettingsRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*InsertShippingSettingsRequest) GetShippingSetting 
    
    
    func (x *InsertShippingSettingsRequest) GetShippingSetting() *ShippingSettings

### func (*InsertShippingSettingsRequest) ProtoMessage 
    
    
    func (*InsertShippingSettingsRequest) ProtoMessage()

### func (*InsertShippingSettingsRequest) ProtoReflect 
    
    
    func (x *InsertShippingSettingsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*InsertShippingSettingsRequest) Reset 
    
    
    func (x *InsertShippingSettingsRequest) Reset()

### func (*InsertShippingSettingsRequest) String 
    
    
    func (x *InsertShippingSettingsRequest) String() [string](https://pkg.go.dev/builtin#string)

## InventoryVerification
    
    
    type InventoryVerification struct {
    
    	// Output only. The state of the inventory verification process.
    	State InventoryVerification_State `protobuf:"varint,1,opt,name=state,proto3,enum=google.shopping.merchant.accounts.v1beta.InventoryVerification_State" json:"state,omitempty"`
    	// Required. The name of the contact for the inventory verification process.
    	Contact [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=contact,proto3" json:"contact,omitempty"`
    	// Required. The email address of the contact for the inventory verification
    	// process.
    	ContactEmail [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=contact_email,json=contactEmail,proto3" json:"contact_email,omitempty"`
    	// Output only. The state of the contact verification.
    	ContactState ReviewState_State `protobuf:"varint,4,opt,name=contact_state,json=contactState,proto3,enum=google.shopping.merchant.accounts.v1beta.ReviewState_State" json:"contact_state,omitempty"`
    	// contains filtered or unexported fields
    }

Collection of information related to [inventory verification](https://support.google.com/merchants/answer/14684499?hl=en&ref_topic=15145634&sjid=6892280366904591178-NC).

### func (*InventoryVerification) Descriptor 
    
    
    func (*InventoryVerification) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use InventoryVerification.ProtoReflect.Descriptor instead.

### func (*InventoryVerification) GetContact 
    
    
    func (x *InventoryVerification) GetContact() [string](https://pkg.go.dev/builtin#string)

### func (*InventoryVerification) GetContactEmail 
    
    
    func (x *InventoryVerification) GetContactEmail() [string](https://pkg.go.dev/builtin#string)

### func (*InventoryVerification) GetContactState 
    
    
    func (x *InventoryVerification) GetContactState() ReviewState_State

### func (*InventoryVerification) GetState 
    
    
    func (x *InventoryVerification) GetState() InventoryVerification_State

### func (*InventoryVerification) ProtoMessage 
    
    
    func (*InventoryVerification) ProtoMessage()

### func (*InventoryVerification) ProtoReflect 
    
    
    func (x *InventoryVerification) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*InventoryVerification) Reset 
    
    
    func (x *InventoryVerification) Reset()

### func (*InventoryVerification) String 
    
    
    func (x *InventoryVerification) String() [string](https://pkg.go.dev/builtin#string)

## InventoryVerification_State
    
    
    type InventoryVerification_State [int32](https://pkg.go.dev/builtin#int32)

The state of the [inventory verification](https://support.google.com/merchants/answer/14684499?hl=en&ref_topic=15145634&sjid=6892280366904591178-NC) process.

### InventoryVerification_STATE_UNSPECIFIED, InventoryVerification_ACTION_REQUIRED, InventoryVerification_INACTIVE, InventoryVerification_RUNNING, InventoryVerification_SUCCEEDED, InventoryVerification_SUSPENDED
    
    
    const (
    	// Default value. This value is unused.
    	InventoryVerification_STATE_UNSPECIFIED InventoryVerification_State = 0
    	// When the merchant needs to initiate the inventory
    	// verification process. The next state is INACTIVE.
    	InventoryVerification_ACTION_REQUIRED InventoryVerification_State = 1
    	// When the merchant is ready to request inventory verification.
    	InventoryVerification_INACTIVE InventoryVerification_State = 5
    	// The inventory verification process is running. If the merchant is
    	// rejected, the next state is INACTIVE.
    	InventoryVerification_RUNNING InventoryVerification_State = 2
    	// The inventory verification process succeeded.
    	InventoryVerification_SUCCEEDED InventoryVerification_State = 3
    	// When merchant fails the inventory verification process and all attempts
    	// are exhausted.
    	InventoryVerification_SUSPENDED InventoryVerification_State = 4
    )

### func (InventoryVerification_State) Descriptor 
    
    
    func (InventoryVerification_State) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (InventoryVerification_State) Enum 
    
    
    func (x InventoryVerification_State) Enum() *InventoryVerification_State

### func (InventoryVerification_State) EnumDescriptor 
    
    
    func (InventoryVerification_State) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use InventoryVerification_State.Descriptor instead.

### func (InventoryVerification_State) Number 
    
    
    func (x InventoryVerification_State) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (InventoryVerification_State) String 
    
    
    func (x InventoryVerification_State) String() [string](https://pkg.go.dev/builtin#string)

### func (InventoryVerification_State) Type 
    
    
    func (InventoryVerification_State) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## LfpLink
    
    
    type LfpLink struct {
    
    	// Required. The resource name of the LFP provider.
    	// Format: `lfpProviders/{lfp_provider}`
    	LfpProvider [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=lfp_provider,json=lfpProvider,proto3" json:"lfp_provider,omitempty"`
    	// Required. The account ID by which this merchant is known to the LFP
    	// provider.
    	ExternalAccountId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=external_account_id,json=externalAccountId,proto3" json:"external_account_id,omitempty"`
    	// Output only. The state of the LFP link.
    	State ReviewState_State `protobuf:"varint,3,opt,name=state,proto3,enum=google.shopping.merchant.accounts.v1beta.ReviewState_State" json:"state,omitempty"`
    	// contains filtered or unexported fields
    }

Collection of information related to the LFP link.

### func (*LfpLink) Descriptor 
    
    
    func (*LfpLink) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use LfpLink.ProtoReflect.Descriptor instead.

### func (*LfpLink) GetExternalAccountId 
    
    
    func (x *LfpLink) GetExternalAccountId() [string](https://pkg.go.dev/builtin#string)

### func (*LfpLink) GetLfpProvider 
    
    
    func (x *LfpLink) GetLfpProvider() [string](https://pkg.go.dev/builtin#string)

### func (*LfpLink) GetState 
    
    
    func (x *LfpLink) GetState() ReviewState_State

### func (*LfpLink) ProtoMessage 
    
    
    func (*LfpLink) ProtoMessage()

### func (*LfpLink) ProtoReflect 
    
    
    func (x *LfpLink) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*LfpLink) Reset 
    
    
    func (x *LfpLink) Reset()

### func (*LfpLink) String 
    
    
    func (x *LfpLink) String() [string](https://pkg.go.dev/builtin#string)

## LfpProvider
    
    
    type LfpProvider struct {
    
    	// Identifier. The resource name of the LFP provider.
    	// Format:
    	// `accounts/{account}/omnichannelSettings/{omnichannel_setting}/lfpProviders/{lfp_provider}`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Output only. Region code defined by [CLDR](https://cldr.unicode.org/).
    	RegionCode [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=region_code,json=regionCode,proto3" json:"region_code,omitempty"`
    	// The display name of the LFP provider.
    	DisplayName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=display_name,json=displayName,proto3" json:"display_name,omitempty"`
    	// contains filtered or unexported fields
    }

Collection of information related to a Local Feed Partnership (LFP) provider.

### func (*LfpProvider) Descriptor 
    
    
    func (*LfpProvider) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use LfpProvider.ProtoReflect.Descriptor instead.

### func (*LfpProvider) GetDisplayName 
    
    
    func (x *LfpProvider) GetDisplayName() [string](https://pkg.go.dev/builtin#string)

### func (*LfpProvider) GetName 
    
    
    func (x *LfpProvider) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*LfpProvider) GetRegionCode 
    
    
    func (x *LfpProvider) GetRegionCode() [string](https://pkg.go.dev/builtin#string)

### func (*LfpProvider) ProtoMessage 
    
    
    func (*LfpProvider) ProtoMessage()

### func (*LfpProvider) ProtoReflect 
    
    
    func (x *LfpProvider) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*LfpProvider) Reset 
    
    
    func (x *LfpProvider) Reset()

### func (*LfpProvider) String 
    
    
    func (x *LfpProvider) String() [string](https://pkg.go.dev/builtin#string)

## LfpProvidersServiceClient
    
    
    type LfpProvidersServiceClient interface {
    	// Find the LFP provider candidates in a given country.
    	FindLfpProviders(ctx context.Context, in *FindLfpProvidersRequest, opts ...grpc.CallOption) (*FindLfpProvidersResponse, [error](https://pkg.go.dev/builtin#error))
    	// Link the specified merchant to a LFP provider for the specified country.
    	LinkLfpProvider(ctx context.Context, in *LinkLfpProviderRequest, opts ...grpc.CallOption) (*LinkLfpProviderResponse, [error](https://pkg.go.dev/builtin#error))
    }

LfpProvidersServiceClient is the client API for LfpProvidersService service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

### func NewLfpProvidersServiceClient 
    
    
    func NewLfpProvidersServiceClient(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) LfpProvidersServiceClient

## LfpProvidersServiceServer
    
    
    type LfpProvidersServiceServer interface {
    	// Find the LFP provider candidates in a given country.
    	FindLfpProviders(context.Context, *FindLfpProvidersRequest) (*FindLfpProvidersResponse, [error](https://pkg.go.dev/builtin#error))
    	// Link the specified merchant to a LFP provider for the specified country.
    	LinkLfpProvider(context.Context, *LinkLfpProviderRequest) (*LinkLfpProviderResponse, [error](https://pkg.go.dev/builtin#error))
    }

LfpProvidersServiceServer is the server API for LfpProvidersService service. All implementations should embed UnimplementedLfpProvidersServiceServer for forward compatibility

## LinkGbpAccountRequest
    
    
    type LinkGbpAccountRequest struct {
    
    	// Required. The name of the parent resource to which the GBP account is
    	// linked. Format: `accounts/{account}`.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Required. The email address of the Business Profile account.
    	GbpEmail [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=gbp_email,json=gbpEmail,proto3" json:"gbp_email,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the LinkGbpAccount method.

### func (*LinkGbpAccountRequest) Descriptor 
    
    
    func (*LinkGbpAccountRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use LinkGbpAccountRequest.ProtoReflect.Descriptor instead.

### func (*LinkGbpAccountRequest) GetGbpEmail 
    
    
    func (x *LinkGbpAccountRequest) GetGbpEmail() [string](https://pkg.go.dev/builtin#string)

### func (*LinkGbpAccountRequest) GetParent 
    
    
    func (x *LinkGbpAccountRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*LinkGbpAccountRequest) ProtoMessage 
    
    
    func (*LinkGbpAccountRequest) ProtoMessage()

### func (*LinkGbpAccountRequest) ProtoReflect 
    
    
    func (x *LinkGbpAccountRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*LinkGbpAccountRequest) Reset 
    
    
    func (x *LinkGbpAccountRequest) Reset()

### func (*LinkGbpAccountRequest) String 
    
    
    func (x *LinkGbpAccountRequest) String() [string](https://pkg.go.dev/builtin#string)

## LinkGbpAccountResponse
    
    
    type LinkGbpAccountResponse struct {
    
    	// Empty response.
    	Response *emptypb.Empty `protobuf:"bytes,1,opt,name=response,proto3" json:"response,omitempty"`
    	// contains filtered or unexported fields
    }

Response message for the LinkGbpAccount method.

### func (*LinkGbpAccountResponse) Descriptor 
    
    
    func (*LinkGbpAccountResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use LinkGbpAccountResponse.ProtoReflect.Descriptor instead.

### func (*LinkGbpAccountResponse) GetResponse 
    
    
    func (x *LinkGbpAccountResponse) GetResponse() *[emptypb](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb).[Empty](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb#Empty)

### func (*LinkGbpAccountResponse) ProtoMessage 
    
    
    func (*LinkGbpAccountResponse) ProtoMessage()

### func (*LinkGbpAccountResponse) ProtoReflect 
    
    
    func (x *LinkGbpAccountResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*LinkGbpAccountResponse) Reset 
    
    
    func (x *LinkGbpAccountResponse) Reset()

### func (*LinkGbpAccountResponse) String 
    
    
    func (x *LinkGbpAccountResponse) String() [string](https://pkg.go.dev/builtin#string)

## LinkLfpProviderRequest
    
    
    type LinkLfpProviderRequest struct {
    
    	// Required. The name of the LFP provider resource to link.
    	// Format:
    	// `accounts/{account}/omnichannelSettings/{omnichannel_setting}/lfpProviders/{lfp_provider}`.
    	// The `lfp_provider` is the LFP provider ID.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Required. The external account ID by which this merchant is known to the
    	// LFP provider.
    	ExternalAccountId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=external_account_id,json=externalAccountId,proto3" json:"external_account_id,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the LinkLfpProvider method.

### func (*LinkLfpProviderRequest) Descriptor 
    
    
    func (*LinkLfpProviderRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use LinkLfpProviderRequest.ProtoReflect.Descriptor instead.

### func (*LinkLfpProviderRequest) GetExternalAccountId 
    
    
    func (x *LinkLfpProviderRequest) GetExternalAccountId() [string](https://pkg.go.dev/builtin#string)

### func (*LinkLfpProviderRequest) GetName 
    
    
    func (x *LinkLfpProviderRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*LinkLfpProviderRequest) ProtoMessage 
    
    
    func (*LinkLfpProviderRequest) ProtoMessage()

### func (*LinkLfpProviderRequest) ProtoReflect 
    
    
    func (x *LinkLfpProviderRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*LinkLfpProviderRequest) Reset 
    
    
    func (x *LinkLfpProviderRequest) Reset()

### func (*LinkLfpProviderRequest) String 
    
    
    func (x *LinkLfpProviderRequest) String() [string](https://pkg.go.dev/builtin#string)

## LinkLfpProviderResponse
    
    
    type LinkLfpProviderResponse struct {
    
    	// Empty response.
    	Response *emptypb.Empty `protobuf:"bytes,1,opt,name=response,proto3" json:"response,omitempty"`
    	// contains filtered or unexported fields
    }

Response message for the LinkLfpProvider method.

### func (*LinkLfpProviderResponse) Descriptor 
    
    
    func (*LinkLfpProviderResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use LinkLfpProviderResponse.ProtoReflect.Descriptor instead.

### func (*LinkLfpProviderResponse) GetResponse 
    
    
    func (x *LinkLfpProviderResponse) GetResponse() *[emptypb](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb).[Empty](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb#Empty)

### func (*LinkLfpProviderResponse) ProtoMessage 
    
    
    func (*LinkLfpProviderResponse) ProtoMessage()

### func (*LinkLfpProviderResponse) ProtoReflect 
    
    
    func (x *LinkLfpProviderResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*LinkLfpProviderResponse) Reset 
    
    
    func (x *LinkLfpProviderResponse) Reset()

### func (*LinkLfpProviderResponse) String 
    
    
    func (x *LinkLfpProviderResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListAccountIssuesRequest
    
    
    type ListAccountIssuesRequest struct {
    
    	// Required. The parent, which owns this collection of issues.
    	// Format: `accounts/{account}`
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Optional. The maximum number of issues to return. The service may return
    	// fewer than this value. If unspecified, at most 50 users will be returned.
    	// The maximum value is 100; values above 100 will be coerced to 100
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// Optional. A page token, received from a previous `ListAccountIssues` call.
    	// Provide this to retrieve the subsequent page.
    	//
    	// When paginating, all other parameters provided to `ListAccountIssues` must
    	// match the call that provided the page token.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// Optional. The issues in the response will have human-readable fields in the
    	// given language. The format is [BCP-47](https://tools.ietf.org/html/bcp47),
    	// such as `en-US` or `sr-Latn`. If not value is provided, `en-US` will be
    	// used.
    	LanguageCode [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=language_code,json=languageCode,proto3" json:"language_code,omitempty"`
    	// Optional. The [IANA](https://www.iana.org/time-zones) timezone used to
    	// localize times in human-readable fields. For example 'America/Los_Angeles'.
    	// If not set, 'America/Los_Angeles' will be used.
    	TimeZone [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=time_zone,json=timeZone,proto3" json:"time_zone,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the `ListAccountIssues` method.

### func (*ListAccountIssuesRequest) Descriptor 
    
    
    func (*ListAccountIssuesRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListAccountIssuesRequest.ProtoReflect.Descriptor instead.

### func (*ListAccountIssuesRequest) GetLanguageCode 
    
    
    func (x *ListAccountIssuesRequest) GetLanguageCode() [string](https://pkg.go.dev/builtin#string)

### func (*ListAccountIssuesRequest) GetPageSize 
    
    
    func (x *ListAccountIssuesRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListAccountIssuesRequest) GetPageToken 
    
    
    func (x *ListAccountIssuesRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListAccountIssuesRequest) GetParent 
    
    
    func (x *ListAccountIssuesRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListAccountIssuesRequest) GetTimeZone 
    
    
    func (x *ListAccountIssuesRequest) GetTimeZone() [string](https://pkg.go.dev/builtin#string)

### func (*ListAccountIssuesRequest) ProtoMessage 
    
    
    func (*ListAccountIssuesRequest) ProtoMessage()

### func (*ListAccountIssuesRequest) ProtoReflect 
    
    
    func (x *ListAccountIssuesRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListAccountIssuesRequest) Reset 
    
    
    func (x *ListAccountIssuesRequest) Reset()

### func (*ListAccountIssuesRequest) String 
    
    
    func (x *ListAccountIssuesRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListAccountIssuesResponse
    
    
    type ListAccountIssuesResponse struct {
    
    	// The issues from the specified account.
    	AccountIssues []*AccountIssue `protobuf:"bytes,1,rep,name=account_issues,json=accountIssues,proto3" json:"account_issues,omitempty"`
    	// A token, which can be sent as `page_token` to retrieve the next page.
    	// If this field is omitted, there are no subsequent pages.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Response message for the `ListAccountIssues` method.

### func (*ListAccountIssuesResponse) Descriptor 
    
    
    func (*ListAccountIssuesResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListAccountIssuesResponse.ProtoReflect.Descriptor instead.

### func (*ListAccountIssuesResponse) GetAccountIssues 
    
    
    func (x *ListAccountIssuesResponse) GetAccountIssues() []*AccountIssue

### func (*ListAccountIssuesResponse) GetNextPageToken 
    
    
    func (x *ListAccountIssuesResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListAccountIssuesResponse) ProtoMessage 
    
    
    func (*ListAccountIssuesResponse) ProtoMessage()

### func (*ListAccountIssuesResponse) ProtoReflect 
    
    
    func (x *ListAccountIssuesResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListAccountIssuesResponse) Reset 
    
    
    func (x *ListAccountIssuesResponse) Reset()

### func (*ListAccountIssuesResponse) String 
    
    
    func (x *ListAccountIssuesResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListAccountTaxRequest
    
    
    type ListAccountTaxRequest struct {
    
    	// Required. The parent, which owns this collection of account tax.
    	// Format: accounts/{account}
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// The maximum number of tax settings to return in the response, used for
    	// paging.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// The token returned by the previous request.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Request to list all sub-account tax settings only for the requesting merchant This method can only be called on a multi-client account, otherwise it'll return an error.

### func (*ListAccountTaxRequest) Descriptor 
    
    
    func (*ListAccountTaxRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListAccountTaxRequest.ProtoReflect.Descriptor instead.

### func (*ListAccountTaxRequest) GetPageSize 
    
    
    func (x *ListAccountTaxRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListAccountTaxRequest) GetPageToken 
    
    
    func (x *ListAccountTaxRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListAccountTaxRequest) GetParent 
    
    
    func (x *ListAccountTaxRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListAccountTaxRequest) ProtoMessage 
    
    
    func (*ListAccountTaxRequest) ProtoMessage()

### func (*ListAccountTaxRequest) ProtoReflect 
    
    
    func (x *ListAccountTaxRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListAccountTaxRequest) Reset 
    
    
    func (x *ListAccountTaxRequest) Reset()

### func (*ListAccountTaxRequest) String 
    
    
    func (x *ListAccountTaxRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListAccountTaxResponse
    
    
    type ListAccountTaxResponse struct {
    
    	// Page of accounttax settings
    	AccountTaxes []*AccountTax `protobuf:"bytes,1,rep,name=account_taxes,json=accountTaxes,proto3" json:"account_taxes,omitempty"`
    	// The token for the retrieval of the next page of account tax settings.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Response to account tax list request This method can only be called on a multi-client account, otherwise it'll return an error.

### func (*ListAccountTaxResponse) Descriptor 
    
    
    func (*ListAccountTaxResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListAccountTaxResponse.ProtoReflect.Descriptor instead.

### func (*ListAccountTaxResponse) GetAccountTaxes 
    
    
    func (x *ListAccountTaxResponse) GetAccountTaxes() []*AccountTax

### func (*ListAccountTaxResponse) GetNextPageToken 
    
    
    func (x *ListAccountTaxResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListAccountTaxResponse) ProtoMessage 
    
    
    func (*ListAccountTaxResponse) ProtoMessage()

### func (*ListAccountTaxResponse) ProtoReflect 
    
    
    func (x *ListAccountTaxResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListAccountTaxResponse) Reset 
    
    
    func (x *ListAccountTaxResponse) Reset()

### func (*ListAccountTaxResponse) String 
    
    
    func (x *ListAccountTaxResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListAccountsRequest
    
    
    type ListAccountsRequest struct {
    
    	// Optional. The maximum number of accounts to return. The service may return
    	// fewer than this value.  If unspecified, at most 250 accounts are returned.
    	// The maximum value is 500; values above 500 are coerced to 500.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,1,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// Optional. A page token, received from a previous `ListAccounts` call.
    	// Provide this to retrieve the subsequent page.
    	//
    	// When paginating, all other parameters provided to `ListAccounts` must match
    	// the call that provided the page token.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// Optional. Returns only accounts that match the
    	// [filter](/merchant/api/guides/accounts/filter).
    	// For more details, see the
    	// [filter syntax reference](/merchant/api/guides/accounts/filter-syntax).
    	Filter [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=filter,proto3" json:"filter,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the `ListAccounts` method.

### func (*ListAccountsRequest) Descriptor 
    
    
    func (*ListAccountsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListAccountsRequest.ProtoReflect.Descriptor instead.

### func (*ListAccountsRequest) GetFilter 
    
    
    func (x *ListAccountsRequest) GetFilter() [string](https://pkg.go.dev/builtin#string)

### func (*ListAccountsRequest) GetPageSize 
    
    
    func (x *ListAccountsRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListAccountsRequest) GetPageToken 
    
    
    func (x *ListAccountsRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListAccountsRequest) ProtoMessage 
    
    
    func (*ListAccountsRequest) ProtoMessage()

### func (*ListAccountsRequest) ProtoReflect 
    
    
    func (x *ListAccountsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListAccountsRequest) Reset 
    
    
    func (x *ListAccountsRequest) Reset()

### func (*ListAccountsRequest) String 
    
    
    func (x *ListAccountsRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListAccountsResponse
    
    
    type ListAccountsResponse struct {
    
    	// The accounts matching the `ListAccountsRequest`.
    	Accounts []*Account `protobuf:"bytes,1,rep,name=accounts,proto3" json:"accounts,omitempty"`
    	// A token, which can be sent as `page_token` to retrieve the next page.
    	// If this field is omitted, there are no subsequent pages.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Response message for the `ListAccounts` method.

### func (*ListAccountsResponse) Descriptor 
    
    
    func (*ListAccountsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListAccountsResponse.ProtoReflect.Descriptor instead.

### func (*ListAccountsResponse) GetAccounts 
    
    
    func (x *ListAccountsResponse) GetAccounts() []*Account

### func (*ListAccountsResponse) GetNextPageToken 
    
    
    func (x *ListAccountsResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListAccountsResponse) ProtoMessage 
    
    
    func (*ListAccountsResponse) ProtoMessage()

### func (*ListAccountsResponse) ProtoReflect 
    
    
    func (x *ListAccountsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListAccountsResponse) Reset 
    
    
    func (x *ListAccountsResponse) Reset()

### func (*ListAccountsResponse) String 
    
    
    func (x *ListAccountsResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListGbpAccountsRequest
    
    
    type ListGbpAccountsRequest struct {
    
    	// Required. The name of the parent resource under which the GBP accounts are
    	// listed. Format: `accounts/{account}`.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Optional. The maximum number of `GbpAccount` resources to return. The
    	// service returns fewer than this value if the number of gbp accounts is less
    	// that than the `pageSize`. The default value is 50. The maximum value is
    	// 1000; If a value higher than the maximum is specified, then the `pageSize`
    	// will default to the maximum.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// Optional. A page token, received from a previous `ListGbpAccounts` call.
    	// Provide the page token to retrieve the subsequent page.
    	//
    	// When paginating, all other parameters provided to `ListGbpAccounts` must
    	// match the call that provided the page token.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the ListGbpAccounts method.

### func (*ListGbpAccountsRequest) Descriptor 
    
    
    func (*ListGbpAccountsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListGbpAccountsRequest.ProtoReflect.Descriptor instead.

### func (*ListGbpAccountsRequest) GetPageSize 
    
    
    func (x *ListGbpAccountsRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListGbpAccountsRequest) GetPageToken 
    
    
    func (x *ListGbpAccountsRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListGbpAccountsRequest) GetParent 
    
    
    func (x *ListGbpAccountsRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListGbpAccountsRequest) ProtoMessage 
    
    
    func (*ListGbpAccountsRequest) ProtoMessage()

### func (*ListGbpAccountsRequest) ProtoReflect 
    
    
    func (x *ListGbpAccountsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListGbpAccountsRequest) Reset 
    
    
    func (x *ListGbpAccountsRequest) Reset()

### func (*ListGbpAccountsRequest) String 
    
    
    func (x *ListGbpAccountsRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListGbpAccountsResponse
    
    
    type ListGbpAccountsResponse struct {
    
    	// The GBP accounts from the specified merchant in the specified country.
    	GbpAccounts []*GbpAccount `protobuf:"bytes,1,rep,name=gbp_accounts,json=gbpAccounts,proto3" json:"gbp_accounts,omitempty"`
    	// A token, which can be sent as `page_token` to retrieve the next page.
    	// If this field is omitted, there are no subsequent pages.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Response message for the ListGbpAccounts method.

### func (*ListGbpAccountsResponse) Descriptor 
    
    
    func (*ListGbpAccountsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListGbpAccountsResponse.ProtoReflect.Descriptor instead.

### func (*ListGbpAccountsResponse) GetGbpAccounts 
    
    
    func (x *ListGbpAccountsResponse) GetGbpAccounts() []*GbpAccount

### func (*ListGbpAccountsResponse) GetNextPageToken 
    
    
    func (x *ListGbpAccountsResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListGbpAccountsResponse) ProtoMessage 
    
    
    func (*ListGbpAccountsResponse) ProtoMessage()

### func (*ListGbpAccountsResponse) ProtoReflect 
    
    
    func (x *ListGbpAccountsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListGbpAccountsResponse) Reset 
    
    
    func (x *ListGbpAccountsResponse) Reset()

### func (*ListGbpAccountsResponse) String 
    
    
    func (x *ListGbpAccountsResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListOmnichannelSettingsRequest
    
    
    type ListOmnichannelSettingsRequest struct {
    
    	// Required. The parent, which owns this collection of omnichannel settings.
    	// Format: `accounts/{account}`
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Optional. The maximum number of omnichannel settings to return. The service
    	// may return fewer than this value. If unspecified, at most 50 omnichannel
    	// settings will be returned. The maximum value is 1000; values above 1000
    	// will be coerced to 1000.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// Optional. A page token, received from a previous `ListOmnichannelSettings`
    	// call. Provide this to retrieve the subsequent page.
    	//
    	// When paginating, all other parameters provided to `ListOmnichannelSettings`
    	// must match the call that provided the page token.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the ListOmnichannelSettings method.

### func (*ListOmnichannelSettingsRequest) Descriptor 
    
    
    func (*ListOmnichannelSettingsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListOmnichannelSettingsRequest.ProtoReflect.Descriptor instead.

### func (*ListOmnichannelSettingsRequest) GetPageSize 
    
    
    func (x *ListOmnichannelSettingsRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListOmnichannelSettingsRequest) GetPageToken 
    
    
    func (x *ListOmnichannelSettingsRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListOmnichannelSettingsRequest) GetParent 
    
    
    func (x *ListOmnichannelSettingsRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListOmnichannelSettingsRequest) ProtoMessage 
    
    
    func (*ListOmnichannelSettingsRequest) ProtoMessage()

### func (*ListOmnichannelSettingsRequest) ProtoReflect 
    
    
    func (x *ListOmnichannelSettingsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListOmnichannelSettingsRequest) Reset 
    
    
    func (x *ListOmnichannelSettingsRequest) Reset()

### func (*ListOmnichannelSettingsRequest) String 
    
    
    func (x *ListOmnichannelSettingsRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListOmnichannelSettingsResponse
    
    
    type ListOmnichannelSettingsResponse struct {
    
    	// The omnichannel settings from the specified merchant.
    	OmnichannelSettings []*OmnichannelSetting `protobuf:"bytes,1,rep,name=omnichannel_settings,json=omnichannelSettings,proto3" json:"omnichannel_settings,omitempty"`
    	// A token, which can be sent as `page_token` to retrieve the next page.
    	// If this field is omitted, there are no subsequent pages.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Response message for the ListOmnichannelSettings method.

### func (*ListOmnichannelSettingsResponse) Descriptor 
    
    
    func (*ListOmnichannelSettingsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListOmnichannelSettingsResponse.ProtoReflect.Descriptor instead.

### func (*ListOmnichannelSettingsResponse) GetNextPageToken 
    
    
    func (x *ListOmnichannelSettingsResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListOmnichannelSettingsResponse) GetOmnichannelSettings 
    
    
    func (x *ListOmnichannelSettingsResponse) GetOmnichannelSettings() []*OmnichannelSetting

### func (*ListOmnichannelSettingsResponse) ProtoMessage 
    
    
    func (*ListOmnichannelSettingsResponse) ProtoMessage()

### func (*ListOmnichannelSettingsResponse) ProtoReflect 
    
    
    func (x *ListOmnichannelSettingsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListOmnichannelSettingsResponse) Reset 
    
    
    func (x *ListOmnichannelSettingsResponse) Reset()

### func (*ListOmnichannelSettingsResponse) String 
    
    
    func (x *ListOmnichannelSettingsResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListOnlineReturnPoliciesRequest
    
    
    type ListOnlineReturnPoliciesRequest struct {
    
    	// Required. The merchant account for which to list return policies.
    	// Format: `accounts/{account}`
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Optional. The maximum number of `OnlineReturnPolicy` resources to return.
    	// The service returns fewer than this value if the number of return policies
    	// for the given merchant is less that than the `pageSize`. The default value
    	// is 10. The maximum value is 100; If a value higher than the maximum is
    	// specified, then the `pageSize` will default to the maximum
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// Optional. A page token, received from a previous `ListOnlineReturnPolicies`
    	// call. Provide the page token to retrieve the subsequent page.
    	//
    	// When paginating, all other parameters provided to
    	// `ListOnlineReturnPolicies` must match the call that provided the page
    	// token. The token returned as
    	// [nextPageToken][google.shopping.merchant.accounts.v1beta.ListOnlineReturnPoliciesResponse.next_page_token]
    	// in the response to the previous request.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the `ListOnlineReturnPolicies` method.

### func (*ListOnlineReturnPoliciesRequest) Descriptor 
    
    
    func (*ListOnlineReturnPoliciesRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListOnlineReturnPoliciesRequest.ProtoReflect.Descriptor instead.

### func (*ListOnlineReturnPoliciesRequest) GetPageSize 
    
    
    func (x *ListOnlineReturnPoliciesRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListOnlineReturnPoliciesRequest) GetPageToken 
    
    
    func (x *ListOnlineReturnPoliciesRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListOnlineReturnPoliciesRequest) GetParent 
    
    
    func (x *ListOnlineReturnPoliciesRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListOnlineReturnPoliciesRequest) ProtoMessage 
    
    
    func (*ListOnlineReturnPoliciesRequest) ProtoMessage()

### func (*ListOnlineReturnPoliciesRequest) ProtoReflect 
    
    
    func (x *ListOnlineReturnPoliciesRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListOnlineReturnPoliciesRequest) Reset 
    
    
    func (x *ListOnlineReturnPoliciesRequest) Reset()

### func (*ListOnlineReturnPoliciesRequest) String 
    
    
    func (x *ListOnlineReturnPoliciesRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListOnlineReturnPoliciesResponse
    
    
    type ListOnlineReturnPoliciesResponse struct {
    
    	// The retrieved return policies.
    	OnlineReturnPolicies []*OnlineReturnPolicy `protobuf:"bytes,1,rep,name=online_return_policies,json=onlineReturnPolicies,proto3" json:"online_return_policies,omitempty"`
    	// A token, which can be sent as `pageToken` to retrieve the next page.
    	// If this field is omitted, there are no subsequent pages.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Response message for the `ListOnlineReturnPolicies` method.

### func (*ListOnlineReturnPoliciesResponse) Descriptor 
    
    
    func (*ListOnlineReturnPoliciesResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListOnlineReturnPoliciesResponse.ProtoReflect.Descriptor instead.

### func (*ListOnlineReturnPoliciesResponse) GetNextPageToken 
    
    
    func (x *ListOnlineReturnPoliciesResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListOnlineReturnPoliciesResponse) GetOnlineReturnPolicies 
    
    
    func (x *ListOnlineReturnPoliciesResponse) GetOnlineReturnPolicies() []*OnlineReturnPolicy

### func (*ListOnlineReturnPoliciesResponse) ProtoMessage 
    
    
    func (*ListOnlineReturnPoliciesResponse) ProtoMessage()

### func (*ListOnlineReturnPoliciesResponse) ProtoReflect 
    
    
    func (x *ListOnlineReturnPoliciesResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListOnlineReturnPoliciesResponse) Reset 
    
    
    func (x *ListOnlineReturnPoliciesResponse) Reset()

### func (*ListOnlineReturnPoliciesResponse) String 
    
    
    func (x *ListOnlineReturnPoliciesResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListProgramsRequest
    
    
    type ListProgramsRequest struct {
    
    	// Required. The name of the account for which to retrieve all programs.
    	// Format: `accounts/{account}`
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Optional. The maximum number of programs to return in a single response. If
    	// unspecified (or 0), a default size of 1000 is used. The maximum value is
    	// 1000; values above 1000 will be coerced to 1000.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// Optional. A continuation token, received from a previous `ListPrograms`
    	// call. Provide this to retrieve the next page.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the ListPrograms method.

### func (*ListProgramsRequest) Descriptor 
    
    
    func (*ListProgramsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListProgramsRequest.ProtoReflect.Descriptor instead.

### func (*ListProgramsRequest) GetPageSize 
    
    
    func (x *ListProgramsRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListProgramsRequest) GetPageToken 
    
    
    func (x *ListProgramsRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListProgramsRequest) GetParent 
    
    
    func (x *ListProgramsRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListProgramsRequest) ProtoMessage 
    
    
    func (*ListProgramsRequest) ProtoMessage()

### func (*ListProgramsRequest) ProtoReflect 
    
    
    func (x *ListProgramsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListProgramsRequest) Reset 
    
    
    func (x *ListProgramsRequest) Reset()

### func (*ListProgramsRequest) String 
    
    
    func (x *ListProgramsRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListProgramsResponse
    
    
    type ListProgramsResponse struct {
    
    	// The programs for the given account.
    	Programs []*Program `protobuf:"bytes,1,rep,name=programs,proto3" json:"programs,omitempty"`
    	// A token that can be sent as `page_token` to retrieve the next page. If this
    	// field is omitted, there are no subsequent pages.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Response message for the ListPrograms method.

### func (*ListProgramsResponse) Descriptor 
    
    
    func (*ListProgramsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListProgramsResponse.ProtoReflect.Descriptor instead.

### func (*ListProgramsResponse) GetNextPageToken 
    
    
    func (x *ListProgramsResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListProgramsResponse) GetPrograms 
    
    
    func (x *ListProgramsResponse) GetPrograms() []*Program

### func (*ListProgramsResponse) ProtoMessage 
    
    
    func (*ListProgramsResponse) ProtoMessage()

### func (*ListProgramsResponse) ProtoReflect 
    
    
    func (x *ListProgramsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListProgramsResponse) Reset 
    
    
    func (x *ListProgramsResponse) Reset()

### func (*ListProgramsResponse) String 
    
    
    func (x *ListProgramsResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListRegionsRequest
    
    
    type ListRegionsRequest struct {
    
    	// Required. The account to list regions for.
    	// Format: `accounts/{account}`
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Optional. The maximum number of regions to return. The service may return
    	// fewer than this value.
    	// If unspecified, at most 50 regions will be returned.
    	// The maximum value is 1000; values above 1000 will be coerced to 1000.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// Optional. A page token, received from a previous `ListRegions` call.
    	// Provide this to retrieve the subsequent page.
    	//
    	// When paginating, all other parameters provided to `ListRegions` must
    	// match the call that provided the page token.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the `ListRegions` method.

### func (*ListRegionsRequest) Descriptor 
    
    
    func (*ListRegionsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListRegionsRequest.ProtoReflect.Descriptor instead.

### func (*ListRegionsRequest) GetPageSize 
    
    
    func (x *ListRegionsRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListRegionsRequest) GetPageToken 
    
    
    func (x *ListRegionsRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListRegionsRequest) GetParent 
    
    
    func (x *ListRegionsRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListRegionsRequest) ProtoMessage 
    
    
    func (*ListRegionsRequest) ProtoMessage()

### func (*ListRegionsRequest) ProtoReflect 
    
    
    func (x *ListRegionsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListRegionsRequest) Reset 
    
    
    func (x *ListRegionsRequest) Reset()

### func (*ListRegionsRequest) String 
    
    
    func (x *ListRegionsRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListRegionsResponse
    
    
    type ListRegionsResponse struct {
    
    	// The regions from the specified merchant.
    	Regions []*Region `protobuf:"bytes,1,rep,name=regions,proto3" json:"regions,omitempty"`
    	// A token, which can be sent as `page_token` to retrieve the next page.
    	// If this field is omitted, there are no subsequent pages.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Response message for the `ListRegions` method.

### func (*ListRegionsResponse) Descriptor 
    
    
    func (*ListRegionsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListRegionsResponse.ProtoReflect.Descriptor instead.

### func (*ListRegionsResponse) GetNextPageToken 
    
    
    func (x *ListRegionsResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListRegionsResponse) GetRegions 
    
    
    func (x *ListRegionsResponse) GetRegions() []*Region

### func (*ListRegionsResponse) ProtoMessage 
    
    
    func (*ListRegionsResponse) ProtoMessage()

### func (*ListRegionsResponse) ProtoReflect 
    
    
    func (x *ListRegionsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListRegionsResponse) Reset 
    
    
    func (x *ListRegionsResponse) Reset()

### func (*ListRegionsResponse) String 
    
    
    func (x *ListRegionsResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListSubAccountsRequest
    
    
    type ListSubAccountsRequest struct {
    
    	// Required. The parent account.
    	// Format: `accounts/{account}`
    	Provider [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=provider,proto3" json:"provider,omitempty"`
    	// Optional. The maximum number of accounts to return. The service may return
    	// fewer than this value.  If unspecified, at most 250 accounts are returned.
    	// The maximum value is 500; values above 500 are coerced to 500.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// Optional. A page token, received from a previous `ListAccounts` call.
    	// Provide this to retrieve the subsequent page.
    	//
    	// When paginating, all other parameters provided to `ListAccounts` must match
    	// the call that provided the page token.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the `ListSubAccounts` method.

### func (*ListSubAccountsRequest) Descriptor 
    
    
    func (*ListSubAccountsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListSubAccountsRequest.ProtoReflect.Descriptor instead.

### func (*ListSubAccountsRequest) GetPageSize 
    
    
    func (x *ListSubAccountsRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListSubAccountsRequest) GetPageToken 
    
    
    func (x *ListSubAccountsRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListSubAccountsRequest) GetProvider 
    
    
    func (x *ListSubAccountsRequest) GetProvider() [string](https://pkg.go.dev/builtin#string)

### func (*ListSubAccountsRequest) ProtoMessage 
    
    
    func (*ListSubAccountsRequest) ProtoMessage()

### func (*ListSubAccountsRequest) ProtoReflect 
    
    
    func (x *ListSubAccountsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListSubAccountsRequest) Reset 
    
    
    func (x *ListSubAccountsRequest) Reset()

### func (*ListSubAccountsRequest) String 
    
    
    func (x *ListSubAccountsRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListSubAccountsResponse
    
    
    type ListSubAccountsResponse struct {
    
    	// The accounts for which the given parent account is an aggregator.
    	Accounts []*Account `protobuf:"bytes,1,rep,name=accounts,proto3" json:"accounts,omitempty"`
    	// A token, which can be sent as `page_token` to retrieve the next page.
    	// If this field is omitted, there are no subsequent pages.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Response message for the `ListSubAccounts` method.

### func (*ListSubAccountsResponse) Descriptor 
    
    
    func (*ListSubAccountsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListSubAccountsResponse.ProtoReflect.Descriptor instead.

### func (*ListSubAccountsResponse) GetAccounts 
    
    
    func (x *ListSubAccountsResponse) GetAccounts() []*Account

### func (*ListSubAccountsResponse) GetNextPageToken 
    
    
    func (x *ListSubAccountsResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListSubAccountsResponse) ProtoMessage 
    
    
    func (*ListSubAccountsResponse) ProtoMessage()

### func (*ListSubAccountsResponse) ProtoReflect 
    
    
    func (x *ListSubAccountsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListSubAccountsResponse) Reset 
    
    
    func (x *ListSubAccountsResponse) Reset()

### func (*ListSubAccountsResponse) String 
    
    
    func (x *ListSubAccountsResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListUsersRequest
    
    
    type ListUsersRequest struct {
    
    	// Required. The parent, which owns this collection of users.
    	// Format: `accounts/{account}`
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Optional. The maximum number of users to return. The service may return
    	// fewer than this value. If unspecified, at most 50 users will be returned.
    	// The maximum value is 100; values above 100 will be coerced to 100
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// Optional. A page token, received from a previous `ListUsers` call.
    	// Provide this to retrieve the subsequent page.
    	//
    	// When paginating, all other parameters provided to `ListUsers` must match
    	// the call that provided the page token.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the `ListUsers` method.

### func (*ListUsersRequest) Descriptor 
    
    
    func (*ListUsersRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListUsersRequest.ProtoReflect.Descriptor instead.

### func (*ListUsersRequest) GetPageSize 
    
    
    func (x *ListUsersRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListUsersRequest) GetPageToken 
    
    
    func (x *ListUsersRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListUsersRequest) GetParent 
    
    
    func (x *ListUsersRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListUsersRequest) ProtoMessage 
    
    
    func (*ListUsersRequest) ProtoMessage()

### func (*ListUsersRequest) ProtoReflect 
    
    
    func (x *ListUsersRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListUsersRequest) Reset 
    
    
    func (x *ListUsersRequest) Reset()

### func (*ListUsersRequest) String 
    
    
    func (x *ListUsersRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListUsersResponse
    
    
    type ListUsersResponse struct {
    
    	// The users from the specified account.
    	Users []*User `protobuf:"bytes,1,rep,name=users,proto3" json:"users,omitempty"`
    	// A token, which can be sent as `page_token` to retrieve the next page.
    	// If this field is omitted, there are no subsequent pages.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Response message for the `ListUsers` method.

### func (*ListUsersResponse) Descriptor 
    
    
    func (*ListUsersResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListUsersResponse.ProtoReflect.Descriptor instead.

### func (*ListUsersResponse) GetNextPageToken 
    
    
    func (x *ListUsersResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListUsersResponse) GetUsers 
    
    
    func (x *ListUsersResponse) GetUsers() []*User

### func (*ListUsersResponse) ProtoMessage 
    
    
    func (*ListUsersResponse) ProtoMessage()

### func (*ListUsersResponse) ProtoReflect 
    
    
    func (x *ListUsersResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListUsersResponse) Reset 
    
    
    func (x *ListUsersResponse) Reset()

### func (*ListUsersResponse) String 
    
    
    func (x *ListUsersResponse) String() [string](https://pkg.go.dev/builtin#string)

## LocationIdSet
    
    
    type LocationIdSet struct {
    
    	// Required. A non-empty list of
    	// [location
    	// IDs](https://developers.google.com/adwords/api/docs/appendix/geotargeting).
    	// They must all be of the same location type (For
    	// example, state).
    	LocationIds [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,rep,name=location_ids,json=locationIds,proto3" json:"location_ids,omitempty"`
    	// contains filtered or unexported fields
    }

A list of location ID sets. Must be non-empty. Can only be set if all other fields are not set.

### func (*LocationIdSet) Descriptor 
    
    
    func (*LocationIdSet) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use LocationIdSet.ProtoReflect.Descriptor instead.

### func (*LocationIdSet) GetLocationIds 
    
    
    func (x *LocationIdSet) GetLocationIds() [][string](https://pkg.go.dev/builtin#string)

### func (*LocationIdSet) ProtoMessage 
    
    
    func (*LocationIdSet) ProtoMessage()

### func (*LocationIdSet) ProtoReflect 
    
    
    func (x *LocationIdSet) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*LocationIdSet) Reset 
    
    
    func (x *LocationIdSet) Reset()

### func (*LocationIdSet) String 
    
    
    func (x *LocationIdSet) String() [string](https://pkg.go.dev/builtin#string)

## MinimumOrderValueTable
    
    
    type MinimumOrderValueTable struct {
    
    	// Required. A list of store code sets sharing the same minimum order value
    	// (MOV). At least two sets are required and the last one must be empty, which
    	// signifies 'MOV for all other stores'. Each store code can only appear once
    	// across all the sets. All prices within a service must have the same
    	// currency.
    	StoreCodeSetWithMovs []*MinimumOrderValueTable_StoreCodeSetWithMov `protobuf:"bytes,1,rep,name=store_code_set_with_movs,json=storeCodeSetWithMovs,proto3" json:"store_code_set_with_movs,omitempty"`
    	// contains filtered or unexported fields
    }

Table of per store minimum order values for the pickup fulfillment type.

### func (*MinimumOrderValueTable) Descriptor 
    
    
    func (*MinimumOrderValueTable) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use MinimumOrderValueTable.ProtoReflect.Descriptor instead.

### func (*MinimumOrderValueTable) GetStoreCodeSetWithMovs 
    
    
    func (x *MinimumOrderValueTable) GetStoreCodeSetWithMovs() []*MinimumOrderValueTable_StoreCodeSetWithMov

### func (*MinimumOrderValueTable) ProtoMessage 
    
    
    func (*MinimumOrderValueTable) ProtoMessage()

### func (*MinimumOrderValueTable) ProtoReflect 
    
    
    func (x *MinimumOrderValueTable) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*MinimumOrderValueTable) Reset 
    
    
    func (x *MinimumOrderValueTable) Reset()

### func (*MinimumOrderValueTable) String 
    
    
    func (x *MinimumOrderValueTable) String() [string](https://pkg.go.dev/builtin#string)

## MinimumOrderValueTable_StoreCodeSetWithMov
    
    
    type MinimumOrderValueTable_StoreCodeSetWithMov struct {
    
    	// Optional. A list of unique store codes or empty for the catch all.
    	StoreCodes [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,rep,name=store_codes,json=storeCodes,proto3" json:"store_codes,omitempty"`
    	// The minimum order value for the given stores.
    	Value *typepb.Price `protobuf:"bytes,2,opt,name=value,proto3,oneof" json:"value,omitempty"`
    	// contains filtered or unexported fields
    }

A list of store code sets sharing the same minimum order value. At least two sets are required and the last one must be empty, which signifies 'MOV for all other stores'. Each store code can only appear once across all the sets. All prices within a service must have the same currency.

### func (*MinimumOrderValueTable_StoreCodeSetWithMov) Descriptor 
    
    
    func (*MinimumOrderValueTable_StoreCodeSetWithMov) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use MinimumOrderValueTable_StoreCodeSetWithMov.ProtoReflect.Descriptor instead.

### func (*MinimumOrderValueTable_StoreCodeSetWithMov) GetStoreCodes 
    
    
    func (x *MinimumOrderValueTable_StoreCodeSetWithMov) GetStoreCodes() [][string](https://pkg.go.dev/builtin#string)

### func (*MinimumOrderValueTable_StoreCodeSetWithMov) GetValue 
    
    
    func (x *MinimumOrderValueTable_StoreCodeSetWithMov) GetValue() *[typepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/type/typepb).[Price](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/type/typepb#cloud_google_com_go_shopping_type_typepb_Price)

### func (*MinimumOrderValueTable_StoreCodeSetWithMov) ProtoMessage 
    
    
    func (*MinimumOrderValueTable_StoreCodeSetWithMov) ProtoMessage()

### func (*MinimumOrderValueTable_StoreCodeSetWithMov) ProtoReflect 
    
    
    func (x *MinimumOrderValueTable_StoreCodeSetWithMov) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*MinimumOrderValueTable_StoreCodeSetWithMov) Reset 
    
    
    func (x *MinimumOrderValueTable_StoreCodeSetWithMov) Reset()

### func (*MinimumOrderValueTable_StoreCodeSetWithMov) String 
    
    
    func (x *MinimumOrderValueTable_StoreCodeSetWithMov) String() [string](https://pkg.go.dev/builtin#string)

## OmnichannelSetting
    
    
    type OmnichannelSetting struct {
    
    	// Identifier. The resource name of the omnichannel setting. Format:
    	// `accounts/{account}/omnichannelSettings/{omnichannel_setting}`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Required. Immutable. Region code defined by
    	// [CLDR](https://cldr.unicode.org/). Must be provided in the Create method,
    	// and is immutable.
    	RegionCode [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=region_code,json=regionCode,proto3" json:"region_code,omitempty"`
    	// Required. The Local Store Front type for this country.
    	LsfType OmnichannelSetting_LsfType `protobuf:"varint,12,opt,name=lsf_type,json=lsfType,proto3,enum=google.shopping.merchant.accounts.v1beta.OmnichannelSetting_LsfType" json:"lsf_type,omitempty"`
    	// Optional. The InStock URI and state for this country.
    	InStock *InStock `protobuf:"bytes,13,opt,name=in_stock,json=inStock,proto3" json:"in_stock,omitempty"`
    	// Optional. The Pickup URI and state for this country.
    	Pickup *Pickup `protobuf:"bytes,14,opt,name=pickup,proto3" json:"pickup,omitempty"`
    	// Output only. The established link to a LFP provider.
    	LfpLink *LfpLink `protobuf:"bytes,5,opt,name=lfp_link,json=lfpLink,proto3" json:"lfp_link,omitempty"`
    	// Optional. The On Display to Order (ODO) policy URI and state for this
    	// country.
    	Odo *OnDisplayToOrder `protobuf:"bytes,6,opt,name=odo,proto3" json:"odo,omitempty"`
    	// Optional. The about page URI and state for this country.
    	About *About `protobuf:"bytes,7,opt,name=about,proto3" json:"about,omitempty"`
    	// Optional. The inventory verification contact and state for this country.
    	InventoryVerification *InventoryVerification `protobuf:"bytes,8,opt,name=inventory_verification,json=inventoryVerification,proto3" json:"inventory_verification,omitempty"`
    	// contains filtered or unexported fields
    }

Collection of information related to the omnichannel settings of a merchant.

### func (*OmnichannelSetting) Descriptor 
    
    
    func (*OmnichannelSetting) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use OmnichannelSetting.ProtoReflect.Descriptor instead.

### func (*OmnichannelSetting) GetAbout 
    
    
    func (x *OmnichannelSetting) GetAbout() *About

### func (*OmnichannelSetting) GetInStock 
    
    
    func (x *OmnichannelSetting) GetInStock() *InStock

### func (*OmnichannelSetting) GetInventoryVerification 
    
    
    func (x *OmnichannelSetting) GetInventoryVerification() *InventoryVerification

### func (*OmnichannelSetting) GetLfpLink 
    
    
    func (x *OmnichannelSetting) GetLfpLink() *LfpLink

### func (*OmnichannelSetting) GetLsfType 
    
    
    func (x *OmnichannelSetting) GetLsfType() OmnichannelSetting_LsfType

### func (*OmnichannelSetting) GetName 
    
    
    func (x *OmnichannelSetting) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*OmnichannelSetting) GetOdo 
    
    
    func (x *OmnichannelSetting) GetOdo() *OnDisplayToOrder

### func (*OmnichannelSetting) GetPickup 
    
    
    func (x *OmnichannelSetting) GetPickup() *Pickup

### func (*OmnichannelSetting) GetRegionCode 
    
    
    func (x *OmnichannelSetting) GetRegionCode() [string](https://pkg.go.dev/builtin#string)

### func (*OmnichannelSetting) ProtoMessage 
    
    
    func (*OmnichannelSetting) ProtoMessage()

### func (*OmnichannelSetting) ProtoReflect 
    
    
    func (x *OmnichannelSetting) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*OmnichannelSetting) Reset 
    
    
    func (x *OmnichannelSetting) Reset()

### func (*OmnichannelSetting) String 
    
    
    func (x *OmnichannelSetting) String() [string](https://pkg.go.dev/builtin#string)

## OmnichannelSetting_LsfType
    
    
    type OmnichannelSetting_LsfType [int32](https://pkg.go.dev/builtin#int32)

The product page experience type, which is also called the Local Store Front (LSF) type. Check the [HC article](https://support.google.com/merchants/answer/7178526) for more details.

### OmnichannelSetting_LSF_TYPE_UNSPECIFIED, OmnichannelSetting_GHLSF, OmnichannelSetting_MHLSF_BASIC, OmnichannelSetting_MHLSF_FULL
    
    
    const (
    	// Default value. This value is unused.
    	OmnichannelSetting_LSF_TYPE_UNSPECIFIED OmnichannelSetting_LsfType = 0
    	// Google-Hosted Local Store Front. Check the [HC
    	// article](https://support.google.com/merchants/answer/14869424) for more
    	// details.
    	OmnichannelSetting_GHLSF OmnichannelSetting_LsfType = 1
    	// Merchant-Hosted Local Store Front Basic. Check the [HC
    	// article](https://support.google.com/merchants/answer/14615867) for more
    	// details.
    	OmnichannelSetting_MHLSF_BASIC OmnichannelSetting_LsfType = 2
    	// Merchant-Hosted Local Store Front Full. Check the [HC
    	// article](https://support.google.com/merchants/answer/14617076) for more
    	// details.
    	OmnichannelSetting_MHLSF_FULL OmnichannelSetting_LsfType = 3
    )

### func (OmnichannelSetting_LsfType) Descriptor 
    
    
    func (OmnichannelSetting_LsfType) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (OmnichannelSetting_LsfType) Enum 
    
    
    func (x OmnichannelSetting_LsfType) Enum() *OmnichannelSetting_LsfType

### func (OmnichannelSetting_LsfType) EnumDescriptor 
    
    
    func (OmnichannelSetting_LsfType) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use OmnichannelSetting_LsfType.Descriptor instead.

### func (OmnichannelSetting_LsfType) Number 
    
    
    func (x OmnichannelSetting_LsfType) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (OmnichannelSetting_LsfType) String 
    
    
    func (x OmnichannelSetting_LsfType) String() [string](https://pkg.go.dev/builtin#string)

### func (OmnichannelSetting_LsfType) Type 
    
    
    func (OmnichannelSetting_LsfType) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## OmnichannelSettingsServiceClient
    
    
    type OmnichannelSettingsServiceClient interface {
    	// Get the omnichannel settings for a given merchant.
    	GetOmnichannelSetting(ctx context.Context, in *GetOmnichannelSettingRequest, opts ...grpc.CallOption) (*OmnichannelSetting, [error](https://pkg.go.dev/builtin#error))
    	// List all the omnichannel settings for a given merchant.
    	ListOmnichannelSettings(ctx context.Context, in *ListOmnichannelSettingsRequest, opts ...grpc.CallOption) (*ListOmnichannelSettingsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Create the omnichannel settings for a given merchant.
    	CreateOmnichannelSetting(ctx context.Context, in *CreateOmnichannelSettingRequest, opts ...grpc.CallOption) (*OmnichannelSetting, [error](https://pkg.go.dev/builtin#error))
    	// Update the omnichannel setting for a given merchant in a given country.
    	UpdateOmnichannelSetting(ctx context.Context, in *UpdateOmnichannelSettingRequest, opts ...grpc.CallOption) (*OmnichannelSetting, [error](https://pkg.go.dev/builtin#error))
    	// Requests inventory verification for a given merchant in a given country.
    	RequestInventoryVerification(ctx context.Context, in *RequestInventoryVerificationRequest, opts ...grpc.CallOption) (*RequestInventoryVerificationResponse, [error](https://pkg.go.dev/builtin#error))
    }

OmnichannelSettingsServiceClient is the client API for OmnichannelSettingsService service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

### func NewOmnichannelSettingsServiceClient 
    
    
    func NewOmnichannelSettingsServiceClient(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) OmnichannelSettingsServiceClient

## OmnichannelSettingsServiceServer
    
    
    type OmnichannelSettingsServiceServer interface {
    	// Get the omnichannel settings for a given merchant.
    	GetOmnichannelSetting(context.Context, *GetOmnichannelSettingRequest) (*OmnichannelSetting, [error](https://pkg.go.dev/builtin#error))
    	// List all the omnichannel settings for a given merchant.
    	ListOmnichannelSettings(context.Context, *ListOmnichannelSettingsRequest) (*ListOmnichannelSettingsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Create the omnichannel settings for a given merchant.
    	CreateOmnichannelSetting(context.Context, *CreateOmnichannelSettingRequest) (*OmnichannelSetting, [error](https://pkg.go.dev/builtin#error))
    	// Update the omnichannel setting for a given merchant in a given country.
    	UpdateOmnichannelSetting(context.Context, *UpdateOmnichannelSettingRequest) (*OmnichannelSetting, [error](https://pkg.go.dev/builtin#error))
    	// Requests inventory verification for a given merchant in a given country.
    	RequestInventoryVerification(context.Context, *RequestInventoryVerificationRequest) (*RequestInventoryVerificationResponse, [error](https://pkg.go.dev/builtin#error))
    }

OmnichannelSettingsServiceServer is the server API for OmnichannelSettingsService service. All implementations should embed UnimplementedOmnichannelSettingsServiceServer for forward compatibility

## OnDisplayToOrder
    
    
    type OnDisplayToOrder struct {
    
    	// Required. The on display to order (ODO) policy URI.
    	Uri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=uri,proto3" json:"uri,omitempty"`
    	// Output only. The state of the URI.
    	State ReviewState_State `protobuf:"varint,2,opt,name=state,proto3,enum=google.shopping.merchant.accounts.v1beta.ReviewState_State" json:"state,omitempty"`
    	// contains filtered or unexported fields
    }

Collection of information related to the on display to order ([ODO](https://support.google.com/merchants/answer/14615056?hl=en&ref_topic=15145747&sjid=6892280366904591178-NC)).

### func (*OnDisplayToOrder) Descriptor 
    
    
    func (*OnDisplayToOrder) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use OnDisplayToOrder.ProtoReflect.Descriptor instead.

### func (*OnDisplayToOrder) GetState 
    
    
    func (x *OnDisplayToOrder) GetState() ReviewState_State

### func (*OnDisplayToOrder) GetUri 
    
    
    func (x *OnDisplayToOrder) GetUri() [string](https://pkg.go.dev/builtin#string)

### func (*OnDisplayToOrder) ProtoMessage 
    
    
    func (*OnDisplayToOrder) ProtoMessage()

### func (*OnDisplayToOrder) ProtoReflect 
    
    
    func (x *OnDisplayToOrder) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*OnDisplayToOrder) Reset 
    
    
    func (x *OnDisplayToOrder) Reset()

### func (*OnDisplayToOrder) String 
    
    
    func (x *OnDisplayToOrder) String() [string](https://pkg.go.dev/builtin#string)

## OnlineReturnPolicy
    
    
    type OnlineReturnPolicy struct {
    
    	// Identifier. The name of the `OnlineReturnPolicy` resource.
    	// Format: `accounts/{account}/onlineReturnPolicies/{return_policy}`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Output only. Return policy ID generated by Google.
    	ReturnPolicyId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=return_policy_id,json=returnPolicyId,proto3" json:"return_policy_id,omitempty"`
    	// Required. Immutable. This field represents the unique user-defined label of
    	// the return policy. It is important to note that the same label cannot be
    	// used in different return policies for the same country. Unless a product
    	// specifies a specific label attribute, policies will be automatically
    	// labeled as 'default'. To assign a custom return policy to certain product
    	// groups, follow the instructions provided in the [Return policy label]
    	// (https://support.google.com/merchants/answer/9445425).
    	// The label can contain up to 50 characters.
    	Label [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=label,proto3" json:"label,omitempty"`
    	// Required. Immutable. The countries of sale where the return policy applies.
    	// The values must be a valid 2 letter ISO 3166 code.
    	Countries [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,rep,name=countries,proto3" json:"countries,omitempty"`
    	// Optional. The return policy.
    	Policy *OnlineReturnPolicy_Policy `protobuf:"bytes,5,opt,name=policy,proto3" json:"policy,omitempty"`
    	// Optional. Overrides to the general policy for orders placed during a
    	// specific set of time intervals.
    	SeasonalOverrides []*OnlineReturnPolicy_SeasonalOverride `protobuf:"bytes,14,rep,name=seasonal_overrides,json=seasonalOverrides,proto3" json:"seasonal_overrides,omitempty"`
    	// Optional. The restocking fee that applies to all return reason categories.
    	// This would be treated as a free restocking fee if the value is not set.
    	RestockingFee *OnlineReturnPolicy_RestockingFee `protobuf:"bytes,6,opt,name=restocking_fee,json=restockingFee,proto3" json:"restocking_fee,omitempty"`
    	// Optional. The return methods of how customers can return an item. This
    	// value is required to not be empty unless the type of return policy is
    	// noReturns.
    	ReturnMethods []OnlineReturnPolicy_ReturnMethod `protobuf:"varint,7,rep,packed,name=return_methods,json=returnMethods,proto3,enum=google.shopping.merchant.accounts.v1beta.OnlineReturnPolicy_ReturnMethod" json:"return_methods,omitempty"`
    	// Optional. The item conditions accepted for returns must not be empty unless
    	// the type of return policy is 'noReturns'.
    	ItemConditions []OnlineReturnPolicy_ItemCondition `protobuf:"varint,8,rep,packed,name=item_conditions,json=itemConditions,proto3,enum=google.shopping.merchant.accounts.v1beta.OnlineReturnPolicy_ItemCondition" json:"item_conditions,omitempty"`
    	// Optional. The return shipping fee. Should be set only when customer need to
    	// download and print the return label.
    	ReturnShippingFee *OnlineReturnPolicy_ReturnShippingFee `protobuf:"bytes,9,opt,name=return_shipping_fee,json=returnShippingFee,proto3" json:"return_shipping_fee,omitempty"`
    	// Required. The return policy uri. This can used by Google to do a sanity
    	// check for the policy. It must be a valid URL.
    	ReturnPolicyUri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,10,opt,name=return_policy_uri,json=returnPolicyUri,proto3" json:"return_policy_uri,omitempty"`
    	// Optional. This field specifies if merchant
    	// only accepts defective products for returns.
    	AcceptDefectiveOnly *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,11,opt,name=accept_defective_only,json=acceptDefectiveOnly,proto3,oneof" json:"accept_defective_only,omitempty"`
    	// Optional. The field specifies the number of
    	// days it takes for merchants to process refunds.
    	ProcessRefundDays *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,12,opt,name=process_refund_days,json=processRefundDays,proto3,oneof" json:"process_refund_days,omitempty"`
    	// Optional. This field specifies if merchant
    	// allows customers to exchange products.
    	AcceptExchange *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,13,opt,name=accept_exchange,json=acceptExchange,proto3,oneof" json:"accept_exchange,omitempty"`
    	// Optional. The field specifies the return
    	// label source.
    	ReturnLabelSource *OnlineReturnPolicy_ReturnLabelSource `protobuf:"varint,15,opt,name=return_label_source,json=returnLabelSource,proto3,enum=google.shopping.merchant.accounts.v1beta.OnlineReturnPolicy_ReturnLabelSource,oneof" json:"return_label_source,omitempty"`
    	// contains filtered or unexported fields
    }

[Online return policy](https://support.google.com/merchants/answer/10220642) object. This is currently used to represent return policies for ads and free listings programs.

### func (*OnlineReturnPolicy) Descriptor 
    
    
    func (*OnlineReturnPolicy) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use OnlineReturnPolicy.ProtoReflect.Descriptor instead.

### func (*OnlineReturnPolicy) GetAcceptDefectiveOnly 
    
    
    func (x *OnlineReturnPolicy) GetAcceptDefectiveOnly() [bool](https://pkg.go.dev/builtin#bool)

### func (*OnlineReturnPolicy) GetAcceptExchange 
    
    
    func (x *OnlineReturnPolicy) GetAcceptExchange() [bool](https://pkg.go.dev/builtin#bool)

### func (*OnlineReturnPolicy) GetCountries 
    
    
    func (x *OnlineReturnPolicy) GetCountries() [][string](https://pkg.go.dev/builtin#string)

### func (*OnlineReturnPolicy) GetItemConditions 
    
    
    func (x *OnlineReturnPolicy) GetItemConditions() []OnlineReturnPolicy_ItemCondition

### func (*OnlineReturnPolicy) GetLabel 
    
    
    func (x *OnlineReturnPolicy) GetLabel() [string](https://pkg.go.dev/builtin#string)

### func (*OnlineReturnPolicy) GetName 
    
    
    func (x *OnlineReturnPolicy) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*OnlineReturnPolicy) GetPolicy 
    
    
    func (x *OnlineReturnPolicy) GetPolicy() *OnlineReturnPolicy_Policy

### func (*OnlineReturnPolicy) GetProcessRefundDays 
    
    
    func (x *OnlineReturnPolicy) GetProcessRefundDays() [int32](https://pkg.go.dev/builtin#int32)

### func (*OnlineReturnPolicy) GetRestockingFee 
    
    
    func (x *OnlineReturnPolicy) GetRestockingFee() *OnlineReturnPolicy_RestockingFee

### func (*OnlineReturnPolicy) GetReturnLabelSource 
    
    
    func (x *OnlineReturnPolicy) GetReturnLabelSource() OnlineReturnPolicy_ReturnLabelSource

### func (*OnlineReturnPolicy) GetReturnMethods 
    
    
    func (x *OnlineReturnPolicy) GetReturnMethods() []OnlineReturnPolicy_ReturnMethod

### func (*OnlineReturnPolicy) GetReturnPolicyId 
    
    
    func (x *OnlineReturnPolicy) GetReturnPolicyId() [string](https://pkg.go.dev/builtin#string)

### func (*OnlineReturnPolicy) GetReturnPolicyUri 
    
    
    func (x *OnlineReturnPolicy) GetReturnPolicyUri() [string](https://pkg.go.dev/builtin#string)

### func (*OnlineReturnPolicy) GetReturnShippingFee 
    
    
    func (x *OnlineReturnPolicy) GetReturnShippingFee() *OnlineReturnPolicy_ReturnShippingFee

### func (*OnlineReturnPolicy) GetSeasonalOverrides 
    
    
    func (x *OnlineReturnPolicy) GetSeasonalOverrides() []*OnlineReturnPolicy_SeasonalOverride

### func (*OnlineReturnPolicy) ProtoMessage 
    
    
    func (*OnlineReturnPolicy) ProtoMessage()

### func (*OnlineReturnPolicy) ProtoReflect 
    
    
    func (x *OnlineReturnPolicy) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*OnlineReturnPolicy) Reset 
    
    
    func (x *OnlineReturnPolicy) Reset()

### func (*OnlineReturnPolicy) String 
    
    
    func (x *OnlineReturnPolicy) String() [string](https://pkg.go.dev/builtin#string)

## OnlineReturnPolicyServiceClient
    
    
    type OnlineReturnPolicyServiceClient interface {
    	// Gets an existing return policy for a given merchant.
    	GetOnlineReturnPolicy(ctx context.Context, in *GetOnlineReturnPolicyRequest, opts ...grpc.CallOption) (*OnlineReturnPolicy, [error](https://pkg.go.dev/builtin#error))
    	// Lists all existing return policies for a given merchant.
    	ListOnlineReturnPolicies(ctx context.Context, in *ListOnlineReturnPoliciesRequest, opts ...grpc.CallOption) (*ListOnlineReturnPoliciesResponse, [error](https://pkg.go.dev/builtin#error))
    	// Creates a new return policy for a given merchant.
    	CreateOnlineReturnPolicy(ctx context.Context, in *CreateOnlineReturnPolicyRequest, opts ...grpc.CallOption) (*OnlineReturnPolicy, [error](https://pkg.go.dev/builtin#error))
    	// Updates an existing return policy for a given merchant.
    	UpdateOnlineReturnPolicy(ctx context.Context, in *UpdateOnlineReturnPolicyRequest, opts ...grpc.CallOption) (*OnlineReturnPolicy, [error](https://pkg.go.dev/builtin#error))
    	// Deletes an existing return policy.
    	DeleteOnlineReturnPolicy(ctx context.Context, in *DeleteOnlineReturnPolicyRequest, opts ...grpc.CallOption) (*emptypb.Empty, [error](https://pkg.go.dev/builtin#error))
    }

OnlineReturnPolicyServiceClient is the client API for OnlineReturnPolicyService service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

### func NewOnlineReturnPolicyServiceClient 
    
    
    func NewOnlineReturnPolicyServiceClient(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) OnlineReturnPolicyServiceClient

## OnlineReturnPolicyServiceServer
    
    
    type OnlineReturnPolicyServiceServer interface {
    	// Gets an existing return policy for a given merchant.
    	GetOnlineReturnPolicy(context.Context, *GetOnlineReturnPolicyRequest) (*OnlineReturnPolicy, [error](https://pkg.go.dev/builtin#error))
    	// Lists all existing return policies for a given merchant.
    	ListOnlineReturnPolicies(context.Context, *ListOnlineReturnPoliciesRequest) (*ListOnlineReturnPoliciesResponse, [error](https://pkg.go.dev/builtin#error))
    	// Creates a new return policy for a given merchant.
    	CreateOnlineReturnPolicy(context.Context, *CreateOnlineReturnPolicyRequest) (*OnlineReturnPolicy, [error](https://pkg.go.dev/builtin#error))
    	// Updates an existing return policy for a given merchant.
    	UpdateOnlineReturnPolicy(context.Context, *UpdateOnlineReturnPolicyRequest) (*OnlineReturnPolicy, [error](https://pkg.go.dev/builtin#error))
    	// Deletes an existing return policy.
    	DeleteOnlineReturnPolicy(context.Context, *DeleteOnlineReturnPolicyRequest) (*emptypb.Empty, [error](https://pkg.go.dev/builtin#error))
    }

OnlineReturnPolicyServiceServer is the server API for OnlineReturnPolicyService service. All implementations should embed UnimplementedOnlineReturnPolicyServiceServer for forward compatibility

## OnlineReturnPolicy_ItemCondition
    
    
    type OnlineReturnPolicy_ItemCondition [int32](https://pkg.go.dev/builtin#int32)

The available item conditions.

### OnlineReturnPolicy_ITEM_CONDITION_UNSPECIFIED, OnlineReturnPolicy_NEW, OnlineReturnPolicy_USED
    
    
    const (
    	// Default value. This value is unused.
    	OnlineReturnPolicy_ITEM_CONDITION_UNSPECIFIED OnlineReturnPolicy_ItemCondition = 0
    	// New.
    	OnlineReturnPolicy_NEW OnlineReturnPolicy_ItemCondition = 1
    	// Used.
    	OnlineReturnPolicy_USED OnlineReturnPolicy_ItemCondition = 2
    )

### func (OnlineReturnPolicy_ItemCondition) Descriptor 
    
    
    func (OnlineReturnPolicy_ItemCondition) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (OnlineReturnPolicy_ItemCondition) Enum 
    
    
    func (x OnlineReturnPolicy_ItemCondition) Enum() *OnlineReturnPolicy_ItemCondition

### func (OnlineReturnPolicy_ItemCondition) EnumDescriptor 
    
    
    func (OnlineReturnPolicy_ItemCondition) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use OnlineReturnPolicy_ItemCondition.Descriptor instead.

### func (OnlineReturnPolicy_ItemCondition) Number 
    
    
    func (x OnlineReturnPolicy_ItemCondition) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (OnlineReturnPolicy_ItemCondition) String 
    
    
    func (x OnlineReturnPolicy_ItemCondition) String() [string](https://pkg.go.dev/builtin#string)

### func (OnlineReturnPolicy_ItemCondition) Type 
    
    
    func (OnlineReturnPolicy_ItemCondition) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## OnlineReturnPolicy_Policy
    
    
    type OnlineReturnPolicy_Policy struct {
    
    	// Policy type.
    	Type OnlineReturnPolicy_Policy_Type `protobuf:"varint,1,opt,name=type,proto3,enum=google.shopping.merchant.accounts.v1beta.OnlineReturnPolicy_Policy_Type" json:"type,omitempty"`
    	// The number of days items can be returned after delivery, where one day
    	// is defined as 24 hours after the delivery timestamp. Required for
    	// `NUMBER_OF_DAYS_AFTER_DELIVERY` returns.
    	Days [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,2,opt,name=days,proto3" json:"days,omitempty"`
    	// contains filtered or unexported fields
    }

The available policies.

### func (*OnlineReturnPolicy_Policy) Descriptor 
    
    
    func (*OnlineReturnPolicy_Policy) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use OnlineReturnPolicy_Policy.ProtoReflect.Descriptor instead.

### func (*OnlineReturnPolicy_Policy) GetDays 
    
    
    func (x *OnlineReturnPolicy_Policy) GetDays() [int64](https://pkg.go.dev/builtin#int64)

### func (*OnlineReturnPolicy_Policy) GetType 
    
    
    func (x *OnlineReturnPolicy_Policy) GetType() OnlineReturnPolicy_Policy_Type

### func (*OnlineReturnPolicy_Policy) ProtoMessage 
    
    
    func (*OnlineReturnPolicy_Policy) ProtoMessage()

### func (*OnlineReturnPolicy_Policy) ProtoReflect 
    
    
    func (x *OnlineReturnPolicy_Policy) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*OnlineReturnPolicy_Policy) Reset 
    
    
    func (x *OnlineReturnPolicy_Policy) Reset()

### func (*OnlineReturnPolicy_Policy) String 
    
    
    func (x *OnlineReturnPolicy_Policy) String() [string](https://pkg.go.dev/builtin#string)

## OnlineReturnPolicy_Policy_Type
    
    
    type OnlineReturnPolicy_Policy_Type [int32](https://pkg.go.dev/builtin#int32)

Return policy types.

### OnlineReturnPolicy_Policy_TYPE_UNSPECIFIED, OnlineReturnPolicy_Policy_NUMBER_OF_DAYS_AFTER_DELIVERY, OnlineReturnPolicy_Policy_NO_RETURNS, OnlineReturnPolicy_Policy_LIFETIME_RETURNS
    
    
    const (
    	// Default value. This value is unused.
    	OnlineReturnPolicy_Policy_TYPE_UNSPECIFIED OnlineReturnPolicy_Policy_Type = 0
    	// The number of days within which a return is valid after delivery.
    	OnlineReturnPolicy_Policy_NUMBER_OF_DAYS_AFTER_DELIVERY OnlineReturnPolicy_Policy_Type = 1
    	// No returns.
    	OnlineReturnPolicy_Policy_NO_RETURNS OnlineReturnPolicy_Policy_Type = 2
    	// Life time returns.
    	OnlineReturnPolicy_Policy_LIFETIME_RETURNS OnlineReturnPolicy_Policy_Type = 3
    )

### func (OnlineReturnPolicy_Policy_Type) Descriptor 
    
    
    func (OnlineReturnPolicy_Policy_Type) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (OnlineReturnPolicy_Policy_Type) Enum 
    
    
    func (x OnlineReturnPolicy_Policy_Type) Enum() *OnlineReturnPolicy_Policy_Type

### func (OnlineReturnPolicy_Policy_Type) EnumDescriptor 
    
    
    func (OnlineReturnPolicy_Policy_Type) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use OnlineReturnPolicy_Policy_Type.Descriptor instead.

### func (OnlineReturnPolicy_Policy_Type) Number 
    
    
    func (x OnlineReturnPolicy_Policy_Type) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (OnlineReturnPolicy_Policy_Type) String 
    
    
    func (x OnlineReturnPolicy_Policy_Type) String() [string](https://pkg.go.dev/builtin#string)

### func (OnlineReturnPolicy_Policy_Type) Type 
    
    
    func (OnlineReturnPolicy_Policy_Type) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## OnlineReturnPolicy_RestockingFee
    
    
    type OnlineReturnPolicy_RestockingFee struct {
    
    	// Types that are valid to be assigned to Type:
    	//
    	//	*OnlineReturnPolicy_RestockingFee_FixedFee
    	//	*OnlineReturnPolicy_RestockingFee_MicroPercent
    	Type isOnlineReturnPolicy_RestockingFee_Type `protobuf_oneof:"type"`
    	// contains filtered or unexported fields
    }

The restocking fee. This can be a flat fee or a micro percent.

### func (*OnlineReturnPolicy_RestockingFee) Descriptor 
    
    
    func (*OnlineReturnPolicy_RestockingFee) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use OnlineReturnPolicy_RestockingFee.ProtoReflect.Descriptor instead.

### func (*OnlineReturnPolicy_RestockingFee) GetFixedFee 
    
    
    func (x *OnlineReturnPolicy_RestockingFee) GetFixedFee() *[typepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/type/typepb).[Price](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/type/typepb#cloud_google_com_go_shopping_type_typepb_Price)

### func (*OnlineReturnPolicy_RestockingFee) GetMicroPercent 
    
    
    func (x *OnlineReturnPolicy_RestockingFee) GetMicroPercent() [int32](https://pkg.go.dev/builtin#int32)

### func (*OnlineReturnPolicy_RestockingFee) GetType 
    
    
    func (x *OnlineReturnPolicy_RestockingFee) GetType() isOnlineReturnPolicy_RestockingFee_Type

### func (*OnlineReturnPolicy_RestockingFee) ProtoMessage 
    
    
    func (*OnlineReturnPolicy_RestockingFee) ProtoMessage()

### func (*OnlineReturnPolicy_RestockingFee) ProtoReflect 
    
    
    func (x *OnlineReturnPolicy_RestockingFee) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*OnlineReturnPolicy_RestockingFee) Reset 
    
    
    func (x *OnlineReturnPolicy_RestockingFee) Reset()

### func (*OnlineReturnPolicy_RestockingFee) String 
    
    
    func (x *OnlineReturnPolicy_RestockingFee) String() [string](https://pkg.go.dev/builtin#string)

## OnlineReturnPolicy_RestockingFee_FixedFee
    
    
    type OnlineReturnPolicy_RestockingFee_FixedFee struct {
    	// Fixed restocking fee.
    	FixedFee *typepb.Price `protobuf:"bytes,1,opt,name=fixed_fee,json=fixedFee,proto3,oneof"`
    }

## OnlineReturnPolicy_RestockingFee_MicroPercent
    
    
    type OnlineReturnPolicy_RestockingFee_MicroPercent struct {
    	// Percent of total price in micros. 15,000,000 means 15% of the total
    	// price would be charged.
    	MicroPercent [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=micro_percent,json=microPercent,proto3,oneof"`
    }

## OnlineReturnPolicy_ReturnLabelSource
    
    
    type OnlineReturnPolicy_ReturnLabelSource [int32](https://pkg.go.dev/builtin#int32)

The available return label sources.

### OnlineReturnPolicy_RETURN_LABEL_SOURCE_UNSPECIFIED, OnlineReturnPolicy_DOWNLOAD_AND_PRINT, OnlineReturnPolicy_IN_THE_PACKAGE, OnlineReturnPolicy_CUSTOMER_RESPONSIBILITY
    
    
    const (
    	// Default value. This value is unused.
    	OnlineReturnPolicy_RETURN_LABEL_SOURCE_UNSPECIFIED OnlineReturnPolicy_ReturnLabelSource = 0
    	// Download and print.
    	OnlineReturnPolicy_DOWNLOAD_AND_PRINT OnlineReturnPolicy_ReturnLabelSource = 1
    	// Label include in the package.
    	OnlineReturnPolicy_IN_THE_PACKAGE OnlineReturnPolicy_ReturnLabelSource = 2
    	// Customer to provide.
    	OnlineReturnPolicy_CUSTOMER_RESPONSIBILITY OnlineReturnPolicy_ReturnLabelSource = 3
    )

### func (OnlineReturnPolicy_ReturnLabelSource) Descriptor 
    
    
    func (OnlineReturnPolicy_ReturnLabelSource) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (OnlineReturnPolicy_ReturnLabelSource) Enum 
    
    
    func (x OnlineReturnPolicy_ReturnLabelSource) Enum() *OnlineReturnPolicy_ReturnLabelSource

### func (OnlineReturnPolicy_ReturnLabelSource) EnumDescriptor 
    
    
    func (OnlineReturnPolicy_ReturnLabelSource) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use OnlineReturnPolicy_ReturnLabelSource.Descriptor instead.

### func (OnlineReturnPolicy_ReturnLabelSource) Number 
    
    
    func (x OnlineReturnPolicy_ReturnLabelSource) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (OnlineReturnPolicy_ReturnLabelSource) String 
    
    
    func (x OnlineReturnPolicy_ReturnLabelSource) String() [string](https://pkg.go.dev/builtin#string)

### func (OnlineReturnPolicy_ReturnLabelSource) Type 
    
    
    func (OnlineReturnPolicy_ReturnLabelSource) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## OnlineReturnPolicy_ReturnMethod
    
    
    type OnlineReturnPolicy_ReturnMethod [int32](https://pkg.go.dev/builtin#int32)

The available return methods.

### OnlineReturnPolicy_RETURN_METHOD_UNSPECIFIED, OnlineReturnPolicy_BY_MAIL, OnlineReturnPolicy_IN_STORE, OnlineReturnPolicy_AT_A_KIOSK
    
    
    const (
    	// Default value. This value is unused.
    	OnlineReturnPolicy_RETURN_METHOD_UNSPECIFIED OnlineReturnPolicy_ReturnMethod = 0
    	// Return by mail.
    	OnlineReturnPolicy_BY_MAIL OnlineReturnPolicy_ReturnMethod = 1
    	// Return in store.
    	OnlineReturnPolicy_IN_STORE OnlineReturnPolicy_ReturnMethod = 2
    	// Return at a kiosk.
    	OnlineReturnPolicy_AT_A_KIOSK OnlineReturnPolicy_ReturnMethod = 3
    )

### func (OnlineReturnPolicy_ReturnMethod) Descriptor 
    
    
    func (OnlineReturnPolicy_ReturnMethod) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (OnlineReturnPolicy_ReturnMethod) Enum 
    
    
    func (x OnlineReturnPolicy_ReturnMethod) Enum() *OnlineReturnPolicy_ReturnMethod

### func (OnlineReturnPolicy_ReturnMethod) EnumDescriptor 
    
    
    func (OnlineReturnPolicy_ReturnMethod) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use OnlineReturnPolicy_ReturnMethod.Descriptor instead.

### func (OnlineReturnPolicy_ReturnMethod) Number 
    
    
    func (x OnlineReturnPolicy_ReturnMethod) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (OnlineReturnPolicy_ReturnMethod) String 
    
    
    func (x OnlineReturnPolicy_ReturnMethod) String() [string](https://pkg.go.dev/builtin#string)

### func (OnlineReturnPolicy_ReturnMethod) Type 
    
    
    func (OnlineReturnPolicy_ReturnMethod) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## OnlineReturnPolicy_ReturnShippingFee
    
    
    type OnlineReturnPolicy_ReturnShippingFee struct {
    
    	// Required. Type of return shipping fee.
    	Type OnlineReturnPolicy_ReturnShippingFee_Type `protobuf:"varint,1,opt,name=type,proto3,enum=google.shopping.merchant.accounts.v1beta.OnlineReturnPolicy_ReturnShippingFee_Type" json:"type,omitempty"`
    	// Fixed return shipping fee amount. This value is only applicable when type
    	// is `FIXED`. We will treat the return shipping fee as free if type is
    	// `FIXED` and this value is not set.
    	FixedFee *typepb.Price `protobuf:"bytes,2,opt,name=fixed_fee,json=fixedFee,proto3" json:"fixed_fee,omitempty"`
    	// contains filtered or unexported fields
    }

The return shipping fee. This can either be a fixed fee or a boolean to indicate that the customer pays the actual shipping cost.

### func (*OnlineReturnPolicy_ReturnShippingFee) Descriptor 
    
    
    func (*OnlineReturnPolicy_ReturnShippingFee) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use OnlineReturnPolicy_ReturnShippingFee.ProtoReflect.Descriptor instead.

### func (*OnlineReturnPolicy_ReturnShippingFee) GetFixedFee 
    
    
    func (x *OnlineReturnPolicy_ReturnShippingFee) GetFixedFee() *[typepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/type/typepb).[Price](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/type/typepb#cloud_google_com_go_shopping_type_typepb_Price)

### func (*OnlineReturnPolicy_ReturnShippingFee) GetType 
    
    
    func (x *OnlineReturnPolicy_ReturnShippingFee) GetType() OnlineReturnPolicy_ReturnShippingFee_Type

### func (*OnlineReturnPolicy_ReturnShippingFee) ProtoMessage 
    
    
    func (*OnlineReturnPolicy_ReturnShippingFee) ProtoMessage()

### func (*OnlineReturnPolicy_ReturnShippingFee) ProtoReflect 
    
    
    func (x *OnlineReturnPolicy_ReturnShippingFee) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*OnlineReturnPolicy_ReturnShippingFee) Reset 
    
    
    func (x *OnlineReturnPolicy_ReturnShippingFee) Reset()

### func (*OnlineReturnPolicy_ReturnShippingFee) String 
    
    
    func (x *OnlineReturnPolicy_ReturnShippingFee) String() [string](https://pkg.go.dev/builtin#string)

## OnlineReturnPolicy_ReturnShippingFee_Type
    
    
    type OnlineReturnPolicy_ReturnShippingFee_Type [int32](https://pkg.go.dev/builtin#int32)

Return shipping fee types.

### OnlineReturnPolicy_ReturnShippingFee_TYPE_UNSPECIFIED, OnlineReturnPolicy_ReturnShippingFee_FIXED, OnlineReturnPolicy_ReturnShippingFee_CUSTOMER_PAYING_ACTUAL_FEE
    
    
    const (
    	// Default value. This value is unused.
    	OnlineReturnPolicy_ReturnShippingFee_TYPE_UNSPECIFIED OnlineReturnPolicy_ReturnShippingFee_Type = 0
    	// The return shipping fee is a fixed value.
    	OnlineReturnPolicy_ReturnShippingFee_FIXED OnlineReturnPolicy_ReturnShippingFee_Type = 1
    	// Customers will pay the actual return shipping fee.
    	OnlineReturnPolicy_ReturnShippingFee_CUSTOMER_PAYING_ACTUAL_FEE OnlineReturnPolicy_ReturnShippingFee_Type = 2
    )

### func (OnlineReturnPolicy_ReturnShippingFee_Type) Descriptor 
    
    
    func (OnlineReturnPolicy_ReturnShippingFee_Type) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (OnlineReturnPolicy_ReturnShippingFee_Type) Enum 
    
    
    func (x OnlineReturnPolicy_ReturnShippingFee_Type) Enum() *OnlineReturnPolicy_ReturnShippingFee_Type

### func (OnlineReturnPolicy_ReturnShippingFee_Type) EnumDescriptor 
    
    
    func (OnlineReturnPolicy_ReturnShippingFee_Type) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use OnlineReturnPolicy_ReturnShippingFee_Type.Descriptor instead.

### func (OnlineReturnPolicy_ReturnShippingFee_Type) Number 
    
    
    func (x OnlineReturnPolicy_ReturnShippingFee_Type) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (OnlineReturnPolicy_ReturnShippingFee_Type) String 
    
    
    func (x OnlineReturnPolicy_ReturnShippingFee_Type) String() [string](https://pkg.go.dev/builtin#string)

### func (OnlineReturnPolicy_ReturnShippingFee_Type) Type 
    
    
    func (OnlineReturnPolicy_ReturnShippingFee_Type) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## OnlineReturnPolicy_SeasonalOverride
    
    
    type OnlineReturnPolicy_SeasonalOverride struct {
    
    	// ReturnWindow: Specifies either a fixed return date or the number of
    	// days (from the delivery date) until which a product can be returned.
    	// [Merchant Return Days](https://schema.org/merchantReturnDays)
    	//
    	// Types that are valid to be assigned to ReturnWindow:
    	//
    	//	*OnlineReturnPolicy_SeasonalOverride_ReturnDays
    	//	*OnlineReturnPolicy_SeasonalOverride_ReturnUntilDate
    	ReturnWindow isOnlineReturnPolicy_SeasonalOverride_ReturnWindow `protobuf_oneof:"return_window"`
    	// Required. Display name of this seasonal override in Merchant Center.
    	Label [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=label,proto3" json:"label,omitempty"`
    	// Required. Defines the date range when this seasonal override applies.
    	// Both start_date and end_date are inclusive.
    	// The dates of the seasonal overrides should not overlap.
    	StartDate *date.Date `protobuf:"bytes,2,opt,name=start_date,json=startDate,proto3" json:"start_date,omitempty"`
    	// Required. seasonal override end date (inclusive).
    	EndDate *date.Date `protobuf:"bytes,3,opt,name=end_date,json=endDate,proto3" json:"end_date,omitempty"`
    	// contains filtered or unexported fields
    }

### func (*OnlineReturnPolicy_SeasonalOverride) Descriptor 
    
    
    func (*OnlineReturnPolicy_SeasonalOverride) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use OnlineReturnPolicy_SeasonalOverride.ProtoReflect.Descriptor instead.

### func (*OnlineReturnPolicy_SeasonalOverride) GetEndDate 
    
    
    func (x *OnlineReturnPolicy_SeasonalOverride) GetEndDate() *[date](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/date).[Date](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/date#Date)

### func (*OnlineReturnPolicy_SeasonalOverride) GetLabel 
    
    
    func (x *OnlineReturnPolicy_SeasonalOverride) GetLabel() [string](https://pkg.go.dev/builtin#string)

### func (*OnlineReturnPolicy_SeasonalOverride) GetReturnDays 
    
    
    func (x *OnlineReturnPolicy_SeasonalOverride) GetReturnDays() [int32](https://pkg.go.dev/builtin#int32)

### func (*OnlineReturnPolicy_SeasonalOverride) GetReturnUntilDate 
    
    
    func (x *OnlineReturnPolicy_SeasonalOverride) GetReturnUntilDate() *[date](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/date).[Date](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/date#Date)

### func (*OnlineReturnPolicy_SeasonalOverride) GetReturnWindow 
    
    
    func (x *OnlineReturnPolicy_SeasonalOverride) GetReturnWindow() isOnlineReturnPolicy_SeasonalOverride_ReturnWindow

### func (*OnlineReturnPolicy_SeasonalOverride) GetStartDate 
    
    
    func (x *OnlineReturnPolicy_SeasonalOverride) GetStartDate() *[date](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/date).[Date](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/date#Date)

### func (*OnlineReturnPolicy_SeasonalOverride) ProtoMessage 
    
    
    func (*OnlineReturnPolicy_SeasonalOverride) ProtoMessage()

### func (*OnlineReturnPolicy_SeasonalOverride) ProtoReflect 
    
    
    func (x *OnlineReturnPolicy_SeasonalOverride) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*OnlineReturnPolicy_SeasonalOverride) Reset 
    
    
    func (x *OnlineReturnPolicy_SeasonalOverride) Reset()

### func (*OnlineReturnPolicy_SeasonalOverride) String 
    
    
    func (x *OnlineReturnPolicy_SeasonalOverride) String() [string](https://pkg.go.dev/builtin#string)

## OnlineReturnPolicy_SeasonalOverride_ReturnDays
    
    
    type OnlineReturnPolicy_SeasonalOverride_ReturnDays struct {
    	// Number of days (from the delivery date) that the product can be
    	// returned.
    	ReturnDays [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,5,opt,name=return_days,json=returnDays,proto3,oneof"`
    }

## OnlineReturnPolicy_SeasonalOverride_ReturnUntilDate
    
    
    type OnlineReturnPolicy_SeasonalOverride_ReturnUntilDate struct {
    	// Fixed end date until which the product can be returned.
    	ReturnUntilDate *date.Date `protobuf:"bytes,6,opt,name=return_until_date,json=returnUntilDate,proto3,oneof"`
    }

## PhoneVerificationState
    
    
    type PhoneVerificationState [int32](https://pkg.go.dev/builtin#int32)

The phone verification state.

### PhoneVerificationState_PHONE_VERIFICATION_STATE_UNSPECIFIED, PhoneVerificationState_PHONE_VERIFICATION_STATE_VERIFIED, PhoneVerificationState_PHONE_VERIFICATION_STATE_UNVERIFIED
    
    
    const (
    	// Default value. This value is unused.
    	PhoneVerificationState_PHONE_VERIFICATION_STATE_UNSPECIFIED PhoneVerificationState = 0
    	// The phone is verified.
    	PhoneVerificationState_PHONE_VERIFICATION_STATE_VERIFIED PhoneVerificationState = 1
    	// The phone is unverified
    	PhoneVerificationState_PHONE_VERIFICATION_STATE_UNVERIFIED PhoneVerificationState = 2
    )

### func (PhoneVerificationState) Descriptor 
    
    
    func (PhoneVerificationState) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (PhoneVerificationState) Enum 
    
    
    func (x PhoneVerificationState) Enum() *PhoneVerificationState

### func (PhoneVerificationState) EnumDescriptor 
    
    
    func (PhoneVerificationState) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use PhoneVerificationState.Descriptor instead.

### func (PhoneVerificationState) Number 
    
    
    func (x PhoneVerificationState) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (PhoneVerificationState) String 
    
    
    func (x PhoneVerificationState) String() [string](https://pkg.go.dev/builtin#string)

### func (PhoneVerificationState) Type 
    
    
    func (PhoneVerificationState) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Pickup
    
    
    type Pickup struct {
    
    	// Required. Pickup product page URI. It is only used for the review of pickup
    	// serving. This URI domain should match with the business's homepage.
    	Uri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=uri,proto3" json:"uri,omitempty"`
    	// Output only. The state of the pickup serving.
    	State ReviewState_State `protobuf:"varint,2,opt,name=state,proto3,enum=google.shopping.merchant.accounts.v1beta.ReviewState_State" json:"state,omitempty"`
    	// contains filtered or unexported fields
    }

Collection of information related to Pickup.

### func (*Pickup) Descriptor 
    
    
    func (*Pickup) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Pickup.ProtoReflect.Descriptor instead.

### func (*Pickup) GetState 
    
    
    func (x *Pickup) GetState() ReviewState_State

### func (*Pickup) GetUri 
    
    
    func (x *Pickup) GetUri() [string](https://pkg.go.dev/builtin#string)

### func (*Pickup) ProtoMessage 
    
    
    func (*Pickup) ProtoMessage()

### func (*Pickup) ProtoReflect 
    
    
    func (x *Pickup) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Pickup) Reset 
    
    
    func (x *Pickup) Reset()

### func (*Pickup) String 
    
    
    func (x *Pickup) String() [string](https://pkg.go.dev/builtin#string)

## Program
    
    
    type Program struct {
    
    	// Identifier. The resource name of the program.
    	// Format: `accounts/{account}/programs/{program}`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Output only. The URL of a Merchant Center help page describing the program.
    	DocumentationUri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=documentation_uri,json=documentationUri,proto3" json:"documentation_uri,omitempty"`
    	// Output only. The participation state of the account in the program.
    	State Program_State `protobuf:"varint,3,opt,name=state,proto3,enum=google.shopping.merchant.accounts.v1beta.Program_State" json:"state,omitempty"`
    	// Output only. The regions in which the account is actively participating in
    	// the program. Active regions are defined as those where all program
    	// requirements affecting the regions have been met.
    	//
    	// Region codes are defined by [CLDR](https://cldr.unicode.org/). This is
    	// either a country where the program applies specifically to that country or
    	// `001` when the program applies globally.
    	ActiveRegionCodes [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,rep,name=active_region_codes,json=activeRegionCodes,proto3" json:"active_region_codes,omitempty"`
    	// Output only. The requirements that the account has not yet satisfied that
    	// are affecting participation in the program.
    	UnmetRequirements []*Program_Requirement `protobuf:"bytes,5,rep,name=unmet_requirements,json=unmetRequirements,proto3" json:"unmet_requirements,omitempty"`
    	// contains filtered or unexported fields
    }

Defines participation in a given program for the specified account.

Programs provide a mechanism for adding functionality to merchant accounts. A typical example of this is the [Free product listings](https://support.google.com/merchants/topic/9240261?ref_topic=7257954,7259405,&sjid=796648681813264022-EU) program, which enables products from a merchant's store to be shown across Google for free.

### func (*Program) Descriptor 
    
    
    func (*Program) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Program.ProtoReflect.Descriptor instead.

### func (*Program) GetActiveRegionCodes 
    
    
    func (x *Program) GetActiveRegionCodes() [][string](https://pkg.go.dev/builtin#string)

### func (*Program) GetDocumentationUri 
    
    
    func (x *Program) GetDocumentationUri() [string](https://pkg.go.dev/builtin#string)

### func (*Program) GetName 
    
    
    func (x *Program) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Program) GetState 
    
    
    func (x *Program) GetState() Program_State

### func (*Program) GetUnmetRequirements 
    
    
    func (x *Program) GetUnmetRequirements() []*Program_Requirement

### func (*Program) ProtoMessage 
    
    
    func (*Program) ProtoMessage()

### func (*Program) ProtoReflect 
    
    
    func (x *Program) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Program) Reset 
    
    
    func (x *Program) Reset()

### func (*Program) String 
    
    
    func (x *Program) String() [string](https://pkg.go.dev/builtin#string)

## Program_Requirement
    
    
    type Program_Requirement struct {
    
    	// Output only. Name of the requirement.
    	Title [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=title,proto3" json:"title,omitempty"`
    	// Output only. The URL of a help page describing the requirement.
    	DocumentationUri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=documentation_uri,json=documentationUri,proto3" json:"documentation_uri,omitempty"`
    	// Output only. The regions that are currently affected by this requirement
    	// not being met.
    	//
    	// Region codes are defined by [CLDR](https://cldr.unicode.org/). This is
    	// either a country where the program applies specifically to that country
    	// or `001` when the program applies globally.
    	AffectedRegionCodes [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,rep,name=affected_region_codes,json=affectedRegionCodes,proto3" json:"affected_region_codes,omitempty"`
    	// contains filtered or unexported fields
    }

Defines a requirement specified for participation in the program.

### func (*Program_Requirement) Descriptor 
    
    
    func (*Program_Requirement) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Program_Requirement.ProtoReflect.Descriptor instead.

### func (*Program_Requirement) GetAffectedRegionCodes 
    
    
    func (x *Program_Requirement) GetAffectedRegionCodes() [][string](https://pkg.go.dev/builtin#string)

### func (*Program_Requirement) GetDocumentationUri 
    
    
    func (x *Program_Requirement) GetDocumentationUri() [string](https://pkg.go.dev/builtin#string)

### func (*Program_Requirement) GetTitle 
    
    
    func (x *Program_Requirement) GetTitle() [string](https://pkg.go.dev/builtin#string)

### func (*Program_Requirement) ProtoMessage 
    
    
    func (*Program_Requirement) ProtoMessage()

### func (*Program_Requirement) ProtoReflect 
    
    
    func (x *Program_Requirement) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Program_Requirement) Reset 
    
    
    func (x *Program_Requirement) Reset()

### func (*Program_Requirement) String 
    
    
    func (x *Program_Requirement) String() [string](https://pkg.go.dev/builtin#string)

## Program_State
    
    
    type Program_State [int32](https://pkg.go.dev/builtin#int32)

Possible program participation states for the account.

### Program_STATE_UNSPECIFIED, Program_NOT_ELIGIBLE, Program_ELIGIBLE, Program_ENABLED
    
    
    const (
    	// Default value. This value is unused.
    	Program_STATE_UNSPECIFIED Program_State = 0
    	// The account is not eligible to participate in the program.
    	Program_NOT_ELIGIBLE Program_State = 1
    	// The account is eligible to participate in the program.
    	Program_ELIGIBLE Program_State = 2
    	// The program is enabled for the account.
    	Program_ENABLED Program_State = 3
    )

### func (Program_State) Descriptor 
    
    
    func (Program_State) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Program_State) Enum 
    
    
    func (x Program_State) Enum() *Program_State

### func (Program_State) EnumDescriptor 
    
    
    func (Program_State) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Program_State.Descriptor instead.

### func (Program_State) Number 
    
    
    func (x Program_State) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Program_State) String 
    
    
    func (x Program_State) String() [string](https://pkg.go.dev/builtin#string)

### func (Program_State) Type 
    
    
    func (Program_State) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## ProgramsServiceClient
    
    
    type ProgramsServiceClient interface {
    	// Retrieves the specified program for the account.
    	GetProgram(ctx context.Context, in *GetProgramRequest, opts ...grpc.CallOption) (*Program, [error](https://pkg.go.dev/builtin#error))
    	// Retrieves all programs for the account.
    	ListPrograms(ctx context.Context, in *ListProgramsRequest, opts ...grpc.CallOption) (*ListProgramsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Enable participation in the specified program for the account. Executing
    	// this method requires admin access.
    	EnableProgram(ctx context.Context, in *EnableProgramRequest, opts ...grpc.CallOption) (*Program, [error](https://pkg.go.dev/builtin#error))
    	// Disable participation in the specified program for the account. Executing
    	// this method requires admin access.
    	DisableProgram(ctx context.Context, in *DisableProgramRequest, opts ...grpc.CallOption) (*Program, [error](https://pkg.go.dev/builtin#error))
    }

ProgramsServiceClient is the client API for ProgramsService service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

### func NewProgramsServiceClient 
    
    
    func NewProgramsServiceClient(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) ProgramsServiceClient

## ProgramsServiceServer
    
    
    type ProgramsServiceServer interface {
    	// Retrieves the specified program for the account.
    	GetProgram(context.Context, *GetProgramRequest) (*Program, [error](https://pkg.go.dev/builtin#error))
    	// Retrieves all programs for the account.
    	ListPrograms(context.Context, *ListProgramsRequest) (*ListProgramsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Enable participation in the specified program for the account. Executing
    	// this method requires admin access.
    	EnableProgram(context.Context, *EnableProgramRequest) (*Program, [error](https://pkg.go.dev/builtin#error))
    	// Disable participation in the specified program for the account. Executing
    	// this method requires admin access.
    	DisableProgram(context.Context, *DisableProgramRequest) (*Program, [error](https://pkg.go.dev/builtin#error))
    }

ProgramsServiceServer is the server API for ProgramsService service. All implementations should embed UnimplementedProgramsServiceServer for forward compatibility

## RateGroup
    
    
    type RateGroup struct {
    
    	// Required. A list of [shipping
    	// labels](https://support.google.com/merchants/answer/6324504) defining the
    	// products to which this rate group applies to. This is a disjunction: only
    	// one of the labels has to match for the rate group to apply. May only be
    	// empty for the last rate group of a service.
    	ApplicableShippingLabels [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,rep,name=applicable_shipping_labels,json=applicableShippingLabels,proto3" json:"applicable_shipping_labels,omitempty"`
    	// The value of the rate group (For example flat rate $10). Can only be set
    	// if `main_table` and `subtables` are not set.
    	SingleValue *Value `protobuf:"bytes,2,opt,name=single_value,json=singleValue,proto3,oneof" json:"single_value,omitempty"`
    	// A table defining the rate group, when `single_value` is not
    	// expressive enough. Can only be set if `single_value` is not
    	// set.
    	MainTable *Table `protobuf:"bytes,3,opt,name=main_table,json=mainTable,proto3,oneof" json:"main_table,omitempty"`
    	// Optional. A list of subtables referred to by `main_table`. Can only
    	// be set if `main_table` is set.
    	Subtables []*Table `protobuf:"bytes,4,rep,name=subtables,proto3" json:"subtables,omitempty"`
    	// Optional. A list of carrier rates that can be referred to by
    	// `main_table` or `single_value`.
    	CarrierRates []*CarrierRate `protobuf:"bytes,5,rep,name=carrier_rates,json=carrierRates,proto3" json:"carrier_rates,omitempty"`
    	// Optional. Name of the rate group.
    	// If set has to be unique within shipping service.
    	Name *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,6,opt,name=name,proto3,oneof" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Shipping rate group definitions. Only the last one is allowed to have an empty `applicable_shipping_labels`, which means "everything else". The other `applicable_shipping_labels` must not overlap.

### func (*RateGroup) Descriptor 
    
    
    func (*RateGroup) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use RateGroup.ProtoReflect.Descriptor instead.

### func (*RateGroup) GetApplicableShippingLabels 
    
    
    func (x *RateGroup) GetApplicableShippingLabels() [][string](https://pkg.go.dev/builtin#string)

### func (*RateGroup) GetCarrierRates 
    
    
    func (x *RateGroup) GetCarrierRates() []*CarrierRate

### func (*RateGroup) GetMainTable 
    
    
    func (x *RateGroup) GetMainTable() *Table

### func (*RateGroup) GetName 
    
    
    func (x *RateGroup) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*RateGroup) GetSingleValue 
    
    
    func (x *RateGroup) GetSingleValue() *Value

### func (*RateGroup) GetSubtables 
    
    
    func (x *RateGroup) GetSubtables() []*Table

### func (*RateGroup) ProtoMessage 
    
    
    func (*RateGroup) ProtoMessage()

### func (*RateGroup) ProtoReflect 
    
    
    func (x *RateGroup) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*RateGroup) Reset 
    
    
    func (x *RateGroup) Reset()

### func (*RateGroup) String 
    
    
    func (x *RateGroup) String() [string](https://pkg.go.dev/builtin#string)

## Region
    
    
    type Region struct {
    
    	// Identifier. The resource name of the region.
    	// Format: `accounts/{account}/regions/{region}`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. The display name of the region.
    	DisplayName *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=display_name,json=displayName,proto3,oneof" json:"display_name,omitempty"`
    	// Optional. A list of postal codes that defines the region area.
    	PostalCodeArea *Region_PostalCodeArea `protobuf:"bytes,3,opt,name=postal_code_area,json=postalCodeArea,proto3" json:"postal_code_area,omitempty"`
    	// Optional. A list of geotargets that defines the region area.
    	GeotargetArea *Region_GeoTargetArea `protobuf:"bytes,4,opt,name=geotarget_area,json=geotargetArea,proto3" json:"geotarget_area,omitempty"`
    	// Output only. Indicates if the region is eligible for use in the Regional
    	// Inventory configuration.
    	RegionalInventoryEligible *wrapperspb.BoolValue `protobuf:"bytes,5,opt,name=regional_inventory_eligible,json=regionalInventoryEligible,proto3" json:"regional_inventory_eligible,omitempty"`
    	// Output only. Indicates if the region is eligible for use in the Shipping
    	// Services configuration.
    	ShippingEligible *wrapperspb.BoolValue `protobuf:"bytes,6,opt,name=shipping_eligible,json=shippingEligible,proto3" json:"shipping_eligible,omitempty"`
    	// contains filtered or unexported fields
    }

Represents a geographic region that you can use as a target with both the `RegionalInventory` and `ShippingSettings` services. You can define regions as collections of either postal codes or, in some countries, using predefined geotargets. For more information, see [Set up regions ](https://support.google.com/merchants/answer/7410946#zippy=%2Ccreate-a-new-region) for more information.

### func (*Region) Descriptor 
    
    
    func (*Region) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Region.ProtoReflect.Descriptor instead.

### func (*Region) GetDisplayName 
    
    
    func (x *Region) GetDisplayName() [string](https://pkg.go.dev/builtin#string)

### func (*Region) GetGeotargetArea 
    
    
    func (x *Region) GetGeotargetArea() *Region_GeoTargetArea

### func (*Region) GetName 
    
    
    func (x *Region) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Region) GetPostalCodeArea 
    
    
    func (x *Region) GetPostalCodeArea() *Region_PostalCodeArea

### func (*Region) GetRegionalInventoryEligible 
    
    
    func (x *Region) GetRegionalInventoryEligible() *[wrapperspb](https://pkg.go.dev/google.golang.org/protobuf/types/known/wrapperspb).[BoolValue](https://pkg.go.dev/google.golang.org/protobuf/types/known/wrapperspb#BoolValue)

### func (*Region) GetShippingEligible 
    
    
    func (x *Region) GetShippingEligible() *[wrapperspb](https://pkg.go.dev/google.golang.org/protobuf/types/known/wrapperspb).[BoolValue](https://pkg.go.dev/google.golang.org/protobuf/types/known/wrapperspb#BoolValue)

### func (*Region) ProtoMessage 
    
    
    func (*Region) ProtoMessage()

### func (*Region) ProtoReflect 
    
    
    func (x *Region) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Region) Reset 
    
    
    func (x *Region) Reset()

### func (*Region) String 
    
    
    func (x *Region) String() [string](https://pkg.go.dev/builtin#string)

## Region_GeoTargetArea
    
    
    type Region_GeoTargetArea struct {
    
    	// Required. A non-empty list of [location
    	// IDs](https://developers.google.com/adwords/api/docs/appendix/geotargeting).
    	// They must all be of the same location type (for example, state).
    	GeotargetCriteriaIds [][int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,1,rep,packed,name=geotarget_criteria_ids,json=geotargetCriteriaIds,proto3" json:"geotarget_criteria_ids,omitempty"`
    	// contains filtered or unexported fields
    }

A list of geotargets that defines the region area.

### func (*Region_GeoTargetArea) Descriptor 
    
    
    func (*Region_GeoTargetArea) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Region_GeoTargetArea.ProtoReflect.Descriptor instead.

### func (*Region_GeoTargetArea) GetGeotargetCriteriaIds 
    
    
    func (x *Region_GeoTargetArea) GetGeotargetCriteriaIds() [][int64](https://pkg.go.dev/builtin#int64)

### func (*Region_GeoTargetArea) ProtoMessage 
    
    
    func (*Region_GeoTargetArea) ProtoMessage()

### func (*Region_GeoTargetArea) ProtoReflect 
    
    
    func (x *Region_GeoTargetArea) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Region_GeoTargetArea) Reset 
    
    
    func (x *Region_GeoTargetArea) Reset()

### func (*Region_GeoTargetArea) String 
    
    
    func (x *Region_GeoTargetArea) String() [string](https://pkg.go.dev/builtin#string)

## Region_PostalCodeArea
    
    
    type Region_PostalCodeArea struct {
    
    	// Required. [CLDR territory
    	// code](http://www.unicode.org/repos/cldr/tags/latest/common/main/en.xml)
    	// or the country the postal code group applies to.
    	RegionCode [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=region_code,json=regionCode,proto3" json:"region_code,omitempty"`
    	// Required. A range of postal codes.
    	PostalCodes []*Region_PostalCodeArea_PostalCodeRange `protobuf:"bytes,2,rep,name=postal_codes,json=postalCodes,proto3" json:"postal_codes,omitempty"`
    	// contains filtered or unexported fields
    }

A list of postal codes that defines the region area. Note: All regions defined using postal codes are accessible through the account's `ShippingSettings.postalCodeGroups` resource.

### func (*Region_PostalCodeArea) Descriptor 
    
    
    func (*Region_PostalCodeArea) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Region_PostalCodeArea.ProtoReflect.Descriptor instead.

### func (*Region_PostalCodeArea) GetPostalCodes 
    
    
    func (x *Region_PostalCodeArea) GetPostalCodes() []*Region_PostalCodeArea_PostalCodeRange

### func (*Region_PostalCodeArea) GetRegionCode 
    
    
    func (x *Region_PostalCodeArea) GetRegionCode() [string](https://pkg.go.dev/builtin#string)

### func (*Region_PostalCodeArea) ProtoMessage 
    
    
    func (*Region_PostalCodeArea) ProtoMessage()

### func (*Region_PostalCodeArea) ProtoReflect 
    
    
    func (x *Region_PostalCodeArea) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Region_PostalCodeArea) Reset 
    
    
    func (x *Region_PostalCodeArea) Reset()

### func (*Region_PostalCodeArea) String 
    
    
    func (x *Region_PostalCodeArea) String() [string](https://pkg.go.dev/builtin#string)

## Region_PostalCodeArea_PostalCodeRange
    
    
    type Region_PostalCodeArea_PostalCodeRange struct {
    
    	// Required. A postal code or a pattern of the form prefix* denoting the
    	// inclusive lower bound of the range defining the area. Examples values:
    	// `94108`, `9410*`, `9*`.
    	Begin [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=begin,proto3" json:"begin,omitempty"`
    	// Optional. A postal code or a pattern of the form `prefix*` denoting the
    	// inclusive upper bound of the range defining the area. It must have the
    	// same length as postalCodeRangeBegin: if postalCodeRangeBegin is a
    	// postal code then postalCodeRangeEnd must be a postal code too; if
    	// postalCodeRangeBegin is a pattern then postalCodeRangeEnd must be a
    	// pattern with the same prefix length. Optional: if not set, then the
    	// area is defined as being all the postal codes matching
    	// postalCodeRangeBegin.
    	End [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=end,proto3" json:"end,omitempty"`
    	// contains filtered or unexported fields
    }

A range of postal codes that defines the region area.

### func (*Region_PostalCodeArea_PostalCodeRange) Descriptor 
    
    
    func (*Region_PostalCodeArea_PostalCodeRange) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Region_PostalCodeArea_PostalCodeRange.ProtoReflect.Descriptor instead.

### func (*Region_PostalCodeArea_PostalCodeRange) GetBegin 
    
    
    func (x *Region_PostalCodeArea_PostalCodeRange) GetBegin() [string](https://pkg.go.dev/builtin#string)

### func (*Region_PostalCodeArea_PostalCodeRange) GetEnd 
    
    
    func (x *Region_PostalCodeArea_PostalCodeRange) GetEnd() [string](https://pkg.go.dev/builtin#string)

### func (*Region_PostalCodeArea_PostalCodeRange) ProtoMessage 
    
    
    func (*Region_PostalCodeArea_PostalCodeRange) ProtoMessage()

### func (*Region_PostalCodeArea_PostalCodeRange) ProtoReflect 
    
    
    func (x *Region_PostalCodeArea_PostalCodeRange) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Region_PostalCodeArea_PostalCodeRange) Reset 
    
    
    func (x *Region_PostalCodeArea_PostalCodeRange) Reset()

### func (*Region_PostalCodeArea_PostalCodeRange) String 
    
    
    func (x *Region_PostalCodeArea_PostalCodeRange) String() [string](https://pkg.go.dev/builtin#string)

## RegionsServiceClient
    
    
    type RegionsServiceClient interface {
    	// Retrieves a region defined in your Merchant Center account.
    	GetRegion(ctx context.Context, in *GetRegionRequest, opts ...grpc.CallOption) (*Region, [error](https://pkg.go.dev/builtin#error))
    	// Creates a region definition in your Merchant Center account. Executing this
    	// method requires admin access.
    	CreateRegion(ctx context.Context, in *CreateRegionRequest, opts ...grpc.CallOption) (*Region, [error](https://pkg.go.dev/builtin#error))
    	// Updates a region definition in your Merchant Center account. Executing this
    	// method requires admin access.
    	UpdateRegion(ctx context.Context, in *UpdateRegionRequest, opts ...grpc.CallOption) (*Region, [error](https://pkg.go.dev/builtin#error))
    	// Deletes a region definition from your Merchant Center account. Executing
    	// this method requires admin access.
    	DeleteRegion(ctx context.Context, in *DeleteRegionRequest, opts ...grpc.CallOption) (*emptypb.Empty, [error](https://pkg.go.dev/builtin#error))
    	// Lists the regions in your Merchant Center account.
    	ListRegions(ctx context.Context, in *ListRegionsRequest, opts ...grpc.CallOption) (*ListRegionsResponse, [error](https://pkg.go.dev/builtin#error))
    }

RegionsServiceClient is the client API for RegionsService service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

### func NewRegionsServiceClient 
    
    
    func NewRegionsServiceClient(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) RegionsServiceClient

## RegionsServiceServer
    
    
    type RegionsServiceServer interface {
    	// Retrieves a region defined in your Merchant Center account.
    	GetRegion(context.Context, *GetRegionRequest) (*Region, [error](https://pkg.go.dev/builtin#error))
    	// Creates a region definition in your Merchant Center account. Executing this
    	// method requires admin access.
    	CreateRegion(context.Context, *CreateRegionRequest) (*Region, [error](https://pkg.go.dev/builtin#error))
    	// Updates a region definition in your Merchant Center account. Executing this
    	// method requires admin access.
    	UpdateRegion(context.Context, *UpdateRegionRequest) (*Region, [error](https://pkg.go.dev/builtin#error))
    	// Deletes a region definition from your Merchant Center account. Executing
    	// this method requires admin access.
    	DeleteRegion(context.Context, *DeleteRegionRequest) (*emptypb.Empty, [error](https://pkg.go.dev/builtin#error))
    	// Lists the regions in your Merchant Center account.
    	ListRegions(context.Context, *ListRegionsRequest) (*ListRegionsResponse, [error](https://pkg.go.dev/builtin#error))
    }

RegionsServiceServer is the server API for RegionsService service. All implementations should embed UnimplementedRegionsServiceServer for forward compatibility

## RequestInventoryVerificationRequest
    
    
    type RequestInventoryVerificationRequest struct {
    
    	// Required. The name of the omnichannel setting to request inventory
    	// verification. Format:
    	// `accounts/{account}/omnichannelSettings/{omnichannel_setting}`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the RequestInventoryVerification method.

### func (*RequestInventoryVerificationRequest) Descriptor 
    
    
    func (*RequestInventoryVerificationRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use RequestInventoryVerificationRequest.ProtoReflect.Descriptor instead.

### func (*RequestInventoryVerificationRequest) GetName 
    
    
    func (x *RequestInventoryVerificationRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*RequestInventoryVerificationRequest) ProtoMessage 
    
    
    func (*RequestInventoryVerificationRequest) ProtoMessage()

### func (*RequestInventoryVerificationRequest) ProtoReflect 
    
    
    func (x *RequestInventoryVerificationRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*RequestInventoryVerificationRequest) Reset 
    
    
    func (x *RequestInventoryVerificationRequest) Reset()

### func (*RequestInventoryVerificationRequest) String 
    
    
    func (x *RequestInventoryVerificationRequest) String() [string](https://pkg.go.dev/builtin#string)

## RequestInventoryVerificationResponse
    
    
    type RequestInventoryVerificationResponse struct {
    
    	// The omnichannel setting that was updated.
    	OmnichannelSetting *OmnichannelSetting `protobuf:"bytes,1,opt,name=omnichannel_setting,json=omnichannelSetting,proto3" json:"omnichannel_setting,omitempty"`
    	// contains filtered or unexported fields
    }

Response message for the RequestInventoryVerification method.

### func (*RequestInventoryVerificationResponse) Descriptor 
    
    
    func (*RequestInventoryVerificationResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use RequestInventoryVerificationResponse.ProtoReflect.Descriptor instead.

### func (*RequestInventoryVerificationResponse) GetOmnichannelSetting 
    
    
    func (x *RequestInventoryVerificationResponse) GetOmnichannelSetting() *OmnichannelSetting

### func (*RequestInventoryVerificationResponse) ProtoMessage 
    
    
    func (*RequestInventoryVerificationResponse) ProtoMessage()

### func (*RequestInventoryVerificationResponse) ProtoReflect 
    
    
    func (x *RequestInventoryVerificationResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*RequestInventoryVerificationResponse) Reset 
    
    
    func (x *RequestInventoryVerificationResponse) Reset()

### func (*RequestInventoryVerificationResponse) String 
    
    
    func (x *RequestInventoryVerificationResponse) String() [string](https://pkg.go.dev/builtin#string)

## Required
    
    
    type Required struct {
    
    	// The
    	// [termsOfService](google.shopping.merchant.accounts.v1main.TermsOfService)
    	// that need to be accepted.
    	TermsOfService [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=terms_of_service,json=termsOfService,proto3" json:"terms_of_service,omitempty"`
    	// Full URL to the terms of service file. This field is the same as
    	// [TermsOfService.file_uri](TermsOfService.file_uri), it is added
    	// here for convenience only.
    	TosFileUri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=tos_file_uri,json=tosFileUri,proto3" json:"tos_file_uri,omitempty"`
    	// contains filtered or unexported fields
    }

Describes the terms of service which are required to be accepted.

### func (*Required) Descriptor 
    
    
    func (*Required) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Required.ProtoReflect.Descriptor instead.

### func (*Required) GetTermsOfService 
    
    
    func (x *Required) GetTermsOfService() [string](https://pkg.go.dev/builtin#string)

### func (*Required) GetTosFileUri 
    
    
    func (x *Required) GetTosFileUri() [string](https://pkg.go.dev/builtin#string)

### func (*Required) ProtoMessage 
    
    
    func (*Required) ProtoMessage()

### func (*Required) ProtoReflect 
    
    
    func (x *Required) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Required) Reset 
    
    
    func (x *Required) Reset()

### func (*Required) String 
    
    
    func (x *Required) String() [string](https://pkg.go.dev/builtin#string)

## RetrieveForApplicationTermsOfServiceAgreementStateRequest
    
    
    type RetrieveForApplicationTermsOfServiceAgreementStateRequest struct {
    
    	// Required. The account for which to get a TermsOfServiceAgreementState
    	// Format: `accounts/{account}`
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the `RetrieveForApplicationTermsOfServiceAgreementState` method.

### func (*RetrieveForApplicationTermsOfServiceAgreementStateRequest) Descriptor 
    
    
    func (*RetrieveForApplicationTermsOfServiceAgreementStateRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use RetrieveForApplicationTermsOfServiceAgreementStateRequest.ProtoReflect.Descriptor instead.

### func (*RetrieveForApplicationTermsOfServiceAgreementStateRequest) GetParent 
    
    
    func (x *RetrieveForApplicationTermsOfServiceAgreementStateRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*RetrieveForApplicationTermsOfServiceAgreementStateRequest) ProtoMessage 
    
    
    func (*RetrieveForApplicationTermsOfServiceAgreementStateRequest) ProtoMessage()

### func (*RetrieveForApplicationTermsOfServiceAgreementStateRequest) ProtoReflect 
    
    
    func (x *RetrieveForApplicationTermsOfServiceAgreementStateRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*RetrieveForApplicationTermsOfServiceAgreementStateRequest) Reset 
    
    
    func (x *RetrieveForApplicationTermsOfServiceAgreementStateRequest) Reset()

### func (*RetrieveForApplicationTermsOfServiceAgreementStateRequest) String 
    
    
    func (x *RetrieveForApplicationTermsOfServiceAgreementStateRequest) String() [string](https://pkg.go.dev/builtin#string)

## RetrieveLatestTermsOfServiceRequest
    
    
    type RetrieveLatestTermsOfServiceRequest struct {
    
    	// Required. Region code as defined by [CLDR](https://cldr.unicode.org/). This
    	// is either a country when the ToS applies specifically to that country or
    	// 001 when it applies globally.
    	RegionCode [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=region_code,json=regionCode,proto3" json:"region_code,omitempty"`
    	// Required. The Kind this terms of service version applies to.
    	Kind TermsOfServiceKind `protobuf:"varint,2,opt,name=kind,proto3,enum=google.shopping.merchant.accounts.v1beta.TermsOfServiceKind" json:"kind,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the `RetrieveLatestTermsOfService` method.

### func (*RetrieveLatestTermsOfServiceRequest) Descriptor 
    
    
    func (*RetrieveLatestTermsOfServiceRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use RetrieveLatestTermsOfServiceRequest.ProtoReflect.Descriptor instead.

### func (*RetrieveLatestTermsOfServiceRequest) GetKind 
    
    
    func (x *RetrieveLatestTermsOfServiceRequest) GetKind() TermsOfServiceKind

### func (*RetrieveLatestTermsOfServiceRequest) GetRegionCode 
    
    
    func (x *RetrieveLatestTermsOfServiceRequest) GetRegionCode() [string](https://pkg.go.dev/builtin#string)

### func (*RetrieveLatestTermsOfServiceRequest) ProtoMessage 
    
    
    func (*RetrieveLatestTermsOfServiceRequest) ProtoMessage()

### func (*RetrieveLatestTermsOfServiceRequest) ProtoReflect 
    
    
    func (x *RetrieveLatestTermsOfServiceRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*RetrieveLatestTermsOfServiceRequest) Reset 
    
    
    func (x *RetrieveLatestTermsOfServiceRequest) Reset()

### func (*RetrieveLatestTermsOfServiceRequest) String 
    
    
    func (x *RetrieveLatestTermsOfServiceRequest) String() [string](https://pkg.go.dev/builtin#string)

## ReviewState
    
    
    type ReviewState struct {
    	// contains filtered or unexported fields
    }

The state of a omnichannel setting related review process.

### func (*ReviewState) Descriptor 
    
    
    func (*ReviewState) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ReviewState.ProtoReflect.Descriptor instead.

### func (*ReviewState) ProtoMessage 
    
    
    func (*ReviewState) ProtoMessage()

### func (*ReviewState) ProtoReflect 
    
    
    func (x *ReviewState) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ReviewState) Reset 
    
    
    func (x *ReviewState) Reset()

### func (*ReviewState) String 
    
    
    func (x *ReviewState) String() [string](https://pkg.go.dev/builtin#string)

## ReviewState_State
    
    
    type ReviewState_State [int32](https://pkg.go.dev/builtin#int32)

The state of the review process.

### ReviewState_STATE_UNSPECIFIED, ReviewState_ACTIVE, ReviewState_FAILED, ReviewState_RUNNING, ReviewState_ACTION_REQUIRED
    
    
    const (
    	// Default value. This value is unused.
    	ReviewState_STATE_UNSPECIFIED ReviewState_State = 0
    	// The review process has concluded successfully. The reviewed item is
    	// active.
    	ReviewState_ACTIVE ReviewState_State = 1
    	// The review process failed.
    	ReviewState_FAILED ReviewState_State = 2
    	// The review process is running.
    	ReviewState_RUNNING ReviewState_State = 3
    	// The review process is waiting for the merchant to take action.
    	ReviewState_ACTION_REQUIRED ReviewState_State = 4
    )

### func (ReviewState_State) Descriptor 
    
    
    func (ReviewState_State) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (ReviewState_State) Enum 
    
    
    func (x ReviewState_State) Enum() *ReviewState_State

### func (ReviewState_State) EnumDescriptor 
    
    
    func (ReviewState_State) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ReviewState_State.Descriptor instead.

### func (ReviewState_State) Number 
    
    
    func (x ReviewState_State) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (ReviewState_State) String 
    
    
    func (x ReviewState_State) String() [string](https://pkg.go.dev/builtin#string)

### func (ReviewState_State) Type 
    
    
    func (ReviewState_State) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Row
    
    
    type Row struct {
    
    	// Required. The list of cells that constitute the row. Must have the same
    	// length as `columnHeaders` for two-dimensional tables, a length of 1 for
    	// one-dimensional tables.
    	Cells []*Value `protobuf:"bytes,1,rep,name=cells,proto3" json:"cells,omitempty"`
    	// contains filtered or unexported fields
    }

Include a list of cells.

### func (*Row) Descriptor 
    
    
    func (*Row) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Row.ProtoReflect.Descriptor instead.

### func (*Row) GetCells 
    
    
    func (x *Row) GetCells() []*Value

### func (*Row) ProtoMessage 
    
    
    func (*Row) ProtoMessage()

### func (*Row) ProtoReflect 
    
    
    func (x *Row) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Row) Reset 
    
    
    func (x *Row) Reset()

### func (*Row) String 
    
    
    func (x *Row) String() [string](https://pkg.go.dev/builtin#string)

## Service
    
    
    type Service struct {
    
    	// Required. Free-form name of the service. Must be unique within target
    	// account.
    	ServiceName *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=service_name,json=serviceName,proto3,oneof" json:"service_name,omitempty"`
    	// Required. A boolean exposing the active status of the shipping service.
    	Active *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,2,opt,name=active,proto3,oneof" json:"active,omitempty"`
    	// Required. The CLDR territory code of the countries to which the service
    	// applies.
    	DeliveryCountries [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,rep,name=delivery_countries,json=deliveryCountries,proto3" json:"delivery_countries,omitempty"`
    	// The CLDR code of the currency to which this service applies. Must match
    	// that of the prices in rate groups.
    	CurrencyCode *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=currency_code,json=currencyCode,proto3,oneof" json:"currency_code,omitempty"`
    	// Required. Time spent in various aspects from order to the delivery of the
    	// product.
    	DeliveryTime *DeliveryTime `protobuf:"bytes,5,opt,name=delivery_time,json=deliveryTime,proto3,oneof" json:"delivery_time,omitempty"`
    	// Optional. Shipping rate group definitions. Only the last one is allowed to
    	// have an empty `applicable_shipping_labels`, which means "everything else".
    	// The other `applicable_shipping_labels` must not overlap.
    	RateGroups []*RateGroup `protobuf:"bytes,6,rep,name=rate_groups,json=rateGroups,proto3" json:"rate_groups,omitempty"`
    	// Type of locations this service ships orders to.
    	ShipmentType *Service_ShipmentType `protobuf:"varint,7,opt,name=shipment_type,json=shipmentType,proto3,enum=google.shopping.merchant.accounts.v1beta.Service_ShipmentType,oneof" json:"shipment_type,omitempty"`
    	// Minimum order value for this service. If set, indicates that customers
    	// will have to spend at least this amount.
    	// All prices within a service must have the same currency.
    	// Cannot be set together with minimum_order_value_table.
    	MinimumOrderValue *typepb.Price `protobuf:"bytes,8,opt,name=minimum_order_value,json=minimumOrderValue,proto3,oneof" json:"minimum_order_value,omitempty"`
    	// Table of per store minimum order values for the pickup fulfillment type.
    	// Cannot be set together with minimum_order_value.
    	MinimumOrderValueTable *MinimumOrderValueTable `protobuf:"bytes,9,opt,name=minimum_order_value_table,json=minimumOrderValueTable,proto3,oneof" json:"minimum_order_value_table,omitempty"`
    	// A list of stores your products are delivered from.
    	// This is only valid for the local delivery shipment type.
    	StoreConfig *Service_StoreConfig `protobuf:"bytes,10,opt,name=store_config,json=storeConfig,proto3,oneof" json:"store_config,omitempty"`
    	// Optional. Loyalty programs that this shipping service is limited to.
    	LoyaltyPrograms []*Service_LoyaltyProgram `protobuf:"bytes,11,rep,name=loyalty_programs,json=loyaltyPrograms,proto3" json:"loyalty_programs,omitempty"`
    	// contains filtered or unexported fields
    }

Shipping service.

### func (*Service) Descriptor 
    
    
    func (*Service) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Service.ProtoReflect.Descriptor instead.

### func (*Service) GetActive 
    
    
    func (x *Service) GetActive() [bool](https://pkg.go.dev/builtin#bool)

### func (*Service) GetCurrencyCode 
    
    
    func (x *Service) GetCurrencyCode() [string](https://pkg.go.dev/builtin#string)

### func (*Service) GetDeliveryCountries 
    
    
    func (x *Service) GetDeliveryCountries() [][string](https://pkg.go.dev/builtin#string)

### func (*Service) GetDeliveryTime 
    
    
    func (x *Service) GetDeliveryTime() *DeliveryTime

### func (*Service) GetLoyaltyPrograms 
    
    
    func (x *Service) GetLoyaltyPrograms() []*Service_LoyaltyProgram

### func (*Service) GetMinimumOrderValue 
    
    
    func (x *Service) GetMinimumOrderValue() *[typepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/type/typepb).[Price](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/type/typepb#cloud_google_com_go_shopping_type_typepb_Price)

### func (*Service) GetMinimumOrderValueTable 
    
    
    func (x *Service) GetMinimumOrderValueTable() *MinimumOrderValueTable

### func (*Service) GetRateGroups 
    
    
    func (x *Service) GetRateGroups() []*RateGroup

### func (*Service) GetServiceName 
    
    
    func (x *Service) GetServiceName() [string](https://pkg.go.dev/builtin#string)

### func (*Service) GetShipmentType 
    
    
    func (x *Service) GetShipmentType() Service_ShipmentType

### func (*Service) GetStoreConfig 
    
    
    func (x *Service) GetStoreConfig() *Service_StoreConfig

### func (*Service) ProtoMessage 
    
    
    func (*Service) ProtoMessage()

### func (*Service) ProtoReflect 
    
    
    func (x *Service) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Service) Reset 
    
    
    func (x *Service) Reset()

### func (*Service) String 
    
    
    func (x *Service) String() [string](https://pkg.go.dev/builtin#string)

## Service_LoyaltyProgram
    
    
    type Service_LoyaltyProgram struct {
    
    	// This is the loyalty program label set in your loyalty program settings in
    	// Merchant Center. This sub-attribute allows Google to map your loyalty
    	// program to eligible offers.
    	ProgramLabel *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=program_label,json=programLabel,proto3,oneof" json:"program_label,omitempty"`
    	// Optional. Loyalty program tier of this shipping service.
    	LoyaltyProgramTiers []*Service_LoyaltyProgram_LoyaltyProgramTiers `protobuf:"bytes,2,rep,name=loyalty_program_tiers,json=loyaltyProgramTiers,proto3" json:"loyalty_program_tiers,omitempty"`
    	// contains filtered or unexported fields
    }

[Loyalty program](https://support.google.com/merchants/answer/12922446) provided by a merchant.

### func (*Service_LoyaltyProgram) Descriptor 
    
    
    func (*Service_LoyaltyProgram) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Service_LoyaltyProgram.ProtoReflect.Descriptor instead.

### func (*Service_LoyaltyProgram) GetLoyaltyProgramTiers 
    
    
    func (x *Service_LoyaltyProgram) GetLoyaltyProgramTiers() []*Service_LoyaltyProgram_LoyaltyProgramTiers

### func (*Service_LoyaltyProgram) GetProgramLabel 
    
    
    func (x *Service_LoyaltyProgram) GetProgramLabel() [string](https://pkg.go.dev/builtin#string)

### func (*Service_LoyaltyProgram) ProtoMessage 
    
    
    func (*Service_LoyaltyProgram) ProtoMessage()

### func (*Service_LoyaltyProgram) ProtoReflect 
    
    
    func (x *Service_LoyaltyProgram) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Service_LoyaltyProgram) Reset 
    
    
    func (x *Service_LoyaltyProgram) Reset()

### func (*Service_LoyaltyProgram) String 
    
    
    func (x *Service_LoyaltyProgram) String() [string](https://pkg.go.dev/builtin#string)

## Service_LoyaltyProgram_LoyaltyProgramTiers
    
    
    type Service_LoyaltyProgram_LoyaltyProgramTiers struct {
    
    	// The tier label [tier_label] sub-attribute differentiates offer level
    	// benefits between each tier. This value is also set in your program
    	// settings in Merchant Center, and is required for data source changes
    	// even if your loyalty program only has 1 tier.
    	TierLabel *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=tier_label,json=tierLabel,proto3,oneof" json:"tier_label,omitempty"`
    	// contains filtered or unexported fields
    }

Subset of a merchants loyalty program.

### func (*Service_LoyaltyProgram_LoyaltyProgramTiers) Descriptor 
    
    
    func (*Service_LoyaltyProgram_LoyaltyProgramTiers) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Service_LoyaltyProgram_LoyaltyProgramTiers.ProtoReflect.Descriptor instead.

### func (*Service_LoyaltyProgram_LoyaltyProgramTiers) GetTierLabel 
    
    
    func (x *Service_LoyaltyProgram_LoyaltyProgramTiers) GetTierLabel() [string](https://pkg.go.dev/builtin#string)

### func (*Service_LoyaltyProgram_LoyaltyProgramTiers) ProtoMessage 
    
    
    func (*Service_LoyaltyProgram_LoyaltyProgramTiers) ProtoMessage()

### func (*Service_LoyaltyProgram_LoyaltyProgramTiers) ProtoReflect 
    
    
    func (x *Service_LoyaltyProgram_LoyaltyProgramTiers) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Service_LoyaltyProgram_LoyaltyProgramTiers) Reset 
    
    
    func (x *Service_LoyaltyProgram_LoyaltyProgramTiers) Reset()

### func (*Service_LoyaltyProgram_LoyaltyProgramTiers) String 
    
    
    func (x *Service_LoyaltyProgram_LoyaltyProgramTiers) String() [string](https://pkg.go.dev/builtin#string)

## Service_ShipmentType
    
    
    type Service_ShipmentType [int32](https://pkg.go.dev/builtin#int32)

Shipment type of shipping service.

### Service_SHIPMENT_TYPE_UNSPECIFIED, Service_DELIVERY, Service_LOCAL_DELIVERY, Service_COLLECTION_POINT
    
    
    const (
    	// This service did not specify shipment type.
    	Service_SHIPMENT_TYPE_UNSPECIFIED Service_ShipmentType = 0
    	// This service ships orders to an address chosen by the customer.
    	Service_DELIVERY Service_ShipmentType = 1
    	// This service ships orders to an address chosen by the customer.
    	// The order is shipped from a local store near by.
    	Service_LOCAL_DELIVERY Service_ShipmentType = 2
    	// This service ships orders to an address chosen by the customer.
    	// The order is shipped from a collection point.
    	Service_COLLECTION_POINT Service_ShipmentType = 3
    )

### func (Service_ShipmentType) Descriptor 
    
    
    func (Service_ShipmentType) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Service_ShipmentType) Enum 
    
    
    func (x Service_ShipmentType) Enum() *Service_ShipmentType

### func (Service_ShipmentType) EnumDescriptor 
    
    
    func (Service_ShipmentType) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Service_ShipmentType.Descriptor instead.

### func (Service_ShipmentType) Number 
    
    
    func (x Service_ShipmentType) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Service_ShipmentType) String 
    
    
    func (x Service_ShipmentType) String() [string](https://pkg.go.dev/builtin#string)

### func (Service_ShipmentType) Type 
    
    
    func (Service_ShipmentType) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Service_StoreConfig
    
    
    type Service_StoreConfig struct {
    
    	// Indicates whether all stores, or selected stores, listed by this
    	// merchant provide local delivery.
    	StoreServiceType *Service_StoreConfig_StoreServiceType `protobuf:"varint,1,opt,name=store_service_type,json=storeServiceType,proto3,enum=google.shopping.merchant.accounts.v1beta.Service_StoreConfig_StoreServiceType,oneof" json:"store_service_type,omitempty"`
    	// Optional. A list of store codes that provide local delivery.
    	// If empty, then `all_stores` must be true.
    	StoreCodes [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,rep,name=store_codes,json=storeCodes,proto3" json:"store_codes,omitempty"`
    	// Configs related to local delivery ends for the day.
    	CutoffConfig *Service_StoreConfig_CutoffConfig `protobuf:"bytes,3,opt,name=cutoff_config,json=cutoffConfig,proto3,oneof" json:"cutoff_config,omitempty"`
    	// Maximum delivery radius.
    	// This is only required for the local delivery shipment type.
    	ServiceRadius *Distance `protobuf:"bytes,4,opt,name=service_radius,json=serviceRadius,proto3,oneof" json:"service_radius,omitempty"`
    	// contains filtered or unexported fields
    }

A list of stores your products are delivered from. This is only valid for the local delivery shipment type.

### func (*Service_StoreConfig) Descriptor 
    
    
    func (*Service_StoreConfig) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Service_StoreConfig.ProtoReflect.Descriptor instead.

### func (*Service_StoreConfig) GetCutoffConfig 
    
    
    func (x *Service_StoreConfig) GetCutoffConfig() *Service_StoreConfig_CutoffConfig

### func (*Service_StoreConfig) GetServiceRadius 
    
    
    func (x *Service_StoreConfig) GetServiceRadius() *Distance

### func (*Service_StoreConfig) GetStoreCodes 
    
    
    func (x *Service_StoreConfig) GetStoreCodes() [][string](https://pkg.go.dev/builtin#string)

### func (*Service_StoreConfig) GetStoreServiceType 
    
    
    func (x *Service_StoreConfig) GetStoreServiceType() Service_StoreConfig_StoreServiceType

### func (*Service_StoreConfig) ProtoMessage 
    
    
    func (*Service_StoreConfig) ProtoMessage()

### func (*Service_StoreConfig) ProtoReflect 
    
    
    func (x *Service_StoreConfig) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Service_StoreConfig) Reset 
    
    
    func (x *Service_StoreConfig) Reset()

### func (*Service_StoreConfig) String 
    
    
    func (x *Service_StoreConfig) String() [string](https://pkg.go.dev/builtin#string)

## Service_StoreConfig_CutoffConfig
    
    
    type Service_StoreConfig_CutoffConfig struct {
    
    	// Time that local delivery ends for the day.
    	LocalCutoffTime *Service_StoreConfig_CutoffConfig_LocalCutoffTime `protobuf:"bytes,1,opt,name=local_cutoff_time,json=localCutoffTime,proto3,oneof" json:"local_cutoff_time,omitempty"`
    	// Only valid with local delivery fulfillment. Represents cutoff time
    	// as the number of hours before store closing. Mutually exclusive
    	// with `local_cutoff_time`.
    	StoreCloseOffsetHours *[int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,2,opt,name=store_close_offset_hours,json=storeCloseOffsetHours,proto3,oneof" json:"store_close_offset_hours,omitempty"`
    	// Merchants can opt-out of showing n+1 day local delivery when they have
    	// a shipping service configured to n day local delivery. For example, if
    	// the shipping service defines same-day delivery, and it's past the
    	// cut-off, setting this field to `true` results in the calculated
    	// shipping service rate returning `NO_DELIVERY_POST_CUTOFF`. In the
    	// same example, setting this field to `false` results in the calculated
    	// shipping time being one day. This is only for local delivery.
    	NoDeliveryPostCutoff *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,3,opt,name=no_delivery_post_cutoff,json=noDeliveryPostCutoff,proto3,oneof" json:"no_delivery_post_cutoff,omitempty"`
    	// contains filtered or unexported fields
    }

Configs related to local delivery ends for the day.

### func (*Service_StoreConfig_CutoffConfig) Descriptor 
    
    
    func (*Service_StoreConfig_CutoffConfig) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Service_StoreConfig_CutoffConfig.ProtoReflect.Descriptor instead.

### func (*Service_StoreConfig_CutoffConfig) GetLocalCutoffTime 
    
    
    func (x *Service_StoreConfig_CutoffConfig) GetLocalCutoffTime() *Service_StoreConfig_CutoffConfig_LocalCutoffTime

### func (*Service_StoreConfig_CutoffConfig) GetNoDeliveryPostCutoff 
    
    
    func (x *Service_StoreConfig_CutoffConfig) GetNoDeliveryPostCutoff() [bool](https://pkg.go.dev/builtin#bool)

### func (*Service_StoreConfig_CutoffConfig) GetStoreCloseOffsetHours 
    
    
    func (x *Service_StoreConfig_CutoffConfig) GetStoreCloseOffsetHours() [int64](https://pkg.go.dev/builtin#int64)

### func (*Service_StoreConfig_CutoffConfig) ProtoMessage 
    
    
    func (*Service_StoreConfig_CutoffConfig) ProtoMessage()

### func (*Service_StoreConfig_CutoffConfig) ProtoReflect 
    
    
    func (x *Service_StoreConfig_CutoffConfig) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Service_StoreConfig_CutoffConfig) Reset 
    
    
    func (x *Service_StoreConfig_CutoffConfig) Reset()

### func (*Service_StoreConfig_CutoffConfig) String 
    
    
    func (x *Service_StoreConfig_CutoffConfig) String() [string](https://pkg.go.dev/builtin#string)

## Service_StoreConfig_CutoffConfig_LocalCutoffTime
    
    
    type Service_StoreConfig_CutoffConfig_LocalCutoffTime struct {
    
    	// Hour local delivery orders must be placed by to process the same
    	// day.
    	Hour *[int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,1,opt,name=hour,proto3,oneof" json:"hour,omitempty"`
    	// Minute local delivery orders must be placed by to process the same
    	// day.
    	Minute *[int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,2,opt,name=minute,proto3,oneof" json:"minute,omitempty"`
    	// contains filtered or unexported fields
    }

Time that local delivery ends for the day.

### func (*Service_StoreConfig_CutoffConfig_LocalCutoffTime) Descriptor 
    
    
    func (*Service_StoreConfig_CutoffConfig_LocalCutoffTime) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Service_StoreConfig_CutoffConfig_LocalCutoffTime.ProtoReflect.Descriptor instead.

### func (*Service_StoreConfig_CutoffConfig_LocalCutoffTime) GetHour 
    
    
    func (x *Service_StoreConfig_CutoffConfig_LocalCutoffTime) GetHour() [int64](https://pkg.go.dev/builtin#int64)

### func (*Service_StoreConfig_CutoffConfig_LocalCutoffTime) GetMinute 
    
    
    func (x *Service_StoreConfig_CutoffConfig_LocalCutoffTime) GetMinute() [int64](https://pkg.go.dev/builtin#int64)

### func (*Service_StoreConfig_CutoffConfig_LocalCutoffTime) ProtoMessage 
    
    
    func (*Service_StoreConfig_CutoffConfig_LocalCutoffTime) ProtoMessage()

### func (*Service_StoreConfig_CutoffConfig_LocalCutoffTime) ProtoReflect 
    
    
    func (x *Service_StoreConfig_CutoffConfig_LocalCutoffTime) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Service_StoreConfig_CutoffConfig_LocalCutoffTime) Reset 
    
    
    func (x *Service_StoreConfig_CutoffConfig_LocalCutoffTime) Reset()

### func (*Service_StoreConfig_CutoffConfig_LocalCutoffTime) String 
    
    
    func (x *Service_StoreConfig_CutoffConfig_LocalCutoffTime) String() [string](https://pkg.go.dev/builtin#string)

## Service_StoreConfig_StoreServiceType
    
    
    type Service_StoreConfig_StoreServiceType [int32](https://pkg.go.dev/builtin#int32)

Indicates whether all stores, or selected stores, listed by the merchant provide local delivery.

### Service_StoreConfig_STORE_SERVICE_TYPE_UNSPECIFIED, Service_StoreConfig_ALL_STORES, Service_StoreConfig_SELECTED_STORES
    
    
    const (
    	// Did not specify store service type.
    	Service_StoreConfig_STORE_SERVICE_TYPE_UNSPECIFIED Service_StoreConfig_StoreServiceType = 0
    	// Indicates whether all stores, current and future, listed by this
    	// merchant provide local delivery.
    	Service_StoreConfig_ALL_STORES Service_StoreConfig_StoreServiceType = 1
    	// Indicates that only the stores listed in `store_codes` are eligible
    	// for local delivery.
    	Service_StoreConfig_SELECTED_STORES Service_StoreConfig_StoreServiceType = 2
    )

### func (Service_StoreConfig_StoreServiceType) Descriptor 
    
    
    func (Service_StoreConfig_StoreServiceType) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Service_StoreConfig_StoreServiceType) Enum 
    
    
    func (x Service_StoreConfig_StoreServiceType) Enum() *Service_StoreConfig_StoreServiceType

### func (Service_StoreConfig_StoreServiceType) EnumDescriptor 
    
    
    func (Service_StoreConfig_StoreServiceType) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Service_StoreConfig_StoreServiceType.Descriptor instead.

### func (Service_StoreConfig_StoreServiceType) Number 
    
    
    func (x Service_StoreConfig_StoreServiceType) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Service_StoreConfig_StoreServiceType) String 
    
    
    func (x Service_StoreConfig_StoreServiceType) String() [string](https://pkg.go.dev/builtin#string)

### func (Service_StoreConfig_StoreServiceType) Type 
    
    
    func (Service_StoreConfig_StoreServiceType) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## ShippingSettings
    
    
    type ShippingSettings struct {
    
    	// Identifier. The resource name of the shipping setting.
    	// Format: `accounts/{account}/shippingSetting`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. The target account's list of services.
    	Services []*Service `protobuf:"bytes,2,rep,name=services,proto3" json:"services,omitempty"`
    	// Optional. A list of warehouses which can be referred to in `services`.
    	Warehouses []*Warehouse `protobuf:"bytes,3,rep,name=warehouses,proto3" json:"warehouses,omitempty"`
    	// Required. This field is used for avoid async issue. Make sure shipping
    	// setting data
    	//
    	//	didn't change between get call and insert call. The user should do
    	//	following steps：
    	//
    	// 1. Set etag field as empty string for initial shipping setting creation.
    	//
    	// 2. After initial creation, call get method to obtain an etag and current
    	// shipping setting data before call insert.
    	//
    	// 3. Modify to wanted shipping setting information.
    	//
    	// 4. Call insert method with the wanted shipping setting information with
    	// the etag obtained from step 2.
    	//
    	// 5. If shipping setting data changed between step 2 and step 4. Insert
    	// request will fail because the etag changes every time the shipping setting
    	// data changes. User should repeate step 2-4 with the new etag.
    	Etag [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=etag,proto3" json:"etag,omitempty"`
    	// contains filtered or unexported fields
    }

The merchant account's [shipping setting](https://support.google.com/merchants/answer/6069284).

### func (*ShippingSettings) Descriptor 
    
    
    func (*ShippingSettings) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ShippingSettings.ProtoReflect.Descriptor instead.

### func (*ShippingSettings) GetEtag 
    
    
    func (x *ShippingSettings) GetEtag() [string](https://pkg.go.dev/builtin#string)

### func (*ShippingSettings) GetName 
    
    
    func (x *ShippingSettings) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*ShippingSettings) GetServices 
    
    
    func (x *ShippingSettings) GetServices() []*Service

### func (*ShippingSettings) GetWarehouses 
    
    
    func (x *ShippingSettings) GetWarehouses() []*Warehouse

### func (*ShippingSettings) ProtoMessage 
    
    
    func (*ShippingSettings) ProtoMessage()

### func (*ShippingSettings) ProtoReflect 
    
    
    func (x *ShippingSettings) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ShippingSettings) Reset 
    
    
    func (x *ShippingSettings) Reset()

### func (*ShippingSettings) String 
    
    
    func (x *ShippingSettings) String() [string](https://pkg.go.dev/builtin#string)

## ShippingSettingsServiceClient
    
    
    type ShippingSettingsServiceClient interface {
    	// Retrieve shipping setting information.
    	GetShippingSettings(ctx context.Context, in *GetShippingSettingsRequest, opts ...grpc.CallOption) (*ShippingSettings, [error](https://pkg.go.dev/builtin#error))
    	// Replace the shipping setting of a merchant with the request shipping
    	// setting. Executing this method requires admin access.
    	InsertShippingSettings(ctx context.Context, in *InsertShippingSettingsRequest, opts ...grpc.CallOption) (*ShippingSettings, [error](https://pkg.go.dev/builtin#error))
    }

ShippingSettingsServiceClient is the client API for ShippingSettingsService service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

### func NewShippingSettingsServiceClient 
    
    
    func NewShippingSettingsServiceClient(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) ShippingSettingsServiceClient

## ShippingSettingsServiceServer
    
    
    type ShippingSettingsServiceServer interface {
    	// Retrieve shipping setting information.
    	GetShippingSettings(context.Context, *GetShippingSettingsRequest) (*ShippingSettings, [error](https://pkg.go.dev/builtin#error))
    	// Replace the shipping setting of a merchant with the request shipping
    	// setting. Executing this method requires admin access.
    	InsertShippingSettings(context.Context, *InsertShippingSettingsRequest) (*ShippingSettings, [error](https://pkg.go.dev/builtin#error))
    }

ShippingSettingsServiceServer is the server API for ShippingSettingsService service. All implementations should embed UnimplementedShippingSettingsServiceServer for forward compatibility

## Table
    
    
    type Table struct {
    
    	// Name of the table. Required for subtables, ignored for the main table.
    	Name *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3,oneof" json:"name,omitempty"`
    	// Required. Headers of the table's rows.
    	RowHeaders *Headers `protobuf:"bytes,2,opt,name=row_headers,json=rowHeaders,proto3,oneof" json:"row_headers,omitempty"`
    	// Headers of the table's columns. Optional: if not set then the table has
    	// only one dimension.
    	ColumnHeaders *Headers `protobuf:"bytes,3,opt,name=column_headers,json=columnHeaders,proto3,oneof" json:"column_headers,omitempty"`
    	// Required. The list of rows that constitute the table. Must have the same
    	// length as `row_headers`.
    	Rows []*Row `protobuf:"bytes,4,rep,name=rows,proto3" json:"rows,omitempty"`
    	// contains filtered or unexported fields
    }

A table defining the rate group, when `single_value` is not expressive enough.

### func (*Table) Descriptor 
    
    
    func (*Table) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Table.ProtoReflect.Descriptor instead.

### func (*Table) GetColumnHeaders 
    
    
    func (x *Table) GetColumnHeaders() *Headers

### func (*Table) GetName 
    
    
    func (x *Table) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Table) GetRowHeaders 
    
    
    func (x *Table) GetRowHeaders() *Headers

### func (*Table) GetRows 
    
    
    func (x *Table) GetRows() []*Row

### func (*Table) ProtoMessage 
    
    
    func (*Table) ProtoMessage()

### func (*Table) ProtoReflect 
    
    
    func (x *Table) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Table) Reset 
    
    
    func (x *Table) Reset()

### func (*Table) String 
    
    
    func (x *Table) String() [string](https://pkg.go.dev/builtin#string)

## TaxRule
    
    
    type TaxRule struct {
    
    	// Describe the location through either postal code range or a criteria id.
    	//
    	// Types that are valid to be assigned to Location:
    	//
    	//	*TaxRule_LocationId
    	//	*TaxRule_PostCodeRange
    	Location isTaxRule_Location `protobuf_oneof:"location"`
    	// What is the way to calculate tax rate for deliveries to this admin's area.
    	// Can only be set on US states.
    	//
    	// Types that are valid to be assigned to RateCalculation:
    	//
    	//	*TaxRule_UseGoogleRate
    	//	*TaxRule_SelfSpecifiedRateMicros
    	RateCalculation isTaxRule_RateCalculation `protobuf_oneof:"rate_calculation"`
    	// Region code in which this rule is applicable
    	RegionCode [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=region_code,json=regionCode,proto3" json:"region_code,omitempty"`
    	// If set, shipping charge is taxed (at the same rate as product) when
    	// delivering to this admin's area.
    	// Can only be set on US states without category.
    	ShippingTaxed [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,6,opt,name=shipping_taxed,json=shippingTaxed,proto3" json:"shipping_taxed,omitempty"`
    	// Required. Time period when this rule is effective. If the duration is
    	// missing from effective_time listed, then it is open ended to the future.
    	// The start of this time period is inclusive, and the end is exclusive.
    	EffectiveTimePeriod *interval.Interval `protobuf:"bytes,7,opt,name=effective_time_period,json=effectiveTimePeriod,proto3" json:"effective_time_period,omitempty"`
    	// contains filtered or unexported fields
    }

Primary type convension

percent micro : 100% = 1 000 000 and 1% = 10 000
    
    
    cannot be negative.
    

Information about tax nexus and related parameters applicable to orders delivered to the area covered by a single tax admin. Nexus is created when a merchant is doing business in an area administered by tax admin (only US states are supported for nexus configuration). If merchant has nexus in a US state, merchant needs to pay tax to all tax authorities associated with the shipping destination. Next Id : 8

### func (*TaxRule) Descriptor 
    
    
    func (*TaxRule) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use TaxRule.ProtoReflect.Descriptor instead.

### func (*TaxRule) GetEffectiveTimePeriod 
    
    
    func (x *TaxRule) GetEffectiveTimePeriod() *[interval](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/interval).[Interval](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/interval#Interval)

### func (*TaxRule) GetLocation 
    
    
    func (x *TaxRule) GetLocation() isTaxRule_Location

### func (*TaxRule) GetLocationId 
    
    
    func (x *TaxRule) GetLocationId() [int64](https://pkg.go.dev/builtin#int64)

### func (*TaxRule) GetPostCodeRange 
    
    
    func (x *TaxRule) GetPostCodeRange() *TaxRule_TaxPostalCodeRange

### func (*TaxRule) GetRateCalculation 
    
    
    func (x *TaxRule) GetRateCalculation() isTaxRule_RateCalculation

### func (*TaxRule) GetRegionCode 
    
    
    func (x *TaxRule) GetRegionCode() [string](https://pkg.go.dev/builtin#string)

### func (*TaxRule) GetSelfSpecifiedRateMicros 
    
    
    func (x *TaxRule) GetSelfSpecifiedRateMicros() [int64](https://pkg.go.dev/builtin#int64)

### func (*TaxRule) GetShippingTaxed 
    
    
    func (x *TaxRule) GetShippingTaxed() [bool](https://pkg.go.dev/builtin#bool)

### func (*TaxRule) GetUseGoogleRate 
    
    
    func (x *TaxRule) GetUseGoogleRate() [bool](https://pkg.go.dev/builtin#bool)

### func (*TaxRule) ProtoMessage 
    
    
    func (*TaxRule) ProtoMessage()

### func (*TaxRule) ProtoReflect 
    
    
    func (x *TaxRule) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*TaxRule) Reset 
    
    
    func (x *TaxRule) Reset()

### func (*TaxRule) String 
    
    
    func (x *TaxRule) String() [string](https://pkg.go.dev/builtin#string)

## TaxRule_LocationId
    
    
    type TaxRule_LocationId struct {
    	// The admin_id or criteria_id of the region in which this rule is
    	// applicable.
    	LocationId [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,2,opt,name=location_id,json=locationId,proto3,oneof"`
    }

## TaxRule_PostCodeRange
    
    
    type TaxRule_PostCodeRange struct {
    	// The range of postal codes in which this rule is applicable.
    	PostCodeRange *TaxRule_TaxPostalCodeRange `protobuf:"bytes,3,opt,name=post_code_range,json=postCodeRange,proto3,oneof"`
    }

## TaxRule_SelfSpecifiedRateMicros
    
    
    type TaxRule_SelfSpecifiedRateMicros struct {
    	// A fixed rate specified in micros, where 100% = 1_000_000.
    	// Suitable for origin-based states.
    	SelfSpecifiedRateMicros [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,5,opt,name=self_specified_rate_micros,json=selfSpecifiedRateMicros,proto3,oneof"`
    }

## TaxRule_TaxPostalCodeRange
    
    
    type TaxRule_TaxPostalCodeRange struct {
    
    	// Required. The start of the postal code range, which is also the smallest
    	// in the range.
    	Start [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=start,proto3" json:"start,omitempty"`
    	// The end of the postal code range. Will be the same as start if not
    	// specified.
    	End [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=end,proto3" json:"end,omitempty"`
    	// contains filtered or unexported fields
    }

A range of postal codes that defines the area.

### func (*TaxRule_TaxPostalCodeRange) Descriptor 
    
    
    func (*TaxRule_TaxPostalCodeRange) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use TaxRule_TaxPostalCodeRange.ProtoReflect.Descriptor instead.

### func (*TaxRule_TaxPostalCodeRange) GetEnd 
    
    
    func (x *TaxRule_TaxPostalCodeRange) GetEnd() [string](https://pkg.go.dev/builtin#string)

### func (*TaxRule_TaxPostalCodeRange) GetStart 
    
    
    func (x *TaxRule_TaxPostalCodeRange) GetStart() [string](https://pkg.go.dev/builtin#string)

### func (*TaxRule_TaxPostalCodeRange) ProtoMessage 
    
    
    func (*TaxRule_TaxPostalCodeRange) ProtoMessage()

### func (*TaxRule_TaxPostalCodeRange) ProtoReflect 
    
    
    func (x *TaxRule_TaxPostalCodeRange) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*TaxRule_TaxPostalCodeRange) Reset 
    
    
    func (x *TaxRule_TaxPostalCodeRange) Reset()

### func (*TaxRule_TaxPostalCodeRange) String 
    
    
    func (x *TaxRule_TaxPostalCodeRange) String() [string](https://pkg.go.dev/builtin#string)

## TaxRule_UseGoogleRate
    
    
    type TaxRule_UseGoogleRate struct {
    	// Rate that depends on delivery location: if merchant has a nexus in
    	// corresponding US state, rates from authorities with jurisdiction over
    	// delivery area are added up.
    	UseGoogleRate [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,4,opt,name=use_google_rate,json=useGoogleRate,proto3,oneof"`
    }

## TermsOfService
    
    
    type TermsOfService struct {
    
    	// Identifier. The resource name of the terms of service version.
    	// Format: `termsOfService/{version}`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Region code as defined by [CLDR](https://cldr.unicode.org/). This is either
    	// a country where the ToS applies specifically to that country or `001` when
    	// the same `TermsOfService` can be signed in any country. However note that
    	// when signing a ToS that applies globally we still expect that a specific
    	// country is provided  (this should be merchant business country or program
    	// country of participation).
    	RegionCode [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=region_code,json=regionCode,proto3" json:"region_code,omitempty"`
    	// The Kind this terms of service version applies to.
    	Kind TermsOfServiceKind `protobuf:"varint,3,opt,name=kind,proto3,enum=google.shopping.merchant.accounts.v1beta.TermsOfServiceKind" json:"kind,omitempty"`
    	// URI for terms of service file that needs to be displayed to signing users.
    	FileUri *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=file_uri,json=fileUri,proto3,oneof" json:"file_uri,omitempty"`
    	// Whether this terms of service version is external. External terms of
    	// service versions can only be agreed through external processes and not
    	// directly by the merchant through UI or API.
    	External [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,5,opt,name=external,proto3" json:"external,omitempty"`
    	// contains filtered or unexported fields
    }

A `TermsOfService`.

### func (*TermsOfService) Descriptor 
    
    
    func (*TermsOfService) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use TermsOfService.ProtoReflect.Descriptor instead.

### func (*TermsOfService) GetExternal 
    
    
    func (x *TermsOfService) GetExternal() [bool](https://pkg.go.dev/builtin#bool)

### func (*TermsOfService) GetFileUri 
    
    
    func (x *TermsOfService) GetFileUri() [string](https://pkg.go.dev/builtin#string)

### func (*TermsOfService) GetKind 
    
    
    func (x *TermsOfService) GetKind() TermsOfServiceKind

### func (*TermsOfService) GetName 
    
    
    func (x *TermsOfService) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*TermsOfService) GetRegionCode 
    
    
    func (x *TermsOfService) GetRegionCode() [string](https://pkg.go.dev/builtin#string)

### func (*TermsOfService) ProtoMessage 
    
    
    func (*TermsOfService) ProtoMessage()

### func (*TermsOfService) ProtoReflect 
    
    
    func (x *TermsOfService) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*TermsOfService) Reset 
    
    
    func (x *TermsOfService) Reset()

### func (*TermsOfService) String 
    
    
    func (x *TermsOfService) String() [string](https://pkg.go.dev/builtin#string)

## TermsOfServiceAgreementState
    
    
    type TermsOfServiceAgreementState struct {
    
    	// Identifier. The resource name of the terms of service version.
    	// Format: `accounts/{account}/termsOfServiceAgreementState/{identifier}`
    	// The identifier format is: `{TermsOfServiceKind}-{country}`
    	// For example, an identifier could be: `MERCHANT_CENTER-US`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Region code as defined by https://cldr.unicode.org/. This is the
    	// country the current state applies to.
    	RegionCode [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=region_code,json=regionCode,proto3" json:"region_code,omitempty"`
    	// Terms of Service kind associated with the particular version.
    	TermsOfServiceKind TermsOfServiceKind `protobuf:"varint,3,opt,name=terms_of_service_kind,json=termsOfServiceKind,proto3,enum=google.shopping.merchant.accounts.v1beta.TermsOfServiceKind" json:"terms_of_service_kind,omitempty"`
    	// The accepted terms of service of this kind and for the associated
    	// region_code
    	Accepted *Accepted `protobuf:"bytes,4,opt,name=accepted,proto3,oneof" json:"accepted,omitempty"`
    	// The required terms of service
    	Required *Required `protobuf:"bytes,5,opt,name=required,proto3,oneof" json:"required,omitempty"`
    	// contains filtered or unexported fields
    }

This resource represents the agreement state for a given account and terms of service kind. The state is as follows:

  * If the merchant has accepted a terms of service: [accepted](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/merchant/accounts/apiv1beta/TermsOfServiceAggrementState.accepted) will be populated, otherwise it will be empty
  * If the merchant must sign a terms of service: [required](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/merchant/accounts/apiv1beta/TermsOfServiceAggrementState.required) will be populated, otherwise it will be empty.



Note that both [required](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/merchant/accounts/apiv1beta/TermsOfServiceAggrementState.required) and [accepted](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/merchant/accounts/apiv1beta/TermsOfServiceAggrementState.accepted) can be present. In this case the `accepted` terms of services will have an expiration date set in the [valid_until](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/merchant/accounts/apiv1beta/Accepted.valid_until) field. The `required` terms of services need to be accepted before `valid_until` in order for the account to continue having a valid agreement. When accepting new terms of services we expect 3Ps to display the text associated with the given terms of service agreement (the url to the file containing the text is added in the Required message below as [tos_file_uri](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/merchant/accounts/apiv1beta/Accepted.tos_file_uri). The actual acceptance of the terms of service is done by calling accept on the [TermsOfService](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/merchant/accounts/apiv1beta/TermsOfService) resource.

### func (*TermsOfServiceAgreementState) Descriptor 
    
    
    func (*TermsOfServiceAgreementState) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use TermsOfServiceAgreementState.ProtoReflect.Descriptor instead.

### func (*TermsOfServiceAgreementState) GetAccepted 
    
    
    func (x *TermsOfServiceAgreementState) GetAccepted() *Accepted

### func (*TermsOfServiceAgreementState) GetName 
    
    
    func (x *TermsOfServiceAgreementState) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*TermsOfServiceAgreementState) GetRegionCode 
    
    
    func (x *TermsOfServiceAgreementState) GetRegionCode() [string](https://pkg.go.dev/builtin#string)

### func (*TermsOfServiceAgreementState) GetRequired 
    
    
    func (x *TermsOfServiceAgreementState) GetRequired() *Required

### func (*TermsOfServiceAgreementState) GetTermsOfServiceKind 
    
    
    func (x *TermsOfServiceAgreementState) GetTermsOfServiceKind() TermsOfServiceKind

### func (*TermsOfServiceAgreementState) ProtoMessage 
    
    
    func (*TermsOfServiceAgreementState) ProtoMessage()

### func (*TermsOfServiceAgreementState) ProtoReflect 
    
    
    func (x *TermsOfServiceAgreementState) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*TermsOfServiceAgreementState) Reset 
    
    
    func (x *TermsOfServiceAgreementState) Reset()

### func (*TermsOfServiceAgreementState) String 
    
    
    func (x *TermsOfServiceAgreementState) String() [string](https://pkg.go.dev/builtin#string)

## TermsOfServiceAgreementStateServiceClient
    
    
    type TermsOfServiceAgreementStateServiceClient interface {
    	// Returns the state of a terms of service agreement.
    	GetTermsOfServiceAgreementState(ctx context.Context, in *GetTermsOfServiceAgreementStateRequest, opts ...grpc.CallOption) (*TermsOfServiceAgreementState, [error](https://pkg.go.dev/builtin#error))
    	// Retrieves the state of the agreement for the application terms of service.
    	RetrieveForApplicationTermsOfServiceAgreementState(ctx context.Context, in *RetrieveForApplicationTermsOfServiceAgreementStateRequest, opts ...grpc.CallOption) (*TermsOfServiceAgreementState, [error](https://pkg.go.dev/builtin#error))
    }

TermsOfServiceAgreementStateServiceClient is the client API for TermsOfServiceAgreementStateService service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

### func NewTermsOfServiceAgreementStateServiceClient 
    
    
    func NewTermsOfServiceAgreementStateServiceClient(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) TermsOfServiceAgreementStateServiceClient

## TermsOfServiceAgreementStateServiceServer
    
    
    type TermsOfServiceAgreementStateServiceServer interface {
    	// Returns the state of a terms of service agreement.
    	GetTermsOfServiceAgreementState(context.Context, *GetTermsOfServiceAgreementStateRequest) (*TermsOfServiceAgreementState, [error](https://pkg.go.dev/builtin#error))
    	// Retrieves the state of the agreement for the application terms of service.
    	RetrieveForApplicationTermsOfServiceAgreementState(context.Context, *RetrieveForApplicationTermsOfServiceAgreementStateRequest) (*TermsOfServiceAgreementState, [error](https://pkg.go.dev/builtin#error))
    }

TermsOfServiceAgreementStateServiceServer is the server API for TermsOfServiceAgreementStateService service. All implementations should embed UnimplementedTermsOfServiceAgreementStateServiceServer for forward compatibility

## TermsOfServiceKind
    
    
    type TermsOfServiceKind [int32](https://pkg.go.dev/builtin#int32)

The TermsOfService Kind.

### TermsOfServiceKind_TERMS_OF_SERVICE_KIND_UNSPECIFIED, TermsOfServiceKind_MERCHANT_CENTER
    
    
    const (
    	// Default value. This value is unused.
    	TermsOfServiceKind_TERMS_OF_SERVICE_KIND_UNSPECIFIED TermsOfServiceKind = 0
    	// Merchant Center application.
    	TermsOfServiceKind_MERCHANT_CENTER TermsOfServiceKind = 1
    )

### func (TermsOfServiceKind) Descriptor 
    
    
    func (TermsOfServiceKind) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (TermsOfServiceKind) Enum 
    
    
    func (x TermsOfServiceKind) Enum() *TermsOfServiceKind

### func (TermsOfServiceKind) EnumDescriptor 
    
    
    func (TermsOfServiceKind) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use TermsOfServiceKind.Descriptor instead.

### func (TermsOfServiceKind) Number 
    
    
    func (x TermsOfServiceKind) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (TermsOfServiceKind) String 
    
    
    func (x TermsOfServiceKind) String() [string](https://pkg.go.dev/builtin#string)

### func (TermsOfServiceKind) Type 
    
    
    func (TermsOfServiceKind) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## TermsOfServiceServiceClient
    
    
    type TermsOfServiceServiceClient interface {
    	// Retrieves the `TermsOfService` associated with the provided version.
    	GetTermsOfService(ctx context.Context, in *GetTermsOfServiceRequest, opts ...grpc.CallOption) (*TermsOfService, [error](https://pkg.go.dev/builtin#error))
    	// Retrieves the latest version of the `TermsOfService` for a given `kind` and
    	// `region_code`.
    	RetrieveLatestTermsOfService(ctx context.Context, in *RetrieveLatestTermsOfServiceRequest, opts ...grpc.CallOption) (*TermsOfService, [error](https://pkg.go.dev/builtin#error))
    	// Accepts a `TermsOfService`. Executing this method requires admin access.
    	AcceptTermsOfService(ctx context.Context, in *AcceptTermsOfServiceRequest, opts ...grpc.CallOption) (*emptypb.Empty, [error](https://pkg.go.dev/builtin#error))
    }

TermsOfServiceServiceClient is the client API for TermsOfServiceService service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

### func NewTermsOfServiceServiceClient 
    
    
    func NewTermsOfServiceServiceClient(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) TermsOfServiceServiceClient

## TermsOfServiceServiceServer
    
    
    type TermsOfServiceServiceServer interface {
    	// Retrieves the `TermsOfService` associated with the provided version.
    	GetTermsOfService(context.Context, *GetTermsOfServiceRequest) (*TermsOfService, [error](https://pkg.go.dev/builtin#error))
    	// Retrieves the latest version of the `TermsOfService` for a given `kind` and
    	// `region_code`.
    	RetrieveLatestTermsOfService(context.Context, *RetrieveLatestTermsOfServiceRequest) (*TermsOfService, [error](https://pkg.go.dev/builtin#error))
    	// Accepts a `TermsOfService`. Executing this method requires admin access.
    	AcceptTermsOfService(context.Context, *AcceptTermsOfServiceRequest) (*emptypb.Empty, [error](https://pkg.go.dev/builtin#error))
    }

TermsOfServiceServiceServer is the server API for TermsOfServiceService service. All implementations should embed UnimplementedTermsOfServiceServiceServer for forward compatibility

## TransitTable
    
    
    type TransitTable struct {
    
    	// Required. A list of region names
    	// [Region.name][google.shopping.merchant.accounts.v1beta.Region.name] . The
    	// last value can be
    	// `"all other locations"`. Example:
    	// `["zone 1", "zone 2", "all other locations"]`. The referred
    	// postal code groups must match the delivery country of the service.
    	PostalCodeGroupNames [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,rep,name=postal_code_group_names,json=postalCodeGroupNames,proto3" json:"postal_code_group_names,omitempty"`
    	// Required. A list of transit time labels. The last value can be
    	// `"all other labels"`. Example:
    	// `["food", "electronics", "all other labels"]`.
    	TransitTimeLabels [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,rep,name=transit_time_labels,json=transitTimeLabels,proto3" json:"transit_time_labels,omitempty"`
    	// Required. If there's only one dimension set of `postal_code_group_names` or
    	// `transit_time_labels`, there are multiple rows each with one value
    	// for that dimension. If there are two dimensions, each row corresponds to a
    	// `postal_code_group_names`, and columns (values) to a
    	// `transit_time_labels`.
    	Rows []*TransitTable_TransitTimeRow `protobuf:"bytes,3,rep,name=rows,proto3" json:"rows,omitempty"`
    	// contains filtered or unexported fields
    }

Transit time table, number of business days spent in transit based on row and column dimensions. Either `min_transit_days`, `max_transit_days` or `transit_time_table` can be set, but not both.

### func (*TransitTable) Descriptor 
    
    
    func (*TransitTable) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use TransitTable.ProtoReflect.Descriptor instead.

### func (*TransitTable) GetPostalCodeGroupNames 
    
    
    func (x *TransitTable) GetPostalCodeGroupNames() [][string](https://pkg.go.dev/builtin#string)

### func (*TransitTable) GetRows 
    
    
    func (x *TransitTable) GetRows() []*TransitTable_TransitTimeRow

### func (*TransitTable) GetTransitTimeLabels 
    
    
    func (x *TransitTable) GetTransitTimeLabels() [][string](https://pkg.go.dev/builtin#string)

### func (*TransitTable) ProtoMessage 
    
    
    func (*TransitTable) ProtoMessage()

### func (*TransitTable) ProtoReflect 
    
    
    func (x *TransitTable) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*TransitTable) Reset 
    
    
    func (x *TransitTable) Reset()

### func (*TransitTable) String 
    
    
    func (x *TransitTable) String() [string](https://pkg.go.dev/builtin#string)

## TransitTable_TransitTimeRow
    
    
    type TransitTable_TransitTimeRow struct {
    
    	// Required. Transit time range (min-max) in business days.
    	Values []*TransitTable_TransitTimeRow_TransitTimeValue `protobuf:"bytes,1,rep,name=values,proto3" json:"values,omitempty"`
    	// contains filtered or unexported fields
    }

If there's only one dimension set of `postal_code_group_names` or `transit_time_labels`, there are multiple rows each with one value for that dimension. If there are two dimensions, each row corresponds to a `postal_code_group_names`, and columns (values) to a `transit_time_labels`.

### func (*TransitTable_TransitTimeRow) Descriptor 
    
    
    func (*TransitTable_TransitTimeRow) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use TransitTable_TransitTimeRow.ProtoReflect.Descriptor instead.

### func (*TransitTable_TransitTimeRow) GetValues 
    
    
    func (x *TransitTable_TransitTimeRow) GetValues() []*TransitTable_TransitTimeRow_TransitTimeValue

### func (*TransitTable_TransitTimeRow) ProtoMessage 
    
    
    func (*TransitTable_TransitTimeRow) ProtoMessage()

### func (*TransitTable_TransitTimeRow) ProtoReflect 
    
    
    func (x *TransitTable_TransitTimeRow) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*TransitTable_TransitTimeRow) Reset 
    
    
    func (x *TransitTable_TransitTimeRow) Reset()

### func (*TransitTable_TransitTimeRow) String 
    
    
    func (x *TransitTable_TransitTimeRow) String() [string](https://pkg.go.dev/builtin#string)

## TransitTable_TransitTimeRow_TransitTimeValue
    
    
    type TransitTable_TransitTimeRow_TransitTimeValue struct {
    
    	// Minimum transit time range in business days. 0 means same
    	// day delivery, 1 means next day delivery.
    	MinTransitDays *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,1,opt,name=min_transit_days,json=minTransitDays,proto3,oneof" json:"min_transit_days,omitempty"`
    	// Must be greater than or equal to `min_transit_days`.
    	MaxTransitDays *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=max_transit_days,json=maxTransitDays,proto3,oneof" json:"max_transit_days,omitempty"`
    	// contains filtered or unexported fields
    }

Transit time range (min-max) in business days.

### func (*TransitTable_TransitTimeRow_TransitTimeValue) Descriptor 
    
    
    func (*TransitTable_TransitTimeRow_TransitTimeValue) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use TransitTable_TransitTimeRow_TransitTimeValue.ProtoReflect.Descriptor instead.

### func (*TransitTable_TransitTimeRow_TransitTimeValue) GetMaxTransitDays 
    
    
    func (x *TransitTable_TransitTimeRow_TransitTimeValue) GetMaxTransitDays() [int32](https://pkg.go.dev/builtin#int32)

### func (*TransitTable_TransitTimeRow_TransitTimeValue) GetMinTransitDays 
    
    
    func (x *TransitTable_TransitTimeRow_TransitTimeValue) GetMinTransitDays() [int32](https://pkg.go.dev/builtin#int32)

### func (*TransitTable_TransitTimeRow_TransitTimeValue) ProtoMessage 
    
    
    func (*TransitTable_TransitTimeRow_TransitTimeValue) ProtoMessage()

### func (*TransitTable_TransitTimeRow_TransitTimeValue) ProtoReflect 
    
    
    func (x *TransitTable_TransitTimeRow_TransitTimeValue) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*TransitTable_TransitTimeRow_TransitTimeValue) Reset 
    
    
    func (x *TransitTable_TransitTimeRow_TransitTimeValue) Reset()

### func (*TransitTable_TransitTimeRow_TransitTimeValue) String 
    
    
    func (x *TransitTable_TransitTimeRow_TransitTimeValue) String() [string](https://pkg.go.dev/builtin#string)

## UnclaimHomepageRequest
    
    
    type UnclaimHomepageRequest struct {
    
    	// Required. The name of the homepage to unclaim.
    	// Format: `accounts/{account}/homepage`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the `UnclaimHomepage` method.

### func (*UnclaimHomepageRequest) Descriptor 
    
    
    func (*UnclaimHomepageRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UnclaimHomepageRequest.ProtoReflect.Descriptor instead.

### func (*UnclaimHomepageRequest) GetName 
    
    
    func (x *UnclaimHomepageRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*UnclaimHomepageRequest) ProtoMessage 
    
    
    func (*UnclaimHomepageRequest) ProtoMessage()

### func (*UnclaimHomepageRequest) ProtoReflect 
    
    
    func (x *UnclaimHomepageRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UnclaimHomepageRequest) Reset 
    
    
    func (x *UnclaimHomepageRequest) Reset()

### func (*UnclaimHomepageRequest) String 
    
    
    func (x *UnclaimHomepageRequest) String() [string](https://pkg.go.dev/builtin#string)

## UnimplementedAccountIssueServiceServer
    
    
    type UnimplementedAccountIssueServiceServer struct {
    }

UnimplementedAccountIssueServiceServer should be embedded to have forward compatible implementations.

### func (UnimplementedAccountIssueServiceServer) ListAccountIssues 
    
    
    func (UnimplementedAccountIssueServiceServer) ListAccountIssues([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListAccountIssuesRequest) (*ListAccountIssuesResponse, [error](https://pkg.go.dev/builtin#error))

## UnimplementedAccountTaxServiceServer
    
    
    type UnimplementedAccountTaxServiceServer struct {
    }

UnimplementedAccountTaxServiceServer should be embedded to have forward compatible implementations.

### func (UnimplementedAccountTaxServiceServer) GetAccountTax 
    
    
    func (UnimplementedAccountTaxServiceServer) GetAccountTax([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetAccountTaxRequest) (*AccountTax, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedAccountTaxServiceServer) ListAccountTax 
    
    
    func (UnimplementedAccountTaxServiceServer) ListAccountTax([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListAccountTaxRequest) (*ListAccountTaxResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedAccountTaxServiceServer) UpdateAccountTax 
    
    
    func (UnimplementedAccountTaxServiceServer) UpdateAccountTax([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UpdateAccountTaxRequest) (*AccountTax, [error](https://pkg.go.dev/builtin#error))

## UnimplementedAccountsServiceServer
    
    
    type UnimplementedAccountsServiceServer struct {
    }

UnimplementedAccountsServiceServer should be embedded to have forward compatible implementations.

### func (UnimplementedAccountsServiceServer) CreateAndConfigureAccount 
    
    
    func (UnimplementedAccountsServiceServer) CreateAndConfigureAccount([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CreateAndConfigureAccountRequest) (*Account, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedAccountsServiceServer) DeleteAccount 
    
    
    func (UnimplementedAccountsServiceServer) DeleteAccount([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *DeleteAccountRequest) (*[emptypb](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb).[Empty](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb#Empty), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedAccountsServiceServer) GetAccount 
    
    
    func (UnimplementedAccountsServiceServer) GetAccount([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetAccountRequest) (*Account, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedAccountsServiceServer) ListAccounts 
    
    
    func (UnimplementedAccountsServiceServer) ListAccounts([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListAccountsRequest) (*ListAccountsResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedAccountsServiceServer) ListSubAccounts 
    
    
    func (UnimplementedAccountsServiceServer) ListSubAccounts([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListSubAccountsRequest) (*ListSubAccountsResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedAccountsServiceServer) UpdateAccount 
    
    
    func (UnimplementedAccountsServiceServer) UpdateAccount([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UpdateAccountRequest) (*Account, [error](https://pkg.go.dev/builtin#error))

## UnimplementedAutofeedSettingsServiceServer
    
    
    type UnimplementedAutofeedSettingsServiceServer struct {
    }

UnimplementedAutofeedSettingsServiceServer should be embedded to have forward compatible implementations.

### func (UnimplementedAutofeedSettingsServiceServer) GetAutofeedSettings 
    
    
    func (UnimplementedAutofeedSettingsServiceServer) GetAutofeedSettings([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetAutofeedSettingsRequest) (*AutofeedSettings, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedAutofeedSettingsServiceServer) UpdateAutofeedSettings 
    
    
    func (UnimplementedAutofeedSettingsServiceServer) UpdateAutofeedSettings([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UpdateAutofeedSettingsRequest) (*AutofeedSettings, [error](https://pkg.go.dev/builtin#error))

## UnimplementedAutomaticImprovementsServiceServer
    
    
    type UnimplementedAutomaticImprovementsServiceServer struct {
    }

UnimplementedAutomaticImprovementsServiceServer should be embedded to have forward compatible implementations.

### func (UnimplementedAutomaticImprovementsServiceServer) GetAutomaticImprovements 
    
    
    func (UnimplementedAutomaticImprovementsServiceServer) GetAutomaticImprovements([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetAutomaticImprovementsRequest) (*AutomaticImprovements, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedAutomaticImprovementsServiceServer) UpdateAutomaticImprovements 
    
    
    func (UnimplementedAutomaticImprovementsServiceServer) UpdateAutomaticImprovements([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UpdateAutomaticImprovementsRequest) (*AutomaticImprovements, [error](https://pkg.go.dev/builtin#error))

## UnimplementedBusinessIdentityServiceServer
    
    
    type UnimplementedBusinessIdentityServiceServer struct {
    }

UnimplementedBusinessIdentityServiceServer should be embedded to have forward compatible implementations.

### func (UnimplementedBusinessIdentityServiceServer) GetBusinessIdentity 
    
    
    func (UnimplementedBusinessIdentityServiceServer) GetBusinessIdentity([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetBusinessIdentityRequest) (*BusinessIdentity, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedBusinessIdentityServiceServer) UpdateBusinessIdentity 
    
    
    func (UnimplementedBusinessIdentityServiceServer) UpdateBusinessIdentity([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UpdateBusinessIdentityRequest) (*BusinessIdentity, [error](https://pkg.go.dev/builtin#error))

## UnimplementedBusinessInfoServiceServer
    
    
    type UnimplementedBusinessInfoServiceServer struct {
    }

UnimplementedBusinessInfoServiceServer should be embedded to have forward compatible implementations.

### func (UnimplementedBusinessInfoServiceServer) GetBusinessInfo 
    
    
    func (UnimplementedBusinessInfoServiceServer) GetBusinessInfo([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetBusinessInfoRequest) (*BusinessInfo, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedBusinessInfoServiceServer) UpdateBusinessInfo 
    
    
    func (UnimplementedBusinessInfoServiceServer) UpdateBusinessInfo([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UpdateBusinessInfoRequest) (*BusinessInfo, [error](https://pkg.go.dev/builtin#error))

## UnimplementedCheckoutSettingsServiceServer
    
    
    type UnimplementedCheckoutSettingsServiceServer struct {
    }

UnimplementedCheckoutSettingsServiceServer should be embedded to have forward compatible implementations.

### func (UnimplementedCheckoutSettingsServiceServer) CreateCheckoutSettings 
    
    
    func (UnimplementedCheckoutSettingsServiceServer) CreateCheckoutSettings([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CreateCheckoutSettingsRequest) (*CheckoutSettings, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedCheckoutSettingsServiceServer) DeleteCheckoutSettings 
    
    
    func (UnimplementedCheckoutSettingsServiceServer) DeleteCheckoutSettings([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *DeleteCheckoutSettingsRequest) (*[emptypb](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb).[Empty](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb#Empty), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedCheckoutSettingsServiceServer) GetCheckoutSettings 
    
    
    func (UnimplementedCheckoutSettingsServiceServer) GetCheckoutSettings([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetCheckoutSettingsRequest) (*CheckoutSettings, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedCheckoutSettingsServiceServer) UpdateCheckoutSettings 
    
    
    func (UnimplementedCheckoutSettingsServiceServer) UpdateCheckoutSettings([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UpdateCheckoutSettingsRequest) (*CheckoutSettings, [error](https://pkg.go.dev/builtin#error))

## UnimplementedEmailPreferencesServiceServer
    
    
    type UnimplementedEmailPreferencesServiceServer struct {
    }

UnimplementedEmailPreferencesServiceServer should be embedded to have forward compatible implementations.

### func (UnimplementedEmailPreferencesServiceServer) GetEmailPreferences 
    
    
    func (UnimplementedEmailPreferencesServiceServer) GetEmailPreferences([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetEmailPreferencesRequest) (*EmailPreferences, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedEmailPreferencesServiceServer) UpdateEmailPreferences 
    
    
    func (UnimplementedEmailPreferencesServiceServer) UpdateEmailPreferences([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UpdateEmailPreferencesRequest) (*EmailPreferences, [error](https://pkg.go.dev/builtin#error))

## UnimplementedGbpAccountsServiceServer
    
    
    type UnimplementedGbpAccountsServiceServer struct {
    }

UnimplementedGbpAccountsServiceServer should be embedded to have forward compatible implementations.

### func (UnimplementedGbpAccountsServiceServer) LinkGbpAccount 
    
    
    func (UnimplementedGbpAccountsServiceServer) LinkGbpAccount([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *LinkGbpAccountRequest) (*LinkGbpAccountResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedGbpAccountsServiceServer) ListGbpAccounts 
    
    
    func (UnimplementedGbpAccountsServiceServer) ListGbpAccounts([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListGbpAccountsRequest) (*ListGbpAccountsResponse, [error](https://pkg.go.dev/builtin#error))

## UnimplementedHomepageServiceServer
    
    
    type UnimplementedHomepageServiceServer struct {
    }

UnimplementedHomepageServiceServer should be embedded to have forward compatible implementations.

### func (UnimplementedHomepageServiceServer) ClaimHomepage 
    
    
    func (UnimplementedHomepageServiceServer) ClaimHomepage([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ClaimHomepageRequest) (*Homepage, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedHomepageServiceServer) GetHomepage 
    
    
    func (UnimplementedHomepageServiceServer) GetHomepage([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetHomepageRequest) (*Homepage, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedHomepageServiceServer) UnclaimHomepage 
    
    
    func (UnimplementedHomepageServiceServer) UnclaimHomepage([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UnclaimHomepageRequest) (*Homepage, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedHomepageServiceServer) UpdateHomepage 
    
    
    func (UnimplementedHomepageServiceServer) UpdateHomepage([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UpdateHomepageRequest) (*Homepage, [error](https://pkg.go.dev/builtin#error))

## UnimplementedLfpProvidersServiceServer
    
    
    type UnimplementedLfpProvidersServiceServer struct {
    }

UnimplementedLfpProvidersServiceServer should be embedded to have forward compatible implementations.

### func (UnimplementedLfpProvidersServiceServer) FindLfpProviders 
    
    
    func (UnimplementedLfpProvidersServiceServer) FindLfpProviders([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *FindLfpProvidersRequest) (*FindLfpProvidersResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedLfpProvidersServiceServer) LinkLfpProvider 
    
    
    func (UnimplementedLfpProvidersServiceServer) LinkLfpProvider([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *LinkLfpProviderRequest) (*LinkLfpProviderResponse, [error](https://pkg.go.dev/builtin#error))

## UnimplementedOmnichannelSettingsServiceServer
    
    
    type UnimplementedOmnichannelSettingsServiceServer struct {
    }

UnimplementedOmnichannelSettingsServiceServer should be embedded to have forward compatible implementations.

### func (UnimplementedOmnichannelSettingsServiceServer) CreateOmnichannelSetting 
    
    
    func (UnimplementedOmnichannelSettingsServiceServer) CreateOmnichannelSetting([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CreateOmnichannelSettingRequest) (*OmnichannelSetting, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedOmnichannelSettingsServiceServer) GetOmnichannelSetting 
    
    
    func (UnimplementedOmnichannelSettingsServiceServer) GetOmnichannelSetting([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetOmnichannelSettingRequest) (*OmnichannelSetting, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedOmnichannelSettingsServiceServer) ListOmnichannelSettings 
    
    
    func (UnimplementedOmnichannelSettingsServiceServer) ListOmnichannelSettings([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListOmnichannelSettingsRequest) (*ListOmnichannelSettingsResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedOmnichannelSettingsServiceServer) RequestInventoryVerification 
    
    
    func (UnimplementedOmnichannelSettingsServiceServer) RequestInventoryVerification([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *RequestInventoryVerificationRequest) (*RequestInventoryVerificationResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedOmnichannelSettingsServiceServer) UpdateOmnichannelSetting 
    
    
    func (UnimplementedOmnichannelSettingsServiceServer) UpdateOmnichannelSetting([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UpdateOmnichannelSettingRequest) (*OmnichannelSetting, [error](https://pkg.go.dev/builtin#error))

## UnimplementedOnlineReturnPolicyServiceServer
    
    
    type UnimplementedOnlineReturnPolicyServiceServer struct {
    }

UnimplementedOnlineReturnPolicyServiceServer should be embedded to have forward compatible implementations.

### func (UnimplementedOnlineReturnPolicyServiceServer) CreateOnlineReturnPolicy 
    
    
    func (UnimplementedOnlineReturnPolicyServiceServer) CreateOnlineReturnPolicy([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CreateOnlineReturnPolicyRequest) (*OnlineReturnPolicy, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedOnlineReturnPolicyServiceServer) DeleteOnlineReturnPolicy 
    
    
    func (UnimplementedOnlineReturnPolicyServiceServer) DeleteOnlineReturnPolicy([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *DeleteOnlineReturnPolicyRequest) (*[emptypb](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb).[Empty](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb#Empty), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedOnlineReturnPolicyServiceServer) GetOnlineReturnPolicy 
    
    
    func (UnimplementedOnlineReturnPolicyServiceServer) GetOnlineReturnPolicy([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetOnlineReturnPolicyRequest) (*OnlineReturnPolicy, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedOnlineReturnPolicyServiceServer) ListOnlineReturnPolicies 
    
    
    func (UnimplementedOnlineReturnPolicyServiceServer) ListOnlineReturnPolicies([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListOnlineReturnPoliciesRequest) (*ListOnlineReturnPoliciesResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedOnlineReturnPolicyServiceServer) UpdateOnlineReturnPolicy 
    
    
    func (UnimplementedOnlineReturnPolicyServiceServer) UpdateOnlineReturnPolicy([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UpdateOnlineReturnPolicyRequest) (*OnlineReturnPolicy, [error](https://pkg.go.dev/builtin#error))

## UnimplementedProgramsServiceServer
    
    
    type UnimplementedProgramsServiceServer struct {
    }

UnimplementedProgramsServiceServer should be embedded to have forward compatible implementations.

### func (UnimplementedProgramsServiceServer) DisableProgram 
    
    
    func (UnimplementedProgramsServiceServer) DisableProgram([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *DisableProgramRequest) (*Program, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedProgramsServiceServer) EnableProgram 
    
    
    func (UnimplementedProgramsServiceServer) EnableProgram([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *EnableProgramRequest) (*Program, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedProgramsServiceServer) GetProgram 
    
    
    func (UnimplementedProgramsServiceServer) GetProgram([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetProgramRequest) (*Program, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedProgramsServiceServer) ListPrograms 
    
    
    func (UnimplementedProgramsServiceServer) ListPrograms([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListProgramsRequest) (*ListProgramsResponse, [error](https://pkg.go.dev/builtin#error))

## UnimplementedRegionsServiceServer
    
    
    type UnimplementedRegionsServiceServer struct {
    }

UnimplementedRegionsServiceServer should be embedded to have forward compatible implementations.

### func (UnimplementedRegionsServiceServer) CreateRegion 
    
    
    func (UnimplementedRegionsServiceServer) CreateRegion([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CreateRegionRequest) (*Region, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedRegionsServiceServer) DeleteRegion 
    
    
    func (UnimplementedRegionsServiceServer) DeleteRegion([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *DeleteRegionRequest) (*[emptypb](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb).[Empty](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb#Empty), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedRegionsServiceServer) GetRegion 
    
    
    func (UnimplementedRegionsServiceServer) GetRegion([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetRegionRequest) (*Region, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedRegionsServiceServer) ListRegions 
    
    
    func (UnimplementedRegionsServiceServer) ListRegions([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListRegionsRequest) (*ListRegionsResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedRegionsServiceServer) UpdateRegion 
    
    
    func (UnimplementedRegionsServiceServer) UpdateRegion([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UpdateRegionRequest) (*Region, [error](https://pkg.go.dev/builtin#error))

## UnimplementedShippingSettingsServiceServer
    
    
    type UnimplementedShippingSettingsServiceServer struct {
    }

UnimplementedShippingSettingsServiceServer should be embedded to have forward compatible implementations.

### func (UnimplementedShippingSettingsServiceServer) GetShippingSettings 
    
    
    func (UnimplementedShippingSettingsServiceServer) GetShippingSettings([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetShippingSettingsRequest) (*ShippingSettings, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedShippingSettingsServiceServer) InsertShippingSettings 
    
    
    func (UnimplementedShippingSettingsServiceServer) InsertShippingSettings([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *InsertShippingSettingsRequest) (*ShippingSettings, [error](https://pkg.go.dev/builtin#error))

## UnimplementedTermsOfServiceAgreementStateServiceServer
    
    
    type UnimplementedTermsOfServiceAgreementStateServiceServer struct {
    }

UnimplementedTermsOfServiceAgreementStateServiceServer should be embedded to have forward compatible implementations.

### func (UnimplementedTermsOfServiceAgreementStateServiceServer) GetTermsOfServiceAgreementState 
    
    
    func (UnimplementedTermsOfServiceAgreementStateServiceServer) GetTermsOfServiceAgreementState([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetTermsOfServiceAgreementStateRequest) (*TermsOfServiceAgreementState, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedTermsOfServiceAgreementStateServiceServer) RetrieveForApplicationTermsOfServiceAgreementState 
    
    
    func (UnimplementedTermsOfServiceAgreementStateServiceServer) RetrieveForApplicationTermsOfServiceAgreementState([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *RetrieveForApplicationTermsOfServiceAgreementStateRequest) (*TermsOfServiceAgreementState, [error](https://pkg.go.dev/builtin#error))

## UnimplementedTermsOfServiceServiceServer
    
    
    type UnimplementedTermsOfServiceServiceServer struct {
    }

UnimplementedTermsOfServiceServiceServer should be embedded to have forward compatible implementations.

### func (UnimplementedTermsOfServiceServiceServer) AcceptTermsOfService 
    
    
    func (UnimplementedTermsOfServiceServiceServer) AcceptTermsOfService([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *AcceptTermsOfServiceRequest) (*[emptypb](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb).[Empty](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb#Empty), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedTermsOfServiceServiceServer) GetTermsOfService 
    
    
    func (UnimplementedTermsOfServiceServiceServer) GetTermsOfService([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetTermsOfServiceRequest) (*TermsOfService, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedTermsOfServiceServiceServer) RetrieveLatestTermsOfService 
    
    
    func (UnimplementedTermsOfServiceServiceServer) RetrieveLatestTermsOfService([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *RetrieveLatestTermsOfServiceRequest) (*TermsOfService, [error](https://pkg.go.dev/builtin#error))

## UnimplementedUserServiceServer
    
    
    type UnimplementedUserServiceServer struct {
    }

UnimplementedUserServiceServer should be embedded to have forward compatible implementations.

### func (UnimplementedUserServiceServer) CreateUser 
    
    
    func (UnimplementedUserServiceServer) CreateUser([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CreateUserRequest) (*User, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedUserServiceServer) DeleteUser 
    
    
    func (UnimplementedUserServiceServer) DeleteUser([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *DeleteUserRequest) (*[emptypb](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb).[Empty](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb#Empty), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedUserServiceServer) GetUser 
    
    
    func (UnimplementedUserServiceServer) GetUser([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetUserRequest) (*User, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedUserServiceServer) ListUsers 
    
    
    func (UnimplementedUserServiceServer) ListUsers([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListUsersRequest) (*ListUsersResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedUserServiceServer) UpdateUser 
    
    
    func (UnimplementedUserServiceServer) UpdateUser([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UpdateUserRequest) (*User, [error](https://pkg.go.dev/builtin#error))

## UnsafeAccountIssueServiceServer
    
    
    type UnsafeAccountIssueServiceServer interface {
    	// contains filtered or unexported methods
    }

UnsafeAccountIssueServiceServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to AccountIssueServiceServer will result in compilation errors.

## UnsafeAccountTaxServiceServer
    
    
    type UnsafeAccountTaxServiceServer interface {
    	// contains filtered or unexported methods
    }

UnsafeAccountTaxServiceServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to AccountTaxServiceServer will result in compilation errors.

## UnsafeAccountsServiceServer
    
    
    type UnsafeAccountsServiceServer interface {
    	// contains filtered or unexported methods
    }

UnsafeAccountsServiceServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to AccountsServiceServer will result in compilation errors.

## UnsafeAutofeedSettingsServiceServer
    
    
    type UnsafeAutofeedSettingsServiceServer interface {
    	// contains filtered or unexported methods
    }

UnsafeAutofeedSettingsServiceServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to AutofeedSettingsServiceServer will result in compilation errors.

## UnsafeAutomaticImprovementsServiceServer
    
    
    type UnsafeAutomaticImprovementsServiceServer interface {
    	// contains filtered or unexported methods
    }

UnsafeAutomaticImprovementsServiceServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to AutomaticImprovementsServiceServer will result in compilation errors.

## UnsafeBusinessIdentityServiceServer
    
    
    type UnsafeBusinessIdentityServiceServer interface {
    	// contains filtered or unexported methods
    }

UnsafeBusinessIdentityServiceServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to BusinessIdentityServiceServer will result in compilation errors.

## UnsafeBusinessInfoServiceServer
    
    
    type UnsafeBusinessInfoServiceServer interface {
    	// contains filtered or unexported methods
    }

UnsafeBusinessInfoServiceServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to BusinessInfoServiceServer will result in compilation errors.

## UnsafeCheckoutSettingsServiceServer
    
    
    type UnsafeCheckoutSettingsServiceServer interface {
    	// contains filtered or unexported methods
    }

UnsafeCheckoutSettingsServiceServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to CheckoutSettingsServiceServer will result in compilation errors.

## UnsafeEmailPreferencesServiceServer
    
    
    type UnsafeEmailPreferencesServiceServer interface {
    	// contains filtered or unexported methods
    }

UnsafeEmailPreferencesServiceServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to EmailPreferencesServiceServer will result in compilation errors.

## UnsafeGbpAccountsServiceServer
    
    
    type UnsafeGbpAccountsServiceServer interface {
    	// contains filtered or unexported methods
    }

UnsafeGbpAccountsServiceServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to GbpAccountsServiceServer will result in compilation errors.

## UnsafeHomepageServiceServer
    
    
    type UnsafeHomepageServiceServer interface {
    	// contains filtered or unexported methods
    }

UnsafeHomepageServiceServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to HomepageServiceServer will result in compilation errors.

## UnsafeLfpProvidersServiceServer
    
    
    type UnsafeLfpProvidersServiceServer interface {
    	// contains filtered or unexported methods
    }

UnsafeLfpProvidersServiceServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to LfpProvidersServiceServer will result in compilation errors.

## UnsafeOmnichannelSettingsServiceServer
    
    
    type UnsafeOmnichannelSettingsServiceServer interface {
    	// contains filtered or unexported methods
    }

UnsafeOmnichannelSettingsServiceServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to OmnichannelSettingsServiceServer will result in compilation errors.

## UnsafeOnlineReturnPolicyServiceServer
    
    
    type UnsafeOnlineReturnPolicyServiceServer interface {
    	// contains filtered or unexported methods
    }

UnsafeOnlineReturnPolicyServiceServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to OnlineReturnPolicyServiceServer will result in compilation errors.

## UnsafeProgramsServiceServer
    
    
    type UnsafeProgramsServiceServer interface {
    	// contains filtered or unexported methods
    }

UnsafeProgramsServiceServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to ProgramsServiceServer will result in compilation errors.

## UnsafeRegionsServiceServer
    
    
    type UnsafeRegionsServiceServer interface {
    	// contains filtered or unexported methods
    }

UnsafeRegionsServiceServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to RegionsServiceServer will result in compilation errors.

## UnsafeShippingSettingsServiceServer
    
    
    type UnsafeShippingSettingsServiceServer interface {
    	// contains filtered or unexported methods
    }

UnsafeShippingSettingsServiceServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to ShippingSettingsServiceServer will result in compilation errors.

## UnsafeTermsOfServiceAgreementStateServiceServer
    
    
    type UnsafeTermsOfServiceAgreementStateServiceServer interface {
    	// contains filtered or unexported methods
    }

UnsafeTermsOfServiceAgreementStateServiceServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to TermsOfServiceAgreementStateServiceServer will result in compilation errors.

## UnsafeTermsOfServiceServiceServer
    
    
    type UnsafeTermsOfServiceServiceServer interface {
    	// contains filtered or unexported methods
    }

UnsafeTermsOfServiceServiceServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to TermsOfServiceServiceServer will result in compilation errors.

## UnsafeUserServiceServer
    
    
    type UnsafeUserServiceServer interface {
    	// contains filtered or unexported methods
    }

UnsafeUserServiceServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to UserServiceServer will result in compilation errors.

## UpdateAccountRequest
    
    
    type UpdateAccountRequest struct {
    
    	// Required. The new version of the account.
    	Account *Account `protobuf:"bytes,1,opt,name=account,proto3" json:"account,omitempty"`
    	// Required. List of fields being updated.
    	UpdateMask *fieldmaskpb.FieldMask `protobuf:"bytes,2,opt,name=update_mask,json=updateMask,proto3" json:"update_mask,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the `UpdateAccount` method.

### func (*UpdateAccountRequest) Descriptor 
    
    
    func (*UpdateAccountRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UpdateAccountRequest.ProtoReflect.Descriptor instead.

### func (*UpdateAccountRequest) GetAccount 
    
    
    func (x *UpdateAccountRequest) GetAccount() *Account

### func (*UpdateAccountRequest) GetUpdateMask 
    
    
    func (x *UpdateAccountRequest) GetUpdateMask() *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask)

### func (*UpdateAccountRequest) ProtoMessage 
    
    
    func (*UpdateAccountRequest) ProtoMessage()

### func (*UpdateAccountRequest) ProtoReflect 
    
    
    func (x *UpdateAccountRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UpdateAccountRequest) Reset 
    
    
    func (x *UpdateAccountRequest) Reset()

### func (*UpdateAccountRequest) String 
    
    
    func (x *UpdateAccountRequest) String() [string](https://pkg.go.dev/builtin#string)

## UpdateAccountTaxRequest
    
    
    type UpdateAccountTaxRequest struct {
    
    	// Required. The tax setting that will be updated
    	AccountTax *AccountTax `protobuf:"bytes,1,opt,name=account_tax,json=accountTax,proto3" json:"account_tax,omitempty"`
    	// The list of fields to be updated
    	UpdateMask *fieldmaskpb.FieldMask `protobuf:"bytes,2,opt,name=update_mask,json=updateMask,proto3" json:"update_mask,omitempty"`
    	// contains filtered or unexported fields
    }

Request to update the tax settings

### func (*UpdateAccountTaxRequest) Descriptor 
    
    
    func (*UpdateAccountTaxRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UpdateAccountTaxRequest.ProtoReflect.Descriptor instead.

### func (*UpdateAccountTaxRequest) GetAccountTax 
    
    
    func (x *UpdateAccountTaxRequest) GetAccountTax() *AccountTax

### func (*UpdateAccountTaxRequest) GetUpdateMask 
    
    
    func (x *UpdateAccountTaxRequest) GetUpdateMask() *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask)

### func (*UpdateAccountTaxRequest) ProtoMessage 
    
    
    func (*UpdateAccountTaxRequest) ProtoMessage()

### func (*UpdateAccountTaxRequest) ProtoReflect 
    
    
    func (x *UpdateAccountTaxRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UpdateAccountTaxRequest) Reset 
    
    
    func (x *UpdateAccountTaxRequest) Reset()

### func (*UpdateAccountTaxRequest) String 
    
    
    func (x *UpdateAccountTaxRequest) String() [string](https://pkg.go.dev/builtin#string)

## UpdateAutofeedSettingsRequest
    
    
    type UpdateAutofeedSettingsRequest struct {
    
    	// Required. The new version of the autofeed setting.
    	AutofeedSettings *AutofeedSettings `protobuf:"bytes,1,opt,name=autofeed_settings,json=autofeedSettings,proto3" json:"autofeed_settings,omitempty"`
    	// Required. List of fields being updated.
    	UpdateMask *fieldmaskpb.FieldMask `protobuf:"bytes,2,opt,name=update_mask,json=updateMask,proto3" json:"update_mask,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the `UpdateAutofeedSettings` method.

### func (*UpdateAutofeedSettingsRequest) Descriptor 
    
    
    func (*UpdateAutofeedSettingsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UpdateAutofeedSettingsRequest.ProtoReflect.Descriptor instead.

### func (*UpdateAutofeedSettingsRequest) GetAutofeedSettings 
    
    
    func (x *UpdateAutofeedSettingsRequest) GetAutofeedSettings() *AutofeedSettings

### func (*UpdateAutofeedSettingsRequest) GetUpdateMask 
    
    
    func (x *UpdateAutofeedSettingsRequest) GetUpdateMask() *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask)

### func (*UpdateAutofeedSettingsRequest) ProtoMessage 
    
    
    func (*UpdateAutofeedSettingsRequest) ProtoMessage()

### func (*UpdateAutofeedSettingsRequest) ProtoReflect 
    
    
    func (x *UpdateAutofeedSettingsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UpdateAutofeedSettingsRequest) Reset 
    
    
    func (x *UpdateAutofeedSettingsRequest) Reset()

### func (*UpdateAutofeedSettingsRequest) String 
    
    
    func (x *UpdateAutofeedSettingsRequest) String() [string](https://pkg.go.dev/builtin#string)

## UpdateAutomaticImprovementsRequest
    
    
    type UpdateAutomaticImprovementsRequest struct {
    
    	// Required. The new version of the automatic imrovements.
    	AutomaticImprovements *AutomaticImprovements `protobuf:"bytes,1,opt,name=automatic_improvements,json=automaticImprovements,proto3" json:"automatic_improvements,omitempty"`
    	// Required. List of fields being updated.
    	// The following fields are supported (in both `snake_case` and
    	// `lowerCamelCase`):
    	//
    	// - `item_updates`
    	// - `item_updates.account_level_settings`
    	// - `image_improvements`
    	// - `image_improvements.account_level_settings`
    	// - `shipping_improvements`
    	// - `shipping_improvements.allow_shipping_improvements`
    	UpdateMask *fieldmaskpb.FieldMask `protobuf:"bytes,2,opt,name=update_mask,json=updateMask,proto3" json:"update_mask,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the `UpdateAutomaticImprovements` method.

### func (*UpdateAutomaticImprovementsRequest) Descriptor 
    
    
    func (*UpdateAutomaticImprovementsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UpdateAutomaticImprovementsRequest.ProtoReflect.Descriptor instead.

### func (*UpdateAutomaticImprovementsRequest) GetAutomaticImprovements 
    
    
    func (x *UpdateAutomaticImprovementsRequest) GetAutomaticImprovements() *AutomaticImprovements

### func (*UpdateAutomaticImprovementsRequest) GetUpdateMask 
    
    
    func (x *UpdateAutomaticImprovementsRequest) GetUpdateMask() *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask)

### func (*UpdateAutomaticImprovementsRequest) ProtoMessage 
    
    
    func (*UpdateAutomaticImprovementsRequest) ProtoMessage()

### func (*UpdateAutomaticImprovementsRequest) ProtoReflect 
    
    
    func (x *UpdateAutomaticImprovementsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UpdateAutomaticImprovementsRequest) Reset 
    
    
    func (x *UpdateAutomaticImprovementsRequest) Reset()

### func (*UpdateAutomaticImprovementsRequest) String 
    
    
    func (x *UpdateAutomaticImprovementsRequest) String() [string](https://pkg.go.dev/builtin#string)

## UpdateBusinessIdentityRequest
    
    
    type UpdateBusinessIdentityRequest struct {
    
    	// Required. The new version of the business identity.
    	BusinessIdentity *BusinessIdentity `protobuf:"bytes,1,opt,name=business_identity,json=businessIdentity,proto3" json:"business_identity,omitempty"`
    	// Required. List of fields being updated.
    	UpdateMask *fieldmaskpb.FieldMask `protobuf:"bytes,2,opt,name=update_mask,json=updateMask,proto3" json:"update_mask,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the `UpdateBusinessIdentity` method.

### func (*UpdateBusinessIdentityRequest) Descriptor 
    
    
    func (*UpdateBusinessIdentityRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UpdateBusinessIdentityRequest.ProtoReflect.Descriptor instead.

### func (*UpdateBusinessIdentityRequest) GetBusinessIdentity 
    
    
    func (x *UpdateBusinessIdentityRequest) GetBusinessIdentity() *BusinessIdentity

### func (*UpdateBusinessIdentityRequest) GetUpdateMask 
    
    
    func (x *UpdateBusinessIdentityRequest) GetUpdateMask() *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask)

### func (*UpdateBusinessIdentityRequest) ProtoMessage 
    
    
    func (*UpdateBusinessIdentityRequest) ProtoMessage()

### func (*UpdateBusinessIdentityRequest) ProtoReflect 
    
    
    func (x *UpdateBusinessIdentityRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UpdateBusinessIdentityRequest) Reset 
    
    
    func (x *UpdateBusinessIdentityRequest) Reset()

### func (*UpdateBusinessIdentityRequest) String 
    
    
    func (x *UpdateBusinessIdentityRequest) String() [string](https://pkg.go.dev/builtin#string)

## UpdateBusinessInfoRequest
    
    
    type UpdateBusinessInfoRequest struct {
    
    	// Required. The new version of the business info.
    	BusinessInfo *BusinessInfo `protobuf:"bytes,1,opt,name=business_info,json=businessInfo,proto3" json:"business_info,omitempty"`
    	// Required. List of fields being updated.
    	UpdateMask *fieldmaskpb.FieldMask `protobuf:"bytes,2,opt,name=update_mask,json=updateMask,proto3" json:"update_mask,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the `UpdateBusinessInfo` method.

### func (*UpdateBusinessInfoRequest) Descriptor 
    
    
    func (*UpdateBusinessInfoRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UpdateBusinessInfoRequest.ProtoReflect.Descriptor instead.

### func (*UpdateBusinessInfoRequest) GetBusinessInfo 
    
    
    func (x *UpdateBusinessInfoRequest) GetBusinessInfo() *BusinessInfo

### func (*UpdateBusinessInfoRequest) GetUpdateMask 
    
    
    func (x *UpdateBusinessInfoRequest) GetUpdateMask() *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask)

### func (*UpdateBusinessInfoRequest) ProtoMessage 
    
    
    func (*UpdateBusinessInfoRequest) ProtoMessage()

### func (*UpdateBusinessInfoRequest) ProtoReflect 
    
    
    func (x *UpdateBusinessInfoRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UpdateBusinessInfoRequest) Reset 
    
    
    func (x *UpdateBusinessInfoRequest) Reset()

### func (*UpdateBusinessInfoRequest) String 
    
    
    func (x *UpdateBusinessInfoRequest) String() [string](https://pkg.go.dev/builtin#string)

## UpdateCheckoutSettingsRequest
    
    
    type UpdateCheckoutSettingsRequest struct {
    
    	// Required. The updated version of the `CheckoutSettings`.
    	// The `name` field is used to identify the `CheckoutSettings`.
    	// Format: `accounts/{account}/programs/{program}/checkoutSettings`
    	CheckoutSettings *CheckoutSettings `protobuf:"bytes,1,opt,name=checkout_settings,json=checkoutSettings,proto3" json:"checkout_settings,omitempty"`
    	// Required. List of fields being updated.
    	// The following fields are supported (in both `snake_case` and
    	// `lowerCamelCase`):
    	//
    	// - `eligible_destinations`
    	// - `uri_settings`
    	UpdateMask *fieldmaskpb.FieldMask `protobuf:"bytes,2,opt,name=update_mask,json=updateMask,proto3" json:"update_mask,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the `UpdateCheckoutSettings` method.

### func (*UpdateCheckoutSettingsRequest) Descriptor 
    
    
    func (*UpdateCheckoutSettingsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UpdateCheckoutSettingsRequest.ProtoReflect.Descriptor instead.

### func (*UpdateCheckoutSettingsRequest) GetCheckoutSettings 
    
    
    func (x *UpdateCheckoutSettingsRequest) GetCheckoutSettings() *CheckoutSettings

### func (*UpdateCheckoutSettingsRequest) GetUpdateMask 
    
    
    func (x *UpdateCheckoutSettingsRequest) GetUpdateMask() *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask)

### func (*UpdateCheckoutSettingsRequest) ProtoMessage 
    
    
    func (*UpdateCheckoutSettingsRequest) ProtoMessage()

### func (*UpdateCheckoutSettingsRequest) ProtoReflect 
    
    
    func (x *UpdateCheckoutSettingsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UpdateCheckoutSettingsRequest) Reset 
    
    
    func (x *UpdateCheckoutSettingsRequest) Reset()

### func (*UpdateCheckoutSettingsRequest) String 
    
    
    func (x *UpdateCheckoutSettingsRequest) String() [string](https://pkg.go.dev/builtin#string)

## UpdateEmailPreferencesRequest
    
    
    type UpdateEmailPreferencesRequest struct {
    
    	// Required. Email Preferences to be updated.
    	EmailPreferences *EmailPreferences `protobuf:"bytes,1,opt,name=email_preferences,json=emailPreferences,proto3" json:"email_preferences,omitempty"`
    	// Required. List of fields being updated.
    	UpdateMask *fieldmaskpb.FieldMask `protobuf:"bytes,2,opt,name=update_mask,json=updateMask,proto3" json:"update_mask,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for UpdateEmailPreferences method.

### func (*UpdateEmailPreferencesRequest) Descriptor 
    
    
    func (*UpdateEmailPreferencesRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UpdateEmailPreferencesRequest.ProtoReflect.Descriptor instead.

### func (*UpdateEmailPreferencesRequest) GetEmailPreferences 
    
    
    func (x *UpdateEmailPreferencesRequest) GetEmailPreferences() *EmailPreferences

### func (*UpdateEmailPreferencesRequest) GetUpdateMask 
    
    
    func (x *UpdateEmailPreferencesRequest) GetUpdateMask() *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask)

### func (*UpdateEmailPreferencesRequest) ProtoMessage 
    
    
    func (*UpdateEmailPreferencesRequest) ProtoMessage()

### func (*UpdateEmailPreferencesRequest) ProtoReflect 
    
    
    func (x *UpdateEmailPreferencesRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UpdateEmailPreferencesRequest) Reset 
    
    
    func (x *UpdateEmailPreferencesRequest) Reset()

### func (*UpdateEmailPreferencesRequest) String 
    
    
    func (x *UpdateEmailPreferencesRequest) String() [string](https://pkg.go.dev/builtin#string)

## UpdateHomepageRequest
    
    
    type UpdateHomepageRequest struct {
    
    	// Required. The new version of the homepage.
    	Homepage *Homepage `protobuf:"bytes,1,opt,name=homepage,proto3" json:"homepage,omitempty"`
    	// Required. List of fields being updated.
    	UpdateMask *fieldmaskpb.FieldMask `protobuf:"bytes,2,opt,name=update_mask,json=updateMask,proto3" json:"update_mask,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the `UpdateHomepage` method.

### func (*UpdateHomepageRequest) Descriptor 
    
    
    func (*UpdateHomepageRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UpdateHomepageRequest.ProtoReflect.Descriptor instead.

### func (*UpdateHomepageRequest) GetHomepage 
    
    
    func (x *UpdateHomepageRequest) GetHomepage() *Homepage

### func (*UpdateHomepageRequest) GetUpdateMask 
    
    
    func (x *UpdateHomepageRequest) GetUpdateMask() *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask)

### func (*UpdateHomepageRequest) ProtoMessage 
    
    
    func (*UpdateHomepageRequest) ProtoMessage()

### func (*UpdateHomepageRequest) ProtoReflect 
    
    
    func (x *UpdateHomepageRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UpdateHomepageRequest) Reset 
    
    
    func (x *UpdateHomepageRequest) Reset()

### func (*UpdateHomepageRequest) String 
    
    
    func (x *UpdateHomepageRequest) String() [string](https://pkg.go.dev/builtin#string)

## UpdateOmnichannelSettingRequest
    
    
    type UpdateOmnichannelSettingRequest struct {
    
    	// Required. The omnichannel setting to update.
    	//
    	// The omnichannel setting's `name` field is used to identify the
    	// omnichannel setting to be updated.
    	OmnichannelSetting *OmnichannelSetting `protobuf:"bytes,1,opt,name=omnichannel_setting,json=omnichannelSetting,proto3" json:"omnichannel_setting,omitempty"`
    	// Required. The list of fields to be updated.
    	//
    	// The following fields are supported in snake_case only:
    	// - `lsf_type`
    	// - `in_stock`
    	// - `pickup`
    	// - `odo`
    	// - `about`
    	// - `inventory_verification`
    	//
    	// Full replacement with wildcard `*`is supported, while empty/implied update
    	// mask is not.
    	UpdateMask *fieldmaskpb.FieldMask `protobuf:"bytes,2,opt,name=update_mask,json=updateMask,proto3" json:"update_mask,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the UpdateOmnichannelSetting method.

### func (*UpdateOmnichannelSettingRequest) Descriptor 
    
    
    func (*UpdateOmnichannelSettingRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UpdateOmnichannelSettingRequest.ProtoReflect.Descriptor instead.

### func (*UpdateOmnichannelSettingRequest) GetOmnichannelSetting 
    
    
    func (x *UpdateOmnichannelSettingRequest) GetOmnichannelSetting() *OmnichannelSetting

### func (*UpdateOmnichannelSettingRequest) GetUpdateMask 
    
    
    func (x *UpdateOmnichannelSettingRequest) GetUpdateMask() *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask)

### func (*UpdateOmnichannelSettingRequest) ProtoMessage 
    
    
    func (*UpdateOmnichannelSettingRequest) ProtoMessage()

### func (*UpdateOmnichannelSettingRequest) ProtoReflect 
    
    
    func (x *UpdateOmnichannelSettingRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UpdateOmnichannelSettingRequest) Reset 
    
    
    func (x *UpdateOmnichannelSettingRequest) Reset()

### func (*UpdateOmnichannelSettingRequest) String 
    
    
    func (x *UpdateOmnichannelSettingRequest) String() [string](https://pkg.go.dev/builtin#string)

## UpdateOnlineReturnPolicyRequest
    
    
    type UpdateOnlineReturnPolicyRequest struct {
    
    	// Required. The online return policy to update.
    	// The online return policy's `name` field is used to identify the
    	// online return policy to be updated.
    	OnlineReturnPolicy *OnlineReturnPolicy `protobuf:"bytes,1,opt,name=online_return_policy,json=onlineReturnPolicy,proto3" json:"online_return_policy,omitempty"`
    	// Optional. List of fields being updated.
    	//
    	// The following fields are supported (in both `snake_case` and
    	// `lowerCamelCase`):
    	//
    	// - `accept_defective_only`
    	// - `accept_exchange`
    	// - `item_conditions`
    	// - `policy`
    	// - `process_refund_days`
    	// - `restocking_fee`
    	// - `return_methods`
    	// - `return_policy_uri`
    	// - `return_shipping_fee`
    	UpdateMask *fieldmaskpb.FieldMask `protobuf:"bytes,2,opt,name=update_mask,json=updateMask,proto3" json:"update_mask,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the `UpdateOnlineReturnPolicy` method. The method supports field masks and when the mask is provided, only the fields specified in the mask are updated.

### func (*UpdateOnlineReturnPolicyRequest) Descriptor 
    
    
    func (*UpdateOnlineReturnPolicyRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UpdateOnlineReturnPolicyRequest.ProtoReflect.Descriptor instead.

### func (*UpdateOnlineReturnPolicyRequest) GetOnlineReturnPolicy 
    
    
    func (x *UpdateOnlineReturnPolicyRequest) GetOnlineReturnPolicy() *OnlineReturnPolicy

### func (*UpdateOnlineReturnPolicyRequest) GetUpdateMask 
    
    
    func (x *UpdateOnlineReturnPolicyRequest) GetUpdateMask() *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask)

### func (*UpdateOnlineReturnPolicyRequest) ProtoMessage 
    
    
    func (*UpdateOnlineReturnPolicyRequest) ProtoMessage()

### func (*UpdateOnlineReturnPolicyRequest) ProtoReflect 
    
    
    func (x *UpdateOnlineReturnPolicyRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UpdateOnlineReturnPolicyRequest) Reset 
    
    
    func (x *UpdateOnlineReturnPolicyRequest) Reset()

### func (*UpdateOnlineReturnPolicyRequest) String 
    
    
    func (x *UpdateOnlineReturnPolicyRequest) String() [string](https://pkg.go.dev/builtin#string)

## UpdateRegionRequest
    
    
    type UpdateRegionRequest struct {
    
    	// Required. The updated region.
    	Region *Region `protobuf:"bytes,1,opt,name=region,proto3" json:"region,omitempty"`
    	// Optional. The comma-separated field mask indicating the fields to update.
    	// Example:
    	// `"displayName,postalCodeArea.regionCode"`.
    	UpdateMask *fieldmaskpb.FieldMask `protobuf:"bytes,2,opt,name=update_mask,json=updateMask,proto3" json:"update_mask,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the `UpdateRegion` method.

### func (*UpdateRegionRequest) Descriptor 
    
    
    func (*UpdateRegionRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UpdateRegionRequest.ProtoReflect.Descriptor instead.

### func (*UpdateRegionRequest) GetRegion 
    
    
    func (x *UpdateRegionRequest) GetRegion() *Region

### func (*UpdateRegionRequest) GetUpdateMask 
    
    
    func (x *UpdateRegionRequest) GetUpdateMask() *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask)

### func (*UpdateRegionRequest) ProtoMessage 
    
    
    func (*UpdateRegionRequest) ProtoMessage()

### func (*UpdateRegionRequest) ProtoReflect 
    
    
    func (x *UpdateRegionRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UpdateRegionRequest) Reset 
    
    
    func (x *UpdateRegionRequest) Reset()

### func (*UpdateRegionRequest) String 
    
    
    func (x *UpdateRegionRequest) String() [string](https://pkg.go.dev/builtin#string)

## UpdateUserRequest
    
    
    type UpdateUserRequest struct {
    
    	// Required. The new version of the user.
    	//
    	// Use `me` to refer to your own email address, for example
    	// `accounts/{account}/users/me`.
    	User *User `protobuf:"bytes,1,opt,name=user,proto3" json:"user,omitempty"`
    	// Required. List of fields being updated.
    	UpdateMask *fieldmaskpb.FieldMask `protobuf:"bytes,2,opt,name=update_mask,json=updateMask,proto3" json:"update_mask,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the `UpdateUser` method.

### func (*UpdateUserRequest) Descriptor 
    
    
    func (*UpdateUserRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UpdateUserRequest.ProtoReflect.Descriptor instead.

### func (*UpdateUserRequest) GetUpdateMask 
    
    
    func (x *UpdateUserRequest) GetUpdateMask() *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask)

### func (*UpdateUserRequest) GetUser 
    
    
    func (x *UpdateUserRequest) GetUser() *User

### func (*UpdateUserRequest) ProtoMessage 
    
    
    func (*UpdateUserRequest) ProtoMessage()

### func (*UpdateUserRequest) ProtoReflect 
    
    
    func (x *UpdateUserRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UpdateUserRequest) Reset 
    
    
    func (x *UpdateUserRequest) Reset()

### func (*UpdateUserRequest) String 
    
    
    func (x *UpdateUserRequest) String() [string](https://pkg.go.dev/builtin#string)

## UriSettings
    
    
    type UriSettings struct {
    
    	// Specifications related to the `Checkout` URL. The `UriTemplate` is
    	// of the form `https://www.mystore.com/checkout?item_id={id}`
    	// where `{id}` will be automatically replaced with [offer_id]
    	// (https://developers.google.com/shopping-content/reference/rest/v2.1/products#Product.FIELDS.offer_id)
    	// attribute from the merchant account
    	//
    	// Types that are valid to be assigned to UriTemplate:
    	//
    	//	*UriSettings_CheckoutUriTemplate
    	//	*UriSettings_CartUriTemplate
    	UriTemplate isUriSettings_UriTemplate `protobuf_oneof:"uri_template"`
    	// contains filtered or unexported fields
    }

URL settings for cart or checkout URL.

### func (*UriSettings) Descriptor 
    
    
    func (*UriSettings) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UriSettings.ProtoReflect.Descriptor instead.

### func (*UriSettings) GetCartUriTemplate 
    
    
    func (x *UriSettings) GetCartUriTemplate() [string](https://pkg.go.dev/builtin#string)

### func (*UriSettings) GetCheckoutUriTemplate 
    
    
    func (x *UriSettings) GetCheckoutUriTemplate() [string](https://pkg.go.dev/builtin#string)

### func (*UriSettings) GetUriTemplate 
    
    
    func (x *UriSettings) GetUriTemplate() isUriSettings_UriTemplate

### func (*UriSettings) ProtoMessage 
    
    
    func (*UriSettings) ProtoMessage()

### func (*UriSettings) ProtoReflect 
    
    
    func (x *UriSettings) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UriSettings) Reset 
    
    
    func (x *UriSettings) Reset()

### func (*UriSettings) String 
    
    
    func (x *UriSettings) String() [string](https://pkg.go.dev/builtin#string)

## UriSettings_CartUriTemplate
    
    
    type UriSettings_CartUriTemplate struct {
    	// Cart URL template. When the placeholders are expanded will redirect the
    	// buyer to the cart page on the merchant website with the selected
    	// item in cart. For more details, check the [help center
    	// doc](https://support.google.com/merchants/answer/13945960#method1&zippy=%2Cproduct-level-url-formatting%2Caccount-level-url-formatting)
    	CartUriTemplate [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=cart_uri_template,json=cartUriTemplate,proto3,oneof"`
    }

## UriSettings_CheckoutUriTemplate
    
    
    type UriSettings_CheckoutUriTemplate struct {
    	// Checkout URL template. When the placeholders are expanded will redirect
    	// the buyer to the merchant checkout page with the item in the cart. For
    	// more details, check the [help center
    	// doc](https://support.google.com/merchants/answer/13945960#method1&zippy=%2Cproduct-level-url-formatting%2Caccount-level-url-formatting)
    	CheckoutUriTemplate [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=checkout_uri_template,json=checkoutUriTemplate,proto3,oneof"`
    }

## User
    
    
    type User struct {
    
    	// Identifier. The resource name of the user.
    	// Format: `accounts/{account}/user/{email}`
    	//
    	// Use `me` to refer to your own email address, for example
    	// `accounts/{account}/users/me`.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Output only. The state of the user.
    	State User_State `protobuf:"varint,2,opt,name=state,proto3,enum=google.shopping.merchant.accounts.v1beta.User_State" json:"state,omitempty"`
    	// Optional. The [access
    	// rights](https://support.google.com/merchants/answer/12160472?sjid=6789834943175119429-EU#accesstypes)
    	// the user has.
    	AccessRights []AccessRight `protobuf:"varint,4,rep,packed,name=access_rights,json=accessRights,proto3,enum=google.shopping.merchant.accounts.v1beta.AccessRight" json:"access_rights,omitempty"`
    	// contains filtered or unexported fields
    }

A [user](https://support.google.com/merchants/answer/12160472).

### func (*User) Descriptor 
    
    
    func (*User) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use User.ProtoReflect.Descriptor instead.

### func (*User) GetAccessRights 
    
    
    func (x *User) GetAccessRights() []AccessRight

### func (*User) GetName 
    
    
    func (x *User) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*User) GetState 
    
    
    func (x *User) GetState() User_State

### func (*User) ProtoMessage 
    
    
    func (*User) ProtoMessage()

### func (*User) ProtoReflect 
    
    
    func (x *User) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*User) Reset 
    
    
    func (x *User) Reset()

### func (*User) String 
    
    
    func (x *User) String() [string](https://pkg.go.dev/builtin#string)

## UserServiceClient
    
    
    type UserServiceClient interface {
    	// Retrieves a Merchant Center account user.
    	GetUser(ctx context.Context, in *GetUserRequest, opts ...grpc.CallOption) (*User, [error](https://pkg.go.dev/builtin#error))
    	// Creates a Merchant Center account user. Executing this method requires
    	// admin access.
    	CreateUser(ctx context.Context, in *CreateUserRequest, opts ...grpc.CallOption) (*User, [error](https://pkg.go.dev/builtin#error))
    	// Deletes a Merchant Center account user. Executing this method requires
    	// admin access.
    	DeleteUser(ctx context.Context, in *DeleteUserRequest, opts ...grpc.CallOption) (*emptypb.Empty, [error](https://pkg.go.dev/builtin#error))
    	// Updates a Merchant Center account user. Executing this method requires
    	// admin access.
    	UpdateUser(ctx context.Context, in *UpdateUserRequest, opts ...grpc.CallOption) (*User, [error](https://pkg.go.dev/builtin#error))
    	// Lists all users of a Merchant Center account.
    	ListUsers(ctx context.Context, in *ListUsersRequest, opts ...grpc.CallOption) (*ListUsersResponse, [error](https://pkg.go.dev/builtin#error))
    }

UserServiceClient is the client API for UserService service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

### func NewUserServiceClient 
    
    
    func NewUserServiceClient(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) UserServiceClient

## UserServiceServer
    
    
    type UserServiceServer interface {
    	// Retrieves a Merchant Center account user.
    	GetUser(context.Context, *GetUserRequest) (*User, [error](https://pkg.go.dev/builtin#error))
    	// Creates a Merchant Center account user. Executing this method requires
    	// admin access.
    	CreateUser(context.Context, *CreateUserRequest) (*User, [error](https://pkg.go.dev/builtin#error))
    	// Deletes a Merchant Center account user. Executing this method requires
    	// admin access.
    	DeleteUser(context.Context, *DeleteUserRequest) (*emptypb.Empty, [error](https://pkg.go.dev/builtin#error))
    	// Updates a Merchant Center account user. Executing this method requires
    	// admin access.
    	UpdateUser(context.Context, *UpdateUserRequest) (*User, [error](https://pkg.go.dev/builtin#error))
    	// Lists all users of a Merchant Center account.
    	ListUsers(context.Context, *ListUsersRequest) (*ListUsersResponse, [error](https://pkg.go.dev/builtin#error))
    }

UserServiceServer is the server API for UserService service. All implementations should embed UnimplementedUserServiceServer for forward compatibility

## User_State
    
    
    type User_State [int32](https://pkg.go.dev/builtin#int32)

The possible states of a user.

### User_STATE_UNSPECIFIED, User_PENDING, User_VERIFIED
    
    
    const (
    	// Default value. This value is unused.
    	User_STATE_UNSPECIFIED User_State = 0
    	// The user is pending confirmation. In this state, the user first needs to
    	// accept the invitation before performing other actions.
    	User_PENDING User_State = 1
    	// The user is verified.
    	User_VERIFIED User_State = 2
    )

### func (User_State) Descriptor 
    
    
    func (User_State) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (User_State) Enum 
    
    
    func (x User_State) Enum() *User_State

### func (User_State) EnumDescriptor 
    
    
    func (User_State) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use User_State.Descriptor instead.

### func (User_State) Number 
    
    
    func (x User_State) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (User_State) String 
    
    
    func (x User_State) String() [string](https://pkg.go.dev/builtin#string)

### func (User_State) Type 
    
    
    func (User_State) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Value
    
    
    type Value struct {
    
    	// If true, then the product can't be shipped. Must be true when set, can only
    	// be set if all other fields are not set.
    	NoShipping *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,1,opt,name=no_shipping,json=noShipping,proto3,oneof" json:"no_shipping,omitempty"`
    	// A flat rate. Can only be set if all other fields are not set.
    	FlatRate *typepb.Price `protobuf:"bytes,2,opt,name=flat_rate,json=flatRate,proto3,oneof" json:"flat_rate,omitempty"`
    	// A percentage of the price represented as a number in decimal notation
    	// (For example, `"5.4"`). Can only be set if all other fields are not
    	// set.
    	PricePercentage *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=price_percentage,json=pricePercentage,proto3,oneof" json:"price_percentage,omitempty"`
    	// The name of a carrier rate referring to a carrier rate defined in the
    	// same rate group. Can only be set if all other fields are not set.
    	CarrierRate *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=carrier_rate,json=carrierRate,proto3,oneof" json:"carrier_rate,omitempty"`
    	// The name of a subtable. Can only be set in table cells (For example, not
    	// for single values), and only if all other fields are not set.
    	Subtable *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=subtable,proto3,oneof" json:"subtable,omitempty"`
    	// contains filtered or unexported fields
    }

The single value of a rate group or the value of a rate group table's cell. Exactly one of `no_shipping`, `flat_rate`, `price_percentage`, `carrier_rateName`, `subtable_name` must be set.

### func (*Value) Descriptor 
    
    
    func (*Value) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Value.ProtoReflect.Descriptor instead.

### func (*Value) GetCarrierRate 
    
    
    func (x *Value) GetCarrierRate() [string](https://pkg.go.dev/builtin#string)

### func (*Value) GetFlatRate 
    
    
    func (x *Value) GetFlatRate() *[typepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/type/typepb).[Price](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/type/typepb#cloud_google_com_go_shopping_type_typepb_Price)

### func (*Value) GetNoShipping 
    
    
    func (x *Value) GetNoShipping() [bool](https://pkg.go.dev/builtin#bool)

### func (*Value) GetPricePercentage 
    
    
    func (x *Value) GetPricePercentage() [string](https://pkg.go.dev/builtin#string)

### func (*Value) GetSubtable 
    
    
    func (x *Value) GetSubtable() [string](https://pkg.go.dev/builtin#string)

### func (*Value) ProtoMessage 
    
    
    func (*Value) ProtoMessage()

### func (*Value) ProtoReflect 
    
    
    func (x *Value) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Value) Reset 
    
    
    func (x *Value) Reset()

### func (*Value) String 
    
    
    func (x *Value) String() [string](https://pkg.go.dev/builtin#string)

## VerificationMailSettings
    
    
    type VerificationMailSettings struct {
    
    	// Optional. Mode of the verification mail. If not set, the default is
    	// `SEND_VERIFICATION_MAIL`.
    	VerificationMailMode VerificationMailSettings_VerificationMailMode `protobuf:"varint,1,opt,name=verification_mail_mode,json=verificationMailMode,proto3,enum=google.shopping.merchant.accounts.v1beta.VerificationMailSettings_VerificationMailMode" json:"verification_mail_mode,omitempty"`
    	// contains filtered or unexported fields
    }

Settings related to the verification email that is sent after adding a user.

### func (*VerificationMailSettings) Descriptor 
    
    
    func (*VerificationMailSettings) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use VerificationMailSettings.ProtoReflect.Descriptor instead.

### func (*VerificationMailSettings) GetVerificationMailMode 
    
    
    func (x *VerificationMailSettings) GetVerificationMailMode() VerificationMailSettings_VerificationMailMode

### func (*VerificationMailSettings) ProtoMessage 
    
    
    func (*VerificationMailSettings) ProtoMessage()

### func (*VerificationMailSettings) ProtoReflect 
    
    
    func (x *VerificationMailSettings) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*VerificationMailSettings) Reset 
    
    
    func (x *VerificationMailSettings) Reset()

### func (*VerificationMailSettings) String 
    
    
    func (x *VerificationMailSettings) String() [string](https://pkg.go.dev/builtin#string)

## VerificationMailSettings_VerificationMailMode
    
    
    type VerificationMailSettings_VerificationMailMode [int32](https://pkg.go.dev/builtin#int32)

The different configuration options for sending a verification email when adding a user.

### VerificationMailSettings_VERIFICATION_MAIL_MODE_UNSPECIFIED, VerificationMailSettings_SEND_VERIFICATION_MAIL, VerificationMailSettings_SUPPRESS_VERIFICATION_MAIL
    
    
    const (
    	// Default first member of every enum. Do not use.
    	VerificationMailSettings_VERIFICATION_MAIL_MODE_UNSPECIFIED VerificationMailSettings_VerificationMailMode = 0
    	// An invitation email is sent to the user added shortly after.
    	VerificationMailSettings_SEND_VERIFICATION_MAIL VerificationMailSettings_VerificationMailMode = 1
    	// No invitation email is sent. This can be useful if the user is
    	// expected to accept the invitation through the API without needing
    	// another notification.
    	VerificationMailSettings_SUPPRESS_VERIFICATION_MAIL VerificationMailSettings_VerificationMailMode = 2
    )

### func (VerificationMailSettings_VerificationMailMode) Descriptor 
    
    
    func (VerificationMailSettings_VerificationMailMode) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (VerificationMailSettings_VerificationMailMode) Enum 
    
    
    func (x VerificationMailSettings_VerificationMailMode) Enum() *VerificationMailSettings_VerificationMailMode

### func (VerificationMailSettings_VerificationMailMode) EnumDescriptor 
    
    
    func (VerificationMailSettings_VerificationMailMode) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use VerificationMailSettings_VerificationMailMode.Descriptor instead.

### func (VerificationMailSettings_VerificationMailMode) Number 
    
    
    func (x VerificationMailSettings_VerificationMailMode) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (VerificationMailSettings_VerificationMailMode) String 
    
    
    func (x VerificationMailSettings_VerificationMailMode) String() [string](https://pkg.go.dev/builtin#string)

### func (VerificationMailSettings_VerificationMailMode) Type 
    
    
    func (VerificationMailSettings_VerificationMailMode) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Warehouse
    
    
    type Warehouse struct {
    
    	// Required. The name of the warehouse. Must be unique within account.
    	Name *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3,oneof" json:"name,omitempty"`
    	// Required. Shipping address of the warehouse.
    	ShippingAddress *Address `protobuf:"bytes,2,opt,name=shipping_address,json=shippingAddress,proto3,oneof" json:"shipping_address,omitempty"`
    	// Required. The latest time of day that an order can be accepted and begin
    	// processing. Later orders will be processed in the next day. The time is
    	// based on the warehouse postal code.
    	CutoffTime *WarehouseCutoffTime `protobuf:"bytes,3,opt,name=cutoff_time,json=cutoffTime,proto3,oneof" json:"cutoff_time,omitempty"`
    	// Required. The number of days it takes for this warehouse to pack up and
    	// ship an item. This is on the warehouse level, but can be overridden on the
    	// offer level based on the attributes of an item.
    	HandlingDays *[int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,4,opt,name=handling_days,json=handlingDays,proto3,oneof" json:"handling_days,omitempty"`
    	// Business days of the warehouse.
    	// If not set, will be Monday to Friday by default.
    	BusinessDayConfig *BusinessDayConfig `protobuf:"bytes,5,opt,name=business_day_config,json=businessDayConfig,proto3,oneof" json:"business_day_config,omitempty"`
    	// contains filtered or unexported fields
    }

A fulfillment warehouse, which stores and handles inventory. Next tag: 7

### func (*Warehouse) Descriptor 
    
    
    func (*Warehouse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Warehouse.ProtoReflect.Descriptor instead.

### func (*Warehouse) GetBusinessDayConfig 
    
    
    func (x *Warehouse) GetBusinessDayConfig() *BusinessDayConfig

### func (*Warehouse) GetCutoffTime 
    
    
    func (x *Warehouse) GetCutoffTime() *WarehouseCutoffTime

### func (*Warehouse) GetHandlingDays 
    
    
    func (x *Warehouse) GetHandlingDays() [int64](https://pkg.go.dev/builtin#int64)

### func (*Warehouse) GetName 
    
    
    func (x *Warehouse) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Warehouse) GetShippingAddress 
    
    
    func (x *Warehouse) GetShippingAddress() *Address

### func (*Warehouse) ProtoMessage 
    
    
    func (*Warehouse) ProtoMessage()

### func (*Warehouse) ProtoReflect 
    
    
    func (x *Warehouse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Warehouse) Reset 
    
    
    func (x *Warehouse) Reset()

### func (*Warehouse) String 
    
    
    func (x *Warehouse) String() [string](https://pkg.go.dev/builtin#string)

## WarehouseBasedDeliveryTime
    
    
    type WarehouseBasedDeliveryTime struct {
    
    	// Required. Carrier, such as `"UPS"` or `"Fedex"`.
    	Carrier *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=carrier,proto3,oneof" json:"carrier,omitempty"`
    	// Required. Carrier service, such as `"ground"` or `"2 days"`. The name of
    	// the service must be in the eddSupportedServices list.
    	CarrierService *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=carrier_service,json=carrierService,proto3,oneof" json:"carrier_service,omitempty"`
    	// Required. Warehouse name. This should match
    	// [warehouse][ShippingSetting.warehouses.name]
    	Warehouse *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=warehouse,proto3,oneof" json:"warehouse,omitempty"`
    	// contains filtered or unexported fields
    }

Indicates that the delivery time should be calculated per warehouse (shipping origin location) based on the settings of the selected carrier. When set, no other transit time related field in `delivery_time` should be set.

### func (*WarehouseBasedDeliveryTime) Descriptor 
    
    
    func (*WarehouseBasedDeliveryTime) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use WarehouseBasedDeliveryTime.ProtoReflect.Descriptor instead.

### func (*WarehouseBasedDeliveryTime) GetCarrier 
    
    
    func (x *WarehouseBasedDeliveryTime) GetCarrier() [string](https://pkg.go.dev/builtin#string)

### func (*WarehouseBasedDeliveryTime) GetCarrierService 
    
    
    func (x *WarehouseBasedDeliveryTime) GetCarrierService() [string](https://pkg.go.dev/builtin#string)

### func (*WarehouseBasedDeliveryTime) GetWarehouse 
    
    
    func (x *WarehouseBasedDeliveryTime) GetWarehouse() [string](https://pkg.go.dev/builtin#string)

### func (*WarehouseBasedDeliveryTime) ProtoMessage 
    
    
    func (*WarehouseBasedDeliveryTime) ProtoMessage()

### func (*WarehouseBasedDeliveryTime) ProtoReflect 
    
    
    func (x *WarehouseBasedDeliveryTime) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*WarehouseBasedDeliveryTime) Reset 
    
    
    func (x *WarehouseBasedDeliveryTime) Reset()

### func (*WarehouseBasedDeliveryTime) String 
    
    
    func (x *WarehouseBasedDeliveryTime) String() [string](https://pkg.go.dev/builtin#string)

## WarehouseCutoffTime
    
    
    type WarehouseCutoffTime struct {
    
    	// Required. Hour of the cutoff time until which an order has to be placed to
    	// be processed in the same day by the warehouse. Hour is based on the
    	// timezone of warehouse.
    	Hour *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,1,opt,name=hour,proto3,oneof" json:"hour,omitempty"`
    	// Required. Minute of the cutoff time until which an order has to be placed
    	// to be processed in the same day by the warehouse. Minute is based on the
    	// timezone of warehouse.
    	Minute *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=minute,proto3,oneof" json:"minute,omitempty"`
    	// contains filtered or unexported fields
    }

The latest time of day that an order can be accepted and begin processing. Later orders will be processed in the next day. The time is based on the warehouse postal code.

### func (*WarehouseCutoffTime) Descriptor 
    
    
    func (*WarehouseCutoffTime) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use WarehouseCutoffTime.ProtoReflect.Descriptor instead.

### func (*WarehouseCutoffTime) GetHour 
    
    
    func (x *WarehouseCutoffTime) GetHour() [int32](https://pkg.go.dev/builtin#int32)

### func (*WarehouseCutoffTime) GetMinute 
    
    
    func (x *WarehouseCutoffTime) GetMinute() [int32](https://pkg.go.dev/builtin#int32)

### func (*WarehouseCutoffTime) ProtoMessage 
    
    
    func (*WarehouseCutoffTime) ProtoMessage()

### func (*WarehouseCutoffTime) ProtoReflect 
    
    
    func (x *WarehouseCutoffTime) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*WarehouseCutoffTime) Reset 
    
    
    func (x *WarehouseCutoffTime) Reset()

### func (*WarehouseCutoffTime) String 
    
    
    func (x *WarehouseCutoffTime) String() [string](https://pkg.go.dev/builtin#string)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
