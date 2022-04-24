#include <string>
std::string reverseString (std::string str ){
    std::string rvsdStr;
    int add = 0;
    for(int i = str.length(); i > 0; i--){
        rvsdStr[add] = str[i];
    }
    return rvsdStr;
}
int main(){
    std::string meep = reverseString("Hello");
    return 0;
}