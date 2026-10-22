---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/key-encryption/
title: Data encryption \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:40.291519+00:00
---

# Data encryption  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/key-encryption/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Data encryption Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.17 (latest)keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/key-encryption.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/key-encryption.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/key-encryption.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/key-encryption.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/key-encryption.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/key-encryption.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/key-encryption.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/key-encryption.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/key-encryption.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/key-encryption.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/key-encryption.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/key-encryption.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/key-encryption.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/key-encryption.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/key-encryption.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/key-encryption.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/key-encryption.html)



By default, the following data is stored _encrypted_ in the hybrid runtime plane: 

  * Cache data
  * Contract key data
  * Key management system (KMS) data
  * Key-value map (KVM) data



Data encryption does not require any special configuration on your part. However, if for some reason you want to use your own encryption keys (replacing the default ones) you can do so, as explained in this topic. 

##  Encryption key scope 

Apigee hybrid encryption keys have scope. For example, KMS keys have _organization_ scope. This means that the key is used to encrypt KMS data for the entire organization. The following table lists the scope for each type of key: 

Encryption key | Scope  
---|---  
Contract |  Organization only   
KMS |  Organization only   
KVM  |  Organization or environment If a [KVM policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/key-value-map-operations-policy#ScopeElement) specifies `apiproxy` or `policy` (API proxy revision) scope, the organization level key is used to encrypt the data. For a general overview of how KVMs are used in Apigee Edge, see [Working with key-value maps](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps).  
Cache |  Environment only   
  
##  About the default encryption keys 

By default, Apigee hybrid provides a set of Base64-encoded keys that are used to encrypt contract, KVM, KMS, and cache data. The Apigee hybrid installer stores the keys in the runtime plane as [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/), and uses them to encrypt your data with AES-128 standard encryption. The keys are under your control; the hybrid management plane is never aware of them at any time. 

The default keys are applied to all new Apigee hybrid components when you create them. 

The default keys will work for most use cases. If you want to change the default encryption keys, do so when you initially install Apigee hybrid into a new cluster. If you change the encryption keys after the runtime is created in your cluster, previously encrypted data can no longer work (it cannot be decrypted); only new data added after the change will be encrypted and function as expected.

##  Changing the default encryption keys 

Although not required, you can change any of the default encryption keys if you wish. To replace one or more default keys, follow these steps: 

If you change the encryption keys after the runtime is created in your cluster, previously encrypted data can no longer work (it cannot be decrypted); only new data added after the change will be encrypted and function as expected. For this reason, Apigee hybrid does not support key rotation for these keys.

  1. Copy the following stanzas into your overrides file. This configuration lets you change the KMS and KVM encryption keys for the organization level and the KVM and cache encryption keys for the environment level: 
         
         defaults:
           org:
             kmsEncryptionKey: base64-encoded-key
             kvmEncryptionKey: base64-encoded-key
             contractEncryptionKey: base64-encoded-key
         
           env:
             kvmEncryptionKey: base64-encoded-key
             cacheEncryptionKey: base64-encoded-key

  2. Generate a new key for each key you wish to replace. Each key must be a Base64-encoded string that is exactly **16, 24, or 32 bytes long**. See also How to create an encoded key.
  3. Replace the default keys with new ones. In this example, all of the default keys are replaced with keys: 
         
         defaults:
           org:
             kmsEncryptionKey: "JVpTb1FwI0otUHo2RUdRN3pnVyQqVGlMSEFAJXYmb1c="
             kvmEncryptionKey: "T3VkRGM1U3cpOFgtNk9fMnNZU2NaSVA3I1BtZWxkaUU="
             contractEncryptionKey: "RDEyMzQ1Njc4OTAxMjM0NQ=="
           env:
             kvmEncryptionKey: "Q3h6M3R6OWdBeipxTURfKjQwQVdtTng2dU5mODFHcyE="
             cacheEncryptionKey: "b2NTVXdKKjBzN0NORF9XSm9tWFlYKGJ6NUhpNystJVI="




## Override the default keys

You can override the keys for the org or specific envs named in your overrides file. When you create the components, keys you specify for the org or individual envs will be override the defaults.

If you change the encryption keys after the runtime is created in your cluster, previously encrypted data can no longer work (it cannot be decrypted); only new data added after the change will be encrypted and function as expected. For this reason, Apigee hybrid does not support key rotation for these keys.

  1. Copy the following stanzas into your overrides file. This configuration lets you change the KMS and KVM encryption keys for the organization level and the KVM and cache encryption keys for the environment level: 
         
         org:YOUR_ORG_NAME
         
         kmsEncryptionKey: base64-encoded-key
         kvmEncryptionKey: base64-encoded-key
         contractEncryptionKey: base64-encoded-key
         
         envs
           - name: ENV_NAME
             kvmEncryptionKey: base64-encoded-key
             kmsEncryptionKey: base64-encoded-key
             cacheEncryptionKey: base64-encoded-key
         
           - name: 2ND_ENV_NAME
             kvmEncryptionKey: base64-encoded-key
             kmsEncryptionKey: base64-encoded-key
             cacheEncryptionKey: base64-encoded-key

  2. Generate a new key for each key you wish to override. Each key must be a Base64-encoded string that is exactly **16, 24, or 32 bytes long**. See also How to create an encoded key.
  3. Specify the keys you want to override. In this example, all of the default keys are replaced with keys: 
         
         org:hybrid-org
         
         kmsEncryptionKey: "QTEyMz1b2jc4OTAxMjM0NQ=="
         kvmEncryptionKey: "QzEyM2c3Njc4OTAxMjM0NQ=="
         contractEncryptionKey: "RDEyMzQ1Njc4OTAxMjM0NQ=="
         
         envs:
           - name: prod
             kvmEncryptionKey: "QzEyM2c3Njc4OTAxMjM0NQ=="
             kmsEncryptionKey: "QTEyMz1b2jc4OTAxMjM0NQ=="
             cacheEncryptionKey: "QjEyAvC1Njc4OTAxMjM0NQ=="
         
         envs:
           - name: test
             kvmEncryptionKey: "A1b2C3d4E5f6G7h8I9j10K=="
             kmsEncryptionKey: "QTEyMz1b2jc4OTAxMjM0NQ=="
             cacheEncryptionKey: "B1c2D3e4F5f6H7i8J9k10L=="




## Apply the key changes

Apply the overrides file to your cluster as with the following Helm commands: 

  * If you change the contract key or the KVM key for the org, update the org: 
        
        helm upgrade ORG_NAME apigee-org/ \
          --namespace apigee \
          --atomic \
          -f OVERRIDES_FILE.yaml
        

  * If you change Cache key or the KVM key for an environment, update the environment: 
        
        helm upgrade ENV_NAME apigee-env/ \
          --namespace apigee \
          --atomic \
          --set env=ENV_NAME \
          -f OVERRIDES_FILE.yaml
        

  * If you change KMS key, update both the org and environment: 
        
        helm upgrade ORG_NAME apigee-org/ \
          --namespace apigee \
          --atomic \
          -f OVERRIDES_FILE.yaml
        
        
        helm upgrade ENV_NAME apigee-env/ \
          --namespace apigee \
          --set env=ENV_NAME \
          --atomic \
          -f OVERRIDES_FILE.yaml
        


**Note:** If you see an error saying `Error: UPGRADE FAILED: "_ENV_NAME_ " has no deployed releases`, replace `upgrade` with `install` and try the command again.

##  A note about backward compatibility 

If you were to remove the encryption keys in your overrides file the first time you install Apigee hybrid, you would effectively disable encryption and values would be stored unencrypted. If at a later time you enable encryption by providing keys, exiting data remains unencrypted; however, any future data that is added will be encrypted. The system will continue working normally with the unencrypted data and the new encrypted data. 

Also, note that you cannot later change the encryption keys once the runtime data is encrypted. 

##  How to create an encoded key 

A properly formatted Base-64-encoded key is required for KVM, KMS, and cache encryption. The key used for any of these purposes must be Base-64 encoded from a string that is 16, 24, or 32 bytes long, as explained below: 

The key string length requirement exists because the [Advanced Encryption Standard](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) (AES) cipher works on a block size of 128 bits, but can take three different key lengths: 128, 192, and 256 bits (16, 24, or 32 bytes).

The following example command generates a suitable, randomly generated, 32 character, Base64-encoded string: 
    
    
    head -c 32 /dev/random | openssl base64

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
