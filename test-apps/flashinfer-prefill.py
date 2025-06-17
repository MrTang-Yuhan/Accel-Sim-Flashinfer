import torch
import flashinfer
qo_len = 64
kv_len = 64
num_qo_heads = 8
num_kv_heads = 4
head_dim = 64
q = torch.randn(qo_len, num_qo_heads, head_dim).half().to("cuda:0")
k = torch.randn(kv_len, num_kv_heads, head_dim).half().to("cuda:0")
v = torch.randn(kv_len, num_kv_heads, head_dim).half().to("cuda:0")
o = flashinfer.single_prefill_with_kv_cache(q, k, v, causal=True,
        use_fp16_qk_reduction=True)
#print(o.shape)

#import torch
#import flashinfer
#qo_len = 128
#kv_len = 128
#num_qo_heads = 32
#num_kv_heads = 4
#head_dim = 128
#q = torch.randn(qo_len, num_qo_heads, head_dim).half().to("cuda:0")
#k = torch.randn(kv_len, num_kv_heads, head_dim).half().to("cuda:0")
#v = torch.randn(kv_len, num_kv_heads, head_dim).half().to("cuda:0")
#o = flashinfer.single_prefill_with_kv_cache(q, k, v, causal=True,
#        use_fp16_qk_reduction=True)
#print(o.shape)
#mask = torch.tril(
#    torch.full((qo_len, kv_len), True, device="cuda:0"),
#            diagonal=(kv_len - qo_len),
#                    )
#mask
#o_custom = flashinfer.single_prefill_with_kv_cache(q, k, v, custom_mask=mask)
#torch.allclose(o, o_custom, rtol=1e-3, atol=1e-3)
