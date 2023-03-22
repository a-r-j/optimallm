# optimallm

Optimise python functions with LLMs

## Installation

```bash
pip install optimallm
```

### Example Usage

```python
import os
from optimallm import opt

os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY"

def calculate_sum(a, b):
    result = a
    for i in range(b):
        result += 1
    return result

opt(calculate_sum)
```

Output:
> Here's an optimized version of the calculate_sum function:
>
> ```python
> def calculate_sum(a, b):
>    return a + b
>  ```
>
>This optimized version simply adds a and b together and returns the result. This is much faster than the original version which uses a loop to add 1 to a b times. Additionally, this version is more readable and concise.

### Custom prompts

Code is injected into the prompt by replacing `$code`. Similarly, the function name can be injected by replacing `$name`.

```python
prompt = "Make this function go brrr: \n $code"
opt(calculate_sum, prompt)

prompt = "Make $name go brrr: \n $code"
opt(calculate_sum, prompt)

```

#### Setting a new default

```python
import optimallm

optimallm.DEFAULT_PROMPT = "Make code go brrrr: \n $code"
optimallm.opt(my_bad_function)
```

### API Key

API Keys can be set in two ways:

1. As an env var:

```python
import os
os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY"
```

2. Using OpenAI's library

```python
import openai
openai.api_key = "YOUR_API_KEY"
```
