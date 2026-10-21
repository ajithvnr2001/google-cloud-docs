---
url: https://docs.cloud.google.com/universal-ledger/reference/gculpy-language/
title: The GCULpy language \u00a0|\u00a0 Universal Ledger \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:02:06.785550+00:00
---

# The GCULpy language  |  Universal Ledger  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/universal-ledger/reference/gculpy-language/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Universal Ledger ](https://docs.cloud.google.com/universal-ledger)
  * [ Reference ](https://docs.cloud.google.com/universal-ledger/reference/rpc)



Send feedback 

#  The GCULpy language Stay organized with collections  Save and categorize content based on your preferences. 

**Private Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For information about access to this release, see the [ access request page](https://cloud.google.com/application/web3/universal-ledger). 

GCULpy is a strict statically typed subset of Python, designed to be safe, readable, and auditable. Its design intentionally limits certain dynamic features of Python to prevent common smart contract vulnerabilities and ensure that the behavior of a contract is always predictable.

This page provides a reference for the GCULpy language specification, covering the core concepts and the lifecycle of a contract on a Universal Ledger network.

## Core concepts

The following contract defines a sample **ERC20 token** in GCULpy:
    
    
    import gcul
    
    class ERC20Token(gcul.Contract):
        """Sample ERC20 implementation for the Universal Ledger."""
    
        symbol: str
        total_supply: int
        balance: dict[gcul.Account, int]
    
        def __init__(self, symbol: str):
            self.symbol = symbol
    
        def mint(self, beneficiary: gcul.Account, value: int) -> int:
            """Mints tokens to the given beneficiary."""
            assert self.is_owner(gcul.sender), "Only the owner can mint"
            assert value >= 0, "Mint amount must be non-negative"
            self.total_supply += value
            self.balance[beneficiary] += value
            return value
    
        def transfer(self, beneficiary: gcul.Account, value: int) -> int:
            """Transfers tokens from the sender to the given beneficiary."""
            assert value >= 0, "Transfer amount must be non-negative"
            assert (
                value <= self.balance[gcul.sender]
            ), "Sender does not have enough balance"
            self.balance[gcul.sender] -= value
            self.balance[beneficiary] += value
            return value
    

A GCULpy contract is a class that inherits from `gcul.Contract`. It contains **fields** (storing state) and **methods** (processing logic that operate on fields).

### Fields

State in a GCULpy contract is stored in fields. All fields must be declared with a static type at the class level. There are two kinds of fields:

  * **Contract fields** hold a single value stored with the contract itself. In the `ERC20Token` example, `symbol: str` and `total_supply: int` are contract fields.

  * **Account fields** store a separate value for each user account interacting with a contract. They are always declared as a dictionary (`dict`) with `gcul.Account` as the key, such as `balance: dict[gcul.Account, int]`. Before a contract can write to a user's account, the user must explicitly grant storage permission to the contract. Once the data is stored, only the contract instance can modify or delete it—the user cannot.




### Methods

Methods define the executable logic of a contract. They behave like Python methods and can read or modify the contract's fields.

  * `__init__`: The constructor is called only once when the contract is first deployed. It's used to set the initial state of the contract fields. Fields that are not assigned a value in the constructor get a suitable default, for example `0` for an `int` field or an empty dictionary for a `dict` field.

  * **Private methods** : Methods starting with an underscore (for example, `_internal_logic`) are private and can only be called by other methods within the same contract. The Universal Ledger interpreter enforces this constraint.

  * **Public methods** : Any method not starting with an underscore (`_`) is public. Public methods can be called by any user with the `ROLE_CONTRACT_PARTICIPANT` by submitting an [InvokeContractMethod](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#invokecontractmethod) transaction.




## Contract lifecycle

The following sections walk through the typical operations involved in the lifecycle of a GCULpy contract.

### Deploy a contract

First, you compile your GCULpy source code using the `gculpyc` compiler. Then, a user with the `ROLE_CONTRACT_CREATOR` may submit a [CreateContract](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#createcontract) transaction to deploy the compiled bytecode to a Universal Ledger network. For detailed instructions see the [Deploy a programmable contract](https://docs.cloud.google.com/universal-ledger/tutorial/deploy-contract) tutorial.

Such a transaction would look like:
    
    
    client_transaction {
      sender_id: "OWNER_ACCOUNT_ID"
      app {
        [type.googleapis.com/google.cloud.universalledger.v1.CreateContract] {
          contract_bytes: "COMPILED_BYTECODE"
          arguments {
            key: "symbol"
            value: { str_value: "US02079K1079" }
          }
        }
      }
    }
    

When the network processes this transaction:

  * The constructor, that is the `__init__` method, is executed to create a new contract instance.
  * The sender of the transaction becomes the **contract's owner**.
  * The contract instance is permanently stored in the ledger and assigned a unique **contract ID** which is returned as part of the transaction output.



### Grant permissions

Before a contract can store data in an **account field** on behalf of a user, the user must first grant it the storage permission. This is a critical security step. A user with a `ROLE_CONTRACT_PARTICIPANT` may submit a [GrantContractPermissions](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#grantcontractpermissions) transaction for a specific contract ID.
    
    
    client_transaction {
      sender_id: "PARTICIPANT_ACCOUNT_ID"
      app {
        [type.googleapis.com/google.cloud.universalledger.v1.GrantContractPermissions] {
          contract_id: "CONTRACT_ID"
          permissions: CONTRACT_PERMISSION_STORAGE
        }
      }
    }
    

When the network processes this transaction:

  * If the contract does not define any account fields, the transaction is rejected.
  * If the contract defines account fields, all of them are populated with default values (for example, `contract.balance[gcul.sender] = 0`). These values are then stored in the world state as part of the account's data, and the transaction sender is registered as participating with this specific contract instance.



### Invoke contract methods

Once a contract is deployed and any necessary permissions are granted, users can interact with it by calling its public methods. A user with a `ROLE_CONTRACT_PARTICIPANT` may submit an [InvokeContractMethod](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#invokecontractmethod) transaction specifying the contract ID, method name, and argument values.
    
    
    client_transaction {
      sender_id: "PARTICIPANT_ACCOUNT_ID"
      app {
        [type.googleapis.com/google.cloud.universalledger.v1.InvokeContractMethod] {
          contract_id: "CONTRACT_ID"
          method_name: "mint"
          arguments {
            key: "beneficiary"
            value: { account_id: "BENEFICIARY_ID" }
          }
          arguments {
            key: "value"
            value: { int_value: 10 }
          }
        }
      }
    }
    

When the network processes this transaction:

  * The contract instance associated with the provided `CONTRACT_ID` is retrieved.
  * The method `mint(beneficiary=Account("BENEFICIARY_ID"), value=10)` is executed. The `Account` object for the beneficiary is built and validated by the runtime. The method's logic may safely assume that the provided ID is valid and refers to an existing account on the ledger.
  * If the method fails for any reason, the transaction will fail and _no updates_ will be made to the contract's state.
  * If the method succeeds, the updated state of the contract is recorded in the world state.



## Language specification

GCULpy is designed for safety and predictability and, as such, disallows several Python features; these will be called out with the Restriction label. These restrictions are intended to be permanent language features, introduced to make the contract logic easier to read, audit, and analyze statically, limiting surprising or unsafe behaviors.

Other features are called out with the Roadmap label, these are on the implementation roadmap but not yet supported by the `gculpyc` compiler.

### Types

GCULpy supports a range of common variable types with a strong emphasis on static typing.

Core value types:

  * `int`, `bool`, `str`, `None` are already supported.
  * Roadmap `Decimal`, `bytes`, `Enum` are on the roadmap.
  * Restriction `float` and `complex` are not allowed.



Container types: 

  * `dict` is already supported.
  * Roadmap `list`, `tuple`, `set`, `dataclass` are on the roadmap.
  * Restriction Concrete types must be specified for values in a container, for example `dict[str, int]` is allowed, but a plain `dict` or `dict[str, Any]` are not.
  * Nesting of containers is supported, for example `dict[str, list[int]]`.



Restriction All variables—including contract and account fields, function parameters and return types—must be defined and typed statically. Their type cannot be changed at runtime and only concrete types are supported. Types cannot be used as values, for example they cannot be stored in variables or passed to functions as arguments. Trying to assign a value to an undeclared field will result in a compile-time error.

### Classes and inheritance

Initially, you can only define classes that are direct subclasses of the base `gcul.Contract` class. This strict rule prevents the complexities of full Python inheritance, which can introduce hard-to-find bugs and make code difficult to reason about. For security, attempting to override a property or method from a parent class will raise an error, providing a clear safeguard against unexpected behavior.

Roadmap GCULpy will offer more flexibility while maintaining its core principles. The roadmap includes support for **single inheritance** on user-defined classes with method overriding explicitly managed with an `@override` decorator. Additionally, the `super()` built-in will be only supported in its argument-free form, to ensure direct, predictable operations.

### The gcul module

GCULpy provides a built-in `gcul` module with essential types and variables for contract development.

#### class `gcul.Contract`

The base class for all contracts. You cannot create instances of it directly; contracts are only ever instantiated through [CreateContract](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#createcontract) transactions. Methods and properties from the base `gcul.Contract` class cannot be overridden in subclasses.

  * `Contract.is_owner(account: Account) -> bool`

Returns `True` if the provided account is the contract owner.




#### class `gcul.Account`

A built-in type representing a user account on the ledger. You cannot create `gcul.Account` objects directly; the runtime environment creates them for you and provides them as function or method arguments. When you pass an account ID as a transaction argument, the runtime automatically validates it. If it's a valid ID for a registered account, it's converted into a full account object. If not, the transaction fails. This ensures you only ever work with valid accounts.

The definition of the class is roughly equivalent to:
    
    
    @dataclasses.dataclass(frozen=True)
    class Account:
      """A valid account on the ledger."""
    
      id: str  # The ID of the account as a string.
    

#### `gcul.sender: gcul.Account`

A special variable, available in any method, that holds a reference to the account that signed and submitted the current transaction.

Roadmap Improving developers' ability to manage and interact with contracts and accounts—you will be able to pass references to contract objects as arguments, store them in fields, access their unique ID (`contract.id: str`). Similarly, it will be possible to store references to accounts objects and retrieve their IDs.

### Operators

Most operators available in Python are supported in GCULpy and work as expected.

  * Addition (`+`) and subtraction (`-`), including unary and binary forms.
  * Multiplication (`*`), floor division (`//`), and modulo (`%`).
  * Exponentiation (`**`) for positive exponents.
  * Comparisons (`<`, `<=`, `>`, `>=`, `==`, `!=`).
  * Bitwise and (`&`), or (`|`), xor (`^`), left shift (`<<`), right shift (`>>`), negation (`~`).
  * Boolean operations (`and`, `or`, `not`).
  * Roadmap Object identity (`is`).
  * Restriction Negative exponents are not allowed and raise a runtime error.
  * Restriction True division (`/`), as it has a `float` return type, is not allowed and results in a compile-time error.



### Control flow

Most control-flow statements from Python work in GCULpy with the same semantics:

  * `pass` statements.
  * internal function calls (same contract, non-recursive).
  * `assert` statements.
  * `if ... then .. else ...` statements.
  * `for VAR in CONTAINER` statements.
  * Roadmap external function calls (to any other contract, non-recursive).
  * Roadmap `break` and `continue` statements.
  * Roadmap `raise` and `try ... except` statements.
  * Roadmap `match` statements.
  * Roadmap `generators` and `yield` statements.
  * Roadmap context managers and `with` statements.



Restriction GCULpy is intentionally **Turing-incomplete** to prevent infinite loops, facilitate static analysis, and ensure predictable transaction processing costs. Here's how it enforces this:

  * **No infinite loops:** Iteration is only allowed using `for` loops over finite containers; `while` loops are not allowed. Some container updates, for example adding or removing elements to a list or keys to a dictionary, are not allowed while iterating over them.
  * **No recursion:** A function cannot call itself, either directly or indirectly. The runtime environment performs both static and runtime checks to detect and reject the use of recursion.
  * **No async control flow:** Use of `async` primitives is not allowed to maintain the core design principles of predictability, security, and deterministic execution. Asynchronous operations make it difficult to reason about the control flow of a program, often leading to vulnerabilities and race conditions.



### Built-in functions

Roadmap Here's a look at our roadmap for built-in functions with the most fundamental and commonly used functionality to build with confidence.

|  |  |   
---|---|---|---  
_A_  
`abs()`  
`all()`  
`any()` _B_  
`bin()`  
`bool()`  
`bytes()` _C_  
`chr()`  
_D_  
`dict()`  
`divmod()` |  _E_  
`enumerate()` _F_  
`format()`  
`frozenset()` _H_  
`hash()`  
`hex()` _I_  
`id()`  
`int()` _L_  
`len()`  
`list()` |  _M_  
`max()`  
`min()` _O_  
`oct()`  
`ord()` _P_  
`pow()`  
`property()` _R_  
`range()`  
`repr()`  
`reversed()` |  _S_  
`set()`  
`sorted()`  
`staticmethod()`  
`str()`  
`sum()`  
`super()` _T_  
`tuple()` _Z_  
`zip()`  
  
## Release notes

  * **28 Jan, 2026.** Early version of `gculpyc` compiler made available to participants in the Universal Ledger private preview. For a tutorial using the compiler, see [Deploy a programmable contract](https://docs.cloud.google.com/universal-ledger/tutorial/deploy-contract).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-24 UTC."],[],[]] 
