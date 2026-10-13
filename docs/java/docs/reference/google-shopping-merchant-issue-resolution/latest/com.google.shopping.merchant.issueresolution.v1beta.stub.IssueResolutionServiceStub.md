---
url: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-issue-resolution/latest/com.google.shopping.merchant.issueresolution.v1beta.stub.IssueResolutionServiceStub
title: Class IssueResolutionServiceStub (1.27.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:59:20.210768+00:00
---

# Class IssueResolutionServiceStub (1.27.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-issue-resolution/latest/com.google.shopping.merchant.issueresolution.v1beta.stub.IssueResolutionServiceStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class IssueResolutionServiceStub (1.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.27.0 (latest)  1.23.0  1.22.0  1.21.0  1.19.0  1.16.0  1.15.0  1.13.0  1.11.0  1.10.0  1.9.0  1.8.0  1.6.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.10.0  0.8.0  0.7.0  0.4.0  0.3.0  0.2.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 
    
    
    public abstract class IssueResolutionServiceStub implements BackgroundResource

Base stub class for the IssueResolutionService service API.

This class is for advanced usage and reflects the underlying API directly.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > IssueResolutionServiceStub

## Implements

[BackgroundResource](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.BackgroundResource.html)

## Inherited Members

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Constructors 

### IssueResolutionServiceStub()
    
    
    public IssueResolutionServiceStub()

## Methods 

### close()
    
    
    public abstract void close()

### renderAccountIssuesCallable()
    
    
    public UnaryCallable<RenderAccountIssuesRequest,RenderAccountIssuesResponse> renderAccountIssuesCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RenderAccountIssuesRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-issue-resolution/latest/com.google.shopping.merchant.issueresolution.v1beta.RenderAccountIssuesRequest),[RenderAccountIssuesResponse](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-issue-resolution/latest/com.google.shopping.merchant.issueresolution.v1beta.RenderAccountIssuesResponse)>` |   
  
### renderProductIssuesCallable()
    
    
    public UnaryCallable<RenderProductIssuesRequest,RenderProductIssuesResponse> renderProductIssuesCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RenderProductIssuesRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-issue-resolution/latest/com.google.shopping.merchant.issueresolution.v1beta.RenderProductIssuesRequest),[RenderProductIssuesResponse](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-issue-resolution/latest/com.google.shopping.merchant.issueresolution.v1beta.RenderProductIssuesResponse)>` |   
  
### triggerActionCallable()
    
    
    public UnaryCallable<TriggerActionRequest,TriggerActionResponse> triggerActionCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[TriggerActionRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-issue-resolution/latest/com.google.shopping.merchant.issueresolution.v1beta.TriggerActionRequest),[TriggerActionResponse](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-issue-resolution/latest/com.google.shopping.merchant.issueresolution.v1beta.TriggerActionResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
