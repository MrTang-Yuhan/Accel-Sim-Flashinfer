#include <cuda_runtime.h>
#include <iostream>

#define WARPSIZE 32
// 内核函数，使用 __ballot_sync() 和 __activemask()
__global__ void kernel_example(int *g_results) {
    // 获取 warp 中的线程 ID
    int laneId = threadIdx.x % WARPSIZE;

    // 获取 warp 中活跃线程的掩码
    unsigned activeMask = __activemask();
    printf("laneId=%d, active_mask=%d\n", laneId, activeMask);

    // 每个线程设置一个值，如果其线程 ID 是偶数
    int value = (laneId % 2 == 0) ? 1 : 0;

    // 使用 __ballot_sync() 收集 warp 中所有线程的值
    int ballot = __ballot_sync(activeMask, value);

    // 计算 warp 中值为 1 的线程数量
    int count = __popc(ballot);

    // 只有 warp 中第一个线程会写结果到全局内存
    if (laneId == 0) {
        // 计算全局索引
        int idx = blockIdx.x * blockDim.x + threadIdx.x;
        // 保存结果
        g_results[idx] = count;
    }
}

// 主函数
int main() {
    // 定义和分配全局内存数组来存储结果
    int *g_results = nullptr;
    size_t size = 256; // 假设我们有 256 个线程
    cudaMalloc(&g_results, size * sizeof(int));

    // 定义每个块的线程数和块数
    int threadsPerBlock = 32;
    int blocksPerGrid = (size + threadsPerBlock - 1) / threadsPerBlock;

    // 调用内核函数
    kernel_example<<<blocksPerGrid, threadsPerBlock>>>(g_results);

    // 定义和分配主机内存数组来存储结果
    int *h_results = new int[size];

    // 从设备复制结果到主机
    cudaMemcpy(h_results, g_results, size * sizeof(int), cudaMemcpyDeviceToHost);

    // 打印结果
    // for (int i = 0; i < size; ++i) {
    //     std::cout << "Result[" << i << "] = " << h_results[i] << std::endl;
    // }

    // 释放内存
    cudaFree(g_results);
    delete[] h_results;

    return 0;
}