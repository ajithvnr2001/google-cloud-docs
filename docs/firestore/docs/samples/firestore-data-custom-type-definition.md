---
url: https://docs.cloud.google.com/firestore/docs/samples/firestore-data-custom-type-definition/
title: Use a custom type on the client for Firestore documents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:26:08.861236+00:00
---

# Use a custom type on the client for Firestore documents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/docs/samples/firestore-data-custom-type-definition/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)
  * [ Samples ](https://docs.cloud.google.com/firestore/docs/samples)



#  Use a custom type on the client for Firestore documents Stay organized with collections  Save and categorize content based on your preferences. 

Use a custom type on the client for Firestore documents

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Add and update data](https://docs.cloud.google.com/firestore/native/docs/manage-data/add-data)
  * [Getting data](https://docs.cloud.google.com/firestore/native/docs/query-data/get-data)
  * [Query and filter data](https://docs.cloud.google.com/firestore/native/docs/query-data/queries)



## Code sample

### C#

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    [FirestoreData]
    public class City
    {
        [FirestoreProperty]
        public string Name { get; set; }
    
        [FirestoreProperty]
        public string State { get; set; }
    
        [FirestoreProperty]
        public string Country { get; set; }
    
        [FirestoreProperty]
        public bool Capital { get; set; }
    
        [FirestoreProperty]
        public long Population { get; set; }
    }

### Go

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // City represents a city.
    type City struct {
    	Name       string   `firestore:"name,omitempty"`
    	State      string   `firestore:"state,omitempty"`
    	Country    string   `firestore:"country,omitempty"`
    	Capital    bool     `firestore:"capital,omitempty"`
    	Population int64    `firestore:"population,omitempty"`
    	Density    int64    `firestore:"density,omitempty"`
    	Regions    []string `firestore:"regions,omitempty"`
    }
    

### Java

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    public City() {
      // Must have a public no-argument constructor
    }
    
    // Initialize all fields of a city
    public City(
        String name,
        String state,
        String country,
        Boolean capital,
        Long population,
        List<String> regions) {
      this.name = name;
      this.state = state;
      this.country = country;
      this.capital = capital;
      this.population = population;
      this.regions = regions;
    }
    

### PHP

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    class City
    {
        /** @var string */
        public $name;
        /** @var string */
        public $state;
        /** @var string */
        public $country;
        /** @var bool */
        public $capital;
        /** @var int */
        public $population;
        /** @var array<string> */
        public $regions;
    
        /**
         * @param array<string> $regions
         */
        public function __construct(
            string $name,
            string $state,
            string $country,
            bool $capital = false,
            int $population = 0,
            array $regions = []
        ) {
            $this->name = $name;
            $this->state = $state;
            $this->country = $country;
            $this->capital = $capital;
            $this->population = $population;
            $this->regions = $regions;
        }
    
        /**
         * @param array<mixed> $source
         */
        public static function fromArray(array $source): City
        {
            // implementation of fromArray is excluded for brevity
            # ...
        }
    
        /**
         * @return array<mixed>
         */
        public function toArray(): array
        {
            // implementation of toArray is excluded for brevity
            # ...
        }
    
        public function __toString()
        {
            // implementation of __toString is excluded for brevity
            # ...
        }
    }
    

### Python

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    class City:
        def __init__(self, name, state, country, capital=False, population=0, regions=[]):
            self.name = name
            self.state = state
            self.country = country
            self.capital = capital
            self.population = population
            self.regions = regions
    
        @staticmethod
        def from_dict(source):
            # ...
    
        def to_dict(self):
            # ...
    
        def __repr__(self):
            return f"City(\
                    name={self.name}, \
                    country={self.country}, \
                    population={self.population}, \
                    capital={self.capital}, \
                    regions={self.regions}\
                )"
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=firestore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
