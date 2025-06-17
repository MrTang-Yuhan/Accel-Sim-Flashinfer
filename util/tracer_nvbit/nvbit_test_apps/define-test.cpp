#include <iostream>

#define CU_TOOLS_FOR_EACH_CUDA_API_FUNC()                                        \
    DEFINE_ENUM_CBID_API_CUDA( cuda,          1,   cuInit,                                        0)        \
    DEFINE_ENUM_CBID_API_CUDA( cuda,          2,   cuDriverGetVersion,                            0)        \

#define DEFINE_ENUM_CBID_API_CUDA(area, id, name, params) API_CUDA_##name,  

enum {
    API_CUDA_INVALID = 0,
    CU_TOOLS_FOR_EACH_CUDA_API_FUNC()
};



int main() 
{

	printf(API_CUDA_cuInit;
    API_CUDA_INVALID;
 
	return 0;
}
