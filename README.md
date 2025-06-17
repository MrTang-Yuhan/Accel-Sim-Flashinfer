# 快速测试
## 1. 下载Accel-Sim
`git clone --branch v1.3.0 https://github.com/accel-sim/accel-sim-framework.git`

`cd accel-sim-framework`

`source ./gpu-simulator/setup_environment.sh`

`git clone https://github.com/accel-sim/gpu-app-collection`

`source ./gpu-app-collection/src/setup_environment`

`make -j -C ./gpu-simulator/`

## 2. 下载可用的配置文件
`cd accel-sim-framework`

`git clone https://github.com/MrTang-Yuhan/Accel-Sim-Flashinfer.git`

`cp -r Accel-Sim-Flashinfer/util ./`

`cp -r Accel-Sim-Flashinfer/gpu-simulator ./`

`cp -r Accel-Sim-Flashinfer/test-apps/ ./`

`cp -r Accel-Sim-Flashinfer/test-traces/ ./`

`cp -r Accel-Sim-Flashinfer/tested-cfgs/* ./gpu-simulator/gpgpu-sim/configs/tested-cfgs/`

`rm -r Accel-Sim-Flashinfer`


## 3. 测试能否运行程序
`cd accel-sim-framework`

`source ./gpu-simulator/setup_environment.sh`

`make -j -C ./gpu-simulator/`

`./gpu-simulator/bin/release/accel-sim.out -trace ./test-traces/flashinfer-singledecode/traces/kernelslist.g -config ./gpu-simulator/gpgpu-sim/configs/tested-cfgs/A100/gpgpusim.config -config ./gpu-simulator/configs/tested-cfgs/A100/trace.config > result-singledecode.log`


搜索`result-singledecode.log`文件内的`gpu_tot_ipc`，结果应该为`gpu_tot_ipc`

## 4. 测试能否使用trace
`cd accel-sim-framework`

`./util/tracer_nvbit/install_nvbit.sh`

`make -C ./util/tracer_nvbit/`

`CUDA_INJECTION64_PATH=./util/tracer_nvbit/tracer_tool/tracer_tool.so LD_PRELOAD=./util/tracer_nvbit/tracer_tool/tracer_tool.so python3 test-apps/flashinfer-singledecode.py` 

`./util/tracer_nvbit/tracer_tool/traces-processing/post-traces-processing ./traces/kernelslist`

`rm ./traces/kernel*.trace.xz`

`rm ./traces/kernelslist`

更换traces为刚刚生成的`./traces/kernelslist.g`
`./gpu-simulator/bin/release/accel-sim.out -trace ./traces/kernelslist.g -config ./gpu-simulator/gpgpu-sim/configs/tested-cfgs/A100/gpgpusim.config -config ./gpu-simulator/configs/tested-cfgs/A100/trace.config > result-singledecode.log`