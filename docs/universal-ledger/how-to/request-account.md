---
url: https://docs.cloud.google.com/universal-ledger/how-to/request-account/
title: Request a new account \u00a0|\u00a0 Universal Ledger \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:36:07.908855+00:00
---

# Request a new account  |  Universal Ledger  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/universal-ledger/how-to/request-account/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Universal Ledger ](https://docs.cloud.google.com/universal-ledger)
  * [ Guides ](https://docs.cloud.google.com/universal-ledger/overview)



Send feedback 

#  Request a new account Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For information about access to this release, see the [ access request page](https://cloud.google.com/application/web3/universal-ledger). 

New accounts in a Universal Ledger network must be created by a privileged administrator account already present on the ledger. This privileged account must sign and submit a transaction to create the new account.

This guide describes how to request a new account in a Universal Ledger network. Learn how to:

  * Create asymmetric signing keys for the new account using Cloud Key Management Service.

  * Identify the owner of the appropriate privileged account who can create your account.

  * Confirm your account details once it's created on the ledger.




## Before you begin

To complete this guide, you will need the following:

  * A Google Cloud project with the Universal Ledger API enabled.

  * An IAM role such as `roles/universalledger.networkViewer` so you can at least query the state of accounts in a Universal Ledger network.

  * A Google Cloud project with the Cloud KMS enabled.

During testing, this project can be the same as the one with Universal Ledger API enabled.

In production, we recommend you:

    * Use a dedicated project for your Cloud KMS resources, separate from other Google Cloud resources.
    * Create a separate Google Cloud project to manage the Cloud KMS keys for each Universal Ledger network you use.
  * The Cloud KMS Admin (`roles/cloudkms.admin`) IAM role on the project with Cloud KMS enabled, or on a parent resource.




## Create your asymmetric signing keys

Every account operating on a Universal Ledger requires an asymmetric signing public-private key pair. The private key is used for signing transactions, and the public key is registered on the ledger to identify your account and verify signatures.

The following steps guide you through creating a suitable key pair using Cloud KMS and retrieving the public key. You can use other key management approaches as long as they produce keys and signatures compatible with Universal Ledger requirements, such as ECDSA P-256 keys with SHA-256 digests. For details about supported key formats, see the [`KeyFormat`](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#keyformat) reference.

**Tip:** You can also find and manage all of your keys and key rings in the [Key management](https://console.cloud.google.com/security/kms/keyrings) page of the Google Cloud console.

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. Set the default project:
         
         gcloud config set project KEYS_PROJECT
         

Replace `KEYS_PROJECT` with the ID of the project to be used for your Cloud KMS resources.

  3. If you haven't already, create a key ring to hold your keys using the [`gcloud kms keyrings create` command](https://docs.cloud.google.com/sdk/gcloud/reference/kms/keys/create):
         
         gcloud kms keyrings create KEY_RING \
             --location=KEY_LOCATION
         

Replace the following:

     * `KEY_RING`: the name of the key ring to create, for example `test-gcul-keys`. This name is for your own organizational needs and does not need to be recorded on the ledger.
     * `KEY_LOCATION`: the Google Cloud location for the key ring, for example `global`.
  4. For each account you want to use on the ledger, create an asymmetric signing key for it using the [`gcloud kms keys create` command](https://docs.cloud.google.com/sdk/gcloud/reference/kms/keys/create):
         
         gcloud kms keys create KEY_NAME \
             --keyring=KEY_RING \
             --location=KEY_LOCATION \
             --purpose="asymmetric-signing" \
             --default-algorithm="ec-sign-p256-sha256"
         

Replace the following:

     * `KEY_NAME`: the name of the key to create, for example `usd-operator` or `eur-clearinghouse`. This name is for your own organizational needs and does not need to be recorded on the ledger.
     * `KEY_RING`: the name of the key ring to hold the key.
     * `KEY_LOCATION`: the Google Cloud location for the key.

This creates an ECDSA key pair on the P-256 Curve with a SHA-256 digest as supported by the Universal Ledger. For a list of supported formats, consult the [`KeyFormat`](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#keyformat) reference.

  5. Retrieve the public key portion of a key version using the [`gcloud kms keys versions get-public-key` command](https://docs.cloud.google.com/sdk/gcloud/reference/kms/keys/versions/get-public-key):
         
         gcloud kms keys versions get-public-key KEY_VERSION \
             --key=KEY_NAME \
             --keyring=KEY_RING \
             --location=KEY_LOCATION
         

Replace the following:

     * `KEY_VERSION`: the version of the key to get, this is `1` for newly created keys.
     * `KEY_NAME`: the name of the key.
     * `KEY_RING`: the name of the key ring containing the key.
     * `KEY_LOCATION`: the Google Cloud location of the key.

This command outputs the public key in a PEM-encoded format (`KEY_FORMAT_PEM_EC_P256_SHA256`) suitable to use with the Universal Ledger API such as:
    
    -----BEGIN PUBLIC KEY-----
    MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEJ/vWkd5wgakFbVD25k8WM9Ll6We+
    c8RVDS0R4G8xetsmFjfNW/ZxwWeB86IvMjxY8ZsdU9+W7BL5YM6rUB5yCQ==
    -----END PUBLIC KEY-----
    




## Identify who can create your account

The type of account you want to create determines the privileged account on the ledger which has the permission to create it. You need to identify the owner of that privileged account. To learn about the types of accounts in the Universal Ledger, see [Key concepts](https://docs.cloud.google.com/universal-ledger/overview#key_concepts).

Account type | Is created by | Submitting the transaction  
---|---|---  
Currency Operator | Platform Operator | [CreateCurrencyOperator](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#createcurrencyoperator)  
Clearinghouse | Currency Operator | [CreateClearinghouse](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#createclearinghouse)  
Account Manager | Currency Operator | [CreateAccountManager](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#createaccountmanager)  
Token Manager | Currency Operator | [CreateTokenManager](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#createtokenmanager)  
User Account | Account Manager | [CreateAccount](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#createaccount)  
  
Once identified, you'll need to coordinate and share the following details with the owner of the privileged account who can create your account:

  * The name of the network where you want the account created. For a list of supported regions, see [Available networks and regions](https://docs.cloud.google.com/universal-ledger/preview-onboarding#available_networks_and_regions).
  * The public portion of your asymmetric signing key and its corresponding [`KeyFormat`](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#keyformat). If you followed the `gcloud` commands in this guide, the format is `KEY_FORMAT_PEM_EC_P256_SHA256`.
  * An account comment string with any relevant information to record on the ledger associated with your new account. This is an opaque value that is stored on ledger but not interpreted otherwise by the Universal Ledger. Once created, this field is immutable and readable by anyone with access to the network.
  * Any additional details required to populate the transaction to be submitted when creating the account. For example, to create a Currency Operator you also need to specify the `currency` that will be managed by the new operator to be created.



During Preview, reach out to your contact at Google if you are unsure about who is the owner of the relevant privileged account for your use case.

## Confirm your account is created

Once the transaction submitted by the privileged account is successfully executed and finalized on the ledger, the response from the [`QueryTransactionState`](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.UniversalLedger.QueryTransactionState) method will include a [`TransactionCertificate`](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#transactioncertificate) with a `transaction_output` event containing the account ID of the newly created account.

**Important:** The owner of the privileged account must share this ID with you.

The ID will look similar to the following example:
    
    
    1:USR:XTS:025sAZ55EqGKF6vpXEpSS8X891nNDEQU9yFQKYkcFzAb6
    

You can confirm that your new account is present on the ledger by submitting the following REST request:
    
    
    curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        https://universalledger.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/endpoints/NETWORK_NAME:queryAccount?account_id=ACCOUNT_ID
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the Universal Ledger API is enabled.
  * `LOCATION`: the location of the endpoint to reach.
  * `NETWORK_NAME`: the name of the network where your account was created.
  * `ACCOUNT_ID`: the ID of your newly created account.



You will see output similar to the following:
    
    
    {
      "account": {
        "publicKey": "LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUZrd0V3WUhLb1pJemowQ0FRWUlLb1pJemowREFRY0RRZ0FFSi92V2tkNXdnYWtGYlZEMjVrOFdNOUxsNldlKwpjOFJWRFMwUjRHOHhldHNtRmpmTlcvWnh3V2VCODZJdk1qeFk4WnNkVTkrVzdCTDVZTTZyVUI1eUNRPT0KLS0tLS1FTkQgUFVCTElDIEtFWS0tLS0t",
        "roundId": "10962032",
        "comment": "My Test Account",
        "userDetails": {
          "accountManager": {
            "id": "1:ACT:XTS:02f4VSHyPsXeMZmcogbNx7bP4kfn5DYvc7d2K52RYAFd3"
          },
          "tokenManager": {
            "id": "1:TKN:XTS:024fqJS87dJ94ETN9PGhTCGd86btXj9iyWLxGQWgC3dde"
          },
          "roles": [
            "ROLE_PAYER",
            "ROLE_RECEIVER"
          ],
          "accountStatus": "ACCOUNT_STATUS_ACTIVE",
        }
      }
    }
    

## What's next

  * Learn [how to send RPC requests](https://docs.cloud.google.com/universal-ledger/tutorial/send-rpc-request-py) to the Universal Ledger API.
  * Learn about [transactions you can submit using your new account](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#clienttransaction).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-02 UTC."],[],[]] 
