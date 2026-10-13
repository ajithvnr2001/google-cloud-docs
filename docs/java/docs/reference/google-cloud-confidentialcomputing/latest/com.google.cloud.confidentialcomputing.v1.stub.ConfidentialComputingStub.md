---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.stub.ConfidentialComputingStub
title: Class ConfidentialComputingStub (0.85.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:46:53.744007+00:00
---

# Class ConfidentialComputingStub (0.85.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.stub.ConfidentialComputingStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ConfidentialComputingStub (0.85.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.85.0 (latest)  0.81.0  0.80.0  0.79.0  0.77.0  0.74.0  0.73.0  0.71.0  0.69.0  0.68.0  0.67.0  0.66.0  0.64.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.56.0  0.54.0  0.53.0  0.50.0  0.49.0  0.48.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public abstract class ConfidentialComputingStub implements BackgroundResource

Base stub class for the ConfidentialComputing service API.

This class is for advanced usage and reflects the underlying API directly.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ConfidentialComputingStub

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

### ConfidentialComputingStub()
    
    
    public ConfidentialComputingStub()

## Methods 

### close()
    
    
    public abstract void close()

### createChallengeCallable()
    
    
    public UnaryCallable<CreateChallengeRequest,Challenge> createChallengeCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateChallengeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.CreateChallengeRequest),[Challenge](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.Challenge)>` |   
  
### getLocationCallable()
    
    
    public UnaryCallable<GetLocationRequest,Location> getLocationCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### listLocationsCallable()
    
    
    public UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse>` |   
  
### listLocationsPagedCallable()
    
    
    public UnaryCallable<ListLocationsRequest,ConfidentialComputingClient.ListLocationsPagedResponse> listLocationsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.ConfidentialComputingClient.ListLocationsPagedResponse)>` |   
  
### verifyAttestationCallable()
    
    
    public UnaryCallable<VerifyAttestationRequest,VerifyAttestationResponse> verifyAttestationCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[VerifyAttestationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.VerifyAttestationRequest),[VerifyAttestationResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.VerifyAttestationResponse)>` |   
  
### verifyConfidentialGkeCallable()
    
    
    public UnaryCallable<VerifyConfidentialGkeRequest,VerifyConfidentialGkeResponse> verifyConfidentialGkeCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[VerifyConfidentialGkeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.VerifyConfidentialGkeRequest),[VerifyConfidentialGkeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.VerifyConfidentialGkeResponse)>` |   
  
### verifyConfidentialSpaceCallable()
    
    
    public UnaryCallable<VerifyConfidentialSpaceRequest,VerifyConfidentialSpaceResponse> verifyConfidentialSpaceCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[VerifyConfidentialSpaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.VerifyConfidentialSpaceRequest),[VerifyConfidentialSpaceResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.VerifyConfidentialSpaceResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
