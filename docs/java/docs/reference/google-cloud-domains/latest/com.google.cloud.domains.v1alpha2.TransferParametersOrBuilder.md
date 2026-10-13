---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1alpha2.TransferParametersOrBuilder
title: Interface TransferParametersOrBuilder (1.96.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:45:26.384398+00:00
---

# Interface TransferParametersOrBuilder (1.96.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1alpha2.TransferParametersOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface TransferParametersOrBuilder (1.96.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.96.0 (latest)  1.92.0  1.91.0  1.90.0  1.88.0  1.85.0  1.84.0  1.82.0  1.80.0  1.79.0  1.78.0  1.77.0  1.75.0  1.73.0  1.72.0  1.71.0  1.70.0  1.69.0  1.67.0  1.65.0  1.64.0  1.61.0  1.60.0  1.59.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.6  0.7.0  0.6.1  0.5.4 
    
    
    public interface TransferParametersOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCurrentRegistrar()
    
    
    public abstract String getCurrentRegistrar()

The registrar that currently manages the domain.

`string current_registrar = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The currentRegistrar.  
  
### getCurrentRegistrarBytes()
    
    
    public abstract ByteString getCurrentRegistrarBytes()

The registrar that currently manages the domain.

`string current_registrar = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for currentRegistrar.  
  
### getDomainName()
    
    
    public abstract String getDomainName()

The domain name. Unicode domain names are expressed in Punycode format.

`string domain_name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The domainName.  
  
### getDomainNameBytes()
    
    
    public abstract ByteString getDomainNameBytes()

The domain name. Unicode domain names are expressed in Punycode format.

`string domain_name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for domainName.  
  
### getNameServers(int index)
    
    
    public abstract String getNameServers(int index)

The name servers that currently store the configuration of the domain.

`repeated string name_servers = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The nameServers at the given index.  
  
### getNameServersBytes(int index)
    
    
    public abstract ByteString getNameServersBytes(int index)

The name servers that currently store the configuration of the domain.

`repeated string name_servers = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the nameServers at the given index.  
  
### getNameServersCount()
    
    
    public abstract int getNameServersCount()

The name servers that currently store the configuration of the domain.

`repeated string name_servers = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of nameServers.  
  
### getNameServersList()
    
    
    public abstract List<String> getNameServersList()

The name servers that currently store the configuration of the domain.

`repeated string name_servers = 3;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the nameServers.  
  
### getSupportedPrivacy(int index)
    
    
    public abstract ContactPrivacy getSupportedPrivacy(int index)

Contact privacy options that the domain supports.

`repeated .google.cloud.domains.v1alpha2.ContactPrivacy supported_privacy = 5;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[ContactPrivacy](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1alpha2.ContactPrivacy)` | The supportedPrivacy at the given index.  
  
### getSupportedPrivacyCount()
    
    
    public abstract int getSupportedPrivacyCount()

Contact privacy options that the domain supports.

`repeated .google.cloud.domains.v1alpha2.ContactPrivacy supported_privacy = 5;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of supportedPrivacy.  
  
### getSupportedPrivacyList()
    
    
    public abstract List<ContactPrivacy> getSupportedPrivacyList()

Contact privacy options that the domain supports.

`repeated .google.cloud.domains.v1alpha2.ContactPrivacy supported_privacy = 5;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ContactPrivacy](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1alpha2.ContactPrivacy)>` | A list containing the supportedPrivacy.  
  
### getSupportedPrivacyValue(int index)
    
    
    public abstract int getSupportedPrivacyValue(int index)

Contact privacy options that the domain supports.

`repeated .google.cloud.domains.v1alpha2.ContactPrivacy supported_privacy = 5;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire of supportedPrivacy at the given index.  
  
### getSupportedPrivacyValueList()
    
    
    public abstract List<Integer> getSupportedPrivacyValueList()

Contact privacy options that the domain supports.

`repeated .google.cloud.domains.v1alpha2.ContactPrivacy supported_privacy = 5;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` | A list containing the enum numeric values on the wire for supportedPrivacy.  
  
### getTransferLockState()
    
    
    public abstract TransferLockState getTransferLockState()

Indicates whether the domain is protected by a transfer lock. For a transfer to succeed, this must show `UNLOCKED`. To unlock a domain, go to its current registrar.

`.google.cloud.domains.v1alpha2.TransferLockState transfer_lock_state = 4;`

**Returns**  
---  
**Type** | **Description**  
`[TransferLockState](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1alpha2.TransferLockState)` | The transferLockState.  
  
### getTransferLockStateValue()
    
    
    public abstract int getTransferLockStateValue()

Indicates whether the domain is protected by a transfer lock. For a transfer to succeed, this must show `UNLOCKED`. To unlock a domain, go to its current registrar.

`.google.cloud.domains.v1alpha2.TransferLockState transfer_lock_state = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for transferLockState.  
  
### getYearlyPrice()
    
    
    public abstract Money getYearlyPrice()

Price to transfer or renew the domain for one year.

`.google.type.Money yearly_price = 6;`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.Money` | The yearlyPrice.  
  
### getYearlyPriceOrBuilder()
    
    
    public abstract MoneyOrBuilder getYearlyPriceOrBuilder()

Price to transfer or renew the domain for one year.

`.google.type.Money yearly_price = 6;`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.MoneyOrBuilder` |   
  
### hasYearlyPrice()
    
    
    public abstract boolean hasYearlyPrice()

Price to transfer or renew the domain for one year.

`.google.type.Money yearly_price = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the yearlyPrice field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
