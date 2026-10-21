---
url: https://docs.cloud.google.com/universal-ledger/tutorial/deploy-contract/
title: Deploy a programmable contract \u00a0|\u00a0 Universal Ledger \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:45:08.379428+00:00
---

# Deploy a programmable contract  |  Universal Ledger  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/universal-ledger/tutorial/deploy-contract/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Universal Ledger ](https://docs.cloud.google.com/universal-ledger)
  * [ Guides ](https://docs.cloud.google.com/universal-ledger/overview)



Send feedback 

#  Deploy a programmable contract Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For information about access to this release, see the [ access request page](https://cloud.google.com/application/web3/universal-ledger). 

**Preview:** Programmable contracts are a preview feature of the Universal Ledger. The `gculpyc` compiler is under active development to add new features and improve capabilities. Because of this, the binary produced by the compiler could change depending on the version used. Deployed contracts could also behave differently after major updates. For notices and guidance around such changes see [Release notes](https://docs.cloud.google.com/universal-ledger/reference/gculpy-language#release_notes) in the GCULpy language reference.

The Universal Ledger supports programmable contracts that can be deployed in a network to automate and enforce agreements amongst interested participants.

This tutorial shows developers the steps necessary to develop, deploy, and interact with a programmable contract in a Universal Ledger network.

## Before you begin

To complete this tutorial you will need:

  * In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  * A Universal Ledger user account with the `ROLE_CONTRACT_CREATOR`. This account will become the _contract owner_.

  * One or more Universal Ledger user accounts with the `ROLE_CONTRACT_PARTICIPANT`. It can be the same account as the contract owner.

  * Optionally, [Set up the Universal Ledger CLI](https://docs.cloud.google.com/universal-ledger/how-to/set-up-cli) to be able to sign and submit transactions on behalf of these user accounts.




Universal Ledger roles can be assigned to a User Account when created by their Account Manager, at the time when its [CreateAccount](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#createaccount) transaction is submitted, or later modified through an [AddRoles](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#addroles) transaction if the account already exists. For experimentation purposes, you can also use the Universal Ledger CLI to [Manage accounts](https://docs.cloud.google.com/universal-ledger/how-to/set-up-cli#manage-accounts).

## Set up your environment

To simplify the setup, this tutorial has been written for the default environment provided in a Cloud Shell session. You might need to modify these commands if you are using a different environment.

**Experimental:** The `gculpyc` binary is made available as a Docker image to customers participating in the [Universal Ledger preview](https://docs.cloud.google.com/universal-ledger/preview-onboarding). This binary is in active development and subject to change or removal in new versions of the product.

The `gculpyc` compiler takes source code written in the GCULpy language and produces bytecode for the Universal Ledger.

Run each of the following commands to pull the `gculpyc` Docker image, define an alias for running the binary, and confirm that the binary works.
    
    
    docker pull us-docker.pkg.dev/gcul-artifacts/images/client/gculpyc:preview
    alias gculpyc="docker run --rm -i --user $(id -u):$(id -g) \
        --volume .:/workspace --workdir /workspace \
        us-docker.pkg.dev/gcul-artifacts/images/client/gculpyc:preview"
    gculpyc --help

## Write your contract

GCULpy is the language used to write contracts for the Universal Ledger. It is a statically typed subset of Python, optimized for clear, auditable, and comprehensible contract logic. This design prioritizes writing secure code and restricts unexpected or unsafe behaviors. For more details see [The GCULpy language](https://docs.cloud.google.com/universal-ledger/reference/gculpy-language) reference.

Because GCULpy is a strict subset of Python, you can continue to use your preferred integrated development environments (IDEs) along with your existing workflows and development practices.

As an example, your code could look something like:
    
    
    import gcul
    
    class Counter(gcul.Contract):
        """Example contract implementing a counter."""
    
        value: int
    
        def increment(self) -> None:
            """Increments the counter value by 1."""
            self.value += 1
    

Copy this sample code and save it into a file named `counter.py`.

## Test locally

In the near future, developers will have access to a local simulation environment. Provided as part of the `gcul` Python module, it is designed to provide the necessary functionalities for natively simulating a Universal Ledger network within a Python environment. As such, you will be able to run contracts locally and write unit tests using your preferred testing frameworks, ensuring the reliability and correctness of your contracts before deployment.

## Compile the contract

Compile the preceding contract source code into bytecode using the following `gculpyc` command:
    
    
    gculpyc --source_file counter.py --output_file counter.bin

## Deploy the contract

Deploy the contract to a Universal Ledger network by submitting a [CreateContract](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#createcontract) transaction signed by a user account holding the `ROLE_CONTRACT_CREATOR`.

If using the Universal Ledger CLI, you can do this by running the command:
    
    
    ul-cli contracts create \
        --alias counter-contract \
        --sender OWNER_ALIAS \
        counter.bin

Replace the following:

  * `OWNER_ALIAS`: the alias of a user account with the `ROLE_CONTRACT_CREATOR`.



When the transaction is finalized, the output of this command will include the ID of the newly deployed contract. For example:
    
    
    Contract created: 1:CTR:005XvYfiSm3913Jwv4y8HVQucStJ2Ev15Sar6A1kNNX10
    

## Invoke a contract method

Once a contract is deployed, any user account with the `ROLE_CONTRACT_PARTICIPANT` can submit an [InvokeContractMethod](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#invokecontractmethod) transaction to invoke any of the public methods in the contract.

If using the Universal Ledger CLI, you can do this by running the command:
    
    
    ul-cli contracts invoke \
        --alias counter-contract \
        --method-name increment \
        --sender PARTICIPANT_ALIAS

Replace the following:

  * `PARTICIPANT_ALIAS`: the alias of a user account with the `ROLE_CONTRACT_PARTICIPANT`.



## Read the contract state

To conclude this tutorial, you can submit a [QueryAccount](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.UniversalLedger.QueryAccount) request to read and verify the state of the contract stored on the ledger. This is the same API method used to query and retrieve the details of any Universal Ledger account.

Using the Universal Ledger CLI, you can run:
    
    
    ul-cli accounts describe --alias counter-contract

This should confirm that the counter value is now set to 1, producing an output such as:
    
    
    Account: 1:CTR:005XvYfiSm3913Jwv4y8HVQucStJ2Ev15Sar6A1kNNX10
    Contract account details:
      Owner: 1:USR:XCL:022uF6cVkTJBaa6pViqTuYqP4455jnRbRc4bWannZGg0b
      Contract fields:
        value: int64_value:1
    
      Balances:
        None
    

## What's next

  * Explore [The GCULpy language](https://docs.cloud.google.com/universal-ledger/reference/gculpy-language) reference.
  * Learn about other [transactions you can submit to a network](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#clienttransaction).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-26 UTC."],[],[]] 
