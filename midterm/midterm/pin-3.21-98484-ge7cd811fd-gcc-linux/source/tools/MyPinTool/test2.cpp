#include<iostream>
#include<pthread.h>
using namespace std;
void* test(void* args){
    cout<<"test"<<endl;
    return NULL;
}
int main(){
    pthread_t t1;
    pthread_t t2;
    pthread_create(&t1,NULL,test,NULL);
    pthread_create(&t2,NULL,test,NULL);
    pthread_join(t1,NULL);
    return 0;

}
