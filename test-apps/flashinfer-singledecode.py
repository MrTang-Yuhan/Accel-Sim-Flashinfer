import torch
import flashinfer

#device_name = torch.cuda.get_device_name(0)
#print(f"CUDA device 0 name: {device_name}")

kv_len = 128
num_qo_heads = 32
num_kv_heads = 32
head_dim = 128
q = torch.randn(num_qo_heads, head_dim).half().to("cuda:0")
k = torch.randn(kv_len, num_kv_heads, head_dim).half().to("cuda:0")
v = torch.randn(kv_len, num_kv_heads, head_dim).half().to("cuda:0")
o = flashinfer.single_decode_with_kv_cache(q, k, v)
