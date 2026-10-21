---
url: https://docs.cloud.google.com/universal-ledger/how-to/set-up-cli/
title: Set up the Universal Ledger CLI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:36:08.404335+00:00
---

# Set up the Universal Ledger CLI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/universal-ledger/how-to/set-up-cli/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Universal Ledger ](https://docs.cloud.google.com/universal-ledger)
  * [ Guides ](https://docs.cloud.google.com/universal-ledger/overview)



Send feedback 

#  Set up the Universal Ledger CLI Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For information about access to this release, see the [ access request page](https://cloud.google.com/application/web3/universal-ledger). 

The Universal Ledger CLI is a command line interface provided for experimentation purposes to facilitate submitting transactions and interacting with a Universal Ledger network. For production use cases, it is recommended to build integrations using the [Universal Ledger APIs](https://docs.cloud.google.com/universal-ledger/apis) instead.

This guide describes how to get started with the Universal Ledger CLI. Learn how to:

  * Obtain and set up the Universal Ledger CLI.

  * Create and manage accounts using the CLI.

  * Explore other commands available in the CLI.




## Before you begin

To complete this guide, you will need the following:

  * A Google Cloud project with the Universal Ledger API enabled.

  * An IAM role such as `roles/universalledger.networkUser` so you can submit transactions and query the state of accounts in a Universal Ledger network.

  * An existing Universal Ledger account created for you on the network. If you don't have one already, see [Request a new account](https://docs.cloud.google.com/universal-ledger/how-to/request-account).




## Set up the CLI

To simplify the setup, this guide has been written for the default environment provided in a Cloud Shell session. You might need to modify these commands if you want to use the CLI in a different environment.

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

**Experimental:** The `ul-cli` binary is made available as a Docker image to customers participating in the [Universal Ledger preview](https://docs.cloud.google.com/universal-ledger/preview-onboarding). This binary is in active development and subject to change or removal in new versions of the product.

Run the following command to create a directory to hold the CLI configuration files.
    
    
    mkdir -p ~/.config/ul-cli

Run each of the following commands to pull the `ul-cli` Docker image, define an alias for running the binary, and confirm that the binary works.
    
    
    docker pull us-docker.pkg.dev/gcul-artifacts/images/client/ul-cli:preview
    alias ul-cli="docker run --rm -i --user $(id -u):$(id -g) \
        --volume /tmp:/tmp \
        --volume ~/.config/ul-cli:/home/.config/ul-cli \
        --volume ~/.config/gcloud:/home/.config/gcloud \
        --volume .:/workspace \
        --env HOME=/home \
        --workdir /workspace \
        us-docker.pkg.dev/gcul-artifacts/images/client/ul-cli:preview"
    ul-cli --help

Run the following command to configure the CLI.
    
    
    ul-cli config setup projects/PROJECT_ID/locations/REGION/endpoints/NETWORK_NAME

Replace the following:

  * `PROJECT_ID`: the ID of the Google Cloud project where the Universal Ledger API is enabled.
  * `REGION`: the region of the endpoint you want to reach.
  * `NETWORK_NAME`: the name of the network you want to interact with.



If you need help choosing a suitable endpoint, see [Available networks and regions](https://docs.cloud.google.com/universal-ledger/preview-onboarding#available_networks_and_regions).

The previous command will create a file under
    
    
    ~/.config/ul-cli/config.yaml
    

with the configuration that will be used and maintained by the CLI.

## Manage Universal Ledger accounts

This section explains how to register an existing account, create a new account for yourself on the ledger, and create new accounts for someone else.

### Register an existing account

Once an account has been created for you by another participant on the network, you can use the following command to register the account details in the CLI's address book.
    
    
    ul-cli accounts register \
        --alias ACCOUNT_ALIAS \
        --account-id ACCOUNT_ID \
        --key-name ACCOUNT_KMS_KEY

Replace the following:

  * `ACCOUNT_ALIAS`: a short string used locally by the CLI to identify this account in future command invocations. For example: `usd-operator`, `my-token-manager`, or `test-user-account`.
  * `ACCOUNT_ID`: the ID of the Universal Ledger account that has been created for you.
  * `ACCOUNT_KMS_KEY`: the full resource ID of the Cloud KMS **key version** used by this account. The account must have been created using the public portion of this specific key version. See [Retrieving a resource's ID](https://docs.cloud.google.com/kms/docs/resource-hierarchy#retrieve_resource_id) for the expected format.



This is a local operation that will record the account details in the CLI configuration file, allowing you to sign and submit requests to the ledger on behalf of this account.

### Create a new account for you

New accounts can be created using the `ul-cli accounts create` sub-command. For example, to create a new user account, you can use:
    
    
    ul-cli accounts create account \
        --alias NEW_ACCOUNT_ALIAS \
        --key-name NEW_ACCOUNT_KMS_KEY \
        --comment "NEW_ACCOUNT_COMMENT" \
        --roles NEW_ACCOUNT_ROLES \
        --sender ACCOUNT_MANAGER_ALIAS

Replace the following:

  * `NEW_ACCOUNT_ALIAS`: a short string used locally by the CLI to identify this account in future command invocations.
  * `NEW_ACCOUNT_KMS_KEY`: the full resource ID of the Cloud KMS **key version** to be used by the new user account.
  * `NEW_ACCOUNT_COMMENT`: a string with any relevant information to record on the ledger associated with the new user account. This is an opaque value that is stored on ledger but not interpreted otherwise by the Universal Ledger. Once created, this field is immutable and readable by anyone with access to the network.
  * `NEW_ACCOUNT_ROLES`: a comma separated list of [Role](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#role) to be assigned to the new user account. For example: `payer`, `receiver`, `contract-creator`, or `contract-participant`.
  * `ACCOUNT_MANAGER_ALIAS`: the alias of an account manager previously registered or created with the CLI.



This will sign and submit a [CreateAccount](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#createaccount) transaction on behalf of the given account manager.

Run `ul-cli accounts create --help` to view the options available for other kinds of accounts to create.

### Create a new account for someone else

To create an account for someone else, ask them to share with you their public key with you and store it in a file. It's generally recommended that you use PEM encoding format for keys. For example, if their signing key uses the P-256 elliptic curve with SHA256 digest, save it in a file named `pem_ec_p256_sha256.pub`:
    
    
    -----BEGIN PUBLIC KEY-----
    MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEJ/vWkd5wgakFbVD25k8WM9Ll6We+
    c8RVDS0R4G8xetsmFjfNW/ZxwWeB86IvMjxY8ZsdU9+W7BL5YM6rUB5yCQ==
    -----END PUBLIC KEY-----
    

Then, run the following command to create the account:
    
    
    ul-cli accounts create account \
        --alias NEW_ACCOUNT_ALIAS \
        --public-key "$(cat pem_ec_p256_sha256.pub)" \
        --key-format pem_ec_p256_sha256 \
        --comment "NEW_ACCOUNT_COMMENT" \
        --roles NEW_ACCOUNT_ROLES \
        --sender ACCOUNT_MANAGER_ALIAS

Replace the following:

  * `NEW_ACCOUNT_ALIAS`: a short string used locally by the CLI to identify this account in future command invocations. Note, however, since you don't have its private key, you won't be able to sign or submit transactions.
  * `NEW_ACCOUNT_COMMENT`: a string with any relevant information to record on the ledger associated with the new user account. This is an opaque value that is stored on ledger but not interpreted otherwise by the Universal Ledger. Once created, this field is immutable and readable by anyone with access to the network.
  * `NEW_ACCOUNT_ROLES`: a comma separated list of [Role](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#role) to be assigned to the new user account. For example: `payer`, `receiver`, `contract-creator`, or `contract-participant`.
  * `ACCOUNT_MANAGER_ALIAS`: the alias of an account manager previously registered or created with the CLI.



This will sign and submit a [CreateAccount](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#createaccount) transaction on behalf of the given account manager.

The `--public-key` and `--key-format` flags are available for all `accounts create` sub-commands, so you can use them to create other kinds of accounts too. For alternative supported public key formats, see [KeyFormat](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#keyformat) in the Universal Ledger API reference.

### List managed accounts

Run the following command to view all of the accounts locally registered or created with the Universal Ledger CLI:
    
    
    ul-cli accounts list

## Explore other commands

Use the `--help` flag to explore all other commands and subcommands available on the Universal Ledger CLI.

For example, to view the top level commands available run:
    
    
    ul-cli --help

This includes subcommands to submit other kinds of transactions such as:

  * `accounts`: to register or create accounts, and perform management operations on existing accounts such as adding or removing roles, and querying account details.
  * `contracts`: to deploy, grant permissions, and invoke methods on programmable contracts.
  * `issuance`: for a clearinghouse to increase or decrease the issuance limit of a token manager, and to perform settlement operations.
  * `tokens`: for a token manager to mint or burn tokens on a user account.
  * `wallet`: for a user account to transfer an amount from their balance to another user account.



## What's next

  * Learn [how to send RPC requests](https://docs.cloud.google.com/universal-ledger/tutorial/send-rpc-request-py) to the Universal Ledger API.
  * Consult the [Universal Ledger API reference](https://docs.cloud.google.com/universal-ledger/reference/rpc).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-02 UTC."],[],[]] 
