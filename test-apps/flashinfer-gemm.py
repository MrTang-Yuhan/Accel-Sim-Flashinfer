import torch
from flashinfer import SegmentGEMMWrapper
# create a 1MB workspace buffer
workspace_buffer = torch.empty(1 * 2 * 1, dtype=torch.int8, device="cuda")
segment_gemm = SegmentGEMMWrapper(workspace_buffer)
seq_lens = torch.tensor([1, 2, 3, 4], dtype=torch.int64, device="cuda")
# create packed input tensor (10 = 1 + 2 + 3 + 4)
x = torch.randn(10, 1, device="cuda", dtype=torch.float16)
# create weight tensor with 4 weights, each with 128 input and 256 output channels, column major
weights = torch.randn(4, 1, 1, device="cuda", dtype=torch.float16)
# compute the segment GEMM
y = segment_gemm.run(x, weights, 4, True, seg_lens=seq_lens)
# print(y)
# print(f"y_shape:{y.shape}")

