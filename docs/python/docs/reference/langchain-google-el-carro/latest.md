---
url: https://docs.cloud.google.com/python/docs/reference/langchain-google-el-carro/latest/
title: Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:28:37.258667+00:00
---

# Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/langchain-google-el-carro/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# El Carro for Oracle Databases for LangChain

[![image](https://img.shields.io/badge/support-preview-orange.svg)](https://github.com/googleapis/google-cloud-python/blob/main/README.rst#stability-levels) [![image](https://img.shields.io/pypi/v/langchain-google-el-carro.svg)](https://pypi.org/project/langchain-google-el-carro/) [![image](https://img.shields.io/pypi/pyversions/langchain-google-el-carro.svg)](https://pypi.org/project/langchain-google-el-carro/)

  * [Client Library Documentation](https://cloud.google.com/python/docs/reference/langchain-google-el-carro/latest)

  * [Product Documentation](https://github.com/GoogleCloudPlatform/elcarro-oracle-operator)




## Known Limitations

  * The library supports El Carro Operator for Oracle 18c and higher versions.

  * By default the library uses [thin mode.](https://python-oracledb.readthedocs.io/en/latest/user_guide/appendix_b.html) for Oracle connectivity, to use thick mode please follow the corresponding section..

  * To use VARCHAR2 datatype of size more than 4000 please change the parameter [MAX_STRING_SIZE.](https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/MAX_STRING_SIZE.html#GUID-D424D23B-0933-425F-BC69-9C0E6724693C) in the Oracle instance.




## Quick Start

### Create an El Carro Operator Oracle Instance and a Database (PDB)

In order to use this library, you first need to have an El Carro Operator software running with an Instance (CDB) and a Database (PDB).

Please follow the steps for El Carro Oracle Operator to provision a new database and create a PDB:

  * [El Carro Oracle 18c XE quickstart](https://github.com/GoogleCloudPlatform/elcarro-oracle-operator/blob/main/docs/content/quickstart-18c-xe.md)

  * [El Carro Oracle 19c EE quickstart](https://github.com/GoogleCloudPlatform/elcarro-oracle-operator/blob/main/docs/content/quickstart-19c-ee.md)




### Installation

Install this library in a [virtualenv](https://virtualenv.pypa.io/en/latest/) using pip. [virtualenv](https://virtualenv.pypa.io/en/latest/) is a tool to create isolated Python environments. The basic problem it addresses is one of dependencies and versions, and indirectly permissions.

With [virtualenv](https://virtualenv.pypa.io/en/latest/), it’s possible to install this library without needing system install permissions, and without clashing with the installed system dependencies.

#### Supported Python Versions

Python >= 3.8

#### Mac/Linux
    
    
    pip install virtualenv
    virtualenv <your-env>
    source <your-env>/bin/activate
    <your-env>/bin/pip install langchain-google-el-carro
    

#### Windows
    
    
    pip install virtualenv
    virtualenv <your-env>
    <your-env>\Scripts\activate
    <your-env>\Scripts\pip.exe install langchain-google-el-carro
    

### Document Loader Usage

Use a document loader to load data as LangChain `Document`s.
    
    
    from langchain_google_el_carro import ElCarroEngine
    from langchain_google_el_carro.loader import \
        ElCarroLoader, ElCarroDocumentSaver
    
    elcarro_engine = ElCarroEngine.from_instance(
        "Your El Carro endpoint hostname", # e.g. 127.0.0.1
        "Your El Carro endpoint port", # e.g. 3307
        "Your PDB name",  # e.g. PDB1
        "Your DB user",
        "Your DB password",
    )
    loader = ElCarroLoader(
        elcarro_engine,
        table_name="my-table-name"
    )
    docs = loader.lazy_load()
    

See the full [Document Loader](https://github.com/googleapis/langchain-google-el-carro-python/blob/main/docs/document_loader.ipynb) tutorial.

## Chat Message History Usage

Use `ChatMessageHistory` to store messages and provide conversation history to LLMs.
    
    
    from langchain_google_el_carro import ElCarroEngine
    from langchain_google_el_carro.chat_message_history import \
        ElCarroChatMessageHistory
    
    elcarro_engine = ElCarroEngine.from_instance(
        "Your El Carro endpoint hostname", # e.g. 127.0.0.1
        "Your El Carro endpoint port", # e.g. 3307
        "Your PDB name",  # e.g. PDB1
        "Your DB user",
        "Your DB password",
    )
    history = ElCarroChatMessageHistory(
        elcarro_engine=elcarro_engine,
        table_name="my-message-store",
        session_id="my-session_id"
    )
    

See the full [Chat Message History](https://github.com/googleapis/langchain-google-el-carro-python/blob/main/docs/chat_message_history.ipynb) tutorial.

## Oracle Thick Mode Connectivity

Thick mode connectivity requires you to install the Oracle Client libraries and pass `thick_mode=True` to `ElCarroEngine`. Follow these sections of the oracledb installation guide:

  * [Oracle Instant Client Zip Files](https://python-oracledb.readthedocs.io/en/latest/user_guide/installation.html#oracle-instant-client-zip-files)

  * [Oracle Instant Client RPMs](https://python-oracledb.readthedocs.io/en/latest/user_guide/installation.html#oracle-instant-client-rpms)




Example for Linux x64, glibc 2.14+:
    
    
    wget https://download.oracle.com/otn_software/linux/instantclient/2113000/instantclient-basic-linux.x64-21.13.0.0.0dbru.zip -O /tmp/drv.zip
    rm -fr /tmp/instantclient_21_13/; unzip /tmp/drv.zip -d /tmp
    export LD_LIBRARY_PATH=/tmp/instantclient_21_13/:$LD_LIBRARY_PATH
    

### Contributions

Contributions to this library are always welcome and highly encouraged.

See [CONTRIBUTING](https://github.com/googleapis/langchain-google-el-carro-python/blob/main/CONTRIBUTING.md) for more information how to get started.

Please note that this project is released with a Contributor Code of Conduct. By participating in this project you agree to abide by its terms. See [Code of Conduct](https://github.com/googleapis/langchain-google-el-carro-python/blob/main/CODE_OF_CONDUCT.md) for more information.

## License

Apache 2.0 - See [LICENSE](https://github.com/googleapis/langchain-google-el-carro-python/tree/main/LICENSE) for more information.

## Disclaimer

This is not an officially supported Google product.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-30 UTC."],[],[]] 
