---
url: https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants
title: REST Resource: projects.tenants \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:52:54.671109+00:00
---

# REST Resource: projects.tenants  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Reference ](https://docs.cloud.google.com/identity-platform/docs/apis)



Send feedback 

#  REST Resource: projects.tenants Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Tenant
    * JSON representation
  * HashConfig
    * JSON representation
  * HashAlgorithm
  * MultiFactorAuthConfig
    * JSON representation
  * State
  * Provider
  * ProviderConfig
    * JSON representation
  * TotpMfaProviderConfig
    * JSON representation
  * MfaState
  * Inheritance
    * JSON representation
  * RecaptchaConfig
    * JSON representation
  * RecaptchaProviderEnforcementState
  * RecaptchaManagedRule
    * JSON representation
  * RecaptchaAction
  * RecaptchaKey
    * JSON representation
  * RecaptchaKeyClientType
  * RecaptchaTollFraudManagedRule
    * JSON representation
  * RecaptchaAction
  * SmsRegionConfig
    * JSON representation
  * AllowByDefault
    * JSON representation
  * AllowlistOnly
    * JSON representation
  * MonitoringConfig
    * JSON representation
  * RequestLogging
    * JSON representation
  * PasswordPolicyConfig
    * JSON representation
  * PasswordPolicyEnforcementState
  * PasswordPolicyVersion
    * JSON representation
  * CustomStrengthOptions
    * JSON representation
  * EmailPrivacyConfig
    * JSON representation
  * ClientPermissionConfig
    * JSON representation
  * ClientPermissions
    * JSON representation
  * MobileLinksConfig
    * JSON representation
  * Domain
  * Methods



## Resource: Tenant

A Tenant contains configuration for the tenant in a multi-tenant project.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "allowPasswordSignup": boolean,
      "enableEmailLinkSignin": boolean,
      "disableAuth": boolean,
      "hashConfig": {
        object ([HashConfig](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#HashConfig))
      },
      "enableAnonymousUser": boolean,
      "mfaConfig": {
        object ([MultiFactorAuthConfig](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#MultiFactorAuthConfig))
      },
      "testPhoneNumbers": {
        string: string,
        ...
      },
      "inheritance": {
        object ([Inheritance](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#Inheritance))
      },
      "recaptchaConfig": {
        object ([RecaptchaConfig](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#RecaptchaConfig))
      },
      "smsRegionConfig": {
        object ([SmsRegionConfig](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#SmsRegionConfig))
      },
      "autodeleteAnonymousUsers": boolean,
      "monitoring": {
        object ([MonitoringConfig](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#MonitoringConfig))
      },
      "passwordPolicyConfig": {
        object ([PasswordPolicyConfig](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#PasswordPolicyConfig))
      },
      "emailPrivacyConfig": {
        object ([EmailPrivacyConfig](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#EmailPrivacyConfig))
      },
      "client": {
        object ([ClientPermissionConfig](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#ClientPermissionConfig))
      },
      "mobileLinksConfig": {
        object ([MobileLinksConfig](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#MobileLinksConfig))
      }
    }  
  
Fields  
---  
`name` |  `string` Output only. Resource name of a tenant. For example: "projects/{project-id}/tenants/{tenant-id}"  
`displayName` |  `string` Display name of the tenant.  
`allowPasswordSignup` |  `boolean` Whether to allow email/password user authentication.  
`enableEmailLinkSignin` |  `boolean` Whether to enable email link user authentication.  
`disableAuth` |  `boolean` Whether authentication is disabled for the tenant. If true, the users under the disabled tenant are not allowed to sign-in. Admins of the disabled tenant are not able to manage its users.  
`hashConfig` |  `object (`[HashConfig](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#HashConfig)`)` Output only. Hash config information of a tenant for display on Pantheon. This can only be displayed on Pantheon to avoid the sensitive information to get accidentally leaked. Only returned in tenants.get response to restrict reading of this information. Requires firebaseauth.configs.getHashConfig permission on the agent project for returning this field.  
`enableAnonymousUser` |  `boolean` Whether to enable anonymous user authentication.  
`mfaConfig` |  `object (`[MultiFactorAuthConfig](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#MultiFactorAuthConfig)`)` The tenant-level configuration of MFA options.  
`testPhoneNumbers` |  `map (key: string, value: string)` A map of <test phone number, fake code> pairs that can be used for MFA. The phone number should be in E.164 format (<https://www.itu.int/rec/T-REC-E.164/>) and a maximum of 10 pairs can be added (error will be thrown once exceeded).An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`inheritance` |  `object (`[Inheritance](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#Inheritance)`)` Specify the settings that the tenant could inherit.  
`recaptchaConfig` |  `object (`[RecaptchaConfig](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#RecaptchaConfig)`)` The tenant-level reCAPTCHA config.  
`smsRegionConfig` |  `object (`[SmsRegionConfig](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#SmsRegionConfig)`)` Configures which regions are enabled for SMS verification code sending.  
`autodeleteAnonymousUsers` |  `boolean` Whether anonymous users will be auto-deleted after a period of 30 days.  
`monitoring` |  `object (`[MonitoringConfig](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#MonitoringConfig)`)` Configuration related to monitoring project activity.  
`passwordPolicyConfig` |  `object (`[PasswordPolicyConfig](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#PasswordPolicyConfig)`)` The tenant-level password policy config  
`emailPrivacyConfig` |  `object (`[EmailPrivacyConfig](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#EmailPrivacyConfig)`)` Configuration for settings related to email privacy and public visibility.  
`client` |  `object (`[ClientPermissionConfig](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#ClientPermissionConfig)`)` Options related to how clients making requests on behalf of a project should be configured.  
`mobileLinksConfig  
**(deprecated)**` |  `object (`[MobileLinksConfig](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#MobileLinksConfig)`)` This item is deprecated!Optional. Deprecated. Never launched. Configuration for settings related to univeral links (iOS) and app links (Android).  
  
## HashConfig

History information of the hash algorithm and key. Different accounts' passwords may be generated by different version.

JSON representation  
---  
      
    
    {
      "algorithm": enum ([HashAlgorithm](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#HashAlgorithm)),
      "signerKey": string,
      "saltSeparator": string,
      "rounds": integer,
      "memoryCost": integer
    }  
  
Fields  
---  
`algorithm` |  `enum (`[HashAlgorithm](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#HashAlgorithm)`)` Output only. Different password hash algorithms used in Identity Toolkit.  
`signerKey` |  `string` Output only. Signer key in base64.  
`saltSeparator` |  `string` Output only. Non-printable character to be inserted between the salt and plain text password in base64.  
`rounds` |  `integer` Output only. How many rounds for hash calculation. Used by scrypt and other similar password derivation algorithms.  
`memoryCost` |  `integer` Output only. Memory cost for hash calculation. Used by scrypt and other similar password derivation algorithms. See <https://tools.ietf.org/html/rfc7914> for explanation of field.  
  
## HashAlgorithm

Different password hash algorithms used in Identity Toolkit.

Enums  
---  
`HASH_ALGORITHM_UNSPECIFIED` | Default value. Do not use.  
`HMAC_SHA256` | HMAC_SHA256  
`HMAC_SHA1` | HMAC_SHA1  
`HMAC_MD5` | HMAC_MD5  
`SCRYPT` | SCRYPT  
`PBKDF_SHA1` | PBKDF_SHA1  
`MD5` | MD5  
`HMAC_SHA512` | HMAC_SHA512  
`SHA1` | SHA1  
`BCRYPT` | BCRYPT  
`PBKDF2_SHA256` | PBKDF2_SHA256  
`SHA256` | SHA256  
`SHA512` | SHA512  
`STANDARD_SCRYPT` | STANDARD_SCRYPT  
  
## MultiFactorAuthConfig

Options related to MultiFactor Authentication for the project.

JSON representation  
---  
      
    
    {
      "state": enum ([State](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#State)),
      "enabledProviders": [
        enum ([Provider](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#Provider))
      ],
      "providerConfigs": [
        {
          object ([ProviderConfig](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#ProviderConfig))
        }
      ]
    }  
  
Fields  
---  
`state` |  `enum (`[State](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#State)`)` Whether MultiFactor Authentication has been enabled for this project.  
`enabledProviders[]` |  `enum (`[Provider](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#Provider)`)` A list of usable second factors for this project.  
`providerConfigs[]` |  `object (`[ProviderConfig](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#ProviderConfig)`)` A list of usable second factors for this project along with their configurations. This field does not support phone based MFA, for that use the 'enabledProviders' field.  
  
## State

Whether MultiFactor Authentication has been enabled for this project.

Enums  
---  
`STATE_UNSPECIFIED` | Illegal State, should not be used.  
`DISABLED` | Multi-factor authentication cannot be used for this project  
`ENABLED` | Multi-factor authentication can be used for this project  
`MANDATORY` | Multi-factor authentication is required for this project. Users from this project must authenticate with the second factor.  
  
## Provider

A list of usable second factors for this project.

Enums  
---  
`PROVIDER_UNSPECIFIED` | Illegal Provider, should not be used  
`PHONE_SMS` | SMS is enabled as a second factor for this project.  
  
## ProviderConfig

ProviderConfig describes the supported MFA providers along with their configurations.

JSON representation  
---  
      
    
    {
      "state": enum ([MfaState](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#MfaState)),
    
      // Union field mfa_provider_config can be only one of the following:
      "totpProviderConfig": {
        object ([TotpMfaProviderConfig](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#TotpMfaProviderConfig))
      }
      // End of list of possible types for union field mfa_provider_config.
    }  
  
Fields  
---  
`state` |  `enum (`[MfaState](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#MfaState)`)` Describes the state of the MultiFactor Authentication type.  
Union field `mfa_provider_config`.`mfa_provider_config` can be only one of the following:  
`totpProviderConfig` |  `object (`[TotpMfaProviderConfig](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#TotpMfaProviderConfig)`)` TOTP MFA provider config for this project.  
  
## TotpMfaProviderConfig

TotpMFAProviderConfig represents the TOTP based MFA provider.

JSON representation  
---  
      
    
    {
      "adjacentIntervals": integer
    }  
  
Fields  
---  
`adjacentIntervals` |  `integer` The allowed number of adjacent intervals that will be used for verification to avoid clock skew.  
  
## MfaState

Whether MultiFactor Authentication has been enabled for this project.

Enums  
---  
`MFA_STATE_UNSPECIFIED` | Illegal State, should not be used.  
`DISABLED` | Multi-factor authentication cannot be used for this project.  
`ENABLED` | Multi-factor authentication can be used for this project.  
`MANDATORY` | Multi-factor authentication is required for this project. Users from this project must authenticate with the second factor.  
  
## Inheritance

Settings that the tenants will inherit from project level.

JSON representation  
---  
      
    
    {
      "emailSendingConfig": boolean
    }  
  
Fields  
---  
`emailSendingConfig` |  `boolean` Whether to allow the tenant to inherit custom domains, email templates, and custom SMTP settings. If true, email sent from tenant will follow the project level email sending configurations. If false (by default), emails will go with the default settings with no customizations.  
  
## RecaptchaConfig

The reCAPTCHA Enterprise integration config.

JSON representation  
---  
      
    
    {
      "managedRules": [
        {
          object ([RecaptchaManagedRule](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#RecaptchaManagedRule))
        }
      ],
      "recaptchaKeys": [
        {
          object ([RecaptchaKey](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#RecaptchaKey))
        }
      ],
      "tollFraudManagedRules": [
        {
          object ([RecaptchaTollFraudManagedRule](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#RecaptchaTollFraudManagedRule))
        }
      ],
      "emailPasswordEnforcementState": enum ([RecaptchaProviderEnforcementState](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#RecaptchaProviderEnforcementState)),
      "useAccountDefender": boolean,
      "phoneEnforcementState": enum ([RecaptchaProviderEnforcementState](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#RecaptchaProviderEnforcementState)),
      "useSmsBotScore": boolean,
      "useSmsTollFraudProtection": boolean
    }  
  
Fields  
---  
`managedRules[]` |  `object (`[RecaptchaManagedRule](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#RecaptchaManagedRule)`)` The managed rules for authentication action based on reCAPTCHA scores. The rules are shared across providers for a given tenant project.  
`recaptchaKeys[]` |  `object (`[RecaptchaKey](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#RecaptchaKey)`)` The reCAPTCHA keys.  
`tollFraudManagedRules[]` |  `object (`[RecaptchaTollFraudManagedRule](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#RecaptchaTollFraudManagedRule)`)` The managed rules for the authentication action based on reCAPTCHA toll fraud risk scores. Toll fraud managed rules will only take effect when the phoneEnforcementState is AUDIT or ENFORCE and useSmsTollFraudProtection is true.  
`emailPasswordEnforcementState` |  `enum (`[RecaptchaProviderEnforcementState](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#RecaptchaProviderEnforcementState)`)` The reCAPTCHA config for email/password provider, containing the enforcement status. The email/password provider contains all email related user flows protected by reCAPTCHA.  
`useAccountDefender` |  `boolean` Whether to use the account defender for reCAPTCHA assessment. Defaults to `false`.  
`phoneEnforcementState` |  `enum (`[RecaptchaProviderEnforcementState](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#RecaptchaProviderEnforcementState)`)` The reCAPTCHA config for phone provider, containing the enforcement status. The phone provider contains all SMS related user flows protected by reCAPTCHA.  
`useSmsBotScore` |  `boolean` Whether to use the rCE bot score for reCAPTCHA phone provider. Can only be true when the phoneEnforcementState is AUDIT or ENFORCE.  
`useSmsTollFraudProtection` |  `boolean` Whether to use the rCE sms toll fraud protection risk score for reCAPTCHA phone provider. Can only be true when the phoneEnforcementState is AUDIT or ENFORCE.  
  
## RecaptchaProviderEnforcementState

Enforcement states for reCAPTCHA protection.

Enums  
---  
`RECAPTCHA_PROVIDER_ENFORCEMENT_STATE_UNSPECIFIED` | Enforcement state has not been set.  
`OFF` | Unenforced.  
`AUDIT` | reCAPTCHA assessment is created, result is not used to enforce.  
`ENFORCE` | reCAPTCHA assessment is created, result is used to enforce.  
  
## RecaptchaManagedRule

The config for a reCAPTCHA managed rule. Models a single interval [startScore, endScore]. The startScore is implicit. It is either the closest smaller endScore (if one is available) or 0. Intervals in aggregate span [0, 1] without overlapping.

JSON representation  
---  
      
    
    {
      "endScore": number,
      "action": enum ([RecaptchaAction](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#RecaptchaAction))
    }  
  
Fields  
---  
`endScore` |  `number` The end score (inclusive) of the score range for an action. Must be a value between 0.0 and 1.0, at 11 discrete values; e.g. 0, 0.1, 0.2, 0.3, ... 0.9, 1.0. A score of 0.0 indicates the riskiest request (likely a bot), whereas 1.0 indicates the safest request (likely a human). See <https://cloud.google.com/recaptcha-enterprise/docs/interpret-assessment>.  
`action` |  `enum (`[RecaptchaAction](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#RecaptchaAction)`)` The action taken if the reCAPTCHA score of a request is within the interval [startScore, endScore].  
  
## RecaptchaAction

The actions for reCAPTCHA-protected requests.

Enums  
---  
`RECAPTCHA_ACTION_UNSPECIFIED` | The reCAPTCHA action is not specified.  
`BLOCK` | The reCAPTCHA-protected request will be blocked.  
  
## RecaptchaKey

The reCAPTCHA key config. reCAPTCHA Enterprise offers different keys for different client platforms.

JSON representation  
---  
      
    
    {
      "key": string,
      "type": enum ([RecaptchaKeyClientType](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#RecaptchaKeyClientType))
    }  
  
Fields  
---  
`key` |  `string` The reCAPTCHA Enterprise key resource name, e.g. "projects/{project}/keys/{key}"  
`type` |  `enum (`[RecaptchaKeyClientType](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#RecaptchaKeyClientType)`)` The client's platform type.  
  
## RecaptchaKeyClientType

The different clients that reCAPTCHA Enterprise keys support.

Enums  
---  
`CLIENT_TYPE_UNSPECIFIED` | Client type is not specified.  
`WEB` | Client type is web.  
`IOS` | Client type is iOS.  
`ANDROID` | Client type is Android.  
  
## RecaptchaTollFraudManagedRule

The config for a reCAPTCHA toll fraud assessment managed rule. Models a single interval [startScore, endScore]. The endScore is implicit. It is either the closest smaller endScore (if one is available) or 0. Intervals in aggregate span [0, 1] without overlapping.

JSON representation  
---  
      
    
    {
      "startScore": number,
      "action": enum ([RecaptchaAction](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#RecaptchaAction_1))
    }  
  
Fields  
---  
`startScore` |  `number` The start score (inclusive) for an action. Must be a value between 0.0 and 1.0, at 11 discrete values; e.g. 0, 0.1, 0.2, 0.3, ... 0.9, 1.0. A score of 0.0 indicates the safest request (likely legitimate), whereas 1.0 indicates the riskiest request (likely toll fraud). See <https://cloud.google.com/recaptcha-enterprise/docs/sms-fraud-detection#create-assessment-sms>.  
`action` |  `enum (`[RecaptchaAction](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#RecaptchaAction_1)`)` The action taken if the reCAPTCHA score of a request is within the interval [startScore, endScore].  
  
## RecaptchaAction

Defaults to RECAPTCHA_ACTION_UNSPECIFIED

Enums  
---  
`RECAPTCHA_ACTION_UNSPECIFIED` | The reCAPTCHA action is not specified.  
`BLOCK` | The reCAPTCHA-protected request will be blocked.  
  
## SmsRegionConfig

Configures the regions where users are allowed to send verification SMS for the project or tenant. This is based on the calling code of the destination phone number.

JSON representation  
---  
      
    
    {
    
      // Union field sms_region_policy can be only one of the following:
      "allowByDefault": {
        object ([AllowByDefault](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#AllowByDefault))
      },
      "allowlistOnly": {
        object ([AllowlistOnly](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#AllowlistOnly))
      }
      // End of list of possible types for union field sms_region_policy.
    }  
  
Fields  
---  
Union field `sms_region_policy`. A policy for where users are allowed to send verification SMS. This can be to allow all regions by default or to allow regions only by explicit allowlist. `sms_region_policy` can be only one of the following:  
`allowByDefault` |  `object (`[AllowByDefault](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#AllowByDefault)`)` A policy of allowing SMS to every region by default and adding disallowed regions to a disallow list.  
`allowlistOnly` |  `object (`[AllowlistOnly](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#AllowlistOnly)`)` A policy of only allowing regions by explicitly adding them to an allowlist.  
  
## AllowByDefault

Defines a policy of allowing every region by default and adding disallowed regions to a disallow list.

JSON representation  
---  
      
    
    {
      "disallowedRegions": [
        string
      ]
    }  
  
Fields  
---  
`disallowedRegions[]` |  `string` Two letter unicode region codes to disallow as defined by <https://cldr.unicode.org/> The full list of these region codes is here: <https://github.com/unicode-cldr/cldr-localenames-full/blob/master/main/en/territories.json>  
  
## AllowlistOnly

Defines a policy of only allowing regions by explicitly adding them to an allowlist.

JSON representation  
---  
      
    
    {
      "allowedRegions": [
        string
      ]
    }  
  
Fields  
---  
`allowedRegions[]` |  `string` Two letter unicode region codes to allow as defined by <https://cldr.unicode.org/> The full list of these region codes is here: <https://github.com/unicode-cldr/cldr-localenames-full/blob/master/main/en/territories.json>  
  
## MonitoringConfig

Configuration related to monitoring project activity.

JSON representation  
---  
      
    
    {
      "requestLogging": {
        object ([RequestLogging](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#RequestLogging))
      }
    }  
  
Fields  
---  
`requestLogging` |  `object (`[RequestLogging](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#RequestLogging)`)` Configuration for logging requests made to this project to Stackdriver Logging  
  
## RequestLogging

Configuration for logging requests made to this project to Stackdriver Logging

JSON representation  
---  
      
    
    {
      "enabled": boolean
    }  
  
Fields  
---  
`enabled` |  `boolean` Whether logging is enabled for this project or not.  
  
## PasswordPolicyConfig

The configuration for the password policy on the project.

JSON representation  
---  
      
    
    {
      "passwordPolicyEnforcementState": enum ([PasswordPolicyEnforcementState](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#PasswordPolicyEnforcementState)),
      "passwordPolicyVersions": [
        {
          object ([PasswordPolicyVersion](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#PasswordPolicyVersion))
        }
      ],
      "forceUpgradeOnSignin": boolean,
      "lastUpdateTime": string
    }  
  
Fields  
---  
`passwordPolicyEnforcementState` |  `enum (`[PasswordPolicyEnforcementState](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#PasswordPolicyEnforcementState)`)` Which enforcement mode to use for the password policy.  
`passwordPolicyVersions[]` |  `object (`[PasswordPolicyVersion](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#PasswordPolicyVersion)`)` Must be of length 1. Contains the strength attributes for the password policy.  
`forceUpgradeOnSignin` |  `boolean` Users must have a password compliant with the password policy to sign-in.  
`lastUpdateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The last time the password policy on the project was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## PasswordPolicyEnforcementState

Enforcement state for the password policy

Enums  
---  
`PASSWORD_POLICY_ENFORCEMENT_STATE_UNSPECIFIED` | Illegal State, should not be used.  
`OFF` | Password Policy will not be used on the project.  
`ENFORCE` | Passwords non-compliant with the password policy will be rejected with an error thrown.  
  
## PasswordPolicyVersion

The strength attributes for the password policy on the project.

JSON representation  
---  
      
    
    {
      "customStrengthOptions": {
        object ([CustomStrengthOptions](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#CustomStrengthOptions))
      },
      "schemaVersion": integer
    }  
  
Fields  
---  
`customStrengthOptions` |  `object (`[CustomStrengthOptions](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#CustomStrengthOptions)`)` The custom strength options enforced by the password policy.  
`schemaVersion` |  `integer` Output only. schema version number for the password policy  
  
## CustomStrengthOptions

Custom strength options to enforce on user passwords.

JSON representation  
---  
      
    
    {
      "minPasswordLength": integer,
      "maxPasswordLength": integer,
      "containsLowercaseCharacter": boolean,
      "containsUppercaseCharacter": boolean,
      "containsNumericCharacter": boolean,
      "containsNonAlphanumericCharacter": boolean
    }  
  
Fields  
---  
`minPasswordLength` |  `integer` Minimum password length. Range from 6 to 30  
`maxPasswordLength` |  `integer` Maximum password length. No default max length  
`containsLowercaseCharacter` |  `boolean` The password must contain a lower case character.  
`containsUppercaseCharacter` |  `boolean` The password must contain an upper case character.  
`containsNumericCharacter` |  `boolean` The password must contain a number.  
`containsNonAlphanumericCharacter` |  `boolean` The password must contain a non alpha numeric character.  
  
## EmailPrivacyConfig

Configuration for settings related to email privacy and public visibility. Settings in this config protect against email enumeration, but may make some trade-offs in user-friendliness.

JSON representation  
---  
      
    
    {
      "enableImprovedEmailPrivacy": boolean
    }  
  
Fields  
---  
`enableImprovedEmailPrivacy` |  `boolean` Migrates the project to a state of improved email privacy. For example certain error codes are more generic to avoid giving away information on whether the account exists. In addition, this disables certain features that as a side-effect allow user enumeration. Enabling this toggle disables the fetchSignInMethodsForEmail functionality and changing the user's email to an unverified email. It is recommended to remove dependence on this functionality and enable this toggle to improve user privacy.  
  
## ClientPermissionConfig

Options related to how clients making requests on behalf of a tenant should be configured.

JSON representation  
---  
      
    
    {
      "permissions": {
        object ([ClientPermissions](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#ClientPermissions))
      }
    }  
  
Fields  
---  
`permissions` |  `object (`[ClientPermissions](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#ClientPermissions)`)` Configuration related to restricting a user's ability to affect their account.  
  
## ClientPermissions

Configuration related to restricting a user's ability to affect their account.

JSON representation  
---  
      
    
    {
      "disabledUserSignup": boolean,
      "disabledUserDeletion": boolean
    }  
  
Fields  
---  
`disabledUserSignup` |  `boolean` When true, end users cannot sign up for a new account on the associated project through any of our API methods  
`disabledUserDeletion` |  `boolean` When true, end users cannot delete their account on the associated project through any of our API methods  
  
## MobileLinksConfig

Configuration mobile links.

JSON representation  
---  
      
    
    {
      "domain": enum ([Domain](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#Domain))
    }  
  
Fields  
---  
`domain` |  `enum (`[Domain](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#Domain)`)` Open code in app domain to use for app links and universal links.  
  
## Domain

Possible open code in app domain to use for app links and universal links.

Enums  
---  
`DOMAIN_UNSPECIFIED` | Default value. The default domain is the Firebase Dynamic Link domain before the FDL deprecation and the hosting domain after the FDL deprecation.  
`FIREBASE_DYNAMIC_LINK_DOMAIN` | Use Firebase Dynamic Link domain as app link domain. Default value.  
`HOSTING_DOMAIN` | Use hosting domain as app link domain.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants/create)`

|  Create a tenant.  
  
### `[delete](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants/delete)`

|  Delete a tenant.  
  
### `[get](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants/get)`

|  Get a tenant.  
  
### `[getIamPolicy](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants/list)`

|  List tenants under the given agent project.  
  
### `[patch](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants/patch)`

|  Update a tenant.  
  
### `[setIamPolicy](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants/setIamPolicy)`

|  Sets the access control policy for a resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants/testIamPermissions)`

|  Returns the caller's permissions on a resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
