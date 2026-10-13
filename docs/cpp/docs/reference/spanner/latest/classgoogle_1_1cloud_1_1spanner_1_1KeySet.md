---
url: https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1KeySet/
title: Class KeySet (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:45:53.428148+00:00
---

# Class KeySet (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1KeySet/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class KeySet (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

The [`KeySet`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1KeySet) class is a regular type that represents a collection of `Key`s. 

Users can construct a [`KeySet`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1KeySet) instance, then add `Key`s and ranges of `Key`s to the set. The caller is responsible for ensuring that all keys in a given [`KeySet`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1KeySet) instance contain the same number and types of values.

Users may also optionally construct an instance that represents all keys with [`KeySet::All()`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1KeySet#classgoogle_1_1cloud_1_1spanner_1_1KeySet_1a3796d3d86841ed54837c25376a810302).

###### Example
    
    
      auto delete_albums = spanner::DeleteMutationBuilder(
                               "Albums", spanner::KeySet()
                                             .AddKey(spanner::MakeKey(2, 1))
                                             .AddKey(spanner::MakeKey(2, 3)))
                               .Build();
    

###### Example
    
    
    void DeleteAll(google::cloud::spanner::Client client) {
      namespace spanner = ::google::cloud::spanner;
    
      // Delete all the performances, venues, albums and singers.
      auto commit = client.Commit(spanner::Mutations{
          spanner::MakeDeleteMutation("Performances", spanner::KeySet::All()),
          spanner::MakeDeleteMutation("Venues", spanner::KeySet::All()),
          spanner::MakeDeleteMutation("Albums", spanner::KeySet::All()),
          spanner::MakeDeleteMutation("Singers", spanner::KeySet::All()),
      });
      if (!commit) throw std::move(commit).status();
      std::cout << "delete-all was successful\n";
    }
    

## Constructors 

### KeySet()

Constructs an empty [`KeySet`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1KeySet). 

### KeySet(KeySet const &)

**Parameter**  
---  
**Name** | **Description**  
`` |  `KeySet const &`   
  
  
### KeySet(KeySet &&)

**Parameter**  
---  
**Name** | **Description**  
`` |  `KeySet &&`   
  
  
## Operators 

### operator=(KeySet const &)

**Parameter**  
---  
**Name** | **Description**  
`` |  `KeySet const &`   
  
**Returns**  
---  
**Type** | **Description**  
`KeySet &` |   
  
### operator=(KeySet &&)

**Parameter**  
---  
**Name** | **Description**  
`` |  `KeySet &&`   
  
**Returns**  
---  
**Type** | **Description**  
`KeySet &` |   
  
## Functions 

### static All()

Returns a [`KeySet`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1KeySet) that represents the set of "All" keys for the index. 

###### Example
    
    
    void DeleteAll(google::cloud::spanner::Client client) {
      namespace spanner = ::google::cloud::spanner;
    
      // Delete all the performances, venues, albums and singers.
      auto commit = client.Commit(spanner::Mutations{
          spanner::MakeDeleteMutation("Performances", spanner::KeySet::All()),
          spanner::MakeDeleteMutation("Venues", spanner::KeySet::All()),
          spanner::MakeDeleteMutation("Albums", spanner::KeySet::All()),
          spanner::MakeDeleteMutation("Singers", spanner::KeySet::All()),
      });
      if (!commit) throw std::move(commit).status();
      std::cout << "delete-all was successful\n";
    }
    

**Returns**  
---  
**Type** | **Description**  
`KeySet` |   
  
### AddKey(Key)

Adds the given `key` to the [`KeySet`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1KeySet). 

###### Example
    
    
      auto delete_albums = spanner::DeleteMutationBuilder(
                               "Albums", spanner::KeySet()
                                             .AddKey(spanner::MakeKey(2, 1))
                                             .AddKey(spanner::MakeKey(2, 3)))
                               .Build();
    

**Parameter**  
---  
**Name** | **Description**  
`key` |  `Key`   
  
**Returns**  
---  
**Type** | **Description**  
`KeySet &` |   
  
### AddRange(KeyBound, KeyBound)

Adds a range of keys defined by the given [`KeyBound`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1KeyBound)s. 

###### Example
    
    
      auto delete_albums = spanner::DeleteMutationBuilder(
                               "Albums", spanner::KeySet()
                                             .AddKey(spanner::MakeKey(2, 1))
                                             .AddKey(spanner::MakeKey(2, 3)))
                               .Build();
    

**Parameters**  
---  
**Name** | **Description**  
`start` |  `KeyBound`   
  
`end` |  `KeyBound`   
  
**Returns**  
---  
**Type** | **Description**  
`KeySet &` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
