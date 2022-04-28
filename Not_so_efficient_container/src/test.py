# %%
from __future__ import print_function
import torch
# %%
x = torch.rand(5, 3)
print(x)

print("=============>")
print("Is cuda enable? {0}".format(torch.cuda.is_available()))
print(torch.cuda.current_device())
# Check the cuda in docker
print(torch.version.cuda)
print(torch.backends.cudnn.enabled)
# %%
