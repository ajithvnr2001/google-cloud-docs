---
url: https://docs.cloud.google.com/compute/docs/samples/compute-custom-machine-type-helper-class/
title: Create VMs with custom machine types \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:35.153821+00:00
---

# Create VMs with custom machine types  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-custom-machine-type-helper-class/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Create VMs with custom machine types Stay organized with collections  Save and categorize content based on your preferences. 

This sample demonstrates how to create custom machine types for use with Compute Engine instances. Custom machine types allow you to specify the exact number of cores and memory for your instance, providing greater flexibility and control over your compute resources.

## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"fmt"
    	"strings"
    )
    
    const (
    	n1       = "custom"
    	n2       = "n2-custom"
    	n2d      = "n2d-custom"
    	e2       = "e2-custom"
    	e2Micro  = "e2-custom-micro"
    	e2Small  = "e2-custom-small"
    	e2Medium = "e2-custom-medium"
    )
    
    type typeLimit struct {
    	allowedCores     []int
    	minMemPerCore    int
    	maxMemPerCore    int
    	allowExtraMemory bool
    	extraMemoryLimit int
    }
    
    func makeRange(start, end, step int) []int {
    	if step <= 0 || end < start {
    		return []int{}
    	}
    	s := make([]int, 0, 1+(end-start)/step)
    	for start <= end {
    		s = append(s, start)
    		start += step
    	}
    	return s
    }
    
    var (
    	cpuSeriesE2Limit = typeLimit{
    		allowedCores:  makeRange(2, 33, 2),
    		minMemPerCore: 512,
    		maxMemPerCore: 8192,
    	}
    	cpuSeriesE2MicroLimit  = typeLimit{minMemPerCore: 1024, maxMemPerCore: 2048}
    	cpuSeriesE2SmallLimit  = typeLimit{minMemPerCore: 2048, maxMemPerCore: 4096}
    	cpuSeriesE2MeidumLimit = typeLimit{minMemPerCore: 4096, maxMemPerCore: 8192}
    	cpuSeriesN2Limit       = typeLimit{
    		allowedCores:  append(makeRange(2, 33, 2), makeRange(36, 129, 4)...),
    		minMemPerCore: 512, maxMemPerCore: 8192,
    		allowExtraMemory: true,
    		extraMemoryLimit: 624 << 10,
    	}
    	cpuSeriesN2DLimit = typeLimit{
    		allowedCores:  []int{2, 4, 8, 16, 32, 48, 64, 80, 96},
    		minMemPerCore: 512, maxMemPerCore: 8192,
    		allowExtraMemory: true,
    		extraMemoryLimit: 768 << 10,
    	}
    	cpuSeriesN1Limit = typeLimit{
    		allowedCores:     append([]int{1}, makeRange(2, 97, 2)...),
    		minMemPerCore:    922,
    		maxMemPerCore:    6656,
    		allowExtraMemory: true,
    		extraMemoryLimit: 624 << 10,
    	}
    )
    
    type customMachineType struct {
    	zone, cpuSeries     string
    	memoryMb, coreCount int
    	typeLimit
    }
    
    // Validate whether the requested parameters are allowed.
    // Find more information about limitations of custom machine types at:
    // https://cloud.google.com/compute/docs/general-purpose-machines#custom_machine_types
    func validate(cmt *customMachineType) error {
    	// Check the number of cores
    	if len(cmt.typeLimit.allowedCores) > 0 {
    		coreExists := false
    		for _, v := range cmt.typeLimit.allowedCores {
    			if v == cmt.coreCount {
    				coreExists = true
    			}
    		}
    		if !coreExists {
    			return fmt.Errorf("invalid number of cores requested. Allowed number of cores for %v is: %v", cmt.cpuSeries, cmt.typeLimit.allowedCores)
    		}
    	}
    
    	// Memory must be a multiple of 256 MB
    	if cmt.memoryMb%256 != 0 {
    		return fmt.Errorf("requested memory must be a multiple of 256 MB")
    	}
    
    	// Check if the requested memory isn't too little
    	if cmt.memoryMb < cmt.coreCount*cmt.typeLimit.minMemPerCore {
    		return fmt.Errorf("requested memory is too low. Minimal memory for %v is %v MB per core", cmt.cpuSeries, cmt.typeLimit.minMemPerCore)
    	}
    
    	// Check if the requested memory isn't too much
    	if cmt.memoryMb > cmt.coreCount*cmt.typeLimit.maxMemPerCore && !cmt.typeLimit.allowExtraMemory {
    		return fmt.Errorf("requested memory is too large. Maximum memory allowed for %v is %v MB per core", cmt.cpuSeries, cmt.typeLimit.maxMemPerCore)
    	}
    	if cmt.memoryMb > cmt.typeLimit.extraMemoryLimit && cmt.typeLimit.allowExtraMemory {
    		return fmt.Errorf("requested memory is too large. Maximum memory allowed for %v is %v MB", cmt.cpuSeries, cmt.typeLimit.extraMemoryLimit)
    	}
    
    	return nil
    }
    
    // Srring returns the custom machine type in form of a string acceptable by Compute Engine API.
    func (t customMachineType) String() string {
    	containsString := func(s []string, str string) bool {
    		for _, v := range s {
    			if v == str {
    				return true
    			}
    		}
    
    		return false
    	}
    
    	if containsString([]string{e2Small, e2Micro, e2Medium}, t.cpuSeries) {
    		return fmt.Sprintf("zones/%v/machineTypes/%v-%v", t.zone, t.cpuSeries, t.memoryMb)
    	}
    
    	if t.memoryMb > t.coreCount*t.typeLimit.maxMemPerCore {
    		return fmt.Sprintf("zones/%v/machineTypes/%v-%v-%v-ext", t.zone, t.cpuSeries, t.coreCount, t.memoryMb)
    	}
    
    	return fmt.Sprintf("zones/%v/machineTypes/%v-%v-%v", t.zone, t.cpuSeries, t.coreCount, t.memoryMb)
    }
    
    // Returns machine type in a format without the zone. For example, n2-custom-0-10240.
    // This format is used to create instance templates.
    func (t customMachineType) machineType() string {
    	// Return machine type in a format without the zone. For example, n2-custom-0-10240.
    	// This format is used to create instance templates.
    	ss := strings.Split(t.String(), "/")
    	return ss[len(ss)-1]
    }
    
    func createCustomMachineType(zone, cpuSeries string, memoryMb, coreCount int, tl typeLimit) (*customMachineType, error) {
    	containsString := func(s []string, str string) bool {
    		for _, v := range s {
    			if v == str {
    				return true
    			}
    		}
    
    		return false
    	}
    
    	if containsString([]string{e2Small, e2Micro, e2Medium}, cpuSeries) {
    		coreCount = 2
    	}
    	cmt := &customMachineType{
    		zone:      zone,
    		cpuSeries: cpuSeries,
    		memoryMb:  memoryMb,
    		coreCount: coreCount,
    		typeLimit: tl,
    	}
    
    	if err := validate(cmt); err != nil {
    		return &customMachineType{}, err
    	}
    	return cmt, nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import java.util.Arrays;
    import java.util.Collections;
    import java.util.Map;
    import java.util.concurrent.ConcurrentHashMap;
    import java.util.stream.IntStream;
    
    public class HelperClass {
    
      /*
       * This class allows you to create custom machine types to be used with the VM instances.
       */
    
      static class CustomMachineType {
        String zone;
        String cpuSeries;
        int memory;
        int coreCount;
        TypeLimits typeLimit;
    
        CustomMachineType(String zone, String cpuSeries, int memory, int coreCount,
            TypeLimits typeLimit) {
          this.zone = zone;
          this.cpuSeries = cpuSeries;
          this.memory = memory;
          this.coreCount = coreCount;
          // Shared machine types (e2-small, e2-medium and e2-micro) always have
          // 2 vCPUs: https://cloud.google.com/compute/docs/general-purpose-machines#e2_limitations
          this.typeLimit = typeLimit;
        }
    
        @Override
        public String toString() {
          if (cpuSeries.equalsIgnoreCase(CpuSeries.E2_SMALL.cpuSeries)
              || cpuSeries.equalsIgnoreCase(CpuSeries.E2_MICRO.cpuSeries)
              || cpuSeries.equalsIgnoreCase(CpuSeries.E2_MEDIUM.cpuSeries)) {
            return String.format("zones/%s/machineTypes/%s-%d", zone, cpuSeries, memory);
          }
    
          if (memory > typeLimit.maxMemPerCore * coreCount && typeLimit.allowExtraMemory) {
            return String.format("zones/%s/machineTypes/%s-%d-%d-ext", zone, cpuSeries, coreCount,
                memory);
          }
    
          return String.format("zones/%s/machineTypes/%s-%d-%d", zone, cpuSeries, coreCount, memory);
        }
    
        public String shortString() {
          String cmt = this.toString();
          return cmt.substring(cmt.lastIndexOf("/") + 1);
        }
      }
    
      // This class defines the configurable parameters for a custom VM.
      static final class TypeLimits {
    
        int[] allowedCores;
        int minMemPerCore;
        int maxMemPerCore;
        int extraMemoryLimit;
        boolean allowExtraMemory;
    
        TypeLimits(int[] allowedCores, int minMemPerCore, int maxMemPerCore, boolean allowExtraMemory,
            int extraMemoryLimit) {
          this.allowedCores = allowedCores;
          this.minMemPerCore = minMemPerCore;
          this.maxMemPerCore = maxMemPerCore;
          this.allowExtraMemory = allowExtraMemory;
          this.extraMemoryLimit = extraMemoryLimit;
        }
      }
    
      public enum CpuSeries {
        N1("custom"),
        N2("n2-custom"),
        N2D("n2d-custom"),
        E2("e2-custom"),
        E2_MICRO("e2-custom-micro"),
        E2_SMALL("e2-custom-small"),
        E2_MEDIUM("e2-custom-medium");
    
        private static final Map<String, CpuSeries> ENUM_MAP;
    
        static {
          ENUM_MAP = init();
        }
    
        // Build an immutable map of String name to enum pairs.
        public static Map<String, CpuSeries> init() {
          Map<String, CpuSeries> map = new ConcurrentHashMap<>();
          for (CpuSeries instance : CpuSeries.values()) {
            map.put(instance.name().toLowerCase(), instance);
          }
          return Collections.unmodifiableMap(map);
        }
    
        private final String cpuSeries;
    
        CpuSeries(String cpuSeries) {
          this.cpuSeries = cpuSeries;
        }
    
        public static CpuSeries get(String name) {
          return ENUM_MAP.get(name.toLowerCase());
        }
    
        public String getCpuSeries() {
          return this.cpuSeries;
        }
      }
    
      // This enum correlates a machine type with its limits.
      // The limits for various CPU types are described in:
      // https://cloud.google.com/compute/docs/general-purpose-machines
      enum Limits {
        CPUSeries_E2(new TypeLimits(getNumsInRangeWithStep(2, 33, 2), 512, 8192, false, 0)),
        CPUSeries_E2MICRO(new TypeLimits(new int[]{}, 1024, 2048, false, 0)),
        CPUSeries_E2SMALL(new TypeLimits(new int[]{}, 2048, 4096, false, 0)),
        CPUSeries_E2MEDIUM(new TypeLimits(new int[]{}, 4096, 8192, false, 0)),
        CPUSeries_N2(
            new TypeLimits(concat(getNumsInRangeWithStep(2, 33, 2), getNumsInRangeWithStep(36, 129, 4)),
                512, 8192, true, gbToMb(624))),
        CPUSeries_N2D(
            new TypeLimits(new int[]{2, 4, 8, 16, 32, 48, 64, 80, 96}, 512, 8192, true, gbToMb(768))),
        CPUSeries_N1(
            new TypeLimits(concat(new int[]{1}, getNumsInRangeWithStep(2, 97, 2)), 922, 6656, true,
                gbToMb(624)));
    
        private final TypeLimits typeLimits;
    
        Limits(TypeLimits typeLimits) {
          this.typeLimits = typeLimits;
        }
    
        public TypeLimits getTypeLimits() {
          return typeLimits;
        }
      }
    
      // Returns the array of integers within the given range, incremented by the specified step.
      // start (inclusive): starting number of the range
      // stop (inclusive): ending number of the range
      // step : increment value
      static int[] getNumsInRangeWithStep(int start, int stop, int step) {
        return IntStream.range(start, stop).filter(x -> (x - start) % step == 0).toArray();
      }
    
      static int gbToMb(int value) {
        return value << 10;
      }
    
      static int[] concat(int[] a, int[] b) {
        int[] result = new int[a.length + b.length];
        System.arraycopy(a, 0, result, 0, a.length);
        System.arraycopy(b, 0, result, a.length, b.length);
        return result;
      }
    
      // Return the custom machine type in the form of a string acceptable by Compute Engine API.
      public static String returnCustomMachineTypeString(CustomMachineType cmt) {
        // Check if the requested CPU belongs to E2 series.
        if (Arrays.asList(CpuSeries.E2_SMALL.name(), CpuSeries.E2_MICRO.name(),
            CpuSeries.E2_MEDIUM.name()).contains(cmt.cpuSeries)) {
          return String.format("zones/%s/machineTypes/%s-%s", cmt.zone, cmt.cpuSeries, cmt.memory);
        }
    
        // Check if extended memory was requested.
        if (cmt.memory > cmt.coreCount * cmt.typeLimit.maxMemPerCore) {
          return String.format("zones/%s/machineTypes/%s-%s-%s-ext", cmt.zone, cmt.cpuSeries,
              cmt.coreCount,
              cmt.memory);
        }
    
        return String.format("zones/%s/machineTypes/%s-%s-%s", cmt.zone, cmt.cpuSeries, cmt.coreCount,
            cmt.memory);
      }
    
      // Returns machine type in a format without the zone. For example, n2-custom-0-10240.
      // This format is used to create instance templates.
      public static String machineType(CustomMachineType cmt) {
        String[] machineType = returnCustomMachineTypeString(cmt).split("/");
        return machineType[machineType.length - 1];
      }
    
      // Validate whether the requested parameters are allowed.
      // Find more information about limitations of custom machine types at:
      // https://cloud.google.com/compute/docs/general-purpose-machines#custom_machine_types
      public static String validate(CustomMachineType cmt) {
    
        // Check the number of cores and if the coreCount is present in allowedCores.
        if (cmt.typeLimit.allowedCores.length > 0 && Arrays.stream(cmt.typeLimit.allowedCores)
            .noneMatch(x -> x == cmt.coreCount)) {
          throw new Error(String.format(
              "Invalid number of cores requested. Allowed number of cores for %s is: %s",
              cmt.cpuSeries,
              Arrays.toString(cmt.typeLimit.allowedCores)));
        }
    
        // Memory must be a multiple of 256 MB.
        if (cmt.memory % 256 != 0) {
          throw new Error("Requested memory must be a multiple of 256 MB");
        }
    
        // Check if the requested memory isn't too little.
        if (cmt.memory < cmt.coreCount * cmt.typeLimit.minMemPerCore) {
          throw new Error(
              String.format("Requested memory is too low. Minimum memory for %s is %s MB per core",
                  cmt.cpuSeries, cmt.typeLimit.minMemPerCore));
        }
    
        // Check if the requested memory isn't too much.
        if (cmt.memory > cmt.coreCount * cmt.typeLimit.maxMemPerCore
            && !cmt.typeLimit.allowExtraMemory) {
          throw new Error(String.format(
              "Requested memory is too large.. Maximum memory allowed for %s is %s MB per core",
              cmt.cpuSeries, cmt.typeLimit.extraMemoryLimit));
        }
    
        // Check if the requested memory isn't too large.
        if (cmt.memory > cmt.typeLimit.extraMemoryLimit && cmt.typeLimit.allowExtraMemory) {
          throw new Error(
              String.format("Requested memory is too large.. Maximum memory allowed for %s is %s MB",
                  cmt.cpuSeries, cmt.typeLimit.extraMemoryLimit));
        }
    
        return null;
      }
    
      // Create a custom machine type.
      public static CustomMachineType createCustomMachineType(String zone, String cpuSeries, int memory,
          int coreCount, TypeLimits typeLimit) {
        if (Arrays.asList(CpuSeries.E2_SMALL.getCpuSeries(), CpuSeries.E2_MICRO.getCpuSeries(),
            CpuSeries.E2_MEDIUM.getCpuSeries()).contains(cpuSeries)) {
          coreCount = 2;
        }
    
        CustomMachineType cmt = new CustomMachineType(zone, cpuSeries, memory, coreCount, typeLimit);
    
        try {
          validate(cmt);
        } catch (Error e) {
          // Error in validation.
          System.out.printf("Error in validation: %s", e);
          return null;
        }
        return cmt;
      }
    
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment and replace these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const zone = 'europe-central2-b';
    // const cpuSeries = 'N1';
    // const coreCount = 2
    // const memory = 256
    
    function range(from, to, step) {
      return [...Array(Math.floor((to - from) / step) + 1)].map(
        (_, i) => from + i * step
      );
    }
    
    class CustomMachineType {
      constructor(zone, cpuSeries, coreCount, memory) {
        this.zone = zone;
        this.cpuSeries = cpuSeries;
        this.coreCount = coreCount;
        this.memory = memory;
    
        this.N1 = 'custom';
        this.N2 = 'n2-custom';
        this.N2D = 'n2d-custom';
        this.E2 = 'e2-custom';
        this.E2Micro = 'e2-custom-micro';
        this.E2Small = 'e2-custom-small';
        this.E2Medium = 'e2-custom-medium';
    
        this.CpuSeriesE2Limit = {
          allowedCores: range(2, 33, 2),
          minMemPerCore: 512,
          maxMemPerCore: 8192,
          allowExtraMemory: false,
          extraMemoryLimit: 0,
        };
    
        this.CpuSeriesE2MicroLimit = {
          allowedCores: [],
          minMemPerCore: 1024,
          maxMemPerCore: 2048,
          allowExtraMemory: false,
          extraMemoryLimit: 0,
        };
    
        this.CpuSeriesE2SmallLimit = {
          allowedCores: [],
          minMemPerCore: 2048,
          maxMemPerCore: 4096,
          allowExtraMemory: false,
          extraMemoryLimit: 0,
        };
    
        this.CpuSeriesE2MediumLimit = {
          allowedCores: [],
          minMemPerCore: 4096,
          maxMemPerCore: 8192,
          allowExtraMemory: false,
          extraMemoryLimit: 0,
        };
    
        this.CpuSeriesN2Limit = {
          allowedCores: [...range(2, 33, 2), ...range(36, 129, 4)],
          minMemPerCore: 512,
          maxMemPerCore: 8192,
          allowExtraMemory: true,
          extraMemoryLimit: 624 << 10,
        };
    
        this.CpuSeriesN2DLimit = {
          allowedCores: [2, 4, 8, 16, 32, 48, 64, 80, 96],
          minMemPerCore: 512,
          maxMemPerCore: 8192,
          allowExtraMemory: true,
          extraMemoryLimit: 768 << 10,
        };
    
        this.CpuSeriesN1Limit = {
          allowedCores: [1, range(2, 97, 2)],
          minMemPerCore: 922,
          maxMemPerCore: 6656,
          allowExtraMemory: true,
          extraMemoryLimit: 624 << 10,
        };
    
        this.TYPE_LIMITS = {
          [this.N1]: this.CpuSeriesN1Limit,
          [this.N2]: this.CpuSeriesN2Limit,
          [this.N2D]: this.CpuSeriesN2DLimit,
          [this.E2]: this.CpuSeriesE2Limit,
          [this.E2Micro]: this.CpuSeriesE2MicroLimit,
          [this.E2Small]: this.CpuSeriesE2SmallLimit,
          [this.E2Medium]: this.CpuSeriesE2MediumLimit,
        };
    
        this.typeLimit = this.TYPE_LIMITS[this.cpuSeries];
      }
    
      validate() {
        // Check the number of cores
        if (
          this.typeLimit.allowedCores.length > 0 &&
          !this.typeLimit.allowedCores.includes(this.coreCount)
        ) {
          throw new Error(
            `Invalid number of cores requested. Allowed number of cores for ${this.cpuSeries} is: ${this.typeLimit.allowedCores}`
          );
        }
    
        // Memory must be a multiple of 256 MB
        if (this.memory % 256 !== 0) {
          throw new Error('Requested memory must be a multiple of 256 MB');
        }
    
        // Check if the requested memory isn't too little
        if (this.memory < this.coreCount * this.typeLimit.minMemPerCore) {
          throw new Error(
            `Requested memory is too low. Minimal memory for ${this.cpuSeries} is ${this.typeLimit.minMemPerCore} MB per core`
          );
        }
    
        // Check if the requested memory isn't too much
        if (
          this.memory > this.coreCount * this.typeLimit.maxMemPerCore &&
          !this.typeLimit.allowExtraMemory
        ) {
          throw new Error(
            `Requested memory is too large.. Maximum memory allowed for ${this.cpuSeries} is ${this.typeLimit.maxMemPerCore} MB per core`
          );
        }
    
        if (
          this.memory > this.typeLimit.extraMemoryLimit &&
          this.typeLimit.allowExtraMemory
        ) {
          throw new Error(
            `Requested memory is too large.. Maximum memory allowed for ${this.cpuSeries} is ${this.typeLimit.extraMemoryLimit} MB`
          );
        }
      }
    
      // Returns the custom machine type in form of a string acceptable by Compute Engine API.
      getMachineTypeURI() {
        if (
          [this.E2Small, this.E2Micro, this.E2Medium].includes(this.cpuSeries)
        ) {
          return `zones/${this.zone}/machineTypes/${this.cpuSeries}-${this.memory}`;
        }
    
        if (this.memory > this.coreCount * this.typeLimit.maxMemPerCore) {
          return `zones/${this.zone}/machineTypes/${this.cpuSeries}-${coreCount}-${this.memory}-ext`;
        }
    
        return `zones/${zone}/machineTypes/${this.cpuSeries}-${this.coreCount}-${this.memory}`;
      }
    
      // Returns machine type in a format without the zone. For example, n2-custom-0-10240.
      // This format is used to create instance templates.
      getMachineType() {
        return this.getMachineTypeURI().split('/').pop();
      }
    }
    
    async function createCustomMachineType() {
      if (
        [
          CustomMachineType.E2Small,
          CustomMachineType.E2Micro,
          CustomMachineType.E2Medium,
        ].includes(cpuSeries)
      ) {
        coreCount = 2;
      }
    
      const machineType = new CustomMachineType(
        zone,
        cpuSeries,
        coreCount,
        memory
      );
    
      console.log(`URI: ${machineType.getMachineTypeURI()}`);
      console.log(`MachineType: ${machineType.getMachineType()}`);
    }
    
    createCustomMachineType();

### Python

Before trying this sample, follow the Python setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from collections import namedtuple
    from enum import Enum
    from enum import unique
    
    
    def gb_to_mb(value: int) -> int:
        return value << 10
    
    
    class CustomMachineType:
        """
        Allows to create custom machine types to be used with the VM instances.
        """
    
        @unique
        class CPUSeries(Enum):
            N1 = "custom"
            N2 = "n2-custom"
            N2D = "n2d-custom"
            E2 = "e2-custom"
            E2_MICRO = "e2-custom-micro"
            E2_SMALL = "e2-custom-small"
            E2_MEDIUM = "e2-custom-medium"
    
        TypeLimits = namedtuple(
            "TypeLimits",
            [
                "allowed_cores",
                "min_mem_per_core",
                "max_mem_per_core",
                "allow_extra_memory",
                "extra_memory_limit",
            ],
        )
    
        # The limits for various CPU types are described on:
        # https://cloud.google.com/compute/docs/general-purpose-machines
        LIMITS = {
            CPUSeries.E2: TypeLimits(frozenset(range(2, 33, 2)), 512, 8192, False, 0),
            CPUSeries.E2_MICRO: TypeLimits(frozenset(), 1024, 2048, False, 0),
            CPUSeries.E2_SMALL: TypeLimits(frozenset(), 2048, 4096, False, 0),
            CPUSeries.E2_MEDIUM: TypeLimits(frozenset(), 4096, 8192, False, 0),
            CPUSeries.N2: TypeLimits(
                frozenset(range(2, 33, 2)).union(set(range(36, 129, 4))),
                512,
                8192,
                True,
                gb_to_mb(624),
            ),
            CPUSeries.N2D: TypeLimits(
                frozenset({2, 4, 8, 16, 32, 48, 64, 80, 96}), 512, 8192, True, gb_to_mb(768)
            ),
            CPUSeries.N1: TypeLimits(
                frozenset({1}.union(range(2, 97, 2))), 922, 6656, True, gb_to_mb(624)
            ),
        }
    
        def __init__(
            self, zone: str, cpu_series: CPUSeries, memory_mb: int, core_count: int = 0
        ):
            self.zone = zone
            self.cpu_series = cpu_series
            self.limits = self.LIMITS[self.cpu_series]
            # Shared machine types (e2-small, e2-medium and e2-micro) always have
            # 2 vCPUs: https://cloud.google.com/compute/docs/general-purpose-machines#e2_limitations
            self.core_count = 2 if self.is_shared() else core_count
            self.memory_mb = memory_mb
            self._checked = False
            self._check_parameters()
            self.extra_memory_used = self._check_extra_memory()
    
        def is_shared(self):
            return self.cpu_series in (
                CustomMachineType.CPUSeries.E2_SMALL,
                CustomMachineType.CPUSeries.E2_MICRO,
                CustomMachineType.CPUSeries.E2_MEDIUM,
            )
    
        def _check_extra_memory(self) -> bool:
            if self._checked:
                return self.memory_mb > self.core_count * self.limits.max_mem_per_core
            else:
                raise RuntimeError(
                    "You need to call _check_parameters() before calling _check_extra_memory()"
                )
    
        def _check_parameters(self):
            """
            Check whether the requested parameters are allowed. Find more information about limitations of custom machine
            types at: https://cloud.google.com/compute/docs/general-purpose-machines#custom_machine_types
            """
            # Check the number of cores
            if (
                self.limits.allowed_cores
                and self.core_count not in self.limits.allowed_cores
            ):
                raise RuntimeError(
                    f"Invalid number of cores requested. Allowed number of cores for {self.cpu_series.name} is: {sorted(self.limits.allowed_cores)}"
                )
    
            # Memory must be a multiple of 256 MB
            if self.memory_mb % 256 != 0:
                raise RuntimeError("Requested memory must be a multiple of 256 MB.")
    
            # Check if the requested memory isn't too little
            if self.memory_mb < self.core_count * self.limits.min_mem_per_core:
                raise RuntimeError(
                    f"Requested memory is too low. Minimal memory for {self.cpu_series.name} is {self.limits.min_mem_per_core} MB per core."
                )
    
            # Check if the requested memory isn't too much
            if self.memory_mb > self.core_count * self.limits.max_mem_per_core:
                if self.limits.allow_extra_memory:
                    if self.memory_mb > self.limits.extra_memory_limit:
                        raise RuntimeError(
                            f"Requested memory is too large.. Maximum memory allowed for {self.cpu_series.name} is {self.limits.extra_memory_limit} MB."
                        )
                else:
                    raise RuntimeError(
                        f"Requested memory is too large.. Maximum memory allowed for {self.cpu_series.name} is {self.limits.max_mem_per_core} MB per core."
                    )
    
            self._checked = True
    
        def __str__(self) -> str:
            """
            Return the custom machine type in form of a string acceptable by Compute Engine API.
            """
            if self.cpu_series in {
                self.CPUSeries.E2_SMALL,
                self.CPUSeries.E2_MICRO,
                self.CPUSeries.E2_MEDIUM,
            }:
                return f"zones/{self.zone}/machineTypes/{self.cpu_series.value}-{self.memory_mb}"
    
            if self.extra_memory_used:
                return f"zones/{self.zone}/machineTypes/{self.cpu_series.value}-{self.core_count}-{self.memory_mb}-ext"
    
            return f"zones/{self.zone}/machineTypes/{self.cpu_series.value}-{self.core_count}-{self.memory_mb}"
    
        def short_type_str(self) -> str:
            """
            Return machine type in a format without the zone. For example, n2-custom-0-10240.
            This format is used to create instance templates.
            """
            return str(self).rsplit("/", maxsplit=1)[1]
    
        @classmethod
        def from_str(cls, machine_type: str):
            """
            Construct a new object from a string. The string needs to be a valid custom machine type like:
             - https://www.googleapis.com/compute/v1/projects/diregapic-mestiv/zones/us-central1-b/machineTypes/e2-custom-4-8192
             - zones/us-central1-b/machineTypes/e2-custom-4-8192
             - e2-custom-4-8192 (in this case, the zone parameter will not be set)
            """
            zone = None
            if machine_type.startswith("http"):
                machine_type = machine_type[machine_type.find("zones/") :]
    
            if machine_type.startswith("zones/"):
                _, zone, _, machine_type = machine_type.split("/")
    
            extra_mem = machine_type.endswith("-ext")
    
            if machine_type.startswith("custom"):
                cpu = cls.CPUSeries.N1
                _, cores, memory = machine_type.rsplit("-", maxsplit=2)
            else:
                if extra_mem:
                    cpu_series, _, cores, memory, _ = machine_type.split("-")
                else:
                    cpu_series, _, cores, memory = machine_type.split("-")
                if cpu_series == "n2":
                    cpu = cls.CPUSeries.N2
                elif cpu_series == "n2d":
                    cpu = cls.CPUSeries.N2D
                elif cpu_series == "e2":
                    cpu = cls.CPUSeries.E2
                    if cores == "micro":
                        cpu = cls.CPUSeries.E2_MICRO
                        cores = 2
                    elif cores == "small":
                        cpu = cls.CPUSeries.E2_SMALL
                        cores = 2
                    elif cores == "medium":
                        cpu = cls.CPUSeries.E2_MEDIUM
                        cores = 2
                else:
                    raise RuntimeError("Unknown CPU series.")
    
            cores = int(cores)
            memory = int(memory)
    
            return cls(zone, cpu, memory, cores)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
