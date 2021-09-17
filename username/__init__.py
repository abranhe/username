"""
Get the username of the current user.

Example:

```python
import username

username()
# 'abranhe'
```

Read more on the [documentation](https://github.com/abranhe/username)
"""

import sys
import os
import getpass


class Username():
    user = os.environ['SUDO_USER'] if 'SUDO_USER' in os.environ else getpass.getuser()

    def __call__(self):
        return self.user


sys.modules[__name__] = Username()
