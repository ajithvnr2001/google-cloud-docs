---
url: https://docs.cloud.google.com/recaptcha/docs/reference/ios/client/api/Classes/RecaptchaError/
title: RecaptchaEnterprise Framework Reference \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:43:15.518916+00:00
---

# RecaptchaEnterprise Framework Reference  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/reference/ios/client/api/Classes/RecaptchaError/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Reference ](https://docs.cloud.google.com/recaptcha/docs/apis)



Send feedback 

#  RecaptchaEnterprise Framework Reference Stay organized with collections  Save and categorize content based on your preferences. 

# RecaptchaError
    
    
    @interface RecaptchaError : NSError

Error class for reCAPTCHA Events.

  * `

### errorMessage

`

Human readable error message.

#### Declaration

Swift
        
        var errorMessage: String? { get set }

Objective-C
        
        @property (nonatomic, nullable) NSString *errorMessage;

  * `

### errorCode

`

Code relative to the error that was thrown. It maps to `[RecaptchaErrorCode](https://docs.cloud.google.com/recaptcha/docs/reference/ios/client/api/Enums/RecaptchaErrorCode.html)`.

#### Declaration

Swift
        
        var errorCode: Int { get set }

Objective-C
        
        @property (nonatomic) NSInteger errorCode;

  * `

### -initWithDomain:code:userInfo:message:

`

Builds a new reCAPTCHA Error object.

#### Declaration

Swift
        
        init(domain: String, code: [RecaptchaErrorCode](https://docs.cloud.google.com/recaptcha/docs/reference/ios/client/api/Enums/RecaptchaErrorCode.html), userInfo dict: [String : Any]? = nil, message: String?)

Objective-C
        
        - (nonnull instancetype)
            initWithDomain:(nonnull NSErrorDomain)domain
                      code:([RecaptchaErrorCode](https://docs.cloud.google.com/recaptcha/docs/reference/ios/client/api/Enums/RecaptchaErrorCode.html))code
                  userInfo:(NSDictionary<NSErrorUserInfoKey, id> *_Nullable)dict
                   message:(NSString *_Nullable)message;

  * `

### -init

`

Unavailable

Undocumented

#### Declaration

Objective-C
        
        - (instancetype)init NS_UNAVAILABLE;

  * `

### -description

`

For debug purposes, prints a human-friendly description of the error.

#### Declaration

Swift
        
        func description() -> String

Objective-C
        
        - (nonnull NSString *)description;




Deprecated APIs and properties.

  * `

### workflowAbortedTokenKey

`

Deprecated

This property is not used on > 18.X.X versions of the SDK.

If the returned error code is of type `Aborted` you can use this key to get the aborted token out of the `userInfo` property. The token is stored inside an instance of `[RecaptchaToken](https://docs.cloud.google.com/recaptcha/docs/reference/ios/client/api/Classes/RecaptchaToken.html)`.

#### Declaration

Swift
        
        class var workflowAbortedTokenKey: String { get }

Objective-C
        
        @property (class, nonatomic, readonly) NSString *_Nonnull workflowAbortedTokenKey;




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
