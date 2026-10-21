---
url: https://docs.cloud.google.com/universal-ledger/overview/
title: Universal Ledger overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:53:03.514382+00:00
---

# Universal Ledger overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/universal-ledger/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Universal Ledger ](https://docs.cloud.google.com/universal-ledger)
  * [ Guides ](https://docs.cloud.google.com/universal-ledger/overview)



Send feedback 

#  Universal Ledger overview Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For information about access to this release, see the [ access request page](https://cloud.google.com/application/web3/universal-ledger). 

Universal Ledger API is a fully managed service that helps enterprises, such as financial institutions, build and interact with Universal Ledger networks. Use the API to create innovative payment services, tokenize assets, and develop new financial market products.

The API also simplifies managing tokenized assets, such as commercial bank money, and facilitates transfers using a distributed ledger.

## Key concepts

The Universal Ledger operates on the following core concepts:

  * **Accounts:** Entities on the ledger, such as users or institutions. Each account has a unique system-assigned ID, a public key for signing transactions, and roles that define its permissions.
  * **Tokens:** Digital representations of value—for example, commercial bank money—that can be minted, transferred, and burned within the network by accounts with the appropriate permissions.
  * **Transactions:** Signed operations submitted to network endpoints to change the ledger state. Examples include creating accounts and transferring tokens.
  * **Roles:** Control the actions an account is permitted to perform. Examples include `ROLE_PAYER` (permission to send tokens) and `ROLE_RECEIVER` (permission to receive tokens).
  * **Operators & Managers:** Specialized account types with administrative privileges: 
    * **Platform Operator:** Manages the overall network infrastructure.
    * **Currency Operator:** Manages a specific currency within the network.
    * **Account Manager:** Manages end-user accounts, including their creation, status, and role assignments.
    * **Token Manager:** Controls the supply of tokens for the currency it manages, under limits set by a Clearinghouse.
    * **Clearinghouse:** Oversees settlement processes and manages the issuance capacity of Token Managers.



## Key features

  * **Account management:** Create, activate, deactivate, and manage roles for user accounts.
  * **Token lifecycle management:** Mint new tokens into circulation, transfer tokens between accounts, and burn tokens to remove them from circulation.
  * **Settlement workflows:** Support and record settlement processes between participants.
  * **State queries:** Query the current state of any account on the ledger and check the status of submitted transactions.
  * **Secure operations:** Ensure transaction authenticity and integrity through cryptographic signatures.



## Use cases

Universal Ledger is designed for a variety of enterprise use cases, including the following:

  * **Wholesale payments:** Streamline interbank payment and settlement systems.
  * **Tokenized securities:** Issue, trade, and manage securities as digital tokens on a ledger.
  * **Supply-chain finance:** Enhance transparency and efficiency in trade finance ecosystems.
  * **Novel financial products:** Build new instruments and markets for digital assets.



Universal Ledger helps provide a robust platform for institutions to explore these and other innovative financial applications.

## What's next

  * Onboard to the [Universal Ledger preview](https://docs.cloud.google.com/universal-ledger/preview-onboarding).
  * Request the [creation of an account on the ledger](https://docs.cloud.google.com/universal-ledger/how-to/request-account)
  * Learn how to [send RPC requests with Python](https://docs.cloud.google.com/universal-ledger/tutorial/send-rpc-request-py). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-26 UTC."],[],[]] 
