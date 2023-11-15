# common_tools
House common methods, functions, designs and other tools that I use commonly within Python.

## Pip Install Setup
Run the following commands in your local environment to use the package.
- ```pip install git+https://github.com/enisbukalo/common_tools.git```

## Local Setup (Cloning)
Run the following commands in your local environment to test.
- ```python setup.py sdist bdist_wheel clean --all develop```
- ```pip install dist/common_tools-0.1.0-py3-none-any.whl --force-reinstall --no-cache-dir```
---

## Usage
After installing it either locally or via PIP from the github repo, the packages should become available.<br>
IE: ```from class_common import Singleton```

---
## Components
### [Classes](https://github.com/enisbukalo/common_tools/tree/main/class_common)
- [Class Tools](https://github.com/enisbukalo/common_tools/blob/main/class_common/class_tools.py)
---
### [Design](https://github.com/enisbukalo/common_tools/tree/main/design_common)
#### [State Machines](https://github.com/enisbukalo/common_tools/tree/main/design_common/state_machines)
- [Finite State Machine (FSM)](https://github.com/enisbukalo/common_tools/tree/main/design_common/state_machines/FSM)
#### [Queue's](https://github.com/enisbukalo/common_tools/tree/main/design_common/queues)
- [First In First Out (FIFO)](https://github.com/enisbukalo/common_tools/tree/main/design_common/queues/fifo)
- [Last In First Out (LIFO)](https://github.com/enisbukalo/common_tools/tree/main/design_common/queues/lifo)
- [Priority Queue](https://github.com/enisbukalo/common_tools/tree/main/queues/state_machines/priority)
---
### [Logging](https://github.com/enisbukalo/common_tools/tree/main/logging_common)
- [General Logger](https://github.com/enisbukalo/common_tools/blob/main/logging_common/logger.py)
---
### [Network](https://github.com/enisbukalo/common_tools/tree/main/network_common)
- [Network Tools](https://github.com/enisbukalo/common_tools/blob/main/network_common/network_tools.py)
---
### [Statistics](https://github.com/enisbukalo/common_tools/tree/main/statistics_common)
- [Statistics Tools](https://github.com/enisbukalo/common_tools/blob/main/statistics_common/statistics_tools.py)
---
### [Utilities](https://github.com/enisbukalo/common_tools/tree/main/utilities)
#### [Sorting](https://github.com/enisbukalo/common_tools/tree/main/utilities/sorting)
- [Merge Sort](https://github.com/enisbukalo/common_tools/blob/main/utilities/sorting/merge_sort.py)
---
### [Tests](https://github.com/enisbukalo/common_tools/tree/main/tests)
- [Class Tools Tests](https://github.com/enisbukalo/common_tools/tree/main/tests/test_classes)
- [FSM Tests](https://github.com/enisbukalo/common_tools/tree/main/tests/test_design/test_fsm)
- [Network Tools Tests](https://github.com/enisbukalo/common_tools/tree/main/tests/test_network)
- [Statistics Tools Tests](https://github.com/enisbukalo/common_tools/tree/main/tests/test_statistics)
- [Utilities Tests](https://github.com/enisbukalo/common_tools/tree/main/tests/test_utilities)
---