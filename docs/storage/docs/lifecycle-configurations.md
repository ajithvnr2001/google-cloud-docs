---
url: https://docs.cloud.google.com/storage/docs/lifecycle-configurations/
title: Configuration examples for Object Lifecycle Management \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:50.215587+00:00
---

# Configuration examples for Object Lifecycle Management  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/lifecycle-configurations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Configuration examples for Object Lifecycle Management Stay organized with collections  Save and categorize content based on your preferences. 

[Overview](https://docs.cloud.google.com/storage/docs/lifecycle) [Setup](https://docs.cloud.google.com/storage/docs/managing-lifecycles)

This page shows example configurations for [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle). When you [set a lifecycle configuration on a bucket](https://docs.cloud.google.com/storage/docs/managing-lifecycles#set), current and future objects in the bucket that meet the [conditions](https://docs.cloud.google.com/storage/docs/lifecycle#conditions) you define have the specified [action](https://docs.cloud.google.com/storage/docs/lifecycle#actions) performed on them.

## Delete older object versions

**Warning:** This example involves deleting data. Once permanently deleted, objects cannot be recovered. Be familiar with your bucket's [soft delete](https://docs.cloud.google.com/storage/docs/soft-delete) configuration and take care in setting up your lifecycle rules so that you don't cause more data to be deleted than you intend. You should test your lifecycle rules on development data before applying to production to ensure your rules have the effect you intend.

The following lifecycle configuration defines two rules. Note that these rules are applicable only when [using Object Versioning](https://docs.cloud.google.com/storage/docs/using-object-versioning#set) on the bucket:

  1. Delete noncurrent versions of objects if there are 2 newer versions of the object in the bucket. Objects subject to this rule are permanently deleted and cannot be recovered.

  2. Delete noncurrent versions of objects after they've been noncurrent for 7 days. Objects subject to this rule are permanently deleted and cannot be recovered.




The combined effect of these two rules in buckets that use Object Versioning is that live objects have a window of time in which they can be [recovered](https://docs.cloud.google.com/storage/docs/using-versioned-objects#restore) if they get overwritten or deleted: such an object remains in the bucket in a noncurrent state for seven days or until 2 newer versions of the object exist in the bucket.

### Console

These settings use the instructions found in the [set a configuration](https://docs.cloud.google.com/storage/docs/managing-lifecycles#set) section.

  1. To delete noncurrent versions of objects if there is a newer version:

     1. Select the **Delete object** action.
     2. Select the **Live state** condition, and select the **Noncurrent** radio button.
     3. Select the **Number of newer versions** condition, and enter a value of **2**.
  2. To delete noncurrent versions of objects after they're been noncurrent for 7 days:

     1. Select the **Delete object** action.
     2. Select the **Days since becoming noncurrent** condition, and enter a value of **7**.



### Command line

The following lifecycle configuration can be applied to a bucket by [enabling lifecycle management](https://docs.cloud.google.com/storage/docs/managing-lifecycles#set).
    
    
    {
      "lifecycle": {
        "rule": [
          {
            "action": {"type": "Delete"},
            "condition": {
              "numNewerVersions": 2,
              "isLive": false
            }
          },
          {
            "action": {"type": "Delete"},
            "condition": {
              "daysSinceNoncurrentTime": 7
            }
          }
        ]
      }
    }
    

For the generalized format of a lifecycle configuration file, see the [bucket resource representation for JSON](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#resource-representations).

### REST APIs

### JSON API

The following lifecycle configuration can be applied to a bucket by [enabling lifecycle management](https://docs.cloud.google.com/storage/docs/managing-lifecycles#set).
    
    
    {
      "lifecycle": {
        "rule": [
          {
            "action": {"type": "Delete"},
            "condition": {
              "numNewerVersions": 2,
              "isLive": false
            }
          },
          {
            "action": {"type": "Delete"},
            "condition": {
              "daysSinceNoncurrentTime": 7
            }
          }
        ]
      }
    }
    

For the generalized format of a lifecycle configuration file, see the [bucket resource representation for JSON](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#resource-representations).

### XML API

The following lifecycle configuration can be applied to a bucket by [enabling lifecycle management](https://docs.cloud.google.com/storage/docs/managing-lifecycles#set).
    
    
    <?xml version="1.0" encoding="UTF-8" ?>
    <LifecycleConfiguration>
        <Rule>
            <Action>
                <Delete/>
            </Action>
            <Condition>
                <IsLive>false</IsLive>
                <NumberOfNewerVersions>2</Age>
            </Condition>
        </Rule>
        <Rule>
            <Action>
                <Delete/>
            </Action>
            <Condition>
                <DaysSinceNoncurrentTime>7</DaysSinceNoncurrentTime>
            </Condition>
        </Rule>
    </LifecycleConfiguration>
    

For the generalized format of a lifecycle configuration file, see the [lifecycle configuration format for XML](https://docs.cloud.google.com/storage/docs/xml-api/put-bucket-metadata#lifecycle-body).

### Configuration modifications

Depending on your goals, there are several modifications you could make to this example configuration:

  * If you wanted your live objects to have a limited lifetime, create an additional rule that uses the [`Delete`](https://docs.cloud.google.com/storage/docs/lifecycle#delete) action, an [`isLive`](https://docs.cloud.google.com/storage/docs/lifecycle#islive) condition set to `true`, and an [`age`](https://docs.cloud.google.com/storage/docs/lifecycle#age) condition.

  * If you wanted to protect your data from accidental deletion but not accidental overwrite, set the number of newer versions to 1, which also reduces storage costs, because you retain fewer versions of an object.



  * If your data is stored as Nearline storage, Coldline storage, or Archive storage, add an [`age`](https://docs.cloud.google.com/storage/docs/lifecycle#age) condition or use a larger value for [`daysSinceNoncurrentTime`](https://docs.cloud.google.com/storage/docs/lifecycle#dayssincenoncurrenttime) to avoid [early deletion fees](https://docs.cloud.google.com/storage/pricing#early-delete). Note that even with such changes, you might incur early deletion fees, depending on how frequently you overwrite and delete your objects.



## Change an object's storage class

The following lifecycle configuration defines two rules:

  1. Change the [storage class](https://docs.cloud.google.com/storage/docs/storage-classes) of an object to Nearline storage if its [age](https://docs.cloud.google.com/storage/docs/lifecycle#conditions) is greater than 365 days (one year), and its current storage class is Standard storage, and its name ends in either `.jpg` or `.png`.
  2. Change the storage class of an object to Coldline storage if its age is greater than 1095 days (three years), and its current storage class is Nearline storage, and its name ends in either `.jpg` or `.png`.



### Console

These settings use the instructions found in the [set a configuration](https://docs.cloud.google.com/storage/docs/managing-lifecycles#set) section.

  1. To move the objects to Nearline storage 365 days after they were created:

     1. Select the **Set storage class to Nearline** action.
     2. Select the **Object name matches suffix** rule scope.
     3. In the field that appears, type **.jpg** , and press enter. Then type **.png** , and press enter again.
     4. Select the **Age** condition, and enter a value of **365**.
     5. Select the **Storage class matches** condition, and choose the **Standard** option.
  2. To move the objects to Coldline storage 1095 days after they were created:

     1. Select the **Set storage class to Coldline** action.
     2. Select the **Object name matches suffix** rule scope.
     3. In the field that appears, type **.jpg** , and press enter. Then type **.png** , and press enter again.
     4. Select the **Age** condition, and enter a value of **1095**.
     5. Select the **Storage class matches** condition, and choose the **Nearline** option.



### Command line

The following lifecycle configuration can be applied to a bucket by [enabling lifecycle management](https://docs.cloud.google.com/storage/docs/managing-lifecycles#set).
    
    
    {
      "lifecycle": {
        "rule": [
          {
            "action": {
              "type": "SetStorageClass",
              "storageClass": "NEARLINE"
            },
            "condition": {
              "age": 365,
              "matchesStorageClass": [
                "STANDARD"
              ],
              "matchesSuffix": [
                ".jpg",
                ".png"
              ]
            }
          },
          {
            "action": {
              "type": "SetStorageClass",
              "storageClass": "COLDLINE"
            },
            "condition": {
              "age": 1095,
              "matchesStorageClass": [
                "NEARLINE"
              ],
              "matchesSuffix": [
                ".jpg",
                ".png"
              ]
            }
          }
        ]
      }
    }
    

For the generalized format of a lifecycle configuration file, see the [bucket resource representation for JSON](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#resource-representations).

### REST APIs

### JSON API

The following lifecycle configuration can be applied to a bucket by [enabling lifecycle management](https://docs.cloud.google.com/storage/docs/managing-lifecycles#set).
    
    
    {
      "lifecycle": {
        "rule": [
          {
            "action": {
              "type": "SetStorageClass",
              "storageClass": "NEARLINE"
            },
            "condition": {
              "age": 365,
              "matchesStorageClass": [
                "STANDARD"
              ],
              "matchesSuffix": [
                ".jpg",
                ".png"
              ]
            }
          },
          {
            "action": {
              "type": "SetStorageClass",
              "storageClass": "COLDLINE"
            },
            "condition": {
              "age": 1095,
              "matchesStorageClass": [
                "NEARLINE"
              ],
              "matchesSuffix": [
                ".jpg",
                ".png"
              ]
            }
          }
        ]
      }
    }
    

For the generalized format of a lifecycle configuration file, see the [bucket resource representation for JSON](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#resource-representations).

### XML API

The following lifecycle configuration can be applied to a bucket by [enabling lifecycle management](https://docs.cloud.google.com/storage/docs/managing-lifecycles#set).
    
    
    <?xml version="1.0" encoding="UTF-8" ?>
    <LifecycleConfiguration>
        <Rule>
            <Action>
                <SetStorageClass>NEARLINE</SetStorageClass>
            </Action>
            <Condition>
                <Age>365</Age>
                <MatchesStorageClass>STANDARD</MatchesStorageClass>
                <MatchesSuffix>.jpg</MatchesSuffix>
                <MatchesSuffix>.png</MatchesSuffix>
            </Condition>
        </Rule>
        <Rule>
            <Action>
                <SetStorageClass>COLDLINE</SetStorageClass>
            </Action>
            <Condition>
                <Age>1095</Age>
                <MatchesStorageClass>NEARLINE</MatchesStorageClass>
                <MatchesSuffix>.jpg</MatchesSuffix>
                <MatchesSuffix>.png</MatchesSuffix>
            </Condition>
        </Rule>
    </LifecycleConfiguration>
    

For the generalized format of a lifecycle configuration file, see the [lifecycle configuration format for XML](https://docs.cloud.google.com/storage/docs/xml-api/put-bucket-metadata#lifecycle-body).

Depending on your goals, you can add additional conditions to this example configuration. For example, you can add conditions based on the object size:

  * It might not be cost-effective to transition very small objects to colder storage classes. If you only wanted to change the storage class of objects that are larger than 5 MiB, for example, add a [`sizeAboveBytes` condition](https://docs.cloud.google.com/storage/docs/lifecycle#size-above-below-bytes) with the value `5242880`.
  * If you wanted to change the storage class of objects that are within a size range, use both the [`sizeAboveBytes` and `sizeBelowBytes` conditions](https://docs.cloud.google.com/storage/docs/lifecycle#size-above-below-bytes) in the same rule.



## Remove the lifecycle configuration

When [set on a bucket](https://docs.cloud.google.com/storage/docs/managing-lifecycles#set), the following lifecycle configuration disables lifecycle management by removing all rules:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket for which you want to remove lifecycle rules.

  3. Click the **Lifecycle** tab.

  4. Do either of the following things:

     * To remove all rules, click **Delete all**.

     * To remove individual rules, click delete **Delete this rule from your bucket** for the rule that you want to delete.




### Command line

Use the [`gcloud storage buckets update`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/update) command with the `--clear-lifecycle` flag:
    
    
    gcloud storage buckets update gs://BUCKET_NAME --clear-lifecycle

Where BUCKET_NAME is the name of the bucket whose lifecycle configuration you want to remove.

### REST APIs

### JSON API
    
    
    {
      "lifecycle": {
        "rule": []
      }
    }
    

For the generalized format of a lifecycle configuration file, see the [bucket resource representation for JSON](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#resource-representations).

### XML API
    
    
    <?xml version="1.0" encoding="UTF-8" ?>
    <LifecycleConfiguration/>
    

For the generalized format of a lifecycle configuration file, see the [lifecycle configuration format for XML](https://docs.cloud.google.com/storage/docs/xml-api/put-bucket-metadata#lifecycle-body).

## What's next

  * Learn more about [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle), including the available lifecycle actions and lifecycle conditions.
  * [Set and view the lifecycle configuration](https://docs.cloud.google.com/storage/docs/managing-lifecycles) on a bucket.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
