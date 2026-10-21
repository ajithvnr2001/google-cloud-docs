---
url: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/configuration/lifecycle/
title: Package lifecycle \u00a0|\u00a0 Manufacturing Data Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:59:40.234747+00:00
---

# Package lifecycle  |  Manufacturing Data Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/configuration/lifecycle/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Manufacturing Data Engine ](https://docs.cloud.google.com/manufacturing-data-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/manufacturing-data-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Package lifecycle

This page describes Manufacturing Data Engine (MDE)'s package lifecycle.

## Upload a new configuration package

You can upload a new MDE's configuration package using the a REST endpoint or from the MDE web interface by providing a single `*.zip` file.

### REST

Execute the REST API request with the following information:

  * **Method** : POST.
  * **Endpoint** : `/configuration/v1/configuration-packages`.
  * **Request body** : `multiform data with key=”packageArchive”, value=configuration-package-zip file`.
  * **Response code** : 200 OK.
  * **Response body (JSON)** :
        
        {
            "id": "4adaecc2-54b9-482b-90d6-380f5d4b2be6",
            "name": "basic-configuration",
            "provider": "google",
            "latestStatus": "ACTIVATED",
            "status": [
                {
                    "code": "NOT_LOADED",
                    "updatedTime": "1742566718210",
                    "messages": []
                },
                {
                    "code": "VALIDATED",
                    "updatedTime": "1742566718210",
                    "messages": [
                        {
                            "severity": "INFO",
                            "message": "Successfully validated all message classes in the package"
                        },
                        {
                            "severity": "INFO",
                            "message": "Successfully validated all parsers in the package"
                        },
                        {
                            "severity": "INFO",
                            "message": "Successfully validated all types in the package"
                        }
                    ]
                },
                {
                    "code": "LOADED",
                    "updatedTime": "1742566718696",
                    "messages": [
                        {
                            "severity": "INFO",
                            "message": "Successfully applied all message classes in the package"
                        },
                        {
                            "severity": "INFO",
                            "message": "Successfully applied all types in the package"
                        },
                        {
                            "severity": "INFO",
                            "message": "Successfully applied all parsers in the package"
                        }
                    ]
                },
                {
                    "code": "ACTIVATED",
                    "updatedTime": "1742566718792",
                    "messages": [
                        {
                            "severity": "INFO",
                            "message": "Successfully activated all ingestion-specification, if there is any, in the package"
                        },
                        {
                            "severity": "INFO",
                            "message": "Successfully activated all message classes, if there is any, in the package"
                        },
                        {
                            "severity": "INFO",
                            "message": "Successfully activated all buckets, if there is any, in the package"
                        },
                        {
                            "severity": "INFO",
                            "message": "Successfully activated all metadata instance, if there is any, in the package"
                        },
                        {
                            "severity": "INFO",
                            "message": "Successfully activated all types, if there is any, in the package"
                        },
                        {
                            "severity": "INFO",
                            "message": "Successfully activated all parsers, if there is any, in the package"
                        }
                    ]
                }
            ]
        }
        




### Console

  1. Click **Cloud Configuration**.
  2. Click **ADD NEW CONFIGURATION PACKAGE**.
  3. Select the file to upload to the console.
  4. Click **UPLOAD**.



![New configuration package](https://docs.cloud.google.com/static/manufacturing-data-engine/images/configuration-packages-add-new-console.png)

After the package is uploaded, MDE will process it by running the following stages:

  1. **Validation** : In this stage, MDE validates the contents of the package, it ensures that all the files are syntactically correct and that they are in the right place. If this phase is successfully completed, then MDE proceeds to the next stage.

  2. **Loading** : In this stage, MDE tries to load and merge the configurations specified in the package with the current environment configurations. It checks any dependencies and makes sure that there are no naming collisions with existing configurations. This stage is atomic, which means that the package will either successfully be loaded, or it will be rolled-back completely. If the loading is successful, then MDE will proceed with the next stage.

  3. **Activation** : In this stage MDE activates the configuration and makes it visible to the rest of the environment users. It also triggers the creation of any infrastructure elements required as part of the package configuration (for example, activating a type).


**Note:** After the configuration package activation, MDE will _not_ activate the parsers contained in the configuration package (if there are any). You must activate the parsers manually. This directs the traffic to the configuration entities of the new package.

MDE v1.5.0 doesn't support updates for already deployed or activated packages. You can upload the same package again as long as it isn't active if this is required to fix any errors in either the validation or the loading stages. Once the package is set to active, you can't upload the same package again or upload a package that contains configuration entities with conflicting names.

## List existing configuration packages

You can list existing MDE's configuration package using the a REST endpoint or from the MDE web interface.

### REST

Execute the REST API request with the following information:

  * **Method** : GET.
  * **Endpoint** : `/configuration/v1/configuration-packages`.
  * **Response code** : 200 OK.
  * **Response body (JSON)** :
        
        {
            "configurationPackages": [
                {
                    "id": "0505ed17-ad20-458d-9128-d44783704acb",
                    "name": "default-configuration-package",
                    "provider": "google",
                    "latestStatus": "ACTIVATED",
                    "status": [
                        {
                            "code": "NOT_LOADED",
                            "updatedTime": "1742501535249",
                            "messages": []
                        },
                        {
                            "code": "VALIDATED",
                            "updatedTime": "1742501535249",
                            "messages": [
                                {
                                    "severity": "INFO",
                                    "message": "Successfully validated all buckets in the package"
                                },
                                {
                                    "severity": "INFO",
                                    "message": "Successfully validated all message classes in the package"
                                },
                                {
                                    "severity": "INFO",
                                    "message": "Successfully validated all metadata-instances in the package"
                                },
                                {
                                    "severity": "INFO",
                                    "message": "Successfully validated all parsers in the package"
                                },
                                {
                                    "severity": "INFO",
                                    "message": "Successfully validated all types in the package"
                                }
                            ]
                        },
                        {
                            "code": "LOADED",
                            "updatedTime": "1742501536740",
                            "messages": [
                                {
                                    "severity": "INFO",
                                    "message": "Successfully applied all message classes in the package"
                                },
                                {
                                    "severity": "INFO",
                                    "message": "Successfully applied all buckets in the package"
                                },
                                {
                                    "severity": "INFO",
                                    "message": "Successfully validated all metadata-instances in the package"
                                },
                                {
                                    "severity": "INFO",
                                    "message": "Successfully applied all types in the package"
                                },
                                {
                                    "severity": "INFO",
                                    "message": "Successfully applied all parsers in the package"
                                }
                            ]
                        },
                        {
                            "code": "ACTIVATED",
                            "updatedTime": "1742501537289",
                            "messages": [
                                {
                                    "severity": "INFO",
                                    "message": "Successfully activated all ingestion-specification, if there is any, in the package"
                                },
                                {
                                    "severity": "INFO",
                                    "message": "Successfully activated all message classes, if there is any, in the package"
                                },
                                {
                                    "severity": "INFO",
                                    "message": "Successfully activated all buckets, if there is any, in the package"
                                },
                                {
                                    "severity": "INFO",
                                    "message": "Successfully activated all metadata instance, if there is any, in the package"
                                },
                                {
                                    "severity": "INFO",
                                    "message": "Successfully activated all types, if there is any, in the package"
                                },
                                {
                                    "severity": "INFO",
                                    "message": "Successfully activated all parsers, if there is any, in the package"
                                }
                            ]
                        }
                    ]
                },
                {
                    "id": "4adaecc2-54b9-482b-90d6-380f5d4b2be6",
                    "name": "basic-configuration",
                    "provider": "google",
                    "latestStatus": "ACTIVATED",
                    "status": [
                        {
                            "code": "NOT_LOADED",
                            "updatedTime": "1742566718210",
                            "messages": []
                        },
                        {
                            "code": "VALIDATED",
                            "updatedTime": "1742566718210",
                            "messages": [
                                {
                                    "severity": "INFO",
                                    "message": "Successfully validated all message classes in the package"
                                },
                                {
                                    "severity": "INFO",
                                    "message": "Successfully validated all parsers in the package"
                                },
                                {
                                    "severity": "INFO",
                                    "message": "Successfully validated all types in the package"
                                }
                            ]
                        },
                        {
                            "code": "LOADED",
                            "updatedTime": "1742566718696",
                            "messages": [
                                {
                                    "severity": "INFO",
                                    "message": "Successfully applied all message classes in the package"
                                },
                                {
                                    "severity": "INFO",
                                    "message": "Successfully applied all types in the package"
                                },
                                {
                                    "severity": "INFO",
                                    "message": "Successfully applied all parsers in the package"
                                }
                            ]
                        },
                        {
                            "code": "ACTIVATED",
                            "updatedTime": "1742566718792",
                            "messages": [
                                {
                                    "severity": "INFO",
                                    "message": "Successfully activated all ingestion-specification, if there is any, in the package"
                                },
                                {
                                    "severity": "INFO",
                                    "message": "Successfully activated all message classes, if there is any, in the package"
                                },
                                {
                                    "severity": "INFO",
                                    "message": "Successfully activated all buckets, if there is any, in the package"
                                },
                                {
                                    "severity": "INFO",
                                    "message": "Successfully activated all metadata instance, if there is any, in the package"
                                },
                                {
                                    "severity": "INFO",
                                    "message": "Successfully activated all types, if there is any, in the package"
                                },
                                {
                                    "severity": "INFO",
                                    "message": "Successfully activated all parsers, if there is any, in the package"
                                }
                            ]
                        }
                    ]
                }
            ],
            "nextPageToken": ""
        }
        




### Console

You can see the list of existing **configuration packages** on the **Cloud Configuration** section, in the **Configurations** page.

![Lists configuration package](https://docs.cloud.google.com/static/manufacturing-data-engine/images/configuration-packages-list-console.png)

## Delete an existing configuration package

Starting in v1.5.0, MDE supports an environment flag that can change the environment to [development mode](https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/operate/development-mode), which lets you delete configuration entities and delete configuration packages. After this mode is set, you can then delete an already activated package using the REST endpoint or the MDE web interface delete button.

**Warning:** Deleting a package will result in deleting all the configuration, infrastructure, and **data** for that configuration package. If the package contains types, then the table of that type will be deleted along with its data from BigQuery, and the other sinks. Similarly, if the package contains a bucket, then the bucket along with its metadata instances will be deleted from BigQuery and from MDE internal databases. That's why these features are only enabled in development mode, and you should use them with caution.

### REST

Execute the REST API request with the following information:

  * **Method** : DELETE
  * **Endpoint** : `/configuration/v1/configuration-packages/$PACKAGE-ID`
  * **Response code** : 200 OK
  * **Response body (JSON)** :


    
    
    {
        "id": "87e160db-8ff9-403a-a873-e6674f6ac3cb",
        "name": "postman-test-configuration-package",
        "provider": "google",
        "latestStatus": "DELETED",
        "status": [
            {
                "code": "NOT_LOADED",
                "updatedTime": "1742550114832",
                "messages": []
            },
            {
                "code": "VALIDATED",
                "updatedTime": "1742550114832",
                "messages": [
                    {
                        "severity": "INFO",
                        "message": "Successfully validated all buckets in the package"
                    },
                    {
                        "severity": "INFO",
                        "message": "Successfully validated all ingestion-specifications in the package"
                    },
                    {
                        "severity": "INFO",
                        "message": "Successfully validated all message classes in the package"
                    },
                    {
                        "severity": "INFO",
                        "message": "Successfully validated all metadata-instances in the package"
                    },
                    {
                        "severity": "INFO",
                        "message": "Successfully validated all parsers in the package"
                    },
                    {
                        "severity": "INFO",
                        "message": "Successfully validated all types in the package"
                    }
                ]
            },
            {
                "code": "LOADED",
                "updatedTime": "1742550115241",
                "messages": [
                    {
                        "severity": "INFO",
                        "message": "Successfully applied all ingestion-specification in the package"
                    },
                    {
                        "severity": "INFO",
                        "message": "Successfully applied all message classes in the package"
                    },
                    {
                        "severity": "INFO",
                        "message": "Successfully applied all buckets in the package"
                    },
                    {
                        "severity": "INFO",
                        "message": "Successfully validated all metadata-instances in the package"
                    },
                    {
                        "severity": "INFO",
                        "message": "Successfully applied all types in the package"
                    },
                    {
                        "severity": "INFO",
                        "message": "Successfully applied all parsers in the package"
                    }
                ]
            },
            {
                "code": "ACTIVATED",
                "updatedTime": "1742550115327",
                "messages": [
                    {
                        "severity": "INFO",
                        "message": "Successfully activated all ingestion-specification, if there is any, in the package"
                    },
                    {
                        "severity": "INFO",
                        "message": "Successfully activated all message classes, if there is any, in the package"
                    },
                    {
                        "severity": "INFO",
                        "message": "Successfully activated all buckets, if there is any, in the package"
                    },
                    {
                        "severity": "INFO",
                        "message": "Successfully activated all metadata instance, if there is any, in the package"
                    },
                    {
                        "severity": "INFO",
                        "message": "Successfully activated all types, if there is any, in the package"
                    },
                    {
                        "severity": "INFO",
                        "message": "Successfully activated all parsers, if there is any, in the package"
                    }
                ]
            },
            {
                "code": "DELETED",
                "updatedTime": "1742567553260",
                "messages": [
                    {
                        "severity": "INFO",
                        "message": "Successfully deleted all parsers, if there is any, in the package"
                    },
                    {
                        "severity": "INFO",
                        "message": "Successfully deleted all message classes, if there is any, in the package"
                    },
                    {
                        "severity": "INFO",
                        "message": "Successfully deleted all types, if there is any, in the package"
                    },
                    {
                        "severity": "INFO",
                        "message": "Successfully activated all metadata instance, if there is any, in the package"
                    },
                    {
                        "severity": "INFO",
                        "message": "Successfully deleted all buckets, if there is any, in the package"
                    },
                    {
                        "severity": "INFO",
                        "message": "Successfully deleted all ingestion-specification, if there is any, in the package"
                    }
                ]
            }
        ]
    }
    

### Console

  1. Click **Cloud Configuration**.
  2. Select the configuration package to delete.
  3. Click **Actions**.
  4. Click **Delete**.

![Delete configuration package](https://docs.cloud.google.com/static/manufacturing-data-engine/images/configuration-packages-delete-console.png)

  5. Confirm you are sure of deleting the selected configuration package by clicking **Remove**.




![Confirmation of deleting configuration package](https://docs.cloud.google.com/static/manufacturing-data-engine/images/configuration-packages-delete-confirmation-console.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
