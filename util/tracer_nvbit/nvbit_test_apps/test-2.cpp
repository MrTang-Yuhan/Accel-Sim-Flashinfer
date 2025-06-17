#include <iostream>
#include <pthread.h>
#include <unistd.h> // for sleep()

// 线程函数
void* threadFunction(void* arg) {
    std::cout << "Thread is running..." << std::endl;
    sleep(2); // 模拟线程工作
    std::cout << "Thread is exiting..." << std::endl;
    return nullptr; // 返回值
}

int main() {
    pthread_t thread;
    void* status = nullptr; // 用于接收线程的返回值

    // 创建线程
    if(pthread_create(&thread, nullptr, (void*(*)(void*))threadFunction, nullptr) != 0) {
        std::cerr << "Error creating thread" << std::endl;
        return 1;
    }

    // 等待线程结束
    if(pthread_join(thread, &status) != 0) {
        std::cerr << "Error joining thread" << std::endl;
        return 1;
    }

    std::cout << "Thread finished" << std::endl;
    return 0;
}